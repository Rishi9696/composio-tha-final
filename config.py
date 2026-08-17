"""Environment, paths, atomic JSON helpers, and native OpenAI access."""
from __future__ import annotations

import json
import os
import threading
from functools import lru_cache
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

_ENV_ROOT = Path(__file__).resolve().parent
load_dotenv(_ENV_ROOT / ".env")
load_dotenv(_ENV_ROOT / ".env.providers", override=True)

# Actual model used by the latest llm_json() call on this thread. The batch
# runner is concurrent, so this cannot be process-global.
_last_llm = threading.local()


def last_llm_used() -> str:
    return getattr(_last_llm, "value", "")

# --------------------------------------------------------------------------- #
# Paths
# --------------------------------------------------------------------------- #
ROOT = _ENV_ROOT
DATA_DIR = ROOT / "data"
OUT_DIR = ROOT / "out"
REASONING_DIR = OUT_DIR / "reasoning"
CACHE_DIR = OUT_DIR / "cache"
REPORT_DIR = ROOT / "report"
HANDCHECK_DIR = ROOT / "handcheck"

APPS_PATH = DATA_DIR / "apps.json"
PRESEED_PATH = DATA_DIR / "preseed.json"
RESULTS_PATH = OUT_DIR / "results.json"
METRICS_PATH = OUT_DIR / "metrics.json"
FAILURES_PATH = OUT_DIR / "failures.log"
FAILURE_STATE_PATH = OUT_DIR / "failures.json"
USAGE_PATH = OUT_DIR / "usage.json"
BATCH_STATE_PATH = OUT_DIR / "batch_state.json"
BROWSER_EVIDENCE_PATH = OUT_DIR / "browser_evidence.json"
COMPOSIO_COVERAGE_PATH = OUT_DIR / "composio_coverage.json"
HANDCHECK_PATH = HANDCHECK_DIR / "handcheck.json"


def ensure_dirs() -> None:
    for d in (OUT_DIR, REASONING_DIR, CACHE_DIR, HANDCHECK_DIR):
        d.mkdir(parents=True, exist_ok=True)


# --------------------------------------------------------------------------- #
# Small JSON helpers (used across modules)
# --------------------------------------------------------------------------- #
def load_json(path: Path, default: Any = None) -> Any:
    if not Path(path).exists():
        return default
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def save_json(path: Path, data: Any) -> None:
    """Atomically replace a JSON artifact so interrupted batches cannot truncate it."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(
        f".{path.name}.{os.getpid()}.{threading.get_ident()}.tmp"
    )
    try:
        with open(temporary, "w", encoding="utf-8") as fh:
            json.dump(data, fh, indent=2, ensure_ascii=False)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


# --------------------------------------------------------------------------- #
# LLM - one native provider (OpenAI), intentionally no gateway fallback
# --------------------------------------------------------------------------- #
COMPOSIO_API_KEY = os.getenv("COMPOSIO_API_KEY", "")
LLM_TIMEOUT_SECONDS = float(os.getenv("LLM_TIMEOUT_SECONDS", "180"))
OPENAI_MAX_WORKERS = int(os.getenv("OPENAI_MAX_WORKERS", "2"))
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
PRIMARY_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1")
# Model used by the OpenAI web-search step in docs_research.py. A lighter model
# is enough for query-and-cite discovery; synthesis uses PRIMARY_MODEL.
SEARCH_MODEL = os.getenv("OPENAI_SEARCH_MODEL", "gpt-4.1-mini")
OPENAI_TOKEN_PRICES = {
    # USD per 1M (input, output) tokens.
    "gpt-4.1": (2.0, 8.0),
    "gpt-4.1-mini": (0.4, 1.6),
    "gpt-4.1-nano": (0.1, 0.4),
    "gpt-4o": (2.5, 10.0),
    "gpt-4o-mini": (0.15, 0.6),
}


def _openai_token_prices(model: str) -> tuple[float, float]:
    """USD per 1M input/output tokens; unknown models use the conservative 4.1 rate."""
    for known, prices in OPENAI_TOKEN_PRICES.items():
        if model == known or model.startswith(known + "-"):
            return prices
    return OPENAI_TOKEN_PRICES["gpt-4.1"]


@lru_cache(maxsize=1)
def get_client():
    """Return the native OpenAI SDK client."""
    if not OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY is not set")
    from openai import OpenAI

    return OpenAI(
        api_key=OPENAI_API_KEY,
        timeout=LLM_TIMEOUT_SECONDS,
        max_retries=1,
    )


def _extract_json_object(text: str) -> dict:
    """Best-effort parse of a JSON object from an LLM response.

    Handles raw JSON, ```json fenced blocks, and stray prose around the object.
    """
    text = (text or "").strip()
    if text.startswith("```"):
        body = text.split("\n", 1)[1] if "\n" in text else text
        if body.rstrip().endswith("```"):
            body = body.rstrip()[:-3]
        text = body.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start, end = text.find("{"), text.rfind("}")
        if start != -1 and end != -1 and end > start:
            return json.loads(text[start:end + 1])
        raise


class StructuredOutputError(ValueError):
    """The provider answered, but not with a complete JSON object."""


class ProviderQuotaExhausted(RuntimeError):
    """A provider's long-lived project quota is exhausted; pause the batch."""


class ProviderCapacityUnavailable(RuntimeError):
    """Repeated provider capacity failures make continuing the batch wasteful."""


def _classify_error(exc) -> str:
    code = getattr(exc, "status_code", None) or getattr(exc, "code", None)
    try:
        code = int(code)
    except (TypeError, ValueError):
        return "other"
    message = str(exc).lower()
    if code == 429 and any(
        marker in message
        for marker in ("insufficient_quota", "exceeded your current quota", "billing")
    ):
        return "quota"
    return "retry" if code in {408, 409, 429} or code >= 500 else "other"


def is_capacity_error(exc) -> bool:
    """Return true for provider-wide high-demand failures after local retries."""
    code = getattr(exc, "status_code", None) or getattr(exc, "code", None)
    try:
        code = int(code)
    except (TypeError, ValueError):
        return False
    message = str(exc).lower()
    return code in {503, 529} and any(
        marker in message for marker in ("overloaded", "capacity", "unavailable", "high demand")
    )


def llm_json(
    messages: list[dict],
    model: str | None = None,
    temperature: float = 0.0,
    max_tokens: int = 2000,
    thinking_level: str | None = None,  # accepted for call-site compatibility; unused
    response_schema: Any | None = None,
) -> tuple[dict, str]:
    """Call OpenAI Chat Completions and return a parsed strict JSON object.

    When ``response_schema`` is a Pydantic model, OpenAI structured outputs
    constrain the response to that schema; otherwise plain JSON mode is used.
    Deterministic validation downstream remains the final gate either way.
    """
    from tenacity import retry, retry_if_exception, stop_after_attempt, wait_exponential
    import usage_tracker

    selected_model = model or PRIMARY_MODEL
    input_price, output_price = _openai_token_prices(selected_model)
    input_estimate = sum(len(str(message.get("content", ""))) for message in messages) / 4
    conservative_cost = (
        input_estimate * input_price / 1_000_000
        + max_tokens * output_price / 1_000_000
    )
    usage_tracker.ensure_budget("openai", conservative_cost)

    use_schema = response_schema is not None and hasattr(response_schema, "model_json_schema")
    client = get_client()

    @retry(
        retry=retry_if_exception(lambda exc: _classify_error(exc) == "retry"),
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=3, max=30),
        reraise=True,
    )
    def _call():
        common = {
            "model": selected_model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }
        if use_schema:
            parse = getattr(client.chat.completions, "parse", None)
            if parse is None:
                parse = client.beta.chat.completions.parse
            return parse(response_format=response_schema, **common)
        return client.chat.completions.create(
            response_format={"type": "json_object"}, **common
        )

    try:
        response = _call()
    except Exception as exc:
        if _classify_error(exc) == "quota":
            raise ProviderQuotaExhausted(str(exc)) from exc
        raise

    message = response.choices[0].message if response.choices else None
    raw = (getattr(message, "content", None) or "") if message else ""
    usage = getattr(response, "usage", None)
    prompt_tokens = int(getattr(usage, "prompt_tokens", 0) or 0)
    completion_tokens = int(getattr(usage, "completion_tokens", 0) or 0)
    estimated_cost = (
        prompt_tokens * input_price / 1_000_000
        + completion_tokens * output_price / 1_000_000
    )
    usage_tracker.record("openai", "chat_completion", estimated_cost, {
        "model": selected_model,
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "input_usd_per_million": input_price,
        "output_usd_per_million": output_price,
        "finish_reason": str(getattr(response.choices[0], "finish_reason", "") or ""),
    })
    try:
        if message is not None and getattr(message, "refusal", None):
            raise ValueError(f"model refused: {message.refusal}")
        parsed = getattr(message, "parsed", None) if message else None
        if hasattr(parsed, "model_dump"):
            obj = parsed.model_dump(mode="json")
        elif isinstance(parsed, dict):
            obj = parsed
        else:
            if not raw.strip():
                raise ValueError("empty completion")
            obj = _extract_json_object(raw)
        if isinstance(obj, list):
            obj = next((item for item in obj if isinstance(item, dict)), None)
        if not isinstance(obj, dict):
            raise ValueError("model did not return a JSON object")
    except (json.JSONDecodeError, TypeError, ValueError) as exc:
        raise StructuredOutputError(
            f"incomplete JSON from openai:{selected_model}"
        ) from exc
    _last_llm.value = f"openai:{selected_model}"
    return obj, raw

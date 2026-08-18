"""Canonical auth labels and comparison helpers.

The dataset records credential *schemes*, not HTTP header syntax. For example,
an OAuth access token is recorded as ``OAuth2`` rather than also being counted
as ``Bearer Token``. ``Bearer Token`` is reserved for a static vendor-issued
token where no OAuth grant is involved.
"""
from __future__ import annotations

import re

CANONICAL = [
    "OAuth2",
    "API Key",
    "Bearer Token",
    "Basic Auth",
    "Personal Access Token",
    "Service Account",
    "Bot Token",
    "Other Token",
    "None / Not Applicable",
]

_CANONICAL_BY_KEY = {
    re.sub(r"[^a-z0-9]", "", label.lower()): label for label in CANONICAL
}


def normalize_auth(label: str, *, strict: bool = False) -> str | None:
    """Map one auth label to the controlled vocabulary.

    ``strict=True`` is used at model boundaries. It accepts common aliases but
    raises for an unknown non-empty value, preventing arbitrary model text from
    being silently relabeled as ``Other Token``.
    """
    if not label or not str(label).strip():
        return None
    raw = str(label).strip()
    low = raw.lower()
    compact = re.sub(r"[^a-z0-9]", "", low)

    if compact in _CANONICAL_BY_KEY:
        return _CANONICAL_BY_KEY[compact]
    if low in {"none", "n/a", "not applicable", "no authentication"}:
        return "None / Not Applicable"

    # Grant flows. A client-credentials grant is OAuth2; the resulting bearer
    # header is transport detail and must not become a second auth method.
    if (
        "oauth" in low
        or low.startswith("lwa")
        or "login with amazon" in low
        or "sign in with" in low
        or "ims access" in low
        or "token exchange" in low
        or ("client" in low and "credential" in low)
    ):
        return "OAuth2"
    if "personal access" in low or low in {"pat", "pats"}:
        return "Personal Access Token"
    if "bot token" in low or low == "bot":
        return "Bot Token"
    if (
        "service account" in low
        or "key-pair" in low
        or "keypair" in low
        or "key pair" in low
        or "workload identity" in low
    ):
        return "Service Account"
    if "basic auth" in low or "http basic" in low or "digest auth" in low:
        return "Basic Auth"
    if "api key" in low or "api-key" in low or "apikey" in low or "x-api-key" in low:
        return "API Key"
    if "api token" in low or low in {"developer token", "application key"}:
        return "API Key"
    if "bearer" in low or low in {
        "access token",
        "static access token",
        "vendor access token",
        "jwt",
        "jwt token",
    }:
        return "Bearer Token"

    if strict:
        raise ValueError(
            f"unknown auth label {raw!r}; expected one of: {', '.join(CANONICAL)}"
        )
    return "Other Token"


def normalize_auth_list(labels, *, strict: bool = False) -> list[str]:
    """Normalize and de-duplicate auth labels while preserving order.

    The not-applicable sentinel is dropped when a real method is present.
    """
    if isinstance(labels, str):
        labels = [labels]
    out: list[str] = []
    for raw in labels or []:
        canonical = normalize_auth(raw, strict=strict)
        if canonical and canonical not in out:
            out.append(canonical)
    real = [item for item in out if item != "None / Not Applicable"]
    return real if real else out


def auth_set(labels, *, strict: bool = False) -> set[str]:
    """Return the canonical set used by all verification comparisons."""
    return set(normalize_auth_list(labels, strict=strict))


def auth_sets_equal(left, right, *, strict: bool = False) -> bool:
    """Exact semantic equality after canonical label normalization."""
    return auth_set(left, strict=strict) == auth_set(right, strict=strict)


def auth_sets_overlap(left, right, *, strict: bool = False) -> bool:
    """Diagnostic overlap only; never use this as the accuracy score."""
    a = auth_set(left, strict=strict)
    b = auth_set(right, strict=strict)
    return (not a and not b) or bool(a & b)


# --------------------------------------------------------------------------- #
# Blocker clustering
# --------------------------------------------------------------------------- #
# The raw ``main_blocker`` field is free text and near-unique per app, so a plain
# frequency count is not a pattern. classify_blocker() buckets each record into a
# small, stable set of causes using the structured decision fields first (which
# already encode most of the signal) and only falling back to keyword matching on
# the blocker/access text to split within the Gated set.
BLOCKER_BUCKETS = [
    "None — buildable now",
    "Requires partner / sales contact",
    "Requires approval / app review",
    "Requires a paid plan or existing account",
    "No usable public API / MCP-only",
    "Access terms unclear in docs",
    "Other",
]


def classify_blocker(record: dict) -> str:
    """Return one stable blocker bucket for a synthesized record."""
    action = str(record.get("recommended_next_action") or "")
    kind = str((record.get("access_model") or {}).get("kind") or "")
    api_type = str(record.get("api_type") or "")
    text = " ".join([
        str(record.get("main_blocker") or ""),
        str((record.get("access_model") or {}).get("note") or ""),
    ]).lower()

    # No usable programmatic surface dominates everything else.
    if api_type in {"None", "MCP-only"} or "no usable" in text or "no public api" in text:
        if api_type == "MCP-only":
            return "No usable public API / MCP-only"
        if api_type == "None":
            return "No usable public API / MCP-only"

    if action == "Build Now" and kind == "Self-Serve":
        return "None — buildable now"

    if action == "Partner-Gated" or "partner" in text or "contact sales" in text or "contact us" in text:
        return "Requires partner / sales contact"

    # Split the remaining gated / outreach apps by the dominant reason in the text.
    approval_markers = ("approval", "review", "verification", "verify your", "allowlist", "allow list", "waitlist", "request access", "apply for")
    paid_markers = ("paid plan", "paid tier", "paid account", "existing customer", "existing paid", "subscription", "upgrade", "billing", "enterprise plan", "not free")

    if any(m in text for m in approval_markers):
        return "Requires approval / app review"
    if any(m in text for m in paid_markers):
        return "Requires a paid plan or existing account"

    if kind == "Gated":
        # Gated but the text does not name the specific mechanism.
        return "Access terms unclear in docs"
    if action == "Needs Outreach":
        return "Requires approval / app review"
    return "Other"

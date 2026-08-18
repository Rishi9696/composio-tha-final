# Integration Readiness

Can an agent be wired up against 100 requested apps today? This pipeline answers that per app — API surface, auth, production access, MCP ownership, Composio coverage — and ships the answer as a static reviewer console.

**Provider:** OpenAI, exclusively — Responses API `web_search` for documentation discovery, structured Chat Completions output for synthesis. No gateway, no fallback model.

→ **[Live console](https://composio-tha-final-6ujf6e98c-rishi96.vercel.app/)** · [Source](https://github.com/Rishi9696/composio-tha-final)

---

## At a glance

| | |
| --- | --- |
| Apps in scope | 100 (see `data/apps.json`) |
| Record schema | 19 locked fields, semantically validated |
| Synthesis model | `gpt-5`, structured output, `reasoning_effort=medium` |
| Search model | `gpt-4.1-mini`, per-query web search |
| Current counts | `out/metrics.json` — always the live source of truth |

Metric labels are deliberately narrow, not marketing:

- `handcheck.accuracy` — the latest staged pre-fold agreement, not a population-wide accuracy claim.
- `accuracy_movement` — first-pass snapshot vs. corrected dataset, same truth set.
- `confidence` — a triage signal for reviewers, not an accuracy estimate.

## Reading the output

Every committed artifact answers exactly one question:

| Ask | Look in |
| --- | --- |
| What's the current verdict per app? | `out/results.json` |
| What did the very first pass say? | `out/results_firstpass.json` (immutable) |
| How's the dataset trending? | `out/metrics.json` |
| Is there an active Composio toolkit? | `out/composio_coverage.json` |
| Why did the model decide X? | `out/reasoning/<slug>.md` |
| What did a human confirm by hand? | `handcheck/handcheck.json` |
| What did an independent browser agent see? | `out/browser_verification.json` |
| What does the console actually render? | `report/data.js` (generated, not hand-edited) |

`report/data.js` is a publication copy only — `out/` stays canonical, there's no second source of truth to drift.

## The record shape

Every app is forced into the same 19 fields, grouped by what they answer:

```
identity     app · slug · category · one_liner
integration  api_type · api_breadth · auth_methods[] · existing_mcp · composio_toolkit
access       access_model{kind,note} · buildability · main_blocker · recommended_next_action
evidence     evidence_urls[] · primary_docs_url · rate_limit_note
trust        confidence · verification_status · last_verified
```

## Pipeline

| Stage | Module | Does |
| --- | --- | --- |
| 1 | `composio_lookup.py` | Toolkit overlap check during research |
| 2 | `docs_research.py` | OpenAI web search (one call per query) + direct fetch → evidence |
| 3 | `synthesis.py` | Evidence → locked record via OpenAI structured output |
| 4 | `schema.py` | Deterministic enum + semantic gate — fails closed, never guesses |
| 5 | `pipeline.py` | Synchronous, resumable orchestration across all apps |
| 6 | `verify.py` | Metrics, blind re-search checks |
| 7 | `handcheck.py` | Human adjudication against official docs |

**Independently of the above:** `browser_verify.py` runs a cloud browser agent against live docs, and `composio_agent.py` runs one bounded, read-only Composio Session check per app.

Two things worth knowing about how this behaves:
- Evidence that can't support a claim means the app fails synthesis rather than getting a guessed answer — that's intentional, not a bug.
- Historical preseeds only steer *which* apps get prioritized; the model never sees them, so it can't anchor on a prior guess.

Under the hood, `synthesis.py` hands a Pydantic schema to `config.llm_json`, which uses the Chat Completions `parse` helper at `temperature=0`. Whatever the model returns still has to clear `schema.py`'s deterministic checks — the LLM proposes, the validator disposes.

## Composio integration

```bash
python research.py --composio-audit        # SDK-only Active/Catalog-only/Missing audit → out/composio_coverage.json
python research.py --composio-agent otter-ai   # one-app, read-only Session diagnostic
```

The audit atomically replaces its snapshot, or fails without touching the previous one if any profile comes back incomplete. The Session diagnostic loads one current record, runs a single bounded first-party doc-research task via the no-auth `browser_tool`, and deterministically compares the verdict — read-only, so disagreements go to a human, never straight into the dataset. The dataset's own `composio_toolkit` field is untouched by any of this; the SDK sidecar only adds current executable depth on top.

## Getting started

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
cp .env.example .env    # fill in keys below
```

| Key | Powers |
| --- | --- |
| `OPENAI_API_KEY` | search, synthesis, Session reasoning |
| `COMPOSIO_API_KEY` | toolkit audit, Composio Session |
| `BROWSER_USE_API_KEY` | optional — independent browser verification |

**Run everything, fresh:**
```bash
python research.py --all --fresh-run --model gpt-5
python research.py --metrics
```
Drop `--fresh-run` to resume a partial run instead of starting over.

**Iterate on a slice:**
```bash
python research.py --app stripe
python research.py --slugs stripe,notion
python research.py --limit 5
```

**Full verification + rebuild loop:**
```bash
python browser_verify.py --sample 12
python research.py --handcheck-template 24   # then fill handcheck/handcheck.json by hand
python research.py --fold-handcheck
python research.py --apply-handcheck
python research.py --accuracy-movement
python research.py --composio-audit
python research.py --composio-agent otter-ai
python research.py --build-report
```

## Testing & preview

```bash
python -m unittest discover -s tests -v
ruff check *.py tests
python -m compileall -q *.py tests
node --check report/app.js
git diff --check
```

Local preview:
```bash
cd report && python -m http.server 8000   # → http://localhost:8000
```

Deploy: `cd report && vercel deploy --prod` (Vercel project root must be `report/`, not the repo root — there's no build step, it's static).

## Layout

```
.
├─ research.py            single CLI entry point
├─ pipeline.py            synchronous, resumable orchestration
├─ docs_research.py       OpenAI web search + fetch
├─ synthesis.py           structured-output synthesis
├─ schema.py              locked record contract
├─ normalize.py           canonical auth labels
├─ verify.py              metrics + blind re-search
├─ handcheck.py           human adjudication workflow
├─ browser_verify.py      independent cloud-browser checks
├─ composio_lookup.py     toolkit lookup + coverage audit
├─ composio_agent.py      read-only Session diagnostic
├─ config.py              env, atomic JSON I/O, OpenAI client
├─ usage_tracker.py       per-provider spend ledger
├─ data/                  the 100-app catalog + risk preseeds
├─ handcheck/             human-confirmed truth
├─ out/                   canonical results + evidence (source of truth)
├─ report/                static console — the actual deliverable
└─ tests/                 quality + regression suite
```

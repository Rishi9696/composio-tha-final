# Can an AI agent call this app today?

Research pipeline + single-page case study for the Composio AI Product Ops take-home. It evaluates 100 requested apps across auth model, self-serve vs. gated access, API surface, existing MCP coverage, and whether an agent toolkit could be built against each one today.

- Case study: `site/index.html` (open directly in a browser, or deploy the `site/` folder to any static host)
- Full dataset: `results/results_final.json`
- Patterns/metrics: `results/patterns_final.json`
- Verification trail: `results/verification_report.json`

## What's here

```
data/apps.json            the 100-app list from the assignment (id, name, category, hint)
data/schema.md             the locked 15-field research schema every app record follows
results/batch_01..10.json  raw first-pass output, one file per category (10 apps each)
results/pass_1.json        merged, validated first pass (100 records)
results/patterns.json      patterns computed from the first pass
results/verification_blind.json   independent blind re-check of a 20-app sample
results/verification_report.json  methodology, disagreements, adjudication, before/after accuracy
results/results_final.json        pass_1 with verified corrections applied (canonical dataset)
results/patterns_final.json       patterns recomputed from the corrected dataset
build_site.py               generates site/index.html from the three files above
site/index.html             the single self-contained case-study page (data is embedded inline)
```

## How the research was actually done

No paid research API was used. The research agent is Claude itself, given live web search and page-fetching tools, run as **10 parallel subagents** — one per category, 10 apps each. Each subagent was instructed to:

1. Actually search and fetch each app's real developer docs, pricing page, and MCP listings — not answer from memory.
2. Fill in the locked schema (`data/schema.md`) for every app.
3. Cite at least one real URL for every claim, or mark the field `unknown` rather than guess.

Outputs were merged and validated (`results/pass_1.json`), then a Python pass computed cross-cutting patterns (`results/patterns.json`).

### Verification loop

A **separate, blind subagent** — given only the app names, no access to the first pass's answers — independently re-researched a 20-app stratified sample (2 per category, weighted toward apps the first pass had already flagged medium/low confidence). Every field where the two passes disagreed was adjudicated by hand: re-fetching the actual primary source and deciding which answer (or neither) held up.

- First-pass accuracy on the 60 checked fields (20 apps × 3 fields): **78.3%**
- After corrections were folded back into the full 100-app dataset: **100%** on those same checked fields (see the caveat in `verification_report.json` — this reflects known errors fixed, not an independent re-audit of the other 80 apps)
- 9 of 20 sampled apps needed at least one field corrected
- Some disagreements went the *other* way — the first pass was right and the independent re-check was wrong (e.g. Salesforce's official MCP server, iPayX's real MCP repo) — both directions are logged, not just the flattering one
- One app, "Paygent Connect," could not be matched to any real, findable product by either pass and is reported as an honest miss rather than a guess

## Reproducing / extending this

The research itself was run interactively (agent dispatch + tool calls), not via a single CLI command, so there's no `pip install && run.sh` that reproduces the live web research byte-for-byte. What you can rerun deterministically:

```bash
# Recompute patterns_final.json and results_final.json from scratch given the raw batches:
python3 -c "
import json
batches = [json.load(open(f'results/batch_{str(n).zfill(2)}.json')) for n in range(1,11)]
merged = sorted([r for b in batches for r in b], key=lambda r: r['id'])
assert [r['id'] for r in merged] == list(range(1,101))
json.dump(merged, open('results/pass_1.json','w'), indent=2)
print('OK:', len(merged))
"

# Rebuild the case-study page after editing any results/*.json:
python3 build_site.py
```

To extend the research (add apps, re-verify a different sample, wire in Composio's own SDK for a toolkit-coverage audit), follow the same pattern: dispatch a research task with the schema in `data/schema.md`, require real evidence URLs, merge into `results/`, then re-run `build_site.py`.

## Where a human was needed (not automated away)

- Adjudicating every disagreement between the two research passes against the actual primary source
- Deciding consistency rules for judgment calls (e.g. "must already be a paying customer" = `buildable_with_workaround`, applied the same way across Brex, Aircall, DealCloud)
- Catching stale research (Clay's first pass cited older, plan-gated docs; the product had shipped a new free self-serve API since)
- Catching a mid-research rebrand (fanbasis.com → Commas)
- Deciding to report "Paygent Connect" as unresolved instead of forcing an answer

## Composio SDK integration (not wired in)

The assignment calls out using Composio's own SDK as being "in the spirit of the role" — checking, for each app, whether Composio already has a working toolkit, how many actions it exposes, and whether it supports triggers. That requires a Composio API key, which wasn't available in this environment. `results_final.json`'s schema has room for a `composio_toolkit` field to be added the same way the rest of the pipeline works: dispatch a lookup against the Composio SDK for each app, merge the result in, rerun `build_site.py`.

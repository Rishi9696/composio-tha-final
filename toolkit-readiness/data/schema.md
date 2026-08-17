# Research record schema

One JSON object per app, all fields required (use `"unknown"` / empty array honestly if not determinable — never guess).

| field | type | values / notes |
|---|---|---|
| `id` | int | matches `apps.json` id |
| `app` | string | app name |
| `category` | string | one of the 10 assignment categories |
| `one_liner` | string | what the product does, one sentence |
| `auth_methods` | string[] | any of: `OAuth2`, `API Key`, `Basic Auth`, `Token`, `JWT`, `Other`, `Unknown` |
| `access` | string | one of: `self_serve_free`, `self_serve_trial`, `gated_paid_plan`, `gated_approval`, `gated_partnership`, `unclear` |
| `access_note` | string | 1 sentence explaining the access classification |
| `api_type` | string | one of: `REST`, `GraphQL`, `REST+GraphQL`, `SDK_only`, `no_public_api`, `other` |
| `api_breadth` | string | one of: `broad`, `moderate`, `narrow`, `unknown` |
| `api_breadth_note` | string | brief justification (e.g. "40+ resource endpoints covering contacts, deals, pipelines") |
| `existing_mcp` | string | one of: `official`, `community`, `none_found`, `unknown` |
| `existing_mcp_note` | string | link/name of the MCP server if found |
| `buildability` | string | one of: `buildable_now`, `buildable_with_workaround`, `blocked` |
| `main_blocker` | string | the single biggest blocker if not cleanly `buildable_now` (empty string if none) |
| `evidence` | array of `{ "url": string, "note": string }` | at least 1, ideally 2+ real URLs that back the answers above |
| `confidence` | string | `high`, `medium`, `low` — the researcher's own confidence in this record |
| `researcher_notes` | string | anything surprising, ambiguous, or worth a human double-checking |

Do not fabricate URLs or numbers. If a claim can't be backed by something actually seen (docs page, pricing page, GitHub repo, etc.), mark the field `unknown` / lower the confidence and say why in `researcher_notes`.

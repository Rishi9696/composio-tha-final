# MrScraper - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["MrScraper official API authentication developer documentation", "MrScraper API production access approval credentials official documentation", "MrScraper official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://docs.mrscraper.com | HTTP 200 | hint | topics=api,auth,access,mcp
- https://docs.mrscraper.com/docs/features/activating-api | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://docs.mrscraper.com/docs/api/overview | HTTP 200 | search_result | topics=api,auth
- https://docs.mrscraper.com/docs/getting-started/billing | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://docs.mrscraper.com/docs/getting-started/cli | HTTP 200 | search_result | topics=api,auth,mcp
- https://developer.mrscraper.com | HTTP 0 | derived_guess | topics=none

## Model reasoning
1) What the evidence states: The API Overview says the MrScraper API is REST and requires an API token sent in the x-api-token header for all endpoints. The Scraper API page shows enabling "AI Scraper API Access" in the dashboard and lists x-api-token as a required header. The CLI docs require a "MrScraper API Token" (API key) for authentication via login, env vars, or flags. The MCP Server page describes a cloud-hosted, vendor-managed MCP server for MrScraper and lists prerequisites as a MrScraper account and a MrScraper API Token. The Billing page lists Free/Pro/Enterprise plans, explicitly noting a Free plan with 100 tokens/month and that you must upgrade after exhausting the allocation. 2) Production Access Rubric: The Billing page says "The Free plan includes 100 tokens per month with no credit card required... Once your allocation is exhausted, you'll need to upgrade to continue scraping." While this proves self-serve signup and key creation, there is no explicit statement that those credentials constitute unrestricted production entitlement. The rubric warns: a key-generation page proves credential mechanics, not production entitlement, and if free access expires and continued API use needs a paid plan, classify Gated. There is no evidence of manual approval, but also no explicit free production entitlement beyond a quota-limited plan. 3) Conclusions: Auth methods = API Key. API type = REST. An official vendor MCP server exists. Access model = Gated per the rubric (no explicit statement of free production entitlement and continued use requires a paid plan). Buildability = Moderate (clear REST docs and tokens, but production requires paid upgrade/plan decision). Recommended action = Needs Outreach (to upgrade/confirm production plan).

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - Docs show self-serve signup and API tokens, but no explicit free production entitlement; continued use requires a paid plan after free tokens are exhausted.
- recommended_next_action: **Needs Outreach**
- confidence: **0.64**

## Evidence URLs
- https://docs.mrscraper.com/docs/api/overview
- https://docs.mrscraper.com/docs/features/activating-api
- https://docs.mrscraper.com/docs/getting-started/cli
- https://docs.mrscraper.com/docs/getting-started/billing
- https://docs.mrscraper.com/docs/getting-started/mcp-server

## Generated record
```json
{
  "app": "MrScraper",
  "category": "Research/Scraping",
  "one_liner": "MrScraper offers a REST API and official MCP server using API tokens, but production is plan-gated.",
  "auth_methods": [
    "API Key"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Docs show self-serve signup and API tokens, but no explicit free production entitlement; continued use requires a paid plan after free tokens are exhausted."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "Production use requires a paid plan beyond the limited free tokens; no explicit free production entitlement stated.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://docs.mrscraper.com/docs/api/overview",
    "https://docs.mrscraper.com/docs/features/activating-api",
    "https://docs.mrscraper.com/docs/getting-started/cli",
    "https://docs.mrscraper.com/docs/getting-started/billing",
    "https://docs.mrscraper.com/docs/getting-started/mcp-server"
  ],
  "confidence": 0.64,
  "verification_status": "Auto",
  "slug": "mrscraper",
  "primary_docs_url": "https://docs.mrscraper.com/docs/getting-started/billing",
  "rate_limit_note": "Token-based quotas and plan-specific concurrency (e.g., 10 on Free, 100 on Pro); usage exposed via response headers.",
  "last_verified": "2026-08-18"
}
```

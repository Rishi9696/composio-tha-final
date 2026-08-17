# SE Ranking - synthesis reasoning
_generated 2026-08-17 | model openai:gpt-5_

## Research trace
- queries: ["SE Ranking official API authentication developer documentation", "SE Ranking API production access approval credentials official documentation", "SE Ranking official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://seranking.com/api | HTTP 404 | hint | topics=none
- https://help.seranking.com/hc/en-us/articles/22447958135068-Getting-Started-with-SE-Ranking-s-API | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://help.seranking.com/hc/en-us/articles/21487397355420-API-pricing | HTTP 200 | search_result | topics=api,access,mcp
- https://seranking.com/api/data/getting-started/ | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://developer.seranking.com | HTTP 0 | derived_guess | topics=none
- https://developers.seranking.com | HTTP 0 | derived_guess | topics=none

## Model reasoning
1) What the evidence states:
- REST API surface: The Help Center states “The Data API and Project API are unified under a single API key. One key provides access to both … through the same api.seranking.com gateway,” and provides steps to “Generate an API key” in the API Dashboard (help.seranking.com Getting Started with SE Ranking’s API). The Data API ‘Getting started’ page includes Authentication and Making requests sections (seranking.com/api/data/getting-started/), supporting REST usage.
- Auth credentials (REST): Explicit API key generation is described (“Click Create API Key”) and a single key is used across Data and Project APIs (help.seranking.com Getting Started).
- MCP surface: SE Ranking hosts an official MCP integration page (seranking.com/api/integrations/mcp/). Third-party listings describe the SE Ranking MCP server as OAuth-based: Gamut shows “Auth: OAuth” and MCPBundles says “OAuth-authenticated MCP tools.”
- Access/pricing: The Help Center repeats: “The API package is available as a standalone product — no active SE Ranking subscription is required. Start with a 14-day trial that includes 100,000 free API credits. Paid plans include monthly Data API credits…” (both ‘Getting Started with SE Ranking’s API’ and ‘API pricing’ articles).

2) Production Access Rubric application:
- Evidence shows a time-limited free trial (“14-day trial… 100,000 free API credits”) and then ongoing use via paid plans (“Paid plans include monthly Data API credits…”). There is no statement of a free self-serve production tier. Per the rubric, if free access expires and continued API use needs a paid plan, classify Gated. The docs also show credential enablement (API key) but do not claim unrestricted self-serve production use without payment or approval.

3) Decisions from the above:
- api_type: REST is the dominant public surface (Data/Project APIs), with an additional official MCP surface. 
- auth_methods: API Key (REST). MCP uses OAuth2 (per Gamut and MCPBundles) — included as an additional official surface.
- existing_mcp: Official (vendor-hosted MCP page).
- access_model: Gated due to paid plan required after the 14-day trial.
- buildability: Moderate — docs and auth are clear and keys are generated in-dashboard, but production requires purchasing the API package (not self-serve free production).
- recommended_next_action: Needs Outreach — obtain/activate a paid API plan (or coordinate with SE Ranking sales/billing) to enable production use.

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - API key is generated in the dashboard, but ongoing production use requires purchasing the standalone API package; only a 14‑day trial (100k credits) is free.
- recommended_next_action: **Needs Outreach**
- confidence: **0.77**

## Evidence URLs
- https://help.seranking.com/hc/en-us/articles/22447958135068-Getting-Started-with-SE-Ranking-s-API
- https://help.seranking.com/hc/en-us/articles/21487397355420-API-pricing
- https://seranking.com/api/data/getting-started/
- https://seranking.com/api/integrations/mcp/
- https://www.gamut.so/mcp/analytics-marketing/se-ranking
- https://www.mcpbundles.com/skills/seranking-mcp

## Generated record
```json
{
  "app": "SE Ranking",
  "category": "Research/Scraping",
  "one_liner": "SE Ranking offers a REST API with API keys and an official MCP; production access requires a paid plan.",
  "auth_methods": [
    "API Key",
    "OAuth2"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "API key is generated in the dashboard, but ongoing production use requires purchasing the standalone API package; only a 14‑day trial (100k credits) is free."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "No",
  "buildability": "Moderate",
  "main_blocker": "Production access requires a paid API plan; the free 14‑day trial is non‑ongoing.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://help.seranking.com/hc/en-us/articles/22447958135068-Getting-Started-with-SE-Ranking-s-API",
    "https://help.seranking.com/hc/en-us/articles/21487397355420-API-pricing",
    "https://seranking.com/api/data/getting-started/",
    "https://seranking.com/api/integrations/mcp/",
    "https://www.gamut.so/mcp/analytics-marketing/se-ranking",
    "https://www.mcpbundles.com/skills/seranking-mcp"
  ],
  "confidence": 0.77,
  "verification_status": "Auto",
  "slug": "se-ranking",
  "primary_docs_url": "https://help.seranking.com/hc/en-us/articles/22447958135068-Getting-Started-with-SE-Ranking-s-API",
  "rate_limit_note": "Credit-based usage; 14-day trial includes 100,000 credits and paid plans include monthly credits. Separate rate limit docs exist.",
  "last_verified": "2026-08-17"
}
```

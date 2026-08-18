# Apify - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Apify official API authentication developer documentation", "Apify API production access approval credentials official documentation", "Apify official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://docs.apify.com | HTTP 200 | hint | topics=api,auth,mcp
- https://docs.apify.com/api/v2#getting-started | HTTP 200 | search_result | topics=api,auth,mcp
- https://www.youtube.com/watch?v=XoMUf-ML5eY | HTTP 200 | search_result | topics=none
- https://docs.apify.com/api | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://developer.apify.com | HTTP 0 | derived_guess | topics=none
- https://developers.apify.com | HTTP 200 | derived_guess | topics=api,auth,mcp

## Model reasoning
1) Evidence summary: The Apify API docs state it is an HTTP REST API and show requests authenticated with Authorization: Bearer <YOUR_API_TOKEN> and client libraries initialized with a token (e.g., token: 'MY-APIFY-TOKEN') on https://docs.apify.com/api. The API reference at https://docs.apify.com/api/v2#getting-started lists extensive endpoints (Actors, Storage, Webhooks, Schedules, etc.), indicating a broad surface. The MCP integration docs state the Apify MCP server (mcp.apify.com) allows AI agents to interact with Apify and that you can connect via a hosted service “using Streamable HTTP with OAuth,” or run the server locally (https://docs.apify.com/platform/integrations/mcp and https://docs.apify.com/integrations/mcp). 2) Production Access Rubric: The docs demonstrate immediate-use credentials (API token) and a hosted MCP connection via OAuth and do not mention approval gates, paid-plan prerequisites, or manual reviews. There is no sentence imposing approvals; the flows are documented as available. In absence of gating evidence and given credential enablement examples, this supports Self-Serve classification. 3) Decisions: Auth methods = API Key (Apify API token) and OAuth2 (hosted MCP). Dominant public API = REST. Existing MCP = Official (vendor-hosted). Access model = Self-Serve based on token/OAuth flows described without approval requirements. Buildability = Easy due to clear REST and MCP docs. Recommended next action = Build Now.

## Key decisions
- buildability: **Easy**
- access_model: **Self-Serve** - Docs show usage with an API token and a hosted MCP using OAuth, with no stated approval or paid-plan prerequisites.
- recommended_next_action: **Build Now**
- confidence: **0.55**

## Evidence URLs
- https://docs.apify.com/api
- https://docs.apify.com/api/v2#getting-started
- https://docs.apify.com/platform/integrations/mcp
- https://docs.apify.com/integrations/mcp
- https://github.com/apify/apify-mcp-server

## Generated record
```json
{
  "app": "Apify",
  "category": "Research/Scraping",
  "one_liner": "Apify offers a broad REST API and official MCP server with API token and OAuth-based access ready to build now.",
  "auth_methods": [
    "API Key",
    "OAuth2"
  ],
  "access_model": {
    "kind": "Self-Serve",
    "note": "Docs show usage with an API token and a hosted MCP using OAuth, with no stated approval or paid-plan prerequisites."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Easy",
  "main_blocker": "None; API token and hosted MCP OAuth flows appear directly usable per docs.",
  "recommended_next_action": "Build Now",
  "evidence_urls": [
    "https://docs.apify.com/api",
    "https://docs.apify.com/api/v2#getting-started",
    "https://docs.apify.com/platform/integrations/mcp",
    "https://docs.apify.com/integrations/mcp",
    "https://github.com/apify/apify-mcp-server"
  ],
  "confidence": 0.55,
  "verification_status": "Auto",
  "slug": "apify",
  "primary_docs_url": "https://docs.apify.com/api",
  "rate_limit_note": "No rate limit details found on the cited pages.",
  "last_verified": "2026-08-18"
}
```

<!-- final-state:start -->
## Final pipeline state
_Updated 2026-08-18 by current human handcheck correction; this supersedes earlier key decisions._

```json
{
  "app": "Apify",
  "category": "Research/Scraping",
  "one_liner": "Apify offers a broad REST API and official MCP server with API token and OAuth-based access ready to build now.",
  "auth_methods": [
    "API Key"
  ],
  "access_model": {
    "kind": "Self-Serve",
    "note": "Docs show usage with an API token and a hosted MCP using OAuth, with no stated approval or paid-plan prerequisites."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Easy",
  "main_blocker": "None; API token and hosted MCP OAuth flows appear directly usable per docs.",
  "recommended_next_action": "Build Now",
  "evidence_urls": [
    "https://docs.apify.com/api/v2/getting-started",
    "https://docs.apify.com/platform/integrations/mcp"
  ],
  "confidence": 0.55,
  "verification_status": "Hand-Checked",
  "slug": "apify",
  "primary_docs_url": "https://docs.apify.com/api/v2/getting-started",
  "rate_limit_note": "No rate limit details found on the cited pages.",
  "last_verified": "2026-08-18"
}
```
<!-- final-state:end -->

# Attio - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Attio official API authentication developer documentation", "Attio API production access approval credentials official documentation", "Attio official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://attio.com | HTTP 200 | hint | topics=api,access,mcp
- https://docs.attio.com/rest-api/guides/authentication | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://attio.com/pricing?utm_source=openai | HTTP 200 | search_result | topics=api,access,mcp
- https://docs.attio.com/sdk/server/attio-api-token | HTTP 200 | search_result | topics=api,auth,mcp
- https://developer.attio.com | HTTP 0 | derived_guess | topics=none
- https://developers.attio.com | HTTP 200 | derived_guess | topics=api,mcp

## Model reasoning
1) What the evidence states: The REST API auth guide says you can generate access tokens either “By implementing an OAuth 2.0 flow” or “By generating an API key for your workspace,” and to use them via Authorization: Bearer. It explicitly adds: “We also support HTTP Basic Authentication, where the username is the token and the password is left blank.” The SDK server doc shows ATTIO_API_TOKEN being used as a Bearer token to call the REST API. MCP overview and mcp.attio.com indicate Attio hosts an MCP server and uses OAuth to connect (“Easy setup — Connect through simple OAuth,” and “complete the OAuth authentication when prompted”). The Help Center page for Attio MCP states: “Available on all plans. Available for all workspace members.” The pricing page shows a Free plan (“Start for free”). Note: the authentication page’s metadata signals include “Other Token”; while the body emphasizes OAuth 2.0, this suggests an additional token variant (e.g., legacy OAuth 1.x) exists, though details are not elaborated here. 2) Production Access Rubric: For MCP, the Help Center explicitly says it’s “Available on all plans. Available for all workspace members,” supporting self-serve availability via OAuth. For the REST API, the docs explain how to obtain tokens (OAuth 2.0 or API key) but do not state that production access is self-serve by plan; per the rubric, credential mechanics alone do not prove production entitlement. Therefore, treat REST as gated/unclear, and note MCP is self-serve. 3) Conclusions: Auth methods: OAuth2, API Key, Basic Auth (explicitly supported), and Other Token (per documented signals indicating an additional token type). Dominant surface: REST (with an additional official, hosted MCP). Access model overall: Gated (REST uncertainty) with a note that MCP is self-serve. Buildability: Moderate (clear docs; OAuth/app setup; potential outreach to confirm REST production use). Next action: Needs Outreach (confirm REST production access or proceed via MCP).

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - REST API: docs show OAuth2, API keys, and Basic Auth but do not confirm self-serve production access by plan. MCP: Help Center states “Available on all plans. Available for all workspace members,” using OAuth with one‑click setup.
- recommended_next_action: **Needs Outreach**
- confidence: **0.6**

## Evidence URLs
- https://docs.attio.com/rest-api/guides/authentication
- https://docs.attio.com/sdk/server/attio-api-token
- https://docs.attio.com/mcp/overview
- https://attio.com/help/reference/attio-ai/attio-mcp
- https://mcp.attio.com/
- https://attio.com/pricing?utm_source=openai

## Generated record
```json
{
  "app": "Attio",
  "category": "CRM",
  "one_liner": "Attio offers REST and an official hosted MCP; OAuth2/API keys supported, MCP is self-serve; REST access unclear.",
  "auth_methods": [
    "OAuth2",
    "API Key",
    "Basic Auth",
    "Other Token"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "REST API: docs show OAuth2, API keys, and Basic Auth but do not confirm self-serve production access by plan. MCP: Help Center states “Available on all plans. Available for all workspace members,” using OAuth with one‑click setup."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "No explicit proof that REST API production use is self-serve; plan/approval requirements are not stated.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://docs.attio.com/rest-api/guides/authentication",
    "https://docs.attio.com/sdk/server/attio-api-token",
    "https://docs.attio.com/mcp/overview",
    "https://attio.com/help/reference/attio-ai/attio-mcp",
    "https://mcp.attio.com/",
    "https://attio.com/pricing?utm_source=openai"
  ],
  "confidence": 0.6,
  "verification_status": "Auto",
  "slug": "attio",
  "primary_docs_url": "https://docs.attio.com/rest-api/guides/authentication",
  "rate_limit_note": "Docs mention rate limits and handling but no concrete numeric limits are specified on the cited pages.",
  "last_verified": "2026-08-18"
}
```

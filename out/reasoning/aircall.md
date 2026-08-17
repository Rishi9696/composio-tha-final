# Aircall - synthesis reasoning
_generated 2026-08-17 | model openai:gpt-5_

## Research trace
- queries: ["Aircall official API authentication developer documentation", "Aircall API production access approval credentials official documentation", "Aircall official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://aircall.io | HTTP 200 | hint | topics=api,access
- https://apis.io/apis/aircall/aircall-calls-api/ | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://aircall.io/pricing/ | HTTP 200 | search_result | topics=api,access
- https://developer.aircall.io/tutorials/basic-authentication/ | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://developer.aircall.io | HTTP 200 | derived_guess | topics=api,access,mcp
- https://developers.aircall.io | HTTP 200 | derived_guess | topics=api,auth,access

## Model reasoning
1) What the evidence explicitly says:
- API surface: The developer portal promotes a REST API and webhooks (“REST API and webhooks”) and lists Foundations docs including “Authenticate with API Keys” and an “OAuth implementation guide” (developer.aircall.io/tutorials/basic-authentication/; developer.aircall.io).
- Auth: The apis.io OpenAPI page states: “Authentication supports OAuth 2.0 (for technology partners) or HTTP Basic auth using api_id / api_token (for customers). Rate limit: 120 requests per minute per API key.” It also confirms the REST base URL https://api.aircall.io/v1 and broad resources (users, teams, calls, numbers, contacts, tags, messages, webhooks, etc.) (apis.io/apis/aircall/aircall-calls-api/). The Aircall docs index shows “Authenticate with API Keys” and “OAuth implementation guide,” corroborating API key and OAuth surfaces (developer.aircall.io/tutorials/basic-authentication/).
- MCP: The developer portal mentions MCP as part of the platform (“AI API MCP … Connect your tools and data to Aircall’s AI Virtual Agents through MCP”), implying MCP is used for integrating tools into Aircall’s agents, but there is no vendor-hosted MCP server documentation shown (developer.aircall.io). No solid fetched content confirms an official or third‑party MCP server for Aircall; the StackOne page fetch was too thin to rely on.

2) Production Access Rubric application:
- Evidence indicating gating: apis.io states OAuth 2.0 is “for technology partners,” implying partner approval for OAuth. It also says HTTP Basic using api_id/api_token is “for customers,” implying you must be an Aircall customer to use production API keys. There is no statement anywhere that a new developer can obtain production credentials without approval or payment. Therefore, by the rubric, production access is Gated.

3) Decisions derived:
- Auth methods: Basic Auth (with api_id/api_token) and API Key are supported for customers; OAuth2 exists for technology partners. No evidence for Bearer Token, Personal Access Token, or Service Account.
- API type: REST is the dominant public surface; webhooks exist but do not change the dominant type.
- Existing MCP: No confirmed official server; third-party evidence is insufficiently substantiated in fetched content, so mark None.
- Access model: Gated, since production requires being a customer for API keys or a technology partner for OAuth, with no proof of self‑serve production credentials for non‑customers.
- Buildability: Hard due to commercial/partner gating despite clear REST docs.
- Next action: Needs Outreach (become a customer or engage the partner program).
- Rate limits: 120 requests/min per API key per apis.io page.

## Key decisions
- buildability: **Hard**
- access_model: **Gated** - apis.io states OAuth2 is for technology partners and HTTP Basic with api_id/api_token is for customers; no evidence of self-serve production credentials for non-customers.
- recommended_next_action: **Needs Outreach**
- confidence: **0.64**

## Evidence URLs
- https://apis.io/apis/aircall/aircall-calls-api/
- https://developer.aircall.io
- https://developer.aircall.io/tutorials/basic-authentication/

## Generated record
```json
{
  "app": "Aircall",
  "category": "Comms",
  "one_liner": "Aircall provides a REST API with API key (Basic) and OAuth2, but production access is gated to customers/partners.",
  "auth_methods": [
    "Basic Auth",
    "API Key",
    "OAuth2"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "apis.io states OAuth2 is for technology partners and HTTP Basic with api_id/api_token is for customers; no evidence of self-serve production credentials for non-customers."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "None",
  "composio_toolkit": "No",
  "buildability": "Hard",
  "main_blocker": "Production credentials require being an Aircall customer (for API keys) or an approved technology partner (for OAuth2).",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://apis.io/apis/aircall/aircall-calls-api/",
    "https://developer.aircall.io",
    "https://developer.aircall.io/tutorials/basic-authentication/"
  ],
  "confidence": 0.64,
  "verification_status": "Auto",
  "slug": "aircall",
  "primary_docs_url": "https://developer.aircall.io/tutorials/basic-authentication/",
  "rate_limit_note": "apis.io notes 120 requests per minute per API key.",
  "last_verified": "2026-08-17"
}
```

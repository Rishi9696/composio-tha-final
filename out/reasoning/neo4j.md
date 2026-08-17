# Neo4j - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Neo4j official API authentication developer documentation", "Neo4j API production access approval credentials official documentation", "Neo4j official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://neo4j.com/docs/api | HTTP 404 | hint | topics=none
- https://neo4j.com/docs/aura/api/authentication/ | HTTP 200 | search_result | topics=api,auth,access
- https://neo4j.com/pricing/?utm_source=openai | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://neo4j.com/docs/http-api/current/authentication-authorization/ | HTTP 200 | search_result | topics=api,auth
- https://developer.neo4j.com | HTTP 0 | derived_guess | topics=none
- https://developers.neo4j.com | HTTP 0 | derived_guess | topics=none

## Model reasoning
1) What the evidence states:
- HTTP API: The "Authorize requests" page confirms an HTTP surface and auth requirement: it says the HTTP API authorize flow is "Not available on Aura" and that examples are deprecated in 5.26 in favor of the HTTP Query API, and that "Unless authentication is disabled on the server, all requests must be authorized using the login credentials..." (https://neo4j.com/docs/http-api/current/authentication-authorization/). This supports a REST-like HTTP API and requires auth.
- Aura API auth: There is a dedicated Aura API authentication doc page (https://neo4j.com/docs/aura/api/authentication/). The fetched record flags OAuth2/Basic/Bearer signals, indicating OAuth 2.0-based authentication for Aura APIs, though the visible snippet is sparse.
- MCP: There is an official Neo4j MCP docs page on neo4j.com (https://neo4j.com/docs/mcp/current/?utm_source=openai) and a GitHub repository at github.com/neo4j/mcp, indicating an official MCP server offering/documentation.
- Pricing/production: The pricing page (https://neo4j.com/pricing/?utm_source=openai) shows commercial offerings and "Get started free" messaging but does not explicitly state that new developers get production API credentials without approval or a paid plan.

2) Production Access Rubric application:
- There is no explicit sentence confirming that a new developer can obtain production credentials self-serve without approval/payment. The pricing page is commercial and does not state a free self-serve production entitlement. Therefore, per the rubric, without explicit proof of self-serve production access, classify as Gated.

3) Decisions deriving from 1 and 2:
- api_type: REST is the dominant public HTTP surface evidenced by the HTTP API/Query API docs; MCP also exists but is an additional surface.
- auth_methods: Basic Auth (HTTP API requires login credentials) and OAuth2 (Aura API authentication docs indicate OAuth 2.0). Do not add Bearer Token separately since OAuth2 tokens being sent as Bearer does not constitute an independent static token method.
- existing_mcp: Official, given official docs on neo4j.com and the neo4j-owned GitHub repo.
- access_model: Gated because there is no explicit proof of self-serve production entitlement; commercial pricing implies production use ties to Aura accounts/plans.
- buildability: Hard due to gated production access ambiguity and split surfaces (Aura OAuth2 vs self-managed HTTP API not available on Aura), requiring account/plan setup or outreach.
- recommended_next_action: Needs Outreach to clarify production access and obtain appropriate Aura credentials/plan.

## Key decisions
- buildability: **Hard**
- access_model: **Gated** - Docs show HTTP/Query API with auth and Aura OAuth2, but no explicit self-serve production entitlement; pricing indicates commercial plans and Aura account/plan needed.
- recommended_next_action: **Needs Outreach**
- confidence: **0.49**

## Evidence URLs
- https://neo4j.com/docs/http-api/current/authentication-authorization/
- https://neo4j.com/docs/aura/api/authentication/
- https://neo4j.com/pricing/?utm_source=openai
- https://neo4j.com/docs/mcp/current/?utm_source=openai
- https://github.com/neo4j/mcp?utm_source=openai

## Generated record
```json
{
  "app": "Neo4j",
  "category": "DevInfra",
  "one_liner": "Neo4j offers REST and MCP integrations, but production access likely requires an Aura account or plan.",
  "auth_methods": [
    "OAuth2",
    "Basic Auth"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Docs show HTTP/Query API with auth and Aura OAuth2, but no explicit self-serve production entitlement; pricing indicates commercial plans and Aura account/plan needed."
  },
  "api_type": "REST",
  "api_breadth": "Moderate",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Hard",
  "main_blocker": "No explicit evidence of self-serve production credentials; Aura access appears tied to commercial plans/accounts.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://neo4j.com/docs/http-api/current/authentication-authorization/",
    "https://neo4j.com/docs/aura/api/authentication/",
    "https://neo4j.com/pricing/?utm_source=openai",
    "https://neo4j.com/docs/mcp/current/?utm_source=openai",
    "https://github.com/neo4j/mcp?utm_source=openai"
  ],
  "confidence": 0.49,
  "verification_status": "Auto",
  "slug": "neo4j",
  "primary_docs_url": "https://neo4j.com/docs/aura/api/authentication/",
  "rate_limit_note": "No public rate limit details found in the cited docs.",
  "last_verified": "2026-08-18"
}
```

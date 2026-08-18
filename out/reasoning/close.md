# Close - synthesis reasoning
_generated 2026-08-17 | model openai:gpt-5_

## Research trace
- queries: ["Close official API authentication developer documentation", "Close API production access approval credentials official documentation", "Close official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://close.com | HTTP 200 | hint | topics=api,access,mcp
- https://developer.close.com/api/overview/api-key-authentication | HTTP 200 | search_result | topics=api,auth | content=https://developer.close.com/api/overview/api-key-authentication.md
- https://developer.close.com/api/overview/oauth-authentication | HTTP 200 | search_result | topics=api,auth | content=https://developer.close.com/api/overview/oauth-authentication.md
- https://help.close.com/integrations/api-keys-oauth | HTTP 200 | search_result | topics=api,auth,access,mcp | content=https://help.close.com/integrations/api-keys-oauth.md
- https://developer.close.com | HTTP 200 | derived_guess | topics=api,auth,access,mcp | content=https://developer.close.com/.md
- https://developers.close.com | HTTP 0 | derived_guess | topics=none

## Model reasoning
1) What the evidence states:
- REST API and endpoints: The developer docs present a REST API with an API base URL “https://api.close.com/api/v1” and a full API reference (developer portal). Auth options are documented as API keys and OAuth 2.0. (“API keys use HTTP Basic client side authentication… API Base URL: https://api.close.com/api/v1”; “To implement authentication with OAuth 2.0, you need to create an OAuth app… obtain Access Token and use Authorization: Bearer”).
- Auth credentials: API keys can be created in Close under Settings → Developer → API Keys; requests use HTTP Basic with the API key as username and blank password. OAuth 2.0 uses the standard authorization code flow; tokens are Bearer tokens obtained via https://api.close.com/oauth2/token/ and sent via Authorization: Bearer. The Help Center reiterates the two methods (API keys and OAuth).
- MCP: Close provides an official MCP server at https://mcp.close.com/mcp. The MCP server supports OAuth 2.0 Dynamic Client Registration and can also accept an API key via Close-API-Key plus Close-Scope headers to control tool access. The developer portal mentions “MCP Server” as part of the platform.
- Breadth: The developer portal lists core areas (REST API, webhooks & events, reporting, sequences, bulk actions, email/SMS, integrations), indicating a broad CRM surface.

2) Production Access Rubric application:
- Evidence of credential enablement exists: “API keys can be created and managed in your Close account under Settings → Developer → API Keys” and “create an OAuth app to get your Client ID and Client Secret.”
- There is no explicit statement that production credentials are self-serve without being a paying customer or approval. The marketing site says “Start free… No credit card required,” which implies a trial but the rubric notes that a trial alone does not prove self-serve production. No page states that production API use is available without manual approval or paid plans.
- Therefore, lacking explicit proof of self-serve production entitlement, classify access as Gated per rubric.

3) Decisions:
- auth_methods: API Key and Basic Auth (for API key usage) and OAuth2 (for OAuth 2.0). Do not add Bearer Token separately because it is part of OAuth2 handling.
- api_type: REST is the dominant public surface; an official MCP server also exists. 
- existing_mcp: Official, because Close documents and hosts its MCP server.
- access_model: Gated, due to no explicit self-serve production guarantee despite easy key/app creation and a free trial.
- buildability: Moderate — clear REST and OAuth docs and an official MCP, but uncertainty around production entitlement/payment; likely need an active Close org.
- recommended_next_action: Needs Outreach — confirm plan/production access requirements and any partner/listing processes before shipping.

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - Docs show you can create API keys and OAuth apps in-account, but no explicit statement of self-serve production access without paid plans or approval; a free trial exists but does not prove production entitlement.
- recommended_next_action: **Needs Outreach**
- confidence: **0.64**

## Evidence URLs
- https://developer.close.com/api/overview/api-key-authentication
- https://developer.close.com/api/overview/oauth-authentication
- https://help.close.com/integrations/api-keys-oauth
- https://help.close.com/docs/mcp-server
- https://developer.close.com
- https://close.com

## Generated record
```json
{
  "app": "Close",
  "category": "CRM",
  "one_liner": "Close offers a REST API and official MCP server with API key or OAuth2, but production use likely requires a paid org.",
  "auth_methods": [
    "API Key",
    "Basic Auth",
    "OAuth2"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Docs show you can create API keys and OAuth apps in-account, but no explicit statement of self-serve production access without paid plans or approval; a free trial exists but does not prove production entitlement."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "No explicit proof of self-serve production access; likely requires an active (paid) Close org to use API in production.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://developer.close.com/api/overview/api-key-authentication",
    "https://developer.close.com/api/overview/oauth-authentication",
    "https://help.close.com/integrations/api-keys-oauth",
    "https://help.close.com/docs/mcp-server",
    "https://developer.close.com",
    "https://close.com"
  ],
  "confidence": 0.64,
  "verification_status": "Auto",
  "slug": "close",
  "primary_docs_url": "https://help.close.com/integrations/api-keys-oauth",
  "rate_limit_note": "Not specified in the cited documentation.",
  "last_verified": "2026-08-17"
}
```

<!-- final-state:start -->
## Final pipeline state
_Updated 2026-08-18 by current human handcheck correction; this supersedes earlier key decisions._

```json
{
  "app": "Close",
  "category": "CRM",
  "one_liner": "Close offers a REST API and official MCP server with API key or OAuth2, but production use likely requires a paid org.",
  "auth_methods": [
    "API Key",
    "Basic Auth",
    "OAuth2"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Close provides a temporary trial; continued production API and MCP use requires a paid Close subscription."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "Production credentials require an existing paid customer account.",
  "recommended_next_action": "Partner-Gated",
  "evidence_urls": [
    "https://developer.close.com/api/overview/api-key-authentication",
    "https://developer.close.com/api/overview/oauth-authentication",
    "https://developer.close.com/mcp",
    "https://close.com/pricing"
  ],
  "confidence": 0.64,
  "verification_status": "Hand-Checked",
  "slug": "close",
  "primary_docs_url": "https://developer.close.com/api/overview/api-key-authentication",
  "rate_limit_note": "Not specified in the cited documentation.",
  "last_verified": "2026-08-17"
}
```
<!-- final-state:end -->

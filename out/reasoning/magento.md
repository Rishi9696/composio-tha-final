# Magento (Adobe Commerce) - synthesis reasoning
_generated 2026-08-17 | model openai:gpt-5_

## Research trace
- queries: ["Magento (Adobe Commerce) official API authentication developer documentation", "Magento (Adobe Commerce) API production access approval credentials official documentation", "Magento (Adobe Commerce) official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://developer.adobe.com/commerce | HTTP 200 | hint | topics=api,access
- https://developer.adobe.com/commerce/webapi/get-started/authentication/gs-authentication-oauth | HTTP 200 | search_result | topics=api,auth
- https://developer.adobe.com/commerce/webapi/get-started/ | HTTP 200 | search_result | topics=api,auth
- https://developer.adobe.com/commerce/webapi/get-started/authentication/ | HTTP 200 | search_result | topics=api,auth
- https://developer.adobe.com | HTTP 200 | derived_guess | topics=api
- https://developers.adobe.com | HTTP 200 | derived_guess | topics=api

## Model reasoning
1) Evidence states: Adobe Commerce/Magento exposes web APIs supporting REST, GraphQL, and SOAP. Docs list three auth types: third‑party apps use OAuth 1.0a; mobile apps use tokens; admins/customers authenticate with login credentials. You must enable web services in Admin and create an Integration; permissions are controlled via acl.xml/webapi.xml. The OAuth 1.0a flow is detailed: merchant creates an integration, Commerce generates consumer key/secret, app requests a short‑lived request token and exchanges it for a long‑lived access token (revocable). Sources: “Support for GraphQL, REST and SOAP. Three types of authentication: Third‑party applications authenticate with OAuth 1.0a. Mobile applications authenticate using tokens… You must register a web service on Admin… Create a new integration on Admin.” and “As the process of registering the integration proceeds, Commerce creates the tokens… It first creates a request token… Access tokens are long‑lived…”. The Adobe Commerce developer landing page describes API‑first capabilities and provides the main entry to developer docs (access topic). 2) Production Access Rubric: The Getting Started page explicitly instructs that a merchant/admin can create integrations and thereby issue credentials (“You must register a web service on Admin… Create a new integration on Admin.”). The OAuth page confirms tokens are created during integration registration. There is no mention of vendor approval, partnership, business verification, or paid plan gating to use the APIs on a Commerce instance. Therefore production access is self‑serve at the store level (credentials are issued by the merchant admin), not vendor‑gated. 3) From this: auth_methods = Other Token (OAuth 1.0a) and Bearer Token (token‑based); api_type = REST as the dominant surface (with GraphQL/SOAP also supported); existing_mcp = Community (CData MCP Server for Adobe Commerce); access_model = Self‑Serve (per‑instance admin can create integrations/tokens; no vendor approval indicated); buildability = Moderate (clear docs, but OAuth 1.0a app setup and needing store admin access); main_blocker = needing access to a Commerce instance/admin to create an integration/token; recommended_next_action = Build Now; rate limits not documented in fetched pages.

## Key decisions
- buildability: **Moderate**
- access_model: **Self-Serve** - Credentials are issued per Commerce/Magento instance by a merchant admin via Admin > System > Extensions > Integration; docs show creating integrations and tokens with no vendor approval required.
- recommended_next_action: **Build Now**
- confidence: **0.69**

## Evidence URLs
- https://developer.adobe.com/commerce/webapi/get-started/
- https://developer.adobe.com/commerce/webapi/get-started/authentication/
- https://developer.adobe.com/commerce/webapi/get-started/authentication/gs-authentication-oauth
- https://developer.adobe.com/commerce
- https://cdn.cdata.com/help/BZK/mcp/pg_mcpintro.htm?utm_source=openai

## Generated record
```json
{
  "app": "Magento (Adobe Commerce)",
  "category": "Commerce",
  "one_liner": "Adobe Commerce offers REST/GraphQL APIs with OAuth 1.0a and token auth; per-store access is self-serve via Admin.",
  "auth_methods": [
    "Other Token",
    "Bearer Token"
  ],
  "access_model": {
    "kind": "Self-Serve",
    "note": "Credentials are issued per Commerce/Magento instance by a merchant admin via Admin > System > Extensions > Integration; docs show creating integrations and tokens with no vendor approval required."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Community",
  "composio_toolkit": "No",
  "buildability": "Moderate",
  "main_blocker": "Requires access to a Commerce instance and admin rights to create an integration and generate tokens.",
  "recommended_next_action": "Build Now",
  "evidence_urls": [
    "https://developer.adobe.com/commerce/webapi/get-started/",
    "https://developer.adobe.com/commerce/webapi/get-started/authentication/",
    "https://developer.adobe.com/commerce/webapi/get-started/authentication/gs-authentication-oauth",
    "https://developer.adobe.com/commerce",
    "https://cdn.cdata.com/help/BZK/mcp/pg_mcpintro.htm?utm_source=openai"
  ],
  "confidence": 0.69,
  "verification_status": "Auto",
  "slug": "magento",
  "primary_docs_url": "https://developer.adobe.com/commerce/webapi/get-started/authentication/gs-authentication-oauth",
  "rate_limit_note": "No explicit rate limits are documented in the fetched pages.",
  "last_verified": "2026-08-17"
}
```

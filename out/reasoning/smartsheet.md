# Smartsheet - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Smartsheet official API authentication developer documentation", "Smartsheet API production access approval credentials official documentation", "Smartsheet official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://smartsheet.com/developers | HTTP 200 | hint | topics=api,auth,mcp
- https://developers.smartsheet.com/api/smartsheet/guides/basics/authentication | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://www.smartsheet.com/pricing?utm_source=openai | HTTP 200 | search_result | topics=api,access,mcp
- https://developers.smartsheet.com/api/smartsheet/introduction | HTTP 200 | search_result | topics=api,auth,mcp
- https://developer.smartsheet.com | HTTP 0 | derived_guess | topics=none
- https://developers.smartsheet.com | HTTP 200 | derived_guess | topics=api,auth,mcp

## Model reasoning
1) Evidence summary:
- API auth: The Authentication guide states, "The API authenticates using access tokens (API keys). You can generate access tokens in the Smartsheet UI... Each API request requires passing in an access token as the Bearer value" and notes Smartsheet uses a "3-legged" OAuth 2.0 process for user-consent scenarios (developers.smartsheet.com/api/smartsheet/guides/basics/authentication). The MCP install guide lists prerequisites: a "Valid Smartsheet API token, unless you're connecting an AI tool that supports Smartsheet's OAuth" (developers.smartsheet.com/ai-mcp/smartsheet/install-the-smartsheet-mcp-server).
- API surface: The API introduction confirms the REST base URL and broad resources, SDKs, and explicitly: "Required plan: Business, Enterprise, or Advanced Work Management" (developers.smartsheet.com/api/smartsheet/introduction). The MCP server introduction and install pages also show "Required plan: Business, Enterprise, or Advanced Work Management" (developers.smartsheet.com/ai-mcp/smartsheet/mcp-server; developers.smartsheet.com/ai-mcp/smartsheet/install-the-smartsheet-mcp-server). MCP tools require OAuth scopes and are subject to API rate limits (developers.smartsheet.com/ai-mcp/smartsheet/mcp-server-tools). An official hosted-connection article introduces the Smartsheet MCP server for AI clients (smartsheet.com/content-center/product-insights/product-updates/introducing-smartsheet-mcp-server). The pricing page provides official plan context (smartsheet.com/pricing).
2) Production Access Rubric application:
- Gating evidence: The developer docs repeatedly state "Required plan: Business, Enterprise, or Advanced Work Management" for both REST API and MCP, indicating production access is tied to paid plans, not free self-serve. The hosted-connection MCP article corroborates an official connection surface, and the pricing page is the official plans reference. Token generation in UI shows credential mechanics but not free production entitlement.
3) Decisions derived:
- Auth methods: API Key (personal access token) and OAuth2 are documented. 
- API type: REST is the dominant public API; MCP is an additional official surface built atop it.
- Existing MCP: Official, published by Smartsheet.
- Access model: Gated, because Business/Enterprise/AWM plans are required.
- Buildability: Moderate due to clear docs/SDKs but plan requirement and OAuth app setup for user-consent flows.
- Next action: Needs Outreach to secure an eligible paid plan and register/configure credentials.

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - Both REST API and the official MCP require a paid Smartsheet plan (Business, Enterprise, or Advanced Work Management).
- recommended_next_action: **Needs Outreach**
- confidence: **0.86**

## Evidence URLs
- https://developers.smartsheet.com/api/smartsheet/guides/basics/authentication
- https://developers.smartsheet.com/api/smartsheet/introduction
- https://developers.smartsheet.com/ai-mcp/smartsheet/mcp-server
- https://developers.smartsheet.com/ai-mcp/smartsheet/install-the-smartsheet-mcp-server
- https://developers.smartsheet.com/ai-mcp/smartsheet/mcp-server-tools
- https://www.smartsheet.com/content-center/product-insights/product-updates/introducing-smartsheet-mcp-server
- https://www.smartsheet.com/pricing?utm_source=openai

## Generated record
```json
{
  "app": "Smartsheet",
  "category": "Productivity/PM",
  "one_liner": "Smartsheet offers a robust REST API and official MCP, but production access requires a paid Business+ plan.",
  "auth_methods": [
    "OAuth2",
    "API Key"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Both REST API and the official MCP require a paid Smartsheet plan (Business, Enterprise, or Advanced Work Management)."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "No",
  "buildability": "Moderate",
  "main_blocker": "Access to production API/MCP requires a paid Business/Enterprise/Advanced Work Management plan.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://developers.smartsheet.com/api/smartsheet/guides/basics/authentication",
    "https://developers.smartsheet.com/api/smartsheet/introduction",
    "https://developers.smartsheet.com/ai-mcp/smartsheet/mcp-server",
    "https://developers.smartsheet.com/ai-mcp/smartsheet/install-the-smartsheet-mcp-server",
    "https://developers.smartsheet.com/ai-mcp/smartsheet/mcp-server-tools",
    "https://www.smartsheet.com/content-center/product-insights/product-updates/introducing-smartsheet-mcp-server",
    "https://www.smartsheet.com/pricing?utm_source=openai"
  ],
  "confidence": 0.86,
  "verification_status": "Auto",
  "slug": "smartsheet",
  "primary_docs_url": "https://developers.smartsheet.com/api/smartsheet/guides/basics/authentication",
  "rate_limit_note": "MCP tools and underlying REST API are subject to Smartsheet API rate limits and standard limitations.",
  "last_verified": "2026-08-18"
}
```

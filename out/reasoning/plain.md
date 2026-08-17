# Plain - synthesis reasoning
_generated 2026-08-17 | model openai:gpt-5_

## Research trace
- queries: ["Plain official API authentication developer documentation", "Plain API production access approval credentials official documentation", "Plain official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://plain.com | HTTP 200 | hint | topics=api
- https://developer.hellosign.com/api/reference/authentication/ | HTTP 0 | search_result | topics=none
- https://developer.va.gov/production-access | HTTP 200 | search_result | topics=access
- https://developer.zendesk.com/documentation/conversations/getting-started/api-authentication/ | HTTP 200 | search_result | topics=api,auth,access
- https://developer.plain.com | HTTP 0 | derived_guess | topics=none
- https://help.plain.com/article/api-quickstart | HTTP 200 | browser_verified_summary | topics=api,auth,access

## Model reasoning
1) Evidence states: (a) API surface/auth: “Plain provides a GraphQL API. A workspace user can generate an API key from Settings, send it as a Bearer credential, and use Plain's API explorer after setting up a workspace.” (help.plain.com/article/api-quickstart). (b) MCP: “The Plain MCP server at https://mcp.plain.com/mcp… You authenticate with your existing Plain account… No API keys needed… Set authentication to OAuth, then… complete the login flow.” (help.plain.com/article/mcp-server). (c) Marketing site mentions an API but no auth specifics (plain.com). 2) Production Access Rubric: The docs explicitly show that a workspace user can self-generate an API key and immediately use the API explorer; and the MCP server uses an OAuth login with an existing account. There is no mention of manual approval, partnership, or paid-plan gating. In absence of any stated approval step and with explicit credential self-generation, classify as Self-Serve based on the provided lines. 3) Therefore: auth_methods are API Key (GraphQL) and OAuth2 (MCP). api_type is GraphQL (with an official MCP surface available). existing_mcp is Official. Access model is Self-Serve, citing the self-generation of API keys and OAuth login. Buildability is Easy given clear quickstarts and credential paths. Next action: Build Now.

## Key decisions
- buildability: **Easy**
- access_model: **Self-Serve** - Docs show a workspace user can generate an API key and use it, and the MCP server uses OAuth login with an existing Plain account—no approval or paid gating is mentioned.
- recommended_next_action: **Build Now**
- confidence: **0.55**

## Evidence URLs
- https://help.plain.com/article/api-quickstart
- https://help.plain.com/article/mcp-server
- https://plain.com

## Generated record
```json
{
  "app": "Plain",
  "category": "Support",
  "one_liner": "Plain offers a self-serve GraphQL API and official MCP server with API key and OAuth login.",
  "auth_methods": [
    "API Key",
    "OAuth2"
  ],
  "access_model": {
    "kind": "Self-Serve",
    "note": "Docs show a workspace user can generate an API key and use it, and the MCP server uses OAuth login with an existing Plain account—no approval or paid gating is mentioned."
  },
  "api_type": "GraphQL",
  "api_breadth": "Moderate",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Easy",
  "main_blocker": "None evident beyond needing a Plain workspace/account to create credentials.",
  "recommended_next_action": "Build Now",
  "evidence_urls": [
    "https://help.plain.com/article/api-quickstart",
    "https://help.plain.com/article/mcp-server",
    "https://plain.com"
  ],
  "confidence": 0.55,
  "verification_status": "Auto",
  "slug": "plain",
  "primary_docs_url": "https://help.plain.com/article/api-quickstart",
  "rate_limit_note": "No rate limit details are provided in the cited docs.",
  "last_verified": "2026-08-17"
}
```

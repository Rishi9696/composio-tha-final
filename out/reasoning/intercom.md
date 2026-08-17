# Intercom - synthesis reasoning
_generated 2026-08-17 | model openai:gpt-5_

## Research trace
- queries: ["Intercom official API authentication developer documentation", "Intercom API production access approval credentials official documentation", "Intercom official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://intercom.com | HTTP 200 | hint | topics=access
- https://developers.intercom.com/docs/build-an-integration/learn-more/authentication | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://www.intercom.com/pricing?tab=1 | HTTP 200 | search_result | topics=access
- https://developers.intercom.com/docs/references/preview/rest-api/api.intercom.io | HTTP 200 | search_result | topics=api
- https://developer.intercom.com | HTTP 0 | derived_guess | topics=none
- https://developers.intercom.com | HTTP 200 | derived_guess | topics=api,access

## Model reasoning
1) API/MCP/auth evidence: Intercom’s auth docs state: “To access the Intercom API… An Access Token is for… a private app… OAuth is for… a public app.” and “We provide you with an Access Token as soon as you create an app on your workspace.” This confirms two independent auth paths for the REST API: a static access token for private use and OAuth2 for public apps. The REST API reference describes broad resources (contacts, companies, conversations, articles, etc.), confirming a REST surface. Intercom publishes an official MCP surface: the MCP guide says “The Intercom MCP server is available for US and EU hosted workspaces,” and the Help Center article for “Fin Agent API: MCP Server” says it is “currently in beta,” with two connection modes (Teammate via a Fin Agent API key; End-user via a Messenger JWT) and endpoints at api.intercom.io/fin/mcp. The Intercom developers homepage mentions a “free development workspace to test and publish your app.” 2) Production Access rubric: The pricing page presents paid plans and “Start free trial,” with no evidence of a free, self-serve production tier. The developers page explicitly offers a “free development workspace,” implying non-production. There is no statement that a new developer can obtain production credentials without being a paying customer. The Fin Agent API MCP Server is “currently in beta,” indicating potential manual/feature gating. Therefore, production access is Gated under the rubric. 3) Conclusions: Auth methods include OAuth2 (public apps), a static access token for private REST (mapped to Bearer Token per controlled vocab), and an API Key for the Fin Agent MCP server. Dominant API type is REST; breadth is Broad. There is an Official MCP. Buildability is Moderate (clear docs and self-serve dev workspace, but production appears pay/feature-gated). Recommended action: Needs Outreach to secure a paid workspace and, if relevant, beta MCP access.

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - Intercom provides an access token upon app creation in a workspace and supports OAuth for public apps, but pricing shows paid plans with a free trial and the developers site mentions a free development workspace (non‑production). No evidence of self‑serve, free production entitlement. The Fin Agent API MCP Server is in beta and may require enablement.
- recommended_next_action: **Needs Outreach**
- confidence: **0.68**

## Evidence URLs
- https://developers.intercom.com/docs/build-an-integration/learn-more/authentication
- https://developers.intercom.com/docs/references/preview/rest-api/api.intercom.io
- https://developers.intercom.com
- https://developers.intercom.com/docs/guides/mcp
- https://www.intercom.com/help/en/articles/15481203-fin-agent-api-mcp-server
- https://www.intercom.com/pricing?tab=1

## Generated record
```json
{
  "app": "Intercom",
  "category": "Support",
  "one_liner": "Intercom offers a broad REST API and official MCP; production access appears gated by paid workspace and beta MCP.",
  "auth_methods": [
    "OAuth2",
    "Bearer Token",
    "API Key"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Intercom provides an access token upon app creation in a workspace and supports OAuth for public apps, but pricing shows paid plans with a free trial and the developers site mentions a free development workspace (non‑production). No evidence of self‑serve, free production entitlement. The Fin Agent API MCP Server is in beta and may require enablement."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "Production use appears to require a paid Intercom workspace and the Fin Agent API MCP server is in beta.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://developers.intercom.com/docs/build-an-integration/learn-more/authentication",
    "https://developers.intercom.com/docs/references/preview/rest-api/api.intercom.io",
    "https://developers.intercom.com",
    "https://developers.intercom.com/docs/guides/mcp",
    "https://www.intercom.com/help/en/articles/15481203-fin-agent-api-mcp-server",
    "https://www.intercom.com/pricing?tab=1"
  ],
  "confidence": 0.68,
  "verification_status": "Auto",
  "slug": "intercom",
  "primary_docs_url": "https://developers.intercom.com/docs/build-an-integration/learn-more/authentication",
  "rate_limit_note": "Rate limits not specified in the cited docs; check the REST API reference for current limits.",
  "last_verified": "2026-08-17"
}
```

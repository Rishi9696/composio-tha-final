# Linear - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Linear official API authentication developer documentation", "Linear API production access approval credentials official documentation", "Linear official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://developers.linear.app | HTTP 200 | hint | topics=api,auth,access
- https://linear.app/developers/oauth-2-0-authentication | HTTP 200 | search_result | topics=api,auth,access
- https://aitoolsatlas.ai/tools/linear-api/pricing | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://mindcloud.co/docs/universal/rest/linear/1.0.84/introduction/authentication | HTTP 200 | search_result | topics=api,auth,access
- https://developer.linear.app | HTTP 200 | derived_guess | topics=api,auth,access
- https://docs.linear.app | HTTP 200 | derived_guess | topics=access

## Model reasoning
1) Evidence states: • Developers site: “Use OAuth 2.0 or personal API keys to authenticate your requests to the Linear API” and provides GraphQL API docs and a TypeScript SDK (https://developers.linear.app). • OAuth 2.0 page documents creating an OAuth app, scopes, and authorization URL (https://linear.app/developers/oauth-2-0-authentication). • MCP page states Linear hosts a centrally managed, authenticated remote MCP server; setup uses OAuth 2.1 with dynamic client registration and can also authenticate with a bearer token or Linear API key (https://linear.app/docs/mcp). • A third‑party pricing page claims a Free plan includes “API and webhook access” (https://aitoolsatlas.ai/tools/linear-api/pricing). 2) Production Access Rubric application: There is no explicit statement in the official Linear docs confirming that a new developer can obtain production credentials without approval or payment. The only explicit “free API access” claim comes from a third‑party pricing page, not official documentation. Therefore, per the rubric, absent official proof of self‑serve production entitlement, classify as Gated. 3) Conclusions consistent with 1–2: Auth methods supported are OAuth2 and personal API keys on the GraphQL API, and MCP mentions bearer token/API key auth; the dominant API is GraphQL; there is an official MCP. Access model is Gated due to lack of official confirmation of self‑serve production access. Buildability is Moderate (docs are clear, but production access terms need confirmation). Recommended next action: Needs Outreach to confirm production access/plan requirements.

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - Official docs show OAuth apps and personal API keys but do not explicitly confirm self-serve production access; confirm plan/approval requirements with Linear.
- recommended_next_action: **Needs Outreach**
- confidence: **0.56**

## Evidence URLs
- https://developers.linear.app
- https://linear.app/developers/oauth-2-0-authentication
- https://linear.app/docs/mcp
- https://aitoolsatlas.ai/tools/linear-api/pricing

## Generated record
```json
{
  "app": "Linear",
  "category": "Productivity/PM",
  "one_liner": "Linear offers a GraphQL API and official MCP; production access terms need confirmation from Linear.",
  "auth_methods": [
    "OAuth2",
    "API Key",
    "Bearer Token"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Official docs show OAuth apps and personal API keys but do not explicitly confirm self-serve production access; confirm plan/approval requirements with Linear."
  },
  "api_type": "GraphQL",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "No explicit official confirmation of self-serve production credentials or plan eligibility.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://developers.linear.app",
    "https://linear.app/developers/oauth-2-0-authentication",
    "https://linear.app/docs/mcp",
    "https://aitoolsatlas.ai/tools/linear-api/pricing"
  ],
  "confidence": 0.56,
  "verification_status": "Auto",
  "slug": "linear",
  "primary_docs_url": "https://linear.app/developers/oauth-2-0-authentication",
  "rate_limit_note": "Rate limiting is documented on the Developers site; specific thresholds not confirmed in fetched pages.",
  "last_verified": "2026-08-18"
}
```

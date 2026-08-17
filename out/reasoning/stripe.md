# Stripe - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Stripe official API authentication developer documentation", "Stripe API production access approval credentials official documentation", "Stripe official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://stripe.com/docs/api | HTTP 200 | search_result | topics=api,auth,access
- https://docs.stripe.com/api/authentication?javascript=false&lang=curl | HTTP 200 | search_result | topics=api,auth,access
- https://stripe.com/pricing | HTTP 200 | search_result | topics=api,auth,access
- https://developer.stripe.com | HTTP 0 | derived_guess | topics=none
- https://developers.stripe.com | HTTP 0 | derived_guess | topics=none
- https://docs.stripe.com | HTTP 200 | derived_guess | topics=api,auth,access

## Model reasoning
1) API/MCP/auth from evidence: The API reference states “The Stripe API is organized around REST” and notes you can use sandboxes, with the API key determining sandbox vs live mode (stripe.com/docs/api). The authentication page shows Stripe uses API keys, with test and live keys, and includes examples using HTTP Basic (-u sk_...) and Authorization: Bearer patterns (docs.stripe.com/api/authentication). For MCP, Stripe documents an official MCP server in public preview to let agents interact with the Stripe API (docs.stripe.com/mcp). The MCP GitHub entry states “Stripe hosts a remote MCP server at https://mcp.stripe.com. This allows secure MCP client access via OAuth.” (github.com/mcp/com.stripe/mcp). 2) Production Access Rubric: The API docs explicitly mention sandboxes and test vs live keys (“You can use the Stripe API in sandboxes… The API key … determines whether the request runs in live mode or in a sandbox.”) but there is no explicit statement that a new developer can obtain live/production credentials self‑serve without approval. Therefore, there’s no evidence proving self‑serve production entitlement. The MCP page is “Public preview,” and the GitHub notes OAuth sign‑in, but again no statement about self‑serve production access. By the rubric, absent explicit proof of self‑serve production, classify as Gated. 3) Conclusions: Auth methods include API Key and (as shown in docs) HTTP Basic; Bearer is just the header transport for the API key so not listed separately. MCP uses OAuth2 per the GitHub entry. The dominant API is REST, breadth is broad. MCP is Official. Buildability is Moderate (clear docs and easy sandbox, but production access lacks explicit self‑serve proof). Recommended action: Needs Outreach to confirm/enable production (live) access.

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - Docs clearly show sandbox/test keys are available, but provide no explicit claim that live/production access is self‑serve. MCP is public preview with OAuth sign‑in to a Stripe account.
- recommended_next_action: **Needs Outreach**
- confidence: **0.66**

## Evidence URLs
- https://stripe.com/docs/api
- https://docs.stripe.com/api/authentication?javascript=false&lang=curl
- https://docs.stripe.com/mcp
- https://github.com/mcp/com.stripe/mcp

## Generated record
```json
{
  "app": "Stripe",
  "category": "Fintech",
  "one_liner": "Stripe provides a broad REST API with API keys and an official MCP server; production access appears gated.",
  "auth_methods": [
    "API Key",
    "Basic Auth",
    "OAuth2"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Docs clearly show sandbox/test keys are available, but provide no explicit claim that live/production access is self‑serve. MCP is public preview with OAuth sign‑in to a Stripe account."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "No explicit documentation confirming self‑serve production (live) access beyond sandbox/test mode.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://stripe.com/docs/api",
    "https://docs.stripe.com/api/authentication?javascript=false&lang=curl",
    "https://docs.stripe.com/mcp",
    "https://github.com/mcp/com.stripe/mcp"
  ],
  "confidence": 0.66,
  "verification_status": "Auto",
  "slug": "stripe",
  "primary_docs_url": "https://docs.stripe.com/api/authentication?javascript=false&lang=curl",
  "rate_limit_note": "Not specified in the cited pages.",
  "last_verified": "2026-08-18"
}
```

# Plaid - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Plaid official API authentication developer documentation", "Plaid API production access approval credentials official documentation", "Plaid official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://plaid.com/docs | HTTP 200 | hint | topics=api,auth,access,mcp
- https://plaid.com/plaid-exchange/docs/authentication/ | HTTP 200 | search_result | topics=api,auth,access
- https://support.plaid.com/hc/en-us/articles/16194695660311-Can-I-use-Plaid-for-free | HTTP 200 | search_result | topics=api,auth,access
- https://plaid.com/docs/api/products/auth/ | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://developer.plaid.com | HTTP 0 | derived_guess | topics=none
- https://developers.plaid.com | HTTP 0 | derived_guess | topics=none

## Model reasoning
1) Evidence on API, MCP, and auth: The Plaid docs home shows an API Reference and many product endpoints (e.g., Auth) and prominently includes a “Get API Keys” entry, indicating API key-based credentials are issued via the Dashboard. The Auth product page lists REST endpoints such as /auth/get and /auth/verify, confirming a REST surface. The Plaid MCP resources page states Plaid offers two MCP servers, including a remote, Plaid-hosted Dashboard MCP server that “provides Production diagnostics and analytics tools” and that it “works with Production data only,” establishing an official MCP surface hosted by Plaid. The Plaid Exchange Authentication page describes an OAuth 2.0 authorization and token flow for data partners and explicitly instructs partners to “issue Plaid a client ID and client secret” and “provide them to your Plaid contact,” which is about Plaid authenticating to a partner’s OAuth server, not developer auth for Plaid’s public API. No fetched page provides detailed API request auth mechanics beyond the presence of “Get API Keys.”
2) Production Access Rubric application: The support article states: “Plaid also offers a free Trial plan … which lets you use Plaid with real production data… Trial plans support up to 10 Production Items … prior to full Production approval … To create additional Items beyond the 10-Item limit, you’ll need to upgrade to a paid plan.” This shows limited, temporary production access with later need for approval/paid upgrade, so full production use is gated. The Exchange auth page also requires sharing credentials with “your Plaid contact,” implying manual engagement for that surface.
3) Conclusions: Auth methods evidenced for the public API are API Key (from “Get API Keys” in docs). The dominant API type is REST (API reference and endpoints). There is an official vendor-hosted MCP (Dashboard MCP server). Access model is Gated due to the need for full Production approval and/or paid upgrade beyond a limited trial. Buildability is Hard since production requires approval/paid plan despite clear docs and sandbox/trial. Recommended next action is Needs Outreach to obtain production approval/pricing. Evidence about rate limits was not present.

## Key decisions
- buildability: **Hard**
- access_model: **Gated** - Support docs describe a Trial with up to 10 Production Items prior to full Production approval and require a paid upgrade beyond that; Exchange OAuth setup also references working with a Plaid contact.
- recommended_next_action: **Needs Outreach**
- confidence: **0.64**

## Evidence URLs
- https://plaid.com/docs
- https://plaid.com/docs/api/products/auth/
- https://support.plaid.com/hc/en-us/articles/16194695660311-Can-I-use-Plaid-for-free
- https://plaid.com/docs/resources/mcp/
- https://plaid.com/plaid-exchange/docs/authentication/

## Generated record
```json
{
  "app": "Plaid",
  "category": "Fintech",
  "one_liner": "Plaid offers a broad REST API and official MCP, but full production access requires approval or a paid plan.",
  "auth_methods": [
    "API Key"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Support docs describe a Trial with up to 10 Production Items prior to full Production approval and require a paid upgrade beyond that; Exchange OAuth setup also references working with a Plaid contact."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "No",
  "buildability": "Hard",
  "main_blocker": "Full production use requires approval and/or a paid upgrade beyond a limited Trial plan.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://plaid.com/docs",
    "https://plaid.com/docs/api/products/auth/",
    "https://support.plaid.com/hc/en-us/articles/16194695660311-Can-I-use-Plaid-for-free",
    "https://plaid.com/docs/resources/mcp/",
    "https://plaid.com/plaid-exchange/docs/authentication/"
  ],
  "confidence": 0.64,
  "verification_status": "Auto",
  "slug": "plaid",
  "primary_docs_url": "https://plaid.com/docs/api/products/auth/",
  "rate_limit_note": "No rate limit details found in the fetched documentation.",
  "last_verified": "2026-08-18"
}
```

## Risk seed (withheld from synthesis)
This prior was retained only for audit sampling and was not shown to the model.
```json
{
  "access_model": "Self-Serve",
  "recommended_next_action": "Build Now",
  "main_blocker": "Free/instant sandbox is self-serve, but PRODUCTION access requires a Plaid approval/review process.",
  "note": "Capture as 'self-serve trial, gated production', not a flat label."
}
```

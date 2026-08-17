# Sherlock - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Sherlock official API authentication developer documentation", "Sherlock API production access approval credentials official documentation", "Sherlock official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://github.com/sherlock-project/sherlock | HTTP 200 | hint | topics=access,mcp
- https://docs.c-core.app/docs/legacy/sherlock/sherlock-authorization | HTTP 200 | search_result | topics=api,auth,access
- https://www.sherlocks.ai/pricing | HTTP 200 | search_result | topics=access
- https://www.usesherlock.ai/pricing | HTTP 200 | search_result | topics=access
- https://developer.github.com | HTTP 200 | derived_guess | topics=api,auth
- https://developers.github.com | HTTP 200 | derived_guess | topics=none

## Model reasoning
1) What the evidence states: The C‑CORE legacy “Sherlock Authorization Strategy” describes internal auth for a Sherlock platform using AWS Cognito with email/password or Google ID and token-based access containing scopes and groups; it mentions “Client API Access” and “Public API Access” but provides no endpoints, credential issuance steps, or developer signup for an API. The sherlock-project GitHub repo is an open-source CLI/tooling repo, not a hosted API or MCP. The sherlocks.ai and usesherlock.ai pricing pages describe product plans, self-serve onboarding, and Slack/Microsoft Teams integrations but do not mention a public developer API or keys. The MCP listing “sherlock-mcp” is a community server for domain management, unrelated to these Sherlock products and not vendor-hosted. 2) Production Access Rubric: There is no statement that a new developer can obtain production API credentials self-serve. Pricing pages note “Self-serve onboarding” for the product (“Start free with 30 investigations per month… Slack & Microsoft Teams integration”), but this is not evidence of API production entitlement. No page documents API credential generation or production approval. Hence, no proof of Self‑Serve; default to Gated. 3) Conclusions: With no confirmed public API or official MCP, treat auth as not applicable and api_type as None. existing_mcp is None (the only MCP found is unrelated community). Buildability is Blocked due to lack of a usable hosted API/MCP. Next action: Blocked until vendor publishes API docs or confirms access.

## Key decisions
- buildability: **Blocked**
- access_model: **Gated** - No official public API or credential issuance is documented; pricing pages describe product self-serve onboarding, not API access.
- recommended_next_action: **Blocked**
- confidence: **0.34**

## Evidence URLs
- https://docs.c-core.app/docs/legacy/sherlock/sherlock-authorization
- https://github.com/sherlock-project/sherlock
- https://www.sherlocks.ai/pricing
- https://www.usesherlock.ai/pricing

## Generated record
```json
{
  "app": "Sherlock",
  "category": "Research/Scraping",
  "one_liner": "No official Sherlock API or MCP is documented; integration is blocked pending vendor API details.",
  "auth_methods": [
    "None / Not Applicable"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "No official public API or credential issuance is documented; pricing pages describe product self-serve onboarding, not API access."
  },
  "api_type": "None",
  "api_breadth": "Narrow",
  "existing_mcp": "None",
  "composio_toolkit": "No",
  "buildability": "Blocked",
  "main_blocker": "No official public API/MCP docs or production credential process found.",
  "recommended_next_action": "Blocked",
  "evidence_urls": [
    "https://docs.c-core.app/docs/legacy/sherlock/sherlock-authorization",
    "https://github.com/sherlock-project/sherlock",
    "https://www.sherlocks.ai/pricing",
    "https://www.usesherlock.ai/pricing"
  ],
  "confidence": 0.34,
  "verification_status": "Auto",
  "slug": "sherlock",
  "primary_docs_url": "https://docs.c-core.app/docs/legacy/sherlock/sherlock-authorization",
  "rate_limit_note": "No public rate limit information available.",
  "last_verified": "2026-08-18"
}
```

## Risk seed (withheld from synthesis)
This prior was retained only for audit sampling and was not shown to the model.
```json
{
  "api_type": "None",
  "access_model": "Self-Serve",
  "recommended_next_action": "Blocked",
  "main_blocker": "Open-source CLI tool (username OSINT), not an API service; nothing to integrate via a hosted API."
}
```

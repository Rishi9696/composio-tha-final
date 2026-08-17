# Fathom - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Fathom official API authentication developer documentation", "Fathom API production access approval credentials official documentation", "Fathom official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://fathom.video | HTTP 200 | hint | topics=api,access,mcp
- https://developers.fathom.ai/sdks/oauth | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://www.fathom.ai/pricing | HTTP 200 | search_result | topics=api,access,mcp
- https://developers.fathom.ai/quickstart | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://developer.fathom.video | HTTP 0 | derived_guess | topics=none
- https://developers.fathom.video | HTTP 0 | derived_guess | topics=none

## Model reasoning
1) What the evidence states: - REST API: The Quickstart shows generating an API key in User Settings and calling https://api.fathom.ai/external/v1/meetings with X-Api-Key, noting keys are scoped to the creating user/team sharing (developers.fathom.ai/quickstart). - OAuth2: The OAuth docs state you must register an app to get client credentials and use OAuth 2.0 with supported SDKs; includes token exchange and mentions an "OAuth Rate limits" section (developers.fathom.ai/sdks/oauth). - MCP: Fathom offers an official MCP server at https://api.fathom.ai/mcp and you must authenticate to access meeting data (developers.fathom.ai/mcp-docs). mcpservers.org says the Fathom remote MCP uses OAuth (mcpservers.org/remote-mcp-servers/fathom). pulsemcp.com lists the same remote URL but claims Auth Type = API Key and that it’s paid-only, which conflicts with mcpservers.org (pulsemcp.com/servers/fathom). - Pricing: A free plan is advertised ("Free forever"), but the page does not explicitly mention API/MCP access entitlements (fathom.ai/pricing). 2) Production Access Rubric: There is no explicit statement that production API/MCP access is available self-serve on any plan. Quickstart proves credential generation mechanics (“Head to the API Access section of your User Settings and generate an API key”), but the rubric warns that key-generation alone does not prove production entitlement. The pricing page does not confirm API availability on free or paid tiers. Therefore, there is insufficient evidence to classify as Self-Serve; choose Gated. 3) Decisions: Auth methods = OAuth2 and API Key (both are independently documented). API type = REST (dominant surface; MCP also exists). existing_mcp = Official (vendor-hosted MCP docs). Access model = Gated due to lack of explicit self-serve production proof and contradictory third-party MCP auth/cost notes. Buildability = Moderate (clear docs and quickstart, but production entitlement uncertainty). Recommended next action = Needs Outreach to confirm plan eligibility and production access, and to resolve MCP auth method discrepancy. Confidence reduced due to contradictory MCP auth info.

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - Docs show self-generated API keys and OAuth app registration, but no explicit statement that production API/MCP access is available without approval or a paid plan; pricing page does not confirm API entitlements. MCP auth details conflict across third-party listings.
- recommended_next_action: **Needs Outreach**
- confidence: **0.46**

## Evidence URLs
- https://developers.fathom.ai/quickstart
- https://developers.fathom.ai/sdks/oauth
- https://developers.fathom.ai/mcp-docs
- https://mcpservers.org/remote-mcp-servers/fathom
- https://www.fathom.ai/pricing

## Generated record
```json
{
  "app": "Fathom",
  "category": "AI/Meeting-tools",
  "one_liner": "Fathom provides a REST API (API keys/OAuth) and an official MCP, but production access terms are unclear.",
  "auth_methods": [
    "OAuth2",
    "API Key"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Docs show self-generated API keys and OAuth app registration, but no explicit statement that production API/MCP access is available without approval or a paid plan; pricing page does not confirm API entitlements. MCP auth details conflict across third-party listings."
  },
  "api_type": "REST",
  "api_breadth": "Moderate",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "Unclear production entitlement and plan requirements; conflicting MCP auth method (OAuth vs API key) across sources.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://developers.fathom.ai/quickstart",
    "https://developers.fathom.ai/sdks/oauth",
    "https://developers.fathom.ai/mcp-docs",
    "https://mcpservers.org/remote-mcp-servers/fathom",
    "https://www.fathom.ai/pricing"
  ],
  "confidence": 0.46,
  "verification_status": "Auto",
  "slug": "fathom",
  "primary_docs_url": "https://developers.fathom.ai/sdks/oauth",
  "rate_limit_note": "OAuth docs reference an 'OAuth Rate limits' section, but specific limits are not provided in the fetched excerpts.",
  "last_verified": "2026-08-18"
}
```

## Risk seed (withheld from synthesis)
This prior was retained only for audit sampling and was not shown to the model.
```json
{
  "api_type": "None",
  "main_blocker": "May be webhook/Zapier-only; unclear whether a fully public REST API exists — verify against docs, do not trust memory."
}
```

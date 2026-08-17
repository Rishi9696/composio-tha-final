# Brex - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Brex official API authentication developer documentation", "Brex API production access approval credentials official documentation", "Brex official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://developer.brex.com | HTTP 200 | hint | topics=api,access,mcp
- https://developer.brex.com/guides/partner_authentication | HTTP 200 | search_result | topics=api,auth,access
- https://www.brex.com/pricing | HTTP 200 | search_result | topics=api,access
- https://developer.brex.com/ | HTTP 200 | search_result | topics=api,access,mcp
- https://developers.brex.com | HTTP 200 | derived_guess | topics=api,access,mcp
- https://docs.brex.com | HTTP 0 | derived_guess | topics=none

## Model reasoning
1) What the evidence states: - API surface: The Brex docs say their APIs are REST, JSON over HTTPS, with multiple domains (Accounting, Budgets, Expenses, Fields, Onboarding, Payments, Team, Transactions, Travel, Webhooks). The partner authentication page shows OAuth2/OpenID Connect with production and staging auth base URLs and mentions client credentials for certain flows. The MCP doc confirms an official hosted MCP server at https://api.brex.com/mcp, and that MCP auth is via OAuth, with per-employee authorization after enabling a beta. It also states the standard Developer API uses "admin-provisioned API tokens." - Auth credentials: Evidence explicitly mentions OAuth2/OpenID Connect for partners and MCP, and "admin-provisioned API tokens" for the Developer API. - MCP: There is an official, vendor-hosted remote MCP server documented by Brex. 2) Production Access Rubric: - Partner OAuth is not open to everyone: "Note: This section is only for Brex developer partners." - MCP requires existing account configuration: "An account admin or card admin must accept the Developer API agreement... Enable the beta... Once enabled, all users in your Brex account can connect..." This implies access is tied to being a Brex customer with admin settings, not open self-serve for any new developer. - Pricing shows "Brex API access" as a plan feature, implying you must be a Brex customer/plan holder to use the API in production. There is no explicit statement that a new external developer can obtain production credentials without approval or being a customer. Therefore, by the rubric, production access is Gated. 3) Decisions: Auth methods = OAuth2 (for partners and MCP) and API Key (admin-provisioned API tokens). API type = REST (dominant surface), with an official MCP also available. Existing MCP = Official. Access model = Gated due to partner-only OAuth and account-admin/beta prerequisites; API access is a plan feature. Buildability = Hard (access requires being a customer and/or partner; MCP is beta; partner OAuth gated). Recommended next action = Needs Outreach (become a Brex customer and/or apply for developer partnership to obtain production access for multi-tenant use).

## Key decisions
- buildability: **Hard**
- access_model: **Gated** - Partner OAuth is restricted ("only for Brex developer partners"), and both REST and MCP usage require a Brex account with admin setup (accept Developer API agreement; enable beta for MCP). API access is a plan feature, not an open self-serve production credential.
- recommended_next_action: **Needs Outreach**
- confidence: **0.64**

## Evidence URLs
- https://developer.brex.com/
- https://developer.brex.com/guides/partner_authentication
- https://developer.brex.com/docs/mcp
- https://www.brex.com/pricing

## Generated record
```json
{
  "app": "Brex",
  "category": "Fintech",
  "one_liner": "Brex offers REST APIs and an official MCP server, but production access is gated to customers and partners.",
  "auth_methods": [
    "OAuth2",
    "API Key"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Partner OAuth is restricted (\"only for Brex developer partners\"), and both REST and MCP usage require a Brex account with admin setup (accept Developer API agreement; enable beta for MCP). API access is a plan feature, not an open self-serve production credential."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Hard",
  "main_blocker": "Production access requires being a Brex customer and/or approved developer partner; MCP also requires enabling a beta in-account.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://developer.brex.com/",
    "https://developer.brex.com/guides/partner_authentication",
    "https://developer.brex.com/docs/mcp",
    "https://www.brex.com/pricing"
  ],
  "confidence": 0.64,
  "verification_status": "Auto",
  "slug": "brex",
  "primary_docs_url": "https://developer.brex.com/guides/partner_authentication",
  "rate_limit_note": "Rate limits are documented in the Brex guides, but specific limits are not shown in the cited pages.",
  "last_verified": "2026-08-18"
}
```

## Risk seed (withheld from synthesis)
This prior was retained only for audit sampling and was not shown to the model.
```json
{
  "access_model": "Gated",
  "recommended_next_action": "Needs Outreach",
  "main_blocker": "API access is tied to being a Brex business customer; not self-serve for a solo developer testing."
}
```

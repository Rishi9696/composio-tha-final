# Monday.com - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Monday.com official API authentication developer documentation", "Monday.com API production access approval credentials official documentation", "Monday.com official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://developer.monday.com | HTTP 200 | hint | topics=api,auth,access,mcp
- https://developer.monday.com/api-reference/docs/authentication | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://apis.io/plans/monday-com/monday-com-plans-pricing/ | HTTP 200 | search_result | topics=api,auth,mcp
- https://support.monday.com/hc/en-us/articles/360005144659-Does-monday-com-have-an-API | HTTP 200 | search_result | topics=api,auth,access
- https://developers.monday.com | HTTP 200 | derived_guess | topics=api,auth,access,mcp
- https://docs.monday.com | HTTP 406 | derived_guess | topics=none

## Model reasoning
1) What the evidence states:
- API surface: monday.com offers a platform API “built on GraphQL” for accessing and changing account data (support article explicitly: “Our API is built on GraphQL”). The developer site positions the “Platform API” as the way to connect to monday data and lists extensive capabilities. Separate from the API, monday provides an official hosted MCP server for AI agents, with many documented tools and a security overview. 
- MCP: Support docs say “monday MCP is the hosted server that gives AI tools secure access to your monday.com workspace,” and the dev docs include sections to “Integrate with the monday MCP server,” “Authenticate with an API token,” and “Control MCP access with your own OAuth app,” indicating an official, vendor-hosted MCP surface and auth options.
- Auth credentials: The Authentication docs and MCP sections reference “Authenticate with an API token” (i.e., a personal API token) and using OAuth via “your own OAuth app,” implying Personal Access Token and OAuth2 as independent methods. 
- Rate limits/commercial controls: The support article states: “If you run out of daily API calls, an admin can purchase additional daily API call capacity with an API calls add-on… by reaching out to your account team or support. Each unit adds 25,000 daily API calls.”

2) Production Access Rubric application:
- There is no explicit sentence confirming that a new developer can obtain production credentials self-serve without approval or being a paying customer. The support article indicates manual/commercial gating for higher throughput: “purchase additional daily API call capacity… by reaching out to your account team or support.” This is concrete evidence of manual/commercial gating. Therefore, absent proof of self-serve production entitlement, classify as Gated per the rubric.

3) Decisions flowing from 1–2:
- api_type: GraphQL (dominant public API), with an additional official hosted MCP surface (noted in access_model note).
- auth_methods: Personal Access Token and OAuth2, as independently supported by the docs.
- existing_mcp: Official (vendor-hosted MCP server).
- access_model: Gated due to lack of explicit self-serve production entitlement and evidence of manual/commercial gating for capacity.
- buildability: Moderate — clear docs and well-defined GraphQL/MCP surfaces, but production use may require plan/admin steps.
- recommended_next_action: Needs Outreach — verify plan requirements, obtain necessary admin enablement and, if needed, purchase API call add-ons.

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - Platform GraphQL API and official hosted MCP are documented. No explicit proof of self-serve production credentials; API capacity increases require admin purchase and may involve contacting account team/support. Expect plan/admin enablement for production.
- recommended_next_action: **Needs Outreach**
- confidence: **0.64**

## Evidence URLs
- https://support.monday.com/hc/en-us/articles/360005144659-Does-monday-com-have-an-API
- https://developer.monday.com/api-reference/docs/authentication
- https://developer.monday.com
- https://support.monday.com/hc/en-us/articles/28515034903314-Get-started-with-monday-MCP
- https://developer.monday.com/api-reference/docs/monday-mcp-security-overview

## Generated record
```json
{
  "app": "Monday.com",
  "category": "Productivity/PM",
  "one_liner": "GraphQL API and official MCP with PAT/OAuth; production likely gated by plan and admin approvals.",
  "auth_methods": [
    "OAuth2",
    "Personal Access Token"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Platform GraphQL API and official hosted MCP are documented. No explicit proof of self-serve production credentials; API capacity increases require admin purchase and may involve contacting account team/support. Expect plan/admin enablement for production."
  },
  "api_type": "GraphQL",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "No explicit self-serve production entitlement; plan/admin approval and API call add-on purchases may be required.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://support.monday.com/hc/en-us/articles/360005144659-Does-monday-com-have-an-API",
    "https://developer.monday.com/api-reference/docs/authentication",
    "https://developer.monday.com",
    "https://support.monday.com/hc/en-us/articles/28515034903314-Get-started-with-monday-MCP",
    "https://developer.monday.com/api-reference/docs/monday-mcp-security-overview"
  ],
  "confidence": 0.64,
  "verification_status": "Auto",
  "slug": "monday",
  "primary_docs_url": "https://developer.monday.com/api-reference/docs/authentication",
  "rate_limit_note": "Daily API calls apply; admins can buy 25,000-call units via an add-on by contacting account team or support.",
  "last_verified": "2026-08-18"
}
```

<!-- final-state:start -->
## Final pipeline state
_Updated 2026-08-18 by current handcheck fold; this supersedes earlier key decisions._

```json
{
  "app": "Monday.com",
  "category": "Productivity/PM",
  "one_liner": "GraphQL API and official MCP with PAT/OAuth; production likely gated by plan and admin approvals.",
  "auth_methods": [
    "OAuth2",
    "Personal Access Token"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Platform GraphQL API and official hosted MCP are documented. No explicit proof of self-serve production credentials; API capacity increases require admin purchase and may involve contacting account team/support. Expect plan/admin enablement for production."
  },
  "api_type": "GraphQL",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "No explicit self-serve production entitlement; plan/admin approval and API call add-on purchases may be required.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://support.monday.com/hc/en-us/articles/360005144659-Does-monday-com-have-an-API",
    "https://developer.monday.com/api-reference/docs/authentication",
    "https://developer.monday.com",
    "https://support.monday.com/hc/en-us/articles/28515034903314-Get-started-with-monday-MCP",
    "https://developer.monday.com/api-reference/docs/monday-mcp-security-overview"
  ],
  "confidence": 0.64,
  "verification_status": "Hand-Checked",
  "slug": "monday",
  "primary_docs_url": "https://developer.monday.com/api-reference/docs/authentication",
  "rate_limit_note": "Daily API calls apply; admins can buy 25,000-call units via an add-on by contacting account team or support.",
  "last_verified": "2026-08-18"
}
```
<!-- final-state:end -->

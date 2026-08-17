# Ramp - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Ramp official API authentication developer documentation", "Ramp API production access approval credentials official documentation", "Ramp official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://docs.ramp.com | HTTP 200 | hint | topics=api
- https://docs.ramp.com/developer-api/v1/authorization/scopes | HTTP 200 | search_result | topics=api,auth
- https://support.ramp.com/ramp-pricing-overview/ | HTTP 200 | search_result | topics=access
- https://docs.ramp.com/developer-api/v1/applications | HTTP 200 | search_result | topics=api
- https://developer.ramp.com | HTTP 200 | derived_guess | topics=api,auth,access,mcp
- https://developers.ramp.com | HTTP 0 | derived_guess | topics=none

## Model reasoning
1) What the evidence states: The Ramp developer site promotes “Agent-ready protocols, real-time data access, and modular APIs,” and says you can “Use Ramp’s MCP server and APIs to create agents” (developer.ramp.com). The MCP overview (agents.ramp.com) describes three connection options—MCP, CLI, and API—notes MCP can be instant while API setup can take hours to days, and clarifies that actions are attributed to the authenticated user/agent and “API actions are scoped to the business owner’s identity,” indicating user- or business-scoped authentication. The MCP directory lists an official Ramp MCP server published by ramp-public exposing 16 tools (transactions, receipts, approvals, etc.), confirming an official MCP surface (mcp.directory). Ramp’s pricing page states the core Ramp card and expense management software is free, but does not discuss API credential issuance or production entitlement (support.ramp.com). The docs pages under docs.ramp.com rendered as shells and did not provide content here. No fetched text explicitly details OAuth flows or a key issuance page; however, the agents doc clearly indicates authenticated, role-scoped access tied to a Ramp identity. 2) Production Access Rubric: There is no explicit statement that a new developer can obtain production API credentials self-serve. The agents doc states “API actions are scoped to the business owner’s identity,” implying you must have a Ramp business account, and the site also highlights a technology partner program. No page confirms free, unreviewed, production credential issuance. Therefore, per the rubric (“If you cannot point to a specific evidence sentence confirming free or self-serve PRODUCTION entitlement, choose Gated”), access should be classified as Gated. 3) Decisions: Auth appears to be an authenticated, user/business-scoped connection consistent with OAuth-style flows (though exact grant types are not shown in fetched text). The dominant integration surface is a public REST API alongside an official MCP server. Given lack of confirmed self-serve production access and thin auth details in fetched pages, buildability is Hard; the next action is outreach to Ramp to obtain/enable production credentials or join the partner program. Confidence is limited due to missing detailed auth docs in the fetched content.

## Key decisions
- buildability: **Hard**
- access_model: **Gated** - No fetched doc confirms self-serve production credentials. Agents doc says API actions are scoped to a Ramp business owner’s identity; developer site emphasizes a partner program. Production access likely requires a Ramp account and approval.
- recommended_next_action: **Needs Outreach**
- confidence: **0.55**

## Evidence URLs
- https://developer.ramp.com
- https://agents.ramp.com/docs/mcp/overview
- https://mcp.directory/servers/ramp
- https://support.ramp.com/ramp-pricing-overview/

## Generated record
```json
{
  "app": "Ramp",
  "category": "Fintech",
  "one_liner": "Ramp offers REST APIs and an official MCP server, but production access appears gated to Ramp accounts.",
  "auth_methods": [
    "OAuth2"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "No fetched doc confirms self-serve production credentials. Agents doc says API actions are scoped to a Ramp business owner’s identity; developer site emphasizes a partner program. Production access likely requires a Ramp account and approval."
  },
  "api_type": "REST",
  "api_breadth": "Moderate",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Hard",
  "main_blocker": "No documented self-serve production credential path; access appears tied to a Ramp business account/partner program.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://developer.ramp.com",
    "https://agents.ramp.com/docs/mcp/overview",
    "https://mcp.directory/servers/ramp",
    "https://support.ramp.com/ramp-pricing-overview/"
  ],
  "confidence": 0.55,
  "verification_status": "Auto",
  "slug": "ramp",
  "primary_docs_url": "https://developer.ramp.com",
  "rate_limit_note": "Not stated in fetched pages.",
  "last_verified": "2026-08-18"
}
```

## Risk seed (withheld from synthesis)
This prior was retained only for audit sampling and was not shown to the model.
```json
{
  "access_model": "Gated",
  "recommended_next_action": "Needs Outreach",
  "main_blocker": "API access is tied to being a Ramp business customer; not self-serve for a solo developer testing."
}
```

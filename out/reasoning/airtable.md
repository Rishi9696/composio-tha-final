# Airtable - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Airtable official API authentication developer documentation", "Airtable API production access approval credentials official documentation", "Airtable official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://airtable.com/developers | HTTP 200 | hint | topics=api,auth,mcp
- https://www.airtablemcp.com/docs/authentication | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://airtable.com/pricing | HTTP 200 | search_result | topics=api,access
- https://support.airtable.com/v1/docs/getting-started-with-airtables-web-api | HTTP 200 | search_result | topics=api,auth,access
- https://developer.airtable.com | HTTP 0 | derived_guess | topics=none
- https://developers.airtable.com | HTTP 0 | derived_guess | topics=none

## Model reasoning
1) Evidence states:
- REST/Web API: Airtable’s support doc for the Web API shows concrete REST endpoints and usage (e.g., https://api.airtable.com/v0/appxxx/TableName), pagination behavior, and a fixed rate limit: “Yes, the Web API has a rate limit of 5 requests per second, per base… the same across all pricing tiers and increased rate limits are not currently available.” It also says “Plan availability All plan types with varying call limitations,” and notes certain capabilities require higher-role/admin permissions for Business/Enterprise.
- MCP: The Airtable support page “Using the Airtable MCP server” says “Plan availability All plans” and describes that Owners/Creators/Editors can set up OAuth integrations and manage MCP access; it’s positioned to work with Claude/ChatGPT and other MCP clients. The Airtable Developers portal highlights MCP and says Claude/ChatGPT “Connects in one click via OAuth.” The MCP directory (mcp.so) lists a hosted endpoint at https://mcp.airtable.com/mcp and states “Airtable uses OAuth” for the MCP server. The airtablemcp.com guide explains using a Personal Access Token (PAT) with scopes for the MCP server.
- Auth credentials: OAuth2 is used for the official hosted MCP connection; Personal Access Token (PAT) is documented for authenticating to Airtable’s API in the MCP context.
2) Production Access Rubric application:
- The REST doc says “Plan availability All plan types,” and the MCP doc says “Plan availability All plans,” but neither page explicitly confirms that a brand-new developer can obtain production API/MCP credentials without any manual approval or without being on a paid plan. The pricing page exists but does not explicitly state API production entitlement for free users. Therefore, there is no explicit self-serve production confirmation; per the rubric, we must treat production access as Gated absent clear evidence of free, approval-free production access.
3) Decisions:
- Auth methods: OAuth2 (for official MCP) and Personal Access Token (for API/MCP as documented). API type: REST is the dominant public API; MCP also exists as an official surface. Existing MCP: Official (vendor-hosted endpoint). Access model: Gated (no explicit evidence of self-serve production entitlement; role/plan requirements may apply). Buildability: Moderate (docs are clear, but production access uncertainties and required roles/plans introduce friction). Recommended next action: Needs Outreach to confirm production eligibility and any plan/approval requirements.

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - Docs show REST and an official hosted MCP on all plans, but do not explicitly guarantee self-serve production credentials for new developers without paid plans or approval. Role- and plan-based permissions may be required.
- recommended_next_action: **Needs Outreach**
- confidence: **0.6**

## Evidence URLs
- https://support.airtable.com/v1/docs/getting-started-with-airtables-web-api
- https://support.airtable.com/docs/using-the-airtable-mcp-server
- https://airtable.com/developers
- https://mcp.so/servers/airtable
- https://www.airtablemcp.com/docs/authentication

## Generated record
```json
{
  "app": "Airtable",
  "category": "Productivity/PM",
  "one_liner": "Airtable offers REST and an official MCP server, but production access terms aren’t explicitly self-serve.",
  "auth_methods": [
    "OAuth2",
    "Personal Access Token"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Docs show REST and an official hosted MCP on all plans, but do not explicitly guarantee self-serve production credentials for new developers without paid plans or approval. Role- and plan-based permissions may be required."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "Unclear production entitlement; may require specific plan/roles or approval to enable API/MCP access.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://support.airtable.com/v1/docs/getting-started-with-airtables-web-api",
    "https://support.airtable.com/docs/using-the-airtable-mcp-server",
    "https://airtable.com/developers",
    "https://mcp.so/servers/airtable",
    "https://www.airtablemcp.com/docs/authentication"
  ],
  "confidence": 0.6,
  "verification_status": "Auto",
  "slug": "airtable",
  "primary_docs_url": "https://support.airtable.com/v1/docs/getting-started-with-airtables-web-api",
  "rate_limit_note": "Web API is limited to 5 requests/second per base across all tiers; no higher limits available.",
  "last_verified": "2026-08-18"
}
```

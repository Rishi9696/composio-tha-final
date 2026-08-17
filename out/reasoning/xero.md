# Xero - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Xero official API authentication developer documentation", "Xero API production access approval credentials official documentation", "Xero official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://developer.xero.com | HTTP 200 | hint | topics=api,auth,access,mcp
- https://developer.xero.com/documentation/guides/oauth2/overview | HTTP 200 | search_result | topics=auth
- https://developer.xero.com/documentation/guides/oauth2/client-credentials/ | HTTP 200 | search_result | topics=auth
- https://developer.xero.com/documentation/guides/oauth2/token-types | HTTP 200 | search_result | topics=auth
- https://developers.xero.com | HTTP 0 | derived_guess | topics=none
- https://docs.xero.com | HTTP 0 | derived_guess | topics=none

## Model reasoning
1) What the evidence states:
- Xero developer site: "Sign up for a free account to build on the Xero platform" and references certification and app store publishing ("Get Certified... you'll need ten to get certified"; "Publish your app on the Xero App Store"). It mentions Xero APIs but does not detail protocol in the fetched excerpt.
- MCP: The Xero MCP Server page (mcp.so) shows configuration and explicitly supports two auth modes: OAuth2 via Custom Connections (client_id/secret, scopes) or providing a pre-obtained bearer token env var. It describes the server as a bridge to "Xero's API" and lists example tools (e.g., list-accounts, create-invoice).
- GrowthEngineer page calls it the "Official MCP server from Xero (XeroAPI)" and states it uses Xero's OAuth2 Custom Connections or a runtime bearer token; it exposes 60+ tools across accounting, payments, and payroll.
- CData MCP Server for Xero docs reference OAuth-related setup ("Creating a Custom Authentication Application") and include a section titled "Xero API Limits" and a broad data model list (accounting and payroll), implying wide surface coverage. 
Auth credentials: OAuth2 is clearly required; the MCP server can accept a pre-obtained bearer token but it’s described as coming from an OAuth flow (not a static vendor token).
API surface: The MCP server bridges to Xero’s API; fetched excerpts do not explicitly label REST, but Xero’s public API is implied via the developer site and MCP descriptions.

2) Production Access Rubric application:
- Evidence of Self-Serve production: None explicit. While "Sign up for a free account to build on the Xero platform" exists, it does not confirm production entitlement without approvals or paid accounts.
- Evidence of gating: The site emphasizes certification/partner steps ("Get Certified... you'll need ten to get certified" and "Publish your app on the Xero App Store"), indicating review/partnering for public/multi-tenant production apps. No fetched sentence confirms free, approval-free production access for new developers.
Result: Classify as Gated per rubric due to lack of explicit self-serve production proof and presence of certification/partner program requirements.

3) Decisions:
- auth_methods: OAuth2 (the MCP and developer materials consistently show OAuth2; the "bearer token" option on MCP is still OAuth-derived, not an independent static token).
- api_type: REST as the dominant public API (MCP bridges to Xero’s API; although the excerpt doesn’t say REST verbatim, this is the standard Xero surface; confidence noted as limited due to thin explicit wording).
- existing_mcp: Official (explicitly called official by GrowthEngineer and listed as XeroAPI on mcp.so).
- access_model: Gated (partner certification steps for public apps; no explicit self-serve production entitlement documented in fetched content).
- buildability: Hard (gating/partner certification implications; thin explicit production-access detail despite available tooling).
- recommended_next_action: Needs Outreach (engage Xero’s developer/partner program or confirm production eligibility for Custom Connections).
If evidence is thin: acknowledged above; confidence reduced accordingly.

## Key decisions
- buildability: **Hard**
- access_model: **Gated** - The developer site highlights certification and app partner steps (e.g., “Get Certified…”, app store publishing) and does not explicitly confirm self-serve production access for new developers. MCP can be used with OAuth2 Custom Connections, but production eligibility is not clearly self-serve in the fetched docs.
- recommended_next_action: **Needs Outreach**
- confidence: **0.48**

## Evidence URLs
- https://developer.xero.com
- https://mcp.so/servers/xero-mcp-server
- https://growthengineer.ai/mcp-servers/xero
- https://cdn.cdata.com/help/DXK/mcp/

## Generated record
```json
{
  "app": "Xero",
  "category": "Fintech",
  "one_liner": "Xero offers OAuth2 APIs and an official MCP server, but production access appears partner-gated.",
  "auth_methods": [
    "OAuth2"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "The developer site highlights certification and app partner steps (e.g., “Get Certified…”, app store publishing) and does not explicitly confirm self-serve production access for new developers. MCP can be used with OAuth2 Custom Connections, but production eligibility is not clearly self-serve in the fetched docs."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Hard",
  "main_blocker": "No explicit proof of self-serve production credentials; partner certification/app review appears required for public apps.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://developer.xero.com",
    "https://mcp.so/servers/xero-mcp-server",
    "https://growthengineer.ai/mcp-servers/xero",
    "https://cdn.cdata.com/help/DXK/mcp/"
  ],
  "confidence": 0.48,
  "verification_status": "Auto",
  "slug": "xero",
  "primary_docs_url": "https://developer.xero.com",
  "rate_limit_note": "Rate limits are referenced (\"Xero API Limits\" section in CData docs), but specific quotas were not in fetched excerpts.",
  "last_verified": "2026-08-18"
}
```

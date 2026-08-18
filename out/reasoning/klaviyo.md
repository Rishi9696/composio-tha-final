# Klaviyo - synthesis reasoning
_generated 2026-08-17 | model openai:gpt-5_

## Research trace
- queries: ["Klaviyo official API authentication developer documentation", "Klaviyo API production access approval credentials official documentation", "Klaviyo official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://developers.klaviyo.com | HTTP 200 | hint | topics=api,auth,access
- https://developers.klaviyo.com/en/docs/authenticate_ | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://www.klaviyo.com/pricing | HTTP 200 | search_result | topics=api,access
- https://developers.klaviyo.com/en/v2023-01-24/docs/authenticate_?utm_source=openai | HTTP 200 | search_result | topics=api,auth,access
- https://developer.klaviyo.com | HTTP 0 | derived_guess | topics=none
- https://docs.klaviyo.com | HTTP 200 | derived_guess | topics=api,auth,access

## Model reasoning
1) Evidence about surfaces and auth:
- REST API: The v2023 auth doc explicitly states: “All /api endpoints use API private keys to authenticate requests. If you do not use an API key…your call will return an error.” It also points to generating private keys (developers.klaviyo.com/en/v2023-01-24/docs/authenticate_?utm_source=openai).
- Developer site shows a robust public REST API, SDKs, and test accounts: “Test accounts — Test custom integrations and apps without the risk of impacting your production account.” and “Get started for free.” (developers.klaviyo.com).
- MCP: There is an official “Klaviyo MCP server” page on the Klaviyo developer docs (developers.klaviyo.com/en/docs/klaviyo_mcp_server), and third-party documentation describes two auth modes: remote (hosted) using OAuth with dynamic client registration, and local using a Klaviyo Private API Key (growthengineer.ai/mcp-servers/klaviyo). This supports OAuth2 (for MCP remote) and API Key (for REST and MCP local) as independent auth methods.

2) Production Access Rubric application:
- Self-serve proof: While the dev site says “Get started for free” and offers “Create a test account,” there is no explicit statement in the cited docs that a new developer can obtain production credentials without approval or a paid plan. The presence of partner/app review materials in the nav (e.g., “Submit your app for review”) suggests some production/public distribution flows are reviewed, but we do not have a clear sentence guaranteeing self-serve production entitlement.
- Therefore, per the rubric, absent explicit proof of self-serve production access, classify as Gated.

3) Conclusions tied to evidence:
- api_type: REST is the dominant public API; MCP exists as an additional official surface.
- auth_methods: API Key (for REST and local MCP) and OAuth2 (for MCP remote) are independently documented.
- existing_mcp: Official (there is an official Klaviyo MCP server page on the Klaviyo developer site).
- access_model: Gated due to lack of explicit self-serve production entitlement in the docs; test accounts are clearly available but do not prove production access.
- buildability: Moderate — clear REST authentication with API keys and available docs, but production access uncertainty and potential app review for public OAuth apps increase friction.
- next action: Engage Klaviyo to confirm production access entitlements/scopes and any review or plan requirements.

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - Docs clearly show API key generation and OAuth for MCP, plus test accounts, but provide no explicit statement that new developers get production credentials without approval or paid plans. Public app distribution appears to require review.
- recommended_next_action: **Needs Outreach**
- confidence: **0.56**

## Evidence URLs
- https://developers.klaviyo.com/en/v2023-01-24/docs/authenticate_?utm_source=openai
- https://developers.klaviyo.com/en/docs/authenticate_
- https://developers.klaviyo.com
- https://developers.klaviyo.com/en/docs/klaviyo_mcp_server
- https://growthengineer.ai/mcp-servers/klaviyo

## Generated record
```json
{
  "app": "Klaviyo",
  "category": "Ads/Marketing",
  "one_liner": "Klaviyo offers REST APIs and an official MCP server with API key and OAuth auth, but production access appears gated.",
  "auth_methods": [
    "API Key",
    "OAuth2"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Docs clearly show API key generation and OAuth for MCP, plus test accounts, but provide no explicit statement that new developers get production credentials without approval or paid plans. Public app distribution appears to require review."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "No explicit proof of self-serve production access; potential app review/plan requirements for production and public OAuth apps.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://developers.klaviyo.com/en/v2023-01-24/docs/authenticate_?utm_source=openai",
    "https://developers.klaviyo.com/en/docs/authenticate_",
    "https://developers.klaviyo.com",
    "https://developers.klaviyo.com/en/docs/klaviyo_mcp_server",
    "https://growthengineer.ai/mcp-servers/klaviyo"
  ],
  "confidence": 0.56,
  "verification_status": "Auto",
  "slug": "klaviyo",
  "primary_docs_url": "https://developers.klaviyo.com/en/docs/authenticate_",
  "rate_limit_note": "Docs reference a rate limits guide, but specific limits are not detailed in the cited pages.",
  "last_verified": "2026-08-17"
}
```

<!-- final-state:start -->
## Final pipeline state
_Updated 2026-08-18 by current handcheck fold; this supersedes earlier key decisions._

```json
{
  "app": "Klaviyo",
  "category": "Ads/Marketing",
  "one_liner": "Klaviyo offers REST APIs and an official MCP server with API key and OAuth auth, but production access appears gated.",
  "auth_methods": [
    "API Key",
    "OAuth2"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Docs clearly show API key generation and OAuth for MCP, plus test accounts, but provide no explicit statement that new developers get production credentials without approval or paid plans. Public app distribution appears to require review."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "No explicit proof of self-serve production access; potential app review/plan requirements for production and public OAuth apps.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://developers.klaviyo.com/en/v2023-01-24/docs/authenticate_?utm_source=openai",
    "https://developers.klaviyo.com/en/docs/authenticate_",
    "https://developers.klaviyo.com",
    "https://developers.klaviyo.com/en/docs/klaviyo_mcp_server",
    "https://growthengineer.ai/mcp-servers/klaviyo"
  ],
  "confidence": 0.56,
  "verification_status": "Hand-Checked",
  "slug": "klaviyo",
  "primary_docs_url": "https://developers.klaviyo.com/en/docs/authenticate_",
  "rate_limit_note": "Docs reference a rate limits guide, but specific limits are not detailed in the cited pages.",
  "last_verified": "2026-08-17"
}
```
<!-- final-state:end -->

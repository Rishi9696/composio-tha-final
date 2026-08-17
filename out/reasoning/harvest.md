# Harvest - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Harvest official API authentication developer documentation", "Harvest API production access approval credentials official documentation", "Harvest official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://help.getharvest.com/api-v2 | HTTP 200 | hint | topics=api,auth
- https://support.getharvest.com/hc/en-us/articles/360048180732-The-Harvest-API | HTTP 200 | derived_guess | topics=api,access
- https://help.getharvest.com/api-v2/authentication-api/authentication/authentication/ | HTTP 200 | search_result | topics=api,auth
- https://support.getharvest.com/hc/en-us/articles/31447072608397-Information-about-pricing-plans | HTTP 200 | search_result | topics=access
- https://mindcloud.co/docs/universal/rest/harvest/latest | HTTP 200 | search_result | topics=api,auth,access
- https://developer.getharvest.com | HTTP 0 | derived_guess | topics=none

## Model reasoning
1) Evidence states: Harvest API v2 requires an access token with two options: Personal Access Token (PAT) or implementing an OAuth2 flow; PATs are created in the Developers section of Harvest ID and used via Authorization: Bearer plus Harvest-Account-Id (help.getharvest.com/api-v2/authentication-api/authentication/authentication/). The API v2 Help Center shows extensive REST endpoints across many resources (help.getharvest.com/api-v2). The Help article says: “Your Harvest subscription includes API access for all accounts (including free and trial accounts)” and “All Harvest accounts are able to access the Harvest API,” and notes throttling (support.getharvest.com/hc/en-us/articles/360048180732-The-Harvest-API). Pricing describes Free, Teams, and Enterprise plans but does not explicitly detail production API entitlements beyond general plan info (support.getharvest.com/hc/en-us/articles/31447072608397-Information-about-pricing-plans). MCP: third-party/community MCP servers exist (harvest-mcp.southleft.com; lobehub.com listing requiring HARVEST_ACCESS_TOKEN and HARVEST_ACCOUNT_ID). No official Harvest MCP is shown. 2) Production Access Rubric: While the Help article indicates API access for all accounts including free and trial, there is no explicit statement that a new developer can obtain production credentials without any manual approval and without needing a paid plan beyond trial/free, nor explicit confirmation of production entitlement terms. No page states an official self-serve MCP. Therefore, lacking explicit free production entitlement language per the rubric, classify as Gated. 3) Conclusions: Auth methods: Personal Access Token and OAuth2. API type: REST with broad coverage. Existing MCP: Community. Buildability is Moderate (auth/docs are clear, but production entitlement is uncertain under the rubric). Recommended next action: Needs Outreach to confirm production usage terms and any plan/approval requirements. Rate limits exist per Help Center reference.

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - Docs show PAT and OAuth2 setup is self-serve, but there is no explicit statement confirming free self-serve production credentials without approval; thus classify as gated per rubric.
- recommended_next_action: **Needs Outreach**
- confidence: **0.66**

## Evidence URLs
- https://help.getharvest.com/api-v2/authentication-api/authentication/authentication/
- https://help.getharvest.com/api-v2
- https://support.getharvest.com/hc/en-us/articles/360048180732-The-Harvest-API
- https://support.getharvest.com/hc/en-us/articles/31447072608397-Information-about-pricing-plans
- https://harvest-mcp.southleft.com/?utm_source=openai
- https://lobehub.com/pl/mcp/valtirallc-harvest-mcp-server?utm_source=openai

## Generated record
```json
{
  "app": "Harvest",
  "category": "Productivity/PM",
  "one_liner": "Harvest offers a broad REST API with PAT and OAuth2; confirm production access terms before building.",
  "auth_methods": [
    "Personal Access Token",
    "OAuth2"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Docs show PAT and OAuth2 setup is self-serve, but there is no explicit statement confirming free self-serve production credentials without approval; thus classify as gated per rubric."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Community",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "Unclear production entitlement and plan requirements for API usage under the rubric.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://help.getharvest.com/api-v2/authentication-api/authentication/authentication/",
    "https://help.getharvest.com/api-v2",
    "https://support.getharvest.com/hc/en-us/articles/360048180732-The-Harvest-API",
    "https://support.getharvest.com/hc/en-us/articles/31447072608397-Information-about-pricing-plans",
    "https://harvest-mcp.southleft.com/?utm_source=openai",
    "https://lobehub.com/pl/mcp/valtirallc-harvest-mcp-server?utm_source=openai"
  ],
  "confidence": 0.66,
  "verification_status": "Auto",
  "slug": "harvest",
  "primary_docs_url": "https://mindcloud.co/docs/universal/rest/harvest/latest",
  "rate_limit_note": "Harvest throttles API requests; rate limit details are referenced in the API overview.",
  "last_verified": "2026-08-18"
}
```

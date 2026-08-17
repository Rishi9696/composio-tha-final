# ClickUp - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["ClickUp official API authentication developer documentation", "ClickUp API production access approval credentials official documentation", "ClickUp official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://clickup.com/api | HTTP 200 | hint | topics=api,auth,mcp
- https://developer.clickup.com/docs/authentication | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://clickup.com/pricing | HTTP 200 | search_result | topics=api,auth,access
- https://developer.clickup.com/docs/apis-available-by-plan | HTTP 200 | search_result | topics=api,auth,mcp
- https://developer.clickup.com | HTTP 200 | derived_guess | topics=api,auth,mcp
- https://developers.clickup.com | HTTP 200 | derived_guess | topics=none

## Model reasoning
1) Evidence states: The Authentication doc says, “Authenticate to the ClickUp API using a personal token or OAuth,” with instructions to generate a personal API token in user Settings; personal tokens never expire; OAuth 2.0 Authorization Code flow is supported with specified URLs. The API availability page says, “Our Public API is available on all ClickUp Plans. Some endpoints and parameters are limited by plan,” listing Enterprise-only endpoints. The pricing page references “Enterprise API” and “Enterprise-Scale API Usage.” MCP docs state: “ClickUp's MCP server is currently in public beta … available on all plans.” 2) Production Access Rubric application: While the docs show credential mechanics (personal token generation, OAuth app setup) and say the public API and MCP are available on all plans, none of the cited pages explicitly state that a new developer can use production access for free without any gating beyond plan limitations. The pricing page implies higher tiers for “Enterprise-Scale API Usage,” and the API availability page lists Enterprise-only endpoints. Therefore, there is no explicit sentence guaranteeing free production entitlement; per the rubric, absent such proof, classify as Gated. 3) Decisions: Auth methods are Personal Access Token and OAuth2. Dominant surface is REST; there is also an official MCP server. Access model is Gated due to lack of explicit free production entitlement and plan-gated endpoints. Buildability is Moderate: clear docs and tokens exist, but plan-based gating may require outreach or upgrading for needed endpoints/scale. Recommended next action: Needs Outreach to confirm required plan and production quotas for the intended use.

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - Docs show personal tokens and OAuth and say the Public API and MCP are available on all plans, but they do not explicitly guarantee free, ungated production entitlement; some endpoints/scale are plan- or Enterprise-gated.
- recommended_next_action: **Needs Outreach**
- confidence: **0.71**

## Evidence URLs
- https://developer.clickup.com/docs/authentication
- https://developer.clickup.com/docs/apis-available-by-plan
- https://clickup.com/pricing
- https://developer.clickup.com/docs/connect-an-ai-assistant-to-clickups-mcp-server
- https://help.clickup.com/hc/en-us/articles/33335772678423-What-is-ClickUp-MCP

## Generated record
```json
{
  "app": "ClickUp",
  "category": "Productivity/PM",
  "one_liner": "ClickUp offers a broad REST API and official MCP, but production use is plan-gated and may need outreach.",
  "auth_methods": [
    "Personal Access Token",
    "OAuth2"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Docs show personal tokens and OAuth and say the Public API and MCP are available on all plans, but they do not explicitly guarantee free, ungated production entitlement; some endpoints/scale are plan- or Enterprise-gated."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "Plan-based gating and Enterprise-only endpoints may limit required functionality and scale.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://developer.clickup.com/docs/authentication",
    "https://developer.clickup.com/docs/apis-available-by-plan",
    "https://clickup.com/pricing",
    "https://developer.clickup.com/docs/connect-an-ai-assistant-to-clickups-mcp-server",
    "https://help.clickup.com/hc/en-us/articles/33335772678423-What-is-ClickUp-MCP"
  ],
  "confidence": 0.71,
  "verification_status": "Auto",
  "slug": "clickup",
  "primary_docs_url": "https://developer.clickup.com/docs/authentication",
  "rate_limit_note": "API features and scale vary by plan; MCP is public beta with fair-use limits that may change.",
  "last_verified": "2026-08-18"
}
```

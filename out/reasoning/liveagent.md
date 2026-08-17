# LiveAgent - synthesis reasoning
_generated 2026-08-17 | model openai:gpt-5_

## Research trace
- queries: ["LiveAgent official API authentication developer documentation", "LiveAgent API production access approval credentials official documentation", "LiveAgent official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://liveagent.com | HTTP 200 | hint | topics=access
- https://support.liveagent.com/docs/api/v3/#authentication | HTTP 200 | search_result | topics=api,auth
- https://www.liveagent.com/pricing/ | HTTP 200 | search_result | topics=access
- https://www.liveagent.com/pricing/#features | HTTP 200 | search_result | topics=access
- https://developer.liveagent.com | HTTP 0 | derived_guess | topics=none
- https://developers.liveagent.com | HTTP 0 | derived_guess | topics=none

## Model reasoning
1) Evidence about surface and auth: LiveAgent’s support doc explicitly says “LiveAgent exposes a built-in MCP server (Model Context Protocol)” with a server URL at https://<your-liveagent-domain>/api/mcp using “Streamable HTTP,” and lists “Two ways to authenticate your MCP client: Bearer token … [and] OAuth 2.1 (Authorization Code + PKCE).” It also notes tokens are generated in the user profile and OAuth apps are authorized in-account. No fetched doc here details the REST API; only the MCP server is described. 2) Production access rubric: The pricing page says “Start with a 30-day free trial. No credit card required.” There is no statement that production API/MCP access is freely available without payment; continued use appears tied to a paid plan. Therefore, production access cannot be classified as self-serve free production; it is gated by commercial subscription. 3) Decisions: Auth methods are Bearer Token and OAuth2 (from the MCP doc). The dominant documented surface here is MCP, so api_type = MCP-only. There is an official vendor-hosted MCP server, so existing_mcp = Official. Access_model = Gated due to the paid plan requirement after a 30-day trial. Buildability = Moderate (clear MCP docs and auth, but production requires plan/account). Recommended_next_action = Needs Outreach (secure/upgrade a LiveAgent plan to obtain production credentials).

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - MCP tokens/OAuth apps are issued within a LiveAgent account, and pricing states a 30‑day free trial with ongoing use tied to paid plans (“Start with a 30-day free trial. No credit card required.”). No evidence of free self-serve production access.
- recommended_next_action: **Needs Outreach**
- confidence: **0.62**

## Evidence URLs
- https://support.liveagent.com/647358-MCP-Integration-for-Agents
- https://www.liveagent.com/pricing/

## Generated record
```json
{
  "app": "LiveAgent",
  "category": "Support",
  "one_liner": "LiveAgent offers an official MCP server with OAuth2 or tokens; production access requires a paid plan.",
  "auth_methods": [
    "Bearer Token",
    "OAuth2"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "MCP tokens/OAuth apps are issued within a LiveAgent account, and pricing states a 30‑day free trial with ongoing use tied to paid plans (“Start with a 30-day free trial. No credit card required.”). No evidence of free self-serve production access."
  },
  "api_type": "MCP-only",
  "api_breadth": "Moderate",
  "existing_mcp": "Official",
  "composio_toolkit": "No",
  "buildability": "Moderate",
  "main_blocker": "Production MCP access requires a LiveAgent account/paid plan; only a 30-day trial is free.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://support.liveagent.com/647358-MCP-Integration-for-Agents",
    "https://www.liveagent.com/pricing/"
  ],
  "confidence": 0.62,
  "verification_status": "Auto",
  "slug": "liveagent",
  "primary_docs_url": "https://www.liveagent.com/pricing/#features",
  "rate_limit_note": "Not documented in the cited LiveAgent pages.",
  "last_verified": "2026-08-17"
}
```

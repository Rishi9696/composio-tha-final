# Discord - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Discord official API authentication developer documentation", "Discord API production access approval credentials official documentation", "Discord official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://discord.com | HTTP 200 | hint | topics=none
- https://docs.discord.com/developers/topics/oauth2 | HTTP 200 | search_result | topics=api,auth,access
- https://apis.io/plans/discord/discord-plans-pricing/?utm_source=openai | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://docs.discord.com/developers/reference | HTTP 200 | search_result | topics=api,auth
- https://developer.discord.com | HTTP 0 | derived_guess | topics=none
- https://developers.discord.com | HTTP 0 | derived_guess | topics=none

## Model reasoning
1) Evidence states: Discord exposes a REST API with base URL https://discord.com/api (docs.discord.com/developers/reference). OAuth2 is supported with authorization, token, and revocation endpoints, and Discord notes “We support the authorization code grant, the implicit grant, client credentials, and some modified special-for-Discord flows for Bots and Webhooks” (docs.discord.com/developers/topics/oauth2). The same OAuth2 page states: “Some scopes require approval from Discord to use,” indicating permissions gating. APIs.io’s Discord Plans page states “Discord API access is free for developers,” providing a pricing/plan signal (apis.io/plans/discord/discord-plans-pricing). No official Discord-hosted MCP server or API was found; only a community Discord server listing related to MCP, and the MCP registry search did not surface a concrete Discord MCP server in the fetched content. 2) Production Access Rubric: Hosted connection is evidenced by official OAuth2 endpoints on discord.com. While APIs.io indicates the API is free for developers, the OAuth2 docs explicitly say some scopes require Discord approval, which is gating. There is no explicit statement guaranteeing fully self-serve production use without approvals. Therefore, choose Gated. 3) Conclusions: Auth method: OAuth2. API type: REST. Existing MCP: None (only community server references). Access model: Gated due to scope approval. Buildability: Moderate—docs are clear, but required scopes may need approval. Next action: request/confirm required scope approvals with Discord.

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - OAuth2 docs state some scopes require Discord approval; while APIs.io notes API access is free, production scopes can be gated.
- recommended_next_action: **Needs Outreach**
- confidence: **0.68**

## Evidence URLs
- https://docs.discord.com/developers/reference
- https://docs.discord.com/developers/topics/oauth2
- https://apis.io/plans/discord/discord-plans-pricing/?utm_source=openai

## Generated record
```json
{
  "app": "Discord",
  "category": "Comms",
  "one_liner": "Discord has a REST API with OAuth2; some scopes require approval, so plan for gated production access.",
  "auth_methods": [
    "OAuth2"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "OAuth2 docs state some scopes require Discord approval; while APIs.io notes API access is free, production scopes can be gated."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "None",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "Obtaining Discord approval for required OAuth2 scopes/permissions.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://docs.discord.com/developers/reference",
    "https://docs.discord.com/developers/topics/oauth2",
    "https://apis.io/plans/discord/discord-plans-pricing/?utm_source=openai"
  ],
  "confidence": 0.68,
  "verification_status": "Auto",
  "slug": "discord",
  "primary_docs_url": "https://docs.discord.com/developers/topics/oauth2",
  "rate_limit_note": "Discord documents HTTP rate limits; design with bucketed limits and retries per docs.",
  "last_verified": "2026-08-18"
}
```

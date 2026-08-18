# Squarespace - synthesis reasoning
_generated 2026-08-17 | model openai:gpt-5_

## Research trace
- queries: ["Squarespace official API authentication developer documentation", "Squarespace API production access approval credentials official documentation", "Squarespace official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://developers.squarespace.com | HTTP 200 | hint | topics=api,access
- https://developers.squarespace.com/commerce-apis/authentication-and-permissions | HTTP 200 | search_result | topics=api,auth,access
- https://www.techradar.com/reviews/squarespace | HTTP 200 | search_result | topics=access
- https://developers.squarespace.com/commerce-apis/oauth | HTTP 200 | search_result | topics=api,auth,access
- https://developer.squarespace.com | HTTP 200 | derived_guess | topics=none
- https://docs.squarespace.com | HTTP 404 | derived_guess | topics=none

## Model reasoning
1) What the evidence states: The Authentication and permissions page says requests can be authenticated "by using an API key or OAuth access token" and lists many Commerce APIs plus that "Webhook Subscriptions API (OAuth only)" is available. It also states, "A Squarespace merchant site can use both API keys and OAuth for data access," and adds a paywall: "With Squarespace's Commerce Advanced plan, you can develop a custom application for a Squarespace merchant site." The OAuth page requires client registration and explicitly notes manual review: "We will review your registration and respond with your_client_id and your_client_secret as soon as possible." The developers homepage confirms the surface is REST: "Commerce APIs ... REST endpoints, webhooks for order events." MCP evidence shows an official Squarespace MCP server providing domain tools: "Overview of the Squarespace MCP Server... Today the server provides domain tools." No rate limits are documented on the cited pages. 2) Production Access Rubric: Gating is evidenced by (a) manual review for OAuth client issuance ("We will review your registration and respond...") and (b) a paid plan requirement to generate API keys for custom apps ("With Squarespace's Commerce Advanced plan, you can develop a custom application..."). There is no statement that a new developer can obtain production credentials self-serve without approval or paid accounts. 3) Decisions: Auth methods are API Key and OAuth2. Dominant API is REST with broad Commerce coverage. There is an official MCP server (domain tools only). Given manual review and paid plan requirements, access is Gated. Buildability is Hard due to approval and plan gating. Next action is Needs Outreach to register an OAuth client and confirm plan requirements.

## Key decisions
- buildability: **Hard**
- access_model: **Gated** - OAuth clients require manual review (Squarespace responds with client_id/secret), and API keys for custom apps require a Commerce Advanced plan.
- recommended_next_action: **Needs Outreach**
- confidence: **0.68**

## Evidence URLs
- https://developers.squarespace.com/commerce-apis/authentication-and-permissions
- https://developers.squarespace.com/commerce-apis/oauth
- https://developers.squarespace.com
- https://developers-preview.squarespace.com/mcp/overview?utm_source=openai

## Generated record
```json
{
  "app": "Squarespace",
  "category": "Commerce",
  "one_liner": "Squarespace offers REST Commerce APIs with API keys and OAuth, but production access is gated.",
  "auth_methods": [
    "API Key",
    "OAuth2"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "OAuth clients require manual review (Squarespace responds with client_id/secret), and API keys for custom apps require a Commerce Advanced plan."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "No",
  "buildability": "Hard",
  "main_blocker": "Manual OAuth client approval and paid Commerce Advanced plan needed for API key-based custom apps.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://developers.squarespace.com/commerce-apis/authentication-and-permissions",
    "https://developers.squarespace.com/commerce-apis/oauth",
    "https://developers.squarespace.com",
    "https://developers-preview.squarespace.com/mcp/overview?utm_source=openai"
  ],
  "confidence": 0.68,
  "verification_status": "Auto",
  "slug": "squarespace",
  "primary_docs_url": "https://developers.squarespace.com/commerce-apis/oauth",
  "rate_limit_note": "No rate limits documented on the cited pages.",
  "last_verified": "2026-08-17"
}
```

<!-- final-state:start -->
## Final pipeline state
_Updated 2026-08-18 by current handcheck fold; this supersedes earlier key decisions._

```json
{
  "app": "Squarespace",
  "category": "Commerce",
  "one_liner": "Squarespace offers REST Commerce APIs with API keys and OAuth, but production access is gated.",
  "auth_methods": [
    "OAuth2",
    "API Key"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "OAuth clients require manual review (Squarespace responds with client_id/secret), and API keys for custom apps require a Commerce Advanced plan."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Community",
  "composio_toolkit": "No",
  "buildability": "Hard",
  "main_blocker": "Manual OAuth client approval and paid Commerce Advanced plan needed for API key-based custom apps.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://developers.squarespace.com/oauth",
    "https://developers.squarespace.com/commerce-apis/authentication-and-permissions",
    "https://github.com/BusyBee3333/squarespace-mcp-2026-complete"
  ],
  "confidence": 0.68,
  "verification_status": "Hand-Checked",
  "slug": "squarespace",
  "primary_docs_url": "https://developers.squarespace.com/oauth",
  "rate_limit_note": "No rate limits documented on the cited pages.",
  "last_verified": "2026-08-17"
}
```
<!-- final-state:end -->

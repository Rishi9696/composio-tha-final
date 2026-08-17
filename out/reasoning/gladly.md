# Gladly - synthesis reasoning
_generated 2026-08-17 | model openai:gpt-5_

## Research trace
- queries: ["Gladly official API authentication developer documentation", "Gladly API production access approval credentials official documentation", "Gladly official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://gladly.com | HTTP 200 | hint | topics=api,access
- https://apis.io/apis/gladly/gladly-webhooks-api/ | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://www.xpay.sh/saas-pricing/gladly/ | HTTP 200 | search_result | topics=api,access,mcp,non_hosted
- https://developer.gladly.com/rest/index.html#authentication | HTTP 200 | search_result | topics=api,auth,access
- https://developer.gladly.com | HTTP 200 | derived_guess | topics=api
- https://developers.gladly.com | HTTP 0 | derived_guess | topics=none

## Model reasoning
1) What the evidence states: The official Gladly REST API docs expose many resources (Agents, Answers, Audiences, Business Hours, Communications, Conversations, Customers, Reports, Tasks, Teams, Webhooks, etc.) and include “Creating API Tokens,” “Replacing/Rotating API Tokens,” and “Authentication,” plus rate limit sections (developer.gladly.com/rest/index.html#authentication). Authentication is documented as using API tokens and explicitly via HTTP Basic for API requests (token-based Basic), reflected in the Authentication section and corroborated by the Gladly Webhooks API listing indicating token-based Basic Authentication (apis.io/apis/gladly/gladly-webhooks-api/). No evidence of OAuth flows is shown in the official docs. No official MCP server for Gladly is referenced. 2) Production Access Rubric: There is no statement in official docs that a new developer can obtain production credentials self-serve. An external pricing analysis states sales-led pricing with no public tiers or self-serve checkout and no advertised free tier (xpay.sh). Therefore, per the rubric, without explicit self-serve production entitlement, access should be classified as Gated. 3) Decisions: Auth methods: API Key (API tokens) and Basic Auth (HTTP Basic using the token). API type: REST. Existing MCP: None. Access model: Gated (sales-led). Buildability: Hard (requires outreach/sales for production credentials; auth mechanics are clear but access is gated). Recommended next action: Needs Outreach. Confidence moderate.

## Key decisions
- buildability: **Hard**
- access_model: **Gated** - Production use appears sales-led with no public self-serve checkout; docs show token creation and HTTP Basic auth but do not grant self-serve production entitlement.
- recommended_next_action: **Needs Outreach**
- confidence: **0.63**

## Evidence URLs
- https://developer.gladly.com/rest/index.html#authentication
- https://developer.gladly.com
- https://apis.io/apis/gladly/gladly-webhooks-api/
- https://www.xpay.sh/saas-pricing/gladly/

## Generated record
```json
{
  "app": "Gladly",
  "category": "Support",
  "one_liner": "Gladly has a broad REST API using API tokens with HTTP Basic, but production access is sales-gated.",
  "auth_methods": [
    "API Key",
    "Basic Auth"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Production use appears sales-led with no public self-serve checkout; docs show token creation and HTTP Basic auth but do not grant self-serve production entitlement."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "None",
  "composio_toolkit": "No",
  "buildability": "Hard",
  "main_blocker": "Production credential access appears to require becoming a Gladly customer via sales.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://developer.gladly.com/rest/index.html#authentication",
    "https://developer.gladly.com",
    "https://apis.io/apis/gladly/gladly-webhooks-api/",
    "https://www.xpay.sh/saas-pricing/gladly/"
  ],
  "confidence": 0.63,
  "verification_status": "Auto",
  "slug": "gladly",
  "primary_docs_url": "https://developer.gladly.com/rest/index.html#authentication",
  "rate_limit_note": "Docs mention default rate limits and handling guidance; specific numeric limits are not shown in the cited excerpt.",
  "last_verified": "2026-08-17"
}
```

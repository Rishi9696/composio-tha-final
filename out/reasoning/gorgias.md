# Gorgias - synthesis reasoning
_generated 2026-08-17 | model openai:gpt-5_

## Research trace
- queries: ["Gorgias official API authentication developer documentation", "Gorgias API production access approval credentials official documentation", "Gorgias official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://gorgias.com | HTTP 200 | hint | topics=api,access
- https://developers.gorgias.com/reference/authentication | HTTP 200 | search_result | topics=api,auth
- https://www.gorgias.com/pricing/choose-your-plan | HTTP 200 | search_result | topics=api,access
- https://developers.gorgias.com/docs/oauth2-authentication-for-creating-apps-with-gorgias | HTTP 200 | search_result | topics=api,auth,access
- https://developer.gorgias.com | HTTP 200 | derived_guess | topics=none
- https://developers.gorgias.com | HTTP 200 | derived_guess | topics=api,access

## Model reasoning
1) Evidence: The OAuth2 doc states: "In order to be able to have an approved public app with Gorgias, it is required that the app is using OAuth2 for authentication," and outlines client_id/client_secret, authorization redirect, access token (24h), and refresh token (no expiration). It also shows headings for "Private vs. Public App Authentication" and "Access Tokens (API Keys)." The Developer portal homepage says public apps require joining the Developer Portal and submission for review, and explicitly: "For Private apps there is no need for approval. Go ahead and use it!" The API Reference page lists extensive REST resources, indicating a REST surface. The official MCP help article says: "Available on all Helpdesk plans. Everyone can install the Gorgias MCP," and instructs to add an HTTP MCP server and authenticate with Gorgias; it also notes MCP is in beta. 2) Production Access Rubric: For public REST apps, the OAuth2 doc shows a review step ("Submit app for review"), proving a manual gate. The Developer portal confirms review for public apps and no approval for private apps. For MCP, the help article states "Available on all Helpdesk plans. Everyone can install the Gorgias MCP," implying production use is tied to having a Helpdesk plan (no evidence of free, self-serve production access for new developers). There is no explicit statement that a new developer can obtain production credentials without being a Gorgias customer or without review. Therefore, production access is Gated. 3) Conclusions: Auth methods include OAuth2 (public apps) and API Key (private apps, referenced by the "Access Tokens (API Keys)" section). The dominant API is REST. There is an official MCP. Given review for public apps and plan requirements for MCP/private usage, buildability is Hard, and the next action is Needs Outreach to secure app approval or customer plan access.

## Key decisions
- buildability: **Hard**
- access_model: **Gated** - Public apps require OAuth2 and app review/approval; private apps need no approval but require a Gorgias account; MCP is available only on Helpdesk plans.
- recommended_next_action: **Needs Outreach**
- confidence: **0.71**

## Evidence URLs
- https://developers.gorgias.com/docs/oauth2-authentication-for-creating-apps-with-gorgias
- https://developers.gorgias.com
- https://developers.gorgias.com/reference/authentication
- https://docs.gorgias.com/en-US/connect-your-ai-assistant-to-the-gorgias-mcp-6310546

## Generated record
```json
{
  "app": "Gorgias",
  "category": "Support",
  "one_liner": "Gorgias offers a broad REST API with OAuth2/API keys and an official MCP, but production access is gated.",
  "auth_methods": [
    "OAuth2",
    "API Key"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Public apps require OAuth2 and app review/approval; private apps need no approval but require a Gorgias account; MCP is available only on Helpdesk plans."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Hard",
  "main_blocker": "Public app review for REST access and Helpdesk plan requirement for MCP/private use; no clear self-serve production path.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://developers.gorgias.com/docs/oauth2-authentication-for-creating-apps-with-gorgias",
    "https://developers.gorgias.com",
    "https://developers.gorgias.com/reference/authentication",
    "https://docs.gorgias.com/en-US/connect-your-ai-assistant-to-the-gorgias-mcp-6310546"
  ],
  "confidence": 0.71,
  "verification_status": "Auto",
  "slug": "gorgias",
  "primary_docs_url": "https://developers.gorgias.com/docs/oauth2-authentication-for-creating-apps-with-gorgias",
  "rate_limit_note": "Rate limit details are in the API Reference but not specified in the fetched excerpts.",
  "last_verified": "2026-08-17"
}
```

<!-- final-state:start -->
## Final pipeline state
_Updated 2026-08-18 by current human handcheck correction; this supersedes earlier key decisions._

```json
{
  "app": "Gorgias",
  "category": "Support",
  "one_liner": "Gorgias offers a broad REST API with OAuth2/API keys and an official MCP, but production access is gated.",
  "auth_methods": [
    "Basic Auth",
    "API Key",
    "OAuth2"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Gorgias provides a seven-day trial; continued production API and MCP use requires a paid plan."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "Production credentials require an existing paid customer account.",
  "recommended_next_action": "Partner-Gated",
  "evidence_urls": [
    "https://developers.gorgias.com/reference/authentication",
    "https://developers.gorgias.com/docs/access-tokens-api-keys",
    "https://www.gorgias.com/pricing/choose-your-plan",
    "https://docs.gorgias.com/en-US/connect-your-ai-assistant-to-the-gorgias-mcp-6310546"
  ],
  "confidence": 0.71,
  "verification_status": "Hand-Checked",
  "slug": "gorgias",
  "primary_docs_url": "https://developers.gorgias.com/reference/authentication",
  "rate_limit_note": "Rate limit details are in the API Reference but not specified in the fetched excerpts.",
  "last_verified": "2026-08-17"
}
```
<!-- final-state:end -->

# Google Ads - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Google Ads official API authentication developer documentation", "Google Ads API production access approval credentials official documentation", "Google Ads official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://developers.google.com/google-ads | HTTP 200 | hint | topics=api
- https://developers.google.com/google-ads/api/docs/oauth/user-authentication?hl=en&utm_source=openai | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://developers.google.com/google-ads/api/docs/productionize/access-levels?utm_source=openai | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://developers.google.com/google-ads/api/rest/auth?hl=en&utm_source=openai | HTTP 200 | search_result | topics=api,auth,access
- https://developer.google.com | HTTP 200 | derived_guess | topics=api,auth,access
- https://developers.google.com | HTTP 200 | derived_guess | topics=api,auth,access

## Model reasoning
1) What the evidence states:
- API surface/auth: The "Authorization with REST" page is specifically about authorization and HTTP headers for the Google Ads API REST interface (developers.google.com/google-ads/api/rest/auth). The "User authentication workflow" page exists for Google Ads API and indicates OAuth-based user auth flows (developers.google.com/google-ads/api/docs/oauth/user-authentication). The REST docs navigation also explicitly lists "REST API Introduction" and "Authorization with REST," confirming REST as a public surface.
- MCP: There is an official Google-hosted page for a "Google Ads MCP server" under developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server, indicating an official MCP integration guide. The a2a-mcp.org entry explicitly says: "Official open-source Model Context Protocol (MCP) server from Google" and describes capabilities (GAQL support), notes it is "Currently read-only," and that it runs locally with proper "OAuth/service account credentials."
- Access/production: There is a Google Ads API "Access levels ... productionize" page (developers.google.com/google-ads/api/docs/productionize/access-levels) which, by its title and placement, addresses access levels for productionizing. However, the fetched content is largely navigational; no explicit sentence about automatic self-serve production entitlement is visible in the excerpts.

2) Production Access Rubric application:
- I cannot find a sentence in the fetched excerpts that states production access is self-serve. The presence of the "Access levels ... productionize" page indicates gating/levels, but the page content in our fetch does not provide a verbatim line. Per the rubric, without explicit evidence of self-serve production entitlement, we must classify as Gated.

3) Decisions:
- auth_methods: OAuth2 is clearly indicated by the dedicated user authentication and REST authorization pages. Although the a2a page mentions service accounts for the MCP server, I’m not elevating that to a global Ads API method here without a vendor-quote; thus listing OAuth2 only.
- api_type: REST is the dominant public API per the REST authorization and navigation references. MCP exists as an additional surface, but REST remains primary.
- existing_mcp: Official, since Google hosts a "Google Ads MCP server" page on developers.google.com. The a2a listing corroborates and adds details (read-only, GAQL support).
- access_model: Gated, because we have no explicit self-serve production entitlement in the fetched content and an "access levels/productionize" page exists, implying approval levels.
- buildability: Hard, due to production access gating/approval and thin explicit access text, even though overall docs appear extensive.
- recommended_next_action: Needs Outreach, to pursue production access/approval per the access levels process.
- Rate limits: Not specified in the fetched excerpts.

## Key decisions
- buildability: **Hard**
- access_model: **Gated** - Production use appears subject to access levels/approval per the Google Ads API productionize/access-levels page; no evidence of self-serve production credentials.
- recommended_next_action: **Needs Outreach**
- confidence: **0.56**

## Evidence URLs
- https://developers.google.com/google-ads/api/rest/auth?hl=en&utm_source=openai
- https://developers.google.com/google-ads/api/docs/oauth/user-authentication?hl=en&utm_source=openai
- https://developers.google.com/google-ads/api/docs/productionize/access-levels?utm_source=openai
- https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server?utm_source=openai
- https://a2a-mcp.org/entry/google-ads-mcp?utm_source=openai

## Generated record
```json
{
  "app": "Google Ads",
  "category": "Ads/Marketing",
  "one_liner": "Google Ads API uses OAuth2; production access is gated; an official read-only MCP server exists for GAQL querying.",
  "auth_methods": [
    "OAuth2"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Production use appears subject to access levels/approval per the Google Ads API productionize/access-levels page; no evidence of self-serve production credentials."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Hard",
  "main_blocker": "Production access requires access-level approval; explicit self-serve production entitlement is not shown in fetched docs.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://developers.google.com/google-ads/api/rest/auth?hl=en&utm_source=openai",
    "https://developers.google.com/google-ads/api/docs/oauth/user-authentication?hl=en&utm_source=openai",
    "https://developers.google.com/google-ads/api/docs/productionize/access-levels?utm_source=openai",
    "https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server?utm_source=openai",
    "https://a2a-mcp.org/entry/google-ads-mcp?utm_source=openai"
  ],
  "confidence": 0.56,
  "verification_status": "Auto",
  "slug": "google-ads",
  "primary_docs_url": "https://developers.google.com/google-ads/api/docs/oauth/user-authentication?hl=en&utm_source=openai",
  "rate_limit_note": "Rate limits are not described in the fetched excerpts.",
  "last_verified": "2026-08-18"
}
```

## Risk seed (withheld from synthesis)
This prior was retained only for audit sampling and was not shown to the model.
```json
{
  "access_model": "Gated",
  "recommended_next_action": "Needs Outreach",
  "main_blocker": "Requires a developer token approval + OAuth; not instant self-serve."
}
```

<!-- final-state:start -->
## Final pipeline state
_Updated 2026-08-18 by current human handcheck correction; this supersedes earlier key decisions._

```json
{
  "app": "Google Ads",
  "category": "Ads/Marketing",
  "one_liner": "Google Ads API uses OAuth2; production access is gated; an official read-only MCP server exists for GAQL querying.",
  "auth_methods": [
    "OAuth2",
    "API Key",
    "Service Account"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Production use appears subject to access levels/approval per the Google Ads API productionize/access-levels page; no evidence of self-serve production credentials."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Hard",
  "main_blocker": "Production access requires access-level approval; explicit self-serve production entitlement is not shown in fetched docs.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://developers.google.com/google-ads/api/docs/oauth/overview",
    "https://developers.google.com/google-ads/api/docs/api-policy/developer-token",
    "https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server"
  ],
  "confidence": 0.56,
  "verification_status": "Hand-Checked",
  "slug": "google-ads",
  "primary_docs_url": "https://developers.google.com/google-ads/api/docs/oauth/overview",
  "rate_limit_note": "Rate limits are not described in the fetched excerpts.",
  "last_verified": "2026-08-18"
}
```
<!-- final-state:end -->

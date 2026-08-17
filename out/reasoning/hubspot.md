# HubSpot - synthesis reasoning
_generated 2026-08-17 | model openai:gpt-5_

## Research trace
- queries: ["HubSpot official API authentication developer documentation", "HubSpot API production access approval credentials official documentation", "HubSpot official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://hubspot.com | HTTP 200 | hint | topics=access
- https://www.acucoders.com/guides/hubspot-api-credentials/ | HTTP 200 | search_result | topics=api,auth,access
- https://apispine.com/hubspot-api/pricing | HTTP 200 | search_result | topics=api,access
- https://www.iv-lead.com/blog/hubspot-api-reference-documentation | HTTP 200 | search_result | topics=api,auth,access
- https://developer.hubspot.com | HTTP 200 | derived_guess | topics=api,access
- https://developers.hubspot.com | HTTP 200 | derived_guess | topics=api,access

## Model reasoning
1) What the evidence states:
- MCP: HubSpot offers two MCP servers (remote and developer). The remote MCP server enables secure read/write access to HubSpot CRM data and requires configuring an app to authenticate requests; docs cover PKCE and token refresh, indicating OAuth2 is used (developers.hubspot.com/mcp; developers.hubspot.com/docs/apps/developer-platform/build-apps/integrate-with-the-remote-hubspot-mcp-server). A third-party guide adds it works with OAuth 2.1 with PKCE, is GA, and usage counts against normal API limits (hubjoy.co/hubspot/mcp-connector).
- REST API: A third-party summary states HubSpot APIs follow REST conventions under https://api.hubapi.com and return JSON (iv-lead.com/blog/hubspot-api-reference-documentation).
- Auth credentials: A third-party guide lists OAuth 2.0 and describes “Private App Tokens (Recommended)” for HubSpot API access; it also notes legacy API keys were deprecated (acucoders.com/guides/hubspot-api-credentials/).
- Access/plan info: A third-party pricing overview says there is a Free Tier and API access is included with HubSpot product subscriptions; rate limits vary by subscription tier (apispine.com/hubspot-api/pricing). For MCP, a third-party guide states it “works on every HubSpot plan at no extra cost,” and each teammate authenticates with their own HubSpot login; usage via MCP counts against normal API limits (hubjoy.co/hubspot/mcp-connector).

2) Production Access Rubric application:
- MCP: Evidence explicitly indicates broad availability with no extra cost and standard OAuth login (“works on every HubSpot plan at no extra cost… each teammate then authenticates with their own HubSpot login”), supporting Self-Serve production access for the official MCP surface (hubjoy.co/hubspot/mcp-connector) and aligning with the official MCP auth setup docs (developers.hubspot.com/.../integrate-with-the-remote-hubspot-mcp-server).
- REST: Evidence indicates API access is bundled with subscriptions, including a free tier, and rate limits vary by tier (“API access included with HubSpot product subscriptions… Free Tier Yes; Rate Limits vary by tier” — apispine.com). No explicit manual approval requirement is shown in the fetched official docs; this suggests self-serve but with slightly lower confidence than MCP.

3) Decisions:
- Auth methods: OAuth2 is clearly evidenced for both MCP and OAuth apps. While third-party docs describe “Private App Tokens,” the exact controlled-vocabulary label is not named in the evidence; to avoid mismatch, list OAuth2 only.
- API type: REST is the dominant public API; MCP exists as an additional protocol surface to those APIs.
- Existing MCP: Official, per HubSpot’s own MCP documentation.
- Access model: Self-Serve, anchored by MCP’s all-plan availability and OAuth login; note REST access ties to subscription tiers with a free tier per third-party.
- Buildability: Easy, given self-serve MCP OAuth setup and broadly documented REST APIs.
- Next action: Build Now, starting with the official MCP server or REST via OAuth.

## Key decisions
- buildability: **Easy**
- access_model: **Self-Serve** - Official MCP server is GA and available on every HubSpot plan at no extra cost; authenticate via OAuth2 with PKCE (developers.hubspot.com; hubjoy.co). REST access is available via OAuth apps; API access is included with HubSpot subscriptions and a free tier exists; rate limits vary by tier (apispine.com).
- recommended_next_action: **Build Now**
- confidence: **0.72**

## Evidence URLs
- https://developers.hubspot.com/mcp
- https://developers.hubspot.com/docs/apps/developer-platform/build-apps/integrate-with-the-remote-hubspot-mcp-server
- https://www.acucoders.com/guides/hubspot-api-credentials/
- https://www.iv-lead.com/blog/hubspot-api-reference-documentation
- https://apispine.com/hubspot-api/pricing
- https://www.hubjoy.co/hubspot/mcp-connector

## Generated record
```json
{
  "app": "HubSpot",
  "category": "CRM",
  "one_liner": "HubSpot provides REST APIs and an official MCP server with self-serve OAuth access across all plans.",
  "auth_methods": [
    "OAuth2"
  ],
  "access_model": {
    "kind": "Self-Serve",
    "note": "Official MCP server is GA and available on every HubSpot plan at no extra cost; authenticate via OAuth2 with PKCE (developers.hubspot.com; hubjoy.co). REST access is available via OAuth apps; API access is included with HubSpot subscriptions and a free tier exists; rate limits vary by tier (apispine.com)."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Easy",
  "main_blocker": "None beyond requiring a HubSpot portal and adhering to plan-based API limits.",
  "recommended_next_action": "Build Now",
  "evidence_urls": [
    "https://developers.hubspot.com/mcp",
    "https://developers.hubspot.com/docs/apps/developer-platform/build-apps/integrate-with-the-remote-hubspot-mcp-server",
    "https://www.acucoders.com/guides/hubspot-api-credentials/",
    "https://www.iv-lead.com/blog/hubspot-api-reference-documentation",
    "https://apispine.com/hubspot-api/pricing",
    "https://www.hubjoy.co/hubspot/mcp-connector"
  ],
  "confidence": 0.72,
  "verification_status": "Auto",
  "slug": "hubspot",
  "primary_docs_url": "https://www.acucoders.com/guides/hubspot-api-credentials/",
  "rate_limit_note": "API limits vary by subscription tier; MCP usage counts against normal API limits.",
  "last_verified": "2026-08-17"
}
```

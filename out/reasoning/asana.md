# Asana - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Asana official API authentication developer documentation", "Asana API production access approval credentials official documentation", "Asana official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://developers.asana.com | HTTP 200 | hint | topics=api,auth
- https://developers.asana.com/docs/authentication | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://asana.com/pricing | HTTP 200 | search_result | topics=auth,access
- https://developers.asana.com/docs/api-explorer | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://developer.asana.com | HTTP 200 | derived_guess | topics=api,access
- https://docs.asana.com | HTTP 404 | derived_guess | topics=none

## Model reasoning
1) What the evidence states:
- REST API surface: The API Explorer says you can "make API requests (and view responses) directly in your browser" and that by authenticating with a personal access token you will be "operating on real data" in your Asana instance (developers.asana.com/docs/api-explorer).
- Auth credentials: The Authentication page states a "personal access token (PAT) is the quickest and simplest way to authenticate," and explicitly: "Using a PAT with your production app is a sufficient option" for scripts/simple apps (developers.asana.com/docs/authentication). OAuth app setup is documented across the site and in the MCP integration guide.
- MCP surface: Asana provides an official MCP server; the integration guide says you "create an OAuth app in the Asana developer console and use it to authenticate your MCP client" (developers.asana.com/docs/mcp-server; developers.asana.com/docs/integrating-with-asanas-mcp-server).
- Pricing/account: The pricing page shows a "Personal" tier at "$0 Free forever" (asana.com/pricing). It does not explicitly state API production access is included on the free tier.

2) Production Access Rubric application:
- There is clear evidence that PATs are usable for production apps and operate on real data. However, there is no explicit sentence confirming that a new developer on a free plan can obtain production credentials without any manual approval or payment. The pricing page shows a free plan but does not explicitly grant production API entitlement. Therefore, per the rubric, without explicit proof of free self-serve production access, classify as Gated.

3) Decisions derived:
- Auth methods: Personal Access Token and OAuth2 are documented. 
- API type: REST is the dominant public surface; MCP exists as an additional official surface.
- Existing MCP: Official, per Asana-hosted MCP docs.
- Access model: Gated (lack of explicit self-serve production entitlement text for free users despite PAT production wording).
- Buildability: Moderate (docs are clear and auth is standard, but production entitlement ambiguity requires confirmation).
- Next action: Needs Outreach to confirm production API access terms (especially for free vs paid) and any approval steps.
- Evidence is sufficient but lacks explicit production entitlement language for free/self-serve; confidence slightly reduced.

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - Docs allow PATs for production use and show OAuth app creation, but no explicit statement that new developers get production API access without approval or a paid plan.
- recommended_next_action: **Needs Outreach**
- confidence: **0.69**

## Evidence URLs
- https://developers.asana.com/docs/authentication
- https://developers.asana.com/docs/api-explorer
- https://asana.com/pricing
- https://developers.asana.com/docs/mcp-server
- https://developers.asana.com/docs/integrating-with-asanas-mcp-server

## Generated record
```json
{
  "app": "Asana",
  "category": "Productivity/PM",
  "one_liner": "Asana has a robust REST API and official MCP, but production access terms need confirmation.",
  "auth_methods": [
    "Personal Access Token",
    "OAuth2"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Docs allow PATs for production use and show OAuth app creation, but no explicit statement that new developers get production API access without approval or a paid plan."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "No explicit confirmation that free-tier users get self-serve production API credentials.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://developers.asana.com/docs/authentication",
    "https://developers.asana.com/docs/api-explorer",
    "https://asana.com/pricing",
    "https://developers.asana.com/docs/mcp-server",
    "https://developers.asana.com/docs/integrating-with-asanas-mcp-server"
  ],
  "confidence": 0.69,
  "verification_status": "Auto",
  "slug": "asana",
  "primary_docs_url": "https://developers.asana.com/docs/authentication",
  "rate_limit_note": "API has rate limits; confirm limits and whether they vary by plan before scaling.",
  "last_verified": "2026-08-18"
}
```

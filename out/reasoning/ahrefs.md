# Ahrefs - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Ahrefs official API authentication developer documentation", "Ahrefs API production access approval credentials official documentation", "Ahrefs official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://ahrefs.com/api | HTTP 200 | hint | topics=api,auth,mcp
- https://docs.ahrefs.com/en/api/docs/introduction | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://ahrefs.com/pricing | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://docs.ahrefs.com/en/ahrefs-connect/docs/api-guide | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://developer.ahrefs.com | HTTP 404 | derived_guess | topics=none
- https://developers.ahrefs.com | HTTP 404 | derived_guess | topics=none

## Model reasoning
1) What the evidence states: Ahrefs exposes a public REST API v3 with many endpoints (Site Explorer, Keywords Explorer, Rank Tracker, Site Audit, SERP Overview, Batch Analysis, etc.). The API docs explicitly include “API keys creation and management” and describe plan-based unit consumption with a minimum cost per paid request. Eligibility states: “Ahrefs API is available on eligible paid plans. On all other plans, you'll still have access to a limited set of free test queries.” Ahrefs Connect (developer platform) uses OAuth flows: “when your app is first created, it will be in Inactive status… you can test OAuth flows… Once your app is approved and activated, production requests will consume units,” and it links to an Approval process. For MCP, Ahrefs provides a hosted MCP server: “allows users with a Lite plan or higher to connect their Ahrefs account,” and “The remote MCP server is available on paid plans starting from Lite,” with limits documented in the Help Center. 2) Production Access Rubric: The REST API page explicitly gates production to paid plans (“available on eligible paid plans… limited set of free test queries” otherwise), so not self-serve production. Ahrefs Connect requires manual app approval (“Once your app is approved and activated”), so production via OAuth is gated. MCP requires a paid plan (“users with a Lite plan or higher… available on paid plans starting from Lite”), so also gated. There is no evidence of free, self-serve production credentials. 3) Decisions: Auth methods are API Key (REST) and OAuth2 (Ahrefs Connect). Dominant public surface is REST; MCP exists as an official hosted server. Access model is Gated due to paid plan requirement and/or app approval. Docs are clear but production requires purchase/approval, so buildability is Moderate. Next action: Needs Outreach (apply for Ahrefs Connect approval or secure a paid plan for API key use).

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - REST API v3 is available on eligible paid plans; others get only limited free test queries. Ahrefs Connect apps must be approved before production. MCP access is available on paid plans (Lite+).
- recommended_next_action: **Needs Outreach**
- confidence: **0.88**

## Evidence URLs
- https://docs.ahrefs.com/en/api/docs/introduction
- https://docs.ahrefs.com/en/ahrefs-connect/docs/api-guide
- https://docs.ahrefs.com/en/mcp/docs/introduction
- https://help.ahrefs.com/en/articles/13913559-getting-started-with-ahrefs-mcp
- https://ahrefs.com/api

## Generated record
```json
{
  "app": "Ahrefs",
  "category": "Research/Scraping",
  "one_liner": "Ahrefs offers REST API keys and OAuth apps; production requires a paid plan and/or app approval.",
  "auth_methods": [
    "API Key",
    "OAuth2"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "REST API v3 is available on eligible paid plans; others get only limited free test queries. Ahrefs Connect apps must be approved before production. MCP access is available on paid plans (Lite+)."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "Production use requires a paid Ahrefs plan or Ahrefs Connect app approval; no self-serve production credentials.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://docs.ahrefs.com/en/api/docs/introduction",
    "https://docs.ahrefs.com/en/ahrefs-connect/docs/api-guide",
    "https://docs.ahrefs.com/en/mcp/docs/introduction",
    "https://help.ahrefs.com/en/articles/13913559-getting-started-with-ahrefs-mcp",
    "https://ahrefs.com/api"
  ],
  "confidence": 0.88,
  "verification_status": "Auto",
  "slug": "ahrefs",
  "primary_docs_url": "https://docs.ahrefs.com/en/api/docs/introduction",
  "rate_limit_note": "Most endpoints consume API units; minimum 50 units per paid request. Free test queries are available; consumed units are non-refundable.",
  "last_verified": "2026-08-18"
}
```

## Risk seed (withheld from synthesis)
This prior was retained only for audit sampling and was not shown to the model.
```json
{
  "access_model": "Gated",
  "recommended_next_action": "Needs Outreach",
  "main_blocker": "API access likely requires a paid Ahrefs plan at a certain tier (verify)."
}
```

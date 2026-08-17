# Copper - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Copper official API authentication developer documentation", "Copper API production access approval credentials official documentation", "Copper official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://copper.com | HTTP 200 | hint | topics=api,access
- https://developer.copper.com/introduction/authentication.html | HTTP 200 | search_result | topics=api,auth,access
- https://www.copper.com/pricing?offset=-600&utm_source=openai | HTTP 200 | search_result | topics=api,access
- https://developer.copper.co/api-reference/authentication | HTTP 200 | search_result | topics=api,auth,access
- https://developer.copper.com | HTTP 200 | derived_guess | topics=api,auth
- https://developers.copper.com | HTTP 0 | derived_guess | topics=none

## Model reasoning
1) Evidence states: The Copper Developer API docs (developer.copper.com) have an Authentication Overview listing two methods: “API Keys” and “OAuth2.0,” and the site navigation shows many REST resources (Leads, People, Companies, Opportunities, Projects, Tasks, Activities, Custom Fields, etc.), indicating a broad REST API. No pages mention an MCP server or MCP support. The copper.co portal we found describes service accounts and blockchain endpoints, which are for a different company (crypto) and not Copper CRM, so it is not applicable here. 2) Production Access Rubric: The authentication page explains API Keys and OAuth2.0 but does not state that a new developer can obtain production credentials without approval or a paid plan. The Copper pricing page fetched does not mention API access terms or a free/self-serve production entitlement. With no explicit statement of self-serve production access, we must classify access as Gated per the rubric. 3) Therefore: auth_methods are API Key and OAuth2; api_type is REST; existing_mcp is None; access_model is Gated due to lack of proof of self-serve production access; buildability is Moderate (clear REST docs with OAuth/app setup, but access terms unclear); recommended_next_action is Needs Outreach to confirm production API availability and plan/approval requirements.

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - Docs show API Keys and OAuth2 but provide no evidence that new developers get production credentials self-serve; confirm plan/approval requirements.
- recommended_next_action: **Needs Outreach**
- confidence: **0.55**

## Evidence URLs
- https://developer.copper.com/introduction/authentication.html
- https://developer.copper.com
- https://www.copper.com/pricing?offset=-600&utm_source=openai

## Generated record
```json
{
  "app": "Copper",
  "category": "CRM",
  "one_liner": "Copper CRM exposes a broad REST API with API keys and OAuth; production access terms are not clearly stated.",
  "auth_methods": [
    "API Key",
    "OAuth2"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Docs show API Keys and OAuth2 but provide no evidence that new developers get production credentials self-serve; confirm plan/approval requirements."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "None",
  "composio_toolkit": "No",
  "buildability": "Moderate",
  "main_blocker": "No explicit proof of self-serve production API access or plan requirements in the cited docs.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://developer.copper.com/introduction/authentication.html",
    "https://developer.copper.com",
    "https://www.copper.com/pricing?offset=-600&utm_source=openai"
  ],
  "confidence": 0.55,
  "verification_status": "Auto",
  "slug": "copper",
  "primary_docs_url": "https://developer.copper.com/introduction/authentication.html",
  "rate_limit_note": "No rate limit details found on the cited pages.",
  "last_verified": "2026-08-18"
}
```

# Zendesk - synthesis reasoning
_generated 2026-08-17 | model openai:gpt-5_

## Research trace
- queries: ["Zendesk official API authentication developer documentation", "Zendesk API production access approval credentials official documentation", "Zendesk official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://zendesk.com | HTTP 200 | hint | topics=auth,access
- https://developer.zendesk.com/api-reference/introduction/security-and-auth/ | HTTP 200 | search_result | topics=api,auth,access
- https://apis.io/plans/zendesk/zendesk-plans-pricing/ | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://developer.zendesk.com/documentation/conversations/getting-started/api-authentication/ | HTTP 200 | search_result | topics=api,auth,access
- https://developer.zendesk.com | HTTP 200 | derived_guess | topics=api,auth,access
- https://developers.zendesk.com | HTTP 200 | derived_guess | topics=api,access

## Model reasoning
1) What the evidence states: The Zendesk Security and authentication doc says: “You must be a verified user to make API requests. Zendesk supports using OAuth access tokens… Note: If you’re an existing Zendesk customer and are currently using basic authentication or API tokens, you will have to migrate to OAuth access tokens…” and if distributing to multiple customers “you must use global OAuth tokens.” This indicates the primary REST API supports OAuth2, with API tokens (deprecated) and Basic Auth historically present. The Sunshine Conversations auth guide states its scheme is distinct from Zendesk API tokens and supports “basic authentication and bearer tokens (via JWT)… Both… require you to generate an API key in Admin Center,” which applies to the Sunshine Conversations API, not the core Support API. The developer homepage advertises “Try out the Sunshine Platform with a free, 14-day trial account,” and lists multiple API areas (Ticketing, Help Center, Messaging, Voice, Chat), showing a broad REST surface. For MCP, we only have community servers (Stork/Fruggr, CData, UBOS); there’s no official Zendesk-hosted MCP documentation in the fetched sources. 2) Production Access Rubric: The APIs.io plans page states “API access is included with every paid plan; per‑plan API request rate limits scale with the tier … and a separate ‘High Volume API’ add‑on…” and the dev homepage offers only a “free, 14‑day trial,” not a free production tier. The Security and authentication page also requires being a “verified user.” Together, this indicates production access is tied to being a paying Zendesk customer (or limited trial), so it is Gated, not self‑serve production. 3) Decisions: Auth methods for the dominant public REST API are OAuth2, with legacy API token (API Key) and Basic Auth mentioned as being migrated away from; Sunshine Conversations' JWT/Bearer is a separate product and not used as the dominant Support API method. The dominant api_type is REST with broad breadth. Existing MCP is Community (third‑party servers). Access model is Gated due to paid plan requirement and verified-user constraints. Buildability is Moderate (clear docs and OAuth app setup, but production requires a paid plan). Next action: Needs Outreach (procure a paid Zendesk plan or engage sales). Rate limits are per‑plan, with a High Volume API add‑on per APIs.io.

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - Production API use requires being a verified user on a paid Zendesk plan; only a 14-day trial is offered for new accounts. APIs.io notes API access is included with paid plans and a High Volume API add-on is available.
- recommended_next_action: **Needs Outreach**
- confidence: **0.72**

## Evidence URLs
- https://developer.zendesk.com/api-reference/introduction/security-and-auth/
- https://developer.zendesk.com/documentation/conversations/getting-started/api-authentication/
- https://developer.zendesk.com
- https://apis.io/plans/zendesk/zendesk-plans-pricing/

## Generated record
```json
{
  "app": "Zendesk",
  "category": "Support",
  "one_liner": "Zendesk offers broad REST APIs using OAuth2; production access is gated to paid, verified accounts.",
  "auth_methods": [
    "OAuth2",
    "API Key",
    "Basic Auth"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Production API use requires being a verified user on a paid Zendesk plan; only a 14-day trial is offered for new accounts. APIs.io notes API access is included with paid plans and a High Volume API add-on is available."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Community",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "Production credentials require a paid Zendesk subscription; access limited to verified users within a Zendesk instance.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://developer.zendesk.com/api-reference/introduction/security-and-auth/",
    "https://developer.zendesk.com/documentation/conversations/getting-started/api-authentication/",
    "https://developer.zendesk.com",
    "https://apis.io/plans/zendesk/zendesk-plans-pricing/"
  ],
  "confidence": 0.72,
  "verification_status": "Auto",
  "slug": "zendesk",
  "primary_docs_url": "https://developer.zendesk.com/documentation/conversations/getting-started/api-authentication/",
  "rate_limit_note": "Per-plan rate limits apply; a High Volume API add-on can raise limits (e.g., up to 2,500 req/min for qualifying plans per APIs.io).",
  "last_verified": "2026-08-17"
}
```

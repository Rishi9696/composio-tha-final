# Freshdesk - synthesis reasoning
_generated 2026-08-17 | model openai:gpt-5_

## Research trace
- queries: ["Freshdesk official API authentication developer documentation", "Freshdesk API production access approval credentials official documentation", "Freshdesk official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://freshdesk.com | HTTP 200 | hint | topics=access,mcp
- https://support.freshdesk.com/support/solutions/articles/225435-where-can-i-find-my-api-key | HTTP 200 | search_result | topics=api,auth,access
- https://www.freshworks.com/freshdesk/pricing/ | HTTP 200 | search_result | topics=auth,access
- https://developer.freshdesk.com/api/v1/ | HTTP 200 | search_result | topics=api,auth,access
- https://developer.freshdesk.com | HTTP 200 | derived_guess | topics=api,access
- https://developers.freshdesk.com | HTTP 200 | derived_guess | topics=api,access

## Model reasoning
1) Evidence states: Freshdesk has public API documentation with REST endpoints (tickets, users, agents, companies, forums) and mentions a Rate Limit section (developer.freshdesk.com/api/v1). A Freshdesk Support article explains how to obtain an API key and explicitly notes: "If your account is on the Sprout plan, the API key and the API functionality will NOT be available" (support.freshdesk.com/.../225435). The pricing page lists paid plans and try-it-free options but does not confirm API availability in a free production tier (freshworks.com/freshdesk/pricing). An official Freshdesk support article describes a Freshworks MCP server integration as an EAP, indicating hosted MCP connectivity that uses public APIs and supported auth methods (support.freshdesk.com/.../mcp-integration-in-freshdesk-eap-). No fetched evidence explicitly documents OAuth2 or other auth types beyond API key. 2) Applying the Production Access Rubric: The Sprout/free plan restriction proves production API access is not self-serve free: "API key and the API functionality will NOT be available" on Sprout. The MCP is labeled EAP, implying enablement/approval. There is no statement guaranteeing that a new developer can get production credentials without approval or payment. Therefore, access is Gated. 3) Conclusions: auth_methods = [API Key]; api_type = REST; existing_mcp = Official (vendor EAP MCP); access_model = Gated (free plan lacks API; MCP is EAP); buildability = Moderate (clear REST surface with API key, but production gated by plan/EAP and v1 docs shown are dated); recommended_next_action = Needs Outreach (obtain a paid plan and/or request MCP EAP enablement).

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - Freshdesk’s API key and API functionality are not available on the Sprout (free) plan; production use requires a paid plan. The official MCP integration is in EAP and requires enablement.
- recommended_next_action: **Needs Outreach**
- confidence: **0.63**

## Evidence URLs
- https://support.freshdesk.com/support/solutions/articles/225435-where-can-i-find-my-api-key
- https://developer.freshdesk.com/api/v1/
- https://www.freshworks.com/freshdesk/pricing/
- https://support.freshdesk.com/support/solutions/articles/50000012670-model-context-protocol-mcp-integration-in-freshdesk-eap-

## Generated record
```json
{
  "app": "Freshdesk",
  "category": "Support",
  "one_liner": "Freshdesk has a REST API with API keys, but production access requires a paid plan; MCP is an EAP integration.",
  "auth_methods": [
    "API Key"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Freshdesk’s API key and API functionality are not available on the Sprout (free) plan; production use requires a paid plan. The official MCP integration is in EAP and requires enablement."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "API access is unavailable on the free/Sprout plan; the official MCP integration is EAP-gated.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://support.freshdesk.com/support/solutions/articles/225435-where-can-i-find-my-api-key",
    "https://developer.freshdesk.com/api/v1/",
    "https://www.freshworks.com/freshdesk/pricing/",
    "https://support.freshdesk.com/support/solutions/articles/50000012670-model-context-protocol-mcp-integration-in-freshdesk-eap-"
  ],
  "confidence": 0.63,
  "verification_status": "Auto",
  "slug": "freshdesk",
  "primary_docs_url": "https://support.freshdesk.com/support/solutions/articles/225435-where-can-i-find-my-api-key",
  "rate_limit_note": "API docs include a Rate Limit section, but exact limits are not specified in the cited excerpts.",
  "last_verified": "2026-08-17"
}
```

<!-- final-state:start -->
## Final pipeline state
_Updated 2026-08-18 by current handcheck fold; this supersedes earlier key decisions._

```json
{
  "app": "Freshdesk",
  "category": "Support",
  "one_liner": "Freshdesk has a REST API with API keys, but production access requires a paid plan; MCP is an EAP integration.",
  "auth_methods": [
    "API Key",
    "Basic Auth"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Freshdesk Free currently permits zero API calls; production API use requires a paid Growth, Pro, or Enterprise account."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "Production API credentials require an existing paid Freshdesk customer account.",
  "recommended_next_action": "Partner-Gated",
  "evidence_urls": [
    "https://developers.freshdesk.com/api/",
    "https://partnersupport.freshworks.com/support/solutions/articles/225439-what-are-the-rate-limits-for-the-api-calls-to-freshdesk-",
    "https://support.freshdesk.com/support/solutions/articles/50000012670-model-context-protocol-mcp-integration-in-freshdesk-eap-"
  ],
  "confidence": 0.63,
  "verification_status": "Hand-Checked",
  "slug": "freshdesk",
  "primary_docs_url": "https://developers.freshdesk.com/api/",
  "rate_limit_note": "API docs include a Rate Limit section, but exact limits are not specified in the cited excerpts.",
  "last_verified": "2026-08-17"
}
```
<!-- final-state:end -->

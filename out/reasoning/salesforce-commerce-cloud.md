# Salesforce Commerce Cloud - synthesis reasoning
_generated 2026-08-17 | model openai:gpt-5_

## Research trace
- queries: ["Salesforce Commerce Cloud official API authentication developer documentation", "Salesforce Commerce Cloud API production access approval credentials official documentation", "Salesforce Commerce Cloud official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://developer.salesforce.com/docs/commerce | HTTP 403 | hint | topics=none
- https://developer.salesforce.com/docs/commerce/commerce-solutions/guide/custom-api-authentication.html | HTTP 403 | search_result | topics=none
- https://www.salesforce.com/products/commerce-cloud/pricing/ | HTTP 200 | search_result | topics=access
- https://developer.salesforce.com/docs/commerce/commerce-api/guide/authorization-for-admin-apis.html | HTTP 403 | search_result | topics=none
- https://developer.salesforce.com/docs/commerce/account-manager/guide/account-manager-get-started.html | HTTP 403 | derived_guess | topics=none
- https://developer.salesforce.com/docs/commerce/commerce-api/guide/authorization.html | HTTP 200 | browser_verified_summary | topics=api,auth,access

## Model reasoning
1) Evidence states: - Salesforce B2C Commerce APIs use OAuth 2.1 scopes; “Admin tokens require an API client in Account Manager and the oauth2/access_token endpoint.” (developer.salesforce.com authorization page). - An SFCC MCP server exists that “supports OCAPI authentication… client credentials flow,” “support[s] all SFCC GET Data API endpoints,” and “require[s] pre-configuration of API client permissions.” (mcp.aibase.com). - An Agentforce/ACP connector page lists a Salesforce Commerce Cloud connector (docs.agentforcemcp.com), but the fetched content is index-like and does not detail auth; it does evidence a connector exists. - The Commerce Cloud pricing page content fetched doesn’t state anything actionable about API access. 2) Production Access Rubric: The authorization doc explicitly requires an API client in Account Manager to obtain admin tokens. There is no statement that a new developer can obtain production credentials self-serve without being a customer or getting manual approval. The MCP server page also notes preconfiguration of API client permissions. No evidence of free/self-serve production entitlement. Therefore, classify as Gated. 3) Conclusions: Auth methods: OAuth2 (client-credentials/standard OAuth2.1). API type: REST (SCAPI/OCAPI context, and MCP page references Data API endpoints). Existing MCP: Community (third-party MCP server listing and ACP connector docs; no vendor-hosted MCP connector evidence). Access model: Gated due to Account Manager requirement and no self-serve proof. Buildability: Hard (requires Commerce Cloud org and configured API client; docs for auth are clear but access is gated). Next action: Needs Outreach to a Commerce Cloud admin/Salesforce to obtain/enable API client. Rate limits: not documented in cited pages.

## Key decisions
- buildability: **Hard**
- access_model: **Gated** - Admin/API access requires creating an API client in Salesforce Account Manager; no evidence of self-serve production credentials.
- recommended_next_action: **Needs Outreach**
- confidence: **0.62**

## Evidence URLs
- https://developer.salesforce.com/docs/commerce/commerce-api/guide/authorization.html
- https://mcp.aibase.com/server/1916355561904906241
- https://docs.agentforcemcp.com/connectors/salesforce-commerce-cloud-connector
- https://www.salesforce.com/eu/agentforce/mcp-support/model-context-protocol/?bc=OTH

## Generated record
```json
{
  "app": "Salesforce Commerce Cloud",
  "category": "Commerce",
  "one_liner": "Salesforce Commerce Cloud offers OAuth2 REST APIs; production access is gated via Account Manager.",
  "auth_methods": [
    "OAuth2"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Admin/API access requires creating an API client in Salesforce Account Manager; no evidence of self-serve production credentials."
  },
  "api_type": "REST",
  "api_breadth": "Moderate",
  "existing_mcp": "Community",
  "composio_toolkit": "No",
  "buildability": "Hard",
  "main_blocker": "Requires a Commerce Cloud org and Account Manager API client; no self-serve production access documented.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://developer.salesforce.com/docs/commerce/commerce-api/guide/authorization.html",
    "https://mcp.aibase.com/server/1916355561904906241",
    "https://docs.agentforcemcp.com/connectors/salesforce-commerce-cloud-connector",
    "https://www.salesforce.com/eu/agentforce/mcp-support/model-context-protocol/?bc=OTH"
  ],
  "confidence": 0.62,
  "verification_status": "Auto",
  "slug": "salesforce-commerce-cloud",
  "primary_docs_url": "https://developer.salesforce.com/docs/commerce/commerce-api/guide/authorization.html",
  "rate_limit_note": "No rate limit details found on the cited pages.",
  "last_verified": "2026-08-17"
}
```

## Risk seed (withheld from synthesis)
This prior was retained only for audit sampling and was not shown to the model.
```json
{
  "access_model": "Gated",
  "recommended_next_action": "Needs Outreach",
  "main_blocker": "Enterprise commerce platform sold via sales; no self-serve signup (distinct from core Salesforce CRM's free dev org)."
}
```

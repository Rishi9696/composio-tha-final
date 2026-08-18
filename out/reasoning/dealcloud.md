# DealCloud - synthesis reasoning
_generated 2026-08-17 | model openai:gpt-5_

## Research trace
- queries: ["DealCloud official API authentication developer documentation", "DealCloud API production access approval credentials official documentation", "DealCloud official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://api.docs.dealcloud.com | HTTP 200 | hint | topics=api,auth,mcp
- https://api.docs.dealcloud.com/docs/apikeys | HTTP 200 | derived_guess | topics=api,auth,access,mcp
- https://api.docs.dealcloud.com/docs | HTTP 200 | search_result | topics=api,auth,mcp
- https://www.xpay.sh/saas-pricing/dealcloud/ | HTTP 200 | search_result | topics=api,access,mcp
- https://api.docs.dealcloud.com/ | HTTP 200 | search_result | topics=api,auth,mcp
- https://developer.dealcloud.com | HTTP 0 | derived_guess | topics=none

## Model reasoning
1) Evidence on surface and auth: The official docs list "API Keys" and "Obtaining an API Key" alongside "Authorization Token" and a full "API Reference" with many resources (e.g., Data, Users, Files, Reports), indicating a broad REST API (api.docs.dealcloud.com/docs, /docs/apikeys). The MCP section states "DealCloud MCP Server — client preview starting July 2026" (api.docs.dealcloud.com/mcp, /mcp/getting-started). No explicit OAuth2 flow is shown in the fetched text; the only explicit credential mechanism named is API Keys. 2) Production Access Rubric: The pricing intelligence page states "Intapp DealCloud has sales-led pricing — no public tiers; every CTA goes to a sales contact form" and "Dealcloud does not advertise a free tier" (xpay.sh/saas-pricing/dealcloud/). The docs do not state that a new developer can obtain production credentials self-serve. MCP is explicitly in "client preview", implying limited access. Therefore, production access should be classified as Gated. 3) Conclusions: auth_methods=API Key (only method explicitly evidenced); api_type=REST (dominant public API); existing_mcp=Official (vendor-published MCP, but in client preview); access_model=Gated (sales-led, no public tiers, no self-serve proof); buildability=Hard (manual approval/customer status likely required despite clear docs); recommended_next_action=Needs Outreach (contact DealCloud sales/support for API/MCP production access).

## Key decisions
- buildability: **Hard**
- access_model: **Gated** - Docs describe API Keys, but no proof of self-serve production issuance. Pricing is sales-led with no public tiers; every CTA to contact sales. The MCP server is in client preview starting July 2026.
- recommended_next_action: **Needs Outreach**
- confidence: **0.62**

## Evidence URLs
- https://api.docs.dealcloud.com/docs/apikeys
- https://api.docs.dealcloud.com/docs
- https://api.docs.dealcloud.com/mcp
- https://api.docs.dealcloud.com/mcp/getting-started
- https://www.xpay.sh/saas-pricing/dealcloud/

## Generated record
```json
{
  "app": "DealCloud",
  "category": "CRM",
  "one_liner": "DealCloud exposes a broad REST API and an official MCP (preview), but production access is sales-gated.",
  "auth_methods": [
    "API Key"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Docs describe API Keys, but no proof of self-serve production issuance. Pricing is sales-led with no public tiers; every CTA to contact sales. The MCP server is in client preview starting July 2026."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "No",
  "buildability": "Hard",
  "main_blocker": "Production credentials appear to require sales approval/customer status; MCP is limited to a client preview.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://api.docs.dealcloud.com/docs/apikeys",
    "https://api.docs.dealcloud.com/docs",
    "https://api.docs.dealcloud.com/mcp",
    "https://api.docs.dealcloud.com/mcp/getting-started",
    "https://www.xpay.sh/saas-pricing/dealcloud/"
  ],
  "confidence": 0.62,
  "verification_status": "Auto",
  "slug": "dealcloud",
  "primary_docs_url": "https://api.docs.dealcloud.com/docs/apikeys",
  "rate_limit_note": "Docs include a Rate Limits section; specific limits not shown in the fetched text.",
  "last_verified": "2026-08-17"
}
```

## Risk seed (withheld from synthesis)
This prior was retained only for audit sampling and was not shown to the model.
```json
{
  "access_model": "Gated",
  "api_type": "REST",
  "api_breadth": "Broad",
  "recommended_next_action": "Partner-Gated",
  "main_blocker": "Broad, well-documented REST/OAuth2 API, but keys are only issuable by an admin on an existing paid DealCloud site; no public trial/signup."
}
```

<!-- final-state:start -->
## Final pipeline state
_Updated 2026-08-18 by current human handcheck correction; this supersedes earlier key decisions._

```json
{
  "app": "DealCloud",
  "category": "CRM",
  "one_liner": "DealCloud exposes a broad REST API and an official MCP (preview), but production access is sales-gated.",
  "auth_methods": [
    "OAuth2",
    "API Key"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Docs describe API Keys, but no proof of self-serve production issuance. Pricing is sales-led with no public tiers; every CTA to contact sales. The MCP server is in client preview starting July 2026."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "No",
  "buildability": "Hard",
  "main_blocker": "Production credentials appear to require sales approval/customer status; MCP is limited to a client preview.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://api.docs.dealcloud.com/docs/token",
    "https://api.docs.dealcloud.com/docs/apikeys",
    "https://api.docs.dealcloud.com/releases"
  ],
  "confidence": 0.62,
  "verification_status": "Hand-Checked",
  "slug": "dealcloud",
  "primary_docs_url": "https://api.docs.dealcloud.com/docs/token",
  "rate_limit_note": "Docs include a Rate Limits section; specific limits not shown in the fetched text.",
  "last_verified": "2026-08-17"
}
```
<!-- final-state:end -->

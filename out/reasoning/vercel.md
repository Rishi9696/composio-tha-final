# Vercel - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Vercel official API authentication developer documentation", "Vercel API production access approval credentials official documentation", "Vercel official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://vercel.com/docs/rest-api | HTTP 200 | search_result | topics=api,auth,access
- https://www.sasanova.com/pricing/vercel | HTTP 200 | search_result | topics=access
- https://vercel.com/docs/integrations/create-integration/marketplace-api/reference/vercel | HTTP 200 | search_result | topics=api,auth,access
- https://developer.vercel.com | HTTP 404 | derived_guess | topics=none
- https://developers.vercel.com | HTTP 404 | derived_guess | topics=none
- https://docs.vercel.com | HTTP 200 | derived_guess | topics=api,auth,access,mcp

## Model reasoning
1) Evidence about surfaces and auth: The Vercel REST API page lists many REST endpoints but the fetched excerpt does not state the auth mechanism. The Marketplace API reference lists endpoints, but the provided excerpt is insufficient to rely on a specific credential scheme. The MCP docs show an official “Use Vercel’s MCP server” page and a deployment guide that says MCP servers can be deployed with OAuth authentication. No rate limit details are shown in the cited docs. 2) Production Access Rubric: There is no statement in the fetched REST or Marketplace API docs confirming that a new developer can obtain production credentials self-serve. The MCP docs do not claim self-serve production access either. The pricing source indicates “Hobby Free … non-commercial,” implying that commercial/production use generally requires a paid plan. Therefore, per the rubric and without explicit proof of self-serve production entitlement, classify as Gated. 3) Conclusions: The only clearly evidenced auth method is OAuth2 (from MCP deployment guidance). The dominant public surface is REST, with an official MCP also available. Access model is Gated due to lack of explicit self-serve production statements and the non-commercial free tier note. Buildability is Moderate: docs and endpoints exist, but production access clarity for REST is thin and likely requires plan alignment. Recommended next action is to reach out to confirm the production access path and credential issuance for REST and integrations.

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - Docs show OAuth for MCP deployments; no explicit statement that production API access is self-serve. Pricing indicates the free Hobby plan is non-commercial, implying paid plans for production.
- recommended_next_action: **Needs Outreach**
- confidence: **0.5**

## Evidence URLs
- https://vercel.com/docs/rest-api
- https://vercel.com/docs/integrations/create-integration/marketplace-api/reference/vercel
- https://vercel.com/docs/mcp/deploy-mcp-servers-to-vercel
- https://vercel.com/docs/agent-resources/vercel-mcp
- https://www.sasanova.com/pricing/vercel

## Generated record
```json
{
  "app": "Vercel",
  "category": "DevInfra",
  "one_liner": "Vercel offers REST and official MCP; OAuth is documented, but production access appears gated.",
  "auth_methods": [
    "OAuth2"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Docs show OAuth for MCP deployments; no explicit statement that production API access is self-serve. Pricing indicates the free Hobby plan is non-commercial, implying paid plans for production."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "No explicit self-serve production access or clear REST auth details; likely need a paid plan for commercial use.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://vercel.com/docs/rest-api",
    "https://vercel.com/docs/integrations/create-integration/marketplace-api/reference/vercel",
    "https://vercel.com/docs/mcp/deploy-mcp-servers-to-vercel",
    "https://vercel.com/docs/agent-resources/vercel-mcp",
    "https://www.sasanova.com/pricing/vercel"
  ],
  "confidence": 0.5,
  "verification_status": "Auto",
  "slug": "vercel",
  "primary_docs_url": "https://vercel.com/docs/rest-api",
  "rate_limit_note": "No public rate-limit details found in the cited docs.",
  "last_verified": "2026-08-18"
}
```

<!-- final-state:start -->
## Final pipeline state
_Updated 2026-08-18 by current handcheck fold; this supersedes earlier key decisions._

```json
{
  "app": "Vercel",
  "category": "DevInfra",
  "one_liner": "Vercel offers REST and official MCP; OAuth is documented, but production access appears gated.",
  "auth_methods": [
    "OAuth2"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Docs show OAuth for MCP deployments; no explicit statement that production API access is self-serve. Pricing indicates the free Hobby plan is non-commercial, implying paid plans for production."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "No explicit self-serve production access or clear REST auth details; likely need a paid plan for commercial use.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://vercel.com/docs/rest-api",
    "https://vercel.com/docs/integrations/create-integration/marketplace-api/reference/vercel",
    "https://vercel.com/docs/mcp/deploy-mcp-servers-to-vercel",
    "https://vercel.com/docs/agent-resources/vercel-mcp",
    "https://www.sasanova.com/pricing/vercel"
  ],
  "confidence": 0.5,
  "verification_status": "Hand-Checked",
  "slug": "vercel",
  "primary_docs_url": "https://vercel.com/docs/rest-api",
  "rate_limit_note": "No public rate-limit details found in the cited docs.",
  "last_verified": "2026-08-18"
}
```
<!-- final-state:end -->

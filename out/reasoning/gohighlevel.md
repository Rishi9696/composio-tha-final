# GoHighLevel - synthesis reasoning
_generated 2026-08-17 | model openai:gpt-5_

## Research trace
- queries: ["GoHighLevel official API authentication developer documentation", "GoHighLevel API production access approval credentials official documentation", "GoHighLevel official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://highlevel.stoplight.io | HTTP 200 | hint | topics=none
- https://www.gohighlevel.ai/blog/gohighlevel-pricing-plans | HTTP 200 | search_result | topics=api,access
- https://help.gohighlevel.com/support/solutions/articles/48001060529-highlevel-api | HTTP 200 | search_result | topics=api,auth,access
- https://www.gohighlevel.ai/pricing | HTTP 200 | search_result | topics=api,access
- https://developer.stoplight.io | HTTP 200 | derived_guess | topics=none
- https://developers.stoplight.io | HTTP 200 | derived_guess | topics=none

## Model reasoning
1) What the evidence states: The HighLevel support doc confirms a public REST API with endpoints for contacts, messaging, workflows, calendars, payments, webhooks, etc., and notes: “HighLevel API documentation is now available at https://marketplace.gohighlevel.com/docs/” and that “the ability to generate new API keys will be removed… for accounts that have not yet generated or are not currently using a API key,” indicating legacy API keys exist but are being phased out in favor of newer auth. The marketplace docs include an OAuth 2.0 section and an official MCP Server page describing per‑client MCP endpoints (e.g., https://services.leadconnectorhq.com/mcp/{client}/v2), showing an official MCP surface alongside the REST API. The MCP setup guide gives the MCP endpoint (https://services.leadconnectorhq.com/mcp/) and positions it as a standardized HTTP bridge to HighLevel services. Pricing pages state API access is tied to paid plans: “Unlimited $297/month … Full API access” and “Agency Pro $497/month … Advanced API access,” with a time‑limited free trial mentioned. No specific rate‑limit numbers are visible in the fetched text. 2) Production Access Rubric: The pricing page explicitly ties API access to higher‑tier paid plans (“Full API access” on Unlimited; “Advanced API access” on Agency Pro) and mentions only a 14/30‑day trial, which expires. This is evidence of gating rather than free self‑serve production access. There’s no statement that a new developer can obtain production credentials without paying or approval; instead, API access is a paid feature by plan. 3) Conclusions: Auth methods supported include OAuth2 (documented in the API portal) and API Key (still present for some accounts but being removed for new ones). The dominant API surface is REST; there is also an official MCP server. Access model is Gated due to API access being restricted to higher‑tier paid plans despite a trial. API breadth is Broad given the numerous domains listed. Buildability is Moderate: clear docs and standard OAuth, but production requires a paid plan and API key generation is being deprecated for new accounts. Recommended next action is Needs Outreach (subscribe/upgrade to a plan that includes API access and set up OAuth credentials). Confidence is moderate because auth specifics for MCP tokens aren’t fully shown in the excerpts, but gating by plan is explicit on pricing.

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - API access is a paid feature (Unlimited: Full API access; Agency Pro: Advanced API access). Trials expire; new API keys are being removed for accounts not already using one.
- recommended_next_action: **Needs Outreach**
- confidence: **0.72**

## Evidence URLs
- https://help.gohighlevel.com/support/solutions/articles/48001060529-highlevel-api
- https://www.gohighlevel.ai/pricing
- https://marketplace.gohighlevel.com/docs/other/mcp/index.html
- https://help.gohighlevel.com/support/solutions/articles/155000005741

## Generated record
```json
{
  "app": "GoHighLevel",
  "category": "Ads/Marketing",
  "one_liner": "GoHighLevel offers a broad REST API and official MCP, but production access requires higher‑tier paid plans.",
  "auth_methods": [
    "OAuth2",
    "API Key"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "API access is a paid feature (Unlimited: Full API access; Agency Pro: Advanced API access). Trials expire; new API keys are being removed for accounts not already using one."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "No",
  "buildability": "Moderate",
  "main_blocker": "Production API access requires paid higher-tier plans; new API key generation is being deprecated for new accounts.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://help.gohighlevel.com/support/solutions/articles/48001060529-highlevel-api",
    "https://www.gohighlevel.ai/pricing",
    "https://marketplace.gohighlevel.com/docs/other/mcp/index.html",
    "https://help.gohighlevel.com/support/solutions/articles/155000005741"
  ],
  "confidence": 0.72,
  "verification_status": "Auto",
  "slug": "gohighlevel",
  "primary_docs_url": "https://help.gohighlevel.com/support/solutions/articles/48001060529-highlevel-api",
  "rate_limit_note": "Rate limits are referenced in the support doc but specific values were not visible in the fetched excerpts.",
  "last_verified": "2026-08-17"
}
```

## Risk seed (withheld from synthesis)
This prior was retained only for audit sampling and was not shown to the model.
```json
{
  "access_model": "Self-Serve",
  "recommended_next_action": "Build Now",
  "main_blocker": "Sub-account API keys are self-serve; public marketplace app listing needs review (public-vs-private app distinction)."
}
```

<!-- final-state:start -->
## Final pipeline state
_Updated 2026-08-18 by current handcheck fold; this supersedes earlier key decisions._

```json
{
  "app": "GoHighLevel",
  "category": "Ads/Marketing",
  "one_liner": "GoHighLevel offers a broad REST API and official MCP, but production access requires higher‑tier paid plans.",
  "auth_methods": [
    "OAuth2",
    "Bearer Token"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "HighLevel API access is available on paid agency plans after the temporary trial."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "No",
  "buildability": "Moderate",
  "main_blocker": "Production credentials require an existing paid customer account.",
  "recommended_next_action": "Partner-Gated",
  "evidence_urls": [
    "https://marketplace.gohighlevel.com/docs/Authorization/authorization_doc/",
    "https://marketplace.gohighlevel.com/docs/",
    "https://www.gohighlevel.com/pricing",
    "https://marketplace.gohighlevel.com/docs/other/mcp/index.html"
  ],
  "confidence": 0.72,
  "verification_status": "Hand-Checked",
  "slug": "gohighlevel",
  "primary_docs_url": "https://marketplace.gohighlevel.com/docs/Authorization/authorization_doc/",
  "rate_limit_note": "Rate limits are referenced in the support doc but specific values were not visible in the fetched excerpts.",
  "last_verified": "2026-08-17"
}
```
<!-- final-state:end -->

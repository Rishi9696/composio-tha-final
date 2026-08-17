# Consensus - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Consensus official API authentication developer documentation", "Consensus API production access approval credentials official documentation", "Consensus official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://consensus.app | HTTP 200 | hint | topics=none
- https://support.goconsensus.com/how-to-access-your-api-credentials | HTTP 200 | search_result | topics=api,auth
- https://help.consensus.app/en/articles/10087865-subscription-plans | HTTP 200 | search_result | topics=api,access
- https://consensus.app/home/api/ | HTTP 200 | search_result | topics=api,access
- https://developer.consensus.app | HTTP 0 | derived_guess | topics=none
- https://developers.consensus.app | HTTP 0 | derived_guess | topics=none

## Model reasoning
1) Evidence on surfaces and auth: The Consensus MCP docs provide an official server URL (https://mcp.consensus.app/mcp) and show connection steps for Claude and ChatGPT where “OAuth sign-in will open automatically,” indicating OAuth-based authentication and a hosted MCP surface. The API marketing page says “Build with the Consensus API” but prominently shows “Request access,” without exposing self-serve credentials. The Subscription Plans help page states “Consensus is free to use, with optional subscription plans…” and lists a Free tier, but also notes “Coming Soon: Consensus Search API,” implying the REST Search API is not generally available yet or is gated. No explicit rate limit details are shown in these materials. 2) Production Access Rubric application: For REST, the API page’s “Request access” indicates manual gate rather than self-serve; the plans page further says “Coming Soon: Consensus Search API,” reinforcing that production REST access is not self-serve. For MCP, while the docs show immediate OAuth connection (“you’ll be searching in under 2 minutes” and sign-in flow), there is no explicit sentence confirming production entitlements across plans; the rubric requires explicit proof of self-serve production, so absent that, classify overall as Gated. 3) Conclusions: Auth method = OAuth2 (per MCP connection flow). Dominant public surface = MCP-only (official MCP docs and URL; REST is request-only/coming soon). Existing MCP = Official. Access model = Gated overall, noting REST is request-gated and MCP appears connectable but lacks explicit production entitlement language. Buildability = Moderate (clear MCP docs and OAuth flow, but REST gating and unclear plan entitlements). Recommended action = Needs Outreach to request REST API access and/or confirm MCP production entitlements and pricing.

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - REST Search API shows 'Request access' and plans say 'Coming Soon'. MCP server is documented with OAuth sign-in, but no explicit statement confirms self-serve production entitlements; confirm usage rights and plan requirements.
- recommended_next_action: **Needs Outreach**
- confidence: **0.55**

## Evidence URLs
- https://docs.consensus.app/docs/mcp
- https://consensus.app/home/api/
- https://help.consensus.app/en/articles/10087865-subscription-plans
- https://mcp.so/servers/consensus

## Generated record
```json
{
  "app": "Consensus",
  "category": "AI/Meeting-tools",
  "one_liner": "Consensus has an official MCP server; REST API access is request-gated and not clearly self-serve.",
  "auth_methods": [
    "OAuth2"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "REST Search API shows 'Request access' and plans say 'Coming Soon'. MCP server is documented with OAuth sign-in, but no explicit statement confirms self-serve production entitlements; confirm usage rights and plan requirements."
  },
  "api_type": "MCP-only",
  "api_breadth": "Moderate",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "REST API is request-only/coming soon and MCP production entitlements are not explicitly documented.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://docs.consensus.app/docs/mcp",
    "https://consensus.app/home/api/",
    "https://help.consensus.app/en/articles/10087865-subscription-plans",
    "https://mcp.so/servers/consensus"
  ],
  "confidence": 0.55,
  "verification_status": "Auto",
  "slug": "consensus",
  "primary_docs_url": "https://help.consensus.app/en/articles/10087865-subscription-plans",
  "rate_limit_note": "No public rate limit details found in the cited docs.",
  "last_verified": "2026-08-18"
}
```

## Risk seed (withheld from synthesis)
This prior was retained only for audit sampling and was not shown to the model.
```json
{
  "access_model": "Gated",
  "recommended_next_action": "Needs Outreach",
  "main_blocker": "'OAuth requested' hint suggests a public API is not yet generally available."
}
```

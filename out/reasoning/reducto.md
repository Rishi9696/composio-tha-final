# Reducto - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Reducto official API authentication developer documentation", "Reducto API production access approval credentials official documentation", "Reducto official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://reducto.ai | HTTP 200 | hint | topics=api,auth,access,mcp
- https://docs.reducto.ai/agent-guide | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://reducto.ai/pricing | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://docs.reducto.ai/quickstart | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://developer.reducto.ai | HTTP 0 | derived_guess | topics=none
- https://developers.reducto.ai | HTTP 0 | derived_guess | topics=none

## Model reasoning
1) Evidence: Quickstart explicitly says “Set REDUCTO_API_KEY” and shows CLI/SDK/cURL usage, indicating an HTTP API using an API key (docs.reducto.ai/quickstart). The Agent Guide is a structured API reference for coding agents (docs.reducto.ai/agent-guide). The Reducto MCP Server page offers “Option A: Hosted server (no install)”, indicating an official hosted MCP surface (docs.reducto.ai/mcp-server). Pricing shows “Free Up to your first 15K credits Get started” and lists core APIs (Parse, Extract, Edit, Split) with “No Page Limits Then, $0.015 per credit after first 15K” (reducto.ai/pricing).
2) Production Access Rubric: While pricing lists a free tier and core APIs, there is no explicit sentence confirming that a new developer can obtain production credentials without approval; the pages do not state “no approval required” or explicitly label the free tier as production. The MCP page mentions a hosted option but does not explicitly state self-serve connection without approval. Therefore, there is no definitive evidence proving self-serve production access; per the rubric, in absence of explicit proof, classify as Gated.
3) Decisions: Auth method evidenced is API Key. API type is REST (via cURL/SDK examples). Existing MCP is Official (vendor-hosted MCP server doc). Access model is Gated due to lack of explicit self-serve production entitlement language. Buildability is Moderate: clear docs and SDKs, but production access terms are unclear. Recommended action is Needs Outreach to confirm production access on the Standard/free plan and any approval steps. Rate limits are mentioned at a plan level (premium/priority limits), but exact thresholds are not shown in the fetched text.

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - Docs show API Key usage and a hosted MCP server, and pricing lists a free tier, but no explicit statement confirms self-serve production credentials without approval.
- recommended_next_action: **Needs Outreach**
- confidence: **0.61**

## Evidence URLs
- https://docs.reducto.ai/quickstart
- https://docs.reducto.ai/agent-guide
- https://docs.reducto.ai/mcp-server
- https://reducto.ai/pricing

## Generated record
```json
{
  "app": "Reducto",
  "category": "AI/Meeting-tools",
  "one_liner": "Reducto has a key-based REST API and official MCP server, but production access terms need confirmation.",
  "auth_methods": [
    "API Key"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Docs show API Key usage and a hosted MCP server, and pricing lists a free tier, but no explicit statement confirms self-serve production credentials without approval."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "No",
  "buildability": "Moderate",
  "main_blocker": "No explicit confirmation of self-serve production access; approval or paid plan requirements are unclear.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://docs.reducto.ai/quickstart",
    "https://docs.reducto.ai/agent-guide",
    "https://docs.reducto.ai/mcp-server",
    "https://reducto.ai/pricing"
  ],
  "confidence": 0.61,
  "verification_status": "Auto",
  "slug": "reducto",
  "primary_docs_url": "https://docs.reducto.ai/quickstart",
  "rate_limit_note": "Plans reference rate limits and premium/priority limits; exact default thresholds not specified in the fetched pages.",
  "last_verified": "2026-08-18"
}
```

# Clay - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Clay official API authentication developer documentation", "Clay API production access approval credentials official documentation", "Clay official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://clay.com | HTTP 200 | hint | topics=api,access,mcp
- https://community.clay.com/x/support/5cwjpgptccda/authenticating-an-api-key-in-clay-steps-beyond-cur | HTTP 200 | derived_guess | topics=api,auth
- https://university.clay.com/docs/clay-api-cli | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://www.clay.com/pricing | HTTP 200 | search_result | topics=api,access,mcp
- https://api.clay.cl/ | HTTP 200 | search_result | topics=api
- https://developer.clay.com | HTTP 0 | derived_guess | topics=none

## Model reasoning
1) Evidence about surfaces and auth: The Clay API & CLI doc states there is a Public API and CLI, and shows OAuth 2.0 device authorization for CLI login (“clay login --device … uses the standard OAuth 2.0 device authorization flow”). The MCP docs state Clay exposes an MCP server and detail OAuth-based Dynamic Client Registration: “Dynamic Client Registration (DCR) is the self-service path … your platform registers itself at connect time to obtain OAuth client credentials, with no manual setup on Clay’s side,” and describe discovery via an unauthenticated POST to https://api.clay.com/v3/mcp leading to protected-resource metadata (OAuth2). The MCP settings doc emphasizes workspace-admin controls and plan-based features: “Credit controls and usage monitoring are available on all modern paid plans (Launch, Growth, Enterprise)… The Enable for MCP option on Functions is available on modern Launch, Growth, Enterprise, and Legacy Enterprise plans.” The MCP guide also indicates broad capability (“exposes 150+ data providers, AI research agents, and your team’s prebuilt workflows”). No fetched doc provides concrete REST auth mechanics beyond noting a Public API exists; specific API key/token details for REST aren’t present in the cited text. 2) Production Access Rubric: There is explicit evidence of self-serve credential issuance for MCP via DCR (“self-service path … no manual setup on Clay’s side”). However, plan gating is indicated for using MCP features in a workspace (“available on … paid plans” and “Enable for MCP … on [paid] plans”). There is no explicit statement that a new, unpaid developer can use MCP or API in production. Therefore, per the rubric, without explicit free production entitlement, classify production access as Gated. 3) Decisions: Auth methods center on OAuth2 (for MCP and CLI). The dominant, well-documented public integration surface in evidence is the official MCP server; REST exists but lacks sufficient auth details in the fetched docs, so select MCP-only and note breadth from the MCP guide. Access model is Gated due to plan requirements. Buildability is Moderate: clear OAuth2/DCR docs, but production requires paid workspace/admin enablement. Next action is to reach out/secure the appropriate plan or workspace enablement.

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - MCP client registration is self-serve via OAuth2 DCR, but workspace MCP features (credits, Functions enabled for MCP) are tied to paid plans; no evidence that free users get production MCP/API access.
- recommended_next_action: **Needs Outreach**
- confidence: **0.64**

## Evidence URLs
- https://university.clay.com/docs/connect-to-clay-mcp?utm_source=openai
- https://university.clay.com/docs/mcp-settings?utm_source=openai
- https://university.clay.com/docs/clay-api-cli
- https://www.clay.com/guides/clay-mcp?utm_source=openai

## Generated record
```json
{
  "app": "Clay",
  "category": "Research/Scraping",
  "one_liner": "Clay offers an OAuth2-based MCP with self-serve DCR, but production use appears tied to paid plans.",
  "auth_methods": [
    "OAuth2"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "MCP client registration is self-serve via OAuth2 DCR, but workspace MCP features (credits, Functions enabled for MCP) are tied to paid plans; no evidence that free users get production MCP/API access."
  },
  "api_type": "MCP-only",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "No",
  "buildability": "Moderate",
  "main_blocker": "Production use appears to require a paid Clay workspace and admin-enabled MCP features; no proof of free production access.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://university.clay.com/docs/connect-to-clay-mcp?utm_source=openai",
    "https://university.clay.com/docs/mcp-settings?utm_source=openai",
    "https://university.clay.com/docs/clay-api-cli",
    "https://www.clay.com/guides/clay-mcp?utm_source=openai"
  ],
  "confidence": 0.64,
  "verification_status": "Auto",
  "slug": "clay",
  "primary_docs_url": "https://university.clay.com/docs/clay-api-cli",
  "rate_limit_note": "Not stated in the cited docs.",
  "last_verified": "2026-08-18"
}
```

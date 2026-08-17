# Otter AI - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Otter AI official API authentication developer documentation", "Otter AI API production access approval credentials official documentation", "Otter AI official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://help.otter.ai | HTTP 200 | hint | topics=access
- https://developer-guides-staging.tryotter.com/docs/guides-authentication/ | HTTP 200 | search_result | topics=api,auth,access
- https://artificial-intelligence-wiki.com/ai-tools/ai-productivity-tools/otter-ai-pricing-plans/ | HTTP 200 | search_result | topics=access
- https://apis.io/apis/otter-ai/otter-ai-api/ | HTTP 200 | search_result | topics=api,auth,mcp
- https://developer.otter.ai | HTTP 0 | derived_guess | topics=none
- https://developers.otter.ai | HTTP 0 | derived_guess | topics=none
- https://help.otter.ai/hc/en-us/articles/36130822688279-Otter-ai-Public-API | HTTP 200 | browser_verified_summary | topics=api,auth,mcp

## Model reasoning
1) What the evidence states:
- Otter.ai Public API page: “available to Enterprise workspaces after account-manager enablement.” Requests “use a user-created API key in the Authorization Bearer header” and rate limit is “10 requests per second.” It also notes “Otter’s official MCP server separately uses OAuth authentication.”
- Otter MCP Server help page: MCP connection exists and “All access is OAuth-authenticated with granular permissions.”
- Help Center root provides enterprise-focused sections but does not contradict the above; no self-serve statement is present.

2) Production Access Rubric application:
- Gated REST: Explicitly stated — “available to Enterprise workspaces after account-manager enablement,” requiring Enterprise status and manual enablement.
- MCP: OAuth-based authentication is documented but there is no evidence of self-serve production access; per rubric, treat as gated absent explicit self-serve proof.

3) Conclusions:
- Auth methods: API Key (for REST Public API) and OAuth2 (for MCP server).
- API type: REST is the dominant public surface; MCP exists in parallel but doesn’t change primary classification.
- Existing MCP: Official (vendor-hosted per Help Center article).
- Access model: Gated due to Enterprise-only + account-manager enablement; MCP lacks self-serve proof.
- Buildability: Hard because access requires Enterprise account and manual approval despite available docs.
- Next action: Needs Outreach to Otter account manager/sales for enablement.

## Key decisions
- buildability: **Hard**
- access_model: **Gated** - REST API requires Enterprise workspace with account-manager enablement; MCP uses OAuth but no self-serve production access is documented.
- recommended_next_action: **Needs Outreach**
- confidence: **0.7**

## Evidence URLs
- https://help.otter.ai/hc/en-us/articles/36130822688279-Otter-ai-Public-API
- https://help.otter.ai/hc/en-us/articles/35287607569687-Otter-MCP-Server
- https://help.otter.ai

## Generated record
```json
{
  "app": "Otter AI",
  "category": "AI/Meeting-tools",
  "one_liner": "Enterprise-gated REST API with API key and an OAuth-based official MCP server for meeting data.",
  "auth_methods": [
    "API Key",
    "OAuth2"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "REST API requires Enterprise workspace with account-manager enablement; MCP uses OAuth but no self-serve production access is documented."
  },
  "api_type": "REST",
  "api_breadth": "Moderate",
  "existing_mcp": "Official",
  "composio_toolkit": "No",
  "buildability": "Hard",
  "main_blocker": "Enterprise-only enablement by an account manager; no confirmed self-serve production credentials.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://help.otter.ai/hc/en-us/articles/36130822688279-Otter-ai-Public-API",
    "https://help.otter.ai/hc/en-us/articles/35287607569687-Otter-MCP-Server",
    "https://help.otter.ai"
  ],
  "confidence": 0.7,
  "verification_status": "Auto",
  "slug": "otter-ai",
  "primary_docs_url": "https://developer-guides-staging.tryotter.com/docs/guides-authentication/",
  "rate_limit_note": "Public API rate limit: 10 requests per second.",
  "last_verified": "2026-08-18"
}
```

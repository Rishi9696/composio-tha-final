# Pipedrive - synthesis reasoning
_generated 2026-08-17 | model openai:gpt-5_

## Research trace
- queries: ["Pipedrive official API authentication developer documentation", "Pipedrive API production access approval credentials official documentation", "Pipedrive official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://pipedrive.com | HTTP 200 | hint | topics=access
- https://pipedrive.readme.io/docs/core-api-concepts-authentication | HTTP 200 | search_result | topics=api,auth,access
- https://www.pipedrive.com/en/pricing | HTTP 200 | search_result | topics=api,access,mcp
- https://developers.pipedrive.com/docs/api/v1 | HTTP 200 | search_result | topics=api,auth,access
- https://developer.pipedrive.com | HTTP 200 | derived_guess | topics=api,access
- https://developers.pipedrive.com | HTTP 200 | derived_guess | topics=api,access

## Model reasoning
1) API/MCP/auth evidence: The API Reference states it is a RESTful API with JSON and that “all requests are validated against an API token. The API token can be obtained manually from the Pipedrive app.” It also recommends using a separate account for sandboxing and links to request a Developer Sandbox account. The Authentication docs say “All requests to our API need authentication. If you're creating an app Continue to OAuth 2.0 overview,” and its navigation includes “How to find the API token,” confirming both API token and OAuth 2.0. Pipedrive provides official client libraries (Node.js, PHP). Pricing shows paid plans with a “Free 14-day trial. No credit card required,” but no permanent free tier. The developer docs index includes an “App approval process,” implying review for public apps. MCP: Pipedrive publishes a native MCP with KB pages showing you can connect the Pipedrive MCP server to ChatGPT or Claude and listing MCP tools, indicating an official MCP surface tied to a user’s Pipedrive permissions. 2) Production Access Rubric: Evidence of credential enablement exists (“API token can be obtained manually from the Pipedrive app”). However, there is no proof of self-serve production use without being a paying customer; pricing shows only a “Free 14-day trial,” implying continued use requires payment. The docs also reference an “App approval process,” signaling manual review for public/marketplace apps. There is a sandbox, but that is non-production. Therefore, production access is Gated. 3) Conclusions: Auth methods are API Key (API token) and OAuth2. Dominant API type is REST; breadth is broad across core CRM objects. There is an Official MCP. Buildability is Moderate (clear docs/SDKs and self-serve token issuance, but production is commercially gated and public apps require approval). Recommended next action: Needs Outreach (to secure paid production access and/or navigate app approval).

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - API token is self-generated in-app and OAuth2 is available, but pricing shows only a 14‑day trial and paid plans for ongoing use; docs reference an App approval process for public apps. Sandbox is available for non-production.
- recommended_next_action: **Needs Outreach**
- confidence: **0.66**

## Evidence URLs
- https://developers.pipedrive.com/docs/api/v1
- https://pipedrive.readme.io/docs/core-api-concepts-authentication
- https://www.pipedrive.com/en/pricing
- https://support.pipedrive.com/en/article/mcp?category=pipedrive-ai
- https://support.pipedrive.com/en/article/mcp-chatgpt
- https://support.pipedrive.com/en/article/mcp-claude
- https://support.pipedrive.com/en/article/mcp-tools

## Generated record
```json
{
  "app": "Pipedrive",
  "category": "CRM",
  "one_liner": "Pipedrive offers a REST API with API tokens and OAuth2; production access appears gated by paid plans and app review.",
  "auth_methods": [
    "API Key",
    "OAuth2"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "API token is self-generated in-app and OAuth2 is available, but pricing shows only a 14‑day trial and paid plans for ongoing use; docs reference an App approval process for public apps. Sandbox is available for non-production."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "No confirmed self-serve production access; ongoing use requires a paid account and public apps face approval.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://developers.pipedrive.com/docs/api/v1",
    "https://pipedrive.readme.io/docs/core-api-concepts-authentication",
    "https://www.pipedrive.com/en/pricing",
    "https://support.pipedrive.com/en/article/mcp?category=pipedrive-ai",
    "https://support.pipedrive.com/en/article/mcp-chatgpt",
    "https://support.pipedrive.com/en/article/mcp-claude",
    "https://support.pipedrive.com/en/article/mcp-tools"
  ],
  "confidence": 0.66,
  "verification_status": "Auto",
  "slug": "pipedrive",
  "primary_docs_url": "https://developers.pipedrive.com/docs/api/v1",
  "rate_limit_note": "Rate limiting is documented; specifics not confirmed here.",
  "last_verified": "2026-08-17"
}
```

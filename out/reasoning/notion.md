# Notion - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Notion official API authentication developer documentation", "Notion API production access approval credentials official documentation", "Notion official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://developers.notion.com | HTTP 200 | hint | topics=api,auth,access,mcp
- https://developers.notion.com/guides/get-started/personal-access-tokens | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://apiterms.com/api/notion.so/ | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://developers.notion.com/reference/authentication | HTTP 200 | search_result | topics=api,auth
- https://developer.notion.com | HTTP 0 | derived_guess | topics=none
- https://docs.notion.com | HTTP 0 | derived_guess | topics=none

## Model reasoning
1) Evidence states: Notion offers a REST API; requests authenticate via bearer tokens, provided when you create an internal connection, create a personal access token (PAT), or complete OAuth for a public connection (developers.notion.com/reference/authentication). The connections overview lists three authentication models: internal connections (static API token), public connections (OAuth 2.0), and personal access tokens, and mentions installation scope including “Any workspace (any Notion user can install; Marketplace-eligible)” (developers.notion.com). The PAT guide explains PATs are user-scoped, created in the Developer portal, and can call the Notion REST API (developers.notion.com/guides/get-started/personal-access-tokens). For MCP, Notion provides an official hosted MCP server: “Notion MCP is a remote MCP server hosted by Notion… After you authorize a connection with OAuth, the MCP client can use Notion MCP tools…” and it uses the Notion API (developers.notion.com/guides/mcp/overview). The MCP get-started guide shows OAuth-based authorization to connect clients (developers.notion.com/guides/mcp/get-started-with-mcp). 2) Production Access Rubric: I do not find an explicit vendor statement on developers.notion.com that production API use is free/self-serve across plans. While the connections page implies “Any workspace (any Notion user can install),” it does not explicitly guarantee production entitlement without approval. API Terms (apiterms.com) states “Public API available on Free plan; access included across plans,” but this is third-party aggregation even though it’s in allowed URLs. There is no explicit vendor doc sentence confirming free production credentials or self-serve production MCP access without any gating. Therefore, per the rubric, default to Gated. 3) Conclusions: Auth methods are OAuth2, Personal Access Token, and a static token for internal connections (API Key). Dominant surface is REST; there is also an official hosted MCP. Access model is Gated due to lack of explicit self-serve production entitlement in vendor docs. Buildability is Moderate—docs are clear and tokens are obtainable, but production status may require verification/approval depending on use (e.g., Marketplace). Next action: Needs Outreach to confirm production terms or required reviews.

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - Docs show PATs, internal tokens, and OAuth connections, but no explicit vendor statement confirms free self-serve PRODUCTION access; Marketplace/public distribution may require review. Confirm production entitlement and any plan or approval requirements.
- recommended_next_action: **Needs Outreach**
- confidence: **0.64**

## Evidence URLs
- https://developers.notion.com/reference/authentication
- https://developers.notion.com/guides/get-started/personal-access-tokens
- https://developers.notion.com
- https://developers.notion.com/guides/mcp/overview
- https://developers.notion.com/guides/mcp/get-started-with-mcp
- https://www.notion.com/help/notion-mcp
- https://www.notion.com/blog/notions-hosted-mcp-server-an-inside-look
- https://apiterms.com/api/notion.so/

## Generated record
```json
{
  "app": "Notion",
  "category": "Productivity/PM",
  "one_liner": "Notion offers a broad REST API and official hosted MCP, but production terms need confirmation.",
  "auth_methods": [
    "OAuth2",
    "Personal Access Token",
    "API Key"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Docs show PATs, internal tokens, and OAuth connections, but no explicit vendor statement confirms free self-serve PRODUCTION access; Marketplace/public distribution may require review. Confirm production entitlement and any plan or approval requirements."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "No explicit vendor doc confirming self-serve production entitlement; potential review for public apps/Marketplace.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://developers.notion.com/reference/authentication",
    "https://developers.notion.com/guides/get-started/personal-access-tokens",
    "https://developers.notion.com",
    "https://developers.notion.com/guides/mcp/overview",
    "https://developers.notion.com/guides/mcp/get-started-with-mcp",
    "https://www.notion.com/help/notion-mcp",
    "https://www.notion.com/blog/notions-hosted-mcp-server-an-inside-look",
    "https://apiterms.com/api/notion.so/"
  ],
  "confidence": 0.64,
  "verification_status": "Auto",
  "slug": "notion",
  "primary_docs_url": "https://developers.notion.com/guides/get-started/personal-access-tokens",
  "rate_limit_note": "Per API Terms: ~3 req/s per connection with bursts; shared per-workspace limit scaled by plan; 429 on exceed.",
  "last_verified": "2026-08-18"
}
```

<!-- final-state:start -->
## Final pipeline state
_Updated 2026-08-18 by current handcheck fold; this supersedes earlier key decisions._

```json
{
  "app": "Notion",
  "category": "Productivity/PM",
  "one_liner": "Notion offers a broad REST API and official hosted MCP, but production terms need confirmation.",
  "auth_methods": [
    "OAuth2",
    "Personal Access Token",
    "API Key"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Docs show PATs, internal tokens, and OAuth connections, but no explicit vendor statement confirms free self-serve PRODUCTION access; Marketplace/public distribution may require review. Confirm production entitlement and any plan or approval requirements."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "No explicit vendor doc confirming self-serve production entitlement; potential review for public apps/Marketplace.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://developers.notion.com/reference/authentication",
    "https://developers.notion.com/guides/get-started/personal-access-tokens",
    "https://developers.notion.com",
    "https://developers.notion.com/guides/mcp/overview",
    "https://developers.notion.com/guides/mcp/get-started-with-mcp",
    "https://www.notion.com/help/notion-mcp",
    "https://www.notion.com/blog/notions-hosted-mcp-server-an-inside-look",
    "https://apiterms.com/api/notion.so/"
  ],
  "confidence": 0.64,
  "verification_status": "Hand-Checked",
  "slug": "notion",
  "primary_docs_url": "https://developers.notion.com/guides/get-started/personal-access-tokens",
  "rate_limit_note": "Per API Terms: ~3 req/s per connection with bursts; shared per-workspace limit scaled by plan; 429 on exceed.",
  "last_verified": "2026-08-18"
}
```
<!-- final-state:end -->

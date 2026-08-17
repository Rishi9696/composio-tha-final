# Firecrawl - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Firecrawl official API authentication developer documentation", "Firecrawl API production access approval credentials official documentation", "Firecrawl official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://firecrawl.dev | HTTP 200 | hint | topics=api,auth,access,mcp
- https://docs.firecrawl.dev/api-reference/v2-introduction | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://www.firecrawl.dev/pricing | HTTP 200 | search_result | topics=api,auth,access
- https://docs.firecrawl.dev/api-reference/introduction | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://developer.firecrawl.dev | HTTP 0 | derived_guess | topics=none
- https://developers.firecrawl.dev | HTTP 0 | derived_guess | topics=none

## Model reasoning
1) Evidence states: Firecrawl exposes a hosted REST API at https://api.firecrawl.dev with many endpoints (Search, Scrape, Crawl, Map, Interact, Parse, Monitor, Agent). Authentication: “For authentication, it’s required to include an Authorization header. The header should contain Bearer fc-123456789, where fc-123456789 represents your API Key.” Docs mention standard codes and “429 responses.” The homepage shows SDK usage with api_key. MCP: The Developers & MCP page says “Firecrawl Official MCP server” connecting to Claude Desktop, Cursor, etc., and the /mcp page shows an MCP server configuration (docs-scoped), indicating an official MCP surface exists. No OAuth is described; auth is via API Key. 2) Production Access Rubric: Pricing advertises a “Free Plan… No cost, no card, no hassle,” but there is no explicit statement that these credentials are production-entitled without manual approval beyond signup, nor an explicit self-serve production statement. Per rubric, key generation or free/trial alone is insufficient to prove self-serve production. Therefore, absent explicit confirmation of self-serve production entitlement, classify as Gated. 3) Conclusions: Auth methods = API Key. API type = REST (official MCP also exists). Access model = Gated (lack of explicit self-serve production guarantee). Existing MCP = Official. API breadth = Broad. Buildability = Moderate (clear docs but need to confirm production entitlement/plan). Next action = Needs Outreach to clarify production use and plan requirements.

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - Docs require an API Key in Authorization; pricing shows a Free plan, but there is no explicit statement that production credentials are self-serve without approval. Per rubric, treat production access as gated until confirmed.
- recommended_next_action: **Needs Outreach**
- confidence: **0.65**

## Evidence URLs
- https://docs.firecrawl.dev/api-reference/introduction
- https://docs.firecrawl.dev/api-reference/v2-introduction
- https://www.firecrawl.dev/pricing
- https://docs.firecrawl.dev/use-cases/developers-mcp
- https://docs.firecrawl.dev/mcp
- https://firecrawl.dev

## Generated record
```json
{
  "app": "Firecrawl",
  "category": "Research/Scraping",
  "one_liner": "Broad REST API with API key auth and an official MCP server; confirm production access and plan needs before build.",
  "auth_methods": [
    "API Key"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Docs require an API Key in Authorization; pricing shows a Free plan, but there is no explicit statement that production credentials are self-serve without approval. Per rubric, treat production access as gated until confirmed."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "Unclear production entitlement; may need a paid plan or approval to operate beyond free limits.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://docs.firecrawl.dev/api-reference/introduction",
    "https://docs.firecrawl.dev/api-reference/v2-introduction",
    "https://www.firecrawl.dev/pricing",
    "https://docs.firecrawl.dev/use-cases/developers-mcp",
    "https://docs.firecrawl.dev/mcp",
    "https://firecrawl.dev"
  ],
  "confidence": 0.65,
  "verification_status": "Auto",
  "slug": "firecrawl",
  "primary_docs_url": "https://www.firecrawl.dev/pricing",
  "rate_limit_note": "Docs reference 429 responses; pricing lists concurrency caps (e.g., Free: 2 concurrent requests).",
  "last_verified": "2026-08-18"
}
```

# Bright Data - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Bright Data official API authentication developer documentation", "Bright Data API production access approval credentials official documentation", "Bright Data official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://brightdata.com | HTTP 200 | hint | topics=api,access,mcp
- https://docs.brightdata.com/api-reference/authentication | HTTP 200 | search_result | topics=api,auth,access
- https://apis.io/plans/bright-data/bright-data-plans-pricing/ | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://docs.brightdata.com/scraping-automation/serp-api/pricing-and-billing | HTTP 200 | search_result | topics=api,access
- https://developer.brightdata.com | HTTP 0 | derived_guess | topics=none
- https://developers.brightdata.com | HTTP 0 | derived_guess | topics=none

## Model reasoning
1) API/MCP/auth facts from docs: The Authentication doc states: “Authenticate with Bright Data using 1 of 2 methods: API Access with an API key or Native Access with proxy username and password… We create a default key for you upon account creation automatically.” It shows a REST sample with Authorization: Bearer <token>, i.e., API key used in a Bearer header. No OAuth is mentioned. MCP docs show an official Bright Data MCP server with token-based access (e.g., https://mcp.brightdata.com/mcp?token=<token>) and that “Every new account includes 5,000 free requests per month,” with hosted remote or self‑hosted modes. SERP API pricing explains per‑1,000 successful requests billing and that failed requests aren’t billed. The Bright Data site lists FREE TIER for multiple Web Access APIs and says “Get started for free. No credit card required.” 2) Production Access Rubric: Evidence for self-serve production: “We create a default key for you upon account creation automatically” (credentials on signup) and “Every new account includes 5,000 free requests per month” for the MCP server (self-serve free production usage). The homepage shows “FREE TIER” for Web Access APIs and “Get started for free. No credit card required,” indicating self-serve entry without manual approval. No doc mentions required manual review/partnership. Usage is “charged according to your pricing plan,” but free tiers exist. 3) Therefore: auth_methods = [API Key]; api_type = REST (dominant public surface; MCP also exists); existing_mcp = Official; access_model = Self-Serve (note MCP free tier and free tiers for APIs); buildability = Easy (clear docs, API key auth, official MCP server); recommended_next_action = Build Now.

## Key decisions
- buildability: **Easy**
- access_model: **Self-Serve** - Default API key is created on account signup; official MCP server grants 5,000 free requests/month to every new account. Homepage lists FREE TIER for Web Access APIs with “Get started for free. No credit card required.” Usage billed per selected plan.
- recommended_next_action: **Build Now**
- confidence: **0.77**

## Evidence URLs
- https://docs.brightdata.com/api-reference/authentication
- https://docs.brightdata.com/ai/mcp-server/overview
- https://docs.brightdata.com/ai/mcp-server/faqs
- https://docs.brightdata.com/ai/for-agents/docs-mcp
- https://docs.brightdata.com/scraping-automation/serp-api/pricing-and-billing
- https://brightdata.com

## Generated record
```json
{
  "app": "Bright Data",
  "category": "Research/Scraping",
  "one_liner": "Bright Data offers API key–based scraping APIs and an official MCP server with a self-serve free tier.",
  "auth_methods": [
    "API Key"
  ],
  "access_model": {
    "kind": "Self-Serve",
    "note": "Default API key is created on account signup; official MCP server grants 5,000 free requests/month to every new account. Homepage lists FREE TIER for Web Access APIs with “Get started for free. No credit card required.” Usage billed per selected plan."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Easy",
  "main_blocker": "None significant; choose product/zone and configure the API key.",
  "recommended_next_action": "Build Now",
  "evidence_urls": [
    "https://docs.brightdata.com/api-reference/authentication",
    "https://docs.brightdata.com/ai/mcp-server/overview",
    "https://docs.brightdata.com/ai/mcp-server/faqs",
    "https://docs.brightdata.com/ai/for-agents/docs-mcp",
    "https://docs.brightdata.com/scraping-automation/serp-api/pricing-and-billing",
    "https://brightdata.com"
  ],
  "confidence": 0.77,
  "verification_status": "Auto",
  "slug": "bright-data",
  "primary_docs_url": "https://docs.brightdata.com/api-reference/authentication",
  "rate_limit_note": "MCP server: 5,000 free requests/month for new accounts. SERP API bills per 1,000 successful requests; failed requests not billed.",
  "last_verified": "2026-08-18"
}
```

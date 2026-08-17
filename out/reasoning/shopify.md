# Shopify - synthesis reasoning
_generated 2026-08-17 | model openai:gpt-5_

## Research trace
- queries: ["Shopify official API authentication developer documentation", "Shopify API production access approval credentials official documentation", "Shopify official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://shopify.dev | HTTP 200 | hint | topics=api,access
- https://shopify.dev/docs/api/usage/authentication | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://apispine.com/shopify-api/pricing | HTTP 200 | search_result | topics=api,access
- https://www.youtube.com/watch?v=9a7A2pTtTDc | HTTP 200 | search_result | topics=none
- https://developer.shopify.dev | HTTP 0 | derived_guess | topics=none
- https://developers.shopify.dev | HTTP 0 | derived_guess | topics=none

## Model reasoning
1) What the evidence states:
- API surface and auth: Shopify’s auth guide indicates Admin API access for apps uses Shopify-managed installation, session tokens, and token exchange; the Storefront API supports tokenless and token-based access with public and private access tokens and up to 100 active tokens per shop (shopify.dev/docs/api/usage/authentication).
- MCP: Shopify documents Storefront MCP, describing MCP servers that expose commerce data to AI assistants (shopify.dev/docs/apps/build/storefront-mcp and /index). The MCP.so listing shows a hosted remote MCP server at https://setup.shopify.com/mcp that uses OAuth for authentication and a Streamable HTTP transport (mcp.so/servers/shopify).
- Production/pricing: apispine states API access is tied to a merchant’s Shopify subscription plan and included with a Shopify store subscription, with only a short free trial (“Free Tier 3-day free trial”) and starting at $39/month (apispine.com/shopify-api/pricing).
2) Production Access Rubric:
- Gated evidence: “Shopify API access is primarily tied to a merchant’s Shopify subscription plan… included with a Shopify store subscription,” and only a brief trial exists. Per the rubric, if free access expires and continued API use needs a paid plan, classify Gated. No evidence shows self-serve free production credentials.
- No doc indicates production self-serve for MCP independent of having a paid store; MCP.so mentions OAuth sign-in but not production entitlements.
3) Decisions:
- Auth methods: OAuth2 (for Admin apps and the remote MCP server). While Storefront API mentions access tokens, the evidence doesn’t label them under a scheme from the controlled vocabulary; to avoid over-inference, list only OAuth2.
- API type: GraphQL is the dominant public surface (Admin GraphQL and Storefront GraphQL), with REST also present; MCP exists in parallel.
- existing_mcp: Official, based on Shopify’s own MCP docs and the vendor-hosted remote MCP server listing.
- access_model: Gated due to requirement for a paid Shopify store plan for production use.
- buildability: Moderate (clear docs and OAuth/app setup; production requires access to a paid merchant store).
- recommended_next_action: Needs Outreach (secure a merchant store subscription or coordinate with a merchant for production access).

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - API access is bundled with a merchant’s paid Shopify store plan; a short free trial exists but continued production use requires a subscription.
- recommended_next_action: **Needs Outreach**
- confidence: **0.64**

## Evidence URLs
- https://shopify.dev/docs/api/usage/authentication
- https://shopify.dev/docs/apps/build/storefront-mcp
- https://shopify.dev/docs/apps/build/storefront-mcp/index
- https://mcp.so/servers/shopify
- https://apispine.com/shopify-api/pricing

## Generated record
```json
{
  "app": "Shopify",
  "category": "Commerce",
  "one_liner": "Shopify provides OAuth2 APIs and an official MCP server, but production access requires a paid store plan.",
  "auth_methods": [
    "OAuth2"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "API access is bundled with a merchant’s paid Shopify store plan; a short free trial exists but continued production use requires a subscription."
  },
  "api_type": "GraphQL",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "Production credentials require a paid Shopify store plan; no evidence of free, self-serve production entitlement.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://shopify.dev/docs/api/usage/authentication",
    "https://shopify.dev/docs/apps/build/storefront-mcp",
    "https://shopify.dev/docs/apps/build/storefront-mcp/index",
    "https://mcp.so/servers/shopify",
    "https://apispine.com/shopify-api/pricing"
  ],
  "confidence": 0.64,
  "verification_status": "Auto",
  "slug": "shopify",
  "primary_docs_url": "https://shopify.dev/docs/api/usage/authentication",
  "rate_limit_note": "No rate-limit specifics were present in the cited evidence.",
  "last_verified": "2026-08-17"
}
```

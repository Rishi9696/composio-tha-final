# WooCommerce - synthesis reasoning
_generated 2026-08-17 | model openai:gpt-5_

## Research trace
- queries: ["WooCommerce official API authentication developer documentation", "WooCommerce API production access approval credentials official documentation", "WooCommerce official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://woocommerce.com/document/woocommerce-rest-api | HTTP 200 | hint | topics=api,auth,access
- https://woocommerce.github.io/woocommerce-rest-api-docs/ | HTTP 200 | search_result | topics=api,auth
- https://woocommerce.com/pricing/ | HTTP 200 | search_result | topics=access
- https://developer.woocommerce.com/docs/apis/ | HTTP 200 | search_result | topics=api,auth,access
- https://developer.woocommerce.com | HTTP 200 | derived_guess | topics=api,access,mcp
- https://developers.woocommerce.com | HTTP 0 | derived_guess | topics=none

## Model reasoning
1) What the evidence states: The WooCommerce REST API “connects your store to external systems,” and “most integrations require you to generate API keys in WooCommerce… The WooCommerce REST API uses a key system to control access,” issuing a Consumer Key and Consumer Secret per WordPress user with configurable permissions (woocommerce.com/document/woocommerce-rest-api). The technical REST docs include “Authentication” with “REST API keys” and expose extensive endpoints for orders, products, customers, coupons, reports, etc. (woocommerce.github.io/woocommerce-rest-api-docs/). The APIs overview notes the WC REST API (read/write store data), Store API (public, unauthenticated), and an experimental Dual API that can generate a GraphQL endpoint (developer.woocommerce.com/docs/apis/). MCP: “WooCommerce includes native support for the Model Context Protocol (MCP)… with proper authentication and permissions,” but it is “currently in developer preview” (developer.woocommerce.com/docs/features/mcp/?utm_source=openai). The W7S Marketplace extension page says WooCommerce ships a built-in MCP feature but it’s narrow and requires setup; the extension offers “one-click connection” and broader operations, and “You stay in control of access through your WooCommerce API keys,” and is a paid product (woocommerce.com/products/w7s-mcp/?utm_source=openai). Pricing states “WooCommerce is the free, open-source ecommerce platform… Core platform: WooCommerce Free” (woocommerce.com/pricing/).
2) Production Access Rubric: There is clear credential-generation guidance, but no statement that a new third-party developer can obtain production credentials without store-owner involvement. Instead, production keys are generated within each merchant’s WooCommerce store (“Most integrations require you to generate API keys in WooCommerce”), implying access depends on store-owner approval. MCP production is further constrained: core MCP is a “developer preview” and the broader/turnkey MCP path is via a paid extension. No evidence explicitly promises free, vendor-issued production credentials to new developers without approval. Therefore, by the rubric, production access is Gated.
3) Conclusions aligned to the above: Auth method is API Key (Consumer Key/Secret). Dominant public surface is REST (WC REST API); Store API is public/unauthenticated; Dual API’s GraphQL is experimental. MCP exists officially but is in developer preview; a paid extension expands it. Access model is Gated because production access requires per-store key issuance by the merchant and MCP’s practical path may involve a paid extension. Buildability is Moderate: docs are clear, but access relies on each merchant enabling permalinks and generating keys, and MCP is preview/paid-extension for broader coverage.

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - Production access requires each merchant to generate API keys in their WooCommerce store; core MCP is in developer preview and broader MCP connectivity is offered via a paid extension.
- recommended_next_action: **Needs Outreach**
- confidence: **0.64**

## Evidence URLs
- https://woocommerce.com/document/woocommerce-rest-api
- https://woocommerce.github.io/woocommerce-rest-api-docs/
- https://developer.woocommerce.com/docs/apis/
- https://developer.woocommerce.com/docs/features/mcp/?utm_source=openai
- https://woocommerce.com/products/w7s-mcp/?utm_source=openai
- https://woocommerce.com/pricing/

## Generated record
```json
{
  "app": "WooCommerce",
  "category": "Commerce",
  "one_liner": "WooCommerce offers a broad REST API with per-store API keys and official, preview-stage MCP support.",
  "auth_methods": [
    "API Key"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Production access requires each merchant to generate API keys in their WooCommerce store; core MCP is in developer preview and broader MCP connectivity is offered via a paid extension."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "No",
  "buildability": "Moderate",
  "main_blocker": "Per-store approval and key generation; MCP beyond basics is preview or requires a paid extension.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://woocommerce.com/document/woocommerce-rest-api",
    "https://woocommerce.github.io/woocommerce-rest-api-docs/",
    "https://developer.woocommerce.com/docs/apis/",
    "https://developer.woocommerce.com/docs/features/mcp/?utm_source=openai",
    "https://woocommerce.com/products/w7s-mcp/?utm_source=openai",
    "https://woocommerce.com/pricing/"
  ],
  "confidence": 0.64,
  "verification_status": "Auto",
  "slug": "woocommerce",
  "primary_docs_url": "https://developer.woocommerce.com/docs/apis/",
  "rate_limit_note": "No global vendor rate limits documented; performance and limits depend on each store’s hosting.",
  "last_verified": "2026-08-17"
}
```

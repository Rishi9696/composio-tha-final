# Binance - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Binance official API authentication developer documentation", "Binance API production access approval credentials official documentation", "Binance official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://binance-docs.github.io | HTTP 404 | hint | topics=none
- https://developers.binance.com/en/docs/products/spot/rest-api#authentication-and-security | HTTP 202 | search_result | topics=none
- https://www.binance.com/en/fee/schedule | HTTP 202 | search_result | topics=none
- https://developers.binance.com/en/docs/products/spot/rest-api | HTTP 202 | search_result | topics=none
- https://developer.github.io | HTTP 404 | derived_guess | topics=none
- https://developers.github.io | HTTP 404 | derived_guess | topics=none

## Model reasoning
1) What the evidence says: The mcp.so page explicitly describes an “Unofficial tools and server implementation for Binance’s Model Context Protocol (MCP)” that bridges AI assistants to a Binance exchange account. It instructs users to “Set BINANCE_API_KEY and BINANCE_API_SECRET environment variables (optionally BINANCE_TESTNET=true for testnet).” It lists capabilities such as real-time market data, account management, trading operations, and portfolio tracking. It also notes “No standard config provided” and shows no tool definitions, rate limits, or official production-access terms. The other allowed links provide no Binance-specific API/auth/access details. 2) Production Access Rubric: There is no statement proving that a new developer can obtain production credentials self-serve. The only concrete instruction is to use your own Binance API key/secret; no page confirms production entitlement without approval or paid account. Per the rubric, absent explicit proof of self-serve production access, classify as Gated. 3) Conclusions: Auth method = API Key (per env vars). Existing MCP = Community (explicitly labeled ‘Unofficial’). Given we only have MCP evidence (not official REST docs in allowed sources), set api_type to MCP-only. Access model = Gated due to lack of explicit self-serve production entitlement. Buildability = Moderate (install is straightforward but unofficial server with thin docs). Recommended next action = Needs Outreach (confirm production API key eligibility/terms with Binance or rely on user-provided keys and compliance). Evidence is thin; confidence moderate.

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - No evidence of self-serve production credentials; the only path shown is using an existing Binance API key/secret via an unofficial community MCP server. Production use depends on a user’s Binance account and its API permissions.
- recommended_next_action: **Needs Outreach**
- confidence: **0.48**

## Evidence URLs
- https://mcp.so/servers/BinanceMCPServer?utm_source=openai

## Generated record
```json
{
  "app": "Binance",
  "category": "Fintech",
  "one_liner": "Community MCP server bridges AI assistants to Binance via API keys; production access appears gated.",
  "auth_methods": [
    "API Key"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "No evidence of self-serve production credentials; the only path shown is using an existing Binance API key/secret via an unofficial community MCP server. Production use depends on a user’s Binance account and its API permissions."
  },
  "api_type": "MCP-only",
  "api_breadth": "Broad",
  "existing_mcp": "Community",
  "composio_toolkit": "No",
  "buildability": "Moderate",
  "main_blocker": "No official production access documentation in allowed sources; only an unofficial MCP bridge that requires user API keys.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://mcp.so/servers/BinanceMCPServer?utm_source=openai"
  ],
  "confidence": 0.48,
  "verification_status": "Auto",
  "slug": "binance",
  "primary_docs_url": "https://mcp-hub.ink/servers/binance/?utm_source=openai",
  "rate_limit_note": "No rate limit information in the cited sources.",
  "last_verified": "2026-08-18"
}
```

## Risk seed (withheld from synthesis)
This prior was retained only for audit sampling and was not shown to the model.
```json
{
  "access_model": "Self-Serve",
  "recommended_next_action": "Build Now",
  "main_blocker": "",
  "note": "Easy-win example: API key is self-serve via account signup, no OAuth/partner gate."
}
```

# PitchBook - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["PitchBook official API authentication developer documentation", "PitchBook API production access approval credentials official documentation", "PitchBook official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://pitchbook.com | HTTP 200 | hint | topics=api,access
- https://pitchbook.com/data/pitchbook-api | HTTP 404 | search_result | topics=none
- https://pitchbook.com/pricing | HTTP 200 | search_result | topics=api,access
- https://pitchbook.com/help/data-feed-api-crm-direct-data-solutions-q3-2025 | HTTP 403 | search_result | topics=none
- https://developer.pitchbook.com | HTTP 0 | derived_guess | topics=none
- https://pitchbook.com/help/PitchBook-api | HTTP 200 | browser_verified_summary | topics=api,auth,access
- https://pitchbook.com/media/press-releases/pitchbook-announces-new-essential-mcp-integration-with-perplexity-expanding-access-to-ai-powered-verifiable-market-intelligence | HTTP 200 | browser_verified_summary | topics=access,mcp

## Model reasoning
1) What the evidence states:
- REST API: The PitchBook help page explicitly says “PitchBook's REST API is a separate offering requiring a standalone contract. Access starts through Direct Data; credentials are API keys or authentication tokens.” This confirms a hosted REST API, contract-based access, and that API keys/tokens are used for auth. (https://pitchbook.com/help/PitchBook-api)
- MCP: An official remote MCP server exists at https://premium.mcp.pitchbook.com/mcp. The MCP listing states “Does the PitchBook MCP server require authentication? Yes. PitchBook uses OAuth: the first time you connect, your MCP client opens a browser window to sign in and authorize access.” (https://mcp.so/servers/pitchbook). Apigene further labels it “Official MCP Servers … Verified Official Vendor Maintained … Hosted on pitchbook.com,” indicating vendor-hosted official status. (https://apigene.ai/mcp/official/pitchbook). A PitchBook press release announces an Essential MCP integration with Perplexity, corroborating official MCP presence. (https://pitchbook.com/media/press-releases/pitchbook-announces-new-essential-mcp-integration-with-perplexity-expanding-access-to-ai-powered-verifiable-market-intelligence)

2) Production Access Rubric application:
- For REST: The help page states it is “a separate offering requiring a standalone contract. Access starts through Direct Data,” which signifies manual approval/contractual gating rather than self-serve production access.
- For MCP: While setup and OAuth login are described, there is no evidence that a new developer can obtain production access without approval or a paid contract; no self-serve/ free production entitlement is documented. Therefore, absent explicit self-serve proof, treat as Gated per rubric.

3) Decisions flowing from the above:
- Auth methods: API Key (REST per help page); OAuth2 (MCP per mcp.so). 
- API type: REST is the dominant public API; MCP also exists but does not replace REST as the primary surface.
- Existing MCP: Official (vendor-hosted/published server on pitchbook.com and confirmed via press and listings).
- Access model: Gated due to required standalone contract for REST and no self-serve production evidence for MCP.
- Buildability: Hard, since production requires contracting/approval and docs imply commercial onboarding; MCP details exist but access requirements remain gated.
- Next action: Needs Outreach to PitchBook/Direct Data team to obtain contractual access/credentials.

## Key decisions
- buildability: **Hard**
- access_model: **Gated** - REST API requires a standalone contract via Direct Data; the official MCP server uses OAuth but no self-serve production access is documented.
- recommended_next_action: **Needs Outreach**
- confidence: **0.67**

## Evidence URLs
- https://pitchbook.com/help/PitchBook-api
- https://mcp.so/servers/pitchbook
- https://apigene.ai/mcp/official/pitchbook
- https://pitchbook.com/media/press-releases/pitchbook-announces-new-essential-mcp-integration-with-perplexity-expanding-access-to-ai-powered-verifiable-market-intelligence

## Generated record
```json
{
  "app": "PitchBook",
  "category": "Fintech",
  "one_liner": "PitchBook’s REST API and official OAuth-based MCP are production-gated; access requires a contract.",
  "auth_methods": [
    "API Key",
    "OAuth2"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "REST API requires a standalone contract via Direct Data; the official MCP server uses OAuth but no self-serve production access is documented."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "No",
  "buildability": "Hard",
  "main_blocker": "Production credentials require a standalone contract with PitchBook Direct Data; no self-serve entitlement is documented.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://pitchbook.com/help/PitchBook-api",
    "https://mcp.so/servers/pitchbook",
    "https://apigene.ai/mcp/official/pitchbook",
    "https://pitchbook.com/media/press-releases/pitchbook-announces-new-essential-mcp-integration-with-perplexity-expanding-access-to-ai-powered-verifiable-market-intelligence"
  ],
  "confidence": 0.67,
  "verification_status": "Auto",
  "slug": "pitchbook",
  "primary_docs_url": "https://pitchbook.com/help/PitchBook-api",
  "rate_limit_note": "No public rate limit details are provided in the cited documentation.",
  "last_verified": "2026-08-18"
}
```

## Risk seed (withheld from synthesis)
This prior was retained only for audit sampling and was not shown to the model.
```json
{
  "access_model": "Gated",
  "recommended_next_action": "Partner-Gated",
  "main_blocker": "Enterprise research platform; API is contact-sales / partner-only, no public self-serve tier."
}
```

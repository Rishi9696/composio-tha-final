# Coda - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Coda official API authentication developer documentation", "Coda API production access approval credentials official documentation", "Coda official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://coda.io/developers | HTTP 200 | hint | topics=api,auth,mcp
- https://coda.io/developers/apis/v1 | HTTP 200 | search_result | topics=api,auth,mcp
- https://apis.io/finops/coda/coda-finops/ | HTTP 200 | search_result | topics=api,auth,mcp
- https://apiseeds.co/en/apis/coda-api | HTTP 200 | search_result | topics=api,auth
- https://developer.coda.io | HTTP 0 | derived_guess | topics=none
- https://developers.coda.io | HTTP 0 | derived_guess | topics=none

## Model reasoning
1) What the evidence states:
- Official API surface: The coda.io/developers/apis/v1 reference is an official REST API for “Superhuman Docs (formerly Coda)” with extensive endpoints covering docs, pages, tables/rows, permissions, publishing, analytics, automations, etc., and it includes a Rate Limiting section (no specific numbers shown in the excerpt).
- MCP surface: Official help docs describe the Coda MCP, its capabilities, and how to connect. The “Connect to the Coda MCP” article lists Supported clients and explicitly lists Method of authentication per client: OAuth 2 for ChatGPT/Claude/Cursor, and Personal Access Tokens for others. It notes the MCP is in beta and provides hosted-connection style instructions.
- Auth credentials: The MCP connect page explicitly references OAuth 2 and Personal Access Tokens. A community MCP server registry entry for Coda shows it “requires an API key,” with instructions to generate an API token at coda.io/account, indicating a static token mechanism exists for API access. The official API reference page itself (in the provided excerpt) does not show the auth sentence, but the presence of “Using the API” and rate limit sections indicates a conventional REST API surface.
- Access/pricing: The APIs.io FinOps profile (allowed source) asserts “Editors, viewers, and the public API are free across all tiers” and “There is no metered API surcharge,” citing coda.io/pricing and the API docs as sources.

2) Production Access Rubric application:
- Self-serve signals for MCP: The official “Connect to the Coda MCP” help article shows end-user/OAuth2 or Personal Access Token flows with step-by-step connection for multiple clients, with no mention of approvals or reviews (e.g., the table listing “ChatGPT — OAuth 2,” “Claude — OAuth 2,” “CoPilot Studio — Personal Access Tokens”), which evidences self-serve production access to the hosted MCP surface for a user’s workspace.
- Self-serve signals for REST: The community MCP registry page instructs generating an API token at coda.io/account (“Generate API token”), indicating token issuance is self-serve. The APIs.io FinOps profile states the public API is free across all tiers (no additional gating), supporting production entitlement without manual approval. No fetched evidence indicates required vendor approval, partnership, or paid plan solely to use the API.
- Caveats: The REST auth sentence isn’t quoted from the API reference due to excerpt limits; reliance on the community MCP listing and the FinOps profile is noted. MCP is explicitly marked beta in the help docs, which may affect stability but not credential issuance.

3) Decisions derived:
- auth_methods: OAuth2 (for MCP) and Personal Access Token (static token for MCP and REST). 
- api_type: REST is the dominant public integration surface; an official MCP also exists.
- existing_mcp: Official, since Coda’s help center documents the Coda MCP and connection steps.
- access_model: Self-Serve, based on the MCP connection guide’s OAuth2/PAT flows and the FinOps profile’s statement that the public API is free across tiers.
- buildability: Easy — clear REST docs plus self-serve OAuth2/PAT for MCP; only note is MCP being beta.
- recommended_next_action: Build Now.
- rate limits: API docs include a Rate Limiting section; specific numbers not captured here.

## Key decisions
- buildability: **Easy**
- access_model: **Self-Serve** - Official help shows OAuth2/PAT flows to connect MCP without approvals; community docs show self-serve API tokens; FinOps profile states the public API is free across tiers.
- recommended_next_action: **Build Now**
- confidence: **0.72**

## Evidence URLs
- https://coda.io/developers/apis/v1
- https://help.coda.io/hc/en-us/articles/44722661982989-Connect-to-the-Coda-MCP
- https://help.coda.io/hc/en-us/articles/44722756780173-Using-the-Coda-MCP
- https://coda.io/resources/guides/getting_started_with_coda_mcp
- https://mcpmux.com/servers/orellazri.coda-mcp-npx/
- https://apis.io/finops/coda/coda-finops/

## Generated record
```json
{
  "app": "Coda",
  "category": "Productivity/PM",
  "one_liner": "Coda (Superhuman Docs) offers a broad REST API and official MCP with self-serve OAuth2/PAT access.",
  "auth_methods": [
    "OAuth2",
    "Personal Access Token"
  ],
  "access_model": {
    "kind": "Self-Serve",
    "note": "Official help shows OAuth2/PAT flows to connect MCP without approvals; community docs show self-serve API tokens; FinOps profile states the public API is free across tiers."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Easy",
  "main_blocker": "MCP is in beta; behavior and tools may change.",
  "recommended_next_action": "Build Now",
  "evidence_urls": [
    "https://coda.io/developers/apis/v1",
    "https://help.coda.io/hc/en-us/articles/44722661982989-Connect-to-the-Coda-MCP",
    "https://help.coda.io/hc/en-us/articles/44722756780173-Using-the-Coda-MCP",
    "https://coda.io/resources/guides/getting_started_with_coda_mcp",
    "https://mcpmux.com/servers/orellazri.coda-mcp-npx/",
    "https://apis.io/finops/coda/coda-finops/"
  ],
  "confidence": 0.72,
  "verification_status": "Auto",
  "slug": "coda",
  "primary_docs_url": "https://coda.io/developers/apis/v1",
  "rate_limit_note": "API reference includes a Rate Limiting section, but specific limits aren’t shown in the excerpt.",
  "last_verified": "2026-08-18"
}
```

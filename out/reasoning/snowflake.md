# Snowflake - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Snowflake official API authentication developer documentation", "Snowflake API production access approval credentials official documentation", "Snowflake official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://docs.snowflake.com | HTTP 200 | hint | topics=api
- https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/authentication | HTTP 200 | search_result | topics=api,auth,non_hosted
- https://docs.snowflake.cn/en/user-guide/api-authentication | HTTP 200 | search_result | topics=api,auth,access
- https://docs.snowflake.com/en/user-guide/intro-landing.html#pricing | HTTP 404 | search_result | topics=none
- https://www.snowflake.com/en/pricing-options/ | HTTP 200 | derived_guess | topics=access
- https://developer.snowflake.com | HTTP 200 | derived_guess | topics=api,access

## Model reasoning
1) API surface, MCP, auth credentials from evidence: The Snowflake REST APIs are documented, including an authentication page for those REST APIs (Authenticating Snowflake REST APIs with Snowflake). That page is the official source for REST auth and indicates modern methods (e.g., OAuth2, programmatic access tokens, and key-pair/JWT-based auth). Snowflake also documents an official, Snowflake-managed MCP server for agents, marked Generally Available, and provides SQL commands like SHOW MCP SERVERS to manage MCP objects. 2) Production Access Rubric: The docs home highlights "Getting a Trial Account," implying trial availability, but there is no statement that a new developer can obtain free, self-serve production credentials. The pricing page lists paid editions with "Get Started" for Standard/Enterprise/Business Critical, showing a commercial plan is required for ongoing/production use. There is no explicit evidence of self-serve, free production API entitlement without being a paying customer. Therefore, classify as Gated. 3) Conclusions: Auth methods supported for Snowflake’s public REST APIs are OAuth2, Personal Access Token (programmatic access tokens), and key-pair/private-key (mapped to Service Account). The dominant public integration surface is REST, with an additional official MCP surface. Access model is Gated due to lack of evidence for free self-serve production and the commercial pricing page. Buildability is Moderate (clear docs, but requires account/commercial access and auth setup). Recommended next action: Needs Outreach (ensure customer Snowflake account/plan or engage Snowflake/Sales).

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - Docs mention trials and paid editions; no evidence of free self-serve production API credentials. Production use requires a Snowflake account/plan.
- recommended_next_action: **Needs Outreach**
- confidence: **0.63**

## Evidence URLs
- https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/authentication
- https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp
- https://docs.snowflake.com/en/en/sql-reference/sql/show-mcp-servers
- https://docs.snowflake.com
- https://www.snowflake.com/en/pricing-options/

## Generated record
```json
{
  "app": "Snowflake",
  "category": "DevInfra",
  "one_liner": "Snowflake provides REST APIs and an official MCP server; production access requires a Snowflake account.",
  "auth_methods": [
    "OAuth2",
    "Personal Access Token",
    "Service Account"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Docs mention trials and paid editions; no evidence of free self-serve production API credentials. Production use requires a Snowflake account/plan."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "Production credentials require a Snowflake account/plan; no self-serve free production access documented.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/authentication",
    "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp",
    "https://docs.snowflake.com/en/en/sql-reference/sql/show-mcp-servers",
    "https://docs.snowflake.com",
    "https://www.snowflake.com/en/pricing-options/"
  ],
  "confidence": 0.63,
  "verification_status": "Auto",
  "slug": "snowflake",
  "primary_docs_url": "https://docs.snowflake.cn/en/user-guide/api-authentication",
  "rate_limit_note": "No explicit public rate limit details found in the cited docs.",
  "last_verified": "2026-08-18"
}
```

<!-- final-state:start -->
## Final pipeline state
_Updated 2026-08-18 by current human handcheck correction; this supersedes earlier key decisions._

```json
{
  "app": "Snowflake",
  "category": "DevInfra",
  "one_liner": "Snowflake provides REST APIs and an official MCP server; production access requires a Snowflake account.",
  "auth_methods": [
    "OAuth2",
    "Personal Access Token",
    "Service Account"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Docs mention trials and paid editions; no evidence of free self-serve production API credentials. Production use requires a Snowflake account/plan."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "Production credentials require a Snowflake account/plan; no self-serve free production access documented.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/authentication",
    "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp",
    "https://github.com/Snowflake-Labs/mcp"
  ],
  "confidence": 0.63,
  "verification_status": "Hand-Checked",
  "slug": "snowflake",
  "primary_docs_url": "https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/authentication",
  "rate_limit_note": "No explicit public rate limit details found in the cited docs.",
  "last_verified": "2026-08-18"
}
```
<!-- final-state:end -->

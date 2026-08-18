# Jira - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Jira official API authentication developer documentation", "Jira API production access approval credentials official documentation", "Jira official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://developer.atlassian.com | HTTP 200 | hint | topics=none
- https://developer.atlassian.com/server/jira/platform/jira-rest-api-example-oauth-authentication-6291692/ | HTTP 200 | search_result | topics=api,auth,access
- https://www.atlassian.com/software/jira/jira/pricing?utm_source=openai | HTTP 200 | search_result | topics=access
- https://developer.atlassian.com/server/jira/platform/basic-authentication/ | HTTP 200 | search_result | topics=api,auth
- https://developers.atlassian.com | HTTP 200 | derived_guess | topics=none
- https://docs.atlassian.com | HTTP 200 | derived_guess | topics=none

## Model reasoning
1) What the evidence states:
- REST/auth: The Jira Data Center docs explicitly list authentication methods for the REST API: “Basic authentication is available for Jira Data Center… consider using… OAuth 1.0a, OAuth 2.0, Personal access token.” The OAuth example page shows authenticating to Jira REST endpoints using OAuth alongside basic and cookie-based auth.
- MCP: Atlassian’s “Atlassian Rovo MCP Server” support page shows it connects AI agents to Jira and documents “Authentication and authorization,” including “Configuring OAuth 2.1” and “Configuring authentication via API token,” implying Jira access via MCP.
- Pricing/access: The Jira pricing page presents a “Free forever for 10 users” plan with a “Get it now” button, but it does not mention API/MCP production entitlement.

2) Production Access Rubric:
- There is no sentence explicitly granting self-serve PRODUCTION API or MCP access without approval. The pricing page indicates free signup but does not confirm API production use: it does not state that API access is enabled in production without review/approval. Therefore, based on the rubric, without explicit self-serve production entitlement, we must classify as Gated.

3) Decisions derived:
- auth_methods: OAuth2, Basic Auth, Personal Access Token, and Other Token (for OAuth 1.0a) are directly named in the docs.
- api_type: REST is the dominant integration surface; the MCP server exists but uses underlying APIs.
- existing_mcp: Official, since Atlassian documents the Rovo MCP server supporting Jira.
- access_model: Gated due to lack of explicit evidence that a new developer can obtain production API/MCP access self-serve.
- buildability: Moderate — clear REST/MCP auth docs exist, but production entitlement is unclear/possibly requires an existing site/admin.
- recommended_next_action: Needs Outreach — confirm production API/MCP eligibility and any plan/approval requirements.
- Rate limits: none cited in fetched docs.

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - Docs show OAuth2/API token and an official MCP server, but no explicit statement that production API/MCP access is self-serve; pricing page doesn’t confirm production API entitlement.
- recommended_next_action: **Needs Outreach**
- confidence: **0.53**

## Evidence URLs
- https://developer.atlassian.com/server/jira/platform/basic-authentication/
- https://developer.atlassian.com/server/jira/platform/jira-rest-api-example-oauth-authentication-6291692/
- https://support.atlassian.com/atlassian-rovo-mcp-server/docs/getting-started-with-the-atlassian-remote-mcp-server/
- https://www.atlassian.com/software/jira/jira/pricing?utm_source=openai

## Generated record
```json
{
  "app": "Jira",
  "category": "Productivity/PM",
  "one_liner": "Jira offers a broad REST API and an official MCP server, but production access terms aren’t explicitly self-serve.",
  "auth_methods": [
    "OAuth2",
    "Basic Auth",
    "Personal Access Token",
    "Other Token"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Docs show OAuth2/API token and an official MCP server, but no explicit statement that production API/MCP access is self-serve; pricing page doesn’t confirm production API entitlement."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "No explicit evidence of self-serve production entitlement; may require existing Jira site/admin and plan confirmation.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://developer.atlassian.com/server/jira/platform/basic-authentication/",
    "https://developer.atlassian.com/server/jira/platform/jira-rest-api-example-oauth-authentication-6291692/",
    "https://support.atlassian.com/atlassian-rovo-mcp-server/docs/getting-started-with-the-atlassian-remote-mcp-server/",
    "https://www.atlassian.com/software/jira/jira/pricing?utm_source=openai"
  ],
  "confidence": 0.53,
  "verification_status": "Auto",
  "slug": "jira",
  "primary_docs_url": "https://developer.atlassian.com/server/jira/platform/jira-rest-api-example-oauth-authentication-6291692/",
  "rate_limit_note": "No rate limit details in the cited sources; check Jira REST API limits per plan/site.",
  "last_verified": "2026-08-18"
}
```

<!-- final-state:start -->
## Final pipeline state
_Updated 2026-08-18 by current handcheck fold; this supersedes earlier key decisions._

```json
{
  "app": "Jira",
  "category": "Productivity/PM",
  "one_liner": "Jira offers a broad REST API and an official MCP server, but production access terms aren’t explicitly self-serve.",
  "auth_methods": [
    "OAuth2",
    "Basic Auth",
    "Personal Access Token",
    "Other Token"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Docs show OAuth2/API token and an official MCP server, but no explicit statement that production API/MCP access is self-serve; pricing page doesn’t confirm production API entitlement."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "No explicit evidence of self-serve production entitlement; may require existing Jira site/admin and plan confirmation.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://developer.atlassian.com/server/jira/platform/basic-authentication/",
    "https://developer.atlassian.com/server/jira/platform/jira-rest-api-example-oauth-authentication-6291692/",
    "https://support.atlassian.com/atlassian-rovo-mcp-server/docs/getting-started-with-the-atlassian-remote-mcp-server/",
    "https://www.atlassian.com/software/jira/jira/pricing?utm_source=openai"
  ],
  "confidence": 0.53,
  "verification_status": "Hand-Checked",
  "slug": "jira",
  "primary_docs_url": "https://developer.atlassian.com/server/jira/platform/jira-rest-api-example-oauth-authentication-6291692/",
  "rate_limit_note": "No rate limit details in the cited sources; check Jira REST API limits per plan/site.",
  "last_verified": "2026-08-18"
}
```
<!-- final-state:end -->

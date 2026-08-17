# GitHub - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["GitHub official API authentication developer documentation", "GitHub API production access approval credentials official documentation", "GitHub official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://docs.github.com/rest | HTTP 200 | hint | topics=api,auth
- https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api | HTTP 200 | search_result | topics=api,auth,access
- https://github.com/pricing?utm_source=openai | HTTP 200 | search_result | topics=api,access,mcp
- https://docs.github.com/en/enterprise-server%403.21/rest/authentication/authenticating-to-the-rest-api?utm_source=openai | HTTP 200 | search_result | topics=api,auth,access
- https://developer.github.com | HTTP 200 | derived_guess | topics=api,auth
- https://developers.github.com | HTTP 200 | derived_guess | topics=none

## Model reasoning
1) Evidence states: GitHub has a public REST API with extensive resources (docs.github.com/rest). The authentication guide covers personal access tokens (fine‑grained PATs), GitHub App installation/user tokens, and OAuth authorizations (docs.github.com/en/rest/authentication/authenticating-to-the-rest-api). MCP: There is a GitHub‑owned repository named github-mcp-server (github.com/github/github-mcp-server), indicating an official MCP server exists. 2) Production Access Rubric: While the pricing page shows a “Free … $0 USD per month forever … Join for free” plan (github.com/pricing), none of the fetched pages explicitly state that API production credentials are freely self‑serve without any gating beyond signup, and the auth docs describe how to authenticate but do not explicitly confer production entitlement. There is also no explicit statement that an official hosted MCP connection is self‑serve. Therefore, explicit proof of self‑serve production access is not present in the evidence. 3) Accordingly: auth_methods = Personal Access Token, OAuth2; api_type = REST; existing_mcp = Official (presence of vendor repo); access_model = Gated due to lack of explicit self‑serve production entitlement; buildability = Moderate (clear docs, but uncertainty on production access policy).

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - Docs show PAT and OAuth token mechanics, and pricing shows a Free plan, but no explicit statement confirms self‑serve PRODUCTION API entitlement or a hosted self‑serve MCP connection.
- recommended_next_action: **Needs Outreach**
- confidence: **0.62**

## Evidence URLs
- https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api
- https://docs.github.com/rest
- https://github.com/pricing?utm_source=openai
- https://github.com/github/github-mcp-server

## Generated record
```json
{
  "app": "GitHub",
  "category": "DevInfra",
  "one_liner": "GitHub offers a broad REST API with PAT/OAuth auth, but production access terms aren’t explicitly self-serve in docs.",
  "auth_methods": [
    "OAuth2",
    "Personal Access Token"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Docs show PAT and OAuth token mechanics, and pricing shows a Free plan, but no explicit statement confirms self‑serve PRODUCTION API entitlement or a hosted self‑serve MCP connection."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "No explicit evidence of self‑serve production API entitlement; potential plan or approval requirements unclear.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api",
    "https://docs.github.com/rest",
    "https://github.com/pricing?utm_source=openai",
    "https://github.com/github/github-mcp-server"
  ],
  "confidence": 0.62,
  "verification_status": "Auto",
  "slug": "github",
  "primary_docs_url": "https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api",
  "rate_limit_note": "Authenticated requests have higher limits; exact limits and plan impacts not confirmed in provided evidence.",
  "last_verified": "2026-08-18"
}
```

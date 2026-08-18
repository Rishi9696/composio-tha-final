# Front - synthesis reasoning
_generated 2026-08-17 | model openai:gpt-5_

## Research trace
- queries: ["Front official API authentication developer documentation", "Front API production access approval credentials official documentation", "Front official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://front.com | HTTP 200 | hint | topics=api,access
- https://dev.frontapp.com/reference/introduction | HTTP 200 | search_result | topics=api,auth
- https://help.front.com/en/articles/2178 | HTTP 200 | search_result | topics=access
- https://front.com/pricing | HTTP 200 | search_result | topics=api,access
- https://developer.front.com | HTTP 0 | derived_guess | topics=none
- https://developers.front.com | HTTP 0 | derived_guess | topics=none

## Model reasoning
1) What the evidence says: The official Front API Reference shows many REST resources/endpoints (Accounts, Analytics, Channels, Drafts, Messages, Comments, Attachments, Rules, Tags, etc.), indicating a broad REST surface (dev.frontapp.com/reference/introduction). The Front developer docs navigation explicitly lists “Authentication” with “OAuth” and “API tokens,” evidencing OAuth2 and API token auth options (dev.frontapp.com/docs/mcp-server). Front has an official MCP Server documented under Front Guides and announced in the official community as “the beta release of the Front MCP server,” with a note to “join the following group to learn how to get started,” indicating a vendor-published MCP surface that is in beta and requires joining a group (dev.frontapp.com/docs/mcp-server; community.front.com post). Pricing pages and help docs show Front is a paid product with a 14‑day free trial (front.com/pricing; help.front.com/en/articles/2178). The help article states: “When you start a free 14-day trial of Front… You do not need a credit card… If you'd like to trial the Enterprise plan, contact us…,” but does not promise ongoing free production API access. 2) Production Access Rubric: The pricing page shows paid plans and “Try for Free,” and the help article specifies a 14‑day trial with limitations. There is no statement that a new developer can obtain free, self‑serve production credentials without approval or payment. Per the rubric, because free access is time‑limited and continued use would require a paid plan, production access is Gated. The MCP server is also in beta and requires joining a group, reinforcing gating for that surface. 3) Decisions: Auth methods are OAuth2 and API Key per the developer docs. Dominant api_type is REST; MCP exists as an additional official surface (beta). Access_model is Gated due to paid plans and time‑limited trial. Buildability is Moderate (docs are clear with standard auth, but production requires becoming a paying customer and MCP is beta). Recommended next action is Needs Outreach (procure a paid account and/or join the MCP beta group).

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - Front is a paid product with a 14-day trial; no evidence of free self-serve production API access. MCP server is in beta and requires joining a group.
- recommended_next_action: **Needs Outreach**
- confidence: **0.66**

## Evidence URLs
- https://dev.frontapp.com/reference/introduction
- https://dev.frontapp.com/docs/mcp-server
- https://community.front.com/api-news-updates-40/the-front-mcp-server-is-here-beta-3712?utm_source=openai
- https://front.com/pricing
- https://help.front.com/en/articles/2178

## Generated record
```json
{
  "app": "Front",
  "category": "Support",
  "one_liner": "Front offers a broad REST API with OAuth2/API tokens; production access requires a paid plan.",
  "auth_methods": [
    "OAuth2",
    "API Key"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Front is a paid product with a 14-day trial; no evidence of free self-serve production API access. MCP server is in beta and requires joining a group."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "Production use requires a paid Front subscription; MCP server is beta and gated via a signup group.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://dev.frontapp.com/reference/introduction",
    "https://dev.frontapp.com/docs/mcp-server",
    "https://community.front.com/api-news-updates-40/the-front-mcp-server-is-here-beta-3712?utm_source=openai",
    "https://front.com/pricing",
    "https://help.front.com/en/articles/2178"
  ],
  "confidence": 0.66,
  "verification_status": "Auto",
  "slug": "front",
  "primary_docs_url": "https://front.com/pricing",
  "rate_limit_note": "Not specified in the cited pages.",
  "last_verified": "2026-08-17"
}
```

<!-- final-state:start -->
## Final pipeline state
_Updated 2026-08-18 by current handcheck fold; this supersedes earlier key decisions._

```json
{
  "app": "Front",
  "category": "Support",
  "one_liner": "Front offers a broad REST API with OAuth2/API tokens; production access requires a paid plan.",
  "auth_methods": [
    "Bearer Token",
    "OAuth2"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Front API access is included with paid plans; the self-serve trial is temporary and does not satisfy the production-access rubric."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "Yes",
  "buildability": "Moderate",
  "main_blocker": "Production API use requires an existing paid Front customer account.",
  "recommended_next_action": "Partner-Gated",
  "evidence_urls": [
    "https://dev.frontapp.com/docs/authentication",
    "https://help.front.com/en/articles/2438",
    "https://dev.frontapp.com/docs/mcp-server"
  ],
  "confidence": 0.66,
  "verification_status": "Hand-Checked",
  "slug": "front",
  "primary_docs_url": "https://dev.frontapp.com/docs/authentication",
  "rate_limit_note": "Not specified in the cited pages.",
  "last_verified": "2026-08-17"
}
```
<!-- final-state:end -->

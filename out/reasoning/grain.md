# Grain - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Grain official API authentication developer documentation", "Grain API production access approval credentials official documentation", "Grain official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://grain.com | HTTP 200 | hint | topics=api,auth,access,mcp
- https://developers.grain.com/authentication | HTTP 403 | search_result | topics=none
- https://support.grain.com/en/articles/9253220-plans | HTTP 200 | search_result | topics=api,access,mcp
- https://developers.grain.com/docs | HTTP 403 | search_result | topics=none
- https://developer.grain.com | HTTP 0 | derived_guess | topics=none
- https://developers.grain.com | HTTP 200 | derived_guess | topics=api,auth,access

## Model reasoning
1) Evidence of API surface, MCP, and auth: The Grain developer docs list three auth methods: Personal Access Token (PAT) and Workspace Access Token (WAT) that can be generated in-app at https://grain.com/app/settings/integrations?tab=api, and an OAuth2 Authorization Code flow with PKCE. The OAuth2 section explicitly shows “Step 1 … Request Client ID & Secret (manually).” The docs enumerate REST endpoints for recordings, transcripts (json/text), download/upload, tags, sharing, hooks, users, teams, and meeting types, and reference Versions and Rate Limits sections. MCP: Grain publishes an “Official Grain MCP Server: Quick Start Guide,” showing native integration with Claude (and notes about ChatGPT), with setup that redirects the user to Grain to approve access. The MCP quick start TOC includes “Free & Starter Plan MCP Tools” and “Business & Enterprise Plan MCP Tools.” 2) Production Access Rubric: The plans page states under Free: “What is not included: … API access.” and under Starter: “Additionally, the Starter Plan includes API access…”, which indicates production API access requires a paid plan. For MCP, the support article shows self-serve connector setup (“Select & connect Grain … You’ll be redirected to Grain to approve the connection”), while the plans page says Business includes “access to Grain’s advanced MCP server,” implying some MCP capabilities are plan-gated. OAuth client credentials require a manual request (“Request Client ID & Secret (manually)”). Together, this supports a Gated classification for production API access. 3) Conclusions: Auth methods are OAuth2, Personal Access Token, and a distinct Workspace Access Token (mapped as Other Token). Dominant public surface is REST; MCP also exists and is official. Access model is Gated (paid plan needed for API; OAuth client issued manually). Buildability is Hard due to paywall plus manual client issuance despite otherwise clear docs. Recommended next action: Needs Outreach (to obtain OAuth client approval and confirm plan entitlements, or upgrade to a paid plan).

## Key decisions
- buildability: **Hard**
- access_model: **Gated** - Free plan excludes API access; Starter includes API access. OAuth clients are issued manually. MCP connectors appear self-serve for basic use, but advanced MCP features are plan-gated.
- recommended_next_action: **Needs Outreach**
- confidence: **0.74**

## Evidence URLs
- https://developers.grain.com
- https://support.grain.com/en/articles/9253220-plans
- https://developers.grain.com/mcp?utm_source=openai
- https://support.grain.com/en/articles/14811968-grain-mcp?utm_source=openai

## Generated record
```json
{
  "app": "Grain",
  "category": "AI/Meeting-tools",
  "one_liner": "Grain has a REST API and official MCP, but production API access requires a paid plan and manual OAuth client.",
  "auth_methods": [
    "OAuth2",
    "Personal Access Token",
    "Other Token"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Free plan excludes API access; Starter includes API access. OAuth clients are issued manually. MCP connectors appear self-serve for basic use, but advanced MCP features are plan-gated."
  },
  "api_type": "REST",
  "api_breadth": "Moderate",
  "existing_mcp": "Official",
  "composio_toolkit": "No",
  "buildability": "Hard",
  "main_blocker": "API access requires a paid plan and OAuth client credentials are requested/approved manually.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://developers.grain.com",
    "https://support.grain.com/en/articles/9253220-plans",
    "https://developers.grain.com/mcp?utm_source=openai",
    "https://support.grain.com/en/articles/14811968-grain-mcp?utm_source=openai"
  ],
  "confidence": 0.74,
  "verification_status": "Auto",
  "slug": "grain",
  "primary_docs_url": "https://developers.grain.com",
  "rate_limit_note": "Rate limits are documented but specific values not confirmed in the fetched excerpt.",
  "last_verified": "2026-08-18"
}
```

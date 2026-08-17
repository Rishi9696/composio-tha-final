# Devin - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Devin official API authentication developer documentation", "Devin API production access approval credentials official documentation", "Devin official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://docs.devin.ai | HTTP 200 | hint | topics=api,auth,access,mcp
- https://docs.devin.ai/api-reference/authentication | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://agentplans.fyi/compare/devin/ | HTTP 200 | search_result | topics=api,access
- https://apis.io/apis/cognition/devin-api/ | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://developer.devin.ai | HTTP 0 | derived_guess | topics=none
- https://developers.devin.ai | HTTP 0 | derived_guess | topics=none

## Model reasoning
1) What the evidence says: The Devin API is documented on docs.devin.ai, with an Authentication page stating a “principal + token” model and sections for “Service users (recommended for automation)”, “Service User API Keys (Enterprise)”, and “Personal access tokens.” The API surface includes extensive endpoints across organization and enterprise scopes (as shown by the navigation on the auth page) and apis.io confirms it is a REST interface (“The Devin API is a REST interface… Endpoints are organized into Organization (/v3/organizations/*) and Enterprise (/v3/enterprise/*) scopes.”). Devin provides an official MCP server: the Devin MCP docs (both docs.devin.ai and docs.devinenterprise.com) note “Devin MCP Server” and that “Authentication [is] Required” with “Enterprise accounts: X-Org-Id header,” and describe supported transports (STDIO, SSE, HTTP). Auth credential types explicitly mentioned include Personal Access Tokens and Service User API Keys (Enterprise). 2) Production Access Rubric: There is no explicit statement that a new developer can obtain production credentials self-serve. Instead, the docs call out “Service User API Keys (Enterprise)” and MCP notes “Enterprise accounts: X-Org-Id header,” which implies enterprise gating. I find no sentence confirming free or self-serve production entitlement; therefore, per rubric, classify as Gated. 3) Conclusions: Auth methods are Personal Access Token and API Key (service user API keys). The dominant API type is REST. There is an official MCP. Access model is Gated due to enterprise-specific keys and no explicit self-serve production assurance. Buildability is Moderate (docs are clear, but production access likely needs paid/enterprise or approval). Recommended next action: Needs Outreach to obtain appropriate plan or enterprise access and confirm production credential issuance and limits.

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - Docs reference Enterprise-only Service User API Keys and MCP use requiring an enterprise X-Org-Id; no explicit self-serve production credential guarantee.
- recommended_next_action: **Needs Outreach**
- confidence: **0.58**

## Evidence URLs
- https://docs.devin.ai/api-reference/authentication
- https://docs.devin.ai/work-with-devin/devin-mcp
- https://docs.devinenterprise.com/work-with-devin/devin-mcp
- https://apis.io/apis/cognition/devin-api/

## Generated record
```json
{
  "app": "Devin",
  "category": "AI/Meeting-tools",
  "one_liner": "Devin exposes a broad REST API and official MCP; production access appears enterprise-gated.",
  "auth_methods": [
    "Personal Access Token",
    "API Key"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Docs reference Enterprise-only Service User API Keys and MCP use requiring an enterprise X-Org-Id; no explicit self-serve production credential guarantee."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Official",
  "composio_toolkit": "No",
  "buildability": "Moderate",
  "main_blocker": "No explicit self-serve production credentials; enterprise or paid plan likely required for API/MCP use.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://docs.devin.ai/api-reference/authentication",
    "https://docs.devin.ai/work-with-devin/devin-mcp",
    "https://docs.devinenterprise.com/work-with-devin/devin-mcp",
    "https://apis.io/apis/cognition/devin-api/"
  ],
  "confidence": 0.58,
  "verification_status": "Auto",
  "slug": "devin",
  "primary_docs_url": "https://docs.devin.ai/api-reference/authentication",
  "rate_limit_note": "Rate limits not specified in the cited docs.",
  "last_verified": "2026-08-18"
}
```

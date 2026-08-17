# NotebookLM - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["NotebookLM official API authentication developer documentation", "NotebookLM API production access approval credentials official documentation", "NotebookLM official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://cloud.google.com/gemini | HTTP 200 | hint | topics=api,auth,access
- https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/set-up-notebooklm | HTTP 200 | derived_guess | topics=api,auth,access
- https://www.googally.com/blog/notebooklm-pricing | HTTP 200 | search_result | topics=access
- https://deepwiki.com/jacob-bd/notebooklm-mcp/7-notebooklm-api-reference | HTTP 200 | search_result | topics=api,auth,mcp
- https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks | HTTP 200 | search_result | topics=api,auth
- https://developer.google.com | HTTP 200 | derived_guess | topics=api,auth,access

## Model reasoning
1) What the evidence says:
- Official API surface: The "Create and manage notebooks (API)" page for Gemini Notebook Enterprise documents REST methods (create, retrieve, list, delete, share). It is marked "Preview" under "Pre-GA Offerings Terms." The curl example shows Authorization: Bearer $(gcloud auth print-access-token), demonstrating a Bearer token in the Authorization header, and prerequisites include "Set up Gemini Notebook Enterprise" and "Get licenses for Gemini Notebook Enterprise."
- Enterprise setup: The "Set up Gemini Notebook Enterprise" page describes configuring an organizational identity provider (Cloud Identity/Google Workspace), indicating enterprise org setup is required.
- MCP: Community MCP servers exist. mcp.directory states "NotebookLM has no public API, so the server drives a real Chrome session," describing a community automation approach; Glama lists a community NotebookLM MCP wrapping a community client. No official vendor MCP is shown.
2) Production Access Rubric application:
- Gated evidence: The API docs require organizational setup and licensing: "Before you begin ... Set up Gemini Notebook Enterprise" and "Get licenses for Gemini Notebook Enterprise." The feature is "Preview" with Pre-GA terms. There is no statement that a new developer can self-serve production credentials without approval or paid enterprise licensing. Therefore, production access is Gated.
3) Decisions:
- Auth method evidenced is Bearer Token (Authorization header with a bearer token from gcloud), as the docs do not explicitly name OAuth2. Dominant surface is REST. Existing MCP is community. Given enterprise licensing and Pre-GA status, buildability is Hard and recommended action is Needs Outreach. No rate limit details are provided in the cited docs.

## Key decisions
- buildability: **Hard**
- access_model: **Gated** - API is an Enterprise feature in Preview; docs require org setup and licenses for Gemini Notebook Enterprise before use.
- recommended_next_action: **Needs Outreach**
- confidence: **0.62**

## Evidence URLs
- https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks
- https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/set-up-notebooklm
- https://mcp.directory/blog/notebooklm-mcp-complete-guide-2026
- https://glama.ai/mcp/servers/ripafratta/notebooklm-py-mcp

## Generated record
```json
{
  "app": "NotebookLM",
  "category": "AI/Meeting-tools",
  "one_liner": "Enterprise REST API (preview) using bearer tokens; org setup and licenses gate production access.",
  "auth_methods": [
    "Bearer Token"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "API is an Enterprise feature in Preview; docs require org setup and licenses for Gemini Notebook Enterprise before use."
  },
  "api_type": "REST",
  "api_breadth": "Moderate",
  "existing_mcp": "Community",
  "composio_toolkit": "No",
  "buildability": "Hard",
  "main_blocker": "Requires Gemini Notebook Enterprise org setup and licenses; API is Pre-GA with limited availability.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks",
    "https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/set-up-notebooklm",
    "https://mcp.directory/blog/notebooklm-mcp-complete-guide-2026",
    "https://glama.ai/mcp/servers/ripafratta/notebooklm-py-mcp"
  ],
  "confidence": 0.62,
  "verification_status": "Auto",
  "slug": "notebooklm",
  "primary_docs_url": "https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/set-up-notebooklm",
  "rate_limit_note": "No rate limit details found in the cited docs.",
  "last_verified": "2026-08-18"
}
```

## Risk seed (withheld from synthesis)
This prior was retained only for audit sampling and was not shown to the model.
```json
{
  "api_type": "None",
  "access_model": "Gated",
  "recommended_next_action": "Needs Outreach",
  "main_blocker": "No public NotebookLM API; the closest workaround is the Gemini Enterprise API."
}
```

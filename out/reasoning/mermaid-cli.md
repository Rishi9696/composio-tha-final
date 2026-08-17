# Mermaid CLI - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Mermaid CLI official API authentication developer documentation", "Mermaid CLI API production access approval credentials official documentation", "Mermaid CLI official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://github.com/mermaid-js/mermaid-cli | HTTP 200 | hint | topics=api,access,mcp
- https://www.mermaidonline.live/pricing?utm_source=openai | HTTP 200 | search_result | topics=none
- https://github.com/mermaid-js/mermaid-cli?utm_source=openai | HTTP 200 | search_result | topics=api,access,mcp
- https://github.com/mermaidjs/mermaid.cli?utm_source=openai | HTTP 200 | search_result | topics=access,mcp
- https://developer.github.com | HTTP 200 | derived_guess | topics=api,auth
- https://developers.github.com | HTTP 200 | derived_guess | topics=none

## Model reasoning
1) What the fetched evidence actually states:
- The GitHub repository mermaid-js/mermaid-cli shows an open-source command-line tool for Mermaid; the fetched page content reveals a repository listing but no mention of a hosted web API surface or authentication for remote access. It is a CLI (local tooling), not an HTTP API (https://github.com/mermaid-js/mermaid-cli).
- The older mermaidjs/mermaid.cli repo is archived and similarly reflects a code repository, not a hosted API (https://github.com/mermaidjs/mermaid.cli?utm_source=openai).
- Mermaid Chart documentation includes an “MCP Server” docs page (https://mermaid.ai/docs/ai/mcp-server?utm_source=openai), which indicates an official MCP surface exists. The visible snippet shows site navigation (“Claude MCP App”, “MCP Server”, “Sign in”, “Start free”, “Contact sales”), but the fetched text does not explicitly state the authentication mechanism (e.g., API key, OAuth) nor confirm self-serve production credential issuance.
- The Wikipedia MCP article is generic background and does not provide vendor-specific access or auth details (https://en.wikipedia.org/wiki/Model_Context_Protocol?utm_source=openai).
2) Production Access Rubric application:
- There is no evidence that Mermaid CLI exposes a hosted API requiring credentials; it is a local CLI.
- For the Mermaid Chart MCP Server page, the fetched snippet contains no explicit sentence confirming that a new developer can obtain production credentials self-serve. The presence of “Sign in” and “Contact sales” suggests possible gating, but we lack a clear statement of self-serve production entitlement. Therefore, per the rubric, absent explicit self-serve proof, classify as Gated.
3) Decisions from the above:
- Since Mermaid CLI itself has no hosted API/MCP surface in the evidence, the dominant integration surface for this app is none. An official MCP server exists for Mermaid Chart as a separate product, but auth details and production access are unclear in the fetched text. This leads to Gated access (no self-serve proof), buildability Blocked for this app (no usable hosted surface documented), and auth_methods None / Not Applicable for Mermaid CLI.

## Key decisions
- buildability: **Blocked**
- access_model: **Gated** - Mermaid CLI exposes no hosted API; Mermaid Chart’s MCP Server docs exist but do not state self-serve production credential availability. Navigation shows “Sign in” and “Contact sales,” implying potential gating.
- recommended_next_action: **Blocked**
- confidence: **0.34**

## Evidence URLs
- https://github.com/mermaid-js/mermaid-cli
- https://github.com/mermaidjs/mermaid.cli?utm_source=openai
- https://mermaid.ai/docs/ai/mcp-server?utm_source=openai

## Generated record
```json
{
  "app": "Mermaid CLI",
  "category": "AI/Meeting-tools",
  "one_liner": "Mermaid CLI is a local tool with no hosted API; a separate Mermaid Chart MCP exists but access is unclear.",
  "auth_methods": [
    "None / Not Applicable"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Mermaid CLI exposes no hosted API; Mermaid Chart’s MCP Server docs exist but do not state self-serve production credential availability. Navigation shows “Sign in” and “Contact sales,” implying potential gating."
  },
  "api_type": "None",
  "api_breadth": "Narrow",
  "existing_mcp": "Official",
  "composio_toolkit": "No",
  "buildability": "Blocked",
  "main_blocker": "No documented hosted API/MCP for Mermaid CLI; Mermaid Chart MCP exists but access/auth details are not confirmed.",
  "recommended_next_action": "Blocked",
  "evidence_urls": [
    "https://github.com/mermaid-js/mermaid-cli",
    "https://github.com/mermaidjs/mermaid.cli?utm_source=openai",
    "https://mermaid.ai/docs/ai/mcp-server?utm_source=openai"
  ],
  "confidence": 0.34,
  "verification_status": "Auto",
  "slug": "mermaid-cli",
  "primary_docs_url": "https://github.com/mermaid-js/mermaid-cli",
  "rate_limit_note": "No public rate limit information found in the fetched documentation.",
  "last_verified": "2026-08-18"
}
```

## Risk seed (withheld from synthesis)
This prior was retained only for audit sampling and was not shown to the model.
```json
{
  "api_type": "None",
  "access_model": "Self-Serve",
  "recommended_next_action": "Blocked",
  "main_blocker": "Open-source CLI/library (diagram rendering), not a hosted API service."
}
```

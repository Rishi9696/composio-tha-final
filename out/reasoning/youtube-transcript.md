# YouTube Transcript - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["YouTube Transcript official API authentication developer documentation", "YouTube Transcript API production access approval credentials official documentation", "YouTube Transcript official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://transcriptapi.com | HTTP 200 | hint | topics=api,auth,access,mcp
- https://transcriptapi.com/docs/api/ | HTTP 200 | search_result | topics=api,auth,mcp
- https://www.youtubetranscript.dev/pricing | HTTP 200 | search_result | topics=api,access
- https://skipthewatch.com/blog/youtube-transcript-api-guide | HTTP 200 | search_result | topics=api,auth,access
- https://developer.transcriptapi.com | HTTP 0 | derived_guess | topics=none
- https://developers.transcriptapi.com | HTTP 0 | derived_guess | topics=none

## Model reasoning
1) API/MCP/auth from evidence: transcriptapi.com home says the product works "via REST API or YouTube MCP" and shows requests using Authorization: Bearer API_KEY. The API reference (transcriptapi.com/docs/api/) lists a REST base URL (https://transcriptapi.com/api/v2), multiple endpoints (transcript, search, channel, playlist), credit usage per endpoint, and error codes including 401 Unauthorized and 402 Payment Required. The TranscriptAPI blog states "TranscriptAPI has a native MCP server". The MCP docs at youtubetranscripts.co/docs/mcp state the MCP server supports two authentication methods: OAuth (browser-based, access/refresh tokens) or a long‑lived API key. 2) Production Access Rubric: Evidence shows credential enablement ("Get API Key") but also credit-based billing and "402 Payment Required" in the API reference. There is no statement that full production use is freely self‑serve; instead, endpoints consume credits and payment is implicated. Per rubric, absent explicit proof of free self‑serve production and with paid credits required, classify as Gated. 3) Conclusions: Auth methods are API Key (for REST and MCP) and OAuth2 (for MCP). Dominant surface is REST (MCP also exists officially). API breadth is moderate (transcripts, search, channel, playlists). Existing MCP is Official per vendor docs/blog. Buildability is Moderate (clear REST docs and API key flow, but production gated by paid credits). Main blocker: paid/credit gating, not approval. Recommended next action: Needs Outreach (sign up/purchase to enable production credits). Rate limits are mentioned but unspecified; headers and 402 Payment Required noted.

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - Credentials are self-serve, but API usage is credit-based with 402 Payment Required; no evidence of free production entitlement.
- recommended_next_action: **Needs Outreach**
- confidence: **0.62**

## Evidence URLs
- https://transcriptapi.com
- https://transcriptapi.com/docs/api/
- https://transcriptapi.com/blog/youtube-mcp-server-setup-connect-claude
- https://youtubetranscripts.co/docs/mcp

## Generated record
```json
{
  "app": "YouTube Transcript",
  "category": "AI/Meeting-tools",
  "one_liner": "YouTube transcripts and discovery via REST and official MCP; API key or OAuth for MCP; production is credit-based.",
  "auth_methods": [
    "API Key",
    "OAuth2"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Credentials are self-serve, but API usage is credit-based with 402 Payment Required; no evidence of free production entitlement."
  },
  "api_type": "REST",
  "api_breadth": "Moderate",
  "existing_mcp": "Official",
  "composio_toolkit": "No",
  "buildability": "Moderate",
  "main_blocker": "Production use requires paid credits; no explicit free self-serve production tier confirmed.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://transcriptapi.com",
    "https://transcriptapi.com/docs/api/",
    "https://transcriptapi.com/blog/youtube-mcp-server-setup-connect-claude",
    "https://youtubetranscripts.co/docs/mcp"
  ],
  "confidence": 0.62,
  "verification_status": "Auto",
  "slug": "youtube-transcript",
  "primary_docs_url": "https://transcriptapi.com",
  "rate_limit_note": "Docs mention rate limits and headers; usage is also constrained by credits and may return 402 Payment Required when exceeded.",
  "last_verified": "2026-08-18"
}
```

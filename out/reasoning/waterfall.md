# Waterfall.io - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["Waterfall.io official API authentication developer documentation", "Waterfall.io API production access approval credentials official documentation", "Waterfall.io official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://waterfall.io | HTTP 200 | hint | topics=api,auth,access
- https://docs.waterfall.io/v1/introduction | HTTP 200 | search_result | topics=api,auth
- https://www.waterfall.io/book-a-call | HTTP 200 | search_result | topics=api,auth,access
- https://www.waterfall.io/ | HTTP 200 | search_result | topics=api,auth,access
- https://developer.waterfall.io | HTTP 0 | derived_guess | topics=none
- https://developers.waterfall.io | HTTP 0 | derived_guess | topics=none

## Model reasoning
1) Evidence of API surface, MCP, and auth: The Waterfall API docs state: “The Waterfall API is available at https://api.waterfall.io. All requests require an API key in the x-api-key header.” The docs list many REST endpoints (Prospector, Search Contact/Company, Contact/Phone/Company Enrichment, Job Change, Email Verification, Company Reveal/Titles) and include “API Keys Management” endpoints (List/Create/Modify). No OAuth is mentioned. The docs navigation includes a “Rate limit” section, but no specific limits were captured. There is no mention of MCP or any MCP server. 2) Production Access Rubric application: The “Book a call” page describes a manual sales process: “Book a call… Talk to our team… Run data quality/coverage tests… Sign, integrate and go-live.” Pricing is prepaid/top-up and indicates a commercial relationship. It also says, “We are very selective in partnering with platform customers,” implying review/approval for certain use cases. There is no evidence of self-serve production credential issuance or a public signup to generate keys. Therefore, production access is Gated. 3) Conclusions: Auth methods = API Key. API type = REST. No MCP evidence, so existing_mcp = None. Access model = Gated due to required sales contact and signing before go-live. Buildability = Hard (manual approval/commercial step despite clear docs). Recommended next action = Needs Outreach to request access and keys. Rate limit details unknown beyond the presence of a section in docs.

## Key decisions
- buildability: **Hard**
- access_model: **Gated** - Docs require an x-api-key for all requests, but there is no self-serve signup. The Book a Call page outlines a manual flow—“Book a call… Talk to our team… Run tests… Sign, integrate and go-live”—and describes prepaid/commercial terms and selective partnerships.
- recommended_next_action: **Needs Outreach**
- confidence: **0.68**

## Evidence URLs
- https://docs.waterfall.io/v1/introduction
- https://www.waterfall.io/book-a-call
- https://www.waterfall.io/

## Generated record
```json
{
  "app": "Waterfall.io",
  "category": "Research/Scraping",
  "one_liner": "REST B2B enrichment API with API key auth; production access requires sales contact and commercial agreement.",
  "auth_methods": [
    "API Key"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Docs require an x-api-key for all requests, but there is no self-serve signup. The Book a Call page outlines a manual flow—“Book a call… Talk to our team… Run tests… Sign, integrate and go-live”—and describes prepaid/commercial terms and selective partnerships."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "None",
  "composio_toolkit": "No",
  "buildability": "Hard",
  "main_blocker": "Production credentials appear to require sales engagement and a signed commercial agreement; no self-serve key issuance.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://docs.waterfall.io/v1/introduction",
    "https://www.waterfall.io/book-a-call",
    "https://www.waterfall.io/"
  ],
  "confidence": 0.68,
  "verification_status": "Auto",
  "slug": "waterfall",
  "primary_docs_url": "https://waterfall.io",
  "rate_limit_note": "Docs include a Rate limit section; specific limits were not present in the fetched excerpt.",
  "last_verified": "2026-08-18"
}
```

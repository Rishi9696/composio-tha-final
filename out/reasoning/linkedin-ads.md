# LinkedIn Ads - synthesis reasoning
_generated 2026-08-18 | model openai:gpt-5_

## Research trace
- queries: ["LinkedIn Ads official API authentication developer documentation", "LinkedIn Ads API production access approval credentials official documentation", "LinkedIn Ads official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://learn.microsoft.com/linkedin/marketing | HTTP 200 | hint | topics=api,auth,access
- https://learn.microsoft.com/en-us/linkedin/marketing/ | HTTP 200 | search_result | topics=api,auth,access
- https://www.linkedin.com/help/linkedin/answer/a524477 | HTTP 200 | search_result | topics=api,access
- https://zernio.com/linkedin-ads-api | HTTP 200 | search_result | topics=api,auth,access,mcp
- https://developer.microsoft.com | HTTP 200 | derived_guess | topics=api,auth,access,mcp
- https://developers.microsoft.com | HTTP 200 | derived_guess | topics=api,auth,access,mcp

## Model reasoning
1) Evidence summary: The LinkedIn Marketing API Program page states the platform "offers APIs to create LinkedIn marketing campaigns, to report campaign performance, to manage leads, and to grow a company Page" and lists an Authentication How-To Guide and multiple API areas (Advertising, Reporting, Events, Community, Lead Sync, Matched Audiences, Audience Insights, Media Planning, Conversions), but does not itself detail auth mechanics. The LinkedIn Help page for Advertising API Application Review explicitly describes an access request form and a review process before approval. Third-party Zernio states the Advertising API requires a partner application and compliance review, and shows their wrapper uses an API key to call Zernio plus an OAuth flow to connect LinkedIn Ads accounts; it also notes LinkedIn enforces application-level and per-member rate limits. No fetched evidence shows an official MCP server. 2) Production Access Rubric: The LinkedIn Help page says: "Create an app... add Advertising API... Complete the Access Request Form... After completing the Access Request Form, we’ll review and notify you of the status and outcome," which demonstrates manual review and therefore Gated production access. There is no evidence of self-serve production credentials. 3) Decisions: Auth is OAuth2 for the official API (the docs cite an Authentication guide and third-party shows OAuth account connection; explicit official auth details aren’t in the fetched text, so confidence is tempered). The dominant surface is REST. No MCP evidence, so existing_mcp = None. Access model is Gated due to the required application review. Buildability is Hard because production use requires approval. Next action: Needs Outreach (apply and work through review).

## Key decisions
- buildability: **Hard**
- access_model: **Gated** - Advertising API requires completing an Access Request Form and passing LinkedIn’s review before production use.
- recommended_next_action: **Needs Outreach**
- confidence: **0.64**

## Evidence URLs
- https://learn.microsoft.com/en-us/linkedin/marketing/
- https://learn.microsoft.com/linkedin/marketing
- https://www.linkedin.com/help/linkedin/answer/a524477
- https://zernio.com/linkedin-ads-api

## Generated record
```json
{
  "app": "LinkedIn Ads",
  "category": "Ads/Marketing",
  "one_liner": "LinkedIn Ads offers REST Marketing APIs, but production access requires application review and approval.",
  "auth_methods": [
    "OAuth2"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Advertising API requires completing an Access Request Form and passing LinkedIn’s review before production use."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "None",
  "composio_toolkit": "Yes",
  "buildability": "Hard",
  "main_blocker": "Must apply for Advertising API access and receive approval; no self-serve production credentials.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://learn.microsoft.com/en-us/linkedin/marketing/",
    "https://learn.microsoft.com/linkedin/marketing",
    "https://www.linkedin.com/help/linkedin/answer/a524477",
    "https://zernio.com/linkedin-ads-api"
  ],
  "confidence": 0.64,
  "verification_status": "Auto",
  "slug": "linkedin-ads",
  "primary_docs_url": "https://learn.microsoft.com/en-us/linkedin/marketing/",
  "rate_limit_note": "Third-party notes app-level and per-member limits; official rate-limit details not in fetched docs.",
  "last_verified": "2026-08-18"
}
```

## Risk seed (withheld from synthesis)
This prior was retained only for audit sampling and was not shown to the model.
```json
{
  "access_model": "Gated",
  "recommended_next_action": "Needs Outreach",
  "main_blocker": "Marketing API access requires LinkedIn Marketing Developer Platform / partner approval."
}
```

<!-- final-state:start -->
## Final pipeline state
_Updated 2026-08-18 by current handcheck fold; this supersedes earlier key decisions._

```json
{
  "app": "LinkedIn Ads",
  "category": "Ads/Marketing",
  "one_liner": "LinkedIn Ads offers REST Marketing APIs, but production access requires application review and approval.",
  "auth_methods": [
    "OAuth2"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Advertising API requires completing an Access Request Form and passing LinkedIn’s review before production use."
  },
  "api_type": "REST",
  "api_breadth": "Broad",
  "existing_mcp": "Community",
  "composio_toolkit": "Yes",
  "buildability": "Hard",
  "main_blocker": "Must apply for Advertising API access and receive approval; no self-serve production credentials.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication",
    "https://learn.microsoft.com/en-us/linkedin/marketing/increasing-access?view=li-lms-2026-06",
    "https://libraries.io/pypi/linkedin-ads-mcp"
  ],
  "confidence": 0.64,
  "verification_status": "Hand-Checked",
  "slug": "linkedin-ads",
  "primary_docs_url": "https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication",
  "rate_limit_note": "Third-party notes app-level and per-member limits; official rate-limit details not in fetched docs.",
  "last_verified": "2026-08-18"
}
```
<!-- final-state:end -->

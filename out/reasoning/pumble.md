# Pumble - synthesis reasoning
_generated 2026-08-17 | model openai:gpt-5_

## Research trace
- queries: ["Pumble official API authentication developer documentation", "Pumble API production access approval credentials official documentation", "Pumble official pricing API access free plan trial production plan"]
- evidence quality: **adequate**
- https://pumble.com | HTTP 200 | hint | topics=api,access,mcp
- https://pumble.com/help/integrations/automation-workflow-integrations/api-keys-integration/ | HTTP 200 | search_result | topics=api,auth,access
- https://pumble.com/help/workspace-administration/pricing/pumble-subscription-plans-and-extra-features/ | HTTP 200 | search_result | topics=api,access
- https://pumble.com/help/workspace-administration/pricing/pumble-subscription-plans-and-extra-features/?utm_source=openai | HTTP 200 | search_result | topics=api,access
- https://developer.pumble.com | HTTP 200 | derived_guess | topics=access
- https://developers.pumble.com | HTTP 200 | derived_guess | topics=access

## Model reasoning
1) Evidence: The Pumble API Overview states the API addon lets users “generate an API key” to send messages, reactions, delete messages, create channels, list channels/DMs, and it’s “Available on all plans.” It also notes, “The rate limit is up to 1000 requests per minute per user,” and mentions Swagger usage by entering the API key. The MCP server guide says to connect an AI assistant you “will have to create a Pumble addon and take credentials from there,” with steps to create/configure an app. The pricing page says, “You can use Pumble Free account… or upgrade to a paid plan,” and shows plan limits, including Integrations caps, but does not explicitly discuss API production entitlement or approvals. 2) Production Access Rubric: While the API page shows key generation and says “Available on all plans,” there is no explicit statement that new developers get free, self-serve PRODUCTION credentials without any approval; the pricing page mentions free and paid plans but does not confirm production API entitlement. Therefore, per the rubric (signup/key generation alone is insufficient), there is no explicit proof of self-serve production access. 3) Conclusions: Auth methods: API Key (from the addon). API type: REST (Swagger, simple HTTP requests). Existing MCP: Official (Pumble Help for MCP server). Access model: Gated (no explicit self-serve production confirmation). Buildability: Moderate (docs are clear; access terms for production are not explicit). Next action: Needs Outreach (confirm production use and plan requirements). Rate limit: up to 1000 rpm per user.

## Key decisions
- buildability: **Moderate**
- access_model: **Gated** - Docs show self-generated API keys via an API addon and MCP credentials from an addon, but there is no explicit statement guaranteeing free, self-serve production entitlement; plan-based integration limits also apply.
- recommended_next_action: **Needs Outreach**
- confidence: **0.58**

## Evidence URLs
- https://pumble.com/help/integrations/automation-workflow-integrations/api-keys-integration/
- https://pumble.com/help/workspace-administration/pricing/pumble-subscription-plans-and-extra-features/
- https://pumble.com/help/integrations/automation-workflow-integrations/how-to-use-the-pumble-mcp-server/

## Generated record
```json
{
  "app": "Pumble",
  "category": "Comms",
  "one_liner": "Pumble provides a REST API via addon with API keys and an official MCP server, but production terms are unclear.",
  "auth_methods": [
    "API Key"
  ],
  "access_model": {
    "kind": "Gated",
    "note": "Docs show self-generated API keys via an API addon and MCP credentials from an addon, but there is no explicit statement guaranteeing free, self-serve production entitlement; plan-based integration limits also apply."
  },
  "api_type": "REST",
  "api_breadth": "Moderate",
  "existing_mcp": "Official",
  "composio_toolkit": "No",
  "buildability": "Moderate",
  "main_blocker": "No explicit confirmation of self-serve production access; unclear plan requirements and possible integration limits.",
  "recommended_next_action": "Needs Outreach",
  "evidence_urls": [
    "https://pumble.com/help/integrations/automation-workflow-integrations/api-keys-integration/",
    "https://pumble.com/help/workspace-administration/pricing/pumble-subscription-plans-and-extra-features/",
    "https://pumble.com/help/integrations/automation-workflow-integrations/how-to-use-the-pumble-mcp-server/"
  ],
  "confidence": 0.58,
  "verification_status": "Auto",
  "slug": "pumble",
  "primary_docs_url": "https://pumble.com/help/integrations/automation-workflow-integrations/api-keys-integration/",
  "rate_limit_note": "Docs state up to 1000 requests per minute per user.",
  "last_verified": "2026-08-17"
}
```

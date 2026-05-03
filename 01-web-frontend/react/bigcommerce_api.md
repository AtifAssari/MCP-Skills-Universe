---
title: bigcommerce-api
url: https://skills.sh/qdhenry/claude-command-suite/bigcommerce-api
---

# bigcommerce-api

skills/qdhenry/claude-command-suite/bigcommerce-api
bigcommerce-api
Installation
$ npx skills add https://github.com/qdhenry/claude-command-suite --skill bigcommerce-api
SKILL.md

<essential_principles>

Always check which version supports your specific endpoint.

Never embed credentials in client-side code. Use environment variables.

Monitor headers: X-Rate-Limit-Requests-Left, X-Rate-Limit-Time-Reset-Ms Implement exponential backoff with jitter for retries.

Always include channel_id when working with multi-storefront stores.

</essential_principles>

Build a new integration (REST API, webhooks, data sync)
Create a headless storefront (GraphQL Storefront, Next.js/Catalyst)
Develop a BigCommerce app (single-click app, marketplace)
Work with specific API (Catalog, Orders, Customers, Payments)
Debug an API issue (errors, authentication, rate limits)
Set up webhooks and event handling
Something else

Wait for response before proceeding.

After reading the workflow, follow it exactly.

<verification_loop> After every API operation:

# 1. Check response status
# 200/201 = Success
# 4xx = Client error (check request)
# 5xx = Server error (retry with backoff)

# 2. Verify rate limit headers
X-Rate-Limit-Requests-Left: [remaining]
X-Rate-Limit-Time-Reset-Ms: [reset time]

# 3. For mutations, verify the change
GET the resource to confirm state


Report to user:

"API call: [status]"
"Rate limit remaining: [X]"
"Data verified: [confirmation]" </verification_loop>

<reference_index>

Authentication & Security:

references/authentication.md - OAuth, tokens, scopes, credentials
references/security-best-practices.md - API keys, PCI compliance, headers

Core APIs:

references/catalog-api.md - Products, categories, brands, variants
references/orders-api.md - Orders, shipments, transactions, fulfillment
references/customers-api.md - Customers, addresses, groups, segments
references/payments-api.md - Payment processing, gateways, checkout

Storefront & Content:

references/graphql-storefront.md - GraphQL queries, carts, checkout
references/widgets-scripts.md - Widgets API, Scripts API, content injection
references/stencil-themes.md - Theme development, Handlebars, CLI

Platform Features:

references/webhooks.md - Events, subscriptions, retry logic
references/multi-storefront.md - MSF, channels, site routing
references/headless-commerce.md - Next.js Commerce, Catalyst, React

Development:

references/app-development.md - Single-click apps, Developer Portal
references/rate-limits-pagination.md - Throttling, cursor pagination, batching
references/error-handling.md - Status codes, troubleshooting, debugging

</reference_index>

<workflows_index>

Workflow	Purpose
build-integration.md	Create data sync, connect external systems
build-headless-storefront.md	Next.js/Catalyst headless frontend
build-app.md	Single-click marketplace app
work-with-api.md	Use specific BigCommerce API
debug-api-issue.md	Fix errors and authentication problems
setup-webhooks.md	Configure webhook subscriptions
</workflows_index>	

<quick_reference>

Base URLs:

REST API: https://api.bigcommerce.com/stores/{store_hash}/v3/
Payments: https://payments.bigcommerce.com/stores/{store_hash}/payments
GraphQL Storefront: https://{store_domain}/graphql
OAuth Token: https://login.bigcommerce.com/oauth2/token

Essential Headers:

X-Auth-Token: {access_token}
Content-Type: application/json
Accept: application/json


GraphQL Storefront Auth:

Authorization: Bearer {storefront_token}


</quick_reference>

Weekly Installs
13
Repository
qdhenry/claude-…nd-suite
GitHub Stars
1.2K
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
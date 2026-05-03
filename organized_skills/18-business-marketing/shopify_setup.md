---
rating: ⭐⭐
title: shopify-setup
url: https://skills.sh/jezweb/claude-skills/shopify-setup
---

# shopify-setup

skills/jezweb/claude-skills/shopify-setup
shopify-setup
Installation
$ npx skills add https://github.com/jezweb/claude-skills --skill shopify-setup
SKILL.md
Shopify Setup

Set up working Shopify CLI authentication and Admin API access for a store. Produces a verified API connection ready for product and content management.

Workflow
Step 1: Check Prerequisites

Verify the Shopify CLI is installed:

shopify version


If not installed:

npm install -g @shopify/cli

Step 2: Authenticate with the Store
shopify auth login --store mystore.myshopify.com


This opens a browser for OAuth. The user must be a store owner or staff member with appropriate permissions.

After login, verify:

shopify store info

Step 3: Create a Custom App for API Access

Custom apps provide stable Admin API access tokens (unlike CLI session tokens which expire).

Check if an app already exists: Ask the user if they have a custom app set up. If yes, skip to Step 4.

If no custom app exists, guide the user through creation via browser:

Navigate to https://{store}.myshopify.com/admin/settings/apps/development
Click Create an app
Name it (e.g. "Claude Code Integration")
Click Configure Admin API scopes
Enable these scopes (see references/api-scopes.md for details):
read_products, write_products
read_content, write_content
read_product_listings
read_inventory, write_inventory
read_files, write_files
Click Save then Install app
Copy the Admin API access token (shown only once)

Use browser automation (Chrome MCP or playwright-cli) if the user prefers assistance navigating the admin.

Step 4: Store the Access Token

Store the token securely. Never commit it to git.

For project use — create .dev.vars:

SHOPIFY_STORE=mystore.myshopify.com
SHOPIFY_ACCESS_TOKEN=shpat_xxxxxxxxxxxxxxxxxxxxx


Ensure .dev.vars is in .gitignore.

For cross-project use — store in your preferred secrets manager (environment variable, 1Password CLI, etc.).

Step 5: Verify API Access

Test the connection with a simple GraphQL query:

curl -s https://{store}.myshopify.com/admin/api/2025-01/graphql.json \
  -H "Content-Type: application/json" \
  -H "X-Shopify-Access-Token: {token}" \
  -d '{"query": "{ shop { name primaryDomain { url } } }"}' | jq .


Expected response includes the shop name and domain. If you get a 401, the token is invalid or expired — recreate the app.

Step 6: Save Store Config

Create a shopify.config.json in the project root for other skills to reference:

{
  "store": "mystore.myshopify.com",
  "apiVersion": "2025-01",
  "tokenSource": ".dev.vars"
}

Critical Patterns
API Version

Always specify an explicit API version (e.g. 2025-01). Using unstable in production will break without warning. Shopify retires API versions quarterly.

Token Types
Token	Format	Use
Admin API access token	shpat_*	Custom apps — stable, long-lived
CLI session token	Short-lived	Shopify CLI commands only
Storefront API token	shpca_*	Public storefront queries

This skill sets up Admin API access tokens — the right choice for product and content management.

Rate Limits

Shopify uses a leaky bucket rate limiter:

REST: 40 requests/second burst, 2/second sustained
GraphQL: 1,000 cost points per second, max 2,000 points per query

For bulk operations, use the bulkOperationRunQuery mutation instead of looping.

Reference Files
references/api-scopes.md — Admin API scopes needed for product and content management
Weekly Installs
668
Repository
jezweb/claude-skills
GitHub Stars
759
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail
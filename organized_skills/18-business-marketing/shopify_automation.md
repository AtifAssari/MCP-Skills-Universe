---
rating: ⭐⭐
title: shopify-automation
url: https://skills.sh/aaaaqwq/claude-code-skills/shopify-automation
---

# shopify-automation

skills/aaaaqwq/claude-code-skills/shopify-automation
shopify-automation
Installation
$ npx skills add https://github.com/aaaaqwq/claude-code-skills --skill shopify-automation
SKILL.md
Shopify Automation via Rube MCP

Automate Shopify operations through Composio's Shopify toolkit via Rube MCP.

Prerequisites
Rube MCP must be connected (RUBE_SEARCH_TOOLS available)
Active Shopify connection via RUBE_MANAGE_CONNECTIONS with toolkit shopify
Always call RUBE_SEARCH_TOOLS first to get current tool schemas
Setup

Get Rube MCP: Add https://rube.app/mcp as an MCP server in your client configuration. No API keys needed — just add the endpoint and it works.

Verify Rube MCP is available by confirming RUBE_SEARCH_TOOLS responds
Call RUBE_MANAGE_CONNECTIONS with toolkit shopify
If connection is not ACTIVE, follow the returned auth link to complete Shopify OAuth
Confirm connection status shows ACTIVE before running any workflows
Core Workflows
1. Manage Products

When to use: User wants to list, search, create, or manage products

Tool sequence:

SHOPIFY_GET_PRODUCTS / SHOPIFY_GET_PRODUCTS_PAGINATED - List products [Optional]
SHOPIFY_GET_PRODUCT - Get single product details [Optional]
SHOPIFY_BULK_CREATE_PRODUCTS - Create products in bulk [Optional]
SHOPIFY_GET_PRODUCTS_COUNT - Get product count [Optional]

Key parameters:

product_id: Product ID for single retrieval
title: Product title
vendor: Product vendor
status: 'active', 'draft', or 'archived'

Pitfalls:

Paginated results require cursor-based pagination for large catalogs
Product variants are nested within the product object
2. Manage Orders

When to use: User wants to list, search, or inspect orders

Tool sequence:

SHOPIFY_GET_ORDERS_WITH_FILTERS - List orders with filters [Required]
SHOPIFY_GET_ORDER - Get single order details [Optional]
SHOPIFY_GET_FULFILLMENT - Get fulfillment details [Optional]
SHOPIFY_GET_FULFILLMENT_EVENTS - Track fulfillment events [Optional]

Key parameters:

status: Order status filter ('any', 'open', 'closed', 'cancelled')
financial_status: Payment status filter
fulfillment_status: Fulfillment status filter
order_id: Order ID for single retrieval
created_at_min/created_at_max: Date range filters

Pitfalls:

Order IDs are numeric; use string format for API calls
Default order listing may not include all statuses; specify 'any' for all
3. Manage Customers

When to use: User wants to list or search customers

Tool sequence:

SHOPIFY_GET_ALL_CUSTOMERS - List all customers [Required]

Key parameters:

limit: Number of customers per page
since_id: Pagination cursor

Pitfalls:

Customer data includes order count and total spent
Large customer lists require pagination
4. Manage Collections

When to use: User wants to manage product collections

Tool sequence:

SHOPIFY_GET_SMART_COLLECTIONS - List smart collections [Optional]
SHOPIFY_GET_SMART_COLLECTION_BY_ID - Get collection details [Optional]
SHOPIFY_CREATE_SMART_COLLECTIONS - Create a smart collection [Optional]
SHOPIFY_ADD_PRODUCT_TO_COLLECTION - Add product to collection [Optional]
SHOPIFY_GET_PRODUCTS_IN_COLLECTION - List products in collection [Optional]

Key parameters:

collection_id: Collection ID
product_id: Product ID for adding to collection
rules: Smart collection rules for automatic inclusion

Pitfalls:

Smart collections auto-populate based on rules; manual collections use custom collections API
Collection count endpoints provide approximate counts
5. Manage Inventory

When to use: User wants to check or manage inventory levels

Tool sequence:

SHOPIFY_GET_INVENTORY_LEVELS / SHOPIFY_RETRIEVES_A_LIST_OF_INVENTORY_LEVELS - Check stock [Required]
SHOPIFY_LIST_LOCATION - List store locations [Optional]

Key parameters:

inventory_item_ids: Inventory item IDs to check
location_ids: Location IDs to filter by

Pitfalls:

Inventory is tracked per variant per location
Location IDs are required for multi-location stores
Common Patterns
Pagination
Use limit and page_info cursor for paginated results
Check response for next link header
Continue until no more pages available
GraphQL Queries

For advanced operations:

1. Call SHOPIFY_GRAPH_QL_QUERY with custom query
2. Parse response from data object

Known Pitfalls

API Versioning:

Shopify REST API has versioned endpoints
Some features require specific API versions

Rate Limits:

REST API: 2 requests/second for standard plans
GraphQL: 1000 cost points per second
Quick Reference
Task	Tool Slug	Key Params
List products	SHOPIFY_GET_PRODUCTS	(filters)
Get product	SHOPIFY_GET_PRODUCT	product_id
Products paginated	SHOPIFY_GET_PRODUCTS_PAGINATED	limit, page_info
Bulk create	SHOPIFY_BULK_CREATE_PRODUCTS	products
Product count	SHOPIFY_GET_PRODUCTS_COUNT	(none)
List orders	SHOPIFY_GET_ORDERS_WITH_FILTERS	status, financial_status
Get order	SHOPIFY_GET_ORDER	order_id
List customers	SHOPIFY_GET_ALL_CUSTOMERS	limit
Shop details	SHOPIFY_GET_SHOP_DETAILS	(none)
Validate access	SHOPIFY_VALIDATE_ACCESS	(none)
Smart collections	SHOPIFY_GET_SMART_COLLECTIONS	(none)
Products in collection	SHOPIFY_GET_PRODUCTS_IN_COLLECTION	collection_id
Inventory levels	SHOPIFY_GET_INVENTORY_LEVELS	inventory_item_ids
Locations	SHOPIFY_LIST_LOCATION	(none)
Fulfillment	SHOPIFY_GET_FULFILLMENT	order_id, fulfillment_id
GraphQL	SHOPIFY_GRAPH_QL_QUERY	query
Bulk query	SHOPIFY_BULK_QUERY_OPERATION	query
Weekly Installs
26
Repository
aaaaqwq/claude-…e-skills
GitHub Stars
53
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
---
title: search-for-service
url: https://skills.sh/coinbase/agentic-wallet-skills/search-for-service
---

# search-for-service

skills/coinbase/agentic-wallet-skills/search-for-service
search-for-service
Installation
$ npx skills add https://github.com/coinbase/agentic-wallet-skills --skill search-for-service
Summary

Search and discover paid API services available on the x402 bazaar marketplace.

Query the marketplace using BM25 relevance search, list all available resources, or inspect specific endpoints to see pricing and payment requirements without paying
Supports filtering by network (base, base-sepolia) and output formats (human-readable or JSON)
Results are cached locally and auto-refresh every 12 hours; no authentication required for any search or discovery operation
Use as a fallback when no other skill matches, or to explore available external services for accomplishing tasks
SKILL.md
Searching the x402 Bazaar

Use the npx awal@2.8.2 x402 commands to discover and inspect paid API endpoints available on the x402 bazaar marketplace. No authentication or balance is required for searching.

Commands
Search the Bazaar

Find paid services by keyword using CDP's vector search:

npx awal@2.8.2 x402 bazaar search <query> [-k <n>] [--network <network>] [--scheme <scheme>] [--max-price <price>] [--json]

Option	Description
-k, --top <n>	Number of results, 1–20 (default: 20)
--network <name>	Filter by chain (base, base-sepolia, polygon, solana, solana-devnet)
--scheme <scheme>	Filter by payment scheme: exact or upto
--max-price <price>	Maximum price in USD (e.g. 0.01)
--asset <address>	Filter by payment asset address
--pay-to <address>	Filter by recipient wallet address
--extensions <type>	Filter by extension type (e.g. outputSchema, bazaar)
--json	Output as JSON
List Bazaar Resources

Browse all available resources:

npx awal@2.8.2 x402 bazaar list [--network <network>] [--full] [--refresh] [--json]

Option	Description
--network <name>	Filter by chain (base, base-sepolia, polygon, solana, solana-devnet)
--full	Show complete details including schemas
--refresh	Re-fetch resource index from CDP API
--json	Output as JSON
Discover Payment Requirements

Inspect an endpoint's x402 payment requirements without paying:

npx awal@2.8.2 x402 details <url> [--json]


Auto-detects the correct HTTP method (GET, POST, PUT, DELETE, PATCH) by trying each until it gets a 402 response, then displays price, accepted payment schemes, network, and input/output schemas.

Examples
# Search for weather-related paid APIs
npx awal@2.8.2 x402 bazaar search "weather"

# Search with more results
npx awal@2.8.2 x402 bazaar search "sentiment analysis" -k 10

# Browse all bazaar resources with full details
npx awal@2.8.2 x402 bazaar list --full

# Check what an endpoint costs
npx awal@2.8.2 x402 details https://example.com/api/weather

Prerequisites
No authentication needed for search, list, or details commands
Next Steps

Once you've found a service you want to use, use the pay-for-service skill to make a paid request to the endpoint.

Error Handling
"CDP API returned 429" - Rate limited; cached data will be used if available
"No X402 payment requirements found" - URL may not be an x402 endpoint
Weekly Installs
2.2K
Repository
coinbase/agenti…t-skills
GitHub Stars
102
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
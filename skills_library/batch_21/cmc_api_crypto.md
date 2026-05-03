---
title: cmc-api-crypto
url: https://skills.sh/coinmarketcap-official/skills-for-ai-agents-by-coinmarketcap/cmc-api-crypto
---

# cmc-api-crypto

skills/coinmarketcap-official/skills-for-ai-agents-by-coinmarketcap/cmc-api-crypto
cmc-api-crypto
Installation
$ npx skills add https://github.com/coinmarketcap-official/skills-for-ai-agents-by-coinmarketcap --skill cmc-api-crypto
SKILL.md
CoinMarketCap Cryptocurrency API

This skill covers the CoinMarketCap Cryptocurrency API endpoints for retrieving price data, market listings, historical quotes, trending coins, and token metadata.

Authentication

All requests require an API key in the header.

curl -X GET "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest" \
  -H "X-CMC_PRO_API_KEY: your-api-key"


Get your API key at: https://pro.coinmarketcap.com/login

Base URL
https://pro-api.coinmarketcap.com

Common Use Cases

See use-cases.md for goal-based guidance on which endpoint to use:

Get current price of a token
Find a token's CMC ID from symbol or name
Get a token by contract address
Get top 100 coins by market cap
Find coins in a price range
Get historical price at a specific date
Build a price chart (OHLCV data)
Find where a coin trades
Get all-time high and distance from ATH
Find today's biggest gainers
Discover newly listed coins
Get all tokens in a category (e.g., DeFi)
API Overview
Endpoint	Description	Reference
GET /v1/cryptocurrency/categories	List all categories with market metrics	categories.md
GET /v1/cryptocurrency/category	Single category details	categories.md
GET /v1/cryptocurrency/listings/historical	Historical listings snapshot	listings.md
GET /v1/cryptocurrency/listings/latest	Current listings with market data	listings.md
GET /v1/cryptocurrency/listings/new	Newly added cryptocurrencies	listings.md
GET /v1/cryptocurrency/map	Map names/symbols to CMC IDs	map.md
GET /v1/cryptocurrency/trending/gainers-losers	Top gainers and losers	trending.md
GET /v1/cryptocurrency/trending/latest	Currently trending coins	trending.md
GET /v1/cryptocurrency/trending/most-visited	Most visited on CMC	trending.md
GET /v2/cryptocurrency/info	Static metadata (logo, description, URLs)	info.md
GET /v2/cryptocurrency/market-pairs/latest	Trading pairs for a coin	market-pairs.md
GET /v2/cryptocurrency/ohlcv/historical	Historical OHLCV candles	ohlcv.md
GET /v2/cryptocurrency/ohlcv/latest	Latest OHLCV data	ohlcv.md
GET /v2/cryptocurrency/price-performance-stats/latest	Price performance stats	price-performance.md
GET /v2/cryptocurrency/quotes/latest	Latest price quotes	quotes.md
GET /v3/cryptocurrency/quotes/historical	Historical price quotes	quotes.md
Common Workflows
Get Token Price by Symbol
First, map the symbol to a CMC ID using /v1/cryptocurrency/map
Then fetch the price using /v2/cryptocurrency/quotes/latest
# Step 1: Get CMC ID for ETH
curl -X GET "https://pro-api.coinmarketcap.com/v1/cryptocurrency/map?symbol=ETH" \
  -H "X-CMC_PRO_API_KEY: your-api-key"

# Step 2: Get price quote (using id=1027 for ETH)
curl -X GET "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest?id=1027" \
  -H "X-CMC_PRO_API_KEY: your-api-key"

Get Top 100 Coins by Market Cap
curl -X GET "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?limit=100&sort=market_cap" \
  -H "X-CMC_PRO_API_KEY: your-api-key"

Get Historical Price Data
curl -X GET "https://pro-api.coinmarketcap.com/v3/cryptocurrency/quotes/historical?id=1&time_start=2024-01-01&time_end=2024-01-31&interval=daily" \
  -H "X-CMC_PRO_API_KEY: your-api-key"

Get Token Metadata
curl -X GET "https://pro-api.coinmarketcap.com/v2/cryptocurrency/info?id=1,1027" \
  -H "X-CMC_PRO_API_KEY: your-api-key"

Error Handling
HTTP Status Codes
Code	Meaning
200	Success
400	Bad request (invalid parameters)
401	Unauthorized (invalid API key)
403	Forbidden (endpoint not available on your plan)
429	Rate limit exceeded
500	Server error
Rate Limits

Rate limits depend on your subscription plan. The response headers include:

X-CMC_PRO_API_KEY_CREDITS_USED - Credits used this call
X-CMC_PRO_API_KEY_CREDITS_LEFT - Credits remaining
Common Errors

Invalid ID: Ensure you use valid CMC IDs from the /map endpoint. Symbol lookups may return multiple matches.

Missing Required Parameter: Some endpoints require at least one identifier (id, slug, or symbol).

Plan Restrictions: Historical endpoints and some features require paid plans. Check your plan limits.

Error Response Format
{
  "status": {
    "timestamp": "2024-01-15T12:00:00.000Z",
    "error_code": 400,
    "error_message": "Invalid value for 'id'",
    "credit_count": 0
  }
}

Response Format

All responses follow this structure:

{
  "status": {
    "timestamp": "2024-01-15T12:00:00.000Z",
    "error_code": 0,
    "error_message": null,
    "credit_count": 1
  },
  "data": { ... }
}

Reference Files

See the references/ directory for complete parameter and response documentation for each endpoint.

Weekly Installs
78
Repository
coinmarketcap-o…arketcap
GitHub Stars
45
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail
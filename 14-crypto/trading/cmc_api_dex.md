---
title: cmc-api-dex
url: https://skills.sh/coinmarketcap-official/skills-for-ai-agents-by-coinmarketcap/cmc-api-dex
---

# cmc-api-dex

skills/coinmarketcap-official/skills-for-ai-agents-by-coinmarketcap/cmc-api-dex
cmc-api-dex
Installation
$ npx skills add https://github.com/coinmarketcap-official/skills-for-ai-agents-by-coinmarketcap --skill cmc-api-dex
SKILL.md
CoinMarketCap DEX API

This skill covers CoinMarketCap's DEX (Decentralized Exchange) APIs for on-chain token data. Unlike CEX endpoints, these APIs fetch data directly from blockchain DEXs like Uniswap, PancakeSwap, and Raydium.

Authentication

All requests require an API key in the header:

curl -X GET "https://pro-api.coinmarketcap.com/v1/dex/platform/list" \
  -H "X-CMC_PRO_API_KEY: your-api-key"


Get your API key at: https://pro.coinmarketcap.com/login

Base URL
https://pro-api.coinmarketcap.com

POST vs GET Endpoints

Many DEX endpoints use POST for complex queries with body parameters. Always check the method:

GET endpoints pass parameters as query strings
POST endpoints pass parameters in JSON body with Content-Type: application/json
Common Use Cases

See use-cases.md for goal-based guidance on which endpoint to use:

Get DEX token price by contract address
Find a token's contract address by name
Get prices for multiple tokens at once
Check token security before trading
Find liquidity pools for a token
Find trending DEX tokens
Find today's biggest DEX gainers
Find newly launched tokens
Detect potential rug pulls (liquidity removal)
Get recent trades for a token
Get supported networks and DEXs
Get meme coins
API Overview
Endpoint	Method	Description	Reference
/v1/dex/token	GET	Token details by platform/address	tokens.md
/v1/dex/token/price	GET	Latest DEX price for a token	tokens.md
/v1/dex/token/price/batch	POST	Batch token prices	tokens.md
/v1/dex/token/pools	GET	Liquidity pools for a token	tokens.md
/v1/dex/token-liquidity/query	GET	Token liquidity over time	tokens.md
/v1/dex/tokens/batch-query	POST	Batch token metadata	tokens.md
/v1/dex/tokens/transactions	GET	Recent DEX transactions	tokens.md
/v1/dex/tokens/trending/list	POST	Trending DEX tokens	tokens.md
/v4/dex/pairs/quotes/latest	GET	Latest DEX pair quotes	pairs.md
/v4/dex/spot-pairs/latest	GET	DEX spot pairs listing	pairs.md
/v1/dex/platform/list	GET	List supported DEX platforms	platforms.md
/v1/dex/platform/detail	GET	Platform details	platforms.md
/v1/dex/search	GET	Search DEX tokens/pairs	platforms.md
/v1/dex/gainer-loser/list	POST	Top DEX gainers/losers	discovery.md
/v1/dex/liquidity-change/list	GET	Tokens with liquidity changes	discovery.md
/v1/dex/meme/list	POST	Meme tokens on DEX	discovery.md
/v1/dex/new/list	POST	Newly discovered DEX tokens	discovery.md
/v1/dex/security/detail	GET	Token security/risk signals	security.md
Common Workflows
Get DEX Token Information
Search for token: /v1/dex/search?keyword=PEPE
Get token details: /v1/dex/token?network_slug=ethereum&contract_address=0x...
Check security risks: /v1/dex/security/detail?network_slug=ethereum&contract_address=0x...
Analyze Token Liquidity
Get token pools: /v1/dex/token/pools?network_slug=ethereum&contract_address=0x...
Get liquidity history: /v1/dex/token-liquidity/query?network_slug=ethereum&contract_address=0x...
Find Trending Tokens
Get trending tokens: POST /v1/dex/tokens/trending/list with filters
Get gainers/losers: POST /v1/dex/gainer-loser/list
Find new tokens: POST /v1/dex/new/list
Monitor DEX Activity
Get recent transactions: /v1/dex/tokens/transactions?network_slug=ethereum&contract_address=0x...
Get pair quotes: /v4/dex/pairs/quotes/latest?network_slug=ethereum&contract_address=0x...
Key Parameters

Most DEX endpoints require:

network_slug or platform_crypto_id: Identifies the blockchain (ethereum, solana, bsc)
contract_address: The token's on-chain contract address

Use /v1/dex/platform/list to get valid network slugs and platform IDs.

Error Handling
Code	Meaning
400	Bad request (invalid parameters)
401	Unauthorized (invalid or missing API key)
403	Forbidden (endpoint not in your plan)
429	Rate limit exceeded
500	Server error

Example error response:

{
  "status": {
    "error_code": 400,
    "error_message": "Invalid value for 'contract_address'"
  }
}

Rate Limits

Rate limits depend on your API plan. Check response headers:

X-CMC_PRO_API_KEY_CREDITS_REMAINING: Credits left
X-CMC_PRO_API_KEY_CREDITS_RESET: Reset timestamp
Response Format

All responses follow this structure:

{
  "status": {
    "timestamp": "2024-01-15T12:00:00.000Z",
    "error_code": 0,
    "error_message": null
  },
  "data": { ... }
}

Weekly Installs
57
Repository
coinmarketcap-o…arketcap
GitHub Stars
45
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
---
title: cmc-api-market
url: https://skills.sh/coinmarketcap-official/skills-for-ai-agents-by-coinmarketcap/cmc-api-market
---

# cmc-api-market

skills/coinmarketcap-official/skills-for-ai-agents-by-coinmarketcap/cmc-api-market
cmc-api-market
Installation
$ npx skills add https://github.com/coinmarketcap-official/skills-for-ai-agents-by-coinmarketcap --skill cmc-api-market
SKILL.md
CoinMarketCap Market API Skill

This skill covers market-wide cryptocurrency data including global metrics, sentiment indicators, market indices, community activity, news content, charting data, and utility endpoints.

Authentication

All requests require the X-CMC_PRO_API_KEY header.

curl -X GET "https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest" \
  -H "X-CMC_PRO_API_KEY: your-api-key"


Get your API key at: https://pro.coinmarketcap.com/login

Base URL
https://pro-api.coinmarketcap.com

Common Use Cases

See use-cases.md for goal-based guidance on which endpoint to use:

Get current market sentiment (Fear & Greed)
Get total crypto market cap
Get BTC dominance
Track market cap history
Track Fear & Greed history
Get CMC100 index performance
Compare CMC100 vs CMC20
Get OHLCV candlestick data for charts
Get simple price time series
Get community trending tokens
Get trending discussion topics
Get latest crypto news
Convert currency amounts
Check API usage and limits
Get fiat currency IDs
API Overview
Global Metrics
Endpoint	Description	Reference
GET /v1/global-metrics/quotes/historical	Historical global market metrics	global-metrics.md
GET /v1/global-metrics/quotes/latest	Latest total market cap, BTC dominance	global-metrics.md
Fear and Greed Index
Endpoint	Description	Reference
GET /v3/fear-and-greed/historical	Historical fear/greed values	fear-greed.md
GET /v3/fear-and-greed/latest	Current market sentiment score	fear-greed.md
Market Indices
Endpoint	Description	Reference
GET /v3/index/cmc100-historical	CMC100 index history	indices.md
GET /v3/index/cmc100-latest	CMC100 current value	indices.md
GET /v3/index/cmc20-historical	CMC20 index history	indices.md
GET /v3/index/cmc20-latest	CMC20 current value	indices.md
Community
Endpoint	Description	Reference
GET /v1/community/trending/token	Trending tokens by community activity	community.md
GET /v1/community/trending/topic	Trending discussion topics	community.md
Content
Endpoint	Description	Reference
GET /v1/content/latest	Latest news and Alexandria articles	content.md
GET /v1/content/posts/comments	Comments on a specific post	content.md
GET /v1/content/posts/latest	Latest community posts	content.md
GET /v1/content/posts/top	Top ranked community posts	content.md
K-Line Charts
Endpoint	Description	Reference
GET /v1/k-line/candles	OHLCV candlestick data	kline.md
GET /v1/k-line/points	Time series price/market cap points	kline.md
Tools
Endpoint	Description	Reference
GET /v1/fiat/map	Map fiat currencies to CMC IDs	tools.md
GET /v1/key/info	API key usage and plan details	tools.md
GET /v2/tools/price-conversion	Convert between currencies	tools.md
Common Workflows
Get Market Sentiment Overview
Fetch fear/greed index: /v3/fear-and-greed/latest
Get global metrics: /v1/global-metrics/quotes/latest
Combine for sentiment analysis with market cap context
Track Market Index Performance
Get current CMC100 value: /v3/index/cmc100-latest
Fetch historical data: /v3/index/cmc100-historical
Compare performance over time
Monitor Community Activity
Check trending tokens: /v1/community/trending/token
Review trending topics: /v1/community/trending/topic
Read latest posts: /v1/content/posts/top
Build Price Charts
Fetch OHLCV candles: /v1/k-line/candles
Use interval parameter for timeframe (1h, 4h, 1d)
Plot candlestick chart with returned data
Currency Conversion
Get fiat currency IDs: /v1/fiat/map
Convert amounts: /v2/tools/price-conversion
Error Handling
Status Code	Meaning	Action
400	Bad Request	Check parameter values and format
401	Unauthorized	Verify API key is valid
403	Forbidden	Endpoint not available on your plan
429	Rate Limited	Wait and retry with backoff
500	Server Error	Retry after delay
Error Response Format
{
  "status": {
    "error_code": 400,
    "error_message": "Invalid value for 'id'"
  }
}

Rate Limit Headers

Check these response headers to monitor usage:

X-CMC_PRO_API_KEY_CREDITS_USED - Credits consumed
X-CMC_PRO_API_KEY_CREDITS_REMAINING - Credits left
X-CMC_PRO_API_KEY_RATE_LIMIT - Requests per minute limit
Response Format

All endpoints return JSON with this structure:

{
  "status": {
    "timestamp": "2024-01-15T10:30:00.000Z",
    "error_code": 0,
    "error_message": null,
    "credit_count": 1
  },
  "data": { }
}

Tips
Use the /v1/key/info endpoint to check your plan limits before heavy usage
Cache global metrics data as it updates every few minutes
Fear/greed index updates daily, no need for frequent polling
K-line data supports multiple intervals for different chart timeframes
Community trending data refreshes periodically throughout the day
Weekly Installs
60
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
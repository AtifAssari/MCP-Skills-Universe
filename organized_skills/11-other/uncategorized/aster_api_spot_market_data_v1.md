---
rating: ⭐⭐
title: aster-api-spot-market-data-v1
url: https://skills.sh/asterdex/aster-skills-hub/aster-api-spot-market-data-v1
---

# aster-api-spot-market-data-v1

skills/asterdex/aster-skills-hub/aster-api-spot-market-data-v1
aster-api-spot-market-data-v1
Installation
$ npx skills add https://github.com/asterdex/aster-skills-hub --skill aster-api-spot-market-data-v1
SKILL.md
Aster Spot API Market Data (v1)

Base: https://sapi.asterdex.com. All GET; query string params; no signature except historicalTrades (API key).

Endpoints
Endpoint	Weight	Key parameters
GET /api/v1/ping	1	None
GET /api/v1/time	1	None → { "serverTime": ms }
GET /api/v1/exchangeInfo	1	None → symbols, filters, rateLimits, assets
GET /api/v1/depth	2–20	symbol (required), limit (5,10,20,50,100,500,1000; default 100)
GET /api/v1/trades	1	symbol, limit (default 500, max 1000)
GET /api/v1/historicalTrades	20	symbol, limit, fromId. MARKET_DATA: requires API key
GET /api/v1/aggTrades	20	symbol, fromId, startTime, endTime, limit (max 1000); startTime–endTime < 1h if both
GET /api/v1/klines	1–10	symbol, interval, startTime, endTime, limit (default 500, max 1500)
GET /api/v1/ticker/24hr	1 or 40	symbol (optional; no symbol = 40 weight)
GET /api/v1/ticker/price	1 or 2	symbol (optional)
GET /api/v1/ticker/bookTicker	1 or 2	symbol (optional)
GET /api/v1/commissionRate	20	symbol (required). Signed.

Depth weight by limit: 5, 10, 20, 50 → 2; 100 → 5; 500 → 10; 1000 → 20.

Intervals (klines): 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M.

Conventions: REST symbols uppercase; WS lowercase; timestamps ms.

Payload shapes: reference.md.

Weekly Installs
15
Repository
asterdex/aster-…ills-hub
GitHub Stars
68
First Seen
Mar 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
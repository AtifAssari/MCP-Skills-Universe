---
rating: ⭐⭐
title: aster-api-websocket-v1
url: https://skills.sh/asterdex/aster-skills-hub/aster-api-websocket-v1
---

# aster-api-websocket-v1

skills/asterdex/aster-skills-hub/aster-api-websocket-v1
aster-api-websocket-v1
Installation
$ npx skills add https://github.com/asterdex/aster-skills-hub --skill aster-api-websocket-v1
SKILL.md
Aster API WebSocket (v1)

Base: wss://fstream.asterdex.com. Raw: /ws/<streamName>. Combined: /stream?streams=name1/name2/... → {"stream":"<name>","data":<payload>}. Stream names lowercase (e.g. btcusdt).

Limits: Connection 24h; ping every 5 min → pong within 15 min; 10 msg/s; max 200 streams.

Market: subscribe / unsubscribe

JSON: Subscribe {"method":"SUBSCRIBE","params":["btcusdt@aggTrade","btcusdt@depth"],"id":1} → {"result":null,"id":1}. Unsubscribe: UNSUBSCRIBE + params. List: LIST_SUBSCRIPTIONS. id = unsigned int.

Stream names (market)
Stream	Description
<symbol>@aggTrade	Aggregate trades (100ms)
<symbol>@depth	Diff. book depth (250/500/100ms: @depth@500ms, @depth@100ms)
<symbol>@depth5, @depth10, @depth20	Partial book depth
<symbol>@kline_<interval>	Kline (e.g. 1m, 1h); interval as in REST
<symbol>@markPrice, <symbol>@markPrice@1s	Mark price (3s or 1s)
!markPrice@arr, !markPrice@arr@1s	All symbols mark price
<symbol>@miniTicker	24h mini ticker (500ms)
!miniTicker@arr	All mini tickers (1000ms)
<symbol>@ticker	24h ticker (500ms)
!ticker@arr	All tickers (1000ms)
<symbol>@bookTicker	Best bid/ask (real-time)
!bookTicker	All book tickers
<symbol>@forceOrder	Liquidation snapshot (1000ms)
!forceOrder@arr	All liquidations
User data stream (signed)
Start: POST /fapi/v1/listenKey → { "listenKey": "..." } (existing key extended 60 min).
Connect: wss://fstream.asterdex.com/ws/.
Keepalive: PUT /fapi/v1/listenKey <60 min (e.g. 30 min).
Close: DELETE /fapi/v1/listenKey.

Events not guaranteed in order; use E for ordering. Events: ACCOUNT_UPDATE, ORDER_TRADE_UPDATE, ACCOUNT_CONFIG_UPDATE, MARGIN_CALL, listenKeyExpired.

Order book sync (depth)
Connect to btcusdt@depth; buffer events.
Snapshot: GET /fapi/v1/depth?symbol=BTCUSDT&limit=1000.
Drop events with u < lastUpdateId; first valid: U ≤ lastUpdateId and u ≥ lastUpdateId.
Each event: pu = previous u; else re-sync from step 2. Qty absolute; 0 = remove level.

Payload shapes: reference.md.

Weekly Installs
22
Repository
asterdex/aster-…ills-hub
GitHub Stars
68
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
---
title: aster-api-spot-trading-v1
url: https://skills.sh/asterdex/aster-skills-hub/aster-api-spot-trading-v1
---

# aster-api-spot-trading-v1

skills/asterdex/aster-skills-hub/aster-api-spot-trading-v1
aster-api-spot-trading-v1
Installation
$ npx skills add https://github.com/asterdex/aster-skills-hub --skill aster-api-spot-trading-v1
SKILL.md
Aster Spot API Trading (v1)

Base: https://sapi.asterdex.com. Signed (TRADE/USER_DATA). POST/DELETE: body application/x-www-form-urlencoded.

New order

POST /api/v1/order (W: 1)

Parameter	Req	Notes
symbol, side, type	Y	side: BUY/SELL; type → see below
timeInForce	N	GTC, IOC, FOK, GTX
quantity, quoteOrderQty	N	MARKET BUY: quantity or quoteOrderQty; MARKET SELL: quantity
price, stopPrice	N	stopPrice for STOP*, TAKE_PROFIT*
newClientOrderId	N	Unique client order ID
newOrderRespType	N	ACK, RESULT, FULL

Type-specific required: LIMIT → timeInForce, quantity, price. MARKET → quantity or quoteOrderQty (BUY). STOP/TAKE_PROFIT → quantity, price, stopPrice. STOP_MARKET/TAKE_PROFIT_MARKET → quantity, stopPrice.

Order types: LIMIT, MARKET, STOP, TAKE_PROFIT, STOP_MARKET, TAKE_PROFIT_MARKET.

Cancel / Query
DELETE /api/v1/order (W: 1): symbol + orderId or origClientOrderId.
GET /api/v1/order (W: 1): symbol + orderId or origClientOrderId.
GET /api/v1/openOrders (W: 1 or 40): symbol optional; no symbol = all (40).
DELETE /api/v1/allOpenOrders (W: 1): symbol (required); optional orderIdList or origClientOrderIdList for batch cancel.
GET /api/v1/allOrders (W: 5): symbol req.; orderId, startTime, endTime, limit (500 default, 1000 max). Max range 7 days.

No POST batchOrders (create); batch cancel via allOpenOrders with list params.

Payload shapes: reference.md.

Weekly Installs
14
Repository
asterdex/aster-…ills-hub
GitHub Stars
68
First Seen
Mar 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketFail
SnykWarn
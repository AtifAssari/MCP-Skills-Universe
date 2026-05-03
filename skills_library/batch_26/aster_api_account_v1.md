---
title: aster-api-account-v1
url: https://skills.sh/asterdex/aster-skills-hub/aster-api-account-v1
---

# aster-api-account-v1

skills/asterdex/aster-skills-hub/aster-api-account-v1
aster-api-account-v1
Installation
$ npx skills add https://github.com/asterdex/aster-skills-hub --skill aster-api-account-v1
SKILL.md
Aster API Account (v1)

Base: https://fapi.asterdex.com. All endpoints signed.

Balance and account
GET /fapi/v2/balance (Weight: 5). No params beyond auth. Returns: see reference.
GET /fapi/v4/account (Weight: 5). Returns: see reference.
Positions
GET /fapi/v2/positionRisk (Weight: 5). Params: symbol (optional). Returns per-symbol/positionSide; one-way = BOTH, hedge = LONG/SHORT. Fields: see reference.
Leverage and margin type
POST /fapi/v1/leverage (Weight: 1): symbol, leverage (1–125). Returns leverage, maxNotionalValue, symbol.
POST /fapi/v1/marginType (Weight: 1): symbol, marginType (ISOLATED | CROSSED). Fails if open orders or position exist when changing (see error codes).
Isolated position margin
POST /fapi/v1/positionMargin (Weight: 1): symbol, positionSide (optional; BOTH or LONG/SHORT in hedge), amount, type (1 = add, 2 = reduce). Only for isolated margin.
GET /fapi/v1/positionMargin/history (Weight: 1): symbol, type (optional), startTime, endTime, limit (default 500).
Transfer (futures ↔ spot)
POST /fapi/v1/asset/wallet/transfer (Weight: 5): amount, asset, clientTranId (required, unique e.g. within 7 days), kindType (FUTURE_SPOT | SPOT_FUTURE), timestamp. Returns tranId, status.
Position and account mode
GET /fapi/v1/positionSide/dual (Weight: 30): returns dualSidePosition (true = hedge, false = one-way).
POST /fapi/v1/positionSide/dual (Weight: 1): dualSidePosition "true"|"false". Affects every symbol.
GET /fapi/v1/multiAssetsMargin (Weight: 30): returns multiAssetsMargin.
POST /fapi/v1/multiAssetsMargin (Weight: 1): multiAssetsMargin "true"|"false". Affects every symbol.
Other
GET /fapi/v1/income (Weight: 30): symbol, incomeType (optional), startTime, endTime, limit (default 100, max 1000). Default 7-day window if no time range. incomeType values: see reference.
GET /fapi/v1/leverageBracket (Weight: 1): symbol optional; notional brackets per symbol.
GET /fapi/v1/adlQuantile (Weight: 5): symbol optional; ADL queue (0–4).
GET /fapi/v1/forceOrders (Weight: 20/50): symbol, autoCloseType (LIQUIDATION | ADL), startTime, endTime, limit (default 50, max 100).
GET /fapi/v1/commissionRate (Weight: 20): symbol required; makerCommissionRate, takerCommissionRate.
GET /fapi/v1/remainingOpenableNotionalValue (Weight: 20): symbol, leverage required; returns remainingOpenableNotionalValue (USDT).

Payload shapes: reference.md.

Weekly Installs
17
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
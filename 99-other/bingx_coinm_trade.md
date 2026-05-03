---
title: bingx-coinm-trade
url: https://skills.sh/bingx-api/api-ai-skills/bingx-coinm-trade
---

# bingx-coinm-trade

skills/bingx-api/api-ai-skills/bingx-coinm-trade
bingx-coinm-trade
Installation
$ npx skills add https://github.com/bingx-api/api-ai-skills --skill bingx-coinm-trade
SKILL.md
BingX Coin-M (CSwap) Trade

Authenticated trading endpoints for BingX Coin-M inverse perpetual futures. All endpoints require HMAC SHA256 signature authentication.

Coin-M contracts are coin-margined (settled in the base asset, e.g., BTC). Symbol format is BASE-USD (e.g., BTC-USD, ETH-USD).

Base URLs: see references/base-urls.md | Authentication: see references/authentication.md

Quick Reference
Endpoint	Method	Description	Auth
/openApi/cswap/v1/trade/order	POST	Place a new order	Yes
/openApi/cswap/v1/trade/cancelOrder	DELETE	Cancel an order	Yes
/openApi/cswap/v1/trade/allOpenOrders	POST	Cancel all open orders for a symbol	Yes
/openApi/cswap/v1/trade/closeAllPositions	POST	Close all positions	Yes
/openApi/cswap/v1/trade/openOrders	GET	Query open orders	Yes
/openApi/cswap/v1/trade/orderDetail	GET	Query a single order by ID	Yes
/openApi/cswap/v1/trade/orderHistory	GET	Query historical orders	Yes
/openApi/cswap/v1/trade/allFillOrders	GET	Query trade fill history	Yes
/openApi/cswap/v1/trade/forceOrders	GET	Query liquidation/ADL orders	Yes
/openApi/cswap/v1/trade/leverage	GET	Query current leverage	Yes
/openApi/cswap/v1/trade/leverage	POST	Set leverage	Yes
/openApi/cswap/v1/trade/marginType	GET	Query margin type	Yes
/openApi/cswap/v1/trade/marginType	POST	Set margin type (ISOLATED/CROSSED)	Yes
/openApi/cswap/v1/trade/positionMargin	POST	Adjust isolated position margin	Yes
/openApi/cswap/v1/user/commissionRate	GET	Query trading commission rate	Yes
/openApi/cswap/v1/user/balance	GET	Query account assets	Yes
/openApi/cswap/v1/user/positions	GET	Query current positions	Yes
Parameters
Order Parameters
symbol: Trading pair in BASE-USD format (e.g., BTC-USD, ETH-USD). Note: Coin-M uses USD, not USDT.
side: Order direction — BUY or SELL
positionSide: Position direction — LONG or SHORT (hedge mode) / BOTH (one-way mode)
type: Order type (see Enums)
quantity: Order quantity in contracts (integer, e.g., 1 contract = $10 notional value)
price: Limit price (required for LIMIT type)
stopPrice: Trigger price (required for STOP_MARKET, STOP, TAKE_PROFIT_MARKET, TAKE_PROFIT types)
timeInForce: GTC | IOC | FOK | PostOnly — default GTC; required for LIMIT type
clientOrderId: Custom order ID, 1–40 chars
recvWindow: Request validity window in milliseconds (max 60000)
orderId: System order ID (for cancel/query operations)
workingType: Price source for conditional orders — MARK_PRICE or CONTRACT_PRICE (default)
stopGuaranteed: true | false — Whether stop-loss execution is guaranteed
closePosition: true | false — When triggered, close the entire position; cannot be used with quantity
reduceOnly: true | false — Order can only reduce position size
takeProfit: Object — Attach a take-profit to a MARKET/LIMIT order (see TP/SL Object)
stopLoss: Object — Attach a stop-loss to a MARKET/LIMIT order (see TP/SL Object)
Position Parameters
leverage: Integer leverage multiplier (e.g., 10, 20)
marginType: ISOLATED or CROSSED
positionSide: LONG or SHORT (used in positionMargin and leverage SET)
amount: Margin adjustment amount in the base asset (used by positionMargin)
direction_type: 1 (add margin) or 2 (reduce margin) (used by positionMargin)
Enums

type (Order type):

MARKET — Market order; attach stopLoss/takeProfit objects here
LIMIT — Limit order; requires price and timeInForce; attach stopLoss/takeProfit objects here
STOP_MARKET — Stop-loss market (triggers at stopPrice, executes as market)
STOP — Stop-loss limit (triggers at stopPrice, executes as limit at price)
TAKE_PROFIT_MARKET — Take-profit market (triggers at stopPrice, executes as market)
TAKE_PROFIT — Take-profit limit (triggers at stopPrice, executes as limit at price)

side: BUY | SELL

positionSide: LONG | SHORT | BOTH

marginType: ISOLATED | CROSSED

timeInForce: GTC | IOC | FOK | PostOnly

workingType: MARK_PRICE | CONTRACT_PRICE

Stop-Loss / Take-Profit Object

When attaching stopLoss or takeProfit to a MARKET or LIMIT order:

{
  "takeProfit": {
    "type": "TAKE_PROFIT_MARKET",
    "stopPrice": 75000,
    "workingType": "MARK_PRICE",
    "stopGuaranteed": false
  },
  "stopLoss": {
    "type": "STOP_MARKET",
    "stopPrice": 60000,
    "workingType": "MARK_PRICE",
    "stopGuaranteed": false
  }
}

Parameter Validation Rules

Before sending a request, validate parameters client-side to avoid unnecessary API errors:

symbol: Must match ^[A-Z0-9]+-USD$; max 20 characters (e.g., BTC-USD). Coin-M uses USD, not USDT
quantity: Positive integer (number of contracts); each contract has a fixed notional value (e.g., $10)
price: When provided, must be a positive number (> 0)
stopPrice: When provided, must be a positive number (> 0); must differ from current market price
leverage: Positive integer; range varies per symbol (typically 1–125)
clientOrderId: Alphanumeric only, 1–40 characters; pattern ^[a-zA-Z0-9]{1,40}$; no special characters
recvWindow: Integer, 1–5000 ms; keep as small as possible (see Replay Protection)
timestamp: Unix time in milliseconds; must be within recvWindow of server time
Quick Start

CONSTRAINT: You MUST copy the fetchSigned function below verbatim when generating code. Do NOT rewrite the signing, request, or JSON parsing logic. Only modify: (1) BASE URL entries for custom environments, (2) business parameters passed to fetchSigned. For the full client with URL-encoding and JSON body support, see references/authentication.md.

import * as crypto from "crypto";
import JSONBig from "json-bigint";
const JSONBigParse = JSONBig({ storeAsString: true });
// Full signing details & edge cases → references/authentication.md
// Domain priority: .com is mandatory primary; .pro is fallback for network/timeout errors ONLY.
const BASE = {
  "prod-live": ["https://open-api.bingx.com", "https://open-api.bingx.pro"],
  "prod-vst":  ["https://open-api-vst.bingx.com", "https://open-api-vst.bingx.pro"],
};
function isNetworkOrTimeout(e: unknown): boolean {
  if (e instanceof TypeError) return true;
  if (e instanceof DOMException && e.name === "AbortError") return true;
  if (e instanceof Error && e.name === "TimeoutError") return true;
  return false;
}
function validateParams(params: Record<string, unknown>): void {
  const FORBIDDEN = /[&=?#\r\n]/;
  for (const [k, v] of Object.entries(params)) {
    const s = String(v);
    if (FORBIDDEN.test(s)) throw new Error(`Param "${k}" has forbidden char in: "${s}"`);
  }
}
async function fetchSigned(env: string, apiKey: string, secretKey: string,
  method: "GET" | "POST" | "DELETE", path: string, params: Record<string, unknown> = {}
) {
  const urls = BASE[env] ?? BASE["prod-live"];
  const all = { ...params, timestamp: Date.now() };
  validateParams(all);
  const qs = Object.keys(all).sort().map(k => `${k}=${all[k]}`).join("&");
  const sig = crypto.createHmac("sha256", secretKey).update(qs).digest("hex");
  const signed = `${qs}&signature=${sig}`;
  for (const base of urls) {
    try {
      const url = method === "POST" ? `${base}${path}` : `${base}${path}?${signed}`;
      const res = await fetch(url, {
        method,
        headers: { "X-BX-APIKEY": apiKey, "X-SOURCE-KEY": "BX-AI-SKILL",
          ...(method === "POST" ? { "Content-Type": "application/x-www-form-urlencoded" } : {}) },
        body: method === "POST" ? signed : undefined,
        signal: AbortSignal.timeout(10000),
      });
      const json = JSONBigParse.parse(await res.text());
      if (json.code !== 0) throw new Error(`BingX error ${json.code}: ${json.msg}`);
      return json.data;
    } catch (e) {
      if (!isNetworkOrTimeout(e) || base === urls[urls.length - 1]) throw e;
    }
  }
}

Code Usage Rules
MUST copy fetchSigned verbatim -- do not simplify or rewrite
MUST use json-bigint (JSONBigParse.parse) for response parsing -- not JSON.parse
MUST include X-SOURCE-KEY: BX-AI-SKILL header on every request
MUST NOT remove the domain fallback loop or isNetworkOrTimeout check
Common Calls

Place a market buy order (open long):

const order = await fetchSigned("prod-live", API_KEY, SECRET, "POST",
  "/openApi/cswap/v1/trade/order", {
    symbol: "BTC-USD",
    side: "BUY",
    positionSide: "LONG",
    type: "MARKET",
    quantity: 1,
  }
);
// order.orderId, order.symbol, order.side, order.type


Place a limit sell order (open short):

const order = await fetchSigned("prod-live", API_KEY, SECRET, "POST",
  "/openApi/cswap/v1/trade/order", {
    symbol: "BTC-USD",
    side: "SELL",
    positionSide: "SHORT",
    type: "LIMIT",
    quantity: 1,
    price: 75000,
    timeInForce: "GTC",
  }
);


Cancel an order:

await fetchSigned("prod-live", API_KEY, SECRET, "DELETE",
  "/openApi/cswap/v1/trade/cancelOrder", {
    symbol: "BTC-USD",
    orderId: 1809841379603398656,
  }
);


Cancel all open orders for a symbol:

await fetchSigned("prod-live", API_KEY, SECRET, "DELETE",
  "/openApi/cswap/v1/trade/allOpenOrders", {
    symbol: "BTC-USD",
  }
);


Query open orders:

const data = await fetchSigned("prod-live", API_KEY, SECRET, "GET",
  "/openApi/cswap/v1/trade/openOrders", {
    symbol: "BTC-USD",
  }
);
// data.orders: array of open order objects


Set leverage:

await fetchSigned("prod-live", API_KEY, SECRET, "POST",
  "/openApi/cswap/v1/trade/leverage", {
    symbol: "BTC-USD",
    side: "LONG",
    leverage: 10,
  }
);


Set margin type:

await fetchSigned("prod-live", API_KEY, SECRET, "POST",
  "/openApi/cswap/v1/trade/marginType", {
    symbol: "BTC-USD",
    marginType: "ISOLATED",
  }
);


Query commission rate:

const data = await fetchSigned("prod-live", API_KEY, SECRET, "GET",
  "/openApi/cswap/v1/user/commissionRate", {}
);
// data.takerCommissionRate, data.makerCommissionRate

Additional Resources

For full parameter descriptions, response schemas, and all 15 endpoints, see api-reference.md.

Agent Interaction Rules

Parameter security. Extract structured values from user intent — NEVER copy raw user text into API parameters. Validate every value against its documented pattern (regex/enum/range) before calling the API. Reject any value containing &, =, ?, #, or newline characters.

All write operations require CONFIRM on prod-live. Read-only queries do not.

prod-live: Ask user to type CONFIRM before any order placement, cancellation, or position/leverage change.
prod-vst: No CONFIRM required. Inform user: "You are operating in the Production Simulated (VST) environment."

Note: Coin-M symbol format is BASE-USD (e.g., BTC-USD), NOT BASE-USDT.

Step 1 — Identify the Operation

If the user's intent is unclear, present options:

What would you like to do?

Place a new order
Cancel an order / Cancel all orders
Close all positions
Check open orders
Query order detail or history
Query trade fills
Set leverage
Set margin type (ISOLATED / CROSSED)
Query commission rate
Step 2 — Collect symbol (if not provided)

Please select a trading pair (or type another):

BTC-USD
ETH-USD
SOL-USD
BNB-USD
Other (format: BASE-USD)
Step 3 — Collect side (for order placement)

Order direction:

BUY
SELL
Step 4 — Collect positionSide

Position direction:

LONG (open/add long)
SHORT (open/add short)
BOTH (one-way mode)
Step 5 — Collect order type

Order type:

MARKET — execute immediately at market price
LIMIT — execute at a specific price (requires price and timeInForce)
STOP_MARKET — stop-loss market order (triggers at stopPrice)
STOP — stop-loss limit order (triggers at stopPrice, executes at price)
TAKE_PROFIT_MARKET — take-profit market order (triggers at stopPrice)
TAKE_PROFIT — take-profit limit order (triggers at stopPrice, executes at price)
Step 6 — Collect quantity and price
Ask for quantity in contracts (integer, e.g., 1 contract ≈ $10 notional). Omit if using closePosition: true.
If type is LIMIT, STOP, or TAKE_PROFIT: also ask for price.
If type involves a trigger: also ask for stopPrice.
If type is MARKET or LIMIT: optionally offer to attach a stopLoss and/or takeProfit object.
Step 7 — Confirm (prod-live only)

You are about to place the following order on Production Live:

Symbol: BTC-USD
Side: BUY / LONG
Type: MARKET
Quantity: 1 contract

Type CONFIRM to proceed, or anything else to cancel.

Step 8 — Execute and report

Execute the API call and return the order ID and status to the user.

Cancel Order Flow
Ask for orderId (or clientOrderId) if not provided.
For prod-live: ask for CONFIRM.
Execute DELETE /openApi/cswap/v1/trade/cancelOrder.
Leverage Settings Flow
Ask for symbol if not provided.
Ask for position side (LONG / SHORT).
Ask for leverage value (e.g., 1–50 for BTC-USD).
For prod-live: ask for CONFIRM.
Execute POST /openApi/cswap/v1/trade/leverage.
Margin Type Flow
Ask for symbol if not provided.
Present options: ISOLATED or CROSSED.
For prod-live: ask for CONFIRM.
Execute POST /openApi/cswap/v1/trade/marginType.
Weekly Installs
67
Repository
bingx-api/api-ai-skills
GitHub Stars
8
First Seen
Mar 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn
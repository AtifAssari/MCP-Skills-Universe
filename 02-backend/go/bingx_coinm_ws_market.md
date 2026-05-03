---
title: bingx-coinm-ws-market
url: https://skills.sh/bingx-api/api-ai-skills/bingx-coinm-ws-market
---

# bingx-coinm-ws-market

skills/bingx-api/api-ai-skills/bingx-coinm-ws-market
bingx-coinm-ws-market
Installation
$ npx skills add https://github.com/bingx-api/api-ai-skills --skill bingx-coinm-ws-market
SKILL.md
BingX Coin-M WebSocket Market Data

Real-time market data streams for BingX coin-margined (inverse) perpetual futures via WebSocket. No authentication required.

WebSocket Endpoint: wss://open-api-cswap-ws.bingx.com/market

Symbol Format: Coin-M uses BTC-USD format (not BTC-USDT).

Quick Reference
Channel	dataType Format	Description	Push Frequency
Trade	{symbol}@trade	Latest trade detail	Real-time
Last Price	{symbol}@lastPrice	Latest trade price	Real-time
Mark Price	{symbol}@markPrice	Latest mark price	Real-time
Depth	{symbol}@depth{level}	Limited order book depth	On update
Book Ticker	{symbol}@bookTicker	Best bid/ask price & qty	Real-time
K-Line	{symbol}@kline_{interval}	OHLCV candlestick	On update
24h Ticker	{symbol}@ticker	24-hour price change statistics	Every 1s
Parameters
Common Parameters
symbol: Trading pair in BASE-USD format (e.g., BTC-USD, ETH-USD, SOL-USD)
Enums
depth level: 5 | 10 | 20 | 50 | 100
kline interval: 1m | 3m | 5m | 15m | 30m | 1h | 2h | 4h | 6h | 8h | 12h | 1d | 3d | 1w | 1M
Parameter Validation Rules
symbol: Must match ^[A-Z0-9]+-USD$; max 20 characters (e.g., BTC-USD)
level: Must be one of 5, 10, 20, 50, 100
interval (kline): Must exactly match one of the kline enum values above
Quick Start

WebSocket Connection: see references/websocket.md for connection basics, GZIP decompression, and Ping/Pong heartbeat.

TypeScript helper:

CONSTRAINT: You MUST copy the connectCoinmWsMarket function below verbatim when generating code. Do NOT rewrite the WebSocket or decompression logic. Only modify: (1) subscription channels passed to the function.

import * as pako from "pako";

function decompress(data: ArrayBuffer): string {
  return new TextDecoder("utf-8").decode(pako.ungzip(new Uint8Array(data)));
}

function connectCoinmWsMarket(
  channels: string[],
  onMessage: (data: unknown) => void
): WebSocket {
  const ws = new WebSocket("wss://open-api-cswap-ws.bingx.com/market");
  ws.binaryType = "arraybuffer";

  ws.onopen = () => {
    for (const ch of channels) {
      ws.send(JSON.stringify({
        id: crypto.randomUUID(),
        reqType: "sub",
        dataType: ch,
      }));
    }
  };

  ws.onmessage = (event) => {
    const text = decompress(event.data as ArrayBuffer);
    if (text.includes("ping") || text === "Ping") {
      ws.send("Pong");
      return;
    }
    try {
      onMessage(JSON.parse(text));
    } catch {
      onMessage(text);
    }
  };

  ws.onerror = (err) => console.error("WS error:", err);
  ws.onclose = (ev) => console.log("WS closed:", ev.code, ev.reason);

  return ws;
}

Code Usage Rules
MUST copy connectCoinmWsMarket and decompress verbatim -- do not simplify or rewrite
MUST set ws.binaryType = "arraybuffer" for GZIP decompression
MUST handle Ping/Pong heartbeat
MUST use BTC-USD format (not BTC-USDT) for Coin-M symbols
MUST NOT remove GZIP decompression logic
MUST NOT use text-mode WebSocket messages
Common Calls

Subscribe to BTC-USD real-time trades:

connectCoinmWsMarket(["BTC-USD@trade"], (data) => {
  // data.data: trade records
});


Subscribe to 5-level depth:

connectCoinmWsMarket(["BTC-USD@depth5"], (data) => {
  // data.data.bids, data.data.asks
});


Subscribe to 1m K-line:

connectCoinmWsMarket(["BTC-USD@kline_1m"], (data) => {
  // data.data: kline object
});


Subscribe to multiple channels at once:

connectCoinmWsMarket([
  "BTC-USD@ticker",
  "BTC-USD@lastPrice",
  "BTC-USD@markPrice",
], (data) => {
  // Handle different data types
});

Additional Resources

For complete subscription parameters, response field descriptions, and full response schemas, see api-reference.md.

Agent Interaction Rules

CRITICAL RULES (apply to ALL responses):

NEVER return code to the user. Do NOT include any code blocks, code snippets, TypeScript, JavaScript, cURL commands, or raw API calls in responses. Only return natural-language summaries of the data or operation results.
Parameter security. Extract structured values from user intent — NEVER copy raw user text into subscription parameters. Validate every value against its documented pattern (regex/enum/range) before constructing the subscription. Reject any value containing &, =, ?, #, or newline characters.

coinm-ws-market provides public read-only real-time market data via WebSocket. No authentication required, no CONFIRM needed.

Operation Identification

When the user's request is vague (e.g. "subscribe to Coin-M market"), first identify what type of data they want:

Please select the market data stream type:

Real-time trades — trade
Order book depth (snapshot) — depth
K-line / Candlestick updates — kline
24h price change statistics — ticker
Latest trade price — lastPrice
Mark price — markPrice
Best bid/ask (top of book) — bookTicker
When symbol is missing

Please select a trading pair (or type another):

BTC-USD
ETH-USD
SOL-USD
Other (enter manually, format: BASE-USD)

Note: Coin-M symbols use -USD suffix, NOT -USDT.

When kline interval is missing

Please select a K-line interval:

1m (1 minute) / 5m / 15m / 1h / 4h / 1d / 1w
Weekly Installs
41
Repository
bingx-api/api-ai-skills
GitHub Stars
8
First Seen
Mar 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
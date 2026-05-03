---
title: kalshi-trading
url: https://skills.sh/newyorkcompute/kalshi/kalshi-trading
---

# kalshi-trading

skills/newyorkcompute/kalshi/kalshi-trading
kalshi-trading
Installation
$ npx skills add https://github.com/newyorkcompute/kalshi --skill kalshi-trading
SKILL.md
Kalshi Trading

Trade on Kalshi, a CFTC-regulated prediction market exchange. This skill enables you to query markets, analyze probabilities, manage positions, and execute trades.

Types
interface Market {
  ticker: string;
  title: string;
  status: string;
  yes_bid?: number;
  yes_ask?: number;
  volume?: number;
  close_time?: string;
}

interface Orderbook {
  yes: [number, number][]; // [price_cents, quantity]
  no: [number, number][];
}

interface Balance {
  balance: number; // cents
  payout: number;  // pending settlement
}

interface Position {
  ticker: string;
  position: number; // positive = YES, negative = NO
  market_exposure: number;
}

interface Order {
  order_id: string;
  ticker: string;
  side: "yes" | "no";
  action: "buy" | "sell";
  count: number;
  status: string;
}

Quick Start
import * as crypto from "crypto";

const API_BASE = "https://api.elections.kalshi.com/trade-api/v2";

// See AUTHENTICATION.md for full setup
function getAuthHeaders(
  apiKey: string,
  privateKeyPem: string,
  method: string,
  path: string
): Record<string, string> {
  const timestamp = Date.now().toString();
  const message = `${timestamp}${method}${path}`;

  const sign = crypto.createSign("RSA-SHA256");
  sign.update(message);
  const signature = sign.sign(privateKeyPem, "base64");

  return {
    "KALSHI-ACCESS-KEY": apiKey,
    "KALSHI-ACCESS-SIGNATURE": signature,
    "KALSHI-ACCESS-TIMESTAMP": timestamp,
    "Content-Type": "application/json",
  };
}

Common Operations
Search Markets
async function searchMarkets(query: string, limit = 10): Promise<Market[]> {
  const url = new URL(`${API_BASE}/markets`);
  url.searchParams.set("status", "open");
  url.searchParams.set("limit", String(limit));

  const response = await fetch(url.toString());
  const data = await response.json();

  // Filter by query in title
  return data.markets.filter((m: Market) =>
    m.title.toLowerCase().includes(query.toLowerCase())
  );
}

Get Market Details
async function getMarket(ticker: string): Promise<Market> {
  const response = await fetch(`${API_BASE}/markets/${ticker}`);
  const data = await response.json();
  return data.market;
}

Get Orderbook
async function getOrderbook(ticker: string): Promise<Orderbook> {
  const response = await fetch(`${API_BASE}/markets/${ticker}/orderbook`);
  const data = await response.json();
  return data.orderbook;
}

Check Balance (Authenticated)
async function getBalance(
  apiKey: string,
  privateKeyPem: string
): Promise<Balance> {
  const path = "/portfolio/balance";
  const headers = getAuthHeaders(apiKey, privateKeyPem, "GET", path);

  const response = await fetch(`${API_BASE}${path}`, { headers });
  return response.json();
}

Get Positions (Authenticated)
async function getPositions(
  apiKey: string,
  privateKeyPem: string
): Promise<Position[]> {
  const path = "/portfolio/positions";
  const headers = getAuthHeaders(apiKey, privateKeyPem, "GET", path);

  const response = await fetch(`${API_BASE}${path}`, { headers });
  const data = await response.json();
  return data.market_positions;
}

Place Order (Authenticated)
async function placeOrder(
  apiKey: string,
  privateKeyPem: string,
  ticker: string,
  side: "yes" | "no",
  action: "buy" | "sell",
  count: number,
  price: number // In cents (1-99)
): Promise<Order> {
  const path = "/portfolio/orders";
  const headers = getAuthHeaders(apiKey, privateKeyPem, "POST", path);

  const body = {
    ticker,
    side,
    action,
    count,
    type: "limit",
    ...(side === "yes" ? { yes_price: price } : { no_price: price }),
  };

  const response = await fetch(`${API_BASE}${path}`, {
    method: "POST",
    headers,
    body: JSON.stringify(body),
  });
  const data = await response.json();
  return data.order;
}

Key Concepts
Markets: Event contracts with Yes/No outcomes (e.g., "Will X happen by Y date?")
Prices: Quoted in cents (1-99), representing probability percentage
Positions: Your holdings in Yes or No contracts
Settlement: Markets resolve to $1.00 (Yes wins) or $0.00 (No wins)
Additional Resources
AUTHENTICATION.md - Detailed API key setup
API_REFERENCE.md - Full endpoint documentation
scripts/kalshi-client.ts - Ready-to-use TypeScript client
Tips
Start with market research: Use searchMarkets() to explore opportunities
Check liquidity: Review orderbook depth before placing large orders
Use limit orders: Avoid market orders to control execution price
Monitor positions: Regularly check your positions and P&L
Weekly Installs
31
Repository
newyorkcompute/kalshi
GitHub Stars
4
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn
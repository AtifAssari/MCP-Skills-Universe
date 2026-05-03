---
rating: ⭐⭐
title: polymarket
url: https://skills.sh/2025emma/vibe-coding-cn/polymarket
---

# polymarket

skills/2025emma/vibe-coding-cn/polymarket
polymarket
Installation
$ npx skills add https://github.com/2025emma/vibe-coding-cn --skill polymarket
Summary

Complete Polymarket integration covering prediction markets, REST API, trading, and real-time WebSocket data streaming.

Supports six WebSocket topic categories: activity (trades, orders), comments (with reactions), RFQ events, crypto price feeds, authenticated user order/trade updates, and market-level price and orderbook data
Includes TypeScript client library with topic-based subscriptions, dynamic filter support, and initial data dumps on connection
Covers REST API for market discovery, portfolio management, trading strategies, and market resolution alongside real-time streaming
Authentication available for private user data streams; public topics require no credentials
SKILL.md
Polymarket Comprehensive Skill

Complete assistance with Polymarket development - covering the full platform (API, trading, market data) and the real-time data streaming client (WebSocket subscriptions for live market activity).

When to Use This Skill

This skill should be triggered when:

Platform & API:

Working with Polymarket prediction markets
Using Polymarket API for market data
Implementing trading strategies
Building applications with Polymarket services
Learning Polymarket best practices

Real-Time Data Streaming:

Connecting to Polymarket's WebSocket service
Building prediction market monitoring tools
Processing live trades, orders, and market updates
Monitoring market comments and social reactions
Tracking RFQ (Request for Quote) activity
Integrating crypto price feeds
Quick Reference
Real-Time Data Client Setup

Installation:

npm install @polymarket/real-time-data-client


Basic Usage:

import { RealTimeDataClient } from "@polymarket/real-time-data-client";

const onMessage = (message: Message): void => {
    console.log(message.topic, message.type, message.payload);
};

const onConnect = (client: RealTimeDataClient): void => {
    client.subscribe({
        subscriptions: [{
            topic: "activity",
            type: "trades"
        }]
    });
};

new RealTimeDataClient({ onMessage, onConnect }).connect();

Supported WebSocket Topics

1. Activity (activity)

trades - Completed trades
orders_matched - Order matching events
Filters: {"event_slug":"string"} OR {"market_slug":"string"}

2. Comments (comments)

comment_created, comment_removed
reaction_created, reaction_removed
Filters: {"parentEntityID":number,"parentEntityType":"Event"}

3. RFQ (rfq)

Request/Quote lifecycle events
No filters, no auth required

4. Crypto Prices (crypto_prices, crypto_prices_chainlink)

update - Real-time price feeds
Filters: {"symbol":"BTC"} (optional)

5. CLOB User (clob_user) ⚠️ Requires Auth

order - User's order updates
trade - User's trade executions

6. CLOB Market (clob_market)

price_change - Price movements
agg_orderbook - Aggregated order book
last_trade_price - Latest prices
market_created, market_resolved
Authentication for User Data
client.subscribe({
    subscriptions: [{
        topic: "clob_user",
        type: "*",
        clob_auth: {
            key: "your-api-key",
            secret: "your-api-secret",
            passphrase: "your-passphrase"
        }
    }]
});

Common Use Cases

Monitor Specific Market:

client.subscribe({
    subscriptions: [{
        topic: "activity",
        type: "trades",
        filters: `{"market_slug":"btc-above-100k-2024"}`
    }]
});


Track Multiple Markets:

client.subscribe({
    subscriptions: [{
        topic: "clob_market",
        type: "price_change",
        filters: `["100","101","102"]`
    }]
});


Monitor Event Comments:

client.subscribe({
    subscriptions: [{
        topic: "comments",
        type: "*",
        filters: `{"parentEntityID":12345,"parentEntityType":"Event"}`
    }]
});

Reference Files

This skill includes comprehensive documentation in references/:

Platform Documentation:

api.md - Polymarket API documentation
getting_started.md - Getting started guide
guides.md - Development guides
learn.md - Learning resources
trading.md - Trading documentation
other.md - Additional resources

Real-Time Client:

README.md - WebSocket client API and examples
llms.md - LLM integration guide
llms-full.md - Complete LLM documentation

Use view to read specific reference files for detailed information.

Key Features

Platform Capabilities: ✅ Prediction market creation and resolution ✅ Trading API (REST & WebSocket) ✅ Market data queries ✅ User portfolio management ✅ Event and market discovery

Real-Time Streaming: ✅ WebSocket-based persistent connections ✅ Topic-based subscriptions ✅ Dynamic subscription management ✅ Filter support for targeted data ✅ User authentication for private data ✅ TypeScript with full type safety ✅ Initial data dumps on connection

Best Practices
WebSocket Connection Management
Use onConnect callback for subscriptions
Implement reconnection logic for production
Clean up with disconnect() when done
Handle authentication errors gracefully
Subscription Strategy
Use wildcards ("*") sparingly
Apply filters to reduce data volume
Unsubscribe from unused streams
Process messages asynchronously
Performance
Consider batching high-frequency data
Use filters to minimize client processing
Validate message payloads before use
Requirements
Node.js: 14+ recommended
TypeScript: Optional but recommended
Package Manager: npm or yarn
Resources
Official Links
Polymarket Platform: https://polymarket.com
Real-Time Client Repo: https://github.com/Polymarket/real-time-data-client
API Documentation: See references/api.md
Working with This Skill

For Beginners: Start with getting_started.md for foundational concepts.

For API Integration: Use api.md and trading.md for REST API details.

For Real-Time Data: Use README.md for WebSocket client implementation.

For LLM Integration: Use llms.md and llms-full.md for AI/ML use cases.

Notes
Real-Time Client is TypeScript/JavaScript (not Python)
Some WebSocket topics require authentication
Use filters to manage message volume effectively
All timestamps are Unix timestamps
Market IDs are strings (e.g., "100", "101")
Platform documentation covers both REST API and WebSocket usage

This comprehensive skill combines Polymarket platform expertise with real-time data streaming capabilities!

Weekly Installs
378
Repository
2025emma/vibe-coding-cn
GitHub Stars
20.1K
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail
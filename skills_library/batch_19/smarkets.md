---
title: smarkets
url: https://skills.sh/alsk1992/cloddsbot/smarkets
---

# smarkets

skills/alsk1992/cloddsbot/smarkets
smarkets
Installation
$ npx skills add https://github.com/alsk1992/cloddsbot --skill smarkets
SKILL.md
Smarkets Exchange

Full integration with Smarkets, a betting exchange with lower fees than Betfair (2% vs 5%). Politics, sports, and entertainment markets.

Quick Start
# Set credentials
export SMARKETS_SESSION_TOKEN="your-session-token"

# Search markets
/sm markets election

# Get market prices
/sm prices 12345

# Place buy order
/sm buy 12345 67890 0.55 10

# Place sell order
/sm sell 12345 67890 0.60 10

Commands
Market Data
Command	Description
/sm markets [query]	Search markets
/sm market <id>	Get market details
/sm prices <marketId>	Current prices
/sm book <marketId> <contractId>	Show orderbook
Trading
Command	Description
/sm buy <marketId> <contractId> <price> <quantity>	Place buy order
/sm sell <marketId> <contractId> <price> <quantity>	Place sell order
/sm cancel <orderId>	Cancel order
/sm cancelall [marketId]	Cancel all orders
/sm orders [marketId]	List open orders

Examples:

/sm buy 123 456 0.55 10    # Buy at 55% price, £10
/sm sell 123 456 0.60 10   # Sell at 60% price, £10
/sm cancel abc123          # Cancel specific order

Account
Command	Description
/sm balance	Check account balance
Configuration
# Required for trading
export SMARKETS_SESSION_TOKEN="your-session-token"

# Optional - API token for market data only
export SMARKETS_API_TOKEN="your-api-token"

Features
Low Fees - 2% commission vs Betfair's 5%
Politics Markets - UK, US, EU elections
Sports - Football, tennis, horse racing
Entertainment - TV, music, awards
Real-time Streaming - WebSocket price updates
Market Types
Domain	Examples
politics	Elections, referendums
sport	Football, tennis, cricket
entertainment	Oscars, Eurovision, reality TV
current_affairs	Economic events, news
esports	CS:GO, League of Legends
Trading Notes
Prices: Expressed as percentages (0.55 = 55%)
Quantities: In GBP
Buy: Betting FOR an outcome
Sell: Betting AGAINST an outcome
Resources
Smarkets Exchange
Smarkets API Docs
Weekly Installs
9
Repository
alsk1992/cloddsbot
GitHub Stars
194
First Seen
Feb 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
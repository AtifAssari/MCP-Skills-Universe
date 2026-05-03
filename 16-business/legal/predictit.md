---
title: predictit
url: https://skills.sh/alsk1992/cloddsbot/predictit
---

# predictit

skills/alsk1992/cloddsbot/predictit
predictit
Installation
$ npx skills add https://github.com/alsk1992/cloddsbot --skill predictit
SKILL.md
PredictIt

Read-only integration with PredictIt, a US political prediction market. View markets and prices.

Quick Start
# Search markets
/pi search president

# Get market details
/pi market 6867

# List all markets
/pi all

Commands
Command	Description
/pi search [query]	Search markets
/pi market <id>	Get market details
/pi all	List all active markets

Examples:

/pi search election       # Search election markets
/pi market 6867           # Get specific market
/pi all                   # List all markets

Features
Political Markets - US elections, congress, policy
Real-time Prices - Last trade and best bid/ask
Contract Details - Individual outcomes with prices
Notes
PredictIt is read-only (no trading API)
Prices shown are last trade price
Market volume not exposed by API
US politics focused
Price Data
Field	Description
lastTradePrice	Most recent trade price
bestBuyYesCost	Best offer to buy Yes
bestBuyNoCost	Best offer to buy No
bestSellYesCost	Best bid to sell Yes
bestSellNoCost	Best bid to sell No
Resources
PredictIt
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
SnykPass
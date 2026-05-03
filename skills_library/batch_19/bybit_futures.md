---
title: bybit-futures
url: https://skills.sh/alsk1992/cloddsbot/bybit-futures
---

# bybit-futures

skills/alsk1992/cloddsbot/bybit-futures
bybit-futures
Installation
$ npx skills add https://github.com/alsk1992/cloddsbot --skill bybit-futures
SKILL.md
Bybit Futures

Trade perpetual futures on Bybit with up to 100x leverage and full database tracking.

Quick Start
# Set credentials
export BYBIT_API_KEY="your-api-key"
export BYBIT_API_SECRET="your-api-secret"

# Check balance
/bb balance

# Open position
/bb long BTCUSDT 0.01 10x

# View stats
/bb stats

Commands
Account
Command	Description
/bb balance	Check wallet balance
/bb positions	View open positions
/bb orders	List open orders
Trading
Command	Description
/bb long <symbol> <size> [leverage]x	Open long position
/bb short <symbol> <size> [leverage]x	Open short position
/bb close <symbol>	Close position
/bb closeall	Close all positions
/bb tp <symbol> <price>	Set take-profit
/bb sl <symbol> <price>	Set stop-loss
/bb leverage <symbol> <value>	Set leverage
Market Data
Command	Description
/bb price <symbol>	Get current price
/bb funding <symbol>	Check funding rate
/bb markets [query]	List markets
Database/History
Command	Description
/bb trades [symbol] [limit]	Trade history from database
/bb dbstats [symbol] [period]	Win rate, PnL, profit factor
/bb dbfunding [symbol]	Funding payments history
/bb dbpositions [all]	Position history

Stats periods: day, week, month

Examples
/bb long BTCUSDT 0.01 10x      # 10x leveraged long
/bb short ETHUSDT 0.1 20x      # 20x leveraged short
/bb tp BTCUSDT 105000          # Take profit at $105k
/bb sl BTCUSDT 95000           # Stop loss at $95k
/bb close BTCUSDT              # Close BTC position
/bb trades BTCUSDT 20          # Last 20 BTC trades
/bb stats ETHUSDT week         # ETH stats for past week

Weekly Installs
25
Repository
alsk1992/cloddsbot
GitHub Stars
194
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
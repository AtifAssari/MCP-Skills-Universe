---
title: binance-futures
url: https://skills.sh/alsk1992/cloddsbot/binance-futures
---

# binance-futures

skills/alsk1992/cloddsbot/binance-futures
binance-futures
Installation
$ npx skills add https://github.com/alsk1992/cloddsbot --skill binance-futures
SKILL.md
Binance Futures

Trade perpetual futures on Binance with up to 125x leverage and full database tracking.

Quick Start
# Set credentials
export BINANCE_API_KEY="your-api-key"
export BINANCE_API_SECRET="your-api-secret"

# Check balance
/bf balance

# Open position
/bf long BTCUSDT 0.01 10x

# View stats
/bf stats

Commands
Account
Command	Description
/bf balance	Check margin balance
/bf positions	View open positions
/bf orders	List open orders
Trading
Command	Description
/bf long <symbol> <size> [leverage]x	Open long position
/bf short <symbol> <size> [leverage]x	Open short position
/bf close <symbol>	Close position
/bf closeall	Close all positions
/bf tp <symbol> <price>	Set take-profit
/bf sl <symbol> <price>	Set stop-loss
/bf leverage <symbol> <value>	Set leverage
Market Data
Command	Description
/bf price <symbol>	Get current price
/bf funding <symbol>	Check funding rate
/bf markets [query]	List markets
Database/History
Command	Description
/bf trades [symbol] [limit]	Trade history from database
/bf dbstats [symbol] [period]	Win rate, PnL, profit factor
/bf dbfunding [symbol]	Funding payments history
/bf dbpositions [all]	Position history

Stats periods: day, week, month

Examples
/bf long BTCUSDT 0.01 10x      # 10x leveraged long
/bf short ETHUSDT 0.1 20x      # 20x leveraged short
/bf tp BTCUSDT 105000          # Take profit at $105k
/bf sl BTCUSDT 95000           # Stop loss at $95k
/bf close BTCUSDT              # Close BTC position
/bf trades BTCUSDT 20          # Last 20 BTC trades
/bf dbstats ETHUSDT week       # ETH stats for past week

Weekly Installs
149
Repository
alsk1992/cloddsbot
GitHub Stars
194
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn
---
title: mexc-futures
url: https://skills.sh/alsk1992/cloddsbot/mexc-futures
---

# mexc-futures

skills/alsk1992/cloddsbot/mexc-futures
mexc-futures
Installation
$ npx skills add https://github.com/alsk1992/cloddsbot --skill mexc-futures
SKILL.md
MEXC Futures

Trade perpetual futures on MEXC with up to 200x leverage. No KYC required for small amounts.

Quick Start
# Set credentials
export MEXC_API_KEY="your-api-key"
export MEXC_API_SECRET="your-api-secret"

# Check balance
/mx balance

# Open position
/mx long BTC_USDT 1 10x

# View stats
/mx stats

Commands
Account
Command	Description
/mx balance	Check account balance
/mx positions	View open positions
/mx orders	List open orders
Trading
Command	Description
/mx long <symbol> <vol> [leverage]x	Open long position
/mx short <symbol> <vol> [leverage]x	Open short position
/mx close <symbol>	Close position
/mx closeall	Close all positions
/mx leverage <symbol> <value>	Set leverage
Market Data
Command	Description
/mx price <symbol>	Get current price
/mx funding <symbol>	Check funding rate
/mx markets [query]	List markets
Database/History
Command	Description
/mx trades [symbol] [limit]	Trade history from database
/mx dbstats [symbol] [period]	Win rate, PnL, profit factor
/mx dbfunding [symbol]	Funding payments history
/mx dbpositions [all]	Position history

Stats periods: day, week, month

Examples
/mx long BTC_USDT 1 10x        # 10x leveraged long, 1 contract
/mx short ETH_USDT 5 20x       # 20x leveraged short, 5 contracts
/mx close BTC_USDT             # Close BTC position
/mx trades BTC_USDT 20         # Last 20 BTC trades
/mx stats ETH_USDT week        # ETH stats for past week

Notes
MEXC uses contract notation (e.g., BTC_USDT not BTCUSDT)
No KYC required for smaller trading volumes
Up to 200x leverage available
Weekly Installs
15
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
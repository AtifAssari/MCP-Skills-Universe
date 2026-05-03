---
rating: ⭐⭐
title: option-chain
url: https://skills.sh/staskh/trading_skills/option-chain
---

# option-chain

skills/staskh/trading_skills/option-chain
option-chain
Installation
$ npx skills add https://github.com/staskh/trading_skills --skill option-chain
SKILL.md
Option Chain

Fetch option chain data from Yahoo Finance for a specific expiration date.

Instructions

Note: If uv is not installed or pyproject.toml is not found, replace uv run python with python in all commands below.

First, get available expiration dates:

uv run python scripts/options.py SYMBOL --expiries


Then fetch the chain for a specific expiry:

uv run python scripts/options.py SYMBOL --expiry YYYY-MM-DD

Arguments
SYMBOL - Ticker symbol (e.g., AAPL, SPY, TSLA)
--expiries - List available expiration dates only
--expiry YYYY-MM-DD - Fetch chain for specific date
Output

Returns JSON with:

calls - Array of call options with strike, bid, ask, volume, openInterest, impliedVolatility
puts - Array of put options with same fields
underlying_price - Current stock price for reference

Present data as a table. Highlight high volume/OI strikes and notable IV levels.

Dependencies
pandas
yfinance
Weekly Installs
39
Repository
staskh/trading_skills
GitHub Stars
139
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
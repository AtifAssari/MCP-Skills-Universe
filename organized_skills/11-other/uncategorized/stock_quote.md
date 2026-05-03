---
rating: ⭐⭐
title: stock-quote
url: https://skills.sh/staskh/trading_skills/stock-quote
---

# stock-quote

skills/staskh/trading_skills/stock-quote
stock-quote
Installation
$ npx skills add https://github.com/staskh/trading_skills --skill stock-quote
SKILL.md
Stock Quote

Fetch current stock data from Yahoo Finance.

Instructions

Note: If uv is not installed or pyproject.toml is not found, replace uv run python with python in all commands below.

Run the quote script with the ticker symbol:

uv run python scripts/quote.py SYMBOL


Replace SYMBOL with the requested ticker (e.g., AAPL, MSFT, TSLA, SPY).

Output

The script outputs JSON with:

symbol, name, price, change, change_percent
volume, avg_volume, market_cap
high_52w, low_52w, pe_ratio, dividend_yield

Present the data in a readable format. Highlight significant moves (>2% change).

Dependencies
yfinance
Weekly Installs
56
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
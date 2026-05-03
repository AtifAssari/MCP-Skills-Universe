---
title: yahoo-finance
url: https://skills.sh/gracefullight/stock-checker/yahoo-finance
---

# yahoo-finance

skills/gracefullight/stock-checker/yahoo-finance
yahoo-finance
Installation
$ npx skills add https://github.com/gracefullight/stock-checker --skill yahoo-finance
Summary

Fetch stock prices, quotes, fundamentals, earnings, options, and analyst ratings from Yahoo Finance without API keys.

Supports 10+ command categories including price quotes, fundamentals, earnings dates, dividends, analyst ratings, options chains, and historical data
Works with US stocks, Indian NSE/BSE symbols, cryptocurrencies, forex pairs, and ETFs
Requires Python 3.11+ and uv package manager; dependencies auto-install on first run via PEP 723 inline script metadata
Includes symbol search, multi-stock comparison, and configurable historical date ranges from 1 day to max available data
SKILL.md
Yahoo Finance CLI

A Python CLI for fetching comprehensive stock data from Yahoo Finance using yfinance.

Requirements
Python 3.11+
uv (for inline script dependencies)
Installing uv

The script requires uv - an extremely fast Python package manager. Check if it's installed:

uv --version


If not installed, install it using one of these methods:

macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

macOS (Homebrew)
brew install uv

Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

pip (any platform)
pip install uv


After installation, restart your terminal or run:

source ~/.bashrc  # or ~/.zshrc on macOS

Installation

The yf script uses PEP 723 inline script metadata - dependencies are auto-installed on first run.

# Make executable
chmod +x /path/to/skills/yahoo-finance/yf

# Optionally symlink to PATH for global access
ln -sf /path/to/skills/yahoo-finance/yf /usr/local/bin/yf


First run will install dependencies (yfinance, rich) to uv's cache. Subsequent runs are instant.

Commands
Price (quick check)
yf AAPL              # shorthand for price
yf price AAPL

Quote (detailed)
yf quote MSFT

Fundamentals
yf fundamentals NVDA


Shows: PE ratios, EPS, market cap, margins, ROE/ROA, analyst targets.

Earnings
yf earnings TSLA


Shows: Next earnings date, EPS estimates, earnings history with surprises.

Company Profile
yf profile GOOGL


Shows: Sector, industry, employees, website, address, business description.

Dividends
yf dividends KO


Shows: Dividend rate/yield, ex-date, payout ratio, recent dividend history.

Analyst Ratings
yf ratings AAPL


Shows: Buy/hold/sell distribution, mean rating, recent upgrades/downgrades.

Options Chain
yf options SPY


Shows: Near-the-money calls and puts with strike, bid/ask, volume, OI, IV.

History
yf history GOOGL 1mo     # 1 month history
yf history TSLA 1y       # 1 year
yf history BTC-USD 5d    # 5 days


Ranges: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max

Compare
yf compare AAPL,MSFT,GOOGL
yf compare RELIANCE.NS,TCS.NS,INFY.NS


Side-by-side comparison with price, change, 52W range, market cap.

Search
yf search "reliance industries"
yf search "bitcoin"
yf search "s&p 500 etf"

Symbol Format
US stocks: AAPL, MSFT, GOOGL, TSLA
Indian NSE: RELIANCE.NS, TCS.NS, INFY.NS
Indian BSE: RELIANCE.BO, TCS.BO
Crypto: BTC-USD, ETH-USD
Forex: EURUSD=X, GBPUSD=X
ETFs: SPY, QQQ, VOO
Examples
# Quick price check
yf AAPL

# Get valuation metrics
yf fundamentals NVDA

# Next earnings date + history
yf earnings TSLA

# Options chain for SPY
yf options SPY

# Compare tech giants
yf compare AAPL,MSFT,GOOGL,META,AMZN

# Find Indian stocks
yf search "infosys"

# Dividend info for Coca-Cola
yf dividends KO

# Analyst ratings for Apple
yf ratings AAPL

Troubleshooting
"command not found: uv"

Install uv using the instructions above.

Rate limiting / connection errors

Yahoo Finance may rate limit excessive requests. Wait a few minutes and try again.

"No data" for a symbol
Verify the symbol exists: yf search "company name"
Some data (options, dividends) isn't available for all securities
Technical Notes
Uses PEP 723 inline script metadata for uv dependencies
Rich library provides colored, formatted tables
First run installs deps to uv cache (~5 seconds)
Subsequent runs are instant (cached environment)
Handles NaN/None values gracefully with fallbacks
Weekly Installs
3.2K
Repository
gracefullight/s…-checker
GitHub Stars
18
First Seen
1 day ago
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail
---
rating: ⭐⭐
title: quick-stats
url: https://skills.sh/marketcalls/vectorbt-backtesting-skills/quick-stats
---

# quick-stats

skills/marketcalls/vectorbt-backtesting-skills/quick-stats
quick-stats
Installation
$ npx skills add https://github.com/marketcalls/vectorbt-backtesting-skills --skill quick-stats
Summary

Inline backtest runner for Indian equities with EMA crossover strategy and benchmark comparison.

Fetches OHLC data from OpenAlgo (with yfinance fallback) and runs a TA-Lib EMA 10/20 crossover strategy without file creation
Applies Indian delivery fees (0.111% + Rs 20 per order) and automatically fetches NIFTY benchmark for alpha calculation
Prints compact results summary including total return, Sharpe/Sortino ratios, max drawdown, win rate, and profit factor with plain-language metric explanations
Generates an interactive Plotly equity curve chart and accepts symbol, exchange, and interval as command arguments with sensible defaults (SBIN, NSE, daily)
SKILL.md

Generate a quick inline backtest and print stats. Do NOT create a file - output code directly for the user to run or execute in a notebook.

Arguments
$0 = symbol (e.g., SBIN, RELIANCE). Default: SBIN
$1 = exchange. Default: NSE
$2 = interval. Default: D
Instructions

Generate a single code block the user can paste into a Jupyter cell or run as a script. The code must:

Fetch data from OpenAlgo (or DuckDB if user provides a DB path, or yfinance as fallback)
Use TA-Lib for EMA 10/20 crossover (never VectorBT built-in)
Clean signals with ta.exrem() (always .fillna(False) before exrem)
Use Indian delivery fees: fees=0.00111, fixed_fees=20
Fetch NIFTY benchmark via OpenAlgo (symbol="NIFTY", exchange="NSE_INDEX")
Print a compact results summary:
Symbol: SBIN | Exchange: NSE | Interval: D
Strategy: EMA 10/20 Crossover
Period: 2023-01-01 to 2026-02-27
Fees: Delivery Equity (0.111% + Rs 20/order)
-------------------------------------------
Total Return:    45.23%
Sharpe Ratio:    1.45
Sortino Ratio:   2.01
Max Drawdown:   -12.34%
Win Rate:        42.5%
Profit Factor:   1.67
Total Trades:    28
-------------------------------------------
Benchmark (NIFTY): 32.10%
Alpha:           +13.13%

Explain key metrics in plain language for normal traders
Show equity curve plot using Plotly (template="plotly_dark")
Example Usage

/quick-stats RELIANCE /quick-stats HDFCBANK NSE 1h

Weekly Installs
740
Repository
marketcalls/vec…g-skills
GitHub Stars
127
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
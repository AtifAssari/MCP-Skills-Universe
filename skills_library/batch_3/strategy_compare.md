---
title: strategy-compare
url: https://skills.sh/marketcalls/vectorbt-backtesting-skills/strategy-compare
---

# strategy-compare

skills/marketcalls/vectorbt-backtesting-skills/strategy-compare
strategy-compare
Installation
$ npx skills add https://github.com/marketcalls/vectorbt-backtesting-skills --skill strategy-compare
Summary

Side-by-side backtesting comparison of multiple trading strategies on the same symbol.

Compares user-specified strategies (or defaults to ema-crossover, rsi, donchian, supertrend) against the same historical data and NIFTY benchmark
Supports "long-vs-short" mode to test longonly, shortonly, and both directions for a given strategy
Uses TA-Lib for standard indicators and OpenAlgo ta for specialty indicators like Supertrend and Donchian; cleans signals with exrem() to avoid consecutive duplicates
Generates a side-by-side metrics table (Total Return, Sharpe, Sortino, Max DD, Win Rate, Trades, Profit Factor) and overlaid Plotly equity curves; includes plain-language explanation of which strategy performed best
Applies Indian delivery equity fees (0.00111 + 20 fixed) and loads data from OpenAlgo or DuckDB depending on availability
SKILL.md

Create a strategy comparison script.

Arguments

Parse $ARGUMENTS as: symbol followed by strategy names

$0 = symbol (e.g., SBIN, RELIANCE, NIFTY)
Remaining args = strategies to compare (e.g., ema-crossover rsi donchian)

If only a symbol is given with no strategies, compare: ema-crossover, rsi, donchian, supertrend. If "long-vs-short" is one of the strategies, compare longonly vs shortonly vs both for the first real strategy.

Instructions
Read the vectorbt-expert skill rules for reference patterns
Create backtesting/strategy_comparison/ directory if it doesn't exist (on-demand)
Create a .py file in backtesting/strategy_comparison/ named {symbol}_strategy_comparison.py
The script must:
Fetch data once via OpenAlgo
If user provides a DuckDB path, load data directly via duckdb.connect(path, read_only=True). See vectorbt-expert rules/duckdb-data.md.
If openalgo.ta is not importable (standalone DuckDB), use inline exrem() fallback.
Use TA-Lib for ALL indicators (never VectorBT built-in)
Use OpenAlgo ta for specialty indicators (Supertrend, Donchian, etc.)
Clean signals with ta.exrem() (always .fillna(False) before exrem)
Run each strategy on the same data
Indian delivery fees: fees=0.00111, fixed_fees=20 for delivery equity
Collect key metrics from each into a side-by-side DataFrame
Include NIFTY benchmark in the comparison table (via OpenAlgo NSE_INDEX)
Print Strategy vs Benchmark comparison table: Total Return, Sharpe, Sortino, Max DD, Win Rate, Trades, Profit Factor
Explain results in plain language - which strategy performed best and why
Plot overlaid equity curves for all strategies using Plotly (template="plotly_dark")
Save comparison to CSV
Never use icons/emojis in code or logger output
Example Usage

/strategy-compare RELIANCE ema-crossover rsi donchian /strategy-compare SBIN long-vs-short ema-crossover

Weekly Installs
768
Repository
marketcalls/vec…g-skills
GitHub Stars
127
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
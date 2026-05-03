---
title: optimize
url: https://skills.sh/marketcalls/vectorbt-backtesting-skills/optimize
---

# optimize

skills/marketcalls/vectorbt-backtesting-skills/optimize
optimize
Installation
$ npx skills add https://github.com/marketcalls/vectorbt-backtesting-skills --skill optimize
Summary

Backtesting strategy parameter optimization with VectorBT, generating performance heatmaps and benchmark comparisons.

Accepts strategy name, symbol, exchange, and interval; creates optimization script in backtesting/{strategy}/ directory
Loads market data from OpenAlgo via .env configuration or directly from DuckDB; uses TA-Lib for all indicators with OpenAlgo ta for specialty indicators like Supertrend and Donchian
Tests parameter combinations across sensible ranges (e.g., EMA 5-50 for fast, 10-60 for slow), tracking total return, Sharpe ratio, max drawdown, and trade count per combo
Generates Plotly heatmaps for total return and Sharpe ratio; fetches NIFTY benchmark and prints strategy vs benchmark comparison table with plain-language results explanation
Applies Indian delivery fees (0.00111 + 20 fixed) and futures lot-size awareness (NIFTY 65, BANKNIFTY 30); saves results to CSV
SKILL.md

Create a parameter optimization script for a VectorBT strategy.

Arguments

Parse $ARGUMENTS as: strategy symbol exchange interval

$0 = strategy name (e.g., ema-crossover, rsi, donchian). Default: ema-crossover
$1 = symbol (e.g., SBIN, RELIANCE, NIFTY). Default: SBIN
$2 = exchange (e.g., NSE, NFO). Default: NSE
$3 = interval (e.g., D, 1h, 5m). Default: D

If no arguments, ask the user which strategy to optimize.

Instructions
Read the vectorbt-expert skill rules for reference patterns
Create backtesting/{strategy_name}/ directory if it doesn't exist (on-demand)
Create a .py file in backtesting/{strategy_name}/ named {symbol}_{strategy}_optimize.py
The script must:
Load .env from project root using find_dotenv() and fetch data via OpenAlgo client.history()
If user provides a DuckDB path, load data directly via duckdb.connect(path, read_only=True). See vectorbt-expert rules/duckdb-data.md.
If openalgo.ta is not importable (standalone DuckDB), use inline exrem() fallback.
Use TA-Lib for ALL indicators (never VectorBT built-in)
Use OpenAlgo ta for specialty indicators (Supertrend, Donchian, etc.)
Use ta.exrem() to clean signals (always .fillna(False) before exrem)
Define sensible parameter ranges for the chosen strategy
Use loop-based optimization to collect multiple metrics per combo
Track: total_return, sharpe_ratio, max_drawdown, trade_count for each combination
Use tqdm for progress bars
Indian delivery fees: fees=0.00111, fixed_fees=20 for delivery equity
Find best parameters by total return AND by Sharpe ratio
Print top 10 results for both criteria
Generate Plotly heatmap of total return across parameter grid (template="plotly_dark")
Generate Plotly heatmap of Sharpe ratio across parameter grid
Fetch NIFTY benchmark and compare best parameters vs benchmark
Print Strategy vs Benchmark comparison table
Explain results in plain language for normal traders
Save results to CSV
Never use icons/emojis in code or logger output
For futures symbols, use lot-size-aware sizing:
NIFTY: min_size=65, size_granularity=65
BANKNIFTY: min_size=30, size_granularity=30
Default Parameter Ranges
Strategy	Parameter 1	Parameter 2
ema-crossover	fast EMA: 5-50	slow EMA: 10-60
rsi	window: 5-30	oversold: 20-40
donchian	period: 5-50	-
supertrend	period: 5-30	multiplier: 1.0-5.0
Example Usage

/optimize ema-crossover RELIANCE NSE D /optimize rsi SBIN

Weekly Installs
796
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
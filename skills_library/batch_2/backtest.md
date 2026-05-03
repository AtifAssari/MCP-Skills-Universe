---
title: backtest
url: https://skills.sh/marketcalls/vectorbt-backtesting-skills/backtest
---

# backtest

skills/marketcalls/vectorbt-backtesting-skills/backtest
backtest
Installation
$ npx skills add https://github.com/marketcalls/vectorbt-backtesting-skills --skill backtest
Summary

Generate complete VectorBT backtesting scripts with data fetch, signals, stats, and plots.

Supports 10+ pre-built strategies (EMA crossover, RSI, Donchian, Supertrend, MACD, SDA2, momentum, and more) with template-based script generation
Fetches data from OpenAlgo API or loads directly from DuckDB; auto-detects Historify vs custom formats
Uses TA-Lib for standard indicators and OpenAlgo ta for specialty indicators (Supertrend, Donchian, Ichimoku); includes signal deduplication via exrem()
Generates portfolio stats, strategy vs NIFTY benchmark comparison table, QuantStats HTML tearsheet, Plotly equity/drawdown charts, and CSV trade exports
Handles Indian delivery fees (0.111% + ₹20 fixed) and F&O lot-size constraints (NIFTY 65, BANKNIFTY 30)
SKILL.md

Create a complete VectorBT backtest script for the user.

Arguments

Parse $ARGUMENTS as: strategy symbol exchange interval

$0 = strategy name (e.g., ema-crossover, rsi, donchian, supertrend, macd, sda2, momentum)
$1 = symbol (e.g., SBIN, RELIANCE, NIFTY). Default: SBIN
$2 = exchange (e.g., NSE, NFO). Default: NSE
$3 = interval (e.g., D, 1h, 5m). Default: D

If no arguments, ask the user which strategy they want.

Instructions
Read the vectorbt-expert skill rules for reference patterns
Create backtesting/{strategy_name}/ directory if it doesn't exist (on-demand)
Create a .py file in backtesting/{strategy_name}/ named {symbol}_{strategy}_backtest.py
Use the matching template from rules/assets/{strategy}/backtest.py as the starting point
The script must:
Load .env from the project root using find_dotenv() (walks up from script dir automatically)
Fetch data via client.history() from OpenAlgo
If user provides a DuckDB path, load data directly via duckdb.connect(path, read_only=True) instead of OpenAlgo API. Auto-detect format: Historify (market_data table, epoch timestamps) vs custom (ohlcv table, date+time). See vectorbt-expert rules/duckdb-data.md.
If openalgo.ta is not importable (standalone DuckDB), use inline exrem() fallback.
Use TA-Lib for ALL indicators (EMA, SMA, RSI, MACD, BBands, ATR, ADX, STDDEV, MOM)
Use OpenAlgo ta for specialty indicators (Supertrend, Donchian, Ichimoku, HMA, KAMA, ALMA)
Use ta.exrem() to clean duplicate signals (always .fillna(False) before exrem)
Run vbt.Portfolio.from_signals() with min_size=1, size_granularity=1
Indian delivery fees: fees=0.00111, fixed_fees=20 for delivery equity
Fetch NIFTY benchmark via OpenAlgo (symbol="NIFTY", exchange="NSE_INDEX")
Print full pf.stats()
Print Strategy vs Benchmark comparison table (Total Return, Sharpe, Sortino, Max DD, Win Rate, Trades, Profit Factor)
Explain the backtest report in plain language for normal traders
Generate QuantStats HTML tearsheet if quantstats is available
Plot equity curve + drawdown using Plotly (template="plotly_dark")
Export trades to CSV
Never use icons/emojis in code or logger output
For futures symbols (NIFTY, BANKNIFTY), use lot-size-aware sizing:
NIFTY: min_size=65, size_granularity=65 (effective 31 Dec 2025)
BANKNIFTY: min_size=30, size_granularity=30
Use fees=0.00018, fixed_fees=20 for F&O futures
Available Strategies
Strategy	Keyword	Template
EMA Crossover	ema-crossover	assets/ema_crossover/backtest.py
RSI	rsi	assets/rsi/backtest.py
Donchian Channel	donchian	assets/donchian/backtest.py
Supertrend	supertrend	assets/supertrend/backtest.py
MACD Breakout	macd	assets/macd/backtest.py
SDA2	sda2	assets/sda2/backtest.py
Momentum	momentum	assets/momentum/backtest.py
Dual Momentum	dual-momentum	assets/dual_momentum/backtest.py
Buy & Hold	buy-hold	assets/buy_hold/backtest.py
RSI Accumulation	rsi-accumulation	assets/rsi_accumulation/backtest.py
Benchmark Rules
Default: NIFTY 50 via OpenAlgo (symbol="NIFTY", exchange="NSE_INDEX")
If user specifies a different benchmark, use that instead
For yfinance: use ^NSEI for India, ^GSPC (S&P 500) for US markets
Always compare: Total Return, Sharpe, Sortino, Max Drawdown
Example Usage

/backtest ema-crossover RELIANCE NSE D /backtest rsi SBIN /backtest supertrend NIFTY NFO 5m

Weekly Installs
1.1K
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
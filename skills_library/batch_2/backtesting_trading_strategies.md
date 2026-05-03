---
title: backtesting-trading-strategies
url: https://skills.sh/gracefullight/stock-checker/backtesting-trading-strategies
---

# backtesting-trading-strategies

skills/gracefullight/stock-checker/backtesting-trading-strategies
backtesting-trading-strategies
Originally fromjeremylongshore/claude-code-plugins-plus-skills
Installation
$ npx skills add https://github.com/gracefullight/stock-checker --skill backtesting-trading-strategies
Summary

Backtest crypto and traditional trading strategies against historical market data.

Includes 8 pre-built strategies (SMA, EMA, RSI, MACD, Bollinger Bands, Breakout, Mean Reversion, Momentum) with customizable parameters
Calculates comprehensive performance metrics: Sharpe, Sortino, Calmar ratios, max drawdown, VaR, volatility, win rate, and profit factor
Supports parameter grid search optimization to find best-performing configurations across strategy parameters
Generates trade-by-trade analysis, equity curves, and visual charts saved to reports directory
Fetches and caches historical data from yfinance; configurable commission, slippage, and position sizing
SKILL.md
Backtesting Trading Strategies
Overview

Validate trading strategies against historical data before risking real capital. This skill provides a complete backtesting framework with 8 built-in strategies, comprehensive performance metrics, and parameter optimization.

Key Features:

8 pre-built trading strategies (SMA, EMA, RSI, MACD, Bollinger, Breakout, Mean Reversion, Momentum)
Full performance metrics (Sharpe, Sortino, Calmar, VaR, max drawdown)
Parameter grid search optimization
Equity curve visualization
Trade-by-trade analysis
Prerequisites

Install required dependencies:

pip install pandas numpy yfinance matplotlib


Optional for advanced features:

pip install ta-lib scipy scikit-learn

Instructions
Step 1: Fetch Historical Data
python {baseDir}/scripts/fetch_data.py --symbol BTC-USD --period 2y --interval 1d


Data is cached to {baseDir}/data/{symbol}_{interval}.csv for reuse.

Step 2: Run Backtest

Basic backtest with default parameters:

python {baseDir}/scripts/backtest.py --strategy sma_crossover --symbol BTC-USD --period 1y


Advanced backtest with custom parameters:

# Example: backtest with specific date range
python {baseDir}/scripts/backtest.py \
  --strategy rsi_reversal \
  --symbol ETH-USD \
  --period 1y \
  --capital 10000 \
  --params '{"period": 14, "overbought": 70, "oversold": 30}'

Step 3: Analyze Results

Results are saved to {baseDir}/reports/ including:

*_summary.txt - Performance metrics
*_trades.csv - Trade log
*_equity.csv - Equity curve data
*_chart.png - Visual equity curve
Step 4: Optimize Parameters

Find optimal parameters via grid search:

python {baseDir}/scripts/optimize.py \
  --strategy sma_crossover \
  --symbol BTC-USD \
  --period 1y \
  --param-grid '{"fast_period": [10, 20, 30], "slow_period": [50, 100, 200]}'

Output
Performance Metrics
Metric	Description
Total Return	Overall percentage gain/loss
CAGR	Compound annual growth rate
Sharpe Ratio	Risk-adjusted return (target: >1.5)
Sortino Ratio	Downside risk-adjusted return
Calmar Ratio	Return divided by max drawdown
Risk Metrics
Metric	Description
Max Drawdown	Largest peak-to-trough decline
VaR (95%)	Value at Risk at 95% confidence
CVaR (95%)	Expected loss beyond VaR
Volatility	Annualized standard deviation
Trade Statistics
Metric	Description
Total Trades	Number of round-trip trades
Win Rate	Percentage of profitable trades
Profit Factor	Gross profit divided by gross loss
Expectancy	Expected value per trade
Example Output
================================================================================
                    BACKTEST RESULTS: SMA CROSSOVER
                    BTC-USD | [start_date] to [end_date]
================================================================================
 PERFORMANCE                          | RISK
 Total Return:        +47.32%         | Max Drawdown:      -18.45%
 CAGR:                +47.32%         | VaR (95%):         -2.34%
 Sharpe Ratio:        1.87            | Volatility:        42.1%
 Sortino Ratio:       2.41            | Ulcer Index:       8.2
--------------------------------------------------------------------------------
 TRADE STATISTICS
 Total Trades:        24              | Profit Factor:     2.34
 Win Rate:            58.3%           | Expectancy:        $197.17
 Avg Win:             $892.45         | Max Consec. Losses: 3
================================================================================

Supported Strategies
Strategy	Description	Key Parameters
sma_crossover	Simple moving average crossover	fast_period, slow_period
ema_crossover	Exponential MA crossover	fast_period, slow_period
rsi_reversal	RSI overbought/oversold	period, overbought, oversold
macd	MACD signal line crossover	fast, slow, signal
bollinger_bands	Mean reversion on bands	period, std_dev
breakout	Price breakout from range	lookback, threshold
mean_reversion	Return to moving average	period, z_threshold
momentum	Rate of change momentum	period, threshold
Configuration

Create {baseDir}/config/settings.yaml:

data:
  provider: yfinance
  cache_dir: ./data

backtest:
  default_capital: 10000
  commission: 0.001     # 0.1% per trade
  slippage: 0.0005      # 0.05% slippage

risk:
  max_position_size: 0.95
  stop_loss: null       # Optional fixed stop loss
  take_profit: null     # Optional fixed take profit

Error Handling

See {baseDir}/references/errors.md for common issues and solutions.

Examples

See {baseDir}/references/examples.md for detailed usage examples including:

Multi-asset comparison
Walk-forward analysis
Parameter optimization workflows
Files
File	Purpose
scripts/backtest.py	Main backtesting engine
scripts/fetch_data.py	Historical data fetcher
scripts/strategies.py	Strategy definitions
scripts/metrics.py	Performance calculations
scripts/optimize.py	Parameter optimization
Resources
yfinance - Yahoo Finance data
TA-Lib - Technical analysis library
QuantStats - Portfolio analytics
Weekly Installs
1.2K
Repository
gracefullight/s…-checker
GitHub Stars
18
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
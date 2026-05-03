---
rating: ⭐⭐⭐
title: fin-guru-quant-analysis
url: https://skills.sh/aojdevstudio/finance-guru/fin-guru-quant-analysis
---

# fin-guru-quant-analysis

skills/aojdevstudio/finance-guru/fin-guru-quant-analysis
fin-guru-quant-analysis
Installation
$ npx skills add https://github.com/aojdevstudio/finance-guru --skill fin-guru-quant-analysis
SKILL.md
Quantitative Analysis Skill

Execute structured quantitative analysis workflows with statistical validation.

Workflow Steps
Plan — Define statistical modeling objectives, metrics, and assumptions
Data Validation — Use data_validator_cli.py for statistical validity (outliers, gaps, splits)
Risk Metrics — Use risk_metrics_cli.py for VaR/CVaR/Sharpe/Sortino/Drawdown (minimum 90 days)
Momentum Analysis — Use momentum_cli.py for confluence analysis
Volatility Metrics — Use volatility_cli.py for regime analysis
Correlation Analysis — Use correlation_cli.py for diversification and covariance matrices
Factor Analysis — Use factors_cli.py for Fama-French 3-factor, Carhart 4-factor models
Strategy Validation — Use backtester_cli.py with transaction costs and realistic slippage
Portfolio Optimization — Use optimizer_cli.py for mean-variance, risk parity, max Sharpe, Black-Litterman
CLI Commands
# Risk metrics
uv run python src/analysis/risk_metrics_cli.py TICKER --days 252 --benchmark SPY

# Momentum confluence
uv run python src/utils/momentum_cli.py TICKER --days 90

# Volatility regime
uv run python src/utils/volatility_cli.py TICKER --days 90

# Correlation matrix
uv run python src/analysis/correlation_cli.py TICKER1 TICKER2 --days 90

# Factor analysis
uv run python src/analysis/factors_cli.py TICKER --days 252 --benchmark SPY

# Backtesting
uv run python src/strategies/backtester_cli.py TICKER --days 252 --strategy rsi

# Portfolio optimization
uv run python src/strategies/optimizer_cli.py TICKERS --days 252 --method max_sharpe

Requirements
Start with clear statistical plan and obtain consent before execution
Validate all assumptions against compliance policies
Apply robust methods with proper confidence intervals
All market data must be timestamped and verified against current date
Minimum 90 days of data for robust statistics
Weekly Installs
16
Repository
aojdevstudio/fi…nce-guru
GitHub Stars
303
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
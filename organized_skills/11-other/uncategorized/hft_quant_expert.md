---
rating: ⭐⭐⭐
title: hft-quant-expert
url: https://skills.sh/kasyap1234/delta-go/hft-quant-expert
---

# hft-quant-expert

skills/kasyap1234/delta-go/hft-quant-expert
hft-quant-expert
Installation
$ npx skills add https://github.com/kasyap1234/delta-go --skill hft-quant-expert
SKILL.md
HFT Quant Expert

Quantitative trading expertise for DeFi and crypto derivatives.

When to Use
Building trading strategies and signals
Implementing risk management
Calculating position sizes
Backtesting strategies
Analyzing volatility and correlations
Workflow
Step 1: Define Signal

Calculate z-score or other entry signal.

Step 2: Size Position

Use Kelly Criterion (0.25x) for position sizing.

Step 3: Validate Backtest

Check for lookahead bias, survivorship bias, overfitting.

Step 4: Account for Costs

Include gas + slippage in profit calculations.

Quick Formulas
# Z-score
zscore = (value - rolling_mean) / rolling_std

# Sharpe (annualized)
sharpe = np.sqrt(252) * returns.mean() / returns.std()

# Kelly fraction (use 0.25x)
kelly = (win_prob * win_loss_ratio - (1 - win_prob)) / win_loss_ratio

# Half-life of mean reversion
half_life = -np.log(2) / lambda_coef

Common Pitfalls
Lookahead bias - Using future data
Survivorship bias - Only existing assets
Overfitting - Too many parameters
Ignoring costs - Gas + slippage
Wrong annualization - 252 daily, 365*24 hourly
Weekly Installs
204
Repository
kasyap1234/delta-go
GitHub Stars
1
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
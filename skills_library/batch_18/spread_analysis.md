---
title: spread-analysis
url: https://skills.sh/staskh/trading_skills/spread-analysis
---

# spread-analysis

skills/staskh/trading_skills/spread-analysis
spread-analysis
Installation
$ npx skills add https://github.com/staskh/trading_skills --skill spread-analysis
SKILL.md
Spread Analysis

Analyze multi-leg option strategies.

Instructions

Note: If uv is not installed or pyproject.toml is not found, replace uv run python with python in all commands below.

uv run python scripts/spreads.py SYMBOL --strategy STRATEGY --expiry YYYY-MM-DD [options]

Strategies and Options

Vertical Spread (bull/bear call/put spread):

uv run python scripts/spreads.py AAPL --strategy vertical --expiry 2026-01-16 --type call --long-strike 180 --short-strike 185


Straddle (long call + long put at same strike):

uv run python scripts/spreads.py AAPL --strategy straddle --expiry 2026-01-16 --strike 180


Strangle (long call + long put at different strikes):

uv run python scripts/spreads.py AAPL --strategy strangle --expiry 2026-01-16 --put-strike 175 --call-strike 185


Iron Condor (sell strangle + buy wider strangle):

uv run python scripts/spreads.py AAPL --strategy iron-condor --expiry 2026-01-16 --put-short 175 --put-long 170 --call-short 185 --call-long 190

Output

Returns JSON with:

strategy - Strategy name and legs
cost - Net debit or credit
max_profit - Maximum potential profit
max_loss - Maximum potential loss
breakeven - Breakeven price(s)
probability - Estimated probability of profit (based on IV)

Explain the risk/reward and when this strategy is appropriate.

Dependencies
pandas
yfinance
Weekly Installs
31
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
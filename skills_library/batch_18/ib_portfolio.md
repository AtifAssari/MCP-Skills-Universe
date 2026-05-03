---
title: ib-portfolio
url: https://skills.sh/staskh/trading_skills/ib-portfolio
---

# ib-portfolio

skills/staskh/trading_skills/ib-portfolio
ib-portfolio
Installation
$ npx skills add https://github.com/staskh/trading_skills --skill ib-portfolio
SKILL.md
IB Portfolio

Fetch current portfolio positions from Interactive Brokers.

Prerequisites

User must have TWS or IB Gateway running locally with API enabled:

Paper trading: port 7497
Live trading: port 7496
Instructions

Note: If uv is not installed or pyproject.toml is not found, replace uv run python with python in all commands below.

uv run python scripts/portfolio.py [--port PORT]

Arguments
--port - IB port (default: 7496 for live trading)
--account - Specific IB account ID (optional, defaults to first account)
Output

Returns JSON with:

connected - Whether connection succeeded
positions - Array of positions with symbol, quantity, avg_cost, market_value, unrealized_pnl

If not connected, explain that TWS/Gateway needs to be running.

Dependencies
ib-async
Weekly Installs
39
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
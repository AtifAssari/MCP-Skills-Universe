---
rating: ⭐⭐
title: ib-account
url: https://skills.sh/staskh/trading_skills/ib-account
---

# ib-account

skills/staskh/trading_skills/ib-account
ib-account
Installation
$ npx skills add https://github.com/staskh/trading_skills --skill ib-account
SKILL.md
IB Account

Fetch account summary from Interactive Brokers.

Prerequisites

User must have TWS or IB Gateway running locally with API enabled:

Paper trading: port 7497
Live trading: port 7496
Instructions

Note: If uv is not installed or pyproject.toml is not found, replace uv run python with python in all commands below.

uv run python scripts/account.py [--port PORT] [--account ACCOUNT_ID] [--all-accounts]

Arguments
--port - IB port (default: 7496 for live trading)
--account - Specific account ID to fetch
--all-accounts - Fetch summaries for all managed accounts

Default behavior (no flags): fetches the first managed account only. Always use --all-accounts unless the user asks for a specific account.

Output

Returns JSON with:

connected - Whether connection succeeded
accounts - List of account summaries, each with account ID, net liquidation, cash, buying power, etc.

If not connected, explain that TWS/Gateway needs to be running.

Dependencies
ib-async
Weekly Installs
34
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
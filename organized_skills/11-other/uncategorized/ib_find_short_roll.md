---
rating: ⭐⭐⭐
title: ib-find-short-roll
url: https://skills.sh/staskh/trading_skills/ib-find-short-roll
---

# ib-find-short-roll

skills/staskh/trading_skills/ib-find-short-roll
ib-find-short-roll
Installation
$ npx skills add https://github.com/staskh/trading_skills --skill ib-find-short-roll
SKILL.md
IB Find Short Roll

Analyze roll options for short positions or find best short options to open against long stock using real-time data from Interactive Brokers.

Prerequisites

User must have TWS or IB Gateway running locally with API enabled:

Paper trading: port 7497
Live trading: port 7496
Instructions
Step 1: Gather Data

Note: If uv is not installed or pyproject.toml is not found, replace uv run python with python in all commands below.

uv run python scripts/roll.py SYMBOL [--strike STRIKE] [--expiry YYYYMMDD] [--right C|P] [--port PORT] [--account ACCOUNT]


The script returns JSON to stdout with all position and candidate data.

Step 2: Format Report

Read templates/markdown-template.md for formatting instructions. Generate a markdown report from the JSON data and save to sandbox/.

Step 3: Report Results

Present key findings to the user: recommended position, credit/debit, and the saved report path.

Behavior
If short option position exists (mode: "roll"): Analyzes roll candidates to different expirations/strikes
If long option position exists (mode: "spread"): Finds best short call/put to create a vertical spread
If long stock exists (mode: "new_short"): Finds best covered call (or protective put) to open
If none of the above: Returns error (use --strike/--expiry to specify manually)
Arguments
SYMBOL - Ticker symbol (e.g., GOOG, AAPL, TSLA)
--strike - Current short strike price (optional, auto-detects from portfolio)
--expiry - Current short expiration in YYYYMMDD format (optional, auto-detects)
--right - Option type: C for call, P for put (default: C)
--port - IB port (default: 7496 for live trading)
--account - Specific account ID (optional)
JSON Output

The script outputs JSON with mode field indicating the analysis type:

Common Fields
success - Boolean
generated - Timestamp
mode - "roll", "spread", or "new_short"
symbol - Ticker
underlying_price - Current stock price
earnings_date - Next earnings date or null
expirations_analyzed - List of expiry dates checked
Mode-specific Fields
roll: current_position, buy_to_close, roll_candidates (dict of expiry -> candidates)
spread: long_option, right, candidates_by_expiry
new_short: long_position, right, candidates_by_expiry
Example Usage
# Auto-detect GOOG position (short option, long option, or long stock)
uv run python scripts/roll.py GOOG --port 7496

# Specify exact short position to roll
uv run python scripts/roll.py GOOG --strike 350 --expiry 20260206 --right C

# Find short call to sell against long call (vertical spread)
uv run python scripts/roll.py AUR --right C

# Find covered put for long stock
uv run python scripts/roll.py TSLA --right P

Dependencies
ib-async
yfinance
Weekly Installs
28
Repository
staskh/trading_skills
GitHub Stars
139
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
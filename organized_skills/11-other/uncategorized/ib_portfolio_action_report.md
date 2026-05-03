---
rating: ⭐⭐⭐
title: ib-portfolio-action-report
url: https://skills.sh/staskh/trading_skills/ib-portfolio-action-report
---

# ib-portfolio-action-report

skills/staskh/trading_skills/ib-portfolio-action-report
ib-portfolio-action-report
Installation
$ npx skills add https://github.com/staskh/trading_skills --skill ib-portfolio-action-report
SKILL.md
IB Portfolio Action Report

Generate a comprehensive portfolio action report that analyzes all positions across Interactive Brokers accounts, fetches earnings dates, and provides traffic-light risk indicators (🔴🟡🟢) for each position.

Prerequisites

User must have TWS or IB Gateway running locally with API enabled:

Paper trading: port 7497
Live trading: port 7496
Instructions
Step 1: Gather Data

Note: If uv is not installed or pyproject.toml is not found, replace uv run python with python in all commands below.

uv run python scripts/report.py [--port PORT] [--account ACCOUNT]


The script returns JSON to stdout with analyzed portfolio data including risk levels, earnings dates, technical indicators, and spread groupings.

Step 2: Format Report

Read templates/markdown-template.md for formatting instructions. Generate a markdown report from the JSON data and save to sandbox/.

Filename: ib_portfolio_action_report_{ACCOUNT}_{YYYY-MM-DD}_{HHmm}.md

Step 3: Report Results

Present critical findings to the user: red/yellow items requiring attention, top priority actions, and the saved report path.

Arguments
--port - IB port (default: 7496 for live trading)
--account - Specific account ID to analyze (optional, defaults to all accounts)
JSON Output

The script returns structured JSON with:

generated - Timestamp
accounts - List of account IDs
summary - Red/yellow/green counts
spreads - All positions grouped into spreads with risk level, urgency, and recommendations
technicals - Technical indicators per symbol (RSI, trend, SMAs, MACD, ADX)
earnings - Earnings dates per symbol
prices - Current prices per symbol
earnings_calendar - Upcoming earnings with account/position info
account_summary - Position and risk counts per account
Report Sections
Critical Summary: Count of positions by risk level (🔴/🟡/🟢)
Immediate Action Required: Positions expiring within 2 days
Urgent - Expiring Within 1 Week: Short-term positions needing attention
Critical Earnings Alert: Positions with earnings this week
Earnings Next Week: Upcoming earnings exposure
Expiring in 2 Weeks: Medium-term expirations
Longer-Dated Positions: Core holdings with spread analysis
Top Priority Actions: Numbered action items by urgency
Position Size Summary: Account-level breakdown
Earnings Calendar: Next 30 days of earnings dates
Technical Analysis Summary: RSI, trend, SMAs, MACD, ADX for each underlying
Example Usage
# All accounts on live trading port
uv run python scripts/report.py --port 7496

# Specific account
uv run python scripts/report.py --port 7496 --account U790497

Dependencies
ib-async
pandas-ta
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
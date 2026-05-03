---
title: mt5-trading
url: https://skills.sh/epinvest516-web/openclaw-skills/mt5-trading
---

# mt5-trading

skills/epinvest516-web/openclaw-skills/mt5-trading
mt5-trading
Installation
$ npx skills add https://github.com/epinvest516-web/openclaw-skills --skill mt5-trading
SKILL.md
MT5 Trading System Management (Babata V6.6 Predator Edition)

This skill consolidates the highest-level quant logic for Gold/Silver trading on Windows VPS.

🚀 V6.6 Core Features (The Predator)
1. 🚀 Infinite RR Logic (Smart Trailing)
Phase 1 (Breakeven): Move SL to Entry + buffer once Profit >= 2.0 * Initial Risk.
Phase 2 (Moon Run): Remove fixed TP. Trail SL behind the previous M15 bar's low/high.
Goal: Capture 1:10+ outliers while securing 0-loss trades early.
2. 🧠 Self-Evolution (Blacklist System)
Review: Weekly automated analysis of journal.csv.
Action: Identifies low-win-rate time/day clusters and generates blacklist.json.
Filtering: Automatically skips entry during blacklisted intervals.
3. 🌪️ Triple-Resonance Selector

Entries require 3 layers of alignment:

H4 Macro Trend (EMA200 / Structure).
M15 Micro Signal (SMC, NakedK, Turtle, Vegas).
MACD Momentum (Histogram direction).
4. 📊 Blackbox Data Logging

Full technical context for every trade is stored in journal.csv for post-mortem analysis.

🛠️ Deployment Checklist
Environment: pip install MetaTrader5 pandas requests pytz.
Files: main.py, config.py, engine/, strategies/.
Supervisor: Always run via START_BOT.cmd to ensure auto-restart.
Sync: Commit and push to Github repository for version control.
🔍 Verification
Telegram: Confirm receipt of "🐺 Babata V6.6 Predator Active!" message.
Journal: Ensure journal.csv is being populated after the first trade.
Weekly Installs
126
Repository
epinvest516-web…w-skills
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
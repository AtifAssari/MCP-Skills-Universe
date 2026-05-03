---
rating: ⭐⭐⭐
title: polymarket-paper-trader
url: https://skills.sh/mjunaidca/polymarket-skills/polymarket-paper-trader
---

# polymarket-paper-trader

skills/mjunaidca/polymarket-skills/polymarket-paper-trader
polymarket-paper-trader
Installation
$ npx skills add https://github.com/mjunaidca/polymarket-skills --skill polymarket-paper-trader
SKILL.md
Polymarket Paper Trading Engine

Simulate trades against live Polymarket prices with zero financial risk. No wallet, no keys, no money at stake. Portfolio persists across sessions in SQLite.

Quick Start
Initialize a Portfolio
python ~/.agents/skills/polymarket-paper-trader/scripts/paper_engine.py --action init --balance 1000

Buy Shares (Market Order)
# Buy $50 of YES shares using live order book prices
python ~/.agents/skills/polymarket-paper-trader/scripts/paper_engine.py \
  --action buy --token TOKEN_ID --side YES --size 50 \
  --reason "High confidence based on news analysis"

Buy Shares (Limit Order)
python ~/.agents/skills/polymarket-paper-trader/scripts/paper_engine.py \
  --action buy --token TOKEN_ID --side YES --size 50 --price 0.45 \
  --reason "Value buy below fair price estimate"

Check Portfolio
python ~/.agents/skills/polymarket-paper-trader/scripts/paper_engine.py --action portfolio
python ~/.agents/skills/polymarket-paper-trader/scripts/paper_engine.py --action portfolio --json

Close a Position
python ~/.agents/skills/polymarket-paper-trader/scripts/paper_engine.py \
  --action close --token TOKEN_ID --reason "Taking profit"

View Trade History
python ~/.agents/skills/polymarket-paper-trader/scripts/paper_engine.py --action trades

Performance Report
python ~/.agents/skills/polymarket-paper-trader/scripts/portfolio_report.py
python ~/.agents/skills/polymarket-paper-trader/scripts/portfolio_report.py --json

Portfolio Health Check (Session Start)
python ~/.agents/skills/polymarket-paper-trader/scripts/health_check.py
python ~/.agents/skills/polymarket-paper-trader/scripts/health_check.py --json


Runs the full session-start workflow in one command: loads portfolio, fetches live prices, updates DB, calculates drawdown, checks stop losses, evaluates all risk limits. Returns GREEN/YELLOW/RED status.

Finding Token IDs

Token IDs come from the Polymarket Gamma API. To find them for a market:

# Search for markets
curl -s 'https://gamma-api.polymarket.com/markets?limit=5&active=true&closed=false&order=volume24hr&ascending=false' | python3 -c "
import sys, json
for m in json.load(sys.stdin):
    tokens = json.loads(m['clobTokenIds'])
    prices = json.loads(m['outcomePrices'])
    print(f\"{m['question'][:60]}\")
    print(f\"  YES token: {tokens[0]}  price: {prices[0]}\")
    print(f\"  NO  token: {tokens[1]}  price: {prices[1]}\")
    print()
"


Or use the polymarket-scanner skill to discover markets first.

Execute Strategy Recommendations

The executor takes structured recommendations from strategy advisors:

python ~/.agents/skills/polymarket-paper-trader/scripts/execute_paper.py \
  --recommendation '{
    "token_id": "TOKEN_ID",
    "side": "YES",
    "action": "BUY",
    "size_usd": 50,
    "confidence": 0.75,
    "reasoning": "Momentum signal detected",
    "strategy": "momentum"
  }'


Dry run (validates without executing):

python ~/.agents/skills/polymarket-paper-trader/scripts/execute_paper.py \
  --recommendation '{"token_id":"TOKEN","side":"YES","size_usd":50}' --dry-run

Risk Rules (Built In)
Rule	Default	Purpose
Max position size	10% of portfolio	No single bet too large
Max drawdown	30%	Stop trading if losing too much
Max concurrent positions	5	Diversification
Daily loss limit	5% of starting balance	Prevent tilt
Max single market exposure	20% of portfolio	No concentration
Human approval threshold	15% of portfolio	Large trades need confirmation

Override with --force flag or by passing custom risk_config on init.

How It Works
Real prices: Fetches live order book from clob.polymarket.com
Book walking: Market orders simulate fills by walking the order book (not mid-price)
Fee modeling: Default 0% (most markets), configurable for crypto markets
SQLite persistence: Portfolio at ~/.polymarket-paper/portfolio.db
Risk engine: Every trade validated against configurable risk rules
API Reference

All scripts support --json for machine-readable output. Key Python functions:

paper_engine.init_portfolio(balance, name) — Create portfolio
paper_engine.place_order(token_id, side, size, price) — Execute trade
paper_engine.close_position(token_id) — Close position
paper_engine.get_portfolio(name) — Get current state
paper_engine.get_trades(name) — Trade history
execute_paper.execute_recommendation(rec) — Execute strategy signal
portfolio_report.generate_report(name) — Full analytics

See references/risk-rules.md for detailed risk parameters and references/paper-trading-guide.md for the full paper trading guide.

Weekly Installs
79
Repository
mjunaidca/polym…t-skills
GitHub Stars
17
First Seen
Mar 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketFail
SnykWarn
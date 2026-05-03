---
rating: ⭐⭐⭐
title: polymarket-live-executor
url: https://skills.sh/mjunaidca/polymarket-skills/polymarket-live-executor
---

# polymarket-live-executor

skills/mjunaidca/polymarket-skills/polymarket-live-executor
polymarket-live-executor
Installation
$ npx skills add https://github.com/mjunaidca/polymarket-skills --skill polymarket-live-executor
SKILL.md
Polymarket Live Executor

Execute real trades on Polymarket with mandatory human-in-the-loop confirmation. This skill requires L2 authentication (wallet private key) and enforces strict safety controls on every operation.

SAFETY REQUIREMENTS

Every trade requires explicit user confirmation. The agent must:

Display full trade details (market, side, size, price, estimated cost)
Show current order book context (spread, depth at target price)
Wait for the user to type "yes" or "confirm" before proceeding
Never batch or auto-confirm trades

Environment safeguards (enforced by all scripts):

POLYMARKET_PRIVATE_KEY must be set (burner wallet only -- NEVER a main wallet)
POLYMARKET_CONFIRM=true must be set to enable any trade execution
Position size hard-capped (default $10, configurable via POLYMARKET_MAX_SIZE)
Daily loss limit tracked in ~/.polymarket-live/trades.log
Setup

Use the setup wizard to configure everything:

# Step 1: Create a burner wallet
python scripts/setup_wallet.py --create

# Step 2: Fund wallet with USDC on Polygon (manually via MetaMask/bridge)

# Step 3: Copy and fill in .env
cp .env.example .env && chmod 600 .env
# Edit .env with your private key and limits

# Step 4: Verify everything is configured
python scripts/setup_wallet.py --verify

# Step 5: Check on-chain balance
python scripts/setup_wallet.py --check-balance


Or set environment variables manually:

export POLYMARKET_PRIVATE_KEY="0x..."    # Burner wallet only!
export POLYMARKET_CONFIRM=true           # Safety gate
export POLYMARKET_MAX_SIZE=10            # Max $ per trade (default: 10)
export POLYMARKET_DAILY_LOSS_LIMIT=50    # Max daily loss (default: 50)


Review the references/live-trading-checklist.md before any live trade.

Available Scripts
1. Execute Trade (scripts/execute_live.py)

Place a real order on Polymarket.

# Limit order: buy 5 YES shares at $0.60
python scripts/execute_live.py --token-id <ID> --side BUY --size 5 --price 0.60

# Market order: buy $5 worth at market price
python scripts/execute_live.py --token-id <ID> --side BUY --amount 5 --market

# Sell: sell 10 shares at $0.75
python scripts/execute_live.py --token-id <ID> --side SELL --size 10 --price 0.75


The script will display full trade details and require interactive confirmation.

2. Check Positions (scripts/check_positions.py)

View wallet balance, open orders, and trade history.

python scripts/check_positions.py                # Summary
python scripts/check_positions.py --orders        # Open orders
python scripts/check_positions.py --trades        # Recent trades
python scripts/check_positions.py --balance       # USDC balance

Workflow
Run analysis with polymarket-analyzer scripts to find opportunities
Paper-trade the idea with polymarket-paper-trader first
Review references/live-trading-checklist.md
Set up environment variables and burner wallet
Use check_positions.py to verify wallet state
Execute trade with execute_live.py -- confirm when prompted
Monitor position with check_positions.py
Risk Controls
All trades logged to ~/.polymarket-live/trades.log
Daily P&L tracked and enforced against loss limit
Position size caps prevent oversized trades
No autonomous execution -- every trade needs human approval
Important Disclaimers
This skill executes REAL trades with REAL money
Use only with burner wallets funded with money you can afford to lose
Past analysis does not guarantee future results
Not financial advice -- you are solely responsible for your trades
Weekly Installs
75
Repository
mjunaidca/polym…t-skills
GitHub Stars
17
First Seen
Mar 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn
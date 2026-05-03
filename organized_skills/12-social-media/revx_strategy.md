---
rating: ⭐⭐⭐
title: revx-strategy
url: https://skills.sh/revolut-engineering/revolut-x-api/revx-strategy
---

# revx-strategy

skills/revolut-engineering/revolut-x-api/revx-strategy
revx-strategy
Installation
$ npx skills add https://github.com/revolut-engineering/revolut-x-api --skill revx-strategy
SKILL.md
Strategy: Grid Bot (revx strategy grid)

Backtest, optimize, and run automated grid trading strategies.

Auth required. Make sure revx is installed and configured before running these commands. If any command fails with an auth-related error — Auth not configured, No private key found, Authentication failed (401), Invalid signature, insecure permissions, or a missing key/config file at ~/.config/revolut-x/ — invoke the revx-auth skill immediately and apply the fix yourself. Do not interrupt the user to ask them to run setup. Only escalate to the user for steps only they can perform (pasting the API key, registering the public key in their Revolut X profile, choosing a passphrase). After the fix, retry the original command.

Symbols use BASE-QUOTE format with a dash: BTC-USD, ETH-EUR, SOL-USD.

Backtest

Test a grid strategy on historical data:

revx strategy grid backtest BTC-USD
revx strategy grid backtest BTC-USD --levels 10 --range 10 --investment 1000
revx strategy grid backtest ETH-USD --days 60 --interval 4h
revx strategy grid backtest BTC-USD --split
revx strategy grid backtest BTC-USD --json

Flag	Default	Description
--levels <n>	5	Grid levels per side (2-25)
--range <pct>	10	Grid range +/- % from mid price
--investment <amount>	1000	Capital in quote currency
--days <n>	3	Historical data period
--interval <res>	1m	Candle resolution
--split	off	Split investment across buy and sell levels (market-buy base for levels above start price)

Not long-running — completes and returns results. Run normally via the Bash tool.

Always confirm these key parameters before running: pair, investment, levels, range, and split mode. These affect capital and strategy behavior — never assume them silently. Other parameters (days, interval) can use defaults unless the user specifies otherwise.

Optimize

Test multiple parameter combinations, ranked by return:

revx strategy grid optimize BTC-USD
revx strategy grid optimize BTC-USD --investment 5000 --days 60
revx strategy grid optimize BTC-USD --levels 5,10,15,20 --ranges 3,5,10 --top 5
revx strategy grid optimize BTC-USD --split

Flag	Default	Description
--levels <csv>	3,5,8,10,15	Level counts to test
--ranges <csv>	3,5,7,10,12,15,20	Range percentages to test
--top <n>	10	Top results to display
--investment <amount>	1000	Capital in quote currency
--days <n>	3	Historical data period
--interval <res>	1m	Candle resolution
--split	off	Split investment across buy and sell levels (market-buy base for levels above start price)

Max 200 parameter combinations. Not long-running — completes and returns results.

Always confirm these key parameters before running: pair, investment, and split mode. These affect capital and strategy behavior — never assume them silently. Other parameters (levels list, ranges list, days, interval, top) can use defaults unless the user specifies otherwise.

Run (Live Trading)
Human Confirmation Required

NEVER execute revx strategy grid run (without --dry-run) without explicit user confirmation. This command places real orders with real money.

Before running a live grid bot, present a confirmation summary to the user:

Grid bot to launch:

Pair: BTC-USD
Investment: $500
Levels: 10 per side
Range: +/-5%
Mode: LIVE (real orders)

This will place real buy and sell orders. Shall I proceed?

Only execute after the user explicitly approves. --dry-run does not require confirmation (no real orders).

Always Suggest Dry Run First

When the user asks to run a live grid bot, always suggest starting with --dry-run before going live — unless the user has already completed a dry run in the current session or explicitly says they want to skip it.

Example response:

Before going live, I'd recommend a dry run first to verify the grid setup:

revx strategy grid run BTC-USD --investment 500 --levels 10 --range 5 --dry-run


This simulates the bot without placing real orders. Want to start with a dry run?

If the user confirms they want to skip the dry run, proceed to the live confirmation flow above.

Missing Parameters — Always Ask, Never Guess

The --investment flag is required by the CLI, but also confirm the user's intent for all key parameters:

Symbol — which pair?
Investment — how much capital?
Levels — how many grid levels per side? (default 5 if user says "use defaults")
Range — what percentage range? (default 5% if user says "use defaults")

If the user says "run a grid bot on BTC", ask for the investment amount at minimum.

Run a live grid bot with real-time dashboard:

revx strategy grid run BTC-USD --investment 500
revx strategy grid run BTC-USD --levels 10 --range 5 --investment 1000 --interval 15
revx strategy grid run BTC-USD --investment 500 --split
revx strategy grid run BTC-USD --investment 100 --dry-run
revx strategy grid run BTC-USD --investment 500 --reset

Flag	Default	Description
--investment <amount>	required	Capital in quote currency
--levels <n>	5	Grid levels per side (2-25)
--range <pct>	5	Grid range +/- % from mid
--split	off	Split investment across buy and sell levels (market-buy base for levels above current price)
--interval <sec>	10	Polling interval in seconds
--dry-run	off	Simulate without real orders
--reset	off	Discard saved state, start fresh

Ctrl+C for graceful shutdown (cancels open orders, prints summary).

Persistence: State auto-saved for crash recovery. Clean shutdown deletes state. Crashed sessions auto-reconcile on restart.

If Telegram connectors are configured (see revx-telegram skill), notifications are sent on startup, shutdown, fills, and P&L changes.

Long-Running Command — Behavioral Instructions for Claude

revx strategy grid run (including --dry-run) runs indefinitely as a continuous polling loop.

How to handle:

Run the command using the Bash tool with run_in_background: true — this frees Claude immediately while the process runs asynchronously
Periodically read the background task output file with the Read tool to monitor status and report key events to the user (orders placed, fills, errors)
If the user asks to stop, use the TaskStop tool with the task ID
Also print the command to the user so they can optionally run it in a separate terminal for the full live dashboard experience (with colors, real-time tables, Ctrl+C to stop)

Example — starting a grid bot:

Bash tool call:

{ "command": "revx strategy grid run BTC-USD --investment 500 --levels 10 --range 5", "run_in_background": true }


Response to user:

Started grid bot for BTC-USD in the background. I'll check for updates periodically.

If you'd like to see the live dashboard, run this in a separate terminal:

revx strategy grid run BTC-USD --investment 500 --levels 10 --range 5


Press Ctrl+C to stop (gracefully cancels open orders).

When to Suggest Split

When the user sets up a grid strategy (backtest, optimize, or run), ask whether they want split mode if they haven't specified --split. Present it as a simple choice with context:

Would you like to use split mode (--split)?

Without split — all capital goes to buy orders below the current price. Best for uptrending markets where you expect price to dip into buy levels and bounce back.
With split — capital is divided across both buy and sell levels. A market buy at the start price funds sell positions above. Best for ranging/sideways markets where price oscillates around the current level.

If the user is unsure, recommend running both variants in backtest/optimize to compare results.

Use --split consistently across backtest, optimize, dry-run, and live when the user has chosen split mode.

P&L Metrics

Realized P&L = sum of profit from each completed sell (sell revenue − cost per level). Measures pure grid trading profit. The initial split buy (if --split is used) does not affect this metric.

Total P&L = (final quote balance + final base × final price) − initial investment. The mark-to-market portfolio value change. No assets are force-sold at the end.

Without --split: only buy levels (below start price) are funded. In uptrending markets all grid cycles may complete, making Realized and Total P&L equal.

With --split: investment is divided across all levels. Levels above start price get positions via a simulated market buy at start price. This creates Realized/Total P&L divergence and allows profiting from both up and down moves within the grid.

Common Workflow: Backtest Then Run
# 1. Optimize to find best parameters
revx strategy grid optimize BTC-USD --investment 1000 --days 30

# 2. Backtest the top result
revx strategy grid backtest BTC-USD --levels 10 --range 7 --investment 1000

# 3. Dry run first
revx strategy grid run BTC-USD --investment 1000 --levels 10 --range 7 --dry-run

# 4. Go live
revx strategy grid run BTC-USD --investment 1000 --levels 10 --range 7


Use --split consistently across all steps if you want to test and run with split investment.

Related Skills
Skill	Purpose
revx-telegram	Get Telegram notifications for grid bot events
revx-market	Check prices and pair data before configuring a grid
revx-account	Check balances and order status
revx-trading	Manual order placement (grid bot places orders automatically)
revx-auth	API key setup and configuration
Weekly Installs
13
Repository
revolut-enginee…ut-x-api
GitHub Stars
9
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
---
title: deploy-bot
url: https://skills.sh/unarmedpuppy/polyjuiced/deploy-bot
---

# deploy-bot

skills/unarmedpuppy/polyjuiced/deploy-bot
deploy-bot
Installation
$ npx skills add https://github.com/unarmedpuppy/polyjuiced --skill deploy-bot
SKILL.md
Deploy Polymarket Bot

WARNING: ALWAYS USE THIS SKILL when deploying changes. Never use manual docker commands.

Safe deployment workflow for the Polymarket arbitrage trading bot that:

Runs regression tests to catch bugs before deployment
Checks for active trades to prevent interrupting pending positions
Why This Matters

The bot executes real-money arbitrage trades on Polymarket. Deploying broken code or restarting during active trades can cause:

Bugs: Untested code can break execution, tracking, or settlement
Lost visibility: Restarting during active trades loses pending position data
Missed resolutions: Container restart can miss market resolution events
Financial losses: All of the above can result in real money losses
Quick Deploy
# From the polyjuiced repo root
./.agents/skills/deploy-bot/deploy.sh

# Skip tests only (still checks active trades)
./.agents/skills/deploy-bot/deploy.sh --skip-tests

# Force deploy (DANGEROUS - skips ALL safety checks)
./.agents/skills/deploy-bot/deploy.sh --force

What the Script Does

Run Regression Tests (Step 0)

Builds a fresh container with latest code
Runs pytest tests/ -v to verify all tests pass
Blocks deployment if any tests fail
Exit code 3 = tests failed

Check Active Trades (Step 1)

Runs scripts/check_active_trades.py in the container
Queries the database for unresolved real trades
Checks if market has resolved (safe) vs still active (danger)
Blocks deployment if active trades exist
Exit code 1 = active trades

Deploy (Steps 2-4)

Git push + pull to sync code
Docker compose rebuild and restart

Verify (Step 5)

Shows startup logs to confirm success
Manual Pre-Checks

Run the checks independently:

# Run regression tests locally
docker compose run --rm --build polymarket-bot python3 -m pytest tests/ -v

# Check active trades (requires running container)
docker exec polymarket-bot python3 /app/scripts/check_active_trades.py

# Exit codes:
#   0 = Safe to deploy
#   1 = Active trades exist (don't deploy)
#   2 = Error checking
#   3 = Tests failed

When to Skip Tests

Use --skip-tests when:

You've already run tests manually
Making config-only changes (.env)
Urgent fix with verified minimal change
When to Force Deploy

Only use --force when:

The bot is crashed/hung and needs restart
You're certain any active trades are already lost
Emergency security fix is needed
User explicitly approves the risk
Trade Lifecycle
Trade Executed → status='pending' → Market Resolves → status='won'/'lost'
                     ↑                                      ↓
              ⚠️ DANGER ZONE                          Safe to deploy

Troubleshooting
"Regression tests failed"

Fix the failing tests before deploying:

docker compose run --rm --build polymarket-bot python3 -m pytest tests/ -v --tb=long

"Container may not be running"

The pre-check failed because the bot isn't running. This is safe to deploy.

Stuck in "not safe" state

If trades are stuck as pending after market resolution:

# Check database state
docker exec polymarket-bot python3 -c "
import asyncio
import aiosqlite
async def check():
    async with aiosqlite.connect('/app/data/gabagool.db') as db:
        db.row_factory = aiosqlite.Row
        async with db.execute('SELECT id, asset, status, market_end_time FROM trades WHERE dry_run=0 ORDER BY created_at DESC LIMIT 5') as cur:
            for row in await cur.fetchall():
                print(dict(row))
asyncio.run(check())
"

Related Files
tests/ - Regression test suite
scripts/check_active_trades.py - Pre-deployment trade check
src/persistence.py - Database schema
src/strategies/gabagool.py - Trading logic
Weekly Installs
8
Repository
unarmedpuppy/polyjuiced
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass
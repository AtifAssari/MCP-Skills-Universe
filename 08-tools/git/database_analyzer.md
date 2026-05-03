---
title: database-analyzer
url: https://skills.sh/niller2005/polyflup/database-analyzer
---

# database-analyzer

skills/niller2005/polyflup/database-analyzer
database-analyzer
Installation
$ npx skills add https://github.com/niller2005/polyflup --skill database-analyzer
SKILL.md
Responsibilities
Syncing the production database (trades.db) using the sync_db tool.
Querying the SQLite database for trade history, PnL, and position data.
Verifying database integrity and migration status.
Identifying trends or anomalies in the trading data.
Workflow
Run sync_db to fetch the latest production state.
Use uv run check_db.py for a quick integrity check.
Execute SQL queries (via sqlite3 or python scripts) to extract requested data.
Report findings with clear data points (e.g., "Total PnL for BTC in Jan: +$X").
Useful Tools & Scripts
sync_db: Downloads the latest trades.db via SSH.
check_db.py: Basic statistics and integrity check.
migrate_db.py: Migration management.
src/data/database.py: DB interaction logic.
Weekly Installs
13
Repository
niller2005/polyflup
GitHub Stars
19
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass
---
title: install-duckdb
url: https://skills.sh/duckdb/duckdb-skills/install-duckdb
---

# install-duckdb

skills/duckdb/duckdb-skills/install-duckdb
install-duckdb
Installation
$ npx skills add https://github.com/duckdb/duckdb-skills --skill install-duckdb
SKILL.md

Arguments: $@

Each extension argument has the form name or name@repo.

name → INSTALL name;
name@repo → INSTALL name FROM repo;
Step 1 — Locate DuckDB
DUCKDB=$(command -v duckdb)


If not found, tell the user:

DuckDB is not installed. Install it first with one of:

macOS: brew install duckdb
Linux: curl -fsSL https://install.duckdb.org | sh
Windows: winget install DuckDB.cli

Then re-run /duckdb-skills:install-duckdb.

Stop if DuckDB is not found.

Step 2 — Check for --update flag

If --update is present in $@, remove it from the argument list and set mode to update. Otherwise mode is install.

Step 3 — Build and run statements

Install mode:

Parse each remaining argument:

If it contains @, split on @ → INSTALL <name> FROM <repo>;
Otherwise → INSTALL <name>;

Run all in a single DuckDB call:

"$DUCKDB" :memory: -c "INSTALL <ext1>; INSTALL <ext2> FROM <repo2>; ..."


Update mode:

First, check if the DuckDB CLI itself is up to date:

CURRENT=$(duckdb --version | grep -oE '[0-9]+\.[0-9]+\.[0-9]+')
LATEST=$(curl -fsSL https://duckdb.org/data/latest_stable_version.txt)


If CURRENT == LATEST → report DuckDB CLI is up to date.

If CURRENT != LATEST → ask the user:

DuckDB CLI is outdated (installed: CURRENT, latest: LATEST). Upgrade now?

If the user agrees, detect the platform and run the appropriate upgrade command:

macOS (brew available): brew upgrade duckdb
Linux: curl -fsSL https://install.duckdb.org | sh
Windows: winget upgrade DuckDB.cli

Then update extensions:

No extension names → update all: UPDATE EXTENSIONS;
With extension names → update in a single call (ignore @repo): UPDATE EXTENSIONS (<name1>, <name2>, ...);
"$DUCKDB" :memory: -c "UPDATE EXTENSIONS;"
# or
"$DUCKDB" :memory: -c "UPDATE EXTENSIONS (<ext1>, <ext2>, ...);"


Report success or failure after the call completes.

Weekly Installs
111
Repository
duckdb/duckdb-skills
GitHub Stars
438
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
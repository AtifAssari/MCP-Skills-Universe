---
title: analyzing-data
url: https://skills.sh/astronomer/agents/analyzing-data
---

# analyzing-data

skills/astronomer/agents/analyzing-data
analyzing-data
Installation
$ npx skills add https://github.com/astronomer/agents --skill analyzing-data
Summary

Query your data warehouse to answer business questions with cached patterns and concept mappings.

Supports pattern lookup and caching for repeated question types, with outcome recording to improve future queries
Includes concept-to-table mapping cache and table schema discovery via INFORMATION_SCHEMA or codebase grep
Provides run_sql() and run_sql_pandas() kernel functions returning Polars or Pandas DataFrames for analysis
CLI commands for managing concept, pattern, and table caches, plus warehouse selection and kernel lifecycle control
SKILL.md
Data Analysis

Answer business questions by querying the data warehouse. The kernel auto-starts on first exec call.

All CLI commands below are relative to this skill's directory. Before running any scripts/cli.py command, cd to the directory containing this file.

Workflow

Pattern lookup — Check for a cached query strategy:

uv run scripts/cli.py pattern lookup "<user's question>"


If a pattern exists, follow its strategy. Record the outcome after executing:

uv run scripts/cli.py pattern record <name> --success  # or --failure


Concept lookup — Find known table mappings:

uv run scripts/cli.py concept lookup <concept>


Table discovery — If cache misses, search the codebase (Grep pattern="<concept>" glob="**/*.sql") or query INFORMATION_SCHEMA. See reference/discovery-warehouse.md.

Execute query:

uv run scripts/cli.py exec "df = run_sql('SELECT ...')"
uv run scripts/cli.py exec "print(df)"


Cache learnings — Always cache before presenting results:

# Cache concept → table mapping
uv run scripts/cli.py concept learn <concept> <TABLE> -k <KEY_COL>
# Cache query strategy (if discovery was needed)
uv run scripts/cli.py pattern learn <name> -q "question" -s "step" -t "TABLE" -g "gotcha"


Present findings to user.

Kernel Functions
Function	Returns
run_sql(query, limit=100)	Polars DataFrame
run_sql_pandas(query, limit=100)	Pandas DataFrame

pl (Polars) and pd (Pandas) are pre-imported.

CLI Reference
Kernel
uv run scripts/cli.py warehouse list      # List warehouses
uv run scripts/cli.py start [-w name]     # Start kernel (with optional warehouse)
uv run scripts/cli.py exec "..."          # Execute Python code
uv run scripts/cli.py status              # Kernel status
uv run scripts/cli.py restart             # Restart kernel
uv run scripts/cli.py stop                # Stop kernel
uv run scripts/cli.py install <pkg>       # Install package

Concept Cache
uv run scripts/cli.py concept lookup <name>                     # Look up
uv run scripts/cli.py concept learn <name> <TABLE> -k <KEY_COL> # Learn
uv run scripts/cli.py concept list                               # List all
uv run scripts/cli.py concept import -p /path/to/warehouse.md   # Bulk import

Pattern Cache
uv run scripts/cli.py pattern lookup "question"                                      # Look up
uv run scripts/cli.py pattern learn <name> -q "..." -s "..." -t "TABLE" -g "gotcha"  # Learn
uv run scripts/cli.py pattern record <name> --success                                # Record outcome
uv run scripts/cli.py pattern list                                                   # List all
uv run scripts/cli.py pattern delete <name>                                          # Delete

Table Schema Cache
uv run scripts/cli.py table lookup <TABLE>            # Look up schema
uv run scripts/cli.py table cache <TABLE> -c '[...]'  # Cache schema
uv run scripts/cli.py table list                       # List cached
uv run scripts/cli.py table delete <TABLE>             # Delete

Cache Management
uv run scripts/cli.py cache status                # Stats
uv run scripts/cli.py cache clear [--stale-only]  # Clear

References
reference/discovery-warehouse.md — Large table handling, warehouse exploration, INFORMATION_SCHEMA queries
reference/common-patterns.md — SQL templates for trends, comparisons, top-N, distributions, cohorts
Weekly Installs
720
Repository
astronomer/agents
GitHub Stars
354
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass
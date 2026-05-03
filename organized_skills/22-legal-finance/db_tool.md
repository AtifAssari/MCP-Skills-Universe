---
rating: ⭐⭐⭐
title: db-tool
url: https://skills.sh/blogic-cz/agent-tools/db-tool
---

# db-tool

skills/blogic-cz/agent-tools/db-tool
db-tool
Installation
$ npx skills add https://github.com/blogic-cz/agent-tools --skill db-tool
SKILL.md
db-tool (Database)

Database query tool — SQL execution and schema introspection. Part of @blogic-cz/agent-tools.

How to Run

Run via bun db-tool (requires @blogic-cz/agent-tools as a dev dependency). NEVER run bare psql — the credential guard will block it. Auth: env var defined by passwordEnvVar in config (e.g. AGENT_TOOLS_DB_PASSWORD).

Commands
bun db-tool sql --env local --sql "SELECT * FROM users LIMIT 5"
bun db-tool sql --env test --sql "SELECT count(*) FROM organizations"
bun db-tool schema --env local --mode tables          # List tables
bun db-tool schema --env local --mode columns --table users # Show table schema


Environment is any string (e.g. local, test, prod). Set defaultEnvironment in agent-tools.json5 to skip --env on every call.

Tips
Use --help on any subcommand for full options.
Error responses include hint, nextCommand, and retryable fields — always check them on failure.
Prefer CLI tool over MCP tools — more efficient, doesn't load extra context.
Weekly Installs
8
Repository
blogic-cz/agent-tools
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
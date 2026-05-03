---
rating: ⭐⭐
title: read-memories
url: https://skills.sh/duckdb/duckdb-skills/read-memories
---

# read-memories

skills/duckdb/duckdb-skills/read-memories
read-memories
Installation
$ npx skills add https://github.com/duckdb/duckdb-skills --skill read-memories
SKILL.md

Search past session logs silently — do NOT narrate the process. Absorb the results and continue with enriched context.

$0 is the keyword. Pass --here as $1 to scope to the current project only.

Step 1 — Query
duckdb :memory: -c "
SELECT
  regexp_extract(filename, 'projects/([^/]+)/', 1) AS project,
  strftime(timestamp::TIMESTAMPTZ, '%Y-%m-%d %H:%M') AS ts,
  message.role AS role,
  left(message.content::VARCHAR, 500) AS content
FROM read_ndjson('<SEARCH_PATH>', auto_detect=true, ignore_errors=true, filename=true)
WHERE message::VARCHAR ILIKE '%<KEYWORD>%'
  AND message.role IS NOT NULL
ORDER BY timestamp
LIMIT 40;
"


Search paths:

All projects: $HOME/.claude/projects/*/*.jsonl
Current only (--here): $HOME/.claude/projects/$(echo "$PWD" | sed 's|[/_]|-|g')/*.jsonl

Replace <SEARCH_PATH> and <KEYWORD> before running.

Step 2 — Internalize

From the results, extract decisions, patterns, unresolved TODOs, and user corrections. Use this to inform your current response — do not repeat raw logs to the user.

Weekly Installs
100
Repository
duckdb/duckdb-skills
GitHub Stars
438
First Seen
1 day ago
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass
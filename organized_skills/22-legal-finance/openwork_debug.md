---
rating: ⭐⭐
title: openwork-debug
url: https://skills.sh/different-ai/openwork/openwork-debug
---

# openwork-debug

skills/different-ai/openwork/openwork-debug
openwork-debug
Installation
$ npx skills add https://github.com/different-ai/openwork --skill openwork-debug
SKILL.md
Credential check

Set these before running the HTTP checks:

OPENWORK_SERVER_URL
OPENWORK_SERVER_TOKEN
OPENWORK_WORKSPACE_ID (optional; use /workspaces to discover)
Quick usage (read-only)
curl -s "$OPENWORK_SERVER_URL/health"
curl -s "$OPENWORK_SERVER_URL/capabilities" \
  -H "Authorization: Bearer $OPENWORK_SERVER_TOKEN"

curl -s "$OPENWORK_SERVER_URL/workspaces" \
  -H "Authorization: Bearer $OPENWORK_SERVER_TOKEN"

Workspace config snapshot
curl -s "$OPENWORK_SERVER_URL/workspace/$OPENWORK_WORKSPACE_ID/config" \
  -H "Authorization: Bearer $OPENWORK_SERVER_TOKEN"

Audit log (recent)
curl -s "$OPENWORK_SERVER_URL/workspace/$OPENWORK_WORKSPACE_ID/audit?limit=25" \
  -H "Authorization: Bearer $OPENWORK_SERVER_TOKEN"

OpenCode engine checks
opencode -p "ping" -f json -q
opencode mcp list
opencode mcp debug <name>

DB fallback (read-only)

When the engine API is unavailable, you can inspect the SQLite db:

sqlite3 ~/.opencode/opencode.db "select id, title, status from sessions order by updated_at desc limit 5;"
sqlite3 ~/.opencode/opencode.db "select role, content from messages order by created_at desc limit 10;"

Notes
Audit logs are stored at .opencode/openwork/audit.jsonl in the workspace root.
OpenWork server writes only within approved workspace roots.
Weekly Installs
88
Repository
different-ai/openwork
GitHub Stars
14.6K
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass
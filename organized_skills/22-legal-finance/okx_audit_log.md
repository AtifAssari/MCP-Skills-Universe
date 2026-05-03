---
rating: ⭐⭐
title: okx-audit-log
url: https://skills.sh/okx/onchainos-skills/okx-audit-log
---

# okx-audit-log

skills/okx/onchainos-skills/okx-audit-log
okx-audit-log
Installation
$ npx skills add https://github.com/okx/onchainos-skills --skill okx-audit-log
SKILL.md
Onchain OS Audit Log

Provide the audit log file path for developers to troubleshoot issues offline.

Response

Tell the user:

Log file path: ~/.onchainos/audit.jsonl (or $ONCHAINOS_HOME/audit.jsonl if the env var is set)
Format: JSON Lines, one JSON object per line
First line (device header): {"type":"device","os":"<os>","arch":"<arch>","version":"<cli_version>"} — written once when the log file is created; preserved across rotations
Entry fields: ts (local time with timezone, e.g. 2026-03-18 +8.0 18:00:00.123), source (cli/mcp), command, ok, duration_ms, args (redacted), error
Rotation: max 10,000 lines, auto-keeps the device header + most recent 5,000 entries

Do NOT read or display the file contents in the conversation.

Weekly Installs
2.7K
Repository
okx/onchainos-skills
GitHub Stars
234
First Seen
Mar 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
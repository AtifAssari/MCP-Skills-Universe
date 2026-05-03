---
title: idempotent-redundancy
url: https://skills.sh/parcadei/continuous-claude-v3/idempotent-redundancy
---

# idempotent-redundancy

skills/parcadei/continuous-claude-v3/idempotent-redundancy
idempotent-redundancy
Installation
$ npx skills add https://github.com/parcadei/continuous-claude-v3 --skill idempotent-redundancy
SKILL.md
Idempotent Redundancy

When adding redundant paths (fallbacks, belt-and-suspenders), make them idempotent.

Pattern

Redundancy without idempotency causes loops, churn, or data corruption.

DO
Use _is_merge: true for Braintrust updates
Check if value exists before writing (fallback only if missing)
Use atomic write/rename for file operations
Make reconciliation steps safe to run repeatedly
DON'T
Write unconditionally in fallback paths
Allow multiple writers to overwrite each other
Fire "repair" actions that can trigger more repairs
Source Sessions
a541f08a: "Redundancy is good only if idempotent"
1c21e6c8: "Belt-and-suspenders, but make it idempotent"
6a9f2d7a: "Idempotent repair hooks"
Weekly Installs
304
Repository
parcadei/contin…laude-v3
GitHub Stars
3.8K
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
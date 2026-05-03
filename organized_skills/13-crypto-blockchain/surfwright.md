---
rating: ⭐⭐
title: surfwright
url: https://skills.sh/marcohefti/surfwright/surfwright
---

# surfwright

skills/marcohefti/surfwright/surfwright
surfwright
Installation
$ npx skills add https://github.com/marcohefti/surfwright --skill surfwright
SKILL.md
SurfWright Skill

Deterministic browser control with JSON-first outputs and explicit handles.

Discovery (Two Lanes)
Action first: run mission commands directly.
Fast lane bootstrap: surfwright contract --profile browser-core.
Do not probe with which, help flags, or repeated skill file reads.
Use surfwright contract --command <id> only after a command-id miss.
Use surfwright contract --commands <id1,id2,...> for small miss batches.
Use surfwright contract --full only for deep-lane catalog discovery.
Runtime Rules
Keep default JSON output; do not parse prose.
Confirm required JSON schema via surfwright contract --command <id> only after a command-id miss.
Start headless unless explicitly instructed otherwise.
For workspace extension workflows, verify open/session payload appliedExtensions[*].state == runtime-installed before proceeding.
Treat non-zero exits as typed failures and branch on code (retryable when present).
Use one unique --agent-id per task.
Treat daemon queue overload codes (E_DAEMON_QUEUE_TIMEOUT, E_DAEMON_QUEUE_SATURATED) as backpressure.
If daemon transport is unreachable and continuity matters, use SURFWRIGHT_DAEMON=0.
For non-trivial plans, prefer run --plan <file> (or --plan -) over inline --plan-json.
For complex JavaScript, prefer target eval --script-file / --script-b64.
Prefer typed primitives over eval when possible: target count, target attr, target click --nth, target click --count-after.
Weekly Installs
30
Repository
marcohefti/surfwright
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
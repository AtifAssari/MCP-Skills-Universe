---
rating: ⭐⭐
title: opsx-apply-subagents
url: https://skills.sh/costicapuntaru/agentica/opsx-apply-subagents
---

# opsx-apply-subagents

skills/costicapuntaru/agentica/opsx-apply-subagents
opsx-apply-subagents
Installation
$ npx skills add https://github.com/costicapuntaru/agentica --skill opsx-apply-subagents
SKILL.md
OpenSpec Parallel Agents

Orchestrates concurrent subagents for OpenSpec — one subagent per independent task, serial execution for dependency chains. Supports OPSX, legacy openspec:*, and Codex CLI prompts:* aliases.

See REFERENCE.md for the full command compatibility matrix and round summary template.

Trigger conditions

Enable when any of these are true:

2+ changes can run independently
/opsx:apply (or alias) has multiple pending non-conflicting tasks
Batch archiving or /opsx:bulk-archive is needed
Concurrency rules
One subagent per task — never group tasks
Only dependency-free nodes run in parallel; chains run serially
No parallel writes to overlapping file regions — downgrade to serial if conflict risk detected
Wait for all subagents before summarizing
/opsx:apply workflow
Run openspec instructions apply --change "<name>" --json → get tasks + context files
Analyze dependencies — identify independent vs chained tasks
Spawn one subagent per independent task (strictly parallel)
Wait for all → mark completed tasks (- [x]) sequentially to avoid conflicts
Repeat for next unblocked batch
Legacy command mapping
Legacy	OPSX equivalent
/openspec:proposal	/opsx:new + /opsx:ff
/openspec:apply	/opsx:apply
/openspec:archive	/opsx:archive
Weekly Installs
14
Repository
costicapuntaru/agentica
GitHub Stars
1
First Seen
Mar 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
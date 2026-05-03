---
rating: ⭐⭐
title: beo-swarming
url: https://skills.sh/minhtri2710/skills/beo-swarming
---

# beo-swarming

skills/minhtri2710/skills/beo-swarming
beo-swarming
Installation
$ npx skills add https://github.com/minhtri2710/skills --skill beo-swarming
SKILL.md

See ../reference/references/shared-hard-gates.md § Shared References Convention.

Beo Swarming
Overview

Swarming is the orchestration layer for parallel current-phase execution. Its job is to launch workers, coordinate them through the live graph and Agent Mail, resolve conflicts, and keep the approved current phase moving.

Core principle: the orchestrator coordinates; workers execute.

Hard Gates
Role Boundary

You are the ORCHESTRATOR. Launch workers, monitor coordination, handle escalations, and keep the approved current phase moving. Do not implement beads or edit source files yourself.

beo-swarming = launch and tend workers
beo-executing = each worker's implementation loop
Default Swarm Loop
confirm current-phase execution is approved and swarm-worthy
confirm Agent Mail is healthy enough to coordinate
register the coordinator and announce the swarm
spawn bounded workers with explicit current-phase scope
monitor completions, blockers, idle workers, and file conflicts
reassign, rescue, or degrade when coordination stops paying off
route to beo-reviewing for final scope or remove approved and route to beo-planning when later phases remain

Use references/swarming-operations.md for the exact readiness checks, worker-spawn contract, monitor/tend loop, progress heuristics, and completion/checkpoint mechanics. Use references/message-templates.md for Agent Mail bodies. Use ../reference/references/worker-template.md when building worker context.

Active Swarm Never Idles

If workers are spawned, online, busy, blocked, or expected to report, you are in a tending phase. Keep looping through Agent Mail and the live bead graph. Do not treat a quiet thread as permission to stop coordinating.

Handoff

See references/swarming-operations.md § 5. Swarm Completion for the full completion checklist, graph verification, and routing logic.

Context Budget

Follow ../reference/references/shared-hard-gates.md § Context Budget Protocol. Skill-specific checkpoint items: active workers, reservations, blockers, and the current planning-aware route state.

Red Flags & Anti-Patterns

See references/swarming-operations.md for monitoring heuristics and completion checks. Verify coordinator behavior against references/pressure-scenarios.md when debugging swarm coordination failures. Stop and diagnose before continuing if the orchestrator starts editing code, workers go idle while ready current-phase beads still exist, Agent Mail falls quiet for too long, file conflicts repeat, or current-phase completion is being mistaken for final review while later phases remain.

Weekly Installs
15
Repository
minhtri2710/skills
GitHub Stars
1
First Seen
Mar 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
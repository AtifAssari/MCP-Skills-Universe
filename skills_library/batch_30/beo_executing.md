---
title: beo-executing
url: https://skills.sh/minhtri2710/skills/beo-executing
---

# beo-executing

skills/minhtri2710/skills/beo-executing
beo-executing
Installation
$ npx skills add https://github.com/minhtri2710/skills --skill beo-executing
SKILL.md

See ../reference/references/shared-hard-gates.md § Shared References Convention.

Beo Executing
Overview

Executing is the per-worker implementation loop for approved current-phase work. Its job is to pick one truly ready bead, execute it safely, verify the result, report it, and repeat.

Core principle: one task at a time — implement, verify, report, loop.

Execution scope is always the currently approved phase. If planning mode is multi-phase, do not silently expand into later phases.

Operating Modes
Worker mode: dispatched by beo-swarming; implement directly, report to the orchestrator, and do not spawn sub-subagents.
Standalone mode: entered after beo-validating; may delegate through the session's normal subagent/task mechanism or implement directly, depending on scope and overhead. Standalone delegation is still one-bead-at-a-time — if multiple beads would benefit from parallel execution, route to beo-swarming instead.
Solo mode: standalone execution when Agent Mail or reservation APIs are unavailable. Before entering Solo mode, verify that no other beo workers are active (check for in-flight beads in the graph and any existing reservation state). If active workers or reservations exist but cannot be coordinated, do not enter Solo mode — pause and report the conflict to the user. Once exclusivity is confirmed, execute one bead at a time, avoid speculative parallelism, and treat local file ownership as exclusive.

The loop is the same in all three modes. The main differences are how results are reported and whether delegated dispatch is available.

Hard Gates
Default Execution Loop
verify approval and current-phase scope
pick the next truly ready bead
verify the bead spec is executable
reserve files and transition the bead cleanly
assemble only the context needed for this bead
dispatch if appropriate, otherwise implement directly
run verification, write the report, and update bead state
loop, or hand off when the current phase is complete

Use references/execution-operations.md for the exact scheduling cascade, transition protocol, dispatch contract, status mapping, completion bookkeeping, and checkpoint procedure. Use references/worker-prompt-guide.md for the full worker prompt template.

Execution Notes
Before implementation: Verify prerequisites, task selection, stale-label cleanup, and description checks per references/execution-operations.md sections 1-4. If swarming supplied a startup hint, verify it against the live graph.
File coordination: Reserve files before editing; see references/execution-operations.md section 5 and references/worker-prompt-guide.md for the prompt template. Never truncate the bead spec.
Dispatch: Implement directly in worker mode; delegate in standalone mode when overhead is justified; never invent pseudo-dispatch. See references/execution-operations.md sections 6-7 for dispatch and result-to-state mapping. If blocked, use references/blocker-handling.md and resume from task selection.
State flushing: After any status transition or reservation update, flush graph state so downstream routing does not depend on stale metadata.
Completion

When all current-phase tasks are closed, run the completion and routing procedure in references/execution-operations.md section 8. When later phases remain, do not claim the whole feature is complete.

For multi-phase completion routing, see ../reference/references/shared-hard-gates.md § Multi-Phase Completion Routing.

Do not track completion only in the conversation. Once verification passes, update the bead state in the graph immediately.

Handoff

When the current phase closes successfully:

route to beo-reviewing if this completes the final execution scope
remove approved and route to beo-planning if later phases remain
never describe current-phase completion as full feature completion when multi-phase work remains
Context Budget

Follow ../reference/references/shared-hard-gates.md § Context Budget Protocol. Skill-specific checkpoint items: current execution state via references/execution-operations.md, and planning-aware fields when known.

Post-Compaction Recovery

If context was compacted, re-read the essential feature artifacts (CONTEXT.md, plan.md, phase-contract.md, story-map.md), relevant state files, and the live task graph before resuming. Continue from the last known good state rather than guessing from memory.

Red Flags & Anti-Patterns

Avoid duplicate dispatch, speculative redispatch after failures, silent spec rewrites during execution, and worker prompts that omit verification requirements.

Weekly Installs
16
Repository
minhtri2710/skills
GitHub Stars
1
First Seen
Mar 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
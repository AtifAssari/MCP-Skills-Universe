---
rating: ⭐⭐
title: beo-router
url: https://skills.sh/minhtri2710/skills/beo-router
---

# beo-router

skills/minhtri2710/skills/beo-router
beo-router
Installation
$ npx skills add https://github.com/minhtri2710/skills --skill beo-router
SKILL.md
Beo Router
Overview

beo-router is the entry point for beo sessions. Its job is simple:

determine the real workflow state from artifacts and the live graph
explain that state in human terms
produce exactly one NextAction — LoadSkill(name), ReturnToUser(reason), or Stop(done)

Core principle: always know where you are before deciding where to go.

Hard Gates

See ../reference/references/shared-hard-gates.md § Shared References Convention.

Default Router Loop
confirm the repository is onboarded and the workspace is healthy
if .beads/beo_status.mjs exists, run node .beads/beo_status.mjs --json as a quick scout
check for .beads/HANDOFF.json
identify the active epic, if any
inspect the active feature's core artifacts and task graph
classify the current state using the canonical routing table
report the state in human terms
emit exactly one NextAction: LoadSkill(name) to continue the pipeline, ReturnToUser(reason) when a decision or clarification is needed, or Stop(done) when the session is complete

Use references/router-operations.md when you need the exact bootstrap steps, Quick-scope scaffold, resume validation procedure, planning-aware routing rules, or doctor-mode commands. Use ../reference/references/pipeline-contracts.md for the canonical state routing table. Use references/go-mode.md when the user says "go", "run the full pipeline", or "go mode" and you need the 3-gate end-to-end sequence. Use ../reference/references/communication-standard.md for inter-skill message formatting when writing handoff messages or state reports.

Report State Before Routing

Always report the state in human terms before loading the next skill. At minimum include:

feature
mode (single-phase, multi-phase, or unknown pre-planning)
current phase if known
canonical state
progress / blockers
next action
New Feature Intake

When no active feature exists, still use the canonical routing model. The intake-specific states are:

new-quick-intake -> create the epic, preserve the immutable slug using ../reference/references/artifact-conventions.md#slug-lifecycle, scaffold minimal artifacts via references/router-operations.md Quick Path Scaffold, then route to beo-validating
new-debug-intake -> beo-debugging
meta-skill -> beo-writing-skills
otherwise -> create the epic and route to beo-exploring

If a request first looks quick but inspection shows it is larger, ambiguous, or phase-shaped, preserve any existing quick task bead as planning input and promote the work into the normal pipeline. Before creating a new epic, always confirm there is not already an active one for the same feature.

Doctor Mode

When asked to check project health, inspect graph health, blocked work, stale work, planning shape, artifact presence, and one next corrective action. On first-session bootstrap or when workspace health is in doubt, include br doctor in the health check flow.

Priority Rules

These override normal routing:

P1 review findings block progress.
CONTEXT.md is the source of truth for locked decisions.
Never skip beo-validating.
Spike failures halt the pipeline and send work back to planning.
Current-phase completion is not whole-feature completion when later phases remain.
Quick-scope work still routes through validation before execution.
Choose beo-swarming only when validated parallel-ready tasks exist; otherwise route to beo-executing.
Handoff

After classification, report the current state in human terms and emit exactly one NextAction: LoadSkill(name), ReturnToUser(reason), or Stop(done). If a checkpoint or resume artifact exists, preserve the planning-aware state while handing off.

Context Budget

Follow ../reference/references/shared-hard-gates.md § Context Budget Protocol. Skill-specific checkpoint items: current STATE.json, selected route, planning-aware fields when known, and any resume detail needed to continue safely.

Red Flags & Anti-Patterns

Known limitation: STATE.json and HANDOFF.json are currently singleton files. When multiple features are in flight simultaneously, verify the feature field matches the intended epic before trusting state. Feature-scoped state files are a future improvement.

Do not create duplicate epics, bypass validation because work seems small, route to swarming without a validated parallel plan, or skip compounding after successful review.

Weekly Installs
19
Repository
minhtri2710/skills
GitHub Stars
1
First Seen
Mar 30, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass
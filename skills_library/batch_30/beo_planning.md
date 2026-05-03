---
title: beo-planning
url: https://skills.sh/minhtri2710/skills/beo-planning
---

# beo-planning

skills/minhtri2710/skills/beo-planning
beo-planning
Installation
$ npx skills add https://github.com/minhtri2710/skills --skill beo-planning
SKILL.md

See ../reference/references/shared-hard-gates.md § Shared References Convention.

Beo Planning
Overview

Planning turns locked decisions in CONTEXT.md into an execution-ready current phase. It should answer two questions in order:

what is the right whole-feature shape?
what is the smallest current phase we should validate next?

Core principle: do not jump from research straight to beads. First shape the feature, then define the current phase, then decompose that phase only.

Hard Gates
Default Planning Loop
confirm CONTEXT.md exists and decisions are truly locked
retrieve prior learnings and critical patterns
run focused discovery and write discovery.md
write approach.md
decide single-phase vs multi-phase
write plan.md
if multi-phase, write phase-plan.md, enter the paused planning state awaiting-planning-approval, and get explicit user approval for the phase sequence and selected current phase before validation handoff
define the current phase in phase-contract.md
map the current phase in story-map.md
create and verify beads for the current phase only
hand off to beo-validating

Load the specific planning reference you need:

references/planning-prerequisites.md for prerequisites, learnings, and planning mode
references/artifact-writing-guide.md for artifact writing, approval, and high-stakes review
references/bead-ops.md for bead creation, wiring, and epic updates
references/planning-state-and-cleanup.md for state updates, replanning cleanup, and checkpointing
../reference/references/communication-standard.md for inter-skill message formatting when writing handoff messages Read references/discovery-reference.md when beginning the discovery phase (step 3) to structure codebase analysis. Read references/bead-ops.md when creating beads (after story-map.md is written) to ensure correct bead structure, dotted ID format, and dependency wiring.
Planning Modes

Use the simplest mode that keeps execution safe and understandable.

single-phase — one believable closed loop, usually 1-4 stories.
multi-phase — feature unfolds across 2+ meaningful capability slices.

See references/planning-prerequisites.md § 3. Decide Planning Mode for the full decision criteria.

phase-plan.md is the whole-feature sequence for multi-phase work. phase-contract.md and story-map.md always describe the current phase only.

Required Artifacts and Their Roles

Artifacts: discovery.md, approach.md, plan.md, phase-plan.md (multi-phase only), phase-contract.md, story-map.md, task beads.

See references/artifact-writing-guide.md sections 4-7 for write order, artifact roles, and required fields. Use the corresponding templates: references/discovery-reference.md, references/approach-template.md, references/plan-template.md, references/phase-plan-template.md, references/phase-contract-template.md, references/story-map-template.md, references/bead-ops.md.

Learnings Retrieval

This step is mandatory before discovery.

Use ../reference/references/learnings-read-protocol.md for the canonical read flow. See references/planning-prerequisites.md section 2 for how learnings must influence planning artifacts.

If no relevant learnings exist, record that explicitly rather than implying the step was skipped.

Discovery and Approach

discovery.md gathers evidence. approach.md turns that evidence into a decision.

approach.md must exist before any current-phase artifacts are written. See references/artifact-writing-guide.md section 5 for the required fields and self-check.

If approach.md is weak, do not compensate by stuffing extra detail into plan.md. Fix approach.md first.

Multi-Phase Approval

If planning mode is multi-phase, the user must explicitly approve the phase sequence and current-phase selection before validation handoff.

Use the canonical approval rule from ../reference/references/approval-gates.md and the exact prompt shape and approval/rejection flow in references/artifact-writing-guide.md section 8.

Until that approval is granted, treat the feature as paused in awaiting-planning-approval, not ready-to-validate.

Current-Phase Definition

Before bead creation, define the current phase as a closed loop. Both phase-contract.md and story-map.md are required, and both describe the current phase only.

See references/artifact-writing-guide.md section 9 for required fields, and use references/phase-contract-template.md and references/story-map-template.md for structure.

If the exit state in phase-contract.md is vague, fix the contract instead of pushing uncertainty into bead descriptions. If stories in story-map.md do not clearly support the phase exit state, fix the story map before creating beads.

Bead Creation Rules

Only create beads after phase-contract.md and story-map.md are real and coherent.

Use references/bead-ops.md section 11 for the exact create / write / wire / validate sequence. Use references/bead-ops.md for decomposition rules and the bead quality checklist.

After creation, read every bead back and verify it passes the quality checklist in references/bead-ops.md. Key checks: concrete verification criteria, believable worker-sized scope, explicit file-overlap sequencing, and no premature future-phase stubs. Prefer durable invariants ("all relevant tests pass") over hardcoded counts in exit criteria.

After wiring dependencies, run br dep cycles --json to confirm the graph is still acyclic.

High-Stakes Review

For HIGH-stakes work — core architecture, auth, data model changes, large blast radius, or multiple HIGH-risk components — use references/artifact-writing-guide.md section 10 for the multi-perspective review before handoff.

Do not inflate ordinary work to HIGH by default. Risk labels should reflect real blast radius and uncertainty.

When artifacts depend on external package or tool versions, verify the versions against the authoritative package registry or source of truth rather than trusting agent-reported version numbers.

Handoff

After current-phase artifacts are written and beads are verified:

write .beads/STATE.json using ../reference/references/state-and-handoff-protocol.md
include planning-aware fields (planning_mode, has_phase_plan, current_phase, total_phases, phase_name) when known
announce handoff to beo-validating

Validation always approves execution readiness for the current phase only. If later phases remain, current-phase completion is not whole-feature completion.

Write .beads/HANDOFF.json only when the context budget requires a checkpoint or the session must pause.

Quick Mode

When CONTEXT.md classifies the feature as Quick (see ../reference/references/pipeline-contracts.md § State Routing Table > Quick-Scope Definition), planning uses an abbreviated flow:

Skip parallel discovery; do a quick single-pass review of affected files
Write abbreviated artifacts (approach + tasks in plan.md, single-story story-map.md, minimal phase-contract.md)
The hard gate requiring phase-contract.md and story-map.md still applies — Quick mode writes abbreviated versions, it does not skip them
Skip the formal multi-perspective review

See references/bead-ops.md § Quick Mode for the exact abbreviated sequence.

Replanning and Phase Advancement

When planning re-enters after a scope change or completed phase, stale artifacts and state fields must be cleaned up before new planning proceeds. Prior approval is always invalidated when the phase structure or execution scope changes.

Use references/planning-state-and-cleanup.md section 14 for the exact cleanup sequence, trigger conditions, and hard rules.

Context Budget

Follow ../reference/references/shared-hard-gates.md § Context Budget Protocol. Skill-specific checkpoint items: planning mode, current-phase selection, artifact completeness, and any ready beads already created.

Red Flags & Anti-Patterns

Guard against plan-to-task shortcuts, vague exit states, and bead descriptions that would force workers to improvise. The inline rules above are the source of truth.

Weekly Installs
20
Repository
minhtri2710/skills
GitHub Stars
1
First Seen
Mar 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
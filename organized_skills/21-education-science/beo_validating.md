---
rating: ⭐⭐
title: beo-validating
url: https://skills.sh/minhtri2710/skills/beo-validating
---

# beo-validating

skills/minhtri2710/skills/beo-validating
beo-validating
Installation
$ npx skills add https://github.com/minhtri2710/skills --skill beo-validating
SKILL.md

See ../reference/references/shared-hard-gates.md § Shared References Convention.

Beo Validating
Overview

Validating is the gate between planning and execution. Its job is to prove that the current phase is structurally sound before any code is written.

Core principle: catch plan failures before they become implementation failures.

If phase-plan.md exists, validation still applies to the current phase only. Whole-feature sequencing matters for context, but approval never expands into later phases.

Communication Standard

All validation outputs (plan-checker findings, bead-reviewer findings, dimension failures) must follow ../reference/references/communication-standard.md: plain language first, evidence with quotes or path:line, concrete failure scenario, and smallest fix.

Hard Gates
Default Validation Loop
confirm current-phase artifacts and task beads exist
retrieve prior learnings and orient to the current phase
run the 8-dimension structural check
inspect graph health and bead quality
run spikes only where yes/no proof would change go / no-go
summarize readiness in human terms
get explicit user approval before execution

Load references/validation-operations.md when you need the exact checker flow, graph commands, spike mechanics, approval summary, Quick mode, or handoff procedure.

Prerequisites

Confirm that all execution prerequisites are met: epic, task beads, and all required artifacts exist and are readable. See references/validation-operations.md Section 1 for the exact artifact checklist and read order.

Current-Phase Orientation

Orient to the current phase before running the structural gate. Verify that current-phase artifacts, state metadata, and task graph all describe the same phase. See references/validation-operations.md Section 2 for the orientation procedure and summary format.

The 8-Dimension Structural Check

Run validation across these 8 dimensions:

Phase contract clarity
Story coverage and ordering
Decision coverage
Dependency correctness
File scope isolation
Context budget
Verification completeness
Exit-state completeness and risk alignment

Use references/validation-operations.md and references/plan-checker-prompt.md for the exact checker procedure and full PASS / FAIL detail.

Repair Rule

See references/validation-operations.md Section 3 (Failure Handling) for the repair-routing table and iteration limits. Do not keep patching a plan whose current phase no longer makes sense as a closed loop. After repairing a failed dimension, re-run the relevant checks instead of assuming the plan now passes. If failures reveal a broader decomposition problem rather than an isolated defect, route back to planning instead of continuing to patch in place.

Graph Health and Bead Quality

Confirm graph integrity, story-to-bead coherence, and bead description quality. See references/validation-operations.md Section 4 for the exact graph-health procedure, and references/bead-reviewer-prompt.md for fresh-eyes bead review when complexity is high.

Spikes for HIGH-Risk Work

Use spikes only when a yes/no proof would change whether this phase should proceed. Do not create ceremonial spikes for already-understood work. See references/validation-operations.md Section 5 for the exact create / record / result-handling sequence.

Exit-State Readiness Review

Before approval, confirm that completing all stories and beads will achieve the phase exit state. See references/plan-checker-prompt.md Dimension 8 for the exact readiness questions. If any answer is no or uncertain, do not approve execution -- route back to the layer that must change.

Reject plans whose phase exit state is vague or non-observable, whose first story cannot explain why it must happen first, or whose bead-level "done" definitions do not trace cleanly to story outcomes.

Approval Gate

Use the canonical approval rule from ../reference/references/approval-gates.md. Approval must be explicit and must apply to the current phase only.

When approval is granted:

run br label add <epic-id> -l approved
choose and explicitly state the next execution mode (beo-executing or beo-swarming)

When approval is rejected or withheld:

do not proceed; route back to planning or exploring as needed

See references/validation-operations.md Section 7 for the full approval summary format, execution-mode decision rule, rejection procedure, and handoff steps.

Quick Mode

For very small, low-risk work (Quick scope), use the Quick-validation shortcut in references/validation-operations.md Section 8. Even in Quick mode, user approval is still required before any code is written.

Handoff

After approval, choose and announce the execution mode, then write .beads/STATE.json. See references/validation-operations.md Section 8 (Normal Handoff) for the decision rule and state fields.

If later phases remain, say so explicitly. Validation approval for the current phase never means the whole feature is approved.

Context Budget

Follow ../reference/references/shared-hard-gates.md § Context Budget Protocol. Skill-specific checkpoint items: validation progress, and see references/validation-operations.md Section 8 for the full checkpoint procedure.

Red Flags & Anti-Patterns

Do not rubber-stamp approval, skip decision coverage, or treat overlap and missing story linkage as minor issues. Validation must produce evidence, not vibes.

Weekly Installs
19
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
---
rating: ⭐⭐
title: design-readiness-check
url: https://skills.sh/freeacger/loom/design-readiness-check
---

# design-readiness-check

skills/freeacger/loom/design-readiness-check
design-readiness-check
Installation
$ npx skills add https://github.com/freeacger/loom --skill design-readiness-check
SKILL.md
Design Readiness Check
Overview

This skill is the quality gate between design work and implementation planning.

Its job is to answer one question clearly: is the current design complete enough to move into writing-plans?

It is not a replacement for design-decision-audit. That skill audits standalone design or plan documents. This skill checks the readiness of an in-progress design workflow before planning.

When to Use

Use this skill when:

the design looks mostly complete
the next possible step is writing-plans
the user asks whether the design is ready to implement
the remaining concern is completeness, not discovery

Do not use this skill when:

the design tree is still missing
major branches remain vague
core decisions are still unresolved
the user is asking for a general audit of an external design document
design_target_type is missing from the design state
Workflow
Phase A: Context Preparation

Goal: Load design state and assemble context for parallel checks.

Load the current design_state from the conversation context.
Read the design tree content and all related context (open branches, decision nodes, risks, validation state).
If design_state does not exist or the design tree is empty, return NOT READY immediately with a handoff to design-structure.
If design_target_type is missing, return NOT READY immediately with a blocking issue for missing required state.
Assemble a context package containing: design tree text, open branches, decision nodes, existing risks, validation entries, and design_target_type.
Perform a lightweight structural integrity check using the shared rules in ../design-tree-core/REFERENCE.md:
mixed responsibilities inside one tree
parent/child ownership confusion
duplicated parent/child logic on the same branch
branches that likely should have been derived but were kept inline
Phase B: Parallel Readiness Checks

Goal: Run four independent checks in parallel using specialized subagents.

Launch four parallel Sonnet subagents, each using one of the checker agent templates:

branch-checker: reads skills/design-readiness-check/agents/branch-checker.md. Fill {{DESIGN_TREE}} and {{CONTEXT}}.
assumption-checker: reads skills/design-readiness-check/agents/assumption-checker.md. Fill {{DESIGN_TREE}} and {{CONTEXT}}.
failure-checker: reads skills/design-readiness-check/agents/failure-checker.md. Fill {{DESIGN_TREE}} and {{CONTEXT}}.
risk-checker: reads skills/design-readiness-check/agents/risk-checker.md. Fill {{DESIGN_TREE}} and {{CONTEXT}}.

Collect results from all four subagents.

Fallback: If any subagent fails or times out, the main agent performs that check inline using the same rubric from the agent template.

Phase C: Verdict Synthesis

Goal: Combine check results into a clear readiness judgment.

Map each subagent's status to a pass/fail entry in the readiness checklist:

required-state check → "Design target type present"
branch-checker → "Design tree present" and "Key branches refined"
assumption-checker → "Decisions resolved" (if assumptions are unresolved)
failure-checker → "Failure paths documented" and "Validation strategy defined"
risk-checker → "Blocking risks mitigated"
structural integrity check → "Structural integrity preserved"

Build the ✓/✗ checklist diagram following Diagram Conventions.

Determine verdict:

READY: required state is present, all four checks return pass, and no structural integrity issue is blocking
NOT READY: required state is missing, any check returns fail, or structural integrity issues are blocking

If NOT READY, determine the handoff target based on which check failed:

required-state fails → hand off to design-structure
branch-checker fails → hand off to design-structure (branches missing) or design-refinement (branches weak)
assumption-checker fails → hand off to design-refinement (assumptions need expansion)
failure-checker fails → hand off to design-refinement (failure paths need adding)
risk-checker fails → hand off to decision-evaluation (unresolved risk decision) or design-refinement (risk documentation weak)
structural integrity fails → hand off to design-orchestrator (re-route ownership), design-structure (derive a child tree), or design-refinement (shrink duplicated inline logic)

Update design_state with:

status.ready_for_planning: true or false
status.blocking_issues: list from failed checks
Updated open_branches, risks, validation if new information emerged
If a persisted design artifact exists, keep its document status aligned with the verdict: draft for NOT READY, ready-for-planning for READY

Return the explicit verdict with checklist diagram. Never give a "probably ready" answer.

Readiness Standard

A design is ready for planning only when:

design_target_type is present
the main design tree is present
key branches are refined enough to guide implementation for the current target type
major decision nodes are resolved or explicitly deferred with acceptable rationale
failure paths and validation strategy are not missing
blocking risks are either mitigated or clearly acknowledged
tree responsibilities are not mixed in a way that breaks routing clarity
Expected Outputs

Produce or update a design_state that includes:

design_target_type
open_branches
risks
validation
status.ready_for_planning
status.blocking_issues

Always return an explicit result:

ready for planning
not ready for planning

If a persisted design file is part of the workflow, its document status should also be explicit:

draft while the design is not ready
ready-for-planning after the readiness gate passes
Diagram Conventions

Present the readiness verdict as a status checklist inside a code block (no language tag):

Readiness Check
├── Design target type present   ✓
├── Design tree present          ✓
├── Key branches refined         ✓
├── Decisions resolved           ✗ (storage choice pending)
├── Failure paths documented     ✓
├── Validation strategy defined  ✓
├── Blocking risks mitigated     ✗ (migration cutover risk)
└── Structural integrity preserved ✓

Verdict: NOT READY — 2 blocking issues


Rules:

Use ✓ (pass) and ✗ (fail) markers with inline reason for failures
Max width: 78 characters
Always include this checklist in the readiness verdict
Entry and Exit Criteria

Enter when:

the design is near completion
the next meaningful step may be implementation planning

Exit when:

you have issued a clear readiness decision
you have identified the next route if the design is not ready
Handoff Rules
Hand off to writing-plans only when the design is clearly ready.
Hand off to design-structure when foundational branches are still missing.
Hand off to design-refinement when important branches exist but are still weak.
Hand off to decision-evaluation when the real blocker is an unresolved decision node.
Hand off to design-orchestrator when the real blocker is tree ownership or routing drift rather than branch weakness.
Treat missing design_target_type as an immediate blocker, not as a soft warning.
Never give a "probably ready" answer. The result must be explicit.
Weekly Installs
13
Repository
freeacger/loom
GitHub Stars
1
First Seen
Mar 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
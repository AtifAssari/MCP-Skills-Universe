---
rating: ⭐⭐⭐
title: planning-jira-tasks
url: https://skills.sh/b-mendoza/agent-skills/planning-jira-tasks
---

# planning-jira-tasks

skills/b-mendoza/agent-skills/planning-jira-tasks
planning-jira-tasks
Installation
$ npx skills add https://github.com/b-mendoza/agent-skills --skill planning-jira-tasks
SKILL.md
Planning Jira Ticket Tasks

Plan a Jira ticket into a structured execution artifact at docs/<TICKET_KEY>-tasks.md. This skill is the Phase 2 orchestrator in the Jira workflow: it dispatches specialist subagents, validates each artifact boundary, preserves planning artifacts for resume and critique, and returns only concise handoff summaries to the parent workflow. It does not decompose work, prioritize dependencies, or validate plan quality inline.

Compatibility:

Downstream phases use TICKET_KEY-oriented handoffs and paths.
In this workflow, TICKET_KEY is the platform-native work-item identifier, so no alias mapping is required.
For cross-workflow comparison only, treat <KEY> as shorthand for this skill's platform-native work-item identifier. Runtime dispatches and returned summaries still use TICKET_KEY.

All artifact paths in this skill use docs/<TICKET_KEY>….

Inputs
Input	Required	Example
TICKET_KEY	Yes	JNS-6065
RE_PLAN	No	true
DECISIONS	No	SSO decision changes task dependencies

Phase 2 is file-driven, so TICKET_KEY is sufficient. JIRA_URL is not required once the ticket snapshot already exists on disk.

The ticket snapshot must already exist at docs/<TICKET_KEY>.md with these sections, produced by fetching-jira-ticket:

Required section	Why it matters
## Description	Primary source for identifying work items
## Acceptance Criteria	Maps to Definition of Done per task
## Comments	Captures scope changes and clarifications
## Subtasks	Prevents duplicate planning
## Linked Issues	Preserves dependency awareness

Stable context sections (## Metadata, ## Retrieval Warnings, ## Attachments, ## Custom Fields) are also required by the stage-validator preflight and are produced by fetching-jira-ticket even when empty.

If any are missing, treat Phase 1 as incomplete and stop with a preflight failure.

If RE_PLAN=true, reuse the same TICKET_KEY, load ./references/re-plan-cycle.md, and pass the supplied DECISIONS only to the stages that need plan revisions.

This skill is self-contained at runtime. Use this file plus the co-located references/ and subagents/ files as the full execution contract. Treat the documented upstream snapshot artifact and parent workflow handoff as inputs, not as external runtime specs.

Output Contract
Artifact contract

Final artifact path: docs/<TICKET_KEY>-tasks.md

The final plan must contain all of these sections for downstream phases:

Section	Consumed by
## Ticket Summary	clarifying-assumptions
## Execution Order Summary	creating-jira-subtasks
## Problem Framing	clarifying-assumptions, critique paths
## Assumptions and Constraints	clarifying-assumptions
## Cross-Cutting Open Questions	clarifying-assumptions
## Tasks marker section plus separate ## Task N headings	clarifying-assumptions, creating-jira-subtasks, task execution
## Dependency Graph	task execution and critique
## Validation Report	clarifying-assumptions

Each final task entry must include these eight subsections:

**Objective:**
**Relevant requirements and context:**
**Questions to answer before starting:**
**Implementation notes:**
**Definition of done:**
**Likely files / artifacts affected:**
**Dependencies / prerequisites:**
**Priority:**

Add **Dependency rationale:** immediately after **Dependencies / prerequisites:** when a dependency relationship needs a short explanation for downstream execution or review.

Phase 2 does not add ## Decisions Log; that artifact is appended later by Phase 3.

Return handoff

Return only the concise phase handoff below. Use PLANNING: PASS only when PLAN: PASS, PRIORITIZATION: PASS, TASK_VALIDATION: PASS, and every STAGE_VALIDATION gate returned PASS. If any stage-validator dispatch returns STAGE_VALIDATION: ERROR, stop at that gate and return PLANNING: FAIL with the existing stage-specific Failure category; the Reason must explicitly state that the validator errored.

PLANNING: PASS | FAIL
TICKET_KEY: <TICKET_KEY>
File: <final file path or "not written">
Tasks: <N>
Cross-cutting questions: <N>
Validation warnings: <N>
Failure category: PREFLIGHT | STAGE_1 | STAGE_2 | STAGE_3 | POSTPIPELINE | NONE
Reason: <one line>
Artifacts preserved: <comma-separated paths>

Workflow Overview
docs/<TICKET_KEY>.md (ticket snapshot)
       │
       ▼
┌──────────────────────────┐
│  task-planner            │  -> Detailed tasks (what + how)
└────────┬─────────────────┘
         ▼
┌──────────────────────────┐
│  dependency-prioritizer  │  -> Dependencies + execution order
└────────┬─────────────────┘
         ▼
┌──────────────────────────┐
│  task-validator          │  -> Final validated plan + report
└──────────────────────────┘
         │
         ▼
docs/<TICKET_KEY>-tasks.md


Each stage writes a Category A orchestration artifact that stays on disk for Phase 3 critique, targeted retries, and workflow resume:

Stage	File	Produced by
1	docs/<TICKET_KEY>-stage-1-detailed.md	task-planner
2	docs/<TICKET_KEY>-stage-2-prioritized.md	dependency-prioritizer
3	docs/<TICKET_KEY>-tasks.md	task-validator

Preserve these planning artifacts on disk. They support resume and critique workflows, and they stay out of git history as orchestration artifacts.

Subagent Registry
Subagent	Path	Purpose
task-planner	./subagents/task-planner.md	Decompose the ticket and draft the stage 1 plan
dependency-prioritizer	./subagents/dependency-prioritizer.md	Annotate dependencies and determine execution order
task-validator	./subagents/task-validator.md	Validate the prioritized plan and append QA findings
stage-validator	./subagents/stage-validator.md	Check preflight, inter-stage, and final output gates

Read a subagent definition only when you are about to dispatch that subagent. Do not read the stage artifacts inline unless a validator or subagent contract explicitly requires it.

How This Skill Works

This skill does exactly three things:

Dispatch the planning subagents in sequence.
Validate each artifact boundary with stage-validator.
Report only stage verdicts and summary counts to the parent workflow.

The orchestrator keeps only decision-relevant handoff data between stages:

The stage subagent status summary (PLAN, PRIORITIZATION, or TASK_VALIDATION)
The validator verdict
The output file path for the passing stage
The specific issues that failed the current gate
Retry count for the current gate

Do not carry raw plan content forward in the orchestrator context.

Phase Guide

Execution order lives in ## Execution Steps. Use this table as the gate and recovery map when deciding which stage to dispatch or retry next.

Phase / gate	Dispatch	Required output	On failure
preflight	stage-validator	Phase 1 snapshot document is present and complete	Stop on STAGE_VALIDATION: FAIL or STAGE_VALIDATION: ERROR with Failure category: PREFLIGHT
Stage 1	task-planner → stage-validator	PLAN: PASS and docs/<TICKET_KEY>-stage-1-detailed.md passes Stage 1 checks	Stop on PLAN: FAIL, PLAN: BLOCKED, or PLAN: ERROR; retry Stage 1 only on STAGE_VALIDATION: FAIL; stop on STAGE_VALIDATION: ERROR with Failure category: STAGE_1
Stage 2	dependency-prioritizer → stage-validator	PRIORITIZATION: PASS and docs/<TICKET_KEY>-stage-2-prioritized.md passes Stage 2 checks	Stop on PRIORITIZATION: FAIL, PRIORITIZATION: BLOCKED, or PRIORITIZATION: ERROR; retry Stage 2 only on STAGE_VALIDATION: FAIL; stop on STAGE_VALIDATION: ERROR with Failure category: STAGE_2
Stage 3	task-validator → stage-validator	TASK_VALIDATION: PASS and docs/<TICKET_KEY>-tasks.md passes Stage 3 checks	Stop on TASK_VALIDATION: FAIL, TASK_VALIDATION: BLOCKED, or TASK_VALIDATION: ERROR; retry Stage 3 only on STAGE_VALIDATION: FAIL; stop on STAGE_VALIDATION: ERROR with Failure category: STAGE_3
postpipeline	stage-validator	Final downstream contract is intact	Re-dispatch Stage 3, then re-run STAGE=3 and STAGE=postpipeline only on STAGE_VALIDATION: FAIL; stop on STAGE_VALIDATION: ERROR with Failure category: POSTPIPELINE
Execution Paths

Use one of these paths:

Normal path: preflight → stage 1 → stage 2 → stage 3 → postpipeline
Re-plan path: read ./references/re-plan-cycle.md, identify the earliest affected stage, resume from that stage using the preserved on-disk artifacts, then rerun every downstream stage and finish with postpipeline

Use targeted fix loops only. When a gate fails, re-dispatch the stage that produced the failing artifact, pass only the validator's issues list, and re-run only the failing gate. Do not restart already-passing stages unless the re-plan rules require it.

Execution Steps

Choose execution path

If RE_PLAN is absent or false, run the normal path.
If RE_PLAN=true, read ./references/re-plan-cycle.md, determine the earliest affected stage, and resume from that point using the on-disk artifacts from the prior run.
Stop after 3 critique-driven re-plan iterations and escalate instead of looping indefinitely.
This re-plan cap is separate from the per-gate retry cap in Step 7.
Start at Stage 1 when the critique changes ticket interpretation, scope, assumptions, or task decomposition.
Start at Stage 2 when the stage 1 task content is still valid but ordering, dependencies, or priority need to change.
Start at Stage 3 when only the final validated artifact or report needs correction.
After rerunning the earliest affected stage, rerun every downstream stage and finish with the post-pipeline gate. Skip preflight on a re-plan unless the ticket snapshot itself changed or must be revalidated.

Preflight Read the stage-validator definition and dispatch it with:

TICKET_KEY=<TICKET_KEY>
STAGE=preflight
FILE_PATH=docs/<TICKET_KEY>.md

If the validator returns STAGE_VALIDATION: FAIL, stop and return PLANNING: FAIL with Failure category: PREFLIGHT.

If the validator returns STAGE_VALIDATION: ERROR, stop and return PLANNING: FAIL with Failure category: PREFLIGHT. The Reason must explicitly state that the validator errored.

Stage 1 - Plan Read the task-planner definition and dispatch it with:

TICKET_KEY=<TICKET_KEY>
INPUT_PATH=docs/<TICKET_KEY>.md
OUTPUT_PATH=docs/<TICKET_KEY>-stage-1-detailed.md
DECISIONS=<DECISIONS> only when Stage 1 is part of a re-plan
VALIDATION_ISSUES=<issues list> only when retrying Stage 1 after a failed validator gate

If PLAN returns FAIL, BLOCKED, or ERROR, stop and return PLANNING: FAIL with Failure category: STAGE_1.

Then validate stage 1 by reading the stage-validator definition and dispatching it with:

TICKET_KEY=<TICKET_KEY>
STAGE=1
FILE_PATH=docs/<TICKET_KEY>-stage-1-detailed.md

If that validator returns STAGE_VALIDATION: FAIL, apply Step 7 before returning a phase failure.

If that validator returns STAGE_VALIDATION: ERROR, stop and return PLANNING: FAIL with Failure category: STAGE_1. The Reason must explicitly state that the validator errored.

Stage 2 - Prioritize Read the dependency-prioritizer definition and dispatch it with:

TICKET_KEY=<TICKET_KEY>
INPUT_PATH=docs/<TICKET_KEY>-stage-1-detailed.md
OUTPUT_PATH=docs/<TICKET_KEY>-stage-2-prioritized.md
DECISIONS=<DECISIONS> only when Stage 2 is part of a re-plan
VALIDATION_ISSUES=<issues list> only when retrying Stage 2 after a failed validator gate

If PRIORITIZATION returns FAIL, BLOCKED, or ERROR, stop and return PLANNING: FAIL with Failure category: STAGE_2.

Then validate stage 2 by reading the stage-validator definition and dispatching it with:

TICKET_KEY=<TICKET_KEY>
STAGE=2
FILE_PATH=docs/<TICKET_KEY>-stage-2-prioritized.md

If that validator returns STAGE_VALIDATION: FAIL, apply Step 7 before returning a phase failure.

If that validator returns STAGE_VALIDATION: ERROR, stop and return PLANNING: FAIL with Failure category: STAGE_2. The Reason must explicitly state that the validator errored.

Stage 3 - Validate Read the task-validator definition and dispatch it with:

TICKET_KEY=<TICKET_KEY>
SNAPSHOT_PATH=docs/<TICKET_KEY>.md
PLAN_PATH=docs/<TICKET_KEY>-stage-2-prioritized.md
OUTPUT_PATH=docs/<TICKET_KEY>-tasks.md
VALIDATION_ISSUES=<issues list> only when retrying Stage 3 or repairing a failed post-pipeline gate

If TASK_VALIDATION returns FAIL, BLOCKED, or ERROR, stop and return PLANNING: FAIL with Failure category: STAGE_3.

Then validate stage 3 by reading the stage-validator definition and dispatching it with:

TICKET_KEY=<TICKET_KEY>
STAGE=3
FILE_PATH=docs/<TICKET_KEY>-tasks.md

If that validator returns STAGE_VALIDATION: FAIL, apply Step 7 before returning a phase failure.

If that validator returns STAGE_VALIDATION: ERROR, stop and return PLANNING: FAIL with Failure category: STAGE_3. The Reason must explicitly state that the validator errored.

Post-pipeline gate Read the stage-validator definition and dispatch it with:

TICKET_KEY=<TICKET_KEY>
STAGE=postpipeline
FILE_PATH=docs/<TICKET_KEY>-tasks.md

This confirms the full output contract for downstream phases.

If that validator returns STAGE_VALIDATION: FAIL, apply Step 7.

If that validator returns STAGE_VALIDATION: ERROR, stop and return PLANNING: FAIL with Failure category: POSTPIPELINE. The Reason must explicitly state that the validator errored.

Targeted retry loop This loop applies only to STAGE_VALIDATION: FAIL results for Stage 1, Stage 2, Stage 3, and postpipeline. STAGE_VALIDATION: ERROR is terminal at the current gate and never enters this loop. Preflight failures are terminal per Step 2. If a stage subagent returns PLAN: FAIL | BLOCKED | ERROR, PRIORITIZATION: FAIL | BLOCKED | ERROR, or TASK_VALIDATION: FAIL | BLOCKED | ERROR, stop and return PLANNING: FAIL. Re-plan iterations and per-gate retry cycles are tracked separately.

For any failing validator gate:

Collect only the validator's issues list.
Re-dispatch only the stage that produced that artifact.
Pass the original inputs plus VALIDATION_ISSUES=<issues list>.
Re-run only the previously failing validator gate.
If the failed gate is postpipeline, re-dispatch Stage 3 with VALIDATION_ISSUES, then rerun STAGE=3 and STAGE=postpipeline.
Stop after 3 failed cycles for the same gate and return PLANNING: FAIL with the relevant failure category.

Report On success, return the completion handoff from ## Output Contract. Include the final file path, task count, cross-cutting question count, warning count, and the preserved artifact paths. State explicitly that planning is complete and implementation has not started.

Example

Dispatch stage-validator with STAGE=preflight, TICKET_KEY=JNS-6065, FILE_PATH=docs/JNS-6065.md -> PASS

Dispatch task-planner with TICKET_KEY=JNS-6065, INPUT_PATH=docs/JNS-6065.md, OUTPUT_PATH=docs/JNS-6065-stage-1-detailed.md -> wrote stage 1 artifact

Validate stage 1 -> PASS

Dispatch dependency-prioritizer with TICKET_KEY=JNS-6065, INPUT_PATH=docs/JNS-6065-stage-1-detailed.md, OUTPUT_PATH=docs/JNS-6065-stage-2-prioritized.md -> wrote stage 2 artifact

Validate stage 2 -> PASS

Dispatch task-validator with TICKET_KEY=JNS-6065, SNAPSHOT_PATH=docs/JNS-6065.md, PLAN_PATH=docs/JNS-6065-stage-2-prioritized.md, OUTPUT_PATH=docs/JNS-6065-tasks.md -> wrote final plan

Dispatch stage-validator with TICKET_KEY=JNS-6065, STAGE=3, FILE_PATH=docs/JNS-6065-tasks.md -> PASS

Dispatch stage-validator with TICKET_KEY=JNS-6065, STAGE=postpipeline, FILE_PATH=docs/JNS-6065-tasks.md -> PASS

Return:

PLANNING: PASS TICKET_KEY: JNS-6065 File: docs/JNS-6065-tasks.md Tasks: 7 Cross-cutting questions: 3 Validation warnings: 1 Failure category: NONE Reason: Final plan validated and ready for Phase 3. Artifacts preserved: docs/JNS-6065-stage-1-detailed.md, docs/JNS-6065-stage-2-prioritized.md, docs/JNS-6065-tasks.md

Weekly Installs
45
Repository
b-mendoza/agent-skills
First Seen
Mar 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
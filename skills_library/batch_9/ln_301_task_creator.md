---
title: ln-301-task-creator
url: https://skills.sh/levnikolaevich/claude-code-skills/ln-301-task-creator
---

# ln-301-task-creator

skills/levnikolaevich/claude-code-skills/ln-301-task-creator
ln-301-task-creator
Installation
$ npx skills add https://github.com/levnikolaevich/claude-code-skills --skill ln-301-task-creator
SKILL.md

Paths: File paths (shared/, references/, ../ln-*) are relative to skills repo root. If not found at CWD, locate this SKILL.md directory and go up one level for repo root.

Task Creator

Type: L3 Worker Category: 3XX Planning

Standalone-first worker for task creation. It creates tasks from an already approved plan and returns a stable summary contract.

MANDATORY READ: Load shared/references/coordinator_summary_contract.md and shared/references/task_plan_worker_runtime_contract.md MANDATORY READ: Load shared/references/environment_state_contract.md, shared/references/storage_mode_detection.md, shared/references/template_loading_pattern.md, shared/references/creation_quality_checklist.md, and shared/references/destructive_operation_safety.md

Inputs

Core inputs:

taskType
storyData
idealPlan — task list with scopes, AC mappings, dependencies, layer classifications
teamId
guideLinks

Coordinator context (passed in ADD/CREATE mode):

traceabilityTablePath — materialized traceability table from coordinator Phase 2
discoveryContext — architecture, tech stack, key files, integration points from coordinator Phase 1
tasksToCreate — specific tasks to create (ADD mode). Worker writes the 7-section document, does not decide whether tasks are needed.

Transport inputs:

standalone: omit runId and summaryArtifactPath
managed: pass both runId and summaryArtifactPath
Runtime

Runtime family: task-plan-worker-runtime

Phase profile:

PHASE_0_CONFIG
PHASE_1_LOAD_INPUTS
PHASE_2_LOAD_CONTEXT
PHASE_3_GENERATE_TASK_DOCS
PHASE_4_VALIDATE_TASKS
PHASE_5_CONFIRM_OR_AUTOAPPROVE
PHASE_6_APPLY_CREATE
PHASE_7_UPDATE_KANBAN
PHASE_8_WRITE_SUMMARY
PHASE_9_SELF_CHECK

Summary artifact rules:

emit summary_kind=task-plan
standalone runs generate their own run_id and write the default worker-family artifact path
managed runs require both runId and summaryArtifactPath and must write the summary to the exact provided path
always write the validated summary artifact before terminal outcome
Output Contract

Always build a structured task-plan summary envelope per:

shared/references/coordinator_summary_contract.md
shared/references/task_plan_worker_runtime_contract.md

Payload fields:

mode
story_id
task_type
tasks_created
tasks_updated
tasks_canceled
task_urls
kanban_updated
dry_warnings_count
warnings

Always write the validated summary before terminal outcome.

Workflow
Resolve task provider and template set.
Run DRY and destructive-operation checks where applicable.
Use coordinator context (discoveryContext, traceabilityTablePath) to understand architecture. Research codebase for implementation details (existing patterns, related files, integration points) to write good Technical Approach sections.
Select scope:
ADD: use tasksToCreate only
CREATE: expand the full idealPlan
Generate task documents from the selected scope.
Validate type-specific rules.
Show preview and get confirmation if needed.
Create tasks in Linear or file mode.
Update kanban.
Return structured summary.
Critical Rules
Remain standalone-capable.
Do not require coordinator runtime state.
Keep implementation, refactoring, and test rules separated by taskType.
Write machine-readable summary output every time.
Ideal plan is binding. Create every task in the approved plan. Do not re-evaluate whether tasks should exist.
Fast path for ADD: tasksToCreate is the execution scope. Do not re-expand the full ideal plan when the coordinator already selected the delta.
STOP before save_issue: verify all 7 sections present in body: Context, Implementation Plan, Technical Approach, Acceptance Criteria, Affected Components, Existing Code Impact, Definition of Done. PreToolUse hook will BLOCK creation without them.
Definition of Done
 Templates loaded
 Task documents generated
 Type-specific validation passed
 Tasks created in provider-specific storage
 kanban updated
 Structured summary returned
 Summary artifact written to the managed or standalone runtime path

Version: 3.0.0 Last Updated: 2025-12-23

Weekly Installs
279
Repository
levnikolaevich/…e-skills
GitHub Stars
445
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
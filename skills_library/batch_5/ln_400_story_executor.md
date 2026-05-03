---
title: ln-400-story-executor
url: https://skills.sh/levnikolaevich/claude-code-skills/ln-400-story-executor
---

# ln-400-story-executor

skills/levnikolaevich/claude-code-skills/ln-400-story-executor
ln-400-story-executor
Installation
$ npx skills add https://github.com/levnikolaevich/claude-code-skills --skill ln-400-story-executor
SKILL.md

Paths: File paths (shared/, references/, ../ln-*) are relative to skills repo root. If not found at CWD, locate this SKILL.md directory and go up one level for repo root. If shared/ is missing, fetch files via WebFetch from https://raw.githubusercontent.com/levnikolaevich/claude-code-skills/master/skills/{path}.

Type: L2 Coordinator Category: 4XX Execution

Story Execution Orchestrator

Runtime-backed coordinator for Story execution. Owns task ordering, worktree lifecycle, task/group checkpoints, and the final Story transition to To Review.

Inputs
Input	Required	Source	Description
storyId	Yes	args, git branch, kanban, user	Story to process
--rework-focus	No	ln-1000	Comma-separated blocking categories from prior quality gate FAIL

Resolution: Story Resolution Chain.
Status filter: Todo, In Progress, To Rework, To Review

Purpose & Scope
Load Story and task metadata once per loop
Execute in order: To Review -> To Rework -> Todo
Launch Todo parallel groups only when explicitly marked
Force immediate review after every executor/rework step
Persist resumable runtime state in .hex-skills/story-execution/runtime/
Move Story only to To Review; never to Done
Runtime Contract

MANDATORY READ: Load shared/references/environment_state_contract.md, shared/references/storage_mode_detection.md, shared/references/input_resolution_pattern.md MANDATORY READ: Load shared/references/coordinator_runtime_contract.md, shared/references/story_execution_runtime_contract.md, shared/references/coordinator_summary_contract.md, shared/references/loop_health_contract.md MANDATORY READ: Load shared/references/git_worktree_fallback.md — use the Story execution row

Runtime CLI:

node shared/scripts/story-execution-runtime/cli.mjs start --story {storyId} --manifest-file .hex-skills/story-execution/manifest.json
node shared/scripts/story-execution-runtime/cli.mjs status
node shared/scripts/story-execution-runtime/cli.mjs checkpoint --phase PHASE_3_SELECT_WORK --payload '{...}'
node shared/scripts/story-execution-runtime/cli.mjs record-worker --task-id {taskId} --payload '{...}'
node shared/scripts/story-execution-runtime/cli.mjs record-group --group-id {groupId} --payload '{...}'
node shared/scripts/story-execution-runtime/cli.mjs record-stage-summary --story {storyId} --payload '{...}'
node shared/scripts/story-execution-runtime/cli.mjs record-loop-health --scope task --scope-id {taskId} --payload '{...}'
node shared/scripts/story-execution-runtime/cli.mjs advance --to PHASE_4_TASK_EXECUTION

Workflow
Phase 0: Config
Resolve storyId.
Detect task_provider from task-management config.
Build execution manifest:
story_id
task_provider
project_root
planned worktree_dir
branch name
parallel_group_policy
status_transition_policy
Start runtime and checkpoint PHASE_0_CONFIG.
Phase 1: Discovery
Resolve Story title and current Story status.
Load child task metadata only:
Linear: list_issues(parentId=storyId)
File mode: parse task files and **Status:**
Build processable_counts for:
to_review
to_rework
todo
Checkpoint PHASE_1_DISCOVERY.
Phase 2: Worktree Setup
Detect current branch.
If already inside feature/*, treat current directory as active worktree.
Otherwise create .hex-skills/worktrees/story-{identifier} and branch feature/{identifier}-{slug} per worktree fallback guide.
Checkpoint PHASE_2_WORKTREE_SETUP with:
worktree_ready
worktree_dir
branch
Advance only after worktree_ready=true.
Phase 3: Select Work

Selection order is deterministic:

Any To Review task first, sequentially
Then any To Rework task, sequentially
Then Todo tasks:
tasks with **Parallel Group:** {N} may run as one group
tasks without a group are single-task sequential units

Checkpoint PHASE_3_SELECT_WORK with:

current_task_id or current_group_id
fresh processable_counts

If all processable counts are zero, skip execution and advance to PHASE_7_STORY_TO_REVIEW.

When rework_focus is provided:

Tasks whose title or AC keywords match any blocking_categories entry are selected first within the same priority tier.
This does not override the To Review > To Rework > Todo ordering — it reorders within each tier.
Phase 4: Task Execution

Used for:

To Review -> ln-402
To Rework -> ln-403, then immediate ln-402
single Todo test task -> ln-404, then immediate ln-402
single Todo impl/refactor task -> ln-401, then immediate ln-402

Flow:

Compute executor childRunId = {parent_run_id}--{worker}--{taskId}.
Compute executor artifact path .hex-skills/runtime-artifacts/runs/{parent_run_id}/task-status/{taskId}--{worker}.json.
Materialize executor manifest at .hex-skills/story-execution/{worker}--{taskId}_manifest.json.
Start task-worker-runtime and checkpoint executor child_run metadata before invocation.
Execute the worker through Agent or Skill with --run-id and --summary-artifact-path.
Read the executor summary artifact from .hex-skills/runtime-artifacts/runs/{parent_run_id}/task-status/{taskId}--{worker}.json.
Record task loop health before retrying the same task/worker/error:
Action: compare current worker output with previous task loop health.
Key point: retry only when new artifact, new ln-402 summary, task status delta, files_changed delta, or scenario improvement exists.
Why: repeated identical worker failures create retry storms without adding evidence.
Evidence: record-loop-health --scope task --scope-id {taskId} result.
Exception: if pause.pause=true, stop and surface paused_reason.
Automation/guard: story-execution runtime pauses after same-error/no-progress threshold.
When review is required, repeat the same runtime-backed sequence for ln-402.
Read the latest ln-402 review summary artifact for the same task from .hex-skills/runtime-artifacts/runs/{parent_run_id}/task-status/{taskId}--ln-402.json.
Record worker artifacts with record-worker.
Checkpoint PHASE_4_TASK_EXECUTION.
Advance to PHASE_6_VERIFY_STATUSES.
Phase 5: Group Execution

Used only for Todo groups with more than one task.

For each task, compute worker-specific child runId, artifact path, and manifest path.
Start one task-worker-runtime per executor and checkpoint all child metadata before spawning Agents.
Spawn all group executors in parallel via Agent tool.
Wait for all executors to finish.
Read each executor summary artifact.
Start one ln-402 runtime per task, review each task sequentially, and read the latest review artifact for every task.
Record each worker artifact with record-worker, then record the group summary with record-group.
Checkpoint PHASE_5_GROUP_EXECUTION.
Advance to PHASE_6_VERIFY_STATUSES.
Phase 6: Verify Statuses
Re-read task metadata from source of truth.
Refresh processable_counts.
Validate that every task touched in this run has a latest ln-402 machine-readable summary.
If any worker leaves an unexpected transition, pause runtime.
If any task hits To Rework for the third consecutive time, pause runtime with escalation reason.
Checkpoint PHASE_6_VERIFY_STATUSES.
If processable work remains -> advance back to PHASE_3_SELECT_WORK.
If no processable work remains -> advance to PHASE_6B_SCENARIO_VALIDATION.
Scenario Validation

Runs once when all tasks are Done. Delegates to an external agent to trace the user scenario end-to-end against implemented code. The executor has completion bias after shepherding tasks through implementation — an external agent has no investment in the story being done.

Load the Story ACs and the traceability table (from .hex-skills/task-planning/{identifier}_traceability.md). If the traceability artifact is missing, reconstruct an equivalent trace from the Story ACs and task Implementation Plans — do not fail scenario validation solely because the planner artifact is absent.

Run agent health check. If an advisor agent is available: a. Build validation prompt from shared/agents/prompt_templates/scenario_validator.md b. Fill with: Story ACs, traceability table, architecture context, project root path (agent reads code directly) c. Save prompt to .hex-skills/story-execution/{identifier}_scenario_prompt.md d. Launch agent:

node shared/agents/agent_runner.mjs \
  --agent {agent} \
  --prompt-file .hex-skills/story-execution/{identifier}_scenario_prompt.md \
  --output-file .hex-skills/story-execution/{identifier}_scenario_result.md \
  --cwd {project_dir}


e. Parse result JSON for broken segments

If no agent available: run self-check as fallback (trace 5 segments via code inspection).

If any segment is broken or missing:

Identify the responsible task from traceability table layer mapping
Record scenario loop health keyed by broken segment before setting another rework
If the same broken segment returns without code/artifact delta, pause instead of reworking blindly
Set that task back to To Rework with scenario findings as rework context
Advance back to PHASE_3_SELECT_WORK

Max 2 scenario validation loops. If still failing after 2 rework cycles, PAUSE for user review.

If all segments pass -> advance to PHASE_7_STORY_TO_REVIEW.

Checkpoint PHASE_6B_SCENARIO_VALIDATION with:

scenario_pass: true/false
segments_traced: count
segments_passed: count
rework_tasks: list of task IDs sent back (empty if pass)
validation_mode: agent_validated or self_check_only
Phase 7: Story To Review
Verify no tasks remain in Todo, To Review, or To Rework.
Update Story status to To Review.
Update kanban to To Review.
Checkpoint PHASE_7_STORY_TO_REVIEW with:
story_transition_done=true
story_final_status="To Review"
final_result="READY_FOR_GATE"
Write Stage 2 coordinator artifact with:
summary_kind=pipeline-stage
stage=2
story_id
status=completed
final_result="READY_FOR_GATE"
story_status="To Review"
warnings
Phase 8: Self-Check

Build final checklist from runtime state, not memory:

 Config checkpoint exists
 Discovery checkpoint exists
 Worktree checkpoint exists and worktree_ready=true
 Every executed task has a latest ln-402 summary artifact
 Every processed group has a recorded runtime result
 Rework loop guard did not trip
 Story moved to To Review
 Stage 2 coordinator artifact recorded

Checkpoint PHASE_8_SELF_CHECK with pass=true|false. Complete runtime only after pass=true.

Worker Invocation (MANDATORY)
Status	Worker	Invocation
To Review	ln-402-task-reviewer	Inline via Skill()
To Rework	ln-403-task-rework	Agent, then immediate ln-402
Todo tests	ln-404-test-executor	Agent, then immediate ln-402
Todo impl/refactor	ln-401-task-executor	Agent, then immediate ln-402

Executors and reworkers run isolated:

node shared/scripts/task-worker-runtime/cli.mjs start --skill {worker} --task-id {taskId} --manifest-file .hex-skills/story-execution/{worker}--{taskId}_manifest.json --run-id {childRunId} --summary-artifact-path .hex-skills/runtime-artifacts/runs/{parent_run_id}/task-status/{taskId}--{worker}.json
node shared/scripts/story-execution-runtime/cli.mjs checkpoint --phase PHASE_4_TASK_EXECUTION --payload '{"child_run":{"worker":"{worker}","task_id":"{taskId}","run_id":"{childRunId}","summary_artifact_path":".hex-skills/runtime-artifacts/runs/{parent_run_id}/task-status/{taskId}--{worker}.json"}}'
Agent(
  description: "Execute task {taskId}",
  prompt: "Execute task worker.\n\nStep 1: Invoke worker:\n  Skill(skill: \"{worker}\", args: \"{taskId} --run-id {childRunId} --summary-artifact-path .hex-skills/runtime-artifacts/runs/{parent_run_id}/task-status/{taskId}--{worker}.json\")\n\nCONTEXT:\nTask ID: {taskId}",
  subagent_type: "general-purpose"
)


Reviewer runs inline:

node shared/scripts/task-worker-runtime/cli.mjs start --skill ln-402 --task-id {taskId} --manifest-file .hex-skills/story-execution/ln-402--{taskId}_manifest.json --run-id {reviewRunId} --summary-artifact-path .hex-skills/runtime-artifacts/runs/{parent_run_id}/task-status/{taskId}--ln-402.json
node shared/scripts/story-execution-runtime/cli.mjs checkpoint --phase PHASE_4_TASK_EXECUTION --payload '{"child_run":{"worker":"ln-402","task_id":"{taskId}","run_id":"{reviewRunId}","summary_artifact_path":".hex-skills/runtime-artifacts/runs/{parent_run_id}/task-status/{taskId}--ln-402.json"}}'
Skill(skill: "ln-402-task-reviewer", args: "{taskId} --run-id {reviewRunId} --summary-artifact-path .hex-skills/runtime-artifacts/runs/{parent_run_id}/task-status/{taskId}--ln-402.json")

TodoWrite format (mandatory)
- Start ln-400 runtime (pending)
- Load Story/task metadata (pending)
- Setup or detect worktree (pending)
- Select next task/group (pending)
- Start child runtime(s) and checkpoint child metadata (pending)
- Execute task/group with managed transport inputs (pending)
- Review task results immediately (pending)
- Re-read statuses and record checkpoint (pending)
- Validate user scenario end-to-end (pending)
- Move Story to To Review (pending)
- Run runtime self-check and complete (pending)

Critical Rules
Runtime state is the orchestration SSOT; kanban is the task-status SSOT.
Never batch reviews.
Never move Story to Done.
Every worker outcome must be read from summary JSON, not from prose-only chat.
record-worker is the primary runtime ingestion path for worker outcomes.
record-loop-health is the primary retry-usefulness ingestion path before repeating task/group/scenario work.
Every managed worker run must be started through task-worker-runtime before invocation.
ln-1000 consumes the Stage 2 coordinator artifact, not free-text stage output.
Reviews remain sequential even when execution groups are parallel.
ln-402 remains the only worker that can accept a task as Done.
Definition of Done
 Runtime started and PHASE_0_CONFIG checkpointed
 Discovery and worktree setup checkpointed
 Every executed task/group recorded in runtime
 Rework-loop escalation handled deterministically (PAUSED) when needed
 Final status verification checkpointed
 Scenario validation passed or PAUSED for user review
 Story moved to To Review, not Done
 Self-check passed and runtime completed
Phase 9: Meta-Analysis

MANDATORY READ: Load shared/references/meta_analysis_protocol.md

Skill type: execution-orchestrator. Run after phases complete. Output to chat using the execution-orchestrator format.

Reference Files
shared/references/coordinator_runtime_contract.md
shared/references/story_execution_runtime_contract.md
shared/references/coordinator_summary_contract.md
shared/references/git_worktree_fallback.md
../ln-401-task-executor/SKILL.md
../ln-402-task-reviewer/SKILL.md
../ln-403-task-rework/SKILL.md
../ln-404-test-executor/SKILL.md

Version: 4.0.0 Last Updated: 2026-01-29

Weekly Installs
272
Repository
levnikolaevich/…e-skills
GitHub Stars
445
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
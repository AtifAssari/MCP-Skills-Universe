---
rating: ⭐⭐⭐
title: super-swarm-spark
url: https://skills.sh/am-will/codex-skills/super-swarm-spark
---

# super-swarm-spark

skills/am-will/codex-skills/super-swarm-spark
super-swarm-spark
Installation
$ npx skills add https://github.com/am-will/codex-skills --skill super-swarm-spark
Summary

Orchestrates parallel task execution across up to 12 concurrent Sparky subagents using a rolling pool scheduler.

Parses markdown plan files, extracts task definitions, and launches subagents continuously as slots open without waiting for batch completion
Maintains canonical file paths and naming constraints across parallel tasks to prevent filename drift and cross-task conflicts
Validates each subagent result, updates the plan file with completion logs, and immediately schedules the next pending task to keep concurrency maxed
Performs final integration pass after all tasks complete: reconciles conflicts, runs tests, fixes failures, and ensures the full codebase converges to plan expectations
Requires explicit agent_type: sparky for all subagent launches; stops and reports if a task needs paths outside its pre-built context pack
SKILL.md
Parallel Task Executor (Sparky Rolling 12-Agent Pool)

You are an Orchestrator for subagents. Parse plan files and delegate tasks in parallel using a rolling pool of up to 15 concurrent Sparky subagents. Keep launching new work whenever a slot opens until the plan is fully complete.

Primary orchestration goals:

Keep the project moving continuously
Ignore dependency maps
Keep up to 15 agents running whenever pending work exists
Give every subagent maximum path/file context
Prevent filename/folder-name drift across parallel tasks
Check every subagent result
Ensure the plan file is updated as tasks complete
Perform final integration fixes after all task execution
Add/adjust tests, then run tests and fix failures
Process
Step 1: Parse Request

Extract from user request:

Plan file: The markdown plan to read
Task subset (optional): Specific task IDs to run

If no subset provided, run the full plan.

Step 2: Read & Parse Plan
Find task subsections (e.g., ### T1: or ### Task 1.1:)
For each task, extract:
Task ID and name
Task linkage metadata for context only
Full content (description, location, acceptance criteria, validation)
Build task list
If a task subset was requested, filter to only those IDs.
Step 3: Build Context Pack Per Task

Before launching a task, prepare a context pack that includes:

Canonical file paths and folder paths the task must touch
Planned new filenames (exact names, not suggestions)
Neighboring tasks that touch the same files/folders
Naming constraints and conventions from the plan/repo
Any known cross-task expectations that could cause conflicts

Rules:

Do not allow subagents to invent alternate file names for the same intent.
Require explicit file targets in every subagent assignment.
If a subagent needs a new file not in its context pack, it must report this before creating it.
Step 4: Launch Subagents (Rolling Pool, Max 12)

Run a rolling scheduler:

States: pending, running, completed, failed
Launch up to 12 tasks immediately (or fewer if less are pending)
Whenever any running task finishes, validate/update plan for that task, then launch the next pending task immediately
Continue until no pending or running tasks remain

For each launched task, use:

agent_type: sparky (Sparky role)
description: "Implement task [ID]: [name]"
prompt: Use template below

Do not wait for grouped batches. The only concurrency limit is 12 active Sparky subagents.

Every launch must set agent_type: sparky. Any other role is invalid for this skill.

Task Prompt Template
You are implementing a specific task from a development plan.

## Context
- Plan: [filename]
- Goals: [relevant overview from plan]
- Task relationships: [related metadata for awareness only, never as a blocker]
- Canonical folders: [exact folders to use]
- Canonical files to edit: [exact paths]
- Canonical files to create: [exact paths]
- Shared-touch files: [files touched by other tasks in parallel]
- Naming rules: [repo/plan naming constraints]
- Constraints: [risks from plan]

## Your Task
**Task [ID]: [Name]**

Location: [File paths]
Description: [Full description]

Acceptance Criteria:
[List from plan]

Validation:
[Tests or verification from plan]

## Instructions
- Use the `sparky` agent role for this task; do not use any other role.
1. Examine the plan and all listed canonical paths before editing
2. Implement changes for all acceptance criteria
3. Keep work atomic and committable
4. For each file: read first, edit carefully, preserve formatting
5. Do not create alternate filename variants; use only the provided canonical names
6. If you need to touch/create a path not listed, stop and report it first
7. Run validation if feasible
8. ALWAYS mark completed tasks IN THE *-plan.md file AS SOON AS YOU COMPLETE IT! and update with:
   - Concise work log
   - Files modified/created
   - Errors or gotchas encountered
9. Commit your work
   - Note: There are other agents working in parallel to you, so only stage and commit the files you worked on. NEVER PUSH. ONLY COMMIT.
10. Double check that you updated the *-plan.md file and committed your work before yielding
11. Return summary of:
   - Files modified/created (exact paths)
   - Changes made
   - How criteria are satisfied
   - Validation performed or deferred

## Important
- Be careful with paths
- Follow canonical naming exactly
- Stop and describe blockers if encountered
- Focus on this specific task

Step 5: Validate Every Completion

As each subagent finishes:

Inspect output for correctness and completeness.
Validate against expected outcomes for that task.
Ensure plan file completion state + logs were updated correctly.
Retry/escalate on failure.
Keep scheduler full: after validation, immediately launch the next pending task if a slot is open.
Step 6: Final Orchestrator Integration Pass

After all subagents are done:

Reconcile parallel-work conflicts and cross-task breakage.
Resolve duplicate/variant filenames and converge to canonical paths.
Ensure the plan is fully and accurately updated.
Add or adjust tests to cover integration/regression gaps.
Run required tests.
Fix failures.
Re-run tests until green (or report explicit blockers with evidence).

Completion bar:

All plan tasks marked complete with logs
Integrated codebase builds/tests per plan expectations
No unresolved path/name divergence introduced by parallel execution
Scheduling Policy (Required)
Max concurrent subagents: 12
If pending tasks exist and running count is below 12: launch more immediately
Do not pause due to relationship metadata
Continue until the full plan (or requested subset) is complete and integrated
Error Handling
Task subset not found: List available task IDs
Parse failure: Show what was tried, ask for clarification
Path ambiguity across tasks: pick one canonical path, announce it, and enforce it in all task prompts
Example Usage
'Implement the plan using super-swarm'
/super-swarm-spark plan.md
/super-swarm-spark ./plans/auth-plan.md T1 T2 T4
/super-swarm-spark user-profile-plan.md --tasks T3 T7

Execution Summary Template
# Execution Summary

## Tasks Assigned: [N]

## Concurrency
- Max workers: 12
- Scheduling mode: rolling pool (continuous refill)

### Completed
- Task [ID]: [Name] - [Brief summary]

### Issues
- Task [ID]: [Name]
  - Issue: [What went wrong]
  - Resolution: [How resolved or what's needed]

### Blocked
- Task [ID]: [Name]
  - Blocker: [What's preventing completion]
  - Next Steps: [What needs to happen]

## Integration Fixes
- [Conflict or regression]: [Fix]

## Tests Added/Updated
- [Test file]: [Coverage added]

## Validation Run
- [Command]: [Pass/Fail + key output]

## Overall Status
[Completion summary]

## Files Modified
[List of changed files]

## Next Steps
[Recommendations]

Weekly Installs
1.1K
Repository
am-will/codex-skills
GitHub Stars
907
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
---
rating: ⭐⭐⭐
title: spec:bg
url: https://skills.sh/cloudvoyant/codevoyant/spec:bg
---

# spec:bg

skills/cloudvoyant/codevoyant/spec:bg
spec:bg
Installation
$ npx skills add https://github.com/cloudvoyant/codevoyant --skill spec:bg
SKILL.md

Compatibility: If AskUserQuestion is unavailable, present options as a numbered list and wait for the user's reply. If Task is unavailable, run parallel steps sequentially. The context: fork and agent: frontmatter fields are Claude Code-specific — on OpenCode and VS Code Copilot they are ignored and the skill runs inline using the current model.

Execute the plan in the background using an autonomous agent.

Overview

This command launches a long-running agent that executes your plan autonomously while you continue working. The agent updates progress in real-time and pauses on errors.

Step 0: Parse Arguments and Flags
PLAN_NAME="[first non-flag argument, or empty]"
AUTO_APPROVE=false; ALLOW_COMMITS=false; SILENT=false
[[ "$*" =~ --yes|-y ]]    && AUTO_APPROVE=true
[[ "$*" =~ --commit|-c ]] && ALLOW_COMMITS=true
[[ "$*" =~ --silent ]]    && SILENT=true

Step 0.5: Select Plan

If plan name not provided in arguments:

If not provided:

Get all active plans with Last Updated timestamps:
npx @codevoyant/agent-kit plans migrate
npx @codevoyant/agent-kit plans list --status Active

Sort plans by Last Updated (most recent first)
If only one plan exists, auto-select it
If multiple plans exist, use AskUserQuestion to present the list (name, progress %, last-updated) and ask the user to choose. Example prompt: "Which plan would you like to work on?\n (1) feature-auth — 60% — updated 2h ago\n (2) refactor-api — 20% — updated 1d ago"
Report to user: "Using plan: {plan-name} (last updated: {timestamp})"
If no plans exist, inform user to create with /new
Step 1: Verify Plan Exists
Check that .codevoyant/plans/{plan-name}/plan.md exists
If not found, inform user to create one with /new or /init
Step 2: Analyze Plan Scope

Read .codevoyant/plans/{plan-name}/plan.md and report:

Total number of phases
Total number of tasks
Starting point (first unchecked task)
Estimated complexity

Example:

Plan: {plan-name} - Authentication System
- 4 phases, 23 tasks
- Starting from: Phase 1, Task 1
- Complexity: Medium (has test requirements)

Step 2.5: Validate and Setup Worktree Context

Handle worktree-based execution automatically:

# Get current branch and working directory
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)
CURRENT_DIR=$(pwd)

# Parse plan metadata
PLAN_BRANCH=$(grep "^- \*\*Branch\*\*:" .codevoyant/plans/{plan-name}/plan.md | sed 's/^- \*\*Branch\*\*: //' | sed 's/ *$//')
PLAN_WORKTREE=$(grep "^- \*\*Worktree\*\*:" .codevoyant/plans/{plan-name}/plan.md | sed 's/^- \*\*Worktree\*\*: //' | sed 's/ *$//')

# Determine worktree status
if [ -n "$PLAN_WORKTREE" ] && [ "$PLAN_WORKTREE" != "(none)" ]; then
  # Plan has worktree specified
  if [ -d "$PLAN_WORKTREE" ]; then
    WORKTREE_EXISTS=true
  else
    WORKTREE_EXISTS=false
  fi
else
  # No worktree for this plan
  WORKTREE_EXISTS=""
fi


Case 1: Worktree exists → Auto-execute there

If WORKTREE_EXISTS=true:

✓ Plan has worktree at: $PLAN_WORKTREE
→ Executing in worktree automatically...


Then continue to Step 3 with this context:

Set execution directory to $PLAN_WORKTREE
When launching agent (Step 6), pass worktree path as working directory
Agent will execute in worktree isolation
No manual cd required!

Case 2: Worktree specified but doesn't exist → Offer to create

If WORKTREE_EXISTS=false:

If AUTO_APPROVE is true:

Automatically create worktree without asking
Report: → Auto-creating worktree with --yes flag
Create worktree: git worktree add -b "$PLAN_BRANCH" "$PLAN_WORKTREE" HEAD
Update .gitignore if needed
Report: ✓ Created worktree at $PLAN_WORKTREE
Set execution directory to $PLAN_WORKTREE
Continue to Step 3

If AUTO_APPROVE is false:

Use AskUserQuestion tool:

question: "This plan needs worktree '$PLAN_WORKTREE' (branch: $PLAN_BRANCH) but it doesn't exist. Create it now?"
header: "Worktree Setup"
multiSelect: false
options:
  - label: "Create worktree and execute"
    description: "Create worktree at $PLAN_WORKTREE, then start execution there"
  - label: "Execute here anyway"
    description: "Skip worktree, execute in current directory (may cause issues)"
  - label: "Cancel"
    description: "Don't execute, let me set it up manually"


Handle response:

"Create worktree and execute":

Create worktree: git worktree add -b "$PLAN_BRANCH" "$PLAN_WORKTREE" HEAD
Update .gitignore if needed
Report: ✓ Created worktree at $PLAN_WORKTREE
Set execution directory to $PLAN_WORKTREE
Continue to Step 3

"Execute here anyway":

Warn: ⚠️ Executing without worktree - changes will affect current branch
Continue to Step 3 (execute in current directory)

"Cancel":

Exit command

Case 3: No worktree for plan → Execute in current directory

If plan has no worktree (PLAN_WORKTREE is "(none)" or empty):

Check if branch matches (if PLAN_BRANCH specified)
If branch mismatch, offer to switch: git checkout $PLAN_BRANCH
Otherwise continue to Step 3 normally

Summary:

Worktree exists → Execute there automatically ✅
Worktree missing → Offer to create ✅
No worktree → Execute here (with branch check) ✅
All seamless, no manual cd required! ✅
Step 3: Validate Implementation Files

Before starting execution, verify all implementation files exist:

Count phases in plan.md:

Parse .codevoyant/plans/{plan-name}/plan.md
Count lines matching: ^### Phase (\d+)
Store total phase count
Note whether ### Phase 0 exists (prerequisites gate) — store as HAS_PHASE_0

Check each implementation file exists:

Phase 0 is a manual prerequisites gate — it has no implementation file. Skip it.
For phase 1 to total phases:
Check .codevoyant/plans/{plan-name}/implementation/phase-{N}.md exists
Check file size > 100 bytes (not empty)

If any files missing:

❌ Cannot start execution - implementation files missing!

Missing implementation files:
- phase-3.md
- phase-5.md

Implementation files are required for all phases before execution.
These files should have been created during /spec:new.

To fix:
1. Create the missing files in .codevoyant/plans/{plan-name}/implementation/
2. Use the template structure from /spec:new Step 5.5
3. Or recreate the plan with /spec:new

Cannot proceed with background execution.


Exit and do not continue to Step 4.

If all files exist:

Report validation success:
✓ Validated {N} implementation files (phase-1.md through phase-{N}.md)

Continue to Step 4
Step 4: Confirm Background Execution

If AUTO_APPROVE is true:

Skip confirmation
Report: → Starting background execution with --yes flag
Proceed directly to Step 5

If AUTO_APPROVE is false:

IMMEDIATELY call the AskUserQuestion tool with exactly these parameters — do NOT print the options as text:

question: "Start background execution for '{plan-name}'? ({N} phases, {M} tasks)\n\nThe agent will:\n✓ Execute all tasks autonomously\n✓ Update plan.md checkboxes in real-time\n✓ Run tests at phase boundaries\n✓ Pause on errors\n[ALLOW_COMMITS=false] ⚠️ Will NOT commit (pass --commit to enable)\n[ALLOW_COMMITS=true] ✓ Will commit as tasks complete\n\nMonitor: /status {plan-name}  |  Stop: /stop {plan-name}"
header: "Start execution?"
multiSelect: false
options:
  - label: "Start execution"
    description: "Launch autonomous agent — you can continue other work while it runs"
  - label: "Cancel"
    description: "Return to prompt without starting"


Wait for the user's response via the tool — do NOT output a numbered list, do NOT print "Please reply with your choice".

Step 5: Initialize Execution Tracking
Create or clear .codevoyant/plans/{plan-name}/execution-log.md:
# Execution Log - {plan-name}

Started: [timestamp]
Plan: [plan objective]
Status: RUNNING

## Progress

- Current Phase: [phase name]
- Completed Tasks: 0/[total]
- Errors: 0

## Timeline

[timestamp] - Execution started


Update the registry:

npx @codevoyant/agent-kit plans update-status --name "$PLAN_NAME" --status Executing


Optionally add execution status to plan.md Insights section (if it exists):

## Insights

### Background Execution

- Status: RUNNING
- Started: [timestamp]
- Check progress: /status {plan-name}
- Stop execution: /stop {plan-name}

Step 6: Launch Background Agent

Determine execution directory:

# If worktree exists and should be used (from Step 2.5)
if [ "$WORKTREE_EXISTS" = "true" ] && [ -d "$PLAN_WORKTREE" ]; then
  EXECUTION_DIR="$PLAN_WORKTREE"
  EXECUTION_MODE="worktree"
else
  EXECUTION_DIR=$(pwd)
  EXECUTION_MODE="current"
fi


Important: Before launching agent, change to execution directory:

cd "$EXECUTION_DIR"


Use the Task tool to spawn a spec-executor agent for each phase in sequence:

Agent:
  subagent_type: spec-executor
  description: "spec-executor: Phase {N} — {phase-name}"
  prompt: [agent-prompt.md content with variables substituted]


Read references/agent-prompt.md and substitute {EXECUTION_DIR}, {PLAN_BRANCH}, {PLAN_WORKTREE}, {ALLOW_COMMITS}, {SILENT}, and {plan-name} with their actual values before passing as the prompt.

Phase 0 gate — check before entering the loop:

If HAS_PHASE_0=true, read the Phase 0 task list from plan.md. If any Phase 0 tasks are unchecked ([ ]):

Stop. Do not launch any executor agents.

Present the unchecked tasks to the user:

⛔ Phase 0 — Prerequisites must be completed before execution can begin.

The following actions require your attention:

  [ ] {task 1}
  [ ] {task 2}
  ...

Complete these steps, then run /spec:bg again to continue.


Exit. Do not proceed to Phase 1.

If all Phase 0 tasks are checked ([x]), continue to the orchestration loop starting at Phase 1.

Orchestration loop — for each phase starting at Phase 1:

Launch phase Task (spec-executor) with the substituted prompt
Wait for completion: TaskOutput (block=true)
Parse the agent's summary report
Orchestrator writes a phase summary to execution-log.md (reliable fallback):
[{timestamp}] ORCHESTRATOR: Phase {N} — {phase-name} summary
  Status: {COMPLETE | FAILED | PARTIAL}
  Agent report: {first 3 lines of agent summary}

If phase failed: stop loop, send failure notification (see below), report to user
If phase succeeded: continue to Phase N+1

After the loop completes (all phases done OR a phase failed), send a desktop notification unless SILENT=true. Use the Bash tool to run:

if [ "$SILENT" != "true" ]; then
  npx @codevoyant/agent-kit notify \
    --title "Claude Code — Spec" \
    --message "{ALL_DONE: Plan '{plan-name}' complete | FAILED: Plan '{plan-name}' stopped at Phase {N}}"
fi

Step 7: Notify User

After launching all phases:

✓ Background execution started for plan "{plan-name}"!

Agent is now working through your plan autonomously.

Monitor progress:
- /status {plan-name} - Check current progress
- /status - View all plans overview
- Watch .codevoyant/plans/{plan-name}/plan.md - See checkboxes update in real-time
- View .codevoyant/plans/{plan-name}/execution-log.md - See detailed execution log

Control execution:
- /stop {plan-name} - Halt execution gracefully
- /pause {plan-name} - Same as /stop (saves state)

You will receive a desktop notification when execution completes or fails.
(Suppress with --silent)

Notes
The background agent works independently - you can continue chatting
Progress is saved continuously in .codevoyant/plans/{plan-name}/plan.md and the registry
If the agent encounters errors, it will pause and preserve state
Resume with /bg {plan-name} again or use /go {plan-name} for interactive execution
Check execution status anytime with /status {plan-name} or /status for all plans
Weekly Installs
11
Repository
cloudvoyant/codevoyant
First Seen
Mar 21, 2026
---
title: divide-and-conquer
url: https://skills.sh/driangle/taskmd/divide-and-conquer
---

# divide-and-conquer

skills/driangle/taskmd/divide-and-conquer
divide-and-conquer
Installation
$ npx skills add https://github.com/driangle/taskmd --skill divide-and-conquer
SKILL.md
Divide and Conquer

Pick up a task and execute it by splitting the work into independent workstreams that run in parallel via subagents.

Instructions

The user's query is in $ARGUMENTS (a task ID like 077 or a task name/keyword).

Look up the task: Run taskmd get $ARGUMENTS to find the task
If not found, run taskmd list to show available tasks and ask the user which one they meant
Read the task file with the Read tool to get the full description, subtasks, and acceptance criteria
Mark the task as in-progress: Run taskmd set <ID> --status in-progress
Start a worklog entry (if worklogs are enabled):
Check .taskmd.yaml for worklogs: true -- only create worklogs if explicitly enabled
If enabled, find or create the worklog file at tasks/<group>/.worklogs/<ID>.md (or tasks/.worklogs/<ID>.md for root tasks)
Append a timestamped entry noting your approach and initial findings
Plan and identify workstreams:
Use EnterPlanMode to design the overall approach
In the plan, include a reference to the original task ID and task file path
Analyze the task and break it into independent workstreams — pieces of work that can proceed in parallel without depending on each other's output
Examples of independent workstreams:
Implementation code vs. tests vs. documentation
Changes to separate packages or modules
Backend changes vs. frontend changes
If the task is simple enough that parallelization adds no benefit, just do it directly (skip to step 7)
Launch subagents in parallel:
Use the Agent tool to launch one subagent per independent workstream
Give each subagent a clear, self-contained prompt describing exactly what to do, including relevant file paths and context
Launch all independent subagents in a single message so they run concurrently
Use isolation: "worktree" for subagents that modify files, to avoid conflicts
Wait for all subagents to complete
Coordinate and integrate:
Review all subagent results for correctness
If subagents ran in worktrees, merge their changes (review diffs, resolve any conflicts)
If any subagent failed, handle the failure directly rather than re-launching
Run tests and linting to verify the integrated result
Check off subtasks (- [x]) in the task file as they are completed
Append worklog entries when you make key decisions, hit blockers, or complete significant subtasks
Write a final worklog entry summarizing what was done, which workstreams ran in parallel, decisions made, and any open items
Mark the task as done:
Check .taskmd.yaml for workflow: pr-review -- if set, use the PR-review workflow below
Solo workflow (default): Run taskmd set <ID> --status completed --verify
The --verify flag will run any verification checks defined in the task before applying the status change
If verification fails, fix the issues and try again
PR-review workflow: Open a PR, then run taskmd set <ID> --status in-review --add-pr <PR-URL> and stop
Worklog Format

Each worklog entry uses a timestamp heading followed by free-form notes:

## 2026-02-15T10:30:00Z

Started divide-and-conquer execution of the search feature task.

**Workstreams identified:**

1. Core search implementation (subagent — worktree)
2. Test suite (subagent — worktree)
3. Documentation updates (subagent)

**Completed:**

- [x] All subagents finished successfully
- [x] Merged worktree changes
- [x] Tests passing after integration

**Decisions:** Used full-text search with SQLite rather than Elasticsearch.

Weekly Installs
19
Repository
driangle/taskmd
GitHub Stars
24
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
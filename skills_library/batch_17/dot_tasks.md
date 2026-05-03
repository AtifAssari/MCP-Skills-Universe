---
title: dot-tasks
url: https://skills.sh/awni00/dot-tasks/dot-tasks
---

# dot-tasks

skills/awni00/dot-tasks/dot-tasks
dot-tasks
Installation
$ npx skills add https://github.com/awni00/dot-tasks --skill dot-tasks
SKILL.md
dot-tasks Skill

dot-tasks is a Python CLI (assumed installed) that tracks human/agent work in a repo-local .tasks/ directory.

Use this skill whenever a repository uses dot-tasks for task lifecycle tracking.

When To Use
Use this skill when the user asks for task suggestions based on existing dot-tasks state.
Use this skill when the user asks to begin or resume work on an existing task.
Use this skill when the user asks for significant new work that should likely be tracked.
Plan Mode Deliverables

By default, when asked to work on a task, produce both artifacts in order:

Develop/refine the task specification and write it to spec.md.
Develop the implementation plan and write it to plan.md.
plan.md must be based on a current, user-confirmed spec.md.
Exceptions:
If explicitly asked for spec-only work, produce/update only spec.md.
If resuming from a completed spec.md, validate it is still current, then produce/update plan.md.
Artifact scope:
spec.md: A precise, testable statement of what must be built, including scope, requirements, interfaces, and acceptance criteria.
plan.md: An ordered execution strategy for how to build it, including steps, dependencies, checkpoints, and risk mitigations.
Workflow 1: Suggest What To Work On Next
Discover candidate work:
Run dot-tasks list todo --json (or dot-tasks list --json if status is not specified).
Inspect likely top candidates with dot-tasks view <task_name_or_id> --json.
Rank candidates using this rubric:
Higher priority first (p1 before p2, etc).
Prefer unblocked tasks (dependency_health: ready) over blocked work.
Note spec readiness and effort when suggesting tasks to user.
Return the top few options with one-line rationale each.
If high-priority work is blocked, call that out explicitly and include:
A short unblock path for the blocked item.
A suggested unblocked fallback task.
Workflow 2: Begin Or Resume Existing Task
Resolve the target task:
If the user provides task_name/task_id, run dot-tasks view <task_name_or_id> --json.
If ambiguous, list likely matches and confirm the target with the user before binding.
Branch by task status:
doing: resume by reading spec.md, plan.md, and recent activity.md, then continue from the latest checkpoint.
todo: run readiness checks before starting.
done: do not silently restart; ask whether to create a follow-up task or reopen scope explicitly.
Ensure spec is ready before planning implementation
If intent is unclear, ask directed open-ended questions in two stages to clarify intent and develop clear spec. Do not proceed on unstated assumptions when high-level intent is unclear.
Workflow 3: Significant New Work
Detect whether the request is substantial (multi-file, plan-heavy, or likely >=30 minutes).
If substantial, ask whether to create and bind a new dot-tasks task.
If the user agrees:
Create task with dot-tasks create ... (include summary and basic metadata).
Confirm the tracking target and bind work to that task.
If work is quick/simple, do not force task creation unless the user asks.
Shared Task Lifecycle Loop

For tracked task execution (regardless of how it was triggered), follow: create -> spec -> confirm -> start -> plan -> log-activity -> complete

Follow Plan Mode Deliverables.
Start active execution with dot-tasks start: sets status to doing and creates empty plan.md.
If Plan Mode/intent work produced a finalized spec artifact, sync that Markdown to spec.md on the first execution turn after Plan Mode.
If Plan Mode produced a finalized <proposed_plan>, sync that Markdown to plan.md on the first execution turn after Plan Mode, after spec confirmation.
Keep plan.md current as implementation decisions become concrete.
Log meaningful progress with dot-tasks log-activity --note.
Log meaningful progress with dot-tasks log-activity --note.
For major tasks, document decisions made during implementation in a decisions.md artifact; include key decision rationale and alternative choices considered. Add "# NOTE: " comments in code for significant decisions. For major decisions, pause and ask user for direction before proceeding. Report back to user at end of execution with a summary of decisions made.
Use dot-tasks update for mid-flight metadata/scope/priority changes.
Before dot-tasks complete, confirm acceptance criteria are satisfied.
Commands
# setup
dot-tasks init                                              # initialize .tasks/

# discover
dot-tasks list --json                                       # list tasks for matching
dot-tasks list [todo|doing|done] --json                    # narrow by status
dot-tasks view <task_name_or_id> --json                    # inspect one task
dot-tasks tags [todo|doing|done] --json                    # tag counts/triage

# lifecycle
dot-tasks create <task_name> --summary "..." --priority [p1|p2|p3|p4] --effort [s|m|l|xl] --tag <tag>
dot-tasks start <task_name_or_id>                          # move to doing + create plan.md
dot-tasks update <task_name_or_id> --priority p1 --effort m --tag backend
dot-tasks log-activity <task_name_or_id> --note "Progress note" [--actor agent]
dot-tasks complete <task_name_or_id>                       # move to done

# maintenance
dot-tasks rename <task_name_or_id> <new_task_name>         # rename task
dot-tasks delete <task_name_or_id>                         # soft-delete to trash

Guardrails
Prefer dot-tasks commands over direct edits to task state files.
Avoid silent auto-binding on fuzzy matches.
Confirm task binding with the user before tracked execution.
Apply ordering/default/exception behavior from Plan Mode Deliverables.
Direct file edits are allowed for:
task.md for writing task summary/specs after dot-tasks create.
spec.md: A precise, testable statement of what must be built, including scope, requirements, interfaces, and acceptance criteria.
plan.md: An ordered execution strategy for how to build it, including steps, dependencies, checkpoints, and risk mitigations.
Other task-local artifacts (for example walkthrough.md, decisions.md, handoff.md) only when useful for scope and naturally produced during the session; confirm with the user before non-trivial additions, and do not manufacture extra artifacts for small/self-contained tasks.
Do not rewrite activity.md history; append only.
Respect dependency checks.
Data Contract
Canonical metadata is in task.md frontmatter.
Dependency references use task_id in metadata.
Dependencies are displayed to humans as task_name (task_id).
activity.md line format is YYYY-MM-DD HH:MM | actor | type | note.
Weekly Installs
24
Repository
awni00/dot-tasks
GitHub Stars
1
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
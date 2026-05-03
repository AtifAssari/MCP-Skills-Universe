---
rating: ⭐⭐
title: werk
url: https://skills.sh/zackbart/werk/werk
---

# werk

skills/zackbart/werk/werk
werk
Installation
$ npx skills add https://github.com/zackbart/werk --skill werk
SKILL.md
werk

Use the werk CLI for all task, decision, and session tracking. DB lives at .werk/tasks.db. Always pass --agent on all write commands.

Items use hash IDs as their primary identifier: ep-a1b2c3 (epic), tk-a1b2c3 (task), st-a1b2c3 (subtask). Always use the id field from JSON output to reference items in subsequent commands. The ref field (e.g. 1.2) is a display-only label for the web UI — do not use it as a CLI argument.

See CLI Reference for full command list and output format. See Guide for issue classification, setup, dependencies, archiving, and other reference material.

Invariants — never break these
Always start and end sessions — this is how context transfers between agents
Always record decisions when making non-obvious technical choices — this prevents re-litigation
Never work on a task with open blockers
Prefer closing over deleting — delete only duplicates and mistakes
Close/delete children before parents (subtasks -> task -> epic)
Always pass --agent on all write commands
File discovered work immediately — don't leave it untracked
Session lifecycle

Sessions are how work context survives between agents and across time. Without them, the next agent starts blind.

Start every session:

werk session start --with-context --agent


The --with-context flag returns the session object bundled with recent log, ready tasks, and in-progress tasks — everything needed to orient in one call.

Alternatively, without --with-context:

werk session start --agent
werk log --pretty --agent              # catch up on recent activity
werk task ready --agent
werk task list --status in_progress --agent


Use werk log --verbose --pretty -n 10 if you need more context (notes, rationale, session details).

End every session:

werk session end --summary "<plain-English description of what was accomplished>" --agent


The summary should orient the next agent quickly in one or two sentences. Cover: what was done, what was filed or discovered, and what's left or blocked. Skip implementation details — focus on outcomes.

Good: "Implemented hash ID generation and wired audit trail to all write commands. Filed 2 tasks for edge cases found during testing." Bad: "Updated id.go to use sha256 truncation with 6-char prefix, added audit INSERT calls to CreateTask, UpdateTask, and DeleteTask functions, also noticed..."

If --summary is omitted, an auto-summary is generated from audit entries during the session.

Core workflow
werk next --agent — pick the highest-priority ready task and start it; response includes subtasks array
Or manually: werk task ready --agent then werk task start <id> --agent
Do the work. File subtasks for steps discovered along the way.
werk task note <id> "<text>" --agent — append progress notes as you go
Decision checkpoint: Did you choose between alternatives or make a non-obvious tradeoff? File a decision now — not later. Keep it tight: the summary is the choice ("Use X over Y"), the rationale is the why in 1-2 sentences. Skip decisions for obvious or forced choices.
werk subtask close <id> --agent — close each subtask as you finish it
werk task close <id> --agent — close the task (all subtasks must be done first)
werk task ready --agent — check for newly unblocked work and repeat
Bulk operations

Start, close, and reopen accept multiple IDs:

werk task close tk-a1b2c3 tk-d4e5f6 tk-g7h8i9 --agent
werk subtask start st-a1b2c3 st-d4e5f6 --agent

Filing new work

Read the Issue Classification Guide for detailed guidance on titles, notes, and when to file each type. Summary:

Epic — a shippable feature or goal spanning multiple sessions (3-10 tasks). Noun phrase title, notes explain why and acceptance criteria.
Task — a concrete unit of work within an epic. Imperative verb title ("Implement X", "Fix Y when Z"). Notes give operational context.
Subtask — a discrete step within a task. Specific title saying exactly what will be done.
Decision — a permanent record of a non-obvious choice. Summary states the choice, rationale explains why.
werk epic create "Feature Name" --high --notes "Why and acceptance criteria" --agent
werk task create "Implement X" --epic ep-a1b2c3 --notes "Approach hints" --agent
werk subtask create "Write migration SQL" --task tk-a1b2c3 --agent
werk decision create "Use X over Y" --rationale "Why, tradeoffs" --agent

Quick reference
werk session start --with-context --agent  Begin a session (do this first)
werk session end --summary "..." --agent   End a session (do this last — summarize what happened)
werk next --agent                       Pick highest-priority ready task and start it
werk log --pretty                       What happened recently?
werk log --pretty --task tk-a1b2c3      Activity for a specific task
werk log --pretty --verbose -n 10       Detailed recent activity
werk task ready                         What can I work on right now?
werk task list --status in_progress     What is currently in flight?
werk task find "login"                  Search tasks by title/notes
werk task note tk-a1b2c3 "progress" --agent   Append notes to a task
werk epic list                          What features exist?
werk dep list <id>                      What blocks this / what does this block?
werk audit <id>                         Full history of a single task
werk handoff <id>             Context packet for agent handoff
werk status                             Project summary (with active session)
werk decision create "X over Y" --rationale "..." --agent   Record a non-obvious choice
werk decision list                      Architectural decision log
werk diff                               Changes since last session
werk export > backup.json               Full data export

Weekly Installs
14
Repository
zackbart/werk
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
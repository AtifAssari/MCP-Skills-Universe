---
title: spec-driven-simple-task
url: https://skills.sh/kw12121212/auto-spec-driven/spec-driven-simple-task
---

# spec-driven-simple-task

skills/kw12121212/auto-spec-driven/spec-driven-simple-task
spec-driven-simple-task
Installation
$ npx skills add https://github.com/kw12121212/auto-spec-driven --skill spec-driven-simple-task
SKILL.md

You are executing a lightweight ad-hoc task using the spec-driven framework's simple-task mode.

Prerequisites

The .spec-driven/ directory must exist at the project root. Before proceeding, verify:

ls .spec-driven/


If this fails, the project is not initialized. Run /spec-driven-init first.

Steps

Entry gate — evaluate the user's task description against three criteria before executing:

Scope check: If the task clearly spans multiple modules, involves schema changes, or affects cross-cutting concerns → reject, recommend /spec-driven-propose or /spec-driven-brainstorm
Hotfix check: If the task is framed as urgent, hotfix, or critical production fix → reject, recommend the formal change workflow (/spec-driven-propose)
If the task fails any check, explain why and suggest the appropriate alternative skill. Do not proceed.

Load spec context — read .spec-driven/config.yaml, .spec-driven/specs/INDEX.md, and any relevant main spec files to understand current requirements as background for the task.

Execute the task — perform the work directly (edit files, run commands, etc.). Do not create or modify anything under .spec-driven/changes/.

Assess spec impact — after completing the task, evaluate whether the work affected any specs:

No spec impact — the task is complete, log it
Spec drift detected — suggest /spec-driven-sync-specs or /spec-driven-spec-edit
Mapping drift detected — suggest /spec-driven-resync-code-mapping
New change need discovered — suggest /spec-driven-propose or /spec-driven-brainstorm
You MUST NOT automatically invoke other skills. Suggestions are advisory only.

Log the task — create a markdown log at .spec-driven/simple-tasks/YYYY-MM-DD-<name>.md:

Ensure the directory exists: mkdir -p .spec-driven/simple-tasks/
<name> is a short kebab-case identifier derived from the task description
The log MUST contain: Task (description), What was done (summary), Spec impact (none / drift / new change), Follow-up (suggestions or "None")
The simple-tasks/ directory is a flat log — no subdirectories, no lifecycle management.
Rules
This skill never creates, modifies, or archives anything under .spec-driven/changes/
Spec context is read-only during task execution — spec updates happen through existing skills
The log file is the only artifact created by this skill
If the task grows beyond simple scope mid-execution, stop and suggest switching to /spec-driven-propose
Weekly Installs
19
Repository
kw12121212/auto…c-driven
First Seen
Apr 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
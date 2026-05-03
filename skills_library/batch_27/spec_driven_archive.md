---
title: spec-driven-archive
url: https://skills.sh/kw12121212/auto-spec-driven/spec-driven-archive
---

# spec-driven-archive

skills/kw12121212/auto-spec-driven/spec-driven-archive
spec-driven-archive
Installation
$ npx skills add https://github.com/kw12121212/auto-spec-driven --skill spec-driven-archive
SKILL.md

You are helping the user archive a completed spec-driven change.

This Skill's Commands

If you cannot remember the exact command used by this skill, look it up here before running anything. Do not guess.

modify: node {{SKILL_DIR}}/scripts/spec-driven.js modify
apply: node {{SKILL_DIR}}/scripts/spec-driven.js apply <name>
verify-spec-mappings: node {{SKILL_DIR}}/scripts/spec-driven.js verify-spec-mappings
archive: node {{SKILL_DIR}}/scripts/spec-driven.js archive <name>

Responsibility Split

Explicitly distinguish script work from AI work when you run this skill.

Handled by CLI scripts

node {{SKILL_DIR}}/scripts/spec-driven.js modify lists active changes
node {{SKILL_DIR}}/scripts/spec-driven.js apply <name> reports task completion status
node {{SKILL_DIR}}/scripts/spec-driven.js archive <name> moves the change directory into .spec-driven/changes/archive/YYYY-MM-DD-<name>/ and, when .spec-driven/roadmap/ exists, reconciles any affected milestone declared status plus .spec-driven/roadmap/INDEX.md

Handled by the AI

Ask the user which change to archive when needed
Interpret the apply output and block archive when tasks remain incomplete
Inspect .spec-driven/changes/<name>/specs/, merge delta specs into .spec-driven/specs/, and remove emptied main spec files when required by REMOVED
Ask for explicit confirmation if the change has no delta specs
Update .spec-driven/specs/INDEX.md to reflect created or deleted main spec files
Preserve or apply spec mapping frontmatter during spec merges
Summarize the merged spec impact, any roadmap status changes caused by archive, and the final archive location
Prerequisites

The .spec-driven/ directory must exist at the project root. Before proceeding, verify:

ls .spec-driven/


If this fails, the project is not initialized. Run /spec-driven-init first.

Steps

Select the change — run node {{SKILL_DIR}}/scripts/spec-driven.js modify to list active changes. Ask which change to archive. If already specified, use it.

Check for incomplete tasks — run:

node {{SKILL_DIR}}/scripts/spec-driven.js apply <name>


If remaining > 0, stop — archiving is not allowed until all tasks are complete. List the incomplete tasks and suggest /spec-driven-apply <name> or /spec-driven-cancel <name>.

Merge delta specs — list all files in .spec-driven/changes/<name>/specs/:

If specs/ is empty: ask the user to confirm this change has no observable spec impact before continuing.
For each delta file (e.g. specs/install/install-behavior.md), merge into the corresponding main spec file (e.g. .spec-driven/specs/install/install-behavior.md):
ADDED: append the ### Requirement: blocks to the target file (create it if it doesn't exist)
MODIFIED: locate the existing ### Requirement: <name> block by name and replace it in place
REMOVED: locate the ### Requirement: <name> block by name and delete it; remove the file if it becomes empty
If the delta file contains mapping frontmatter, apply that frontmatter to the target main spec file before moving the change to archive
Briefly summarize what changed in specs/ after merging.

Update specs/INDEX.md — after merging, update .spec-driven/specs/INDEX.md:

Add entries for any newly created spec files (with a one-line description)
Remove entries for any deleted spec files
Leave existing entries unchanged unless the file's scope changed
Run node {{SKILL_DIR}}/scripts/spec-driven.js verify-spec-mappings and fix mapping frontmatter errors before archive closeout

Archive the change — run:

node {{SKILL_DIR}}/scripts/spec-driven.js archive <name>


This moves the entire change directory (including questions.md) to the archive. If .spec-driven/roadmap/ exists, the command also reconciles milestone declared status and regenerates .spec-driven/roadmap/INDEX.md for any milestone affected by the archived change.

Confirm — report the result:

Where the change was moved to (e.g. .spec-driven/changes/archive/2024-01-15-<name>/)
Any milestone declared status or roadmap index entry that changed because of archive
Suggest running /spec-driven-propose if there's follow-up work
Rules
Always check for incomplete tasks before archiving
Never archive a change with incomplete tasks
Always state which steps are script-executed and which are AI-executed
Always merge delta specs before archiving — this is a hard gate, not optional
If changes/<name>/specs/ is empty, require explicit human confirmation that the change has no observable spec impact
Deleting requirements or empty spec files in .spec-driven/specs/ is allowed when applying REMOVED delta entries
Do not delete the change directory manually — archive the change by running the archive command
Keep implementation and test mappings in frontmatter, not in requirement prose
Weekly Installs
35
Repository
kw12121212/auto…c-driven
First Seen
Mar 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
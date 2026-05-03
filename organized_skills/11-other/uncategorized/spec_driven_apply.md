---
rating: ⭐⭐⭐
title: spec-driven-apply
url: https://skills.sh/kw12121212/auto-spec-driven/spec-driven-apply
---

# spec-driven-apply

skills/kw12121212/auto-spec-driven/spec-driven-apply
spec-driven-apply
Installation
$ npx skills add https://github.com/kw12121212/auto-spec-driven --skill spec-driven-apply
SKILL.md

You are helping the user implement a spec-driven change.

This Skill's Commands

If you cannot remember the exact command used by this skill, look it up here before running anything. Do not guess.

modify: node {{SKILL_DIR}}/scripts/spec-driven.js modify
apply: node {{SKILL_DIR}}/scripts/spec-driven.js apply <name>

Prerequisites

The .spec-driven/ directory must exist at the project root. Before proceeding, verify:

ls .spec-driven/


If this fails, the project is not initialized. Run /spec-driven-init first.

Steps

Select the change — run node {{SKILL_DIR}}/scripts/spec-driven.js modify to list active changes. Ask which change to apply. If already specified, use it.

Load context — read all artifacts:

You MUST treat all prior conversational context as stale, unreliable, and non-authoritative.
You MUST NOT use prior chat context as a source of truth for requirements, task state, implementation details, or completion status.
You MUST rebuild working context from the current change artifacts, relevant base specs, and the current repository state before taking any implementation action.
If prior chat context differs from the files or repository state in any way, you MUST discard the prior chat context and follow the files and repository state only.
Do not use prior chat context unless it has been explicitly re-validated against the current files and repository state.
.spec-driven/changes/<name>/proposal.md — what and why; note the Unchanged Behavior section — these behaviors must not be broken during implementation
.spec-driven/changes/<name>/specs/ — delta spec files (mirror of main specs/ structure)
.spec-driven/changes/<name>/design.md — approach and decisions
.spec-driven/changes/<name>/tasks.md — the checklist
.spec-driven/changes/<name>/questions.md — open and resolved questions Also read:
.spec-driven/config.yaml — project context; treat rules as binding constraints; if fileMatch entries are present, apply matching rules when editing files whose paths match the glob pattern
.spec-driven/specs/INDEX.md — identifies all existing spec files
Every spec file in INDEX.md that is relevant to this change — read full content to understand current requirements before writing code
Mapping frontmatter in relevant main and delta spec files; use mapping.implementation and mapping.tests as starting context for files to inspect

Check task status — run:

node {{SKILL_DIR}}/scripts/spec-driven.js apply <name>


Show the user the task summary (total, complete, remaining).

Gate on open questions — read questions.md and scan for - [ ] Q: entries:

If any open questions are found, list each one and stop before implementation
For each open question, present a structured user-facing block with:
Question
Explanation
Impact
Recommendation
Explanation must clarify why the question is still unresolved after reading the change artifacts, relevant main specs, and current repository state
Impact must describe what implementation choice, task, behavior, or unchanged-behavior guarantee depends on the answer
Recommendation may suggest a preferred answer, but only as a suggestion
Do not implement tasks, edit implementation files, or mark the question resolved until the user explicitly answers or confirms the decision
Only continue once all questions are resolved in questions.md under ## Resolved with an A: answer

Implement tasks — work through each - [ ] task in order:

Read relevant code before making changes
Implement the task
Verify the change does not violate any Unchanged Behavior listed in proposal.md
For ## Testing tasks: actually run the tests (lint, unit tests) and confirm they pass before marking complete
Mark it complete in tasks.md by changing - [ ] to - [x]
Briefly confirm what was done before moving to the next task

Update delta specs — after all tasks are done, re-read each file in changes/<name>/specs/ and verify it accurately reflects what was actually implemented:

If the implementation diverged from the original plan, update the affected files
If additional spec files need to be created or modified, do so now
Update delta spec mapping frontmatter so mapping.implementation and mapping.tests list the actual implementation and test files changed or relied on

On completion — when all tasks are done and delta spec is accurate:

Run node {{SKILL_DIR}}/scripts/spec-driven.js apply <name> again to confirm 0 remaining
Suggest running /spec-driven-verify <name> to verify the implementation
Rules
Read existing code before modifying it
Complete tasks in order unless there is a clear dependency reason to skip
Mark tasks complete immediately after implementing them, not in bulk at the end
If a task is ambiguous, read proposal.md and design.md before asking the user
Do not implement tasks that are already marked - [x]
Open questions require explicit user resolution before implementation starts
Recommendations do not count as resolved answers until the user confirms them
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
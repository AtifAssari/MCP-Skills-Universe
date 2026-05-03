---
rating: ⭐⭐⭐
title: roadmap-plan
url: https://skills.sh/kw12121212/auto-spec-driven/roadmap-plan
---

# roadmap-plan

skills/kw12121212/auto-spec-driven/roadmap-plan
roadmap-plan
Installation
$ npx skills add https://github.com/kw12121212/auto-spec-driven --skill roadmap-plan
SKILL.md

You are helping the user create or restructure the repository roadmap.

This Skill's Commands

If you cannot remember the exact command used by this skill, look it up here before running anything. Do not guess.

init: node {{SKILL_DIR}}/scripts/spec-driven.js init
verify-roadmap: node {{SKILL_DIR}}/scripts/spec-driven.js verify-roadmap

Prerequisites

The .spec-driven/ directory must exist at the project root. Before proceeding, verify:

ls .spec-driven/


If this fails, the project is not initialized. Run /spec-driven-init first.

If .spec-driven/roadmap/ is missing, repair the scaffold first:

node {{SKILL_DIR}}/scripts/spec-driven.js init

Steps

Read roadmap context first — before proposing milestone structure, read:

.spec-driven/config.yaml
.spec-driven/roadmap/INDEX.md if it exists
every existing file under .spec-driven/roadmap/milestones/
.spec-driven/specs/INDEX.md and any main spec files that are clearly relevant to the user's planning scope
active and archived changes under .spec-driven/changes/ as evidence of what is already in progress or complete

You MAY delegate bounded analysis-only work such as roadmap summarization, candidate milestone comparisons, or likely spec-path discovery to a sub-agent. The parent agent MUST keep user confirmation, roadmap shape selection, and final .spec-driven/roadmap/ writes.

Understand the planning goal — determine:

whether the user wants to create a brand-new roadmap or restructure an existing one
what major phases or stage goals the roadmap should express
whether there are existing changes that already belong to specific milestones
whether any existing milestone files are still using a legacy structure, such as an extra ## Candidate Ideas section, a combined ## Dependencies / Risks section, or missing ## In Scope, ## Out of Scope, or ## Notes sections

Converge on milestone boundaries before writing — help the user settle:

milestone names and ordering
each milestone's goal and done criteria
which concrete Planned Changes belong in each milestone
key dependencies, risks, and sequencing
any non-obvious legacy-migration interpretation needed to rewrite older milestone files into the canonical format

Confirm the roadmap shape — before editing files, summarize the intended milestone structure and ask for explicit confirmation. If legacy milestone migration is in scope, include any non-obvious content reinterpretation you plan to make while converting older milestone files.

Write roadmap assets — update:

.spec-driven/roadmap/INDEX.md
.spec-driven/roadmap/milestones/<milestone>.md for each milestone in scope When a milestone is in a legacy format, rewrite it into the canonical section set while preserving clearly recoverable meaning. Use the legacy milestone wording itself as migration evidence.

Preserve roadmap rules — in every milestone file:

use these standard section headings:
## Goal
## In Scope
## Out of Scope
## Done Criteria
## Planned Changes
## Dependencies
## Risks
## Status
## Notes
milestone declared statuses are limited to:
proposed
active
blocked
complete
write each Planned Changes item with a canonical first line, - \` - Declared: - `
planned change declared statuses are limited to:
planned
complete
keep each planned change description on that same line; do not add indented continuation lines below the bullet
default new or unfinished planned changes to Declared: planned
put extra milestone-local context in another section such as ## Notes instead of attaching multiline detail under ## Planned Changes
treat Planned Changes as the milestone's only work list and keep it limited to concrete approved change work
keep each milestone at 10 or fewer planned changes; split larger scopes into multiple milestones
derive milestone completion from archived planned changes rather than manual toggles
when migrating a legacy milestone, map content conservatively:
move clearly approved executable work into ## Planned Changes
split a combined ## Dependencies / Risks section only when the source distinction is clear enough to preserve confidently
infer ## In Scope or ## Out of Scope only when the old milestone wording makes those boundaries clear
preserve useful leftover context in ## Notes instead of dropping it
surface ambiguity to the user instead of silently inventing an exact migration

Validate roadmap size before finish — run:

node {{SKILL_DIR}}/scripts/spec-driven.js verify-roadmap

If validation reports a milestone is too large, stop and tell the user to split it into smaller milestones
Do not present the roadmap as ready while size validation fails

Summarize the result — report the milestone structure created or changed, what planned work was assigned to each milestone, and any remaining planning gaps.

Rules
This is a planning/documentation skill only — do not change product code
Read roadmap files and relevant change history before restructuring anything
Do not collapse multiple milestones into one oversized roadmap document
Do not mark a milestone complete manually if its planned changes are not all archived
Do not let a sub-agent own the confirmation step or final roadmap file edits
Weekly Installs
31
Repository
kw12121212/auto…c-driven
First Seen
11 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
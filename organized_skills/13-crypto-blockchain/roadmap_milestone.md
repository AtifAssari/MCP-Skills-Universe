---
rating: ⭐⭐⭐
title: roadmap-milestone
url: https://skills.sh/kw12121212/auto-spec-driven/roadmap-milestone
---

# roadmap-milestone

skills/kw12121212/auto-spec-driven/roadmap-milestone
roadmap-milestone
Installation
$ npx skills add https://github.com/kw12121212/auto-spec-driven --skill roadmap-milestone
SKILL.md

You are helping the user refine a single roadmap milestone.

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

Choose the milestone — determine whether the user wants to edit an existing milestone or create a new one under .spec-driven/roadmap/milestones/.

Load milestone context — read:

.spec-driven/config.yaml
.spec-driven/roadmap/INDEX.md
the target milestone file when it already exists
any nearby milestone files needed to preserve ordering or avoid overlap
active and archived changes that the milestone already references or might need to reference
whether the target milestone uses a legacy structure, such as an extra ## Candidate Ideas section, a combined ## Dependencies / Risks section, or missing ## In Scope, ## Out of Scope, or ## Notes sections

You MAY delegate bounded analysis-only work such as milestone context summarization, nearby-milestone comparisons, or likely overlap checks to a sub-agent. The parent agent MUST keep milestone-shape decisions and final .spec-driven/roadmap/ edits.

Refine only one milestone at a time — help the user settle:

the milestone Goal
In Scope
Out of Scope
Done Criteria
Planned Changes
Dependencies
Risks
derived Status
Notes Use these standard section headings in the file:
## Goal
## In Scope
## Out of Scope
## Done Criteria
## Planned Changes
## Dependencies
## Risks
## Status
## Notes Milestone declared statuses are limited to:
proposed
active
blocked
complete Write each Planned Changes item with a canonical first line, - \` - Declared: - `. Planned change declared statuses are limited to:
planned
complete Default new or unfinished planned changes to Declared: planned. Keep the milestone at 10 or fewer planned changes; split larger scopes into multiple milestones. Keep the full planned change description on that same line and do not add indented continuation lines below it. If the milestone needs richer local detail, move that context into another section such as ## Notes rather than attaching multiline detail under ## Planned Changes. If the milestone starts in a legacy format and the user wants a one-file migration instead of a whole-roadmap restructure, preserve clearly recoverable content, carry forward useful leftover context into ## Notes when needed, and surface ambiguity instead of guessing silently.

Write the milestone file — create or update the milestone markdown file and keep it focused on that milestone only. If the file started in a legacy format, rewrite it into the canonical section set while preserving intent conservatively.

Update roadmap index if needed — if the milestone is new, add it to .spec-driven/roadmap/INDEX.md in the correct sequence.

Enforce milestone status rules — if listed planned changes are not all archived, the milestone is not complete. Do not add manual completion overrides.

Validate roadmap size before finish — run:

node {{SKILL_DIR}}/scripts/spec-driven.js verify-roadmap


If validation reports that the milestone is too large, stop and tell the user to split it instead of presenting the milestone as ready.

Report the result — summarize what changed in the milestone and identify any follow-up planning gaps that still need decisions before new planned changes are added.

Rules
This is a planning/documentation skill only — do not change product code
Keep Planned Changes limited to concrete approved roadmap work
Keep milestone scope bounded; do not turn this into a whole-roadmap rewrite
Milestone completion is derived from archive state, not user preference
Do not let a sub-agent own the final milestone recommendation or file write
Weekly Installs
32
Repository
kw12121212/auto…c-driven
First Seen
5 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
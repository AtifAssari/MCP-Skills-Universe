---
rating: ⭐⭐
title: roadmap-sync
url: https://skills.sh/kw12121212/auto-spec-driven/roadmap-sync
---

# roadmap-sync

skills/kw12121212/auto-spec-driven/roadmap-sync
roadmap-sync
Installation
$ npx skills add https://github.com/kw12121212/auto-spec-driven --skill roadmap-sync
SKILL.md

You are helping the user synchronize .spec-driven/roadmap/ with the current change history.

This Skill's Commands

If you cannot remember the exact command used by this skill, look it up here before running anything. Do not guess.

init: node {{SKILL_DIR}}/scripts/spec-driven.js init
roadmap-status: node {{SKILL_DIR}}/scripts/spec-driven.js roadmap-status
verify-roadmap: node {{SKILL_DIR}}/scripts/spec-driven.js verify-roadmap

Prerequisites

The .spec-driven/ directory must exist at the project root. Before proceeding, verify:

ls .spec-driven/


If this fails, the project is not initialized. Run /spec-driven-init first.

If .spec-driven/roadmap/ is missing, repair the scaffold first:

node {{SKILL_DIR}}/scripts/spec-driven.js init

Steps

Read roadmap state first — before changing anything, read:

.spec-driven/config.yaml
.spec-driven/roadmap/INDEX.md
every milestone file listed in the roadmap index
run node {{SKILL_DIR}}/scripts/spec-driven.js roadmap-status
inspect the returned milestone and planned change state summary

Compare roadmap to repository reality — use the roadmap-status output as the source of deterministic comparison. For each milestone in scope, identify:

planned changes that are archived
planned changes that still exist as active work
planned changes that are missing or renamed
milestone statuses that no longer match the derived status
any ambiguity the script cannot resolve, such as likely renames or roadmap prose that still needs human judgment

Update roadmap files — reconcile milestone status and each listed planned change's declared status based on the repository evidence you found.

Use only these legal declared status values while interpreting or rewriting roadmap files:

milestone status: proposed, active, blocked, complete
planned change status: planned, complete

Preserve roadmap rules — during sync:

do not mark a milestone complete unless every listed planned change is archived
keep the roadmap as planning state, not an implementation log

Validate roadmap size before finish — run:

node {{SKILL_DIR}}/scripts/spec-driven.js verify-roadmap


If validation reports that any milestone is too large, stop and tell the user to split it instead of presenting roadmap sync as complete.

Report the sync result — summarize:

milestones updated
planned changes whose state changed
missing or ambiguous references that still need human cleanup
Rules
This is a planning/documentation skill only — do not change product code
Use roadmap-status plus roadmap files as the source of truth for deterministic status comparison
Do not preserve stale manual labels that conflict with actual archive state
Surface ambiguity explicitly when a roadmap entry no longer matches any change
Weekly Installs
30
Repository
kw12121212/auto…c-driven
First Seen
Apr 2, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass
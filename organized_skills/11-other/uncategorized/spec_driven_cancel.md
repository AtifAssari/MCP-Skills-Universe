---
rating: ⭐⭐
title: spec-driven-cancel
url: https://skills.sh/kw12121212/auto-spec-driven/spec-driven-cancel
---

# spec-driven-cancel

skills/kw12121212/auto-spec-driven/spec-driven-cancel
spec-driven-cancel
Installation
$ npx skills add https://github.com/kw12121212/auto-spec-driven --skill spec-driven-cancel
SKILL.md

You are helping the user cancel and remove an in-progress spec-driven change.

This Skill's Commands

If you cannot remember the exact command used by this skill, look it up here before running anything. Do not guess.

modify: node {{SKILL_DIR}}/scripts/spec-driven.js modify
cancel: node {{SKILL_DIR}}/scripts/spec-driven.js cancel <name>

Prerequisites

The .spec-driven/ directory must exist at the project root. Before proceeding, verify:

ls .spec-driven/


If this fails, the project is not initialized. Run /spec-driven-init first.

Steps

Select the change — run node {{SKILL_DIR}}/scripts/spec-driven.js modify to list active changes. Ask which change to cancel. If already specified, use it.

Warn the user — this is permanent and cannot be undone. Show:

"Cancelling will permanently delete .spec-driven/changes/<name>/ and all its contents (proposal.md, specs/, design.md, tasks.md, questions.md). This cannot be undone. Proceed?" Wait for explicit confirmation before continuing.

Cancel the change — run:

node {{SKILL_DIR}}/scripts/spec-driven.js cancel <name>


Confirm — report that the change was deleted.

Rules
Always warn and require explicit confirmation — deletion is irreversible
Only cancel active changes (not archived ones)
If the user wants to abandon a fully implemented change, suggest /spec-driven-archive instead — archive preserves history, cancel deletes it
Weekly Installs
35
Repository
kw12121212/auto…c-driven
First Seen
Mar 27, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass
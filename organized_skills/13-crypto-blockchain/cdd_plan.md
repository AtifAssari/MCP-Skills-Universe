---
rating: ⭐⭐
title: cdd-plan
url: https://skills.sh/ruphware/cdd-skills/cdd-plan
---

# cdd-plan

skills/ruphware/cdd-skills/cdd-plan
cdd-plan
Installation
$ npx skills add https://github.com/ruphware/cdd-skills --skill cdd-plan
SKILL.md
CDD Plan (explicit-only)

Treat the target repo’s CDD contract files as the source of truth:

AGENTS.md
README.md
TODO.md (and/or TODO-*.md)
docs/specs/prd.md
docs/specs/blueprint.md
docs/INDEX.md (if present)
Runnable TODO step contract

For any new or rewritten execution step, produce an implementation-ready step rather than a placeholder summary.

Preserve the repo's existing Step template when possible, but add missing sections when the current template would leave the step underspecified.
Preferred section set for non-trivial work:
Goal
Constraints
Tasks
Implementation notes
Automated checks
UAT
A runnable step is decision-complete: the implementer can execute it without reopening PRD/Blueprint to discover missing product, architecture, sequencing, or validation decisions.
Each Tasks bullet must name:
the target boundary or subsystem
the exact change to make
the output artifact, contract, or behavior that must result
any must-preserve invariant or evidence requirement when relevant
Use Implementation notes for file/symbol hints, interface or schema changes, ordering constraints, migration notes, snapshot/audit requirements, and other coding-critical detail that would otherwise be lost in a short task list.
Do not leave essential implementation detail only in the surrounding chat. Put it in the TODO step.
Split work into separate steps when it crosses distinct hard gates, migration boundaries, rollback surfaces, or independently testable subsystems.
Interactive planning contract

Planning in this skill is interactive, review-driven, and continuously refined.

Start in planning mode when the runtime supports a native read-only or plan mode. If it does not, emulate that behavior by staying read-only until the user approves applying the plan.
Review the codebase before and during planning. Audit the relevant code, tests, entrypoints, configs, and current TODO surfaces so the plan is grounded in the actual implementation, not just the docs or user prompt.
Treat clarification as a way to resolve the right assumptions, goals, and implementation paths. Do not ask preference questions that do not materially affect the plan.
Ask at most one substantive clarification or decision question per message.
Keep refining the execution plan as new evidence appears. After each user answer or new repo finding, update boundaries, sequencing, assumptions, and validation requirements before continuing.
Keep messages easy to scan: concise, no fluff, and use lightweight Markdown emphasis such as **bold** and *italics* when helpful. Do not depend on color.
For every clarification or decision message, put the choices at the bottom under a final **Options** section:
offer 2-4 concrete options grounded in the repo context
put the recommended option first and mark it clearly
prefix every option label with a visible selector in the label itself so plan-mode UIs still show a selectable key
default to letters: A., B., C.
use numbers only when the surrounding context is already numeric and that would be clearer
keep each option short and action-oriented
avoid open-ended options unless a free-form value is truly required
when practical, tell the user they can reply with just the selector
Flow (approval-gated)
Read the contract files above, any linked sub-specs, and the relevant codebase surfaces.
Review the current implementation before planning: affected modules, entrypoints, tests, manifests, configs, and existing TODO steps.
Identify the likely boundaries, risks, and validation surfaces for the requested change.
Ask for the change request only if it is not already clear from the user prompt.
Before drafting edits, identify only the blocking or plan-shaping clarifications that would materially change assumptions, goals, implementation paths, file placement, sequencing, or approval boundaries.
Ask clarifying questions one at a time using the interaction contract above.
If any material assumption would remain after the answers, list only those material assumptions and ask the user to confirm or correct them before continuing.
If only minor defaults remain, disclose them briefly in the plan and proceed without blocking.
Before drafting TODO edits, present 2-3 plan shapes when there is a real grouping, sequencing, or write-location decision to make.
Recommend one option based on the codebase review.
Keep the options at the bottom of the message under **Options**, with selector-prefixed labels such as A., B., C..
Draft proposed edits (grouped by file):
PRD/Blueprint deltas only if required
TODO step updates using the repo’s existing Step template
translate spec deltas into implementation deltas instead of restating product intent
for each new or revised execution step, include exact boundaries, interface or contract changes, sequencing notes, and validation evidence
add Implementation notes when the step would otherwise force the implementer to make decisions
split oversized mixed-surface work into dependency-ordered steps
Ask: Approve and apply these changes?
After applying, suggest implementing the next step via $cdd-implement-todo.
Weekly Installs
9
Repository
ruphware/cdd-skills
GitHub Stars
1
First Seen
11 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
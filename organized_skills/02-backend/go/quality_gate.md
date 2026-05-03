---
rating: ⭐⭐⭐
title: quality-gate
url: https://skills.sh/duc01226/easyplatform/quality-gate
---

# quality-gate

skills/duc01226/easyplatform/quality-gate
quality-gate
Installation
$ npx skills add https://github.com/duc01226/easyplatform --skill quality-gate
SKILL.md

[IMPORTANT] Use TaskCreate to break ALL work into small tasks BEFORE starting — including tasks for each file read. This prevents context loss from long files. For simple tasks, AI MUST ATTENTION ask user whether to skip.

Understand Code First — HARD-GATE: Do NOT write, plan, or fix until you READ existing code.

Search 3+ similar patterns (grep/glob) — cite file:line evidence
Read existing files in target area — understand structure, base classes, conventions
Run python .claude/scripts/code_graph trace <file> --direction both --json when .code-graph/graph.db exists
Map dependencies via connections or callers_of — know what depends on your target
Write investigation to .ai/workspace/analysis/ for non-trivial tasks (3+ files)
Re-read analysis file before implementing — never work from memory alone
NEVER invent new patterns when existing ones work — match exactly or document deviation

BLOCKED until: - [ ] Read target files - [ ] Grep 3+ patterns - [ ] Graph trace (if graph.db exists) - [ ] Assumptions verified with evidence

docs/project-reference/domain-entities-reference.md — Domain entity catalog, relationships, cross-service sync (read when task involves business entities/models) (content auto-injected by hook — check for [Injected: ...] header before reading)

Graph Impact Analysis — When .code-graph/graph.db exists, run blast-radius --json to detect ALL files affected by changes (7 edge types: CALLS, MESSAGE_BUS, API_ENDPOINT, TRIGGERS_EVENT, PRODUCES_EVENT, TRIGGERS_COMMAND_EVENT, INHERITS). Compute gap: impacted_files - changed_files = potentially stale files. Risk: <5 Low, 5-20 Medium, >20 High. Use trace --direction downstream for deep chains on high-impact files.

Quick Summary

Goal: Verify readiness criteria before proceeding to next phase.

Workflow:

Identify — Determine gate type (pre-dev, pre-QA, pre-release)
Check — Run gate-specific checklist items
Report — PASS/FAIL with evidence per criterion

Key Rules:

Output must be PASS or FAIL with specific evidence
Never skip checklist items — mark as N/A if not applicable
Block progression on FAIL — list blocking items

Be skeptical. Apply critical thinking, sequential thinking. Every claim needs traced proof, confidence percentages (Idea should be more than 80%).

Frontend/UI Context (if applicable)

When this task involves frontend or UI changes,

UI System Context — For ANY task touching .ts, .html, .scss, or .css files:

MUST ATTENTION READ before implementing:

docs/project-reference/frontend-patterns-reference.md — component base classes, stores, forms
docs/project-reference/scss-styling-guide.md — BEM methodology, SCSS variables, mixins, responsive
docs/project-reference/design-system/README.md — design tokens, component inventory, icons

Reference docs/project-config.json for project-specific paths.

Component patterns: docs/project-reference/frontend-patterns-reference.md
Styling/BEM guide: docs/project-reference/scss-styling-guide.md
Design system tokens: docs/project-reference/design-system/README.md
Gate Types & Checklists
Pre-Development Gate
 Acceptance criteria defined and clear
 Dependencies identified and available
 Design specs available (if UI work)
 No blocking questions unresolved
 Story points assigned (Fibonacci 1-21: 1=trivial, 2=small, 3=medium, 5=large, 8=very large, 13=epic SHOULD split, 21=MUST ATTENTION split)
Pre-QA Gate
 All acceptance criteria implemented
 Unit tests passing
 Code review complete
 No known critical bugs
 Test data prepared
Pre-Release Gate
 All tests passing (unit + integration)
 Code review complete
 CHANGELOG.md up-to-date
 No critical/major open bugs
 Documentation up-to-date
 Rollback strategy defined
Database Performance Gate (ALL gate types)

[IMPORTANT] Database Performance Protocol (MANDATORY):

Paging Required — ALL list/collection queries MUST ATTENTION use pagination. NEVER load all records into memory. Verify: no unbounded GetAll(), ToList(), or Find() without Skip/Take or cursor-based paging.
Index Required — ALL query filter fields, foreign keys, and sort columns MUST ATTENTION have database indexes configured. Verify: entity expressions match index field order, database collections have index management methods, migrations include indexes for WHERE/JOIN/ORDER BY columns.
 All list queries use pagination (no unbounded GetAll/ToList)
 Query filter fields have matching database indexes
 Foreign keys have database indexes configured
 Sort columns have database indexes configured
Output Format
## Quality Gate Result

**Gate Type:** [Pre-Dev | Pre-QA | Pre-Release]
**Verdict:** PASS | FAIL
**Date:** {date}

### Checklist

- [pass] [Item] — [evidence]
- [fail] [Item] — [reason for failure]
- N/A [Item] — [why not applicable]

### Blocking Items (if FAIL)
1. [Specific item that must be resolved]

IMPORTANT Task Planning Notes (MUST ATTENTION FOLLOW)
Always plan and break work into many small todo tasks using TaskCreate
Always add a final review todo task to verify work quality and identify fixes/enhancements
Workflow Recommendation

MANDATORY IMPORTANT MUST ATTENTION — NO EXCEPTIONS: If you are NOT already in a workflow, you MUST ATTENTION use AskUserQuestion to ask the user. Do NOT judge task complexity or decide this is "simple enough to skip" — the user decides whether to use a workflow, not you:

Activate pre-development workflow (Recommended) — quality-gate → plan → plan-review → plan-validate
Execute /quality-gate directly — run this skill standalone
Closing Reminders
IMPORTANT MUST ATTENTION break work into small todo tasks using TaskCreate BEFORE starting
IMPORTANT MUST ATTENTION search codebase for 3+ similar patterns before creating new code
IMPORTANT MUST ATTENTION cite file:line evidence for every claim (confidence >80% to act)
IMPORTANT MUST ATTENTION add a final review todo task to verify work quality MANDATORY IMPORTANT MUST ATTENTION READ the following files before starting:
IMPORTANT MUST ATTENTION search 3+ existing patterns and read code BEFORE any modification. Run graph trace when graph.db exists.
IMPORTANT MUST ATTENTION run graph impact analysis on changed files. Compute gap: impacted minus changed = potentially stale.
IMPORTANT MUST ATTENTION read frontend-patterns-reference, scss-styling-guide, and design-system/README before any UI work.
Weekly Installs
31
Repository
duc01226/easyplatform
GitHub Stars
6
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
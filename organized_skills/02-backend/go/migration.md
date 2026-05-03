---
rating: ⭐⭐
title: migration
url: https://skills.sh/duc01226/easyplatform/migration
---

# migration

skills/duc01226/easyplatform/migration
migration
Installation
$ npx skills add https://github.com/duc01226/easyplatform --skill migration
SKILL.md

[IMPORTANT] Use TaskCreate to break ALL work into small tasks BEFORE starting — including tasks for each file read. This prevents context loss from long files. For simple tasks, AI MUST ATTENTION ask user whether to skip.

Prerequisites: MUST ATTENTION READ before executing:

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
Quick Summary

Goal: Create data or schema migrations following your project's platform patterns.

Workflow:

Analyze — Understand migration requirements and target database
Create — Generate migration following platform conventions
Verify — Run and validate the migration

Key Rules:

Follow platform migration patterns (EF migrations or project data migration executor, see docs/project-reference/backend-patterns-reference.md)
Always use understand-code-first protocol before creating migrations

Be skeptical. Apply critical thinking, sequential thinking. Every claim needs traced proof, confidence percentages (Idea should be more than 80%).

$ARGUMENTS

⚠️ MUST ATTENTION READ references/migration-patterns.md for migration patterns.

IMPORTANT: Present your migration design and wait for explicit user approval before creating files.

Example
/migration "Add department field to Employee entity"

Closing Reminders
MANDATORY IMPORTANT MUST ATTENTION break work into small todo tasks using TaskCreate BEFORE starting
MANDATORY IMPORTANT MUST ATTENTION search codebase for 3+ similar patterns before creating new code
MANDATORY IMPORTANT MUST ATTENTION cite file:line evidence for every claim (confidence >80% to act)
MANDATORY IMPORTANT MUST ATTENTION add a final review todo task to verify work quality MANDATORY IMPORTANT MUST ATTENTION READ the following files before starting:
MANDATORY IMPORTANT MUST ATTENTION search 3+ existing patterns and read code BEFORE any modification. Run graph trace when graph.db exists.
MANDATORY IMPORTANT MUST ATTENTION READ references/migration-patterns.md before starting
Weekly Installs
34
Repository
duc01226/easyplatform
GitHub Stars
6
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
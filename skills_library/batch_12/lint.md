---
title: lint
url: https://skills.sh/duc01226/easyplatform/lint
---

# lint

skills/duc01226/easyplatform/lint
lint
Installation
$ npx skills add https://github.com/duc01226/easyplatform --skill lint
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

Quick Summary

Goal: Run linters (.NET analyzers and/or ESLint/Prettier) and report or auto-fix code quality issues.

Workflow:

Parse — Determine scope from arguments: backend, frontend, or both; fix mode or report-only
Execute — Run dotnet build for .NET analyzers or nx lint / prettier for Angular
Report — Group issues by severity (error/warning/info) with file paths and line numbers

Key Rules:

No argument = run both backend + frontend in report-only mode
fix argument = apply safe auto-fixes, report remaining manual items
Always show file paths and line numbers in output

Be skeptical. Apply critical thinking, sequential thinking. Every claim needs traced proof, confidence percentages (Idea should be more than 80%).

Run linting: $ARGUMENTS

Instructions

Parse arguments:

backend or be → Run .NET analyzers
frontend or fe → Run ESLint/Prettier
fix → Auto-fix issues where possible
No argument → Run both, report only

For Backend (.NET):

dotnet build {SolutionName}.sln /p:TreatWarningsAsErrors=false

Check for analyzer warnings (CA*, IDE*, etc.)
Report code style violations

For Frontend (Angular/Nx):

cd src/{ExampleAppWeb}
nx lint playground-text-snippet
nx lint {lib-name}


With auto-fix:

nx lint playground-text-snippet --fix
npx prettier --write "apps/**/*.{ts,html,scss}" "libs/**/*.{ts,html,scss}"


Report format:

Group issues by severity (error, warning, info)
Show file paths and line numbers
Suggest fixes for common issues

Auto-fix behavior:

If fix argument provided, apply safe auto-fixes
Report what was fixed vs what needs manual attention
Closing Reminders
IMPORTANT MUST ATTENTION break work into small todo tasks using TaskCreate BEFORE starting
IMPORTANT MUST ATTENTION search codebase for 3+ similar patterns before creating new code
IMPORTANT MUST ATTENTION cite file:line evidence for every claim (confidence >80% to act)
IMPORTANT MUST ATTENTION add a final review todo task to verify work quality
IMPORTANT MUST ATTENTION search 3+ existing patterns and read code BEFORE any modification. Run graph trace when graph.db exists.
Weekly Installs
37
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
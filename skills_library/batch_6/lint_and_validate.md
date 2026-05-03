---
title: lint-and-validate
url: https://skills.sh/davila7/claude-code-templates/lint-and-validate
---

# lint-and-validate

skills/davila7/claude-code-templates/lint-and-validate
lint-and-validate
Originally fromsickn33/antigravity-awesome-skills
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill lint-and-validate
SKILL.md
Lint and Validate Skill

MANDATORY: Run appropriate validation tools after EVERY code change. Do not finish a task until the code is error-free.

Procedures by Ecosystem
Node.js / TypeScript
Lint/Fix: npm run lint or npx eslint "path" --fix
Types: npx tsc --noEmit
Security: npm audit --audit-level=high
Python
Linter (Ruff): ruff check "path" --fix (Fast & Modern)
Security (Bandit): bandit -r "path" -ll
Types (MyPy): mypy "path"
The Quality Loop
Write/Edit Code
Run Audit: npm run lint && npx tsc --noEmit
Analyze Report: Check the "FINAL AUDIT REPORT" section.
Fix & Repeat: Submitting code with "FINAL AUDIT" failures is NOT allowed.
Error Handling
If lint fails: Fix the style or syntax issues immediately.
If tsc fails: Correct type mismatches before proceeding.
If no tool is configured: Check the project root for .eslintrc, tsconfig.json, pyproject.toml and suggest creating one.

Strict Rule: No code should be committed or reported as "done" without passing these checks.

Scripts
Script	Purpose	Command
scripts/lint_runner.py	Unified lint check	python scripts/lint_runner.py <project_path>
scripts/type_coverage.py	Type coverage analysis	python scripts/type_coverage.py <project_path>
Weekly Installs
254
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass
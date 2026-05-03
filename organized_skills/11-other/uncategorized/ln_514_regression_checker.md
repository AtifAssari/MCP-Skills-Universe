---
rating: ⭐⭐
title: ln-514-regression-checker
url: https://skills.sh/levnikolaevich/claude-code-skills/ln-514-regression-checker
---

# ln-514-regression-checker

skills/levnikolaevich/claude-code-skills/ln-514-regression-checker
ln-514-regression-checker
Installation
$ npx skills add https://github.com/levnikolaevich/claude-code-skills --skill ln-514-regression-checker
SKILL.md

Paths: File paths (shared/, references/, ../ln-*) are relative to skills repo root. If not found at CWD, locate this SKILL.md directory and go up one level for repo root.

Regression Checker

Runs the existing test suite to ensure no regressions after implementation changes.

Purpose & Scope
Detect test framework (pytest/jest/vitest/go test/etc.) and test dirs.
Execute full suite; capture results for Story quality gate.
Return PASS/FAIL with counts/log excerpts; never modifies Linear or kanban.
When to Use
Invoked by ln-510-quality-coordinator Phase 7
Code quality check passed
Workflow (concise)
Auto-discover test framework per shared/references/ci_tool_detection.md Command Registry (Test Frameworks section).
Read docs/project/runbook.md — get exact test commands, Docker setup, environment variables. Runbook commands take priority over auto-detection (per ci_tool_detection.md Discovery Hierarchy).
Build appropriate test command; run with timeout (5min per ci_tool_detection.md); capture stdout/stderr.
Parse results: passed/failed counts; key failing tests.
Output verdict JSON (PASS or FAIL + failures list) and add Linear comment.
Critical Rules
No selective test runs; run full suite.
Do not fix tests or change status; only report.
Language preservation in comment (EN/RU).
Definition of Done
Framework detected; command executed.
Results parsed; verdict produced with failing tests (if any).
Linear comment posted with summary.
Reference Files
Risk-based limits used downstream: ../shared/references/risk_based_testing_guide.md
CI tool detection: shared/references/ci_tool_detection.md

Version: 3.1.0 Last Updated: 2026-01-09

Weekly Installs
55
Repository
levnikolaevich/…e-skills
GitHub Stars
445
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass
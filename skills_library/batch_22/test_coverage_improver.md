---
title: test-coverage-improver
url: https://skills.sh/openai/openai-agents-python/test-coverage-improver
---

# test-coverage-improver

skills/openai/openai-agents-python/test-coverage-improver
test-coverage-improver
Installation
$ npx skills add https://github.com/openai/openai-agents-python --skill test-coverage-improver
SKILL.md
Test Coverage Improver
Overview

Use this skill whenever coverage needs assessment or improvement (coverage regressions, failing thresholds, or user requests for stronger tests). It runs the coverage suite, analyzes results, highlights the biggest gaps, and prepares test additions while confirming with the user before changing code.

Quick Start
From the repo root run make coverage to regenerate .coverage data and coverage.xml.
Collect artifacts: .coverage and coverage.xml, plus the console output from coverage report -m for drill-downs.
Summarize coverage: total percentages, lowest files, and uncovered lines/paths.
Draft test ideas per file: scenario, behavior under test, expected outcome, and likely coverage gain.
Ask the user for approval to implement the proposed tests; pause until they agree.
After approval, write the tests in tests/, rerun make coverage, and then run $code-change-verification before marking work complete.
Workflow Details
Run coverage: Execute make coverage at repo root. Avoid watch flags and keep prior coverage artifacts only if comparing trends.
Parse summaries efficiently:
Prefer the console output from coverage report -m for file-level totals; fallback to coverage.xml for tooling or spreadsheets.
Use uv run coverage html to generate htmlcov/index.html if you need an interactive drill-down.
Prioritize targets:
Public APIs or shared utilities in src/agents/ before examples or docs.
Files with low statement coverage or newly added code at 0%.
Recent bug fixes or risky code paths (error handling, retries, timeouts, concurrency).
Design impactful tests:
Hit uncovered paths: error cases, boundary inputs, optional flags, and cancellation/timeouts.
Cover combinational logic rather than trivial happy paths.
Place tests under tests/ and avoid flaky async timing.
Coordinate with the user: Present a numbered, concise list of proposed test additions and expected coverage gains. Ask explicitly before editing code or fixtures.
After implementation: Rerun coverage, report the updated summary, and note any remaining low-coverage areas.
Notes
Keep any added comments or code in English.
Do not create scripts/, references/, or assets/ unless needed later.
If coverage artifacts are missing or stale, rerun pnpm test:coverage instead of guessing.
Weekly Installs
183
Repository
openai/openai-a…s-python
GitHub Stars
25.8K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
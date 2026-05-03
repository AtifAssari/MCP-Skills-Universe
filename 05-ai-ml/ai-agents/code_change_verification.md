---
title: code-change-verification
url: https://skills.sh/openai/openai-agents-python/code-change-verification
---

# code-change-verification

skills/openai/openai-agents-python/code-change-verification
code-change-verification
Installation
$ npx skills add https://github.com/openai/openai-agents-python --skill code-change-verification
SKILL.md
Code Change Verification
Overview

Ensure work is only marked complete after formatting, linting, type checking, and tests pass. Use this skill when changes affect runtime code, tests, or build/test configuration. You can skip it for docs-only or repository metadata unless a user asks for the full stack.

Quick start
Keep this skill at ./.agents/skills/code-change-verification so it loads automatically for the repository.
macOS/Linux: bash .agents/skills/code-change-verification/scripts/run.sh.
Windows: powershell -ExecutionPolicy Bypass -File .agents/skills/code-change-verification/scripts/run.ps1.
The scripts run make format first, then run make lint, make typecheck, and make tests in parallel with fail-fast semantics.
While the parallel steps are still running, the scripts emit periodic heartbeat updates so you can tell that work is still in progress.
If any command fails, fix the issue, rerun the script, and report the failing output.
Confirm completion only when all commands succeed with no remaining issues.
Manual workflow
If dependencies are not installed or have changed, run make sync first to install dev requirements via uv.
Run from the repository root with make format first, then make lint, make typecheck, and make tests.
Do not skip steps; stop and fix issues immediately when a command fails.
If you run the steps manually, you may parallelize make lint, make typecheck, and make tests after make format completes, but you must stop the remaining steps as soon as one fails.
Re-run the full stack after applying fixes so the commands execute in the required order.
Resources
scripts/run.sh
Executes make format first, then runs make lint, make typecheck, and make tests in parallel with fail-fast semantics from the repository root. It also emits periodic heartbeat updates while the parallel steps are still running. Prefer this entry point to preserve the required ordering while reducing total runtime.
scripts/run.ps1
Windows-friendly wrapper that runs the same sequence with make format first and the remaining steps in parallel with fail-fast semantics, plus periodic heartbeat updates while work is still running. Use from PowerShell with execution policy bypass if required by your environment.
Weekly Installs
101
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
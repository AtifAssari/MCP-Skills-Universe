---
title: testing
url: https://skills.sh/elie222/inbox-zero/testing
---

# testing

skills/elie222/inbox-zero/testing
testing
Installation
$ npx skills add https://github.com/elie222/inbox-zero --skill testing
SKILL.md
Testing

All testing guidance lives in this directory. Read the relevant file for your task:

Type	File	When to use
Unit tests	unit.md	Framework setup, mocks, colocated tests
Writing tests	write-tests.md	What to test, what to skip, workflow
LLM tests	llm.md	Tests that call real LLMs (pnpm test-ai)
Eval suite	eval.md	Cross-model comparison, LLM-as-judge
Integration	integration.md	Emulator-backed tests (pnpm test-integration)
E2E tests	e2e.md	Real email workflow tests from inbox-zero-e2e repo

Prefer behavior-focused assertions; avoid freezing prompt copy or internal call shapes unless those exact values are the contract under test.

Quick Commands
pnpm test -- path/to/file.test.ts   # Single unit test
pnpm test --run                      # All unit tests
pnpm test-integration                # Integration tests (emulator)
pnpm test-ai your-feature            # AI test (real LLM)
EVAL_MODELS=all pnpm test-ai eval/your-feature  # Eval across models

Weekly Installs
20
Repository
elie222/inbox-zero
GitHub Stars
10.6K
First Seen
Mar 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
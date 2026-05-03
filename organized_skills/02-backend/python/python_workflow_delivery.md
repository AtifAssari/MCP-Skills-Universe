---
rating: ⭐⭐
title: python-workflow-delivery
url: https://skills.sh/ahgraber/skills/python-workflow-delivery
---

# python-workflow-delivery

skills/ahgraber/skills/python-workflow-delivery
python-workflow-delivery
Installation
$ npx skills add https://github.com/ahgraber/skills --skill python-workflow-delivery
SKILL.md
Python Workflow and Delivery
Overview

Branch-to-PR execution discipline for Python work: validate, scope, and ship with confidence. Apply these defaults before opening or updating a PR.

These are preferred defaults for common cases, not universal rules. When deviating, call out tradeoffs and compensating controls (tests, observability, migration, rollback).

When to Use
Preparing a branch or PR for Python changes.
CI gate failures on lint, format, or test steps.
Lockfile or dependency conflicts during uv sync.
Commits that bundle too many concerns or are hard to review.
Uncertainty about which validation steps to run before merge.

When NOT to use:

Pure design or architecture decisions — see python-design-modularity.
Test strategy or fixture design — see python-testing.
Runtime operations or deployment — see python-runtime-operations.
Quick Reference
Use the project-defined Python version first.
Use uv for environment and dependency workflow.
Run checks with uv run ....
Keep scope small, reversible, and reviewable.
Validation Gate

Run as required by project scope:

uv sync
uv sync --locked
uv lock --check
uv run ruff check .
uv run ruff format --check .
uv run pytest

Change-specific checks:

Dependency/lockfile changes: uv run pytest scripts/test_pypi_security_audit.py -v
Async lifecycle changes: run pyleak diagnostics on representative async integration tests.
Common Mistakes
Skipping uv lock --check — merging without verifying the lockfile matches pyproject.toml causes CI failures downstream.
Bundling unrelated changes in one commit — mixing refactors, features, and dependency bumps makes review slow and reverts dangerous.
Running ruff check but not ruff format --check — passing lint does not guarantee formatting; both gates matter.
Forgetting change-specific checks — dependency updates need the security audit; async changes need leak diagnostics. Generic pytest alone is not enough.
Scope Note
Treat these recommendations as preferred defaults for common cases, not universal rules.
If a default conflicts with project constraints or worsens the outcome, suggest a better-fit alternative and explain why it is better for this case.
When deviating, call out tradeoffs and compensating controls (tests, observability, migration, rollback).
Invocation Notice
Inform the user when this skill is being invoked by name: python-design-modularity.
References
references/workflow.md
references/branch-commit-scope.md
Weekly Installs
20
Repository
ahgraber/skills
GitHub Stars
2
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail
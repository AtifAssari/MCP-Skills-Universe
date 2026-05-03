---
rating: ⭐⭐
title: verify
url: https://skills.sh/facebook/react/verify
---

# verify

skills/facebook/react/verify
verify
Installation
$ npx skills add https://github.com/facebook/react --skill verify
Summary

Pre-commit validation for React contributions with parallel type checking and testing.

Runs formatting and linting sequentially, stopping on first failure to catch issues early
Executes type checking and dual test suites (source and www) in parallel using subagents for efficiency
Accepts optional test pattern argument to filter which tests run
Provides detailed failure reporting with suggested fixes when any step fails
SKILL.md
Verification

Run all verification steps.

Arguments:

$ARGUMENTS: Test pattern for the test step
Instructions

Run these first in sequence:

Run yarn prettier - format code (stop if fails)
Run yarn linc - lint changed files (stop if fails)

Then run these with subagents in parallel:

Use /flow to type check (stop if fails)
Use /test to test changes in source (stop if fails)
Use /test www to test changes in www (stop if fails)

If all pass, show success summary. On failure, stop immediately and report the issue with suggested fixes.

Weekly Installs
867
Repository
facebook/react
GitHub Stars
244.8K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
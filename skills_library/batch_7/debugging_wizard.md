---
title: debugging-wizard
url: https://skills.sh/jeffallan/claude-skills/debugging-wizard
---

# debugging-wizard

skills/jeffallan/claude-skills/debugging-wizard
debugging-wizard
Installation
$ npx skills add https://github.com/jeffallan/claude-skills --skill debugging-wizard
Summary

Systematic bug isolation and root cause analysis through hypothesis-driven debugging methodology.

Applies five-step workflow: reproduce, isolate, hypothesize and test, fix, and prevent through regression tests
Includes language-specific debugger guidance (Python pdb, Node.js Inspector, Go delve) and advanced strategies like git bisect for regression hunting
Enforces strict constraints: reproduce first, test one hypothesis at a time, document findings, and remove debug code before committing
Provides structured output format covering root cause, evidence from stack traces or logs, fix implementation, and prevention safeguards
SKILL.md
Debugging Wizard

Expert debugger applying systematic methodology to isolate and resolve issues in any codebase.

Core Workflow
Reproduce - Establish consistent reproduction steps
Isolate - Narrow down to smallest failing case
Hypothesize and test - Form testable theories, verify/disprove each one
Fix - Implement and verify solution
Prevent - Add tests/safeguards against regression
Reference Guide

Load detailed guidance based on context:

Topic	Reference	Load When
Debugging Tools	references/debugging-tools.md	Setting up debuggers by language
Common Patterns	references/common-patterns.md	Recognizing bug patterns
Strategies	references/strategies.md	Binary search, git bisect, time travel
Quick Fixes	references/quick-fixes.md	Common error solutions
Systematic Debugging	references/systematic-debugging.md	Complex bugs, multiple failed fixes, root cause analysis
Constraints
MUST DO
Reproduce the issue first
Gather complete error messages and stack traces
Test one hypothesis at a time
Document findings for future reference
Add regression tests after fixing
Remove all debug code before committing
MUST NOT DO
Guess without testing
Make multiple changes at once
Skip reproduction steps
Assume you know the cause
Debug in production without safeguards
Leave console.log/debugger statements in code
Common Debugging Commands

Python (pdb)

python -m pdb script.py          # launch debugger
# inside pdb:
# b 42          — set breakpoint at line 42
# n             — step over
# s             — step into
# p some_var    — print variable
# bt            — print full traceback


JavaScript (Node.js)

node --inspect-brk script.js     # pause at first line, attach Chrome DevTools
# In Chrome: open chrome://inspect → click "inspect"
# Sources panel: add breakpoints, watch expressions, step through


Git bisect (regression hunting)

git bisect start
git bisect bad                   # current commit is broken
git bisect good v1.2.0           # last known good tag/commit
# Git checks out midpoint — test, then:
git bisect good   # or: git bisect bad
# Repeat until git identifies the first bad commit
git bisect reset


Go (delve)

dlv debug ./cmd/server           # build & attach
# (dlv) break main.go:55
# (dlv) continue
# (dlv) print myVar

Output Templates

When debugging, provide:

Root Cause: What specifically caused the issue
Evidence: Stack trace, logs, or test that proves it
Fix: Code change that resolves it
Prevention: Test or safeguard to prevent recurrence

Documentation

Weekly Installs
1.9K
Repository
jeffallan/claude-skills
GitHub Stars
8.7K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
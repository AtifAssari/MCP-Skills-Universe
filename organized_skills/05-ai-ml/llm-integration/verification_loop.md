---
rating: ⭐⭐⭐
title: verification-loop
url: https://skills.sh/affaan-m/everything-claude-code/verification-loop
---

# verification-loop

skills/affaan-m/everything-claude-code/verification-loop
verification-loop
Installation
$ npx skills add https://github.com/affaan-m/everything-claude-code --skill verification-loop
Summary

Comprehensive verification system running build, type, lint, test, and security checks across Claude Code sessions.

Executes six sequential verification phases: build compilation, type checking, linting, test suite with coverage reporting, security scanning for secrets and debug statements, and git diff review
Supports both JavaScript/TypeScript (npm/pnpm, tsc, ESLint) and Python (pyright, ruff) projects with language-specific commands
Produces a structured verification report indicating pass/fail status for each phase, total test counts, coverage percentage, and a PR-readiness determination
Designed for checkpoint verification after feature completion, refactoring, or before creating pull requests; can run continuously every 15 minutes during long sessions
SKILL.md
Verification Loop Skill

A comprehensive verification system for Claude Code sessions.

When to Use

Invoke this skill:

After completing a feature or significant code change
Before creating a PR
When you want to ensure quality gates pass
After refactoring
Verification Phases
Phase 1: Build Verification
# Check if project builds
npm run build 2>&1 | tail -20
# OR
pnpm build 2>&1 | tail -20


If build fails, STOP and fix before continuing.

Phase 2: Type Check
# TypeScript projects
npx tsc --noEmit 2>&1 | head -30

# Python projects
pyright . 2>&1 | head -30


Report all type errors. Fix critical ones before continuing.

Phase 3: Lint Check
# JavaScript/TypeScript
npm run lint 2>&1 | head -30

# Python
ruff check . 2>&1 | head -30

Phase 4: Test Suite
# Run tests with coverage
npm run test -- --coverage 2>&1 | tail -50

# Check coverage threshold
# Target: 80% minimum


Report:

Total tests: X
Passed: X
Failed: X
Coverage: X%
Phase 5: Security Scan
# Check for secrets
grep -rn "sk-" --include="*.ts" --include="*.js" . 2>/dev/null | head -10
grep -rn "api_key" --include="*.ts" --include="*.js" . 2>/dev/null | head -10

# Check for console.log
grep -rn "console.log" --include="*.ts" --include="*.tsx" src/ 2>/dev/null | head -10

Phase 6: Diff Review
# Show what changed
git diff --stat
git diff HEAD~1 --name-only


Review each changed file for:

Unintended changes
Missing error handling
Potential edge cases
Output Format

After running all phases, produce a verification report:

VERIFICATION REPORT
==================

Build:     [PASS/FAIL]
Types:     [PASS/FAIL] (X errors)
Lint:      [PASS/FAIL] (X warnings)
Tests:     [PASS/FAIL] (X/Y passed, Z% coverage)
Security:  [PASS/FAIL] (X issues)
Diff:      [X files changed]

Overall:   [READY/NOT READY] for PR

Issues to Fix:
1. ...
2. ...

Continuous Mode

For long sessions, run verification every 15 minutes or after major changes:

Set a mental checkpoint:
- After completing each function
- After finishing a component
- Before moving to next task

Run: /verify

Integration with Hooks

This skill complements PostToolUse hooks but provides deeper verification. Hooks catch issues immediately; this skill provides comprehensive review.

Weekly Installs
3.2K
Repository
affaan-m/everyt…ude-code
GitHub Stars
171.6K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail
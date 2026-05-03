---
rating: ⭐⭐
title: forge-quick-spec
url: https://skills.sh/fwehrling/forge/forge-quick-spec
---

# forge-quick-spec

skills/fwehrling/forge/forge-quick-spec
forge-quick-spec
Installation
$ npx skills add https://github.com/fwehrling/forge --skill forge-quick-spec
SKILL.md
/forge-quick-spec — FORGE Quick Track

Fast-track mode for bug fixes and small changes (<1 day). Skips the planning and architecture phases.

Workflow

Load context (if FORGE project):

Read .forge/memory/MEMORY.md for project context (if exists)
forge-memory search "<change description>" --limit 3 (if available)

Classify the request: Bug fix or small feature change?

Bug Fix Track

Root cause analysis (in-memory, no artifact):

Reproduce: Steps to reproduce, expected vs. actual behavior
Identify cause: Pinpoint the root cause (not just the symptom)
Affected components: Frontend / Backend / Database / External services
Code location: File path, function/method, line range

Impact & risk assessment:

Severity: Blocker / Major / Minor / Trivial
Affected users: Scope of impact
Side effects: What else could this fix break?
Rollback plan: How to revert if the fix causes regression

Write regression tests first (TDD):

Test that reproduces the bug (must fail before fix)
Unit tests for the fix
Functional test covering the user flow

Implement the fix

Validate:

Regression test now passes
All pre-existing tests still pass (non-regression)
Lint + typecheck clean
Side effects verified

Propose the commit (format: fix: <description>)

Small Change Track
Analyze the request
Generate a quick spec (in-memory, no artifact)
Write tests (unit + functional for the change)
Implement the change
Validate (lint + typecheck + tests)
Propose the commit
Save Memory

Save memory (ensures fix context persists for avoiding repeated issues):

forge-memory log "Quick-spec terminé : {DESCRIPTION}, {N} tests" --agent dev
forge-memory consolidate --verbose
forge-memory sync


Report to user:

FORGE Quick Track — Complete
──────────────────────────────
Type      : Bug Fix | Small Change
Change    : <description>
Tests     : X unit + Y functional (all passing)
Lint/Type : clean

Commit proposed:
  fix: <description>

Weekly Installs
14
Repository
fwehrling/forge
GitHub Stars
1
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
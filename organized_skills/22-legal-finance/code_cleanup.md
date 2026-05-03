---
rating: ⭐⭐⭐
title: code-cleanup
url: https://skills.sh/hungv47/prod-skills/code-cleanup
---

# code-cleanup

skills/hungv47/prod-skills/code-cleanup
code-cleanup
Installation
$ npx skills add https://github.com/hungv47/prod-skills --skill code-cleanup
SKILL.md
Code Cleanup — Orchestrator

Productivity — Multi-agent orchestration. Structural cleanup, code-level cleanup, and refactoring — without breaking functionality.

Core Question: "Is this change purely structural with zero behavioral impact?"

Inputs Required
A codebase or set of files to clean up
User intent: structural reorganization, code-level cleanup, refactoring, or all three
Output
.agents/cleanup-report.md
Chain Position

Previous: none | Next: none (standalone)

Re-run triggers: After major feature additions, before release milestones, when test suite runtime grows significantly, or when onboarding new team members.

Multi-Agent Architecture
Agent Roster
Agent	File	Focus
structural-scanner-agent	agents/structural-scanner-agent.md	Junk files, empty dirs, naming conventions, structure anomalies
code-scanner-agent	agents/code-scanner-agent.md	AI slop, code smells, dead code, safety issues
dependency-scanner-agent	agents/dependency-scanner-agent.md	Unused packages, duplicates, security vulnerabilities
safe-removal-agent	agents/safe-removal-agent.md	Executes verified deletions with backup commits
refactoring-agent	agents/refactoring-agent.md	Applies targeted refactoring without behavioral change
validation-agent	agents/validation-agent.md	Runs tests, types, lint, build — reports pass/fail
critic-agent	agents/critic-agent.md	Golden rules compliance, behavioral preservation review
Execution Layers
Layer 1 (parallel):
  structural-scanner-agent ───┐
  code-scanner-agent ─────────┤── scan simultaneously
  dependency-scanner-agent ───┘

Layer 2 (sequential):
  safe-removal-agent ──────────── removes verified targets from all 3 scans
    → refactoring-agent ───────── applies code-level fixes from code scanner
      → validation-agent ──────── runs all checks
        → critic-agent ─────────── final golden rules review

Dispatch Protocol
Triage — determine scope from user intent:
"Reorganize files" → structural-scanner only
"Remove AI slop" → code-scanner only
"Clean up the codebase" → all three scanners
Layer 1 dispatch — send brief to relevant scanner agents in parallel.
Safe removal — pass all scan results to safe-removal-agent. It creates a backup commit, then removes verified-safe targets.
Refactoring — pass code scanner results + removal results to refactoring-agent. It fixes code-level issues.
Validation — validation-agent runs all available checks (tests, types, lint, build).
Critic review — critic-agent checks golden rules compliance. If FAIL, identify the specific change to revert.
Assembly — compile cleanup report. Save to .agents/cleanup-report.md.
Routing Rules
Condition	Route
User says "structural only"	Only dispatch structural-scanner → safe-removal → validation → critic
User says "code-level only"	Only dispatch code-scanner → refactoring → validation → critic
User says "refactor this"	Only dispatch code-scanner → refactoring → validation → critic
User says "clean up everything"	All scanners → safe-removal → refactoring → validation → critic
Validation fails	Identify which change broke it; revert that specific change
Critic PASS	Assemble report and deliver
Critic FAIL	Revert specific change; re-run validation
Session >30 changes	Stop and reassess scope
Critical Gates (The 5 Golden Rules)

Before delivering, the critic-agent verifies ALL golden rules pass:

Preserve behavior — Every change must produce the same observable behavior. If you can't verify this, don't make the change.
Small incremental steps — One change at a time. Commit between steps. Never combine a refactor with a feature change.
Check existing conventions first — Before changing anything, read the codebase's existing coding guidelines, linting config, naming patterns, and file structure. Match them.
Test after each change — Run the test suite after every modification. If tests break, revert and try a smaller step.
Rollback awareness — Commit before starting. Note the hash. If a change chain gets too complex, revert and try a different approach.

Additional gate: Session limits — target ~30 changes per cleanup session. After 15 changes, generate an interim summary. If each fix spawns 2+ new issues, stop and reassess.

If any golden rule fails: the critic identifies the specific change that violated it and recommends reverting.

Single-Agent Fallback

When context window is constrained or the cleanup scope is small (fewer than 5 files):

Skip multi-agent dispatch
Create backup commit
Scan the target files for structural issues, code smells, and dead code
Apply fixes one at a time, testing after each
Run all available checks
Verify golden rules compliance as self-review
Save to .agents/cleanup-report.md
Triage

Determine scope before starting. Parts can be used independently or combined.

User intent	Scanners to dispatch
"Reorganize files", "remove dead code", "clean up repo structure"	structural-scanner-agent
"Remove AI slop", "clean up PR", "fix code smells"	code-scanner-agent
"Check dependencies", "remove unused packages"	dependency-scanner-agent
"Refactor this", "extract this", "redesign this module"	code-scanner-agent → refactoring-agent
"Clean up the codebase" (broad)	All three scanners → safe-removal → refactoring
AI Slop Patterns

The code-scanner-agent specifically looks for these AI-generated code patterns:

Comments to remove:

Obvious/redundant comments explaining what code clearly does
Comments that don't match the commenting style elsewhere in the file
Section divider comments when not used elsewhere

Defensive code to remove:

Try/catch blocks around code that doesn't throw
Null/undefined checks when callers guarantee valid input
Type guards that duplicate earlier validation

Type issues to fix:

Casts to any that bypass TypeScript's type system
Type assertions that hide real type mismatches
Overly broad generic types when specific types exist
When NOT to Refactor

The refactoring-agent skips these situations:

No test coverage — you can't verify behavior is preserved. Write tests first.
Tight deadline — ship first, refactor later.
Code that won't change again — if nobody will read or modify it, the investment doesn't pay off.
During a feature change — separate commits. Always.
Anti-Patterns
Anti-Pattern	Problem	INSTEAD
Behavioral changes disguised as cleanup	Observable output changes	refactoring-agent verifies same behavior, different structure
"Tests pass so it's fine"	Incomplete coverage means passing tests don't guarantee equivalence	validation-agent flags uncovered code for manual verification
Combining cleanup with features	One change at a time	safe-removal and refactoring agents never add features
Removing "probably unused" code	May be dynamically imported	dependency-scanner verifies zero imports before flagging
Flagging conventions as smells	Existing patterns are intentional	code-scanner reads surrounding code before flagging
Large batch removals	Can't identify which removal broke something	safe-removal-agent works in small batches, tests between each
Worked Example

User: "Clean up this Express API project, it's gotten messy after 6 months."

Triage: Broad cleanup — dispatch all three scanners.

Layer 1 (parallel):

structural-scanner-agent → 4 unused files in /utils, 2 duplicate helpers, naming inconsistency (userController.js vs product-controller.js)
code-scanner-agent → Pass 1: 0 safety issues. Pass 2: 12 TODO comments, 3 console.log, 2 commented-out blocks (>50 lines each), 5 AI slop instances
dependency-scanner-agent → 2 unused dependencies (lodash, moment), 1 duplicate (underscore alongside lodash)

Layer 2 (sequential):

safe-removal-agent → backup commit, removes 4 unused files + 2 commented blocks + lodash + underscore. Tests pass.
refactoring-agent → extracts shared validation into middleware/validate.js, normalizes to kebab-case, removes 12 TODOs and 3 console.logs
validation-agent → bun test: 47/47 pass. tsc --noEmit: clean. Lint: clean.
critic-agent → PASS. All 5 golden rules pass.

Artifact saved to .agents/cleanup-report.md.

Artifact Template

On re-run: rename existing artifact to cleanup-report.v[N].md and create new with incremented version.

---
skill: code-cleanup
version: 1
date: {{today}}
status: complete
---

# Cleanup Report

## Scope
[Structural / Code-Level / Refactoring / All]

## Changes Made
### Structural
### Code-Level
### Refactoring

## Validation
- Tests: [PASS/FAIL]
- Type check: [PASS/FAIL/SKIPPED]
- Lint: [PASS/FAIL/SKIPPED]
- Build: [PASS/FAIL/SKIPPED]

## Manual Verification Needed
[Features lacking test coverage]

Scripts
scripts/analyze_codebase.py — Static analysis tool that generates dependency reports, identifies junk files, empty directories, large directories, and potentially unused code files. Used by structural-scanner-agent and dependency-scanner-agent.
Weekly Installs
8
Repository
hungv47/prod-skills
GitHub Stars
1
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
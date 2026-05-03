---
title: cleanup
url: https://skills.sh/morphet81/cheat-sheets/cleanup
---

# cleanup

skills/morphet81/cheat-sheets/cleanup
cleanup
Installation
$ npx skills add https://github.com/morphet81/cheat-sheets --skill cleanup
SKILL.md

Orchestrate a full cleanup of the current working directory: review changes, verify tests, fix linting and audit issues, ensure full test coverage, propose fixes, and commit.

Usage:

/cleanup - Run the full cleanup workflow

Instructions:

IMPORTANT: This is an autonomous workflow. Run ALL checks and fixes yourself first, then present the results and proposed fixes to the developer at the end. Do NOT ask the developer questions during the process — only at the final approval step.

SCOPE: Focus exclusively on changes introduced by the current branch. Determine the base branch first (check .agent file for baseBranch=<value>, default to main). All review, coverage analysis, lint fixes, and test writing should target only the files and code changed between the base branch and the current state — do not flag or fix pre-existing issues in unchanged code.

Review uncommitted changes:

Run git status to see all modified, staged, and untracked files
Run git diff to see unstaged changes and git diff --cached to see staged changes
Also run git diff <base-branch>...HEAD to understand the full scope of changes on this branch
Read each changed file to understand the full context of modifications
Produce a brief summary of all changes on this branch grouped by category (new features, bug fixes, refactoring, etc.)

Verify new test cases:

Invoke the /verify-test-cases skill to check all test files modified since last push
Record any issues found (nonsensical tests, duplicates, missing coverage)

Run test coverage (ONCE):

Run the project's coverage command exactly once and save the full output. Do NOT re-run coverage later — reuse this output for all subsequent analysis.
Node.js: npm run test:coverage or npx jest --coverage or npx vitest run --coverage (check package.json scripts first)
Python: pytest --cov or coverage run -m pytest && coverage report
Rust: cargo tarpaulin or cargo llvm-cov
Go: go test -coverprofile=coverage.out ./... && go tool cover -func=coverage.out
Parse the output to identify:
Overall coverage percentage
Files and lines that are NOT covered
If coverage is 100%: record as passing and move on
If coverage is below 100%: for each uncovered file/line in files changed by this branch, write the missing test cases yourself to bring coverage to 100%. Add tests to existing test files or create new ones following the project's conventions. Do not write tests for uncovered lines in files that were not touched by this branch.

Fix lint issues:

Auto-detect the project type by checking for configuration files:

package.json (Node.js/JS/TS)
pyproject.toml, setup.py, requirements.txt (Python)
Cargo.toml (Rust)
go.mod (Go)

Use the auto-fix command when available:

Node.js/JS/TS:
Check package.json scripts for a lint:fix script. If found, run npm run lint:fix
Otherwise, check for ESLint and run npx eslint . --fix
Check for Prettier and run npx prettier --write .
Python:
Check for ruff and run ruff check --fix . then ruff format .
Or check for black and run black .
Or check for autopep8 and run autopep8 --in-place --recursive .
Rust:
Run cargo fmt and cargo clippy --fix --allow-dirty
Go:
Run gofmt -w . and go vet ./...

Record any remaining lint issues that could not be auto-fixed

Run auditing and fix issues:

Node.js: Run npm audit. If vulnerabilities are found, run npm audit fix. If that is not enough, note remaining issues but do NOT run npm audit fix --force automatically
Python: Run pip audit if available. Note any vulnerabilities found
Rust: Run cargo audit if available. Note any vulnerabilities found
Go: Run govulncheck ./... if available. Note any vulnerabilities found
Record any audit issues that could not be auto-fixed

Present proposed fixes and improvements:

Display a full summary of everything that was done and found. Then use the AskUserQuestion tool with multiSelect: true to let the developer choose which fixes and improvements to apply. The developer is NOT choosing which of their own changes to commit — they are choosing which of the agent's proposed fixes/improvements to accept.

Group the items by category:

Lint fixes applied — files auto-formatted by the linter
Coverage fixes — new or updated test files written to reach 100% coverage
Audit fixes applied — dependency changes from audit fix
Test quality issues — issues found by verify-test-cases (with proposed corrections)
Unfixable issues — anything that could not be auto-fixed (for awareness only)

Example question format:

"Which fixes/improvements do you want to apply?"
Options:
- "Lint fixes: 5 files auto-formatted by ESLint"
- "Coverage: added tests for 3 uncovered files (85% → 100%)"
- "Audit fix: updated lodash 4.17.20 → 4.17.21"
- "Test quality: fixed 2 incorrect test descriptions"


If there are more items than fit in 4 options, group them logically (e.g., "All lint fixes (8 files)" as one option).

Apply selected fixes:

For fixes the developer approved: keep the changes
For fixes the developer rejected: revert those specific changes using git restore <file> or by undoing the edits
Stage all approved changes with git add

Handle edge cases:

If there are no uncommitted changes, inform the user and STOP
If no lint tools are detected, skip the lint step and note it in the summary
If no audit tools are detected, skip the audit step and note it in the summary
If no coverage tool is detected, skip the coverage step and note it in the summary
If the /verify-test-cases skill reports no test files modified, skip that section in the summary
If all checks pass with no fixes needed, skip the approval step and go straight to the commit options
If the developer rejects all fixes, commit the developer's original changes only (no fixes)

Example output format:

## Cleanup Summary

### Changes Reviewed
- 3 files modified, 1 file added
- New feature: user profile endpoint
- Bug fix: corrected date parsing in utils

### Lint
✅ 5 files auto-fixed by ESLint
⚠️ 1 issue could not be auto-fixed:
  - src/api.ts:42 — Unexpected any. Specify a different type.

### Test Verification
✅ All test cases verified — no issues found

### Coverage (from single run)
⚠️ Coverage at 87% — missing coverage in:
  - src/services/auth.ts (lines 45-62)
  - src/utils/parser.ts (lines 12-18)
✅ Wrote 2 new test files to cover missing lines

### Audit
✅ npm audit fix applied — resolved 2 vulnerabilities
⚠️ 1 moderate vulnerability remains (no auto-fix available)

---

[Approval checklist: developer picks which fixes to keep]

---

✅ Committed: "Add user profile endpoint, fix date parsing, and improve test coverage"

Weekly Installs
65
Repository
morphet81/cheat-sheets
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
---
title: test-fixing
url: https://skills.sh/sickn33/antigravity-awesome-skills/test-fixing
---

# test-fixing

skills/sickn33/antigravity-awesome-skills/test-fixing
test-fixing
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill test-fixing
Summary

Systematically identify and fix all failing tests using smart error grouping.

Groups failures by error type, affected module, and root cause, then prioritizes fixes by impact and dependency order
Fixes infrastructure issues first (imports, dependencies, configuration), followed by API changes, then logic bugs
Runs focused test subsets after each fix using pytest markers and file patterns to verify progress before moving to the next group
Follows a structured workflow: initial test run, error analysis, grouped fixing with verification, and final full-suite validation
SKILL.md
Test Fixing

Systematically identify and fix all failing tests using smart grouping strategies.

When to Use
Explicitly asks to fix tests ("fix these tests", "make tests pass")
Reports test failures ("tests are failing", "test suite is broken")
Completes implementation and wants tests passing
Mentions CI/CD failures due to tests
Systematic Approach
1. Initial Test Run

Run make test to identify all failing tests.

Analyze output for:

Total number of failures
Error types and patterns
Affected modules/files
2. Smart Error Grouping

Group similar failures by:

Error type: ImportError, AttributeError, AssertionError, etc.
Module/file: Same file causing multiple test failure
Root cause: Missing dependencies, API changes, refactoring impacts

Prioritize groups by:

Number of affected tests (highest impact first)
Dependency order (fix infrastructure before functionality)
3. Systematic Fixing Process

For each group (starting with highest impact):

Identify root cause

Read relevant code
Check recent changes with git diff
Understand the error pattern

Implement fix

Use Edit tool for code changes
Follow project conventions (see CLAUDE.md)
Make minimal, focused changes

Verify fix

Run subset of tests for this group
Use pytest markers or file patterns:
uv run pytest tests/path/to/test_file.py -v
uv run pytest -k "pattern" -v

Ensure group passes before moving on

Move to next group

4. Fix Order Strategy

Infrastructure first:

Import errors
Missing dependencies
Configuration issues

Then API changes:

Function signature changes
Module reorganization
Renamed variables/functions

Finally, logic issues:

Assertion failures
Business logic bugs
Edge case handling
5. Final Verification

After all groups fixed:

Run complete test suite: make test
Verify no regressions
Check test coverage remains intact
Best Practices
Fix one group at a time
Run focused tests after each fix
Use git diff to understand recent changes
Look for patterns in failures
Don't move to next group until current passes
Keep changes minimal and focused
Example Workflow

User: "The tests are failing after my refactor"

Run make test → 15 failures identified
Group errors:
8 ImportErrors (module renamed)
5 AttributeErrors (function signature changed)
2 AssertionErrors (logic bugs)
Fix ImportErrors first → Run subset → Verify
Fix AttributeErrors → Run subset → Verify
Fix AssertionErrors → Run subset → Verify
Run full suite → All pass ✓
Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
460
Repository
sickn33/antigra…e-skills
GitHub Stars
36.0K
First Seen
Jan 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
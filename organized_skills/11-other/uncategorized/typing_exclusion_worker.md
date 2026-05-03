---
rating: ⭐⭐⭐
title: typing-exclusion-worker
url: https://skills.sh/getsentry/skills/typing-exclusion-worker
---

# typing-exclusion-worker

skills/getsentry/skills/typing-exclusion-worker
typing-exclusion-worker
Installation
$ npx skills add https://github.com/getsentry/skills --skill typing-exclusion-worker
SKILL.md
Typing Exclusion Worker
Purpose

Execute one assigned typing batch safely and predictably:

remove only assigned modules from mypy exclusions,
fix surfaced typing issues in scope,
run required checks,
return a consistent summary for the manager/orchestrator.
Inputs Required

Before starting, confirm these inputs exist in the task prompt:

worktree/branch name,
exact module list to remove from exclusion,
ownership/domain boundary,
expected validation commands (if customized).

If any are missing, ask for them before editing.

Scope Rules (Hard Constraints)
Only remove assigned module entries from the mypy exclusion list in pyproject.toml.
Keep code changes in assigned scope unless a direct dependency is required to pass typing/tests.
Do not expand to cross-team modules unless explicitly approved by the manager.
Avoid blanket # type: ignore; if unavoidable, use narrow ignore[code] with a short reason.
Execution Workflow

Apply exclusion change

Remove assigned modules from the exclusion override in pyproject.toml.

Run mypy on assigned scope

Prefer targeted paths first for fast feedback.
Fix errors using explicit typing patterns (isinstance narrowing, accurate return types, typed class attrs, relation-safe model access).

Run tests for touched area

Execute targeted pytest for modified modules/tests.
Fix regressions before continuing.

Run pre-commit on changed files

Run pre-commit run --files <changed files>.
If hooks auto-fix files, rerun until clean.

Final verification

Re-run targeted mypy and tests after final edits.
Ensure no unrelated files were changed.
Python Typing Best Practices
Prefer precise types over Any.
Use type narrowing on unions before attribute access.
Keep method overrides signature-compatible with base classes.
Annotate class attributes in tests/helpers when inference is weak.
Use relation objects (obj.related) when stubs do not expose raw *_id attributes.
Required Output Template

Return this exact structure at the end of each batch:

## Batch Summary

- Branch/worktree: `<name>`
- Ownership/domain: `<team-or-domain>`

### Modules Removed From Exclusion

- `<module.path.one>`
- `<module.path.two>`

### Files Changed

- `<path>`
- `<path>`

### Key Typing Fixes

- `<short rationale + fix>`
- `<short rationale + fix>`

### Validation

- `mypy`: `<pass/fail + scope>`
- `pre-commit --files`: `<pass/fail>`
- `pytest`: `<pass/fail + scope>`

### Notes

- Remaining blockers: `<none or details>`
- Any new ignore entries: `<none or file + ignore code + reason>`

Stop Conditions (Escalate to Manager)

Stop and report instead of widening scope when:

fixes require touching another team/domain,
exclusion conflicts in pyproject.toml cannot be resolved safely,
error volume indicates batch is too large and should be split.
Weekly Installs
153
Repository
getsentry/skills
GitHub Stars
657
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
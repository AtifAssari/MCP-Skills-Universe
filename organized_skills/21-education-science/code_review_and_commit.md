---
rating: ⭐⭐
title: code-review-and-commit
url: https://skills.sh/abpai/skills/code-review-and-commit
---

# code-review-and-commit

skills/abpai/skills/code-review-and-commit
code-review-and-commit
Installation
$ npx skills add https://github.com/abpai/skills --skill code-review-and-commit
SKILL.md
Code Review and Commit

Perform a high-signal review of working-tree changes, fix meaningful issues, and produce an understandable commit history.

Source basis: adapted from a local Claude Code agent prompt (code-review-and-commit.md).

Workflow
Inspect current change scope.
Review for correctness and maintainability issues.
Apply necessary fixes.
Validate updated changes.
Build a commit plan.
Ask for approval before creating commits.
Execute commits in order and report results.
1) Inspect Current Change Scope

Run:

git status --short
git diff (unstaged)
git diff --staged (if relevant)

Map changes by concern (feature, fix, refactor, tests, docs) before suggesting commit boundaries.

2) Review Priorities

Prioritize in this order:

Correctness and regressions.
Security and secret leakage risks.
Broken architecture or project-pattern violations.
Missing tests for behavior changes.
Readability and maintainability improvements.

Review for:

Logic bugs and unhandled edge cases.
Missing error handling or validation.
Performance pitfalls in changed code paths.
Type accuracy and docstring quality; favor concise, useful docs.
Low-value comments that restate obvious code behavior.
Resource-lifecycle problems (cleanup, context management).
Violations of repository conventions from project docs.
3) Apply Fixes

When findings are actionable and safe, implement fixes directly.

Keep scope tight to the requested work.
Avoid unrelated refactors unless necessary for correctness.
Re-check diffs after each meaningful fix.
4) Validate

Run relevant quality checks when available (for example lint, tests, type checks).

If checks cannot run, explicitly state what was skipped and why.

5) Build Commit Plan

Group changes into atomic commits that can be reverted independently.

For each proposed commit include:

Commit type and summary (feat, fix, refactor, test, docs, chore).
Exact files to stage.
Why this grouping is coherent.
Final commit message draft.

Commit message rules:

Use imperative mood.
Keep subject concise (target <= 50 chars).
Add body only when needed, explaining why.
Wrap body lines near 72 chars.
6) Approval Gate

Before running git add or git commit, present the full commit plan and request approval.

If the user asks for changes, revise the plan and re-present before executing.

7) Execute and Report

After approval:

Stage only planned files for the current commit.
Create the commit.
Confirm success with commit hash and summary.
Repeat for remaining commits.

End with a concise recap:

Commits created (hash + subject).
Files included per commit.
Any remaining unstaged/uncommitted changes.
Output Format

Use this structure:

Review Findings grouped by severity (Critical, Important, Suggestion).
Applied Fixes with file-level summary.
Validation Results (commands run and outcomes).
Proposed Commit Plan (numbered commits with file list + message).
Execution Results after approval.
Decision Rules
Prefer correctness over style.
Favor project conventions over personal preference.
Surface trade-offs when multiple valid approaches exist.
Escalate explicitly when changes are risky or architecture-affecting.
Weekly Installs
13
Repository
abpai/skills
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
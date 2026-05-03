---
title: review-pr
url: https://skills.sh/linuxhsj/openclaw-zero-token/review-pr
---

# review-pr

skills/linuxhsj/openclaw-zero-token/review-pr
review-pr
Installation
$ npx skills add https://github.com/linuxhsj/openclaw-zero-token --skill review-pr
SKILL.md
Review PR
Overview

Perform a read-only review and produce both human and machine-readable outputs.

Inputs
Ask for PR number or URL.
If missing, always ask.
Safety
Never push, merge, or modify code intended to keep.
Work only in .worktrees/pr-<PR>.
Wrapper commands are cwd-agnostic; you can run them from repo root or inside the PR worktree.
Execution Contract
Run wrapper setup:
scripts/pr-review <PR>

Use explicit branch mode switches:
Main baseline mode: scripts/pr review-checkout-main <PR>
PR-head mode: scripts/pr review-checkout-pr <PR>
Before writing review outputs, run branch guard:
scripts/pr review-guard <PR>

Write both outputs:
.local/review.md with sections A through J.
.local/review.json with structured findings.
Validate artifacts semantically:
scripts/pr review-validate-artifacts <PR>

Steps
Setup and metadata
scripts/pr-review <PR>
ls -la .local/pr-meta.json .local/pr-meta.env .local/review-context.env .local/review-mode.env

Existing implementation check on main
scripts/pr review-checkout-main <PR>
rg -n "<keyword>" -S src extensions apps || true
git log --oneline --all --grep "<keyword>" | head -20

Claim PR
gh_user=$(gh api user --jq .login)
gh pr edit <PR> --add-assignee "$gh_user" || echo "Could not assign reviewer, continuing"

Read PR description and diff
scripts/pr review-checkout-pr <PR>
gh pr diff <PR>

source .local/review-context.env
git diff --stat "$MERGE_BASE"..pr-<PR>
git diff "$MERGE_BASE"..pr-<PR>

Optional local tests

Use the wrapper for target validation and executed-test verification:

scripts/pr review-tests <PR> <test-file> [<test-file> ...]

Initialize review artifact templates
scripts/pr review-artifacts-init <PR>

Produce review outputs
Fill .local/review.md sections A through J.
Fill .local/review.json.

Minimum JSON shape:

{
  "recommendation": "READY FOR /prepare-pr",
  "findings": [
    {
      "id": "F1",
      "severity": "IMPORTANT",
      "title": "...",
      "area": "path/or/component",
      "fix": "Actionable fix"
    }
  ],
  "tests": {
    "ran": [],
    "gaps": [],
    "result": "pass"
  },
  "docs": "up_to_date|missing|not_applicable",
  "changelog": "required"
}

Guard + validate before final output
scripts/pr review-guard <PR>
scripts/pr review-validate-artifacts <PR>

Guardrails
Keep review read-only.
Do not delete worktree.
Use merge-base scoped diff for local context to avoid stale branch drift.
Weekly Installs
10
Repository
linuxhsj/opencl…ro-token
GitHub Stars
4.7K
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn
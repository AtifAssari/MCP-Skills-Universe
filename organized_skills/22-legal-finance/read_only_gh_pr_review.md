---
rating: ⭐⭐
title: read-only-gh-pr-review
url: https://skills.sh/jawwadfirdousi/agent-skills/read-only-gh-pr-review
---

# read-only-gh-pr-review

skills/jawwadfirdousi/agent-skills/read-only-gh-pr-review
read-only-gh-pr-review
Installation
$ npx skills add https://github.com/jawwadfirdousi/agent-skills --skill read-only-gh-pr-review
SKILL.md
PR Review (Backend, GitHub CLI)
Overview

Review backend pull requests end-to-end using local code analysis and GitHub CLI API calls. Report only actionable, high-signal findings.

Tool Constraints
Use only: SemanticSearch, WebSearch, Grep, LS, Glob, Read, Shell, GitHub CLI.
Before any gh command, source the read-only environment script to enable security enforcement:
source "<SKILL_DIR>/scripts/activate-gh-readonly.sh"

Replace <SKILL_DIR> with the absolute path to this skill directory.
After sourcing, use gh commands directly—they are intercepted by the read-only wrapper.
Verify CLI auth first with gh auth status. If not authenticated, ask the user to run gh auth login.
Enforce strict read-only mode at all times.
Never attempt any write operation, including comments, reviews, edits, assignments, merges, closes, reopens, or API mutations.
If a requested command is blocked by the wrapper, do not try alternatives that can mutate state.
The read-only wrapper blocks command gh and other bypass attempts.
Workflow
Enable read-only environment.
Source the environment script: source "<SKILL_DIR>/scripts/activate-gh-readonly.sh"
All subsequent gh commands in this shell session are now protected.
Prepare review context.
Confirm identity and auth: gh auth status, gh api user.
Resolve repository owner/name from the current repo or pass -R <OWNER>/<REPO>.
Resolve the target PR.
Use gh pr view <PR_NUMBER> [--json <fields>] when PR number is known.
Otherwise shortlist with gh pr list [flags] and pick the target PR.
Sync local repository to the latest PR branch code.
Fetch the latest remote state for the PR head branch before reviewing code.
Example flow:
Get head branch name from PR metadata (headRefName).
Run git fetch --prune origin <HEAD_BRANCH>.
Review files from FETCH_HEAD or check out a local review branch from it.
Gather full PR evidence before judging.
Metadata: gh pr view <PR_NUMBER> [--json <fields>]
Diff: gh pr diff <PR_NUMBER> [--patch|--name-only]
Changed files: gh api repos/<OWNER>/<REPO>/pulls/<PR_NUMBER>/files --paginate
Reviews: gh api repos/<OWNER>/<REPO>/pulls/<PR_NUMBER>/reviews --paginate
Checks: gh pr checks <PR_NUMBER> [--json <fields>]
Comments:
gh pr view <PR_NUMBER> --comments
gh api repos/<OWNER>/<REPO>/issues/<PR_NUMBER>/comments --paginate
gh api repos/<OWNER>/<REPO>/pulls/<PR_NUMBER>/comments --paginate
Inspect changed backend code deeply.
Read all high-risk touched files locally (Read, Grep) and correlate with diff hunks.
Prioritize request handlers/controllers, business services, authorization logic, database queries, migrations, background jobs, and queue/event handlers.
Verify idempotency, transaction safety, concurrency behavior, retry behavior, and backward compatibility for public API contracts.
Use gh api repos/<OWNER>/<REPO>/contents/<PATH>?ref=<REF> when exact remote content is needed (content is usually base64 in .content).
Apply review checklist with risk-first ordering.
Use references/review-checklist.md.
Cover security, correctness, data integrity, API compatibility, performance, and test sufficiency before style concerns.
Produce actionable review output.
Report only issues that are likely defects, regressions, or maintainability risks.
Include exact file:line, impact, and concrete fix guidance.
End with residual risk and missing validation/testing assumptions.
Return findings in chat only; do not write any comment or review back to GitHub.
Response Format

Use this section order:

Critical Issues (Must Fix)
Important Issues (Should Fix)
Suggestions (Consider)
Good Practices Noted

For each issue, use:

Issue: <brief description>
Location: <file:line>
Severity: <Critical|High|Medium|Low>
Problematic Code: <snippet or precise behavior>
Suggestion: <specific fix>
Example: <optional patch-style snippet>

GitHub CLI API Equivalents

Use command mappings in references/github-cli-map.md.

Review Tone
Be constructive and specific.
Explain impact and rationale.
Assume positive intent.
Prefer concise, high-confidence feedback.
Weekly Installs
21
Repository
jawwadfirdousi/…t-skills
GitHub Stars
10
First Seen
Feb 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketFail
SnykWarn
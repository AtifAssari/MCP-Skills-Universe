---
rating: ⭐⭐⭐
title: pr-review-fixer
url: https://skills.sh/arjenschwarz/agentic-coding/pr-review-fixer
---

# pr-review-fixer

skills/arjenschwarz/agentic-coding/pr-review-fixer
pr-review-fixer
Installation
$ npx skills add https://github.com/arjenschwarz/agentic-coding --skill pr-review-fixer
SKILL.md
PR Review Fixer

Fetch unresolved PR comments, validate each issue, create a fix plan, implement fixes, and verify CI checks pass (tests, lint, build).

Workflow
1. Fetch PR Comments
# Get PR info
PR_NUM=$(gh pr view --json number --jq '.number')

# Get all PR comments via GraphQL (code-level AND PR-level)
gh api graphql -f query='
  query($owner: String!, $repo: String!, $pr: Int!) {
    repository(owner: $owner, name: $repo) {
      pullRequest(number: $pr) {
        # Code-level review comments (file/line specific)
        reviewThreads(first: 100) {
          nodes {
            id
            isResolved
            comments(first: 50) {
              nodes { id body author { login } path line }
            }
          }
        }
        # PR-level review comments (top-level review body)
        reviews(first: 50) {
          nodes {
            id
            body
            state
            author { login }
          }
        }
        # PR-level issue comments (general discussion)
        comments(first: 100) {
          nodes {
            id
            body
            author { login }
          }
        }
      }
    }
  }
' -f owner=OWNER -f repo=REPO -F pr=$PR_NUM

2. Filter Comments

Code-level comments (reviewThreads):

Exclude resolved threads: Filter out threads where isResolved: true
claude[bot] handling: For claude[bot] comments, keep only the last comment per thread
Group by file/location: Organize by path and line number

PR-level review comments (reviews):

Exclude empty bodies: Skip reviews with empty or whitespace-only body
Exclude approval-only: Skip reviews with state APPROVED and no actionable feedback
claude[bot] handling: For claude[bot] reviews, keep only the most recent one

PR-level issue comments (comments):

Exclude bot noise: Skip automated comments (CI bots, etc.) unless actionable
claude[bot] handling: Keep only the last claude[bot] comment
Identify actionable items: Look for requested changes, questions, or suggestions
3. Determine Working Location

Review reports are posted as PR comments (not committed). Task files are local working files only.

Working directory: Use a temp directory or .claude/reviews/PR-[number]/ for local task files during the session. These files are not committed.

Iteration tracking: Check existing PR comments by claude[bot] with "PR Review Overview" in the body. Count those to determine the current iteration number N.

4. Validate Issues

Code-level comments:

Read the referenced code at path:line
Evaluate: Is issue still present? Is suggestion correct? Does it align with project conventions?
Mark as valid or invalid with brief rationale

PR-level comments:

Parse the comment for actionable items (suggestions, questions, requested changes)
Check if the feedback applies to current PR state (changes may have been made since)
Evaluate: Is the request reasonable? Does it align with project goals?
Mark as valid or invalid with brief rationale
Skip pure acknowledgments, thanks, or informational comments without action items
5. Create Review Overview

Prepare the review overview content (this will be posted as a PR comment, not committed):

# PR Review Overview - Iteration [N]

**PR**: #[number] | **Branch**: [name] | **Date**: [YYYY-MM-DD]

## Valid Issues

### Code-Level Issues

#### Issue 1: [title]
- **File**: `path:line`
- **Reviewer**: @user
- **Comment**: [quoted]
- **Validation**: [rationale]

### PR-Level Issues

#### Issue 2: [title]
- **Type**: review comment | discussion comment
- **Reviewer**: @user
- **Comment**: [quoted]
- **Validation**: [rationale]

## Invalid/Skipped Issues

### Issue A: [title]
- **Location**: `path:line` or PR-level
- **Reviewer**: @user
- **Comment**: [quoted]
- **Reason**: [why invalid]

6. Create Task List

Use rune to create review-fixes-[N].md:

rune create ${OUTPUT_DIR}/review-fixes-${N}.md \
  --title "PR Review Fixes - Iteration ${N}" \
  --reference ${OUTPUT_DIR}/review-overview-${N}.md

# Add tasks via batch for efficiency
rune batch ${OUTPUT_DIR}/review-fixes-${N}.md --input '{
  "file": "review-fixes-'${N}'.md",
  "operations": [
    {"type": "add", "title": "Fix: [issue 1]"},
    {"type": "add", "title": "Fix: [issue 2]"}
  ]
}'

7. Fix Issues

Loop through tasks:

rune next [file] - get next task
rune progress [file] [id] - mark in-progress
Implement the fix
rune complete [file] [id] - mark complete
Repeat until done
8. Check CI Status

After fixing review comments, verify CI checks:

# Get check status for the PR
gh pr checks --json name,state,conclusion

# For failed checks, get details
gh run view [RUN_ID] --log-failed


Check types to handle:

Test failures: Parse test output, identify failing tests, fix code or tests
Lint errors: Run linter locally, fix reported issues
Type errors: Run type checker, fix type mismatches
Build failures: Check build logs, fix compilation issues
9. Fix CI Issues

For each failed check:

Identify the failure type from check name and logs
Run locally to reproduce:
Tests: make test or project's test command
Lint: make lint or project's lint command
Types: make typecheck or equivalent
Parse error output to identify specific failures
Fix the issues:
For test failures: Check if test expectations need updating or if code has a bug
For lint errors: Apply automatic fixes where possible, manual fixes otherwise
For type errors: Add/fix type annotations or fix type mismatches
Re-run locally to verify fix
Add to task list if not already tracked

Test failure handling:

# Run tests and capture output
make test 2>&1 | tee test-output.txt

# If using pytest
pytest --tb=short 2>&1 | tee test-output.txt

# If using go test
go test ./... 2>&1 | tee test-output.txt


Parse output for:

Failed test names and locations
Assertion errors with expected vs actual values
Stack traces pointing to failure source
10. Resolve Fixed Threads

After fixing code-level issues, resolve the corresponding review threads on GitHub:

# For each fixed code-level thread, resolve it using its thread ID
gh api graphql -f query='
  mutation($threadId: ID!) {
    resolveReviewThread(input: {threadId: $threadId}) {
      thread { isResolved }
    }
  }
' -f threadId=THREAD_NODE_ID


Only resolve threads whose issues were validated and fixed. Do not resolve threads that were skipped or marked invalid — those need human attention.

11. Post Review Report as PR Comment

Post the review overview as a comment on the PR. This replaces committing report files.

# Post the review overview content as a PR comment
gh pr comment $PR_NUM --body "$(cat <<'EOF'
# PR Review Overview - Iteration [N]

**PR**: #[number] | **Branch**: [name] | **Date**: [YYYY-MM-DD]

## Valid Issues (fixed)

[List of validated and fixed issues with file:line, reviewer, and brief description]

## Invalid/Skipped Issues

[List of skipped issues with rationale]

## CI Status

[Summary of CI check results and any fixes applied]
EOF
)"


Do not commit review-overview-*.md or review-fixes-*.md files. They are working files only.

12. Commit, Push, and Verify

After all fixes:

Run full test suite locally
Run linter
Commit only code changes (exclude any local review/task files)
Push to remote
Monitor CI status to confirm checks pass
Key Behaviors
Auto-fix: Fix all validated issues without pausing for approval
Context preservation: Keep diff_hunk context when analyzing
Convention adherence: Follow project's existing patterns
Deduplication: Consolidate multiple comments on same issue into one task
CI verification: Always check CI status after fixing review comments
Local reproduction: Run tests/linters locally before pushing fixes
Reports as comments: Post review reports as PR comments, never commit them
Clean commits: Only commit actual code changes, not working/report files
Weekly Installs
16
Repository
arjenschwarz/ag…c-coding
GitHub Stars
18
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
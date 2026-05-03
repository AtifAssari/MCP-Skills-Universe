---
title: arinhub-verify-requirements-coverage
url: https://skills.sh/arinhubcom/arinhub/arinhub-verify-requirements-coverage
---

# arinhub-verify-requirements-coverage

skills/arinhubcom/arinhub/arinhub-verify-requirements-coverage
arinhub-verify-requirements-coverage
Installation
$ npx skills add https://github.com/arinhubcom/arinhub --skill arinhub-verify-requirements-coverage
SKILL.md
Verify Requirements Coverage

Verify that a pull request or local changes fully implement the requirements described in a GitHub issue. Extracts the issue reference, analyzes the diff against the issue description, and produces a coverage report.

Input
PR number or URL (optional): The pull request identifier. Accepts:
Number: 123
Hash-prefixed: #123
Full URL: https://github.com/owner/repo/pull/123
If omitted, verifies local changes instead.
Issue number (optional, local mode): When verifying local changes, an issue number can be provided to check coverage against (e.g., issue #42).
Diff file path (optional): Path to a pre-existing diff file (e.g., passed by arinhub-code-reviewer). If provided, skip fetching the diff in Step 7 and read this file instead.
Procedure
1. Determine Review Target
Remote PR: If the user provides a PR number or URL (e.g., "Verify PR #123"), target that remote PR. Set MODE=remote.
Local Changes: If no specific PR is mentioned, or if the user asks to "verify my changes" or "do my changes cover the issue", target the current local changes (staged and unstaged). Set MODE=local.
2. Resolve Identifier

If MODE=remote:

Extract the PR number from the user input. Strip any # prefix or parse the number from a URL.

PR_NUMBER=<extracted number>


If MODE=local:

Determine the current branch name and base branch for identification and diffing.

BRANCH_NAME=$(git branch --show-current | tr '/' '-')

# Determine the base (source) branch using this priority:
# 1. If an open/draft PR exists for the current branch, use its base branch.
# 2. Fall back to the repository's default branch.
# 3. Last resort: "main".
BASE_BRANCH=$(gh pr view --json baseRefName -q '.baseRefName' 2>/dev/null || gh repo view --json defaultBranchRef -q '.defaultBranchRef.name' 2>/dev/null || git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|refs/remotes/origin/||')
BASE_BRANCH=${BASE_BRANCH:-main}

# Find the point where the current branch diverged from the base branch.
MERGE_BASE=$(git merge-base "${BASE_BRANCH}" HEAD)

3. Fetch Metadata

If MODE=remote:

Gather PR details including body and linked issues:

gh pr view $PR_NUMBER --json number,title,body,baseRefName,headRefName,files,url


If MODE=local:

Gather the list of changed files on the branch (committed and uncommitted) relative to the base branch:

git diff --name-only "${MERGE_BASE}"

4. Extract Linked Issue Number

If MODE=remote:

Determine the related issue using these methods in priority order:

Method A -- Closing keywords in PR body:

Search the PR body for GitHub closing keywords followed by an issue reference:

closes #N, fixes #N, resolves #N (and their variants: close, closed, fix, fixed, resolve, resolved)
Full URL references: closes https://github.com/owner/repo/issues/N

Method B -- GitHub linked issues API:

gh api graphql \
  -F owner='{owner}' \
  -F repo='{repo}' \
  -F pr_number=$PR_NUMBER \
  -f query='
    query($owner: String!, $repo: String!, $pr_number: Int!) {
      repository(owner: $owner, name: $repo) {
        pullRequest(number: $pr_number) {
          closingIssuesReferences(first: 10) {
            nodes { number title }
          }
        }
      }
    }
  ' --jq '.data.repository.pullRequest.closingIssuesReferences.nodes'


Method C -- Issue reference in PR body:

If Methods A and B yield no results, scan the PR body for any #N pattern or issue URL that is not a closing keyword reference.

If MODE=local:

Determine the related issue using these methods in priority order:

Method A -- User-provided issue number: If the user explicitly provided an issue number (e.g., "verify my changes against issue #42"), use that directly.

Method B -- Branch name convention: Extract an issue number from the branch name if it follows a convention like feature/42-description, fix/42, issue-42-description, 42-description, jj/42-description, etc.

No issue found: If no linked issue can be determined, inform the user and stop. Do not guess or fabricate an issue number.

ISSUE_NUMBER=<extracted number>


If multiple issues are found, process each one and produce a separate coverage report per issue.

5. Fetch Issue Details

Retrieve the full issue description:

gh issue view $ISSUE_NUMBER --json number,title,body,labels

6. Extract Requirements from Issue

Parse the issue body and title to identify discrete, testable requirements. Look for:

Checklist items (- [ ] or - [x])
Numbered steps or acceptance criteria
Explicit behavioral descriptions ("should", "must", "when X then Y")
UI changes, API changes, or data model changes mentioned
Edge cases or error handling requirements
Non-functional requirements (performance, security, accessibility)

Produce a numbered list of requirements:

R1: <requirement description>
R2: <requirement description>
...


If the issue body is vague or contains no clear requirements, use the issue title and any available context to infer the expected behavior. Flag inferred requirements clearly.

7. Fetch Diff

If a diff file path was provided as input, read the diff from that file instead of fetching it. Skip the commands below and proceed to Step 8.

If MODE=remote:

Get the full diff for the pull request:

gh pr diff $PR_NUMBER


Also review the list of changed files from Step 3 to understand the scope of changes.

If MODE=local:

Diff from the merge base (resolved in Step 2) to the current working tree. This captures all changes on the feature branch — both committed and uncommitted — relative to the base branch.

git diff "${MERGE_BASE}"


Also review the list of changed files from Step 3 to understand the scope of changes.

8. Analyze Coverage

For each requirement from Step 6, determine whether the diff addresses it:

Covered: The diff contains code changes that directly implement the requirement
Partially covered: The diff addresses some aspects but misses edge cases or details
Not covered: No code changes in the diff relate to this requirement

Use evidence from the diff to justify each assessment. Do not speculate -- base judgments on actual code changes.

9. Produce Report

Generate one of two outputs based on the analysis.

If all requirements are covered (100% coverage):

MODE=remote:

## PR Requirements Coverage: 100%

All requirements from issue #<ISSUE_NUMBER> are implemented in PR #<PR_NUMBER>.

### Requirements
| # | Requirement | Status |
|---|-------------|--------|
| R1 | <description> | Covered |
| R2 | <description> | Covered |

### Summary
<2-3 sentences confirming that the PR fully addresses the issue, highlighting key implementation decisions>


MODE=local:

## Local Requirements Coverage: 100%

All requirements from issue #<ISSUE_NUMBER> are implemented in local changes on branch ${BRANCH_NAME}.

### Requirements
| # | Requirement | Status |
|---|-------------|--------|
| R1 | <description> | Covered |
| R2 | <description> | Covered |

### Summary
<2-3 sentences confirming that the local changes fully address the issue, highlighting key implementation decisions>


If any requirements are missing or partially covered:

MODE=remote:

## PR Requirements Coverage: <percentage>%

PR #<PR_NUMBER> does not fully implement issue #<ISSUE_NUMBER>.

### Requirements
| # | Requirement | Status | Notes |
|---|-------------|--------|-------|
| R1 | <description> | Covered | |
| R2 | <description> | Not covered | <what is missing> |
| R3 | <description> | Partially covered | <what is incomplete> |

### Missing Implementation
<For each uncovered or partially covered requirement, describe specifically what code changes are needed to complete the implementation>

### Summary
<2-3 sentences describing the overall gap between the issue requirements and the PR implementation>


MODE=local:

## Local Requirements Coverage: <percentage>%

Local changes on branch ${BRANCH_NAME} do not fully implement issue #<ISSUE_NUMBER>.

### Requirements
| # | Requirement | Status | Notes |
|---|-------------|--------|-------|
| R1 | <description> | Covered | |
| R2 | <description> | Not covered | <what is missing> |
| R3 | <description> | Partially covered | <what is incomplete> |

### Missing Implementation
<For each uncovered or partially covered requirement, describe specifically what code changes are needed to complete the implementation>

### Summary
<2-3 sentences describing the overall gap between the issue requirements and the local changes>

10. Report to User

If MODE=remote:

Present the coverage report from Step 9. Include:

The issue number and title for context
The PR URL for reference
The coverage percentage
Clear next steps if coverage is incomplete

If MODE=local:

Present the coverage report from Step 9. Include:

The issue number and title for context
The branch name and list of changed files
The coverage percentage
Clear next steps if coverage is incomplete
Important Notes
Never fabricate requirements that are not present or implied in the issue
If the issue lacks acceptance criteria, clearly state which requirements were inferred from context
Do not evaluate code quality -- this skill only checks implementation completeness against the issue description
For issues with sub-tasks or linked child issues, only evaluate the requirements in the specific linked issue
When multiple issues are linked, report coverage for each issue separately
In MODE=local, the diff comes from git diff "${MERGE_BASE}" (all committed and uncommitted changes on the branch relative to the base branch) instead of a PR diff. The issue must be provided by the user or extracted from the branch name — if neither yields a result, inform the user and stop
Weekly Installs
12
Repository
arinhubcom/arinhub
First Seen
Feb 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
---
rating: ⭐⭐⭐
title: ah-create-pr
url: https://skills.sh/arinhubcom/arinhub/ah-create-pr
---

# ah-create-pr

skills/arinhubcom/arinhub/ah-create-pr
ah-create-pr
Installation
$ npx skills add https://github.com/arinhubcom/arinhub --skill ah-create-pr
SKILL.md
Create or Update GitHub Pull Request

Analyze the current branch and create or update a well-structured GitHub Pull Request. If an open PR already exists for the current branch, it is updated instead of creating a duplicate. The diff against the base branch is the single source of truth for all PR content.

Input
Base branch (REQUIRED): The target branch this PR will merge into (e.g., main, develop). If the user did not provide it, STOP and ask before proceeding. Never assume or default to any branch.
Issue number (optional): The GitHub issue number this PR addresses (e.g., 42, #42). If not provided by the user, do not attempt to infer it from the branch name -- simply omit issue references from the PR.
Labels (optional): Comma-separated list of labels to apply to the PR (e.g., bug,urgent, feature,frontend). If not provided by the user, auto-detect labels in step 2.
Current Git branch with unmerged commits
Git diff against the base branch
Procedure
0. Preparation

Verify GitHub CLI authentication and check for uncommitted changes before proceeding.

gh auth status

# Warn if there are uncommitted changes that won't be included in the PR
git status --porcelain


If gh auth status fails, stop and ask the user to authenticate with gh auth login. If there are uncommitted changes (staged or unstaged), warn the user that these changes will not be included in the PR and ask whether to continue or wait.

Run quality checks to catch issues before creating the PR. If any check fails, report the failure and ask the user how to proceed.

pnpm preflight
pnpm preflight:build


Also compare .env* files in the repo root: identify missing keys across them and flag any security risks or naming inconsistencies.

1. Gather Context

If the user did not provide a base branch, STOP and ask for it before proceeding.

BASE_BRANCH=<user-provided base branch>
CURRENT_BRANCH=$(git branch --show-current)

# Compute merge base for reliable diffing (works even if origin isn't fetched)
git fetch origin "${BASE_BRANCH}" --quiet
MERGE_BASE=$(git merge-base "origin/${BASE_BRANCH}" HEAD)

# Full diff against merge base (primary source of truth)
git diff "${MERGE_BASE}" --stat
DIFF=$(git diff "${MERGE_BASE}")

# Commit history on this branch
git log "${MERGE_BASE}"..HEAD --no-decorate

# Branch tracking status
git status -sb

# Check for existing open PR on this branch
EXISTING_PR_NUMBER=$(gh pr list --head "${CURRENT_BRANCH}" --state open --json number --jq '.[0].number')
EXISTING_PR_URL=$(gh pr list --head "${CURRENT_BRANCH}" --state open --json url --jq '.[0].url')
EXISTING_PR_BASE=$(gh pr list --head "${CURRENT_BRANCH}" --state open --json baseRefName --jq '.[0].baseRefName')


If an open PR already exists for the current branch, the skill will update it in Step 4 instead of creating a new one. If the existing PR targets a different base branch than the one the user provided, warn the user and ask how to proceed before continuing.

If the user provided an issue number, use it for the PR references. Do not infer issue numbers from the branch name or commit messages.

2. Analyze Changed Files
Categorize changes by functional area (features, components, API, config, tests, etc.).
Identify patterns -- look for related changes that form logical blocks (e.g., "Auth flow refactor", "Error handling improvements").
Validate scope -- verify all changes contribute to the same feature/fix. Flag unrelated changes that may need separate PRs.
Determine Labels

If the user provided labels, use them as-is. Otherwise, auto-detect labels by analyzing:

Fetch available labels from the repository:
gh label list --limit 100 --json name,description

Match labels based on the PR content:
PR title type -- map the commit type (feat, fix, refactor, docs, test, perf, chore) to matching labels (e.g., feat -> feature/enhancement, fix -> bug/bugfix, docs -> documentation)
Changed file paths -- infer domain labels from directories (e.g., changes in apps/app-name/ -> app-name, changes in src/api/ -> api/backend, changes in src/components/ -> frontend/ui, changes in infra/ -> infrastructure)
Diff content -- detect patterns like security fixes, dependency updates, breaking changes, and match to corresponding labels
Select only labels that exist in the repository. Never create or suggest labels that do not exist.
Limit to 1-4 labels -- pick the most relevant ones. Prefer specific labels over generic ones.
3. Generate PR Content

Read the PR body template from references/pr-body.md and follow its structure and rules exactly.

4. Create Pull Request

Title format: <type>: <brief description> -- keep under 70 characters.

Types: feat, fix, refactor, chore, test, docs, perf
For monorepos, prefix with app name: app-name/feat: description
Extract from the first commit if it already follows this format.

Draft mode: Create as draft if any of these apply:

TODOs identified in commit messages
Tests missing for new features
Scope seems too large (>20 files changed)

Push the branch to the remote if it has not been pushed yet or is behind:

git push -u origin ${CURRENT_BRANCH}

If an open PR already exists (EXISTING_PR_NUMBER is set)

Update the existing PR with the newly generated content:

gh pr edit ${EXISTING_PR_NUMBER} \
  --title "<type>: <brief description>" \
  --add-label "<label1>" --add-label "<label2>" \
  --body "$(cat <<'EOF'
<PR body from references/pr-body.md>
EOF
)"


Omit --add-label flags entirely if no labels were determined.

If no open PR exists

Create a new PR (include --label flags for each determined label):

gh pr create \
  --base "${BASE_BRANCH}" \
  --head "${CURRENT_BRANCH}" \
  --title "<type>: <brief description>" \
  --label "<label1>" --label "<label2>" \
  --body "$(cat <<'EOF'
<PR body from references/pr-body.md>
EOF
)"


Omit --label flags entirely if no labels were determined.

5. Report to User

After creating or updating the PR, provide:

PR URL -- direct link to the created or updated pull request
Status -- whether the PR was created or updated (existing PR detected)
Summary -- brief recap of what was included
Labels -- list the labels applied and briefly explain why each was chosen (or note that none were applicable)
Action Items -- any TODOs or follow-ups identified
Review Checklist -- quick reminders for self-review before requesting reviewers
Validation Checks

Before submitting the PR, verify:

All applicable sections are populated (Summary, Changes, Tests, and GH if an issue was provided)
No placeholder text like "TODO" or "TBD" remains (unless in explicit TODO checkboxes)
If an issue number was provided, closing keywords are correctly formatted
Changes align with branch name and commit messages
Test coverage is addressed (present or explicitly noted as TODO)
Error Handling
If no base branch was provided, STOP and ask the user for it
If no commits exist ahead of the base branch, abort and inform user
If diff is empty, check for unstaged changes and prompt user
If an existing open PR targets a different base branch than the user provided, warn the user and ask whether to update the existing PR's base or create a new PR
Best Practices
Atomic PRs: Warn if scope seems too broad (suggest splitting if >30 files or multiple unrelated features)
Conventional Commits: Use semantic versioning-friendly titles
Self-Review: Suggest the author review the generated content before requesting reviewers
Weekly Installs
9
Repository
arinhubcom/arinhub
First Seen
Mar 11, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass
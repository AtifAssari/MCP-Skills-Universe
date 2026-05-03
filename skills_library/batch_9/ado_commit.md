---
title: ado-commit
url: https://skills.sh/flora131/atomic/ado-commit
---

# ado-commit

skills/flora131/atomic/ado-commit
ado-commit
Installation
$ npx skills add https://github.com/flora131/atomic --skill ado-commit
SKILL.md
Contains Shell Commands

This skill contains shell command directives (!`command`) that may execute system commands. Review carefully before installing.

ADO Commit

Create a conventional commit on an Azure DevOps-hosted repository: $ARGUMENTS

Current state
Git status: !git status --porcelain
Current branch: !git branch --show-current
Staged diff (stat): !git diff --cached --stat
Unstaged diff (stat): !git diff --stat
Recent commits: !git log --oneline -5
Workflow

The only ADO-specific bits are (a) work-item trailers and (b) the conventions this repo has adopted for talking to reviewers who open PRs in Azure DevOps.

Stage. If nothing is staged, stage all modified and new files with git add -A. If specific files are already staged, commit only those.
Diff. Run git diff --cached to understand the actual change. Read the diff — don't just trust the path names — because the message needs to describe what changed and why, not which files changed.
Split if needed. If the staged diff contains multiple unrelated logical changes, propose splitting into separate commits. One commit = one reason to change.
Write the message in Conventional Commits format (see below), then commit via git commit --message "<subject>" [--trailer ...]. Pass trailers with --trailer so git formats them correctly; don't cat-heredoc them into the body.
Don't skip pre-commit hooks. If .pre-commit-config.yaml exists, hooks run automatically and their failures are signal, not noise. Never pass --no-verify.
Conventional Commits — quick reference
<type>(optional scope): <description>

<optional body>

<optional trailers>


Common types: feat, fix, docs, style, refactor, perf, test, build, ci, chore, revert. Append ! after type/scope for breaking changes (e.g. feat(api)!: change response format). Keep the subject under 72 characters, imperative mood, no trailing period.

Examples:

feat(auth): add JWT refresh endpoint
fix(ui): resolve layout shift on mobile nav
refactor(db): migrate from raw SQL to query builder
chore(deps): bump TypeScript to 5.5
feat(api)!: change pagination response shape

Work-item trailers (ADO-specific)

Azure DevOps auto-links commits to work items when the message contains AB#<id>. Include one whenever you can identify the target work item, because it keeps the board in sync without anyone clicking around.

Where to find the ID:

Branch name — patterns like feature/1234-..., bug/AB1234-..., user/name/1234-... usually encode the work item ID.
User input — if the user mentions "work item 1234" or "this closes 1234", use that.
Prior commits on the branch — run git log --oneline origin/main..HEAD and check if earlier commits reference an ID.
ADO MCP — if the project has the azure-devops MCP server configured and you're still unsure, call wit_my_work_items (or search_workitem with a keyword from the change) to surface likely candidates. Ask the user to confirm rather than guessing.

How to add it — as a trailer, not in the subject:

git commit \
  --message "feat(auth): add JWT refresh endpoint" \
  --trailer "AB#1234" \
  --trailer "Assistant-model: Claude Code"


If you genuinely can't find a work-item ID, skip the trailer rather than inventing one. A missing trailer is recoverable; a wrong one pollutes the board.

AI authorship trailer

ADO code reviews often surface in audit contexts, so mark AI-assisted commits honestly. Use an Assistant-model trailer rather than Co-authored-by — most git tooling validates the latter as an email, and we want to distinguish assistance from authorship:

Assistant-model: Claude Code


Add it every time you commit on the user's behalf.

Putting it together
git add -A
git diff --cached --stat          # sanity check
git commit \
  --message "fix(parser): handle nested escape sequences" \
  --trailer "AB#5678" \
  --trailer "Assistant-model: Claude Code"
git log -1                        # show the user the result

Weekly Installs
62
Repository
flora131/atomic
GitHub Stars
164
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
---
title: git-workflow
url: https://skills.sh/xbklairith/kisune/git-workflow
---

# git-workflow

skills/xbklairith/kisune/git-workflow
git-workflow
Installation
$ npx skills add https://github.com/xbklairith/kisune --skill git-workflow
SKILL.md
Git Workflow Skill
Purpose

Manage git operations with best practices, generating meaningful commit messages, managing branches safely, creating comprehensive pull requests, and preventing common git mistakes.

Activation Triggers

Activate this skill when:

User says "commit my changes"
User mentions "create a branch"
User asks to "create a PR" or "pull request"
User says "push to remote"
Before any destructive git operation
User mentions git or version control
Core Capabilities
1. Smart Commits

Goal: Generate meaningful, consistent commit messages that explain WHY changes were made

Process:

Analyze Changes — Run git status and git diff
Understand Intent — What was added/modified/removed? What problem does this solve?
Generate Commit Message using format: [type]: [concise description in present tense]

Commit Types:

feat - New feature
fix - Bug fix
refactor - Code restructuring without behavior change
test - Adding or updating tests
docs - Documentation changes
chore - Maintenance tasks (deps, config, etc.)
style - Code formatting (no logic change)
perf - Performance improvements

Message Guidelines:

Present tense, imperative mood ("Add" not "Added")
Focus on WHAT and WHY, not HOW
Under 72 characters for first line
No period at the end

Good examples:

feat: Add RSI indicator to market analysis
fix: Handle division by zero in position sizing
refactor: Extract strategy validation into separate function


Avoid: Vague messages ("updated files"), past tense ("Added new stuff"), or non-descriptive ("WIP", "asdfgh").

Show and Confirm — Present proposed message, list of files, and ask for approval
Execute and Verify — Stage files, commit, verify with git log -1 --oneline
2. Branch Management

Naming Convention: [type]/[description]

Type	Purpose	Example
feature/	New features	feature/user-authentication
fix/	Bug fixes	fix/login-timeout-error
refactor/	Code restructuring	refactor/payment-processing
experiment/	Experimental work	experiment/ml-price-prediction
hotfix/	Urgent production fixes	hotfix/security-vulnerability

Key Operations:

Create: git switch -c feature/name
Switch: git switch feature/name
List: git branch -v (or -a for remote)
Delete (safe): git branch -d feature/old
Delete remote: git push origin --delete feature/old

Safety: Before pushing to main/master, warn the user and recommend creating a feature branch with a PR instead.

3. Pull Request Creation

Process:

Analyze all commits: git log main..HEAD --oneline and git diff main...HEAD
Review changes — overall purpose, key changes, breaking changes, testing needs
Generate PR description using this template:
## Summary
[Brief overview of what this PR does and why]

## Changes
- [Key change 1]
- [Key change 2]

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed

## Code Quality
- [ ] Follows project style guidelines
- [ ] Self-review completed
- [ ] No debug code left
- [ ] Documentation updated

## Related Issues
Closes #[issue number]

Create PR: Use gh pr create --title "[Type]: Brief description" --body "..."
Return PR URL with next steps (request reviewers, monitor CI, address feedback)
4. Safety Checks

Pre-Commit:

No Secrets — Scan staged changes for api_key, secret, password, token. If found, warn and recommend .gitignore or environment variables. Abort by default.
Tests Pass — Run test suite. Block commit if tests fail.
Large Commit Warning — If 10+ files changed, suggest breaking into smaller commits.

Pre-Push:

Branch Check — If on main/master, warn and recommend feature branch + PR workflow.
Force Push Warning — If --force detected, issue critical warning about history rewriting, lost work, and broken PRs. Require explicit confirmation.

Pre-Merge:

Check for conflicts: git merge --no-commit --no-ff [branch] then git merge --abort
Verify CI status: gh pr checks
Confirm approvals: gh pr view --json reviews
Workflow Example: Preventing Dangerous Operations

User: "Push my changes to main"

Response:

Detect current branch is main
Warn about risks: no code review, potential production breakage, no CI gate
Recommend: create feature branch, push there, create PR, get review
Offer alternatives: (1) Create branch + PR, (2) Run tests then push, (3) Cancel
Integration Points
Works with review skill for pre-commit reviews
Works with spec-driven skill for commit messages during execution
Works with systematic-testing skill to verify tests before commit
Best Practices
Commit Often — Small, frequent commits over large, infrequent ones
One Concern Per Commit — Each commit represents one logical change
Write Good Messages — Future you will thank present you
Review Before Push — Always review your own changes first
Use Branches — Never work directly on main
Create PRs — Always use pull requests, even for solo projects
Keep History Clean — Meaningful commits, not "WIP" or "fix"
Notes
Always prioritize safety over convenience
Default to the safer option when in doubt
Prevent destructive operations with clear warnings
Make it easy to do the right thing
Weekly Installs
14
Repository
xbklairith/kisune
GitHub Stars
2
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
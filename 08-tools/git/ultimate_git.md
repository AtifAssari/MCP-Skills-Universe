---
title: ultimate-git
url: https://skills.sh/ezeqviel/skills/ultimate-git
---

# ultimate-git

skills/ezeqviel/skills/ultimate-git
ultimate-git
Installation
$ npx skills add https://github.com/ezeqviel/skills --skill ultimate-git
SKILL.md
Ultimate Git

Opinionated Git & GitHub workflow skill built on the gh CLI. Provides branch strategy, PR conventions, repo scaffolding, and common workflows.

Operating Rules
Confirm repo context before any operation: gh repo view --json nameWithOwner -q .nameWithOwner
JSON output: Use --json fields for programmatic output
Heredoc for bodies: Always use heredoc for PR/issue bodies to preserve formatting
Non-destructive: Never force-push to main/develop. Confirm before any destructive operation
Pull before branching: Never create a branch without pulling latest from parent first
Conventional Commits: All commits and PR titles follow the spec. See references/conventional-commits.md for the full type table and examples
Branch Strategy

Two modes — auto-detect before any branching or PR operation:

git branch -r | grep -q 'origin/develop' && echo "Gitflow" || echo "GitHub Flow"


GitHub Flow (no develop branch):

main ← production (protected, PR only)
  feat/*  ← from main, PR to main
  fix/*   ← from main, PR to main


Gitflow (develop branch exists):

main         ← releases + tags (protected, PR only)
  develop    ← stable dev (protected, PR only)
    feat/*   ← from develop, PR to develop
    fix/*    ← from develop, PR to develop
    hotfix/* ← from main, PR to main + develop


For detailed workflows per strategy (feature, release, hotfix), see references/branch-strategies.md.

Merging a PR

Before merging, review commit history: git log --oneline BASE..HEAD

Use AskUserQuestion to let the user choose the merge strategy. Always explain the reasoning behind each option:

header: "Merge strategy"
question: "How to merge PR #NUM? (X commits: [summarize commit quality])"
options:
- { label: "--merge (Recommended)", description: "Preserves the full commit history — useful for traceability and understanding what happened" }
- { label: "--squash", description: "Condenses all commits into one clean commit — useful when the intermediate history (wip, fix typo, etc.) doesn't add value" }


Default recommendation is --merge. Only suggest --squash first when commits are clearly messy (wip, wip2, fix typo, aaa, etc.).

Then run: gh pr merge PR_NUM --[strategy] --delete-branch

Repo Init
Ask: Language? Test command? Install command? Public or private? GitHub Flow or Gitflow?
Init: git init && git checkout -b main (+ git checkout -b develop if Gitflow)
Generate: .gitignore (language-appropriate) + .github/workflows/ci.yml (see references/ci-templates.md)
Commit: git add -A && git commit -m "chore: initial project scaffold"
Remote: gh repo create NAME --source=. --push --public|--private
Default branch: if Gitflow, gh api repos/{owner}/{repo} --method PATCH -f default_branch=develop
Protection: Apply rules for main (and develop if Gitflow). See references/branch-protection.md
Common Workflows

For issues, PR review, stash, and investigation (log/blame/bisect), see references/workflows.md.

Error Resolution
Error	First Action
403 Forbidden	Check token scopes: gh auth status
Merge conflicts	Resolve locally: git pull origin BASE && git merge --no-ff
Status checks failing	gh pr checks PR_NUM — wait or investigate CI
Branch protected	Create PR instead of direct push
Not found	Verify repo: gh repo view and branch exists

Diagnose systematically: auth → repo context → branch state → permissions.

Weekly Installs
19
Repository
ezeqviel/skills
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
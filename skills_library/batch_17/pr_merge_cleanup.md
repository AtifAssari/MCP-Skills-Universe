---
title: pr-merge-cleanup
url: https://skills.sh/jihunkim0/jk-skills/pr-merge-cleanup
---

# pr-merge-cleanup

skills/jihunkim0/jk-skills/pr-merge-cleanup
pr-merge-cleanup
Installation
$ npx skills add https://github.com/jihunkim0/jk-skills --skill pr-merge-cleanup
SKILL.md
PR Merge & Cleanup Workflow

Strict Git/GitHub PR workflow. Changes are CI-tested before entering main, local environment left clean.

Steps

Follow strictly in order:

1. Branch & Commit
git status to identify uncommitted changes.
Aggressively look for and remove unnecessary, temporary, and scratch files before staging. Unless brutally justified, they must be removed. Every single file being committed must be explicitly justified.
Never commit directly to main.
git checkout main && git pull
git checkout -b <type>/descriptive-branch-name — where <type> matches the conventional commit (fix, feat, chore, refactor, etc.)
Stage justified files and commit with a conventional commit message (e.g., fix(module): ..., feat(component): ...).
git push -u origin <branch-name>
2. Create PR
gh pr create --title "..." --body "..."
Clear title, description explaining why and how.
3. CI Validation
Wait for CI to pass:
gh pr checks or gh run list --limit 3
Never use --admin bypass unless the user explicitly says to.
If CI fails: investigate (gh run view <run-id> --log), fix, commit, push, wait again.
If the repo has no CI pipelines, confirm with the user before proceeding to merge.
4. Rebase & Merge
If main has moved ahead, rebase before merging:
git fetch origin && git rebase origin/main
Resolve any conflicts, then git push --force-with-lease
Merge:
gh pr merge <pr-number> --squash --delete-branch
Pull the squash commit:
git checkout main && git pull
5. Cleanup
Delete local feature branch: git branch -D <branch-name>
git branch — remove any stale testing or task branches.
Remove temporary scratch files (test.ts, dummy.patch, .orig, etc.).
git status — must show clean working tree, nothing to commit.
Weekly Installs
10
Repository
jihunkim0/jk-skills
First Seen
Mar 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
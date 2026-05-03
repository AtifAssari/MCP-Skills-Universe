---
title: rebase-assistant
url: https://skills.sh/jmerta/codex-skills/rebase-assistant
---

# rebase-assistant

skills/jmerta/codex-skills/rebase-assistant
rebase-assistant
Installation
$ npx skills add https://github.com/jmerta/codex-skills --skill rebase-assistant
SKILL.md
Rebase assistant
Goal

Rebase the current branch onto a target branch safely, with built-in conflict resolution guidance.

Inputs to confirm (ask if missing)
Target branch (explicit branch name or "default branch").
Preferred conflict bias when ambiguous: keep ours, keep theirs, or manual merge.
Protected paths or file types to avoid touching.
Workflow
Identify the target branch
If user says "default branch": discover via git remote show origin (read "HEAD branch").
If ambiguous or no remote: ask the user which branch to use.
Preflight checks
git status -sb (must be clean before rebase).
git fetch --prune to sync remotes.
Optional safety branch (ask before creating): git branch backup/<current-branch>.
Start the rebase
git rebase <target-branch>
If conflicts occur, resolve (repeat per file)
Inspect conflict list:
git status -sb
git diff --name-only --diff-filter=U
Classify and inspect:
Content conflicts: open file, resolve markers.
Delete/modify or rename conflicts: decide keep vs delete explicitly.
Binary conflicts: choose ours/theirs only.
Show base/ours/theirs when useful:
git show :1:<path>
git show :2:<path>
git show :3:<path>
File-level choice when safe:
git checkout --ours <path>
git checkout --theirs <path>
Stage resolved files: git add <path>
Continue: git rebase --continue
Finish and verify
Ensure no conflicts: git status -sb
Suggest a fast test/build if available.
Safety rules
Never run git reset --hard, git clean -fd, or git rebase --abort unless the user explicitly requests it.
Always show candidate commands before applying destructive changes.
Deliverables
The exact rebase command used and target branch.
Conflict list grouped by type with per-file resolution guidance.
Completion command and a short verification suggestion.
Weekly Installs
20
Repository
jmerta/codex-skills
GitHub Stars
126
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass
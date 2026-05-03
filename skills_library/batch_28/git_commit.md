---
title: git-commit
url: https://skills.sh/everyinc/compound-engineering-plugin/git-commit
---

# git-commit

skills/everyinc/compound-engineering-plugin/git-commit
git-commit
Installation
$ npx skills add https://github.com/everyinc/compound-engineering-plugin --skill git-commit
SKILL.md
Contains Shell Commands

This skill contains shell command directives (!`command`) that may execute system commands. Review carefully before installing.

Git Commit

Create a single, well-crafted git commit from the current working tree changes.

Context

If you are not Claude Code, skip to the "Context fallback" section below and run the command there to gather context.

If you are Claude Code, the five labeled sections below (Git status, Working tree diff, Current branch, Recent commits, Remote default branch) contain pre-populated data. Use them directly throughout this skill -- do not re-run these commands.

Git status: !git status

Working tree diff: !git diff HEAD

Current branch: !git branch --show-current

Recent commits: !git log --oneline -10

Remote default branch: !git rev-parse --abbrev-ref origin/HEAD 2>/dev/null || echo '__DEFAULT_BRANCH_UNRESOLVED__'

Context fallback

If you are Claude Code, skip this section — the data above is already available.

Run this single command to gather all context:

printf '=== STATUS ===\n'; git status; printf '\n=== DIFF ===\n'; git diff HEAD; printf '\n=== BRANCH ===\n'; git branch --show-current; printf '\n=== LOG ===\n'; git log --oneline -10; printf '\n=== DEFAULT_BRANCH ===\n'; git rev-parse --abbrev-ref origin/HEAD 2>/dev/null || echo '__DEFAULT_BRANCH_UNRESOLVED__'

Workflow
Step 1: Gather context

Use the context above (git status, working tree diff, current branch, recent commits, remote default branch). All data needed for this step is already available -- do not re-run those commands.

The remote default branch value returns something like origin/main. Strip the origin/ prefix to get the branch name. If it returned __DEFAULT_BRANCH_UNRESOLVED__ or a bare HEAD, try:

gh repo view --json defaultBranchRef --jq '.defaultBranchRef.name'


If both fail, fall back to main.

If the git status from the context above shows a clean working tree (no staged, modified, or untracked files), report that there is nothing to commit and stop.

If the current branch from the context above is empty, the repository is in detached HEAD state. Explain that a branch is required before committing if the user wants this work attached to a branch. Ask whether to create a feature branch now. Use the platform's blocking question tool (AskUserQuestion in Claude Code, request_user_input in Codex, ask_user in Gemini). If no question tool is available, present the options and wait for the user's reply before proceeding.

If the user chooses to create a branch, derive the name from the change content, create it with git checkout -b <branch-name>, then run git branch --show-current again and use that result as the current branch name for the rest of the workflow.
If the user declines, continue with the detached HEAD commit.
Step 2: Determine commit message convention

Follow this priority order:

Repo conventions already in context -- If project instructions (AGENTS.md, CLAUDE.md, or similar) are already loaded and specify commit message conventions, follow those. Do not re-read these files; they are loaded at session start.
Recent commit history -- If no explicit convention is documented, examine the 10 most recent commits from Step 1. If a clear pattern emerges (e.g., conventional commits, ticket prefixes, emoji prefixes), match that pattern.
Default: conventional commits -- If neither source provides a pattern, use conventional commit format: type(scope): description where type is one of feat, fix, docs, refactor, test, chore, perf, ci, style, build.
Step 3: Consider logical commits

Before staging everything together, scan the changed files for naturally distinct concerns. If modified files clearly group into separate logical changes (e.g., a refactor in one directory and a new feature in another, or test files for a different change than source files), create separate commits for each group.

Keep this lightweight:

Group at the file level only -- do not use git add -p or try to split hunks within a file.
If the separation is obvious (different features, unrelated fixes), split. If it's ambiguous, one commit is fine.
Two or three logical commits is the sweet spot. Do not over-slice into many tiny commits.
Step 4: Stage and commit

If the current branch from the context above is main, master, or the resolved default branch from Step 1, warn the user and ask whether to continue committing here or create a feature branch first. Use the platform's blocking question tool (AskUserQuestion in Claude Code, request_user_input in Codex, ask_user in Gemini). If no question tool is available, present the options and wait for the user's reply before proceeding. If the user chooses to create a branch, derive the name from the change content, create it with git checkout -b <branch-name>, then continue.

Write the commit message:

Subject line: Concise, imperative mood, focused on why not what. Follow the convention determined in Step 2.
Body (when needed): Add a body separated by a blank line for non-trivial changes. Explain motivation, trade-offs, or anything a future reader would need. Omit the body for obvious single-purpose changes.

For each commit group, stage and commit in a single call. Prefer staging specific files by name over git add -A or git add . to avoid accidentally including sensitive files (.env, credentials) or unrelated changes. Use a heredoc to preserve formatting:

git add file1 file2 file3 && git commit -m "$(cat <<'EOF'
type(scope): subject line here

Optional body explaining why this change was made,
not just what changed.
EOF
)"

Step 5: Confirm

Run git status after the commit to verify success. Report the commit hash(es) and subject line(s).

Weekly Installs
233
Repository
everyinc/compou…g-plugin
GitHub Stars
16.0K
First Seen
Mar 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
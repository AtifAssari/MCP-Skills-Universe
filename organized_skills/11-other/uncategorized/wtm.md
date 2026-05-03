---
rating: ⭐⭐
title: wtm
url: https://skills.sh/cedricvidal/coding-skills/wtm
---

# wtm

skills/cedricvidal/coding-skills/wtm
wtm
Installation
$ npx skills add https://github.com/cedricvidal/coding-skills --skill wtm
SKILL.md
Worktree PR Merge (WTM) Workflow
Usage

USE FOR:

new features that require coding
users asks to use the WTM method

DO NOT USE FOR:

asks a question which doesn't require coding
Workflow walkthrough

When the user asks to perform a coding task using the WTM method, follow this end-to-end workflow:

1. Determine base branch
Check the current branch (git branch --show-current).
If the current branch is a mainline branch (main, dev, integration, or similar), use it as the base branch.
Always fetch and use the remote tracking branch (e.g. origin/main) to ensure the worktree is created off the latest code.
If the current branch is a feature/fix branch, ask the user which branch to create the new branch off of (suggest main as the default). Wait for the user's answer.
Remember the chosen <base-branch> — it will be used later as the PR base.
2. Create worktree & branch
Derive a short <task-name> from the user's request (e.g. fix-login-bug, add-export-csv).
Fetch the latest from origin before creating the worktree:
git fetch origin <base-branch>

Create a new branch and worktree off origin/<base-branch> to ensure it starts from the latest remote state:
git worktree add <workspace-path>/.worktrees/<task-name> -b <branch-name> origin/<base-branch>

Default location: <workspace-path>/.worktrees/<task-name> (override if the user specifies a different path).
Branch naming should follow the repo convention (e.g. feat/<task-name>, fix/<task-name>).
3. Code in the worktree
If the task is simple, start implementing right away inside the worktree directory.
If the task is complex, present a plan first and get confirmation before coding.
All file operations (reads, edits, creates) happen inside the worktree path.
4. Commit incrementally
Commit after each logical step — do not batch everything into one giant commit.
Always explicitly list files to stage (never use git add . or git add -A).
When a PR has already been created for this branch

If a PR was previously created (Step 5) for this branch, use the optimistic one-liner to guard against committing to an already-merged branch:

cd <worktree-path> && [[ $(GH_PAGER=cat gh pr view <branch-name> --json state --jq '.state' 2>/dev/null) != 'MERGED' ]] && git add <file1> <file2> && git commit -m '<descriptive message>'


How it works:

If no PR exists yet → gh pr view fails → empty string ≠ MERGED → commit proceeds.
If PR is OPEN → OPEN ≠ MERGED → commit proceeds.
If PR is MERGED → MERGED = MERGED → commit is skipped.

When the commit is skipped (the PR was already merged):

Do not commit. Inform the user that the PR for this branch has already been merged.
Offer to create a new branch off the original <base-branch> (fetching the latest remote) to continue the work. Let the user choose between:
New worktree — create a fresh worktree with the new branch (start again from Step 2).
Reuse current worktree — switch the current worktree to the new branch via git switch -c <new-branch> <base-branch>.
When no PR exists yet

Use the standard commit command (no merge check needed):

cd <worktree-path> && git add <file1> <file2> && git commit -m '<descriptive message>'

5. Push & create PR (on user request)

When the user is happy and asks to merge / submit:

Push the branch:
cd <worktree-path> && git push --set-upstream origin <branch-name>

Create a pull request using gh, targeting the <base-branch> chosen in step 1:
GH_PAGER=cat gh pr create --draft --title '<title>' --body-file <body-file> --base <base-branch> --head <branch-name>

If a plan file was created for this task (e.g. plan.md), read it and include its full contents as-is in the PR body.
For long PR descriptions, write the body to a temp file first and use --body-file.
After the PR is created, ask the user if they want to mark it as ready for review. Wait for the user's answer before proceeding.
6. Mark ready for review

Whenever the user wants to mark the PR as ready (whether right after creation or later):

Mark the PR as ready for review:
GH_PAGER=cat gh pr ready <pr-number-or-url>

After the PR is marked ready, ask the user if they want to merge it. Wait for the user's answer before proceeding.
7. Merge & clean up

Whenever the user wants to merge (whether right after marking ready or later), ask what merge strategy to use: squash, merge commit, or rebase. Default to squash.

Merge the PR using the chosen strategy (--squash, --merge, or --rebase):
GH_PAGER=cat gh pr merge <pr-number-or-url> --squash --delete-branch

After a successful merge, ask the user if they want to delete the worktree. Wait for the user's answer before proceeding.
If the user confirms, remove the worktree:
git worktree remove <workspace-path>/.worktrees/<task-name>


Note: Always wait for explicit user confirmation before marking the PR as ready, merging the PR, or deleting the worktree. If the user declines at any prompt, stop and leave things as-is.

Weekly Installs
8
Repository
cedricvidal/cod…g-skills
GitHub Stars
1
First Seen
5 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
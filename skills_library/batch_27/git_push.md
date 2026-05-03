---
title: git-push
url: https://skills.sh/alpoxdev/hypercore/git-push
---

# git-push

skills/alpoxdev/hypercore/git-push
git-push
Installation
$ npx skills add https://github.com/alpoxdev/hypercore --skill git-push
SKILL.md
Git Push Skill
Available scripts
Script	Purpose
scripts/git-push.sh [--force]	Discover repos, check for unpushed commits, and push safely
Push unpushed commits to the remote for all discovered repositories.
Do nothing if there are no commits to push.
Block unsafe operations (force push to main/master, detached HEAD).

<trigger_conditions>

User intent	Activate
"push"	yes
"git push"	yes
"/git-push"	yes
"push my changes"	yes
"push commits to remote"	yes
"sync to remote"	yes
requests that only ask for commit/rebase/reset	no
"push back on this idea" (non-git context)	no

</trigger_conditions>

<argument_validation>

If ARGUMENT is missing:

Push all unpushed commits in all discovered repositories.

If ARGUMENT is --force:

Use --force-with-lease for push. Protected branches (main/master) are still blocked.

</argument_validation>

<scope_assumptions>

Start from the current working directory. If it is not a git repository, inspect descendant directories for git repositories.
Push only. Do not commit, amend, rebase, or rewrite history.
No confirmation needed — if there are commits to push, push them immediately.
Use Bash commands only.

</scope_assumptions>

Category	Rule
Safety	Never force push to main or master.
Safety	Never push from detached HEAD.
Safety	Use --force-with-lease instead of --force when force pushing.
Upstream	If no upstream is set, push with -u origin <branch> to set tracking.
Idempotent	If already up to date, report and exit cleanly.
Multi-repo	Handle descendant repositories independently.
Category	Avoid
Force push	--force to main or master
History rewrite	amend, rebase, reset, or other history-editing commands
Commit	Do not create commits — that is the git-commit skill's job
Raw force	git push --force — always use --force-with-lease
Run the script
scripts/git-push.sh


Or with force:

scripts/git-push.sh --force


The script handles everything:

Discovers repositories (current directory or descendants).
For each repository, checks the branch and upstream status.
Skips repositories with no unpushed commits, detached HEAD, or protected branch conflicts.
Pushes repositories that have commits ahead of upstream.
Reports a summary of pushed, skipped, and failed repositories.
Simple push
/git-push


Result: discovers repos, pushes any that have unpushed commits.

Force push (feature branch)
/git-push --force


Result: pushes with --force-with-lease. Blocked on main/master.

Nothing to push
/git-push


Result: reports "Already up to date" and exits cleanly.

Multi-repo push
/git-push


Result: discovers descendant repos, pushes each independently, reports summary.

Confirm the script was executed, not manual git commands.
Confirm force push was not used on main/master.
Confirm detached HEAD was skipped.
Confirm the summary output was reported to the user.
Weekly Installs
28
Repository
alpoxdev/hypercore
GitHub Stars
3
First Seen
Mar 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
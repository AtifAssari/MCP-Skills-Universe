---
title: librarian
url: https://skills.sh/mitsuhiko/agent-stuff/librarian
---

# librarian

skills/mitsuhiko/agent-stuff/librarian
librarian
Installation
$ npx skills add https://github.com/mitsuhiko/agent-stuff --skill librarian
SKILL.md

Use this skill when the user points you to a remote git repository (GitHub/GitLab/Bitbucket URLs, git@..., or owner/repo shorthand).

The goal is to keep a reusable local checkout that is:

stable (predictable path)
up to date (periodic fetch + fast-forward when safe)
efficient (partial clone with --filter=blob:none, no repeated full clones)
Cache location

Repositories are stored at:

~/.cache/checkouts/<host>/<org>/<repo>

Example:

github.com/mitsuhiko/minijinja → ~/.cache/checkouts/github.com/mitsuhiko/minijinja

Command
bash checkout.sh <repo> --path-only


Examples:

bash checkout.sh mitsuhiko/minijinja --path-only
bash checkout.sh github.com/mitsuhiko/minijinja --path-only
bash checkout.sh https://github.com/mitsuhiko/minijinja --path-only


The script will:

Parse the repo reference into host/org/repo.
Clone if missing.
Reuse existing checkout if present.
Fetch from origin when stale (default interval: 300s).
Attempt a fast-forward merge if the checkout is clean and has an upstream.
Update strategy
Default behavior is throttled refresh (every 5 minutes) to avoid unnecessary network calls.
Force immediate refresh with:
bash checkout.sh <repo> --force-update --path-only

Recommended workflow
Resolve repository path via checkout.sh --path-only.
Use that path for searching, reading, and analysis.
On later references to the same repo, call checkout.sh again; it will find and update the cached checkout.
If edits are needed

Prefer not to edit directly in the shared cache. Create a separate worktree or copy from the cached checkout for task-specific modifications.

Notes
owner/repo defaults to github.com.
Weekly Installs
25
Repository
mitsuhiko/agent-stuff
GitHub Stars
2.2K
First Seen
Mar 15, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
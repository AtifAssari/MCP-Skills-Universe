---
title: github
url: https://skills.sh/mitsuhiko/agent-commands/github
---

# github

skills/mitsuhiko/agent-commands/github
github
Installation
$ npx skills add https://github.com/mitsuhiko/agent-commands --skill github
SKILL.md
GitHub Skill

Use the gh CLI to interact with GitHub. Always specify --repo owner/repo when not in a git directory, or use URLs directly.

Pull Requests

Check CI status on a PR:

gh pr checks 55 --repo owner/repo


List recent workflow runs:

gh run list --repo owner/repo --limit 10


View a run and see which steps failed:

gh run view <run-id> --repo owner/repo


View logs for failed steps only:

gh run view <run-id> --repo owner/repo --log-failed

API for Advanced Queries

The gh api command is useful for accessing data not available through other subcommands.

Get PR with specific fields:

gh api repos/owner/repo/pulls/55 --jq '.title, .state, .user.login'

JSON Output

Most commands support --json for structured output. You can use --jq to filter:

gh issue list --repo owner/repo --json number,title --jq '.[] | "\(.number): \(.title)"'

Weekly Installs
21
Repository
mitsuhiko/agent-commands
GitHub Stars
2.2K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
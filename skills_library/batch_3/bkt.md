---
title: bkt
url: https://skills.sh/avivsinai/bitbucket-cli/bkt
---

# bkt

skills/avivsinai/bitbucket-cli/bkt
bkt
Installation
$ npx skills add https://github.com/avivsinai/bitbucket-cli --skill bkt
SKILL.md
Bitbucket CLI (bkt)

bkt is a unified CLI for Bitbucket Data Center and Bitbucket Cloud. It mirrors gh ergonomics and provides structured JSON/YAML output for automation.

Before You Start

1. Verify installation — always check before running any bkt command:

bkt --version


If not installed:

Platform	Command
macOS/Linux	brew install avivsinai/tap/bitbucket-cli
Windows	scoop bucket add avivsinai https://github.com/avivsinai/scoop-bucket && scoop install bitbucket-cli
Go	go install github.com/avivsinai/bitbucket-cli/cmd/bkt@latest
Binary	Download from GitHub Releases

2. Check authentication — most commands require an active session:

bkt auth status


Bitbucket Cloud Token Requirements:

Create an "API token with scopes" (not a general API token)
Select Bitbucket as the application
Required scope: Account: Read (read:user:bitbucket)
Additional scopes as needed: Repositories, Pull requests, Issues

For config-free use in containers and CI pipelines, see headless authentication.

If not authenticated, log in:

# Data Center (PAT-based)
bkt auth login https://bitbucket.example.com --username alice --token <PAT>

# Bitbucket Cloud — OAuth (official binaries open browser out of the box)
bkt auth login https://bitbucket.org --kind cloud --web

# Bitbucket Cloud — API token (--web-token opens Atlassian's token creation page)
bkt auth login https://bitbucket.org --kind cloud --web-token


For source and Nix builds, set BKT_OAUTH_CLIENT_ID and BKT_OAUTH_CLIENT_SECRET env vars before running --web.

3. Set up a context — contexts bind a host to a project/workspace and optional default repo, so you don't repeat flags on every command:

# Data Center
bkt context create dc-prod --host bitbucket.example.com --project ABC --set-active

# Cloud
bkt context create cloud-team --host bitbucket.org --workspace myteam --set-active

Platform Awareness

Some commands are Data Center only or Cloud only — check the command reference for *(DC)* and *(Cloud)* badges. Key splits:

Feature	Data Center	Cloud
Pull requests	yes	yes
Repositories	yes	yes
Branches (list)	yes	yes
Branches (create/delete/protect)	yes	—
Issues	—	yes
Pipelines	—	yes
Permissions	yes	—
Webhooks	yes	yes
Auto-merge, tasks, reactions	yes	—
Variables	—	yes

When a user's context is DC, do not suggest Cloud-only commands (and vice versa). If the platform is unknown, ask or check with bkt auth status.

Common Workflows
Create a PR from the current branch
bkt pr create --title "feat: add caching" --target main


Source branch, title, and target default to sensible values from git state. Add --draft for work-in-progress, --reviewer alice to request review.

Review cycle
bkt pr checks 42 --wait          # Wait for CI to pass
bkt pr approve 42                # Approve
bkt pr merge 42                  # Merge (closes source branch by default)

Checkout a colleague's PR locally
bkt pr checkout 42               # Creates pr/42 branch

Structured output for scripting

All commands support --json, --yaml, --jq, and --template:

bkt pr list --mine --json | jq '.[].title'

Raw API escape hatch

For endpoints without a dedicated command:

bkt api /rest/api/1.0/projects --param limit=100 --json

Global Flags

Every command accepts these inherited flags:

Flag	Short	Purpose
--context	-c	Use a specific named context
--json		JSON output
--yaml		YAML output
--jq		Apply a jq expression (requires --json)
--template		Render with Go template
References
headless / env vars — Config-free CI/container auth (BKT_TOKEN, BKT_HOST) and full env var reference
admin — Administrative operations for Bitbucket (DC)
auth — Manage Bitbucket authentication credentials
branch — Inspect and manage branches
commit — Work with commits
context — Manage Bitbucket CLI contexts
extension — Manage bkt CLI extensions
issue — Work with Bitbucket Cloud issues (Cloud)
perms — Manage Bitbucket permissions (DC)
pipeline — Run and inspect Bitbucket Cloud pipelines (Cloud)
pr — Manage pull requests
project — Work with Bitbucket projects (DC)
repo — Work with Bitbucket repositories
status — Inspect commit and pull request statuses
variable — Manage pipeline variables (Cloud)
webhook — Manage Bitbucket webhooks
other — api
Weekly Installs
549
Repository
avivsinai/bitbucket-cli
GitHub Stars
101
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
---
title: railway
url: https://skills.sh/mshumer/claude-skill-railway/railway
---

# railway

skills/mshumer/claude-skill-railway/railway
railway
Installation
$ npx skills add https://github.com/mshumer/claude-skill-railway --skill railway
SKILL.md
Contains Shell Commands

This skill contains shell command directives (!`command`) that may execute system commands. Review carefully before installing.

Railway CLI Skill

Manage Railway deployments and infrastructure using the Railway CLI.

Pre-flight Check

Current status: !railway status 2>&1 || echo "NOT_LINKED"

Auto-Recovery

Before running any command, check the pre-flight status above:

If "command not found": Run npm install -g @railway/cli
If "Not logged in": Tell user to run railway login manually (requires browser)
If "NOT_LINKED" or "No project linked":
Run railway list to show available projects
Ask user which project to link, or auto-detect from package.json name
Link with railway link -p <project-id>
Command Routing

Based on $ARGUMENTS, execute the appropriate workflow:

"status" (default when no args)
railway status
railway domain
railway deployment list --limit 1


Report: project info, URL, and last deployment status/time.

"logs" [options]

Parse natural language options:

"errors" → --filter "@level:error"
"last hour" / "1h" → --since 1h
"build" → --build
Number like "100" → --lines 100

Default: railway logs --lines 30

Summarize output - highlight errors, warnings, or interesting patterns.

"deploy" / "up"
railway up


Then wait and check:

Run railway deployment list --limit 1 to get status
If SUCCESS, fetch the domain URL and verify it responds: curl -s -o /dev/null -w "%{http_code}" <domain>
If FAILED, show build logs: railway logs --build --lines 50
"redeploy"
railway redeploy


Redeploys without rebuilding. Useful for env var changes.

"restart"
railway restart


Restarts the service without rebuild or redeploy.

"vars" / "env" [action]
railway variables


IMPORTANT: When displaying variables, redact sensitive values:

API keys: show first 8 chars + "..."
Passwords: show "********"
Tokens: show first 8 chars + "..."

For setting: railway variables set KEY=value For deleting: railway variables delete KEY (ask for confirmation first!)

"deployments" / "history"
railway deployment list --limit 10


Format as a table with: ID (short), Status, Time ago, Commit message (truncated)

"domain"
railway domain


Show the public URL. If none exists, offer to create one.

"health"
railway domain


Then curl the domain to check HTTP status:

curl -s -o /dev/null -w "%{http_code}" -m 10 <domain-url>


Report if healthy (2xx), unhealthy, or unreachable.

"open"
railway open


Opens the Railway dashboard in browser.

"switch "

Switch to a different Railway project by name (fuzzy match).

# List all projects
railway list


Find the project ID that matches the name, then:

railway link -p <project-id>


Confirm the switch with railway status.

"db" / "connect"

Connect to the project's database shell (Postgres, MongoDB, Redis, etc.)

railway connect


If multiple databases exist, Railway will prompt to select one.

"link"

List available projects and link one:

railway list


Show projects in a numbered list. Ask user which to link, then:

railway link -p <project-id>

Safety Guards

Before destructive operations, ask for confirmation:

railway down - removes deployment
railway variables delete - removes env var
railway unlink - unlinks project

Format: "This will [action]. Are you sure? (y/n)"

Response Format

Always provide:

Summary: One-line status (✓ success / ✗ failure / ⚠ warning)
Details: Relevant information in a clean table or list
URL: Public URL if applicable
Next steps: If something failed, suggest how to fix it
Example Responses

Status check:

✓ MyApp is deployed and healthy

| Project     | MyApp                                    |
| Environment | production                               |
| Service     | MyApp                                    |
| URL         | https://myapp-production.up.railway.app  |
| Last deploy | 2 hours ago (SUCCESS)                    |


After deploy:

✓ Deployment successful

Build completed in 45s
URL: https://myapp-production.up.railway.app
Health check: 200 OK


On error:

✗ Deployment failed

Build error at line 23: Module not found 'xyz'

Suggested fix: Run `npm install xyz` and redeploy

Weekly Installs
123
Repository
mshumer/claude-…-railway
GitHub Stars
25
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn
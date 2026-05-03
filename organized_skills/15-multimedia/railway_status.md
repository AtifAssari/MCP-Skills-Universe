---
rating: ⭐⭐
title: railway-status
url: https://skills.sh/davila7/claude-code-templates/railway-status
---

# railway-status

skills/davila7/claude-code-templates/railway-status
railway-status
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill railway-status
SKILL.md
Railway Status

Check the current Railway project status for this directory.

When to Use
User asks about Railway status, project, services, or deployments
User mentions deploying or pushing to Railway
Before any Railway operation (deploy, update service, add variables)
User asks about environments or domains
When NOT to Use

Use the railway-environment skill instead when user wants:

Detailed service configuration (builder type, dockerfile path, build command, root directory)
Deploy config (start command, restart policy, healthchecks, predeploy command)
Service source (repo, branch, image)
Compare service configs
Query or change environment variables
Check Status

Run:

railway status --json


First verify CLI is installed:

command -v railway

Handling Errors
CLI Not Installed

If command -v railway fails:

Railway CLI is not installed. Install with:

npm install -g @railway/cli


or

brew install railway


Then authenticate: railway login

Not Authenticated

If railway whoami fails:

Not logged in to Railway. Run:

railway login

No Project Linked

If status returns "No linked project":

No Railway project linked to this directory.

To link an existing project: railway link To create a new project: railway init

Presenting Status

Parse the JSON and present:

Project: name and workspace
Environment: current environment (production, staging, etc.)
Services: list with deployment status
Active Deployments: any in-progress deployments (from activeDeployments field)
Domains: any configured domains

Example output format:

Project: my-app (workspace: my-team)
Environment: production

Services:
- web: deployed (https://my-app.up.railway.app)
- api: deploying (build in progress)
- postgres: running


The activeDeployments array on each service shows currently running deployments with their status (building, deploying, etc.).

Weekly Installs
254
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
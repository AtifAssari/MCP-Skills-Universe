---
title: deploy
url: https://skills.sh/railwayapp/railway-skills/deploy
---

# deploy

skills/railwayapp/railway-skills/deploy
deploy
Installation
$ npx skills add https://github.com/railwayapp/railway-skills --skill deploy
Summary

Push code to Railway with railway up, supporting detach and CI streaming modes.

Two deployment modes: detach (default, returns immediately) and CI (streams build logs until complete)
Always include a -m flag with a descriptive commit message summarizing the changes being deployed
Supports targeting specific services and environments via --service and --environment flags, or deploying to unlinked projects with --project and --environment
CLI automatically walks up the directory tree to find a linked project, so subdirectories don't require relinking
Use the deployment skill to check build status after detach mode; do not run railway logs --build after CI mode as logs have already streamed
SKILL.md
Deploy

Deploy code from the current directory to Railway using railway up.

When to Use
User asks to "deploy", "ship", "push code"
User says "railway up" or "deploy to Railway"
User wants to deploy local code changes
User says "deploy and fix any issues" (use --ci mode)
Commit Message

Always use the -m flag with a descriptive commit message summarizing what's being deployed:

railway up --detach -m "Add user authentication endpoint"


Good commit messages:

Describe what changed: "Fix memory leak in worker process"
Reference tickets/issues: "Implement feature #123"
Be concise but meaningful: "Update deps and fix build warnings"
Modes
Detach Mode (default)

Starts deploy and returns immediately. Use for most deploys.

railway up --detach -m "Deploy description here"

CI Mode

Streams build logs until complete. Use when user wants to watch the build or needs to debug issues.

railway up --ci -m "Deploy description here"


When to use CI mode:

User says "deploy and watch", "deploy and fix issues"
User is debugging build failures
User wants to see build output
Deploy Specific Service

Default is linked service. To deploy to a different service:

railway up --detach --service backend -m "Deploy description here"

Deploy to Unlinked Project

Deploy to a project without linking first:

railway up --project <project-id> --environment production --detach -m "Deploy description here"


Requires both --project and --environment flags.

CLI Options
Flag	Description
-m, --message <MSG>	Commit message describing the deploy (always use this)
-d, --detach	Don't attach to logs (default)
-c, --ci	Stream build logs, exit when done
-s, --service <NAME>	Target service (defaults to linked)
-e, --environment <NAME>	Target environment (defaults to linked)
-p, --project <ID>	Target project (requires --environment)
[PATH]	Path to deploy (defaults to current directory)
Directory Linking

Railway CLI walks UP the directory tree to find a linked project. If you're in a subdirectory of a linked project, you don't need to relink.

For subdirectory deployments, prefer setting rootDirectory via the environment skill, then deploy normally with railway up.

After Deploy
Detach mode
Deploying to <service>...


Use deployment skill to check build status (with --lines flag).

CI mode

Build logs stream inline. If build fails, the error will be in the output.

Do NOT run railway logs --build after CI mode - the logs already streamed. If you need more context, use deployment skill with --lines flag (never stream).

Composability
Check status after deploy: Use service skill
View logs: Use deployment skill
Fix config issues: Use environment skill
Redeploy after config fix: Use environment skill
Error Handling
No Project Linked
No Railway project linked. Run `railway link` first.

No Service Linked
No service linked. Use --service flag or run `railway service` to select one.

Build Failure (CI mode)

The build logs already streamed - analyze them directly from the railway up --ci output. Do NOT run railway logs after CI mode (it streams forever without --lines).

Common issues:

Missing dependencies → check package.json/requirements.txt
Build command wrong → use environment skill to fix
Dockerfile issues → check dockerfile path
Weekly Installs
954
Repository
railwayapp/rail…y-skills
GitHub Stars
254
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass
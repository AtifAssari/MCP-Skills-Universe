---
title: use-railway
url: https://skills.sh/railwayapp/railway-skills/use-railway
---

# use-railway

skills/railwayapp/railway-skills/use-railway
use-railway
Installation
$ npx skills add https://github.com/railwayapp/railway-skills --skill use-railway
Summary

Complete Railway infrastructure management: projects, services, databases, deployments, environments, object storage, and troubleshooting.

Operates across Railway's resource hierarchy: workspaces, projects, environments, services, buckets, and deployments with CLI context management
Covers five operational domains: resource setup, code deployment, configuration management, health monitoring, and API/docs access
Includes preflight authentication checks, context resolution, and multi-step composition patterns for common workflows like first deploy, adding object storage, and failure recovery
Supports both CLI commands and GraphQL API fallback for operations the CLI doesn't expose; all outputs use --json for reliable parsing
SKILL.md
Use Railway
Railway resource model

Railway organizes infrastructure in a hierarchy:

Workspace is the billing and team scope. A user belongs to one or more workspaces.
Project is a collection of services under one workspace. It maps to one deployable unit of work.
Environment is an isolated configuration plane inside a project (for example, production, staging). Each environment has its own variables, config, and deployment history.
Service is a single deployable unit inside a project. It can be an app from a repo, a Docker image, or a managed database.
Bucket is an S3-compatible object storage resource inside a project. Buckets are created at the project level and deployed to environments. Each bucket has credentials (endpoint, access key, secret key) for S3-compatible access.
Deployment is a point-in-time release of a service in an environment. It has build logs, runtime logs, and a status lifecycle.

Most CLI commands operate on the linked project/environment/service context. Use railway status --json to see the context, and --project, --environment, --service flags to override.

Parsing Railway URLs

Users often paste Railway dashboard URLs. Extract IDs before doing anything else:

https://railway.com/project/<PROJECT_ID>/service/<SERVICE_ID>?environmentId=<ENV_ID>
https://railway.com/project/<PROJECT_ID>/service/<SERVICE_ID>


The URL always contains projectId and serviceId. It may contain environmentId as a query parameter. If the environment ID is missing and the user specifies an environment by name (e.g., "production"), resolve it:

scripts/railway-api.sh \
  'query getProject($id: String!) {
    project(id: $id) {
      environments { edges { node { id name } } }
    }
  }' \
  '{"id": "<PROJECT_ID>"}'


Match the environment name (case-insensitive) to get the environmentId.

Prefer passing explicit IDs to CLI commands (--project, --environment, --service) and scripts (--project-id, --environment-id, --service-id) instead of running railway link. This avoids modifying global state and is faster.

Preflight

Before any mutation, verify context:

command -v railway                # CLI installed
railway whoami --json             # authenticated
railway --version                 # check CLI version


Context resolution — URL IDs always win:

If the user provides a Railway URL, extract IDs from it. Do NOT run railway status --json — it returns the locally linked project, which is usually unrelated.
If no URL is given, fall back to railway status --json for the linked project/environment/service.

If the CLI is missing, guide the user to install it.

bash <(curl -fsSL cli.new) # Shell script (macOS, Linux, Windows via WSL)
brew install railway # Homebrew (macOS)
npm i -g @railway/cli # npm (macOS, Linux, Windows). Requires Node.js version 16 or higher.


If not authenticated, run railway login. If not linked and no URL was provided, run railway link --project <id-or-name>.

If a command is not recognized (for example, railway environment edit), the CLI may be outdated. Upgrade with:

railway upgrade

Common quick operations

These are frequent enough to handle without loading a reference:

railway status --json                                    # current context
railway whoami --json                                    # auth and workspace info
railway project list --json                              # list projects
railway service status --all --json                      # all services in current context
railway variable list --service <svc> --json             # list variables
railway variable set KEY=value --service <svc>           # set a variable
railway logs --service <svc> --lines 200 --json          # recent logs
railway up --detach -m "<summary>"                       # deploy current directory
railway bucket list --json                               # list buckets in current environment
railway bucket info --bucket <name> --json               # bucket storage and object count
railway bucket credentials --bucket <name> --json        # S3-compatible credentials

Routing

For anything beyond quick operations, load the reference that matches the user's intent. Load only what you need, one reference is usually enough, two at most.

Intent	Reference	Use for
Analyze a database ("analyze <url>", "analyze db", "analyze database", "analyze service", "introspect", "check my postgres/redis/mysql/mongo")	analyze-db.md	Database introspection and performance analysis. analyze-db.md directs you to the DB-specific reference. This takes priority over the status/operate routes when a Railway URL to a database service is provided alongside "analyze".
Create or connect resources	setup.md	Projects, services, databases, buckets, templates, workspaces
Ship code or manage releases	deploy.md	Deploy, redeploy, restart, build config, monorepo, Dockerfile
Change configuration	configure.md	Environments, variables, config patches, domains, networking
Check health or debug failures	operate.md	Status, logs, metrics, build/runtime triage, recovery
Request from API, docs, or community	request.md	Railway GraphQL API queries/mutations, metrics queries, Central Station, official docs

If the request spans two areas (for example, "deploy and then check if it's healthy"), load both references and compose one response.

Execution rules
Prefer Railway CLI. Fall back to scripts/railway-api.sh for operations the CLI doesn't expose.
Use --json output where available for reliable parsing.
Resolve context before mutation. Know which project, environment, and service you're acting on.
For destructive actions (delete service, remove deployment, drop database), confirm intent and state impact before executing.
After mutations, verify the result with a read-back command.
User-only commands (NEVER execute directly)

These commands modify database state and require the user to run them directly in their terminal. Do NOT execute these with Bash. Instead, show the command and ask the user to run it.

Command	Why user-only
python3 scripts/enable-pg-stats.py --service <name>	Modifies shared_preload_libraries, may restart database
python3 scripts/pg-extensions.py --service <name> install <ext>	Installs database extension
python3 scripts/pg-extensions.py --service <name> uninstall <ext>	Removes database extension
ALTER SYSTEM SET ...	Changes PostgreSQL configuration
DROP EXTENSION ...	Removes database extension
CREATE EXTENSION ...	Installs database extension

When these operations are needed:

Explain what the command does and any side effects (e.g., restart required)
Show the exact command the user should run
Wait for user confirmation that they ran it
Verify the result with a read-only query
Composition patterns

Multi-step workflows follow natural chains:

Add object storage: setup (create bucket), setup (get credentials), configure (set S3 variables on app service)
First deploy: setup (create project + service), configure (set variables and source), deploy, operate (verify healthy)
Fix a failure: operate (triage logs), configure (fix config/variables), deploy (redeploy), operate (verify recovery)
Add a domain: configure (add domain + set port), operate (verify DNS and service health)
Docs to action: request (fetch docs answer), route to the relevant operational reference

When composing, return one unified response covering all steps. Don't ask the user to invoke each step separately.

Setup decision flow

When the user wants to create or deploy something, determine the right action from current context:

Run railway status --json in the current directory.
If linked: add a service to the existing project (railway add --service <name>). Do not create a new project unless the user explicitly says "new project" or "separate project".
If not linked: check the parent directory (cd .. && railway status --json).
Parent linked: this is likely a monorepo sub-app. Add a service and set rootDirectory to the sub-app path.
Parent not linked: run railway list --json and look for a project matching the directory name.
Match found: link to it (railway link --project <name>).
No match: create a new project (railway init --name <name>).
When multiple workspaces exist, match by name from railway whoami --json.

Naming heuristic: app names like "flappy-bird" or "my-api" are service names, not project names. Use the directory or repo name for the project.

Response format

For all operational responses, return:

What was done (action and scope).
The result (IDs, status, key output).
What to do next (or confirmation that the task is complete).

Keep output concise. Include command evidence only when it helps the user understand what happened.

Weekly Installs
3.1K
Repository
railwayapp/rail…y-skills
GitHub Stars
254
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail
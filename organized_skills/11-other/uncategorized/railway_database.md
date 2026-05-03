---
rating: ⭐⭐⭐
title: railway-database
url: https://skills.sh/davila7/claude-code-templates/railway-database
---

# railway-database

skills/davila7/claude-code-templates/railway-database
railway-database
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill railway-database
SKILL.md
Railway Database

Add official Railway database services. These are maintained templates with pre-configured volumes, networking, and connection variables.

For non-database templates, see the railway-templates skill.

When to Use
User asks to "add a database", "add Postgres", "add Redis", etc.
User needs a database for their application
User asks about connecting to a database
User says "add postgres and connect to my server"
User says "wire up the database"
Decision Flow

ALWAYS check for existing databases FIRST before creating.

User mentions database
        │
  Check existing DBs first
  (query env config for source.image)
        │
   ┌────┴────┐
 Exists    Doesn't exist
    │           │
    │      Create database
    │      (CLI or API)
    │           │
    │      Wait for deployment
    │           │
    └─────┬─────┘
          │
    User wants to
    connect service?
          │
    ┌─────┴─────┐
   Yes         No
    │           │
Wire vars    Done +
via env     suggest wiring
skill

Check for Existing Databases

Before creating a database, check if one already exists.

For full environment config structure, see environment-config.md.

railway status --json


Then query environment config and check source.image for each service:

query environmentConfig($environmentId: String!) {
  environment(id: $environmentId) {
    config(decryptVariables: false)
  }
}


The config.services object contains each service's configuration. Check source.image for:

ghcr.io/railway/postgres* or postgres:* → Postgres
ghcr.io/railway/redis* or redis:* → Redis
ghcr.io/railway/mysql* or mysql:* → MySQL
ghcr.io/railway/mongo* or mongo:* → MongoDB
Available Databases
Database	Template Code
PostgreSQL	postgres
Redis	redis
MySQL	mysql
MongoDB	mongodb
Prerequisites

Get project context:

railway status --json


Extract:

id - project ID
environments.edges[0].node.id - environment ID

Get workspace ID (not in status output):

bash <<'SCRIPT'
${CLAUDE_PLUGIN_ROOT}/skills/lib/railway-api.sh \
  'query getWorkspace($projectId: String!) {
    project(id: $projectId) { workspaceId }
  }' \
  '{"projectId": "PROJECT_ID"}'
SCRIPT

Adding a Database
Step 1: Fetch Template
bash <<'SCRIPT'
${CLAUDE_PLUGIN_ROOT}/skills/lib/railway-api.sh \
  'query template($code: String!) {
    template(code: $code) {
      id
      name
      serializedConfig
    }
  }' \
  '{"code": "postgres"}'
SCRIPT


This returns the template's id and serializedConfig needed for deployment.

Step 2: Deploy Template
bash <<'SCRIPT'
${CLAUDE_PLUGIN_ROOT}/skills/lib/railway-api.sh \
  'mutation deployTemplate($input: TemplateDeployV2Input!) {
    templateDeployV2(input: $input) {
      projectId
      workflowId
    }
  }' \
  '{
    "input": {
      "templateId": "TEMPLATE_ID",
      "serializedConfig": SERIALIZED_CONFIG,
      "projectId": "PROJECT_ID",
      "environmentId": "ENVIRONMENT_ID",
      "workspaceId": "WORKSPACE_ID"
    }
  }'
SCRIPT


Important: serializedConfig is the exact object from the template query, not a string.

Connecting to the Database

After deployment, other services connect using reference variables.

For complete variable reference syntax and wiring patterns, see variables.md.

Backend Services (Server-side)

Use the private/internal URL for server-to-server communication:

Database	Variable Reference
PostgreSQL	${{Postgres.DATABASE_URL}}
Redis	${{Redis.REDIS_URL}}
MySQL	${{MySQL.MYSQL_URL}}
MongoDB	${{MongoDB.MONGO_URL}}
Frontend Applications

Important: Frontends run in the user's browser and cannot access Railway's private network. They must use public URLs or go through a backend API.

For direct database access from frontend (not recommended):

Use the public URL variables (e.g., ${{MongoDB.MONGO_PUBLIC_URL}})
Requires TCP proxy to be enabled

Better pattern: Frontend → Backend API → Database

Example: Add PostgreSQL
bash <<'SCRIPT'
# 1. Get context
railway status --json
# Extract project.id and environment.id

# 2. Get workspace ID
${CLAUDE_PLUGIN_ROOT}/skills/lib/railway-api.sh \
  'query { project(id: "proj-id") { workspaceId } }' '{}'

# 3. Fetch Postgres template
${CLAUDE_PLUGIN_ROOT}/skills/lib/railway-api.sh \
  'query { template(code: "postgres") { id serializedConfig } }' '{}'

# 4. Deploy template
${CLAUDE_PLUGIN_ROOT}/skills/lib/railway-api.sh \
  'mutation deploy($input: TemplateDeployV2Input!) {
    templateDeployV2(input: $input) { projectId workflowId }
  }' \
  '{"input": {"templateId": "...", "serializedConfig": {...}, "projectId": "...", "environmentId": "...", "workspaceId": "..."}}'
SCRIPT

Then Connect From Another Service

Use railway-environment skill to add the variable reference:

{
  "services": {
    "<backend-service-id>": {
      "variables": {
        "DATABASE_URL": { "value": "${{Postgres.DATABASE_URL}}" }
      }
    }
  }
}

Response

Successful deployment returns:

{
  "data": {
    "templateDeployV2": {
      "projectId": "e63baedb-e308-49e9-8c06-c25336f861c7",
      "workflowId": "deployTemplate/project/e63baedb-e308-49e9-8c06-c25336f861c7/xxx"
    }
  }
}

What Gets Created

Each database template creates:

A service with the database image
A volume for data persistence
Environment variables for connection strings
TCP proxy for external access (where applicable)
Error Handling
Error	Cause	Solution
Template not found	Invalid template code	Use: postgres, redis, mysql, mongodb
Permission denied	User lacks access	Need DEVELOPER role or higher
Project not found	Invalid project ID	Run railway status --json for correct ID
Example Workflows
"add postgres and connect to the server"
Check existing DBs via env config query
If postgres exists: Skip to step 5
If not exists: Deploy postgres template (fetch template → deploy)
Wait for deployment to complete
Identify target service (ask if multiple, or use linked service)
Use railway-environment skill to stage: DATABASE_URL: { "value": "${{Postgres.DATABASE_URL}}" }
Apply changes
"add postgres"
Check existing DBs via env config query
If exists: "Postgres already exists in this project"
If not exists: Deploy postgres template
Inform user: "Postgres created. Connect a service with: DATABASE_URL=${{Postgres.DATABASE_URL}}"
"connect the server to redis"
Check existing DBs via env config query
If redis exists: Wire up REDIS_URL via environment skill → apply
If no redis: Ask "No Redis found. Create one?"
Deploy redis template
Wire REDIS_URL → apply
Composability
Connect services: Use railway-environment skill to add variable references
View database service: Use railway-service skill
Check logs: Use railway-deployment skill
Weekly Installs
267
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
---
rating: ⭐⭐
title: railway-templates
url: https://skills.sh/davila7/claude-code-templates/railway-templates
---

# railway-templates

skills/davila7/claude-code-templates/railway-templates
railway-templates
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill railway-templates
SKILL.md
Railway Templates

Search and deploy services from Railway's template marketplace.

When to Use
User asks to "add Postgres", "add Redis", "add a database"
User asks to "add Ghost", "add Strapi", "add n8n", or any other service
User wants to find templates for a use case (e.g., "CMS", "storage", "monitoring")
User asks "what templates are available?"
User wants to deploy a pre-configured service
Common Template Codes
Category	Template	Code
Databases	PostgreSQL	postgres
	Redis	redis
	MySQL	mysql
	MongoDB	mongodb
CMS	Ghost	ghost
	Strapi	strapi
Storage	Minio	minio
Automation	n8n	n8n
Monitoring	Uptime Kuma	uptime-kuma

For other templates, use the search query below.

Prerequisites

Get project context:

railway status --json


Extract:

id - project ID
environments.edges[0].node.id - environment ID

Get workspace ID:

bash <<'SCRIPT'
${CLAUDE_PLUGIN_ROOT}/skills/lib/railway-api.sh \
  'query getWorkspace($projectId: String!) {
    project(id: $projectId) { workspaceId }
  }' \
  '{"projectId": "PROJECT_ID"}'
SCRIPT

Search Templates

List available templates with optional filters:

bash <<'SCRIPT'
${CLAUDE_PLUGIN_ROOT}/skills/lib/railway-api.sh \
  'query templates($first: Int, $verified: Boolean) {
    templates(first: $first, verified: $verified) {
      edges {
        node {
          name
          code
          description
          category
        }
      }
    }
  }' \
  '{"first": 20, "verified": true}'
SCRIPT

Arguments
Argument	Type	Description
first	Int	Number of results (max ~100)
verified	Boolean	Only verified templates
recommended	Boolean	Only recommended templates
Rate Limit

10 requests per minute. Don't spam searches.

Get Template Details

Fetch a specific template by code:

bash <<'SCRIPT'
${CLAUDE_PLUGIN_ROOT}/skills/lib/railway-api.sh \
  'query template($code: String!) {
    template(code: $code) {
      id
      name
      description
      serializedConfig
    }
  }' \
  '{"code": "postgres"}'
SCRIPT


Returns:

id - template ID (needed for deployment)
serializedConfig - service configuration (needed for deployment)
Deploy Template
Step 1: Fetch Template
bash <<'SCRIPT'
${CLAUDE_PLUGIN_ROOT}/skills/lib/railway-api.sh \
  'query template($code: String!) {
    template(code: $code) {
      id
      serializedConfig
    }
  }' \
  '{"code": "postgres"}'
SCRIPT

Step 2: Deploy to Project
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
      "templateId": "TEMPLATE_ID_FROM_STEP_1",
      "serializedConfig": SERIALIZED_CONFIG_FROM_STEP_1,
      "projectId": "PROJECT_ID",
      "environmentId": "ENVIRONMENT_ID",
      "workspaceId": "WORKSPACE_ID"
    }
  }'
SCRIPT


Important: serializedConfig is the exact JSON object from the template query, not a string.

Composability
Connect services: Use railway-environment skill to add variable references
View deployed service: Use railway-service skill
Check logs: Use railway-deployment skill
Add domains: Use railway-domain skill
Weekly Installs
258
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
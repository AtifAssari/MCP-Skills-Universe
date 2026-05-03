---
rating: ⭐⭐
title: projects
url: https://skills.sh/railwayapp/railway-skills/projects
---

# projects

skills/railwayapp/railway-skills/projects
projects
Installation
$ npx skills add https://github.com/railwayapp/railway-skills --skill projects
Summary

List, switch, and configure Railway projects with CLI commands and GraphQL mutations.

List all projects and workspaces, or switch between projects using railway link and project IDs
Rename projects, enable/disable PR deploys, toggle public/private visibility, and configure bot PR environments via GraphQL mutations
Extract project IDs from railway status --json to use in update operations
Composable with status, new, and environment skills for viewing details, creating projects, and managing environments
SKILL.md
Project Management

List, switch, and configure Railway projects.

When to Use
User asks "show me all my projects" or "what projects do I have"
User asks about projects across workspaces
User asks "what workspaces do I have"
User wants to switch to a different project
User asks to rename a project
User wants to enable/disable PR deploys
User wants to make a project public or private
User asks about project settings
List Projects

The railway list --json output can be very large. Run in a subagent and return only essential fields:

Project: id, name
Workspace: id, name
Services: name (optional, if user needs service context)
railway list --json


Extract and return a simplified summary, not the full JSON.

List Workspaces
railway whoami --json


Returns user info including all workspaces the user belongs to.

Switch Project

Link a different project to the current directory:

railway link -p <project-id-or-name>


Or interactively:

railway link


After switching, use status skill to see project details.

Update Project

Modify project settings via GraphQL API.

Get Project ID
railway status --json


Extract project.id from the response.

Update Mutation
bash <<'SCRIPT'
scripts/railway-api.sh \
  'mutation updateProject($id: String!, $input: ProjectUpdateInput!) {
    projectUpdate(id: $id, input: $input) { name prDeploys isPublic botPrEnvironments }
  }' \
  '{"id": "PROJECT_ID", "input": {"name": "new-name"}}'
SCRIPT

ProjectUpdateInput Fields
Field	Type	Description
name	String	Project name
description	String	Project description
isPublic	Boolean	Make project public/private
prDeploys	Boolean	Enable/disable PR deploys
botPrEnvironments	Boolean	Enable Dependabot/Renovate PR environments
Examples

Rename project:

scripts/railway-api.sh '<mutation>' '{"id": "uuid", "input": {"name": "new-name"}}'


Enable PR deploys:

scripts/railway-api.sh '<mutation>' '{"id": "uuid", "input": {"prDeploys": true}}'


Make project public:

scripts/railway-api.sh '<mutation>' '{"id": "uuid", "input": {"isPublic": true}}'


Multiple fields:

scripts/railway-api.sh '<mutation>' '{"id": "uuid", "input": {"name": "new-name", "prDeploys": true}}'

Composability
View project details: Use status skill
Create new project: Use new skill
Manage environments: Use environment skill
Error Handling
Not Authenticated
Not authenticated. Run `railway login` first.

No Projects
No projects found. Create one with `railway init`.

Permission Denied
You don't have permission to modify this project. Check your Railway role.

Project Not Found
Project "foo" not found. Run `railway list` to see available projects.

Weekly Installs
862
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
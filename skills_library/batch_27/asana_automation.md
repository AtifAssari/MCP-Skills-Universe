---
title: asana-automation
url: https://skills.sh/aaaaqwq/claude-code-skills/asana-automation
---

# asana-automation

skills/aaaaqwq/claude-code-skills/asana-automation
asana-automation
Installation
$ npx skills add https://github.com/aaaaqwq/claude-code-skills --skill asana-automation
SKILL.md
Asana Automation via Rube MCP

Automate Asana operations through Composio's Asana toolkit via Rube MCP.

Prerequisites
Rube MCP must be connected (RUBE_SEARCH_TOOLS available)
Active Asana connection via RUBE_MANAGE_CONNECTIONS with toolkit asana
Always call RUBE_SEARCH_TOOLS first to get current tool schemas
Setup

Get Rube MCP: Add https://rube.app/mcp as an MCP server in your client configuration. No API keys needed — just add the endpoint and it works.

Verify Rube MCP is available by confirming RUBE_SEARCH_TOOLS responds
Call RUBE_MANAGE_CONNECTIONS with toolkit asana
If connection is not ACTIVE, follow the returned auth link to complete Asana OAuth
Confirm connection status shows ACTIVE before running any workflows
Core Workflows
1. Manage Tasks

When to use: User wants to create, search, list, or organize tasks

Tool sequence:

ASANA_GET_MULTIPLE_WORKSPACES - Get workspace ID [Prerequisite]
ASANA_SEARCH_TASKS_IN_WORKSPACE - Search tasks [Optional]
ASANA_GET_TASKS_FROM_A_PROJECT - List project tasks [Optional]
ASANA_CREATE_A_TASK - Create a new task [Optional]
ASANA_GET_A_TASK - Get task details [Optional]
ASANA_CREATE_SUBTASK - Create a subtask [Optional]
ASANA_GET_TASK_SUBTASKS - List subtasks [Optional]

Key parameters:

workspace: Workspace GID (required for search/creation)
projects: Array of project GIDs to add task to
name: Task name
notes: Task description
assignee: Assignee (user GID or email)
due_on: Due date (YYYY-MM-DD)

Pitfalls:

Workspace GID is required for most operations; get it first
Task GIDs are returned as strings, not integers
Search is workspace-scoped, not project-scoped
2. Manage Projects and Sections

When to use: User wants to create projects, manage sections, or organize tasks

Tool sequence:

ASANA_GET_WORKSPACE_PROJECTS - List workspace projects [Optional]
ASANA_GET_A_PROJECT - Get project details [Optional]
ASANA_CREATE_A_PROJECT - Create a new project [Optional]
ASANA_GET_SECTIONS_IN_PROJECT - List sections [Optional]
ASANA_CREATE_SECTION_IN_PROJECT - Create a new section [Optional]
ASANA_ADD_TASK_TO_SECTION - Move task to section [Optional]
ASANA_GET_TASKS_FROM_A_SECTION - List tasks in section [Optional]

Key parameters:

project_gid: Project GID
name: Project or section name
workspace: Workspace GID for creation
task: Task GID for section assignment
section: Section GID

Pitfalls:

Projects belong to workspaces; workspace GID is needed for creation
Sections are ordered within a project
DUPLICATE_PROJECT creates a copy with optional task inclusion
3. Manage Teams and Users

When to use: User wants to list teams, team members, or workspace users

Tool sequence:

ASANA_GET_TEAMS_IN_WORKSPACE - List workspace teams [Optional]
ASANA_GET_USERS_FOR_TEAM - List team members [Optional]
ASANA_GET_USERS_FOR_WORKSPACE - List all workspace users [Optional]
ASANA_GET_CURRENT_USER - Get authenticated user [Optional]
ASANA_GET_MULTIPLE_USERS - Get multiple user details [Optional]

Key parameters:

workspace_gid: Workspace GID
team_gid: Team GID

Pitfalls:

Users are workspace-scoped
Team membership requires the team GID
4. Parallel Operations

When to use: User needs to perform bulk operations efficiently

Tool sequence:

ASANA_SUBMIT_PARALLEL_REQUESTS - Execute multiple API calls in parallel [Required]

Key parameters:

actions: Array of action objects with method, path, and data

Pitfalls:

Each action must be a valid Asana API call
Failed individual requests do not roll back successful ones
Common Patterns
ID Resolution

Workspace name -> GID:

1. Call ASANA_GET_MULTIPLE_WORKSPACES
2. Find workspace by name
3. Extract gid field


Project name -> GID:

1. Call ASANA_GET_WORKSPACE_PROJECTS with workspace GID
2. Find project by name
3. Extract gid field

Pagination
Asana uses cursor-based pagination with offset parameter
Check for next_page in response
Pass offset from next_page.offset for next request
Known Pitfalls

GID Format:

All Asana IDs are strings (GIDs), not integers
GIDs are globally unique identifiers

Workspace Scoping:

Most operations require a workspace context
Tasks, projects, and users are workspace-scoped
Quick Reference
Task	Tool Slug	Key Params
List workspaces	ASANA_GET_MULTIPLE_WORKSPACES	(none)
Search tasks	ASANA_SEARCH_TASKS_IN_WORKSPACE	workspace, text
Create task	ASANA_CREATE_A_TASK	workspace, name, projects
Get task	ASANA_GET_A_TASK	task_gid
Create subtask	ASANA_CREATE_SUBTASK	parent, name
List subtasks	ASANA_GET_TASK_SUBTASKS	task_gid
Project tasks	ASANA_GET_TASKS_FROM_A_PROJECT	project_gid
List projects	ASANA_GET_WORKSPACE_PROJECTS	workspace
Create project	ASANA_CREATE_A_PROJECT	workspace, name
Get project	ASANA_GET_A_PROJECT	project_gid
Duplicate project	ASANA_DUPLICATE_PROJECT	project_gid
List sections	ASANA_GET_SECTIONS_IN_PROJECT	project_gid
Create section	ASANA_CREATE_SECTION_IN_PROJECT	project_gid, name
Add to section	ASANA_ADD_TASK_TO_SECTION	section, task
Section tasks	ASANA_GET_TASKS_FROM_A_SECTION	section_gid
List teams	ASANA_GET_TEAMS_IN_WORKSPACE	workspace_gid
Team members	ASANA_GET_USERS_FOR_TEAM	team_gid
Workspace users	ASANA_GET_USERS_FOR_WORKSPACE	workspace_gid
Current user	ASANA_GET_CURRENT_USER	(none)
Parallel requests	ASANA_SUBMIT_PARALLEL_REQUESTS	actions
Weekly Installs
26
Repository
aaaaqwq/claude-…e-skills
GitHub Stars
53
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
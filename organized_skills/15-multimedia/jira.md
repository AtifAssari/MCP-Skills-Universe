---
rating: ⭐⭐
title: jira
url: https://skills.sh/adrianhdezm/atlassian-bridge/jira
---

# jira

skills/adrianhdezm/atlassian-bridge/jira
jira
Installation
$ npx skills add https://github.com/adrianhdezm/atlassian-bridge --skill jira
SKILL.md
Jira (atl CLI)
Prerequisites

Before running any Jira command, verify the CLI is available and authenticated:

Run atl --version. If it fails, stop and tell the user:

The atl CLI is not installed. Install it with npm i -g @ai-foundry/atlassian-bridge and then run atl auth login.

Note: atl is NOT the official Atlassian CLI. It is a community project (@ai-foundry/atlassian-bridge).

Run atl auth status. If not authenticated, stop and tell the user:

You are not logged in. Run atl auth login to authenticate with your Atlassian account.

Only proceed once both checks pass.

Available Commands
Issues
Action	Command
Get	atl jira issues get <issueKey>
Create	atl jira issues create <summary> --project <key> --type <name> [--description <adf>] [--parent <key>] [--labels <csv>]
Update	atl jira issues update <issueKey> [--summary <text>] [--description <adf>] [--parent <key>] [--labels <csv>] [--status <name>]
Delete	atl jira issues delete <issueKey>
Search	atl jira issues search <jql> [--limit <n>] [--cursor <token>] [--fields <csv>]
Children	atl jira issues children <issueKey>
List Attachments	atl jira issues list-attachments <issueKey>
Get Attachment	atl jira issues get-attachment <attachmentId>
Attachments
Action	Command
List	atl jira attachments list <issueKey>
Get	atl jira attachments get <attachmentId>
Comments
Action	Command
List	atl jira comments list <issueKey> [--limit <n>] [--cursor <n>]
Get	atl jira comments get <commentId> --issue <issueKey>
Add	atl jira comments add <issueKey> --body <adf>
Update	atl jira comments update <commentId> --issue <issueKey> --body <adf>
Delete	atl jira comments delete <commentId> --issue <issueKey>
Projects
Action	Command
Get	atl jira projects get <keyOrId>
List	atl jira projects list [--limit <n>] [--cursor <token>] [--query <text>]
Guidelines
When the user mentions an issue, expect a key like PROJ-123. Use it directly with atl jira issues get.
For search, build a valid JQL query from the user's intent (e.g. project = PIXEL AND status = "In Progress" AND assignee = currentUser()).
When creating issues, --project and --type are required. Common types: Task, Bug, Story, Epic, Sub-task.
When creating or updating issues with --description, the value must be valid ADF (Atlassian Document Format) JSON.
When adding or updating comments with --body, the value must be valid ADF JSON. Wrap in single quotes to prevent shell expansion of brackets.
For get, update, and delete on comments, --issue is required to identify which issue the comment belongs to.
Always show the user the command you are about to run before executing it.
Weekly Installs
13
Repository
adrianhdezm/atl…n-bridge
GitHub Stars
1
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass
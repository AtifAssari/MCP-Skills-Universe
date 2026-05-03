---
title: confluence
url: https://skills.sh/adrianhdezm/atlassian-bridge/confluence
---

# confluence

skills/adrianhdezm/atlassian-bridge/confluence
confluence
Installation
$ npx skills add https://github.com/adrianhdezm/atlassian-bridge --skill confluence
SKILL.md
Confluence (atl CLI)
Prerequisites

Before running any Confluence command, verify the CLI is available and authenticated:

Run atl --version. If it fails, stop and tell the user:

The atl CLI is not installed. Install it with npm i -g @ai-foundry/atlassian-bridge and then run atl auth login.

Note: atl is NOT the official Atlassian CLI. It is a community project (@ai-foundry/atlassian-bridge).

Run atl auth status. If not authenticated, stop and tell the user:

You are not logged in. Run atl auth login to authenticate with your Atlassian account.

Only proceed once both checks pass.

Available Commands
Pages
Action	Command
Get	atl confluence pages get <idOrTitle> [--space <key>]
Create	atl confluence pages create <title> --space <id> [--parent <id>] [--body <adf>]
Update	atl confluence pages update <pageId> [--title <title>] [--body <adf>] [--parent <id>]
Delete	atl confluence pages delete <pageId>
Search	atl confluence pages search <cql> [--limit <n>] [--cursor <token>]
Children	atl confluence pages children <idOrTitle> [--space <key>] [--depth <n>]
Spaces
Action	Command
Get	atl confluence spaces get <idOrKey>
Tree	atl confluence spaces tree <idOrKey> [--depth <n>]
Guidelines
When the user provides a page title instead of an ID, use the title directly — the CLI resolves it. Include --space if the user specifies or if disambiguation is needed.
For search, build a valid CQL query from the user's intent (e.g. type=page AND title~"design doc").
When creating or updating pages with --body, the value must be valid ADF (Atlassian Document Format) JSON.
Always show the user the command you are about to run before executing it.
Weekly Installs
12
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
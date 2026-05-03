---
title: composio
url: https://skills.sh/composiohq/skills/composio
---

# composio

skills/composiohq/skills/composio
composio
Installation
$ npx skills add https://github.com/composiohq/skills --skill composio
Summary

Access and automate 1000+ external apps through CLI commands or SDK integration for agents and applications.

Direct CLI access via composio search, composio execute, and composio link for immediate tool use without coding
SDK support for building AI agents and multi-user apps with per-user authentication to external services like Gmail, Slack, GitHub, and Notion
OAuth-based authentication with composio login and non-interactive mode (--no-wait) for headless environments
Real-time event listening via composio listen for trigger-based automation workflows
SKILL.md
When to Apply
User wants to access or interact with external apps (Gmail, Slack, GitHub, Notion, etc.)
User wants to automate a task using an external service (send email, create issue, post message)
Building an AI agent or app that integrates with external tools
Multi-user apps that need per-user connections to external services
Setup

Check if the CLI is installed; if not, install it:

curl -fsSL https://composio.dev/install | bash


After installation, restart your terminal or source your shell config, then authenticate:

composio login       # OAuth; interactive org/project picker (use -y to skip)
composio whoami      # verify org_id, project_id, user_id


For agents without direct browser access: composio login --no-wait | jq to get URL/key, share URL with user, then composio login --key <cli_key> --no-wait once they complete login.

1. Use Apps via Composio CLI

Use this when: The user wants to take action on an external app directly — no code writing needed. The agent uses the CLI to search, connect, and execute tools on behalf of the user.

Key commands (new top-level aliases):

composio search "<query>" — find tools by use case
composio execute "<TOOL_SLUG>" -d '{...<input params>}' — execute a tool
composio link [toolkit] — connect a user account to an app (agents: always use --no-wait for non-interactive mode)
composio listen — listen for real-time trigger events

Typical workflow: search → link (if needed) → execute

Full reference: Composio CLI Guide

2. Building Apps and Agents with Composio

Use this when: Writing code — an AI agent, app, or backend service that integrates with external tools via the Composio SDK.

Run this first inside the project directory to set up the API key:

composio init


Full reference: Building with Composio

Weekly Installs
2.9K
Repository
composiohq/skills
GitHub Stars
53
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail
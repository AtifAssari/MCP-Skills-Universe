---
title: connect
url: https://skills.sh/composiohq/awesome-claude-skills/connect
---

# connect

skills/composiohq/awesome-claude-skills/connect
connect
Installation
$ npx skills add https://github.com/composiohq/awesome-claude-skills --skill connect
Summary

Execute real actions across 1000+ apps instead of generating text about them.

Supports 1000+ integrations including Gmail, Slack, GitHub, Notion, Airtable, HubSpot, Salesforce, and cloud storage services
Handles OAuth authentication automatically on first use, with persistent connections thereafter
Works with Claude Agent SDK, OpenAI Agents, Vercel AI, LangChain, and any MCP-compatible client
Enables chaining multiple actions in sequence, such as querying GitHub issues, summarizing results, and posting to Slack
SKILL.md
Connect

Connect Claude to any app. Stop generating text about what you could do - actually do it.

When to Use This Skill

Use this skill when you need Claude to:

Send that email instead of drafting it
Create that issue instead of describing it
Post that message instead of suggesting it
Update that database instead of explaining how
What Changes
Without Connect	With Connect
"Here's a draft email..."	Sends the email
"You should create an issue..."	Creates the issue
"Post this to Slack..."	Posts it
"Add this to Notion..."	Adds it
Supported Apps

1000+ integrations including:

Email: Gmail, Outlook, SendGrid
Chat: Slack, Discord, Teams, Telegram
Dev: GitHub, GitLab, Jira, Linear
Docs: Notion, Google Docs, Confluence
Data: Sheets, Airtable, PostgreSQL
CRM: HubSpot, Salesforce, Pipedrive
Storage: Drive, Dropbox, S3
Social: Twitter, LinkedIn, Reddit
Setup
1. Get API Key

Get your free key at platform.composio.dev

2. Set Environment Variable
export COMPOSIO_API_KEY="your-key"

3. Install
pip install composio          # Python
npm install @composio/core    # TypeScript


Done. Claude can now connect to any app.

Examples
Send Email
Email sarah@acme.com - Subject: "Shipped!" Body: "v2.0 is live, let me know if issues"

Create GitHub Issue
Create issue in my-org/repo: "Mobile timeout bug" with label:bug

Post to Slack
Post to #engineering: "Deploy complete - v2.4.0 live"

Chain Actions
Find GitHub issues labeled "bug" from this week, summarize, post to #bugs on Slack

How It Works

Uses Composio Tool Router:

You ask Claude to do something
Tool Router finds the right tool (1000+ options)
OAuth handled automatically
Action executes and returns result
Code
from composio import Composio
from claude_agent_sdk.client import ClaudeSDKClient
from claude_agent_sdk.types import ClaudeAgentOptions
import os

composio = Composio(api_key=os.environ["COMPOSIO_API_KEY"])
session = composio.create(user_id="user_123")

options = ClaudeAgentOptions(
    system_prompt="You can take actions in external apps.",
    mcp_servers={
        "composio": {
            "type": "http",
            "url": session.mcp.url,
            "headers": {"x-api-key": os.environ["COMPOSIO_API_KEY"]},
        }
    },
)

async with ClaudeSDKClient(options) as client:
    await client.query("Send Slack message to #general: Hello!")

Auth Flow

First time using an app:

To send emails, I need Gmail access.
Authorize here: https://...
Say "connected" when done.


Connection persists after that.

Framework Support
Framework	Install
Claude Agent SDK	pip install composio claude-agent-sdk
OpenAI Agents	pip install composio openai-agents
Vercel AI	npm install @composio/core @composio/vercel
LangChain	pip install composio-langchain
Any MCP Client	Use session.mcp.url
Troubleshooting
Auth required → Click link, authorize, say "connected"
Action failed → Check permissions in target app
Tool not found → Be specific: "Slack #general" not "send message"
Weekly Installs
1.7K
Repository
composiohq/awes…e-skills
GitHub Stars
57.5K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
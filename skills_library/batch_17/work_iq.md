---
title: work-iq
url: https://skills.sh/rysweet/amplihack/work-iq
---

# work-iq

skills/rysweet/amplihack/work-iq
work-iq
Installation
$ npx skills add https://github.com/rysweet/amplihack --skill work-iq
SKILL.md
Work IQ Skill

Query your Microsoft 365 workspace using natural language. Search emails, meetings, Teams messages, and documents without leaving your development environment.

Quick Start
0. Enable MCP Server (Required First)

The workiq MCP server is disabled by default. Enable it before use:

/mcp-manager


Select the workiq server and enable it, or manually set "disabled": false in .mcp.json.

1. Accept EULA (Required First)
npx @microsoft/workiq accept-eula

2. Configure MCP

Add to your project's .mcp.json:

{
  "mcpServers": {
    "workiq": {
      "command": "npx",
      "args": ["-y", "@microsoft/workiq", "mcp"]
    }
  }
}

3. Authenticate

First query triggers M365 authentication - a browser window opens for sign-in.

4. Start Querying
"What meetings do I have tomorrow?"
"Find emails from Sarah about the budget"
"Show Teams messages about the deployment"

Core Capabilities
Email Intelligence
Find emails by sender, recipient, subject, or content
Filter by date ranges
Search across inbox, sent items, and archives

Example: "What did John say about the proposal?"

Calendar & Meetings
View upcoming meetings
Search past meetings by title or attendees
Check your schedule

Example: "What's on my calendar this week?"

Teams Messages
Search conversations across channels
Find messages by sender or content
Locate shared files

Example: "Summarize today's messages in Engineering channel"

Document Search
Query SharePoint and OneDrive content
Search by file type, author, or content
Find recently modified documents

Example: "Find my recent PowerPoint presentations"

When This Skill Activates

I load automatically when you mention:

work iq, workiq, m365, microsoft 365
check my email, find meetings, search teams
query calendar, office 365, o365
CLI Commands
Command	Description
workiq accept-eula	Accept End User License Agreement (required first)
workiq ask	Interactive query mode
workiq ask -q "..."	Ask a specific question
workiq mcp	Start MCP server (used by Claude Code)
workiq version	Show version info
Prerequisites
Microsoft 365 Account - Active M365 subscription
Node.js - For npx command
Admin Consent - May be required for some M365 tenants
Quick Troubleshooting
Problem	Solution
"EULA not accepted"	Run npx @microsoft/workiq accept-eula
"Authentication failed"	Re-run query to trigger fresh auth flow
"Admin consent required"	Contact your M365 tenant administrator
"WSL browser issues"	Install xdg-utils and wslu packages
Documentation
Technical Reference - Installation, configuration, authentication
Usage Examples - Real-world query patterns
Platform Support
Windows (x64, arm64)
macOS (x64, arm64)
Linux (x64, arm64)
WSL (with browser support)

References:

Work IQ GitHub
NPM Package
Admin Consent Overview

Version: 1.0.0 | Updated: 2026-01-23

Weekly Installs
99
Repository
rysweet/amplihack
GitHub Stars
55
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
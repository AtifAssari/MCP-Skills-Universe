---
title: setup-api-key
url: https://skills.sh/vapiai/skills/setup-api-key
---

# setup-api-key

skills/vapiai/skills/setup-api-key
setup-api-key
Installation
$ npx skills add https://github.com/vapiai/skills --skill setup-api-key
SKILL.md
Vapi API Key Setup

Guide the user through obtaining and configuring a Vapi API key for the voice AI platform.

Workflow
Step 1: Request the API key

Tell the user:

To set up Vapi, open the API keys page in the Vapi Dashboard: https://dashboard.vapi.ai/org/api-keys

(Need an account? Create one at https://dashboard.vapi.ai/signup first)

If you don't have an API key yet:

Click "Create Key"
Name your key (e.g., "development")
Copy the key immediately — it is only shown once

Paste your API key here when ready.

Then wait for the user's next message which should contain the API key.

Step 2: Validate and configure

Once the user provides the API key:

Validate the key by making a request:

curl -s -o /dev/null -w "%{http_code}" https://api.vapi.ai/assistant \
  -H "Authorization: Bearer <the-api-key>"


If validation fails (non-200 response):

Tell the user the API key appears to be invalid
Ask them to double-check and try again
Remind them of the URL: https://dashboard.vapi.ai/org/api-keys

If validation succeeds (200 response), save the API key:

Check if a .env file exists. If so, append to it. If not, create one:

VAPI_API_KEY=<the-api-key>


Confirm success:

Your Vapi API key is configured and stored in .env as VAPI_API_KEY.

You can now use Vapi's API to create assistants, make calls, and build voice AI agents.

Keep this key safe — do not commit it to version control.

Step 3: Verify .gitignore

Check if .gitignore exists and contains .env. If not, add it:

.env

Environment Variable

All Vapi skills expect the API key in the VAPI_API_KEY environment variable. The base URL for all API requests is:

https://api.vapi.ai


Authentication is via Bearer token:

Authorization: Bearer $VAPI_API_KEY

Additional Resources

This skills repository includes a Vapi documentation MCP server (vapi-docs) that gives your AI agent access to the full Vapi knowledge base. Use the searchDocs tool to look up anything beyond what this skill covers — advanced configuration, troubleshooting, SDK details, and more.

Auto-configured: If you cloned or installed these skills, the MCP server is already configured via .mcp.json (Claude Code), .cursor/mcp.json (Cursor), or .vscode/mcp.json (VS Code Copilot).

Manual setup: If your agent doesn't auto-detect the config, run:

claude mcp add vapi-docs -- npx -y mcp-remote https://docs.vapi.ai/_mcp/server


See the README for full setup instructions across all supported agents.

Weekly Installs
464
Repository
vapiai/skills
GitHub Stars
39
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail
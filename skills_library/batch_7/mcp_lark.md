---
title: mcp-lark
url: https://skills.sh/aahl/skills/mcp-lark
---

# mcp-lark

skills/aahl/skills/mcp-lark
mcp-lark
Installation
$ npx skills add https://github.com/aahl/skills --skill mcp-lark
SKILL.md
MCP Lark / FeiShu

Need to login to the Lark MCP Configuration Platform to add MCP services, obtain the MCP URL, and configure it into environment variables.

Lark MCP docs: https://open.larksuite.com/document/mcp_open_tools/call-feishu-mcp-server-in-remote-mode
飞书 MCP 文档: https://open.feishu.cn/document/mcp_open_tools/end-user-call-remote-mcp-server
Environment variables

Prioritize fetching from .env under the workspace, then use system environment variables. If not configured, ask the user for input and update it to .env.

# Configure multiple MCP service URLs and usage scenarios in environment variables
LARK_MCP_SERVERS='
open.larksuite.com/mcp/stream/xxx:Chats and Mails;
open.larksuite.com/mcp/stream/yyy:Cloud documents;
'

List of available tools
npx -y mcporter list 'open.larksuite.com/mcp/stream/<token>' --all-parameters

# Get the schema of the specified tool
npx -y mcporter list 'open.larksuite.com/mcp/stream/<token>' --json | jq '.tools[] | select(.name == "<tool_name>")'

Call specified tool
npx -y mcporter call 'open.larksuite.com/mcp/stream/<token>.<tool_name>' param1:"value1" foo:"bar"

References
Sent message content: references/message_create.md
About mcporter

To improve compatibility, use npx -y mcporter instead of mcporter when executing commands.

Weekly Installs
876
Repository
aahl/skills
GitHub Stars
120
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail
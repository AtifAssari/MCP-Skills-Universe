---
rating: ⭐⭐⭐
title: create-mcp-servers
url: https://skills.sh/glittercowboy/taches-cc-resources/create-mcp-servers
---

# create-mcp-servers

skills/glittercowboy/taches-cc-resources/create-mcp-servers
create-mcp-servers
Installation
$ npx skills add https://github.com/glittercowboy/taches-cc-resources --skill create-mcp-servers
SKILL.md

<essential_principles>

<the_5_rules> Every MCP server must follow these:

Never Hardcode Secrets - Use ${VAR} expansion in configs, environment variables in code
Use cwd Property - Isolates dependencies (not --cwd in args)
Always Absolute Paths - which uv to find paths, never relative
One Server Per Directory - ~/Developer/mcp/{server-name}/
Use uv for Python - Better than pip, handles venvs automatically </the_5_rules>

<security_checklist>

Never ask user to paste secrets into chat
Always use environment variables for credentials
Use ${VAR} expansion in configs
Provide exact commands for user to run in terminal
Verify environment variable existence without showing values
Never hardcode API keys in code or configs </security_checklist>

<architecture_decision> Operation count determines architecture:

1-2 operations → Traditional pattern (flat tools)
3+ operations → On-demand discovery pattern (meta-tools)

Traditional: Each operation is a separate tool On-demand: 4 meta-tools (discover, get_schema, execute, continue) + operations.json </architecture_decision>

Standard location: ~/Developer/mcp/{server-name}/

</essential_principles>

No context provided (skill invoked without description): Use AskUserQuestion:

header: "Mode"
question: "What would you like to do?"
options:
"Create a new MCP server" → workflows/create-new-server.md
"Update an existing MCP server" → workflows/update-existing-server.md
"Troubleshoot a server" → workflows/troubleshoot-server.md

Context provided (user described what they want): Route directly to workflows/create-new-server.md

<workflows_index>

Workflow	Purpose
create-new-server.md	Full 8-step workflow from intake to verification
update-existing-server.md	Modify or extend an existing server
troubleshoot-server.md	Diagnose and fix connection/runtime issues
</workflows_index>	

<templates_index>

Template	Purpose
python-server.py	Traditional pattern starter for Python
typescript-server.ts	Traditional pattern starter for TypeScript
operations.json	On-demand discovery operations definition
</templates_index>	

<scripts_index>

Script	Purpose
setup-python-project.sh	Initialize Python MCP project with uv
setup-typescript-project.sh	Initialize TypeScript MCP project with npm
</scripts_index>	

<references_index> Core workflow:

creation-workflow.md - Complete step-by-step with exact commands

Architecture patterns:

traditional-pattern.md - For 1-2 operations (flat tools)
large-api-pattern.md - For 3+ operations (on-demand discovery)

Language-specific:

python-implementation.md - Async patterns, type hints
typescript-implementation.md - Type safety, SDK features

Advanced topics:

oauth-implementation.md - OAuth with stdio isolation
response-optimization.md - Field truncation, pagination
tools-and-resources.md - Resources API, prompts, streaming
testing-and-deployment.md - Unit tests, packaging, publishing
validation-checkpoints.md - All validation checks
adaptive-questioning-guide.md - Question templates for intake
api-research-template.md - API research document format </references_index>

<quick_reference>

# List servers
claude mcp list

# Add server (Python)
claude mcp add --transport stdio <name> \
  --env API_KEY='${API_KEY}' \
  -- uv --directory ~/Developer/mcp/<name> run python -m src.server

# Add server (TypeScript)
claude mcp add --transport stdio <name> \
  --env API_KEY='${API_KEY}' \
  -- node ~/Developer/mcp/<name>/build/index.js

# Remove server
claude mcp remove <name>

# Check logs
tail -f ~/Library/Logs/Claude/mcp-server-<name>.log

# Find paths
which uv && which node && which python


</quick_reference>

<troubleshooting_quick> Server not appearing: Check claude mcp list, verify config in ~/.claude/settings.json

"command not found": Use absolute paths from which uv / which node

Environment variable not found:

echo $MY_API_KEY  # Check if set
echo 'export MY_API_KEY="value"' >> ~/.zshrc && source ~/.zshrc


Secrets visible in conversation: STOP. Delete conversation. Rotate credentials. Never paste secrets in chat.

Full troubleshooting: workflows/troubleshoot-server.md </troubleshooting_quick>

<success_criteria> A production-ready MCP server has:

Valid configuration in Claude Code (claude mcp list shows ✓ Connected)
Valid configuration in Claude Desktop config
Environment variables set securely in ~/.zshrc
Architecture matches operation count
OAuth stdio isolation if applicable
Response optimization for list/search operations
All validation checkpoints passed
No errors in logs </success_criteria>
Weekly Installs
88
Repository
glittercowboy/t…esources
GitHub Stars
1.9K
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
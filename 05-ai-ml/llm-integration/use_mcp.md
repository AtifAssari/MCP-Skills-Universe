---
title: use-mcp
url: https://skills.sh/duc01226/easyplatform/use-mcp
---

# use-mcp

skills/duc01226/easyplatform/use-mcp
use-mcp
Installation
$ npx skills add https://github.com/duc01226/easyplatform --skill use-mcp
SKILL.md

[IMPORTANT] Use TaskCreate to break ALL work into small tasks BEFORE starting — including tasks for each file read. This prevents context loss from long files. For simple tasks, AI MUST ATTENTION ask user whether to skip.

Quick Summary

Goal: Utilize MCP (Model Context Protocol) server tools to extend Claude's capabilities.

Workflow:

Discover -- List available MCP tools and their capabilities
Select -- Choose appropriate tool for the task
Execute -- Run MCP tool with correct parameters

Key Rules:

Check available MCP servers before attempting to use tools
Use MCP tools for capabilities not available in built-in tools
Handle MCP tool errors gracefully with fallback approaches

Be skeptical. Apply critical thinking, sequential thinking. Every claim needs traced proof, confidence percentages (Idea should be more than 80%).

Execute MCP operations via Gemini CLI to preserve context budget.

Execution Steps

Execute task via Gemini CLI (using stdin pipe for MCP support):

# IMPORTANT: Use stdin piping, NOT -p flag (deprecated, skips MCP init)
echo "$ARGUMENTS. Return JSON only per GEMINI.md instructions." | gemini -y -m gemini-2.5-flash


Fallback to general-purpose subagent (if Gemini CLI unavailable):

Use general-purpose subagent to discover and execute tools
If the subagent got issues with the scripts of mcp-management skill, use mcp-builder skill to fix them
DO NOT create ANY new scripts
The subagent can only use MCP tools if any to achieve this task
If the subagent can't find any suitable tools, just report it back to the main agent to move on to the next step
Important Notes
MUST ATTENTION use stdin piping - the deprecated -p flag skips MCP initialization
Use -y flag to auto-approve tool execution
GEMINI.md auto-loaded: Gemini CLI automatically loads GEMINI.md from project root, enforcing JSON-only response format
Parseable output: Responses are structured JSON: {"server":"name","tool":"name","success":true,"result":<data>,"error":null}
Anti-Pattern (DO NOT USE)
# BROKEN - deprecated -p flag skips MCP server connections!
gemini -y -m gemini-2.5-flash -p "..."

Closing Reminders
IMPORTANT MUST ATTENTION break work into small todo tasks using TaskCreate BEFORE starting
IMPORTANT MUST ATTENTION search codebase for 3+ similar patterns before creating new code
IMPORTANT MUST ATTENTION cite file:line evidence for every claim (confidence >80% to act)
IMPORTANT MUST ATTENTION add a final review todo task to verify work quality
Weekly Installs
36
Repository
duc01226/easyplatform
GitHub Stars
6
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass
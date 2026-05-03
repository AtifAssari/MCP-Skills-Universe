---
title: copilotkit
url: https://skills.sh/copilotkit/skills/copilotkit
---

# copilotkit

skills/copilotkit/skills/copilotkit
copilotkit
Installation
$ npx skills add https://github.com/copilotkit/skills --skill copilotkit
SKILL.md

Route to the appropriate sub-skill based on the user's task. If the task is ambiguous, ask one clarifying question before routing.

Quickstart (default path)

If the user wants to add CopilotKit to their project, or the request is general/unclear, route here:

copilotkit-setup — Install packages, configure the runtime, wire up the provider, get a working chat UI.

Routing Table
Task	Sub-skill
Initial setup, installation, adding CopilotKit to a project	copilotkit-setup
Building features — frontend tools, shared state, generative UI, actions	copilotkit-develop
Connecting agent frameworks — LangGraph, CrewAI, Mastra, Pydantic AI, etc.	copilotkit-integrations
Debugging errors, fixing runtime issues, troubleshooting	copilotkit-debug
Upgrading versions, migrating between APIs	copilotkit-upgrade
AG-UI protocol — building custom backends, event streaming, debugging protocol issues	copilotkit-agui
Contributing to the CopilotKit repo	copilotkit-contribute
Update/refresh these skills, skills seem stale or wrong	copilotkit-self-update
MCP Documentation Server

The copilotkit-docs MCP server at mcp.copilotkit.ai/mcp provides live documentation search. Use its tools for up-to-date reference material:

search-docs — search CopilotKit documentation by topic
search-code — search CopilotKit source code and examples
search-ag-ui-docs — search AG-UI protocol documentation
search-ag-ui-code — search AG-UI TypeScript SDK source

Prefer MCP lookups over hardcoded knowledge when answering specific API or configuration questions.

Weekly Installs
239
Repository
copilotkit/skills
GitHub Stars
22
First Seen
Mar 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn
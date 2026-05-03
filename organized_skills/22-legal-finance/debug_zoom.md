---
rating: ⭐⭐
title: debug-zoom
url: https://skills.sh/anthropics/knowledge-work-plugins/debug-zoom
---

# debug-zoom

skills/anthropics/knowledge-work-plugins/debug-zoom
debug-zoom
Installation
$ npx skills add https://github.com/anthropics/knowledge-work-plugins --skill debug-zoom
SKILL.md
/debug-zoom

If you see unfamiliar placeholders or need to check which tools are connected, see CONNECTORS.md.

Debug Zoom auth, API, webhook, SDK, or MCP issues without wandering through the entire docs set.

Usage
/debug-zoom $ARGUMENTS

Workflow
Identify the failing layer: auth, API request, webhook, SDK init, media/session behavior, or MCP transport.
Ask for the minimum missing evidence: exact error, platform, request/response, event payload, or code path.
Produce 2-4 plausible causes ranked by likelihood.
Route to the most relevant deep references in skills/.
Give a short verification plan so the user can confirm the fix.
Output
Most likely failure layer
Ranked hypotheses
Targeted fix steps
Verification checklist
Relevant skill links
Related Skills
debug-zoom-integration
setup-zoom-oauth
design-mcp-workflow
Weekly Installs
294
Repository
anthropics/know…-plugins
GitHub Stars
11.7K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
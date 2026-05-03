---
rating: ⭐⭐
title: choose-zoom-approach
url: https://skills.sh/anthropics/knowledge-work-plugins/choose-zoom-approach
---

# choose-zoom-approach

skills/anthropics/knowledge-work-plugins/choose-zoom-approach
choose-zoom-approach
Installation
$ npx skills add https://github.com/anthropics/knowledge-work-plugins --skill choose-zoom-approach
SKILL.md
Choose Zoom Approach

Pick the smallest correct Zoom surface for the job, then layer in only the supporting pieces that are actually required.

Decision Framework
Problem Type	Primary Zoom Surface
Deterministic backend automation, account management, reporting, scheduled jobs	rest-api
Event delivery to your backend	webhooks or websockets
Embed Zoom meetings into your app	meeting-sdk
Build a fully custom video experience	video-sdk
Build inside the Zoom client	zoom-apps-sdk
AI-agent tool workflows over Zoom data	zoom-mcp
Real-time media extraction or meeting bots	rtms plus meeting-sdk when needed
Phone workflows	phone
Contact Center or Virtual Agent flows	contact-center or virtual-agent
Guardrails
Do not recommend Video SDK when the user actually needs Zoom meeting semantics.
Do not recommend Meeting SDK when the user needs a fully custom session product.
Do not replace deterministic backend automation with MCP-only guidance.
Prefer hybrid rest-api + zoom-mcp when the user needs both stable system actions and AI-driven discovery.
What To Produce
One recommended path
Minimum supporting components
Hard constraints and tradeoffs
Immediate next implementation step
Weekly Installs
291
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
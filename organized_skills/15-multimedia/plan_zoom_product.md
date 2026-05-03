---
rating: ⭐⭐
title: plan-zoom-product
url: https://skills.sh/anthropics/knowledge-work-plugins/plan-zoom-product
---

# plan-zoom-product

skills/anthropics/knowledge-work-plugins/plan-zoom-product
plan-zoom-product
Installation
$ npx skills add https://github.com/anthropics/knowledge-work-plugins --skill plan-zoom-product
SKILL.md
/plan-zoom-product

If you see unfamiliar placeholders or need to check which tools are connected, see CONNECTORS.md.

Choose between Zoom REST API, Webhooks, WebSockets, Meeting SDK, Video SDK, Zoom Apps SDK, Phone, Contact Center, or MCP for a specific use case.

Usage
/plan-zoom-product $ARGUMENTS

Workflow
Identify the user's actual goal.
Classify whether the problem is automation, embedded meetings, custom video, in-client app behavior, event delivery, AI tooling, or support/phone/contact-center work.
If the request is ambiguous, ask one short clarifier before locking the recommendation.
Recommend the primary Zoom surface and list the minimum supporting pieces.
Explain why the rejected alternatives are worse for this case.
End with a concrete next-step plan.
Output
Recommended Zoom surface
Supporting components required
Key tradeoffs and constraints
Suggested implementation sequence
Relevant skill links for the next step
Related Skills
start
choose-zoom-approach
design-mcp-workflow
Weekly Installs
296
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
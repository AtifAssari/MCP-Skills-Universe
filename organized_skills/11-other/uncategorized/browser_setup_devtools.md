---
rating: ⭐⭐
title: browser-setup-devtools
url: https://skills.sh/different-ai/openwork/browser-setup-devtools
---

# browser-setup-devtools

skills/different-ai/openwork/browser-setup-devtools
browser-setup-devtools
Installation
$ npx skills add https://github.com/different-ai/openwork --skill browser-setup-devtools
SKILL.md
Browser automation setup (Chrome DevTools MCP)
Principles
Keep prompts minimal; do as much as possible with tools and commands.
Use Chrome DevTools MCP only.
Workflow
Ask: "Do you have Chrome installed on this computer?"
If no or unsure:
Offer to open the download page yourself and do it if possible.
Provide a clickable link: https://www.google.com/chrome/
Continue after installation is confirmed.
Check DevTools MCP availability:
Call chrome-devtools_list_pages.
If pages exist, select one with chrome-devtools_select_page.
If no pages, create one with chrome-devtools_new_page (use https://example.com) and then select it.
If DevTools MCP calls fail:
Ask the user to open Chrome and keep it running.
Retry chrome-devtools_list_pages.
If it still fails, ensure opencode.jsonc includes mcp["chrome-devtools"] with command ['npx', '-y', 'chrome-devtools-mcp@latest'] and ask the user to restart OpenWork/OpenCode.
Retry the DevTools MCP check.
If DevTools MCP is ready:
Offer a first task ("Let's try opening a webpage").
If yes, use chrome-devtools_navigate_page or chrome-devtools_new_page to open the URL and confirm completion.
Response rules
Keep each user prompt to one short sentence when possible.
Use direct offers like "I can open Chrome now" and follow with tool actions.
Always present links as clickable URLs.
Weekly Installs
92
Repository
different-ai/openwork
GitHub Stars
14.6K
First Seen
2 days ago
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn
---
title: browser
url: https://skills.sh/cexll/myclaude/browser
---

# browser

skills/cexll/myclaude/browser
browser
Installation
$ npx skills add https://github.com/cexll/myclaude --skill browser
SKILL.md
Browser Automation

Minimal Chrome DevTools Protocol (CDP) helpers for browser automation without MCP server setup.

Setup

Install dependencies before first use:

npm install --prefix ~/.claude/skills/browser/browser ws

Scripts

All scripts connect to Chrome on localhost:9222.

start.js - Launch Chrome
scripts/start.js              # Fresh profile
scripts/start.js --profile    # Use persistent profile (keeps cookies/auth)

nav.js - Navigate
scripts/nav.js https://example.com        # Navigate current tab
scripts/nav.js https://example.com --new  # Open in new tab

eval.js - Execute JavaScript
scripts/eval.js 'document.title'
scripts/eval.js '(() => { const x = 1; return x + 1; })()'


Use single expressions or IIFE for multiple statements.

screenshot.js - Capture Screenshot
scripts/screenshot.js


Returns { path, filename } of saved PNG in temp directory.

pick.js - Visual Element Picker
scripts/pick.js "Click the submit button"


Returns element metadata: tag, id, classes, text, href, selector, rect.

Workflow
Launch Chrome: scripts/start.js --profile for authenticated sessions
Navigate: scripts/nav.js <url>
Inspect: scripts/eval.js 'document.querySelector(...)'
Capture: scripts/screenshot.js or scripts/pick.js
Return gathered data
Key Points
All operations run locally - credentials never leave the machine
Use --profile flag to preserve cookies and auth tokens
Scripts return structured JSON for agent consumption
Weekly Installs
172
Repository
cexll/myclaude
GitHub Stars
2.6K
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
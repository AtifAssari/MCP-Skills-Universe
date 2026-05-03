---
title: browser
url: https://skills.sh/iamzhihuix/happy-claude-skills/browser
---

# browser

skills/iamzhihuix/happy-claude-skills/browser
browser
Installation
$ npx skills add https://github.com/iamzhihuix/happy-claude-skills --skill browser
SKILL.md
Browser Tools

Minimal CDP tools for collaborative site exploration and scraping.

Credits: Based on Mario Zechner's article What if you don't need MCP?, adapted from Factory.ai.

Setup

Before first use, install dependencies:

npm install --prefix skills/browser

Start Chrome
./skills/browser/scripts/start.js              # Fresh profile
./skills/browser/scripts/start.js --profile    # Copy your profile (cookies, logins)


Start Chrome on :9222 with remote debugging.

Navigate
./skills/browser/scripts/nav.js https://example.com
./skills/browser/scripts/nav.js https://example.com --new


Navigate current tab or open new tab.

Evaluate JavaScript
./skills/browser/scripts/eval.js 'document.title'
./skills/browser/scripts/eval.js 'document.querySelectorAll("a").length'


Execute JavaScript in active tab (async context).

IMPORTANT: The code must be a single expression or use IIFE for multiple statements:

Single expression: 'document.title'
Multiple statements: '(() => { const x = 1; return x + 1; })()'
Avoid newlines in the code string - keep it on one line
Screenshot
./skills/browser/scripts/screenshot.js


Screenshot current viewport, returns temp file path.

Pick Elements
./skills/browser/scripts/pick.js "Click the submit button"


Interactive element picker. Click to select, Cmd/Ctrl+Click for multi-select, Enter to finish.

Workflow
Start Chrome with start.js --profile to mirror your authenticated state.
Drive navigation via nav.js https://target.app or open secondary tabs with --new.
Inspect the DOM using eval.js for quick counts, attribute checks, or extracting JSON payloads.
Capture artifacts with screenshot.js for visual proof or pick.js when you need precise selectors or text snapshots.
Usage Notes
Start Chrome first before using other tools
The --profile flag syncs your actual Chrome profile so you're logged in everywhere
JavaScript evaluation runs in an async context in the page
Pick tool allows you to visually select DOM elements by clicking on them
Weekly Installs
224
Repository
iamzhihuix/happ…e-skills
GitHub Stars
284
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn
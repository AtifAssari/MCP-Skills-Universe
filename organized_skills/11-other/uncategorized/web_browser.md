---
rating: ⭐⭐⭐
title: web-browser
url: https://skills.sh/mitsuhiko/agent-stuff/web-browser
---

# web-browser

skills/mitsuhiko/agent-stuff/web-browser
web-browser
Installation
$ npx skills add https://github.com/mitsuhiko/agent-stuff --skill web-browser
SKILL.md
Web Browser Skill

Minimal CDP tools for collaborative site exploration.

Start Chrome
./scripts/start.js                  # Isolated reusable profile (default)
./scripts/start.js --profile        # Copy your profile into isolated cache
./scripts/start.js --reset-profile  # Clear selected cached profile before launch


Starts Chrome with remote debugging (default port :9222).

Profile behavior:

Default mode uses: ~/.cache/agent-web/browser/fresh-profile
--profile mode uses: ~/.cache/agent-web/browser/profile-copy
The skill does not attach to your live Chrome profile directly
If :9222 is already used by an unknown instance, start will fail instead of reusing it

If Chrome is installed in a non-standard location, set:

BROWSER_BIN=/path/to/chrome ./scripts/start.js


Optional debug endpoint override:

BROWSER_DEBUG_PORT=9333 ./scripts/start.js

Navigate
./scripts/nav.js https://example.com
./scripts/nav.js https://example.com --new


Navigate current tab or open new tab.

Device Emulation (Mobile)
./scripts/emulate.js --list
./scripts/emulate.js iphone-14
./scripts/emulate.js pixel-7 --landscape
./scripts/emulate.js --reset


Set an active device emulation preference (viewport, DPR, touch, UA) for browser skill commands. Use --reset to clear.

Commands like nav.js, eval.js, pick.js, dismiss-cookies.js, and screenshot.js automatically apply the active preference.

Evaluate JavaScript
./scripts/eval.js 'document.title'
./scripts/eval.js 'document.querySelectorAll("a").length'
./scripts/eval.js 'JSON.stringify(Array.from(document.querySelectorAll("a")).map(a => ({ text: a.textContent.trim(), href: a.href })).filter(link => !link.href.startsWith("https://")))'


Execute JavaScript in active tab (async context). Be careful with string escaping, best to use single quotes.

Screenshot
./scripts/screenshot.js
./scripts/screenshot.js --full-page
./scripts/screenshot.js --device iphone-14
./scripts/screenshot.js --device pixel-7 --full-page


Takes a screenshot and returns a temp file path.

Default: current viewport
--full-page: captures full document height
--device <preset>: temporary mobile emulation for that screenshot only
Pick Elements
./scripts/pick.js "Click the submit button"


Interactive element picker. Click to select, Cmd/Ctrl+Click for multi-select, Enter to finish.

Dismiss Cookie Dialogs
./scripts/dismiss-cookies.js          # Accept cookies
./scripts/dismiss-cookies.js --reject # Reject cookies (where possible)


Automatically dismisses EU cookie consent dialogs.

Run after navigating to a page:

./scripts/nav.js https://example.com && ./scripts/dismiss-cookies.js

Quick Mobile Debug Flow
./scripts/start.js
./scripts/nav.js https://example.com
./scripts/emulate.js iphone-14
./scripts/nav.js https://example.com      # reload with mobile UA
./scripts/dismiss-cookies.js
./scripts/screenshot.js --full-page

Background Logging (Console + Errors + Network)

Automatically started by start.js and writes JSONL logs to:

~/.cache/agent-web/logs/YYYY-MM-DD/<targetId>.jsonl


Manually start:

./scripts/watch.js


Tail latest log:

./scripts/logs-tail.js           # dump current log and exit
./scripts/logs-tail.js --follow  # keep following


Summarize network responses:

./scripts/net-summary.js

Weekly Installs
339
Repository
mitsuhiko/agent-stuff
GitHub Stars
2.2K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykWarn
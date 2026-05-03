---
title: chrome-cdp
url: https://skills.sh/pasky/chrome-cdp-skill/chrome-cdp
---

# chrome-cdp

skills/pasky/chrome-cdp-skill/chrome-cdp
chrome-cdp
Installation
$ npx skills add https://github.com/pasky/chrome-cdp-skill --skill chrome-cdp
Summary

Lightweight Chrome DevTools Protocol CLI for inspecting and interacting with local browser tabs via WebSocket.

Connects directly to Chrome/Chromium/Brave/Edge with remote debugging enabled; no Puppeteer dependency, supports 100+ tabs with instant connection
Core commands: list tabs, shot (viewport screenshots), snap (accessibility tree), eval (JavaScript), click/clickxy (interactions), type (text input), nav (navigation), html (DOM extraction), net (resource timing)
Handles coordinate conversion between native image pixels and CSS pixels via device pixel ratio (DPR); clickxy takes CSS pixel coordinates
Requires Node.js 22+, Chrome with remote debugging enabled via chrome://inspect/#remote-debugging, and optional CDP_PORT_FILE env var for non-standard DevToolsActivePort locations
Background daemon persists sessions for 20 minutes, eliminating repeated "Allow debugging" prompts after first tab access
SKILL.md
Chrome CDP

Lightweight Chrome DevTools Protocol CLI. Connects directly via WebSocket — no Puppeteer, works with 100+ tabs, instant connection.

Prerequisites
Chrome (or Chromium, Brave, Edge, Vivaldi) with remote debugging enabled: open chrome://inspect/#remote-debugging and toggle the switch
Node.js 22+ (uses built-in WebSocket)
If your browser's DevToolsActivePort is in a non-standard location, set CDP_PORT_FILE to its full path
Commands

All commands use scripts/cdp.mjs. The <target> is a unique targetId prefix from list; copy the full prefix shown in the list output (for example 6BE827FA). The CLI rejects ambiguous prefixes.

List open pages
scripts/cdp.mjs list

Take a screenshot
scripts/cdp.mjs shot <target> [file]    # default: screenshot-<target>.png in runtime dir


Captures the viewport only. Scroll first with eval if you need content below the fold. Output includes the page's DPR and coordinate conversion hint (see Coordinates below).

Accessibility tree snapshot
scripts/cdp.mjs snap <target>

Evaluate JavaScript
scripts/cdp.mjs eval <target> <expr>


Watch out: avoid index-based selection (querySelectorAll(...)[i]) across multiple eval calls when the DOM can change between them (e.g. after clicking Ignore, card indices shift). Collect all data in one eval or use stable selectors.

Other commands
scripts/cdp.mjs html    <target> [selector]   # full page or element HTML
scripts/cdp.mjs nav     <target> <url>         # navigate and wait for load
scripts/cdp.mjs net     <target>               # resource timing entries
scripts/cdp.mjs click   <target> <selector>    # click element by CSS selector
scripts/cdp.mjs clickxy <target> <x> <y>       # click at CSS pixel coords
scripts/cdp.mjs type    <target> <text>         # Input.insertText at current focus; works in cross-origin iframes unlike eval
scripts/cdp.mjs loadall <target> <selector> [ms]  # click "load more" until gone (default 1500ms between clicks)
scripts/cdp.mjs evalraw <target> <method> [json]  # raw CDP command passthrough
scripts/cdp.mjs open    [url]                  # open new tab (each triggers Allow prompt)
scripts/cdp.mjs stop    [target]               # stop daemon(s)

Coordinates

shot saves an image at native resolution: image pixels = CSS pixels × DPR. CDP Input events (clickxy etc.) take CSS pixels.

CSS px = screenshot image px / DPR


shot prints the DPR for the current page. Typical Retina (DPR=2): divide screenshot coords by 2.

Tips
Prefer snap --compact over html for page structure.
Use type (not eval) to enter text in cross-origin iframes — click/clickxy to focus first, then type.
Chrome shows an "Allow debugging" modal once per tab on first access. A background daemon keeps the session alive so subsequent commands need no further approval. Daemons auto-exit after 20 minutes of inactivity.
Weekly Installs
1.5K
Repository
pasky/chrome-cdp-skill
GitHub Stars
3.0K
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
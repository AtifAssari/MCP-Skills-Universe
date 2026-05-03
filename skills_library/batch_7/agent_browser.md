---
title: agent browser
url: https://skills.sh/am-will/codex-skills/agent-browser
---

# agent browser

skills/am-will/codex-skills/Agent Browser
Agent Browser
Installation
$ npx skills add https://github.com/am-will/codex-skills --skill 'Agent Browser'
Summary

Fast Rust-based headless browser automation with real Chrome profile and session support.

Supports headless Chromium, real Chrome with profile/OAuth reuse via Chrome DevTools Protocol, and persistent session cookies for logged-in workflows
30+ commands covering navigation, interaction (click, type, fill, drag, upload), extraction (text, HTML, attributes, screenshots), and state checks
Deterministic element selection via snapshot refs (@e1, @e2, etc.) and semantic finders (role, text, label, placeholder, testid)
Multi-session isolation for parallel automation and advanced features including frame navigation, JavaScript evaluation, dialog handling, and network-aware waits
JSON output mode and --headed debugging for agent integration and troubleshooting
SKILL.md
Agent Browser

A fast Rust-based headless browser automation CLI with Node.js fallback that enables AI agents to navigate, click, type, and snapshot pages via structured commands.

Installation
npm recommended
npm install -g agent-browser
agent-browser install
agent-browser install --with-deps

From Source
git clone https://github.com/vercel-labs/agent-browser
cd agent-browser
pnpm install
pnpm build
agent-browser install

Quick Start
agent-browser open example.com
agent-browser snapshot
agent-browser click @e2
agent-browser fill @e3 "test@example.com"
agent-browser get text @e1
agent-browser screenshot page.png
agent-browser close

Using Real Chrome Profile (for OAuth/Logged-in Sessions)

For sites requiring Google/Discord/etc login (like star-swap.com):

Method 1: Launch Chrome with custom profile, connect via CDP

# Terminal 1: Launch Chrome with your real profile and remote debugging
google-chrome --remote-debugging-port=9222 --user-data-dir=/home/willr/.config/google-chrome/Default &

# Terminal 2: Connect agent-browser to that Chrome instance
agent-browser --cdp 9222 open "https://star-swap.com"
agent-browser --cdp 9222 snapshot -i
agent-browser --cdp 9222 click e2

# This reuses your existing Google session - no re-login needed!
# Works for: Google OAuth, Discord OAuth, any site you're logged into in Chrome


Method 2: Session persistence (first-time manual login)

# First time: headed mode, login manually
agent-browser --headed --session starswap open "https://star-swap.com"
# Complete Google OAuth manually in the browser window
# Close when done

# Future runs: cookies persist!
agent-browser --session starswap open "https://star-swap.com"
# Already logged in automatically


am.will.ryan Chrome profile: /home/willr/.config/google-chrome/Default

Core Commands
Navigation
agent-browser open <url>
agent-browser back
agent-browser forward
agent-browser reload

Interaction
agent-browser click <sel>
agent-browser dblclick <sel>
agent-browser focus <sel>
agent-browser type <sel> <text>
agent-browser fill <sel> <text>
agent-browser clear <sel>
agent-browser press <key>
agent-browser keydown <key>
agent-browser keyup <key>
agent-browser hover <sel>
agent-browser select <sel> <val>
agent-browser check <sel>
agent-browser uncheck <sel>
agent-browser drag <src> <tgt>
agent-browser upload <sel> <files>

Extraction and Info
agent-browser snapshot
agent-browser get text <sel>
agent-browser get html <sel>
agent-browser get value <sel>
agent-browser get attr <sel> <attr>
agent-browser get title
agent-browser get url
agent-browser get count <sel>
agent-browser get box <sel>
agent-browser screenshot [path]
agent-browser pdf <path>

Check State
agent-browser is visible <sel>
agent-browser is enabled <sel>
agent-browser is checked <sel>

Find Elements
agent-browser find role [value]
agent-browser find text
agent-browser find label [value]
agent-browser find placeholder [value]
agent-browser find alt
agent-browser find title
agent-browser find testid [value]

Actions include click, fill, check, hover, and text.

Wait and Timing
agent-browser wait <selector>
agent-browser wait <ms>
agent-browser wait --text "Welcome"
agent-browser wait --url "**/dash"
agent-browser wait --load networkidle

Advanced Control
agent-browser scroll <dir> [px]
agent-browser scrollintoview <sel>
agent-browser eval <js>
agent-browser mouse move <x> <y>
agent-browser cookies
agent-browser storage local
agent-browser tab new [url]
agent-browser frame <sel>
agent-browser dialog accept [text]

Sessions

Run multiple isolated browser instances.

agent-browser --session agent1 open site-a.com
agent-browser --session agent2 open site-b.com

Snapshot Options

The snapshot command supports filtering to reduce output size.

agent-browser snapshot -i
agent-browser snapshot -c
agent-browser snapshot -d 3
agent-browser snapshot -s "#main"
Selectors and Refs

Refs provide deterministic element selection from snapshots. Use the @ref syntax.

agent-browser snapshot
agent-browser click @e2

Agent Mode

Use --json for machine readable output.

agent-browser snapshot --json

Optimal AI Workflow
Navigate with agent-browser open
Observe with agent-browser snapshot -i --json
Act with @ref from the snapshot
Verify with agent-browser snapshot
Troubleshooting
If the command is not found on Linux ARM64, use the full path in the bin folder.
If an element is not found, use snapshot to find the correct ref.
If the page is not loaded, add a wait command after navigation.
Use --headed to see the browser window for debugging.
Options
--session uses an isolated session.
--json provides JSON output.
--full takes a full page screenshot.
--headed shows the browser window.
--timeout sets the command timeout in milliseconds.
Notes
Refs are stable per page load but change on navigation.
Always snapshot after navigation to get new refs.
Use fill instead of type for input fields to ensure existing text is cleared.
Weekly Installs
–
Repository
am-will/codex-skills
GitHub Stars
907
First Seen
–
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail
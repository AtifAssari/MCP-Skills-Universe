---
rating: ⭐⭐⭐
title: agent-browser-local
url: https://skills.sh/nwparker/agent-browser-local/agent-browser-local
---

# agent-browser-local

skills/nwparker/agent-browser-local/agent-browser-local
agent-browser-local
Installation
$ npx skills add https://github.com/nwparker/agent-browser-local --skill agent-browser-local
SKILL.md
Browser Selection
Default: Use Microsoft Edge unless the user explicitly asks for Chrome, Chromium, or Comet.
User choice: If the user says "use Chrome", "with Chromium", "in Comet", etc., use that browser instead.
CRITICAL:

DO NOT kill the browser process (pkill) unless absolutely necessary. Killing the process will close all of the user's open windows and tabs.

Always check if CDP is already active before attempting to launch or restart the browser.

1. Check if Already Running (PREFERRED)

Before doing anything, check if CDP is already available on the chosen port. If it is, USE IT and do not restart the browser.

CDP_PORT=${CDP_PORT:-9222}
curl -s http://localhost:${CDP_PORT}/json/version >/dev/null 2>&1 && echo "ALREADY RUNNING" || echo "NEED TO LAUNCH"


If "ALREADY RUNNING", skip all setup steps and go straight to your agent-browser --cdp ... commands.

2. Setup: Launch Browser with CDP (ONLY if needed)

If the browser is already running but CDP is not enabled, you must ask the user before killing the process, as this will close their active windows.

Headed Mode (MANDATORY — visible browser window)

CRITICAL RULE: The browser MUST be launched in headed (visible) mode. The human user must be able to see and interact with the browser directly alongside the agent. Do not pass any --headless flags.

Edge (default):

# ONLY if user confirms or if no windows are open
pkill -9 -f "Microsoft Edge" 2>/dev/null; sleep 2

# Launch with CDP
"/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge" --remote-debugging-port=${CDP_PORT:-9222} &disown 2>/dev/null
sleep 3

# Verify CDP is ready
curl -s http://localhost:${CDP_PORT:-9222}/json/version >/dev/null && echo "CDP ready"

# Bring window to foreground
osascript -e 'tell application "Microsoft Edge" to activate'


Chrome (when user asks for it):

pkill -9 -f "Google Chrome" 2>/dev/null; sleep 2
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --remote-debugging-port=${CDP_PORT:-9222} &disown 2>/dev/null
sleep 3
curl -s http://localhost:${CDP_PORT:-9222}/json/version >/dev/null && echo "CDP ready"
osascript -e 'tell application "Google Chrome" to activate'


Chromium (when user asks for it):

pkill -9 -f Chromium 2>/dev/null; sleep 2
"/Applications/Chromium.app/Contents/MacOS/Chromium" --remote-debugging-port=${CDP_PORT:-9222} &disown 2>/dev/null
sleep 3
curl -s http://localhost:${CDP_PORT:-9222}/json/version >/dev/null && echo "CDP ready"
osascript -e 'tell application "Chromium" to activate'


Comet (when user asks for it):

pkill -9 -f Comet 2>/dev/null; sleep 2
/Applications/Comet.app/Contents/MacOS/Comet --remote-debugging-port=${CDP_PORT:-9222} &disown 2>/dev/null
sleep 3
curl -s http://localhost:${CDP_PORT:-9222}/json/version >/dev/null && echo "CDP ready"
osascript -e 'tell application "Comet" to activate'

Core Rule: Always Pass --cdp

Every agent-browser command MUST include --cdp ${CDP_PORT:-9222}. This connects to the local browser instance instead of launching a new one.

# CORRECT — uses local browser (Edge by default)
agent-browser --cdp ${CDP_PORT:-9222} open https://example.com
agent-browser --cdp ${CDP_PORT:-9222} snapshot -i
agent-browser --cdp ${CDP_PORT:-9222} click @e1

# WRONG — would launch isolated headless browser, losing auth
agent-browser open https://example.com

Workflow

Every interaction follows this pattern:

Check CDP first: curl -s http://localhost:9222/json/version
Launch ONLY if missing: Following the setup steps above for the chosen browser.
Check for Existing Tab: If the user specifies to continue on a tab with a given URL, you MUST first try to find whether there is already an active tab for that URL (e.g., by checking curl -s http://localhost:9222/json/list).
Navigate: agent-browser --cdp 9222 open <url> (or switch to/use the existing tab if found).
Snapshot: agent-browser --cdp 9222 snapshot -i (get element refs like @e1, @e2).
Interact: Use refs to click, fill, select — always with --cdp 9222.
Authentication / Login Handling

CRITICAL: Do NOT attempt to log in on behalf of the user. Since this skill uses the user's local browser profile, authentication should be handled by the user directly.

When you encounter any of the following, you MUST stop and ask the user to step in:

A login page or sign-in form
An OAuth/SSO redirect (e.g., "Sign in with Google")
A 2FA/MFA prompt
A CAPTCHA challenge
A "session expired" or "please log in" message
Any authentication wall blocking access to the target content

What to do:

Take a snapshot so you can describe what you see.
Tell the user: "I've hit a login/authentication page. Please log in manually in the browser window, then let me know when you're done."
Wait for the user to confirm they have completed login before proceeding.
After the user confirms, take a fresh snapshot and continue with the task.

Do NOT:

Try to fill in username/password fields yourself
Try to click through OAuth/SSO flows
Try to bypass or work around the login in any way
Assume credentials from environment variables or files
Session Lifecycle
Reuse always: Check CDP before every interaction, never re-launch if already running.
Don't kill on "close": agent-browser --cdp 9222 close only disconnects agent-browser's Playwright session from the CDP endpoint. It does NOT close or kill the browser. The user's browser stays open.
No cleanup needed: When the Claude Code session ends, the browser keeps running as the user's normal browser.
Agent Browser Usage

Please load the agent-browser skill for detailed agent-browser use

Weekly Installs
31
Repository
nwparker/agent-…er-local
GitHub Stars
1
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail
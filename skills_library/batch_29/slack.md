---
title: slack
url: https://skills.sh/azmym/agent-skills/slack
---

# slack

skills/azmym/agent-skills/slack
slack
Installation
$ npx skills add https://github.com/azmym/agent-skills --skill slack
SKILL.md
Slack Web API Skill

Interact with Slack: read, write, search, react, pin, and manage conversations via the Web API.

IMPORTANT: First-Use Initialization

Before executing any Slack operation, check if the mode config file exists:

cat ~/.agents/config/slack/config.env


If the file does not exist (or does not contain SLACK_MODE), you must ask the user which mode they want to use. Present these three options:

Token (macOS only): Extracts session tokens directly from Chrome. Fastest option. Requires Chrome with Slack open, AppleScript enabled, and uvx installed.
Browser (cross-platform): Uses a local Playwright browser to make API calls. Works on macOS, Linux, and Windows. Requires Node.js 18+. Supports SSO and 2FA login.
Auto-detect (recommended): Automatically uses browser mode if a Playwright session exists, otherwise falls back to token mode. Best of both worlds.

Once the user selects a mode, save it immediately:

mkdir -p ~/.agents/config/slack
echo 'SLACK_MODE=<selected_value>' > ~/.agents/config/slack/config.env


Where <selected_value> is token, browser, or auto.

After saving, never ask again. On all subsequent invocations, the config file will exist and the skill will use the saved mode automatically.

If the user selected browser mode, also run the browser session setup:

{SKILL_DIR}/scripts/slack-browser-session.sh login-manual


This opens a visible browser for the user to log in to Slack (supports SSO/2FA). The session is saved and reused for all future API calls.

Mode Selection

The skill supports three modes. Set via ~/.agents/config/slack/config.env or the SLACK_MODE environment variable:

Mode	Value	Behavior
Token	token	Direct curl calls using Chrome session tokens. Fast. macOS only.
Browser	browser	API calls through a local Playwright browser session. Cross-platform.
Auto-detect	auto	Use browser if session exists; falls back to token on auth failure. (default)
Configure the mode

Option 1: Config file (persistent)

echo 'SLACK_MODE=token' > ~/.agents/config/slack/config.env
# or
echo 'SLACK_MODE=browser' > ~/.agents/config/slack/config.env
# or
echo 'SLACK_MODE=auto' > ~/.agents/config/slack/config.env


Option 2: Environment variable (per-call override)

SLACK_MODE=browser slack-api.sh conversations.history channel=C041RSY6DN2 limit=20


The environment variable takes priority over the config file.

Config and State Directory

All skill config and state lives under ~/.agents/config/slack/:

File	Purpose
config.env	Mode selection (SLACK_MODE=auto|token|browser)
tokens.env	Cached session tokens (xoxc, xoxd, user-agent)
browser-session	Active browser session ID
sessions/<id>/storageState.json	Playwright session cookies and localStorage

This directory is created automatically on first use.

API Wrapper

All calls go through a single unified script:

{SKILL_DIR}/scripts/slack-api.sh <method> [key=value ...]


Where {SKILL_DIR} is the base directory provided when this skill is loaded (e.g., ~/.agents/skills/slack).

The script automatically routes to the correct mode based on your configuration. For the full method reference, see references/api-methods.md.

Token Mode (macOS)

Token mode extracts session tokens from your running Chrome browser and makes direct curl calls to the Slack Web API.

Prerequisites:

Chrome running with Slack open at app.slack.com
Chrome > View > Developer > Allow JavaScript from Apple Events
uvx installed (brew install uv)

No manual setup needed. On first API call, tokens are extracted automatically.

Browser Mode (Cross-Platform)

Browser mode uses a local Playwright Chromium instance to maintain a Slack session. API calls are made via fetch() inside the browser context, so no token extraction is needed. This works on macOS, Linux, and Windows.

Prerequisites:

Node.js 18+ installed
Playwright auto-installs on first use (downloads Chromium, ~150 MB)

For detailed documentation, see references/browser-mode.md.

Quick Start (Browser Mode)
# 1. Set mode to browser
echo 'SLACK_MODE=browser' > ~/.agents/config/slack/config.env

# 2. Start a browser session and log in manually (supports SSO/2FA)
{SKILL_DIR}/scripts/slack-browser-session.sh login-manual

# Or: automated email+password login
{SKILL_DIR}/scripts/slack-browser-session.sh start
{SKILL_DIR}/scripts/slack-browser-session.sh login user@example.com mypassword

# 3. Verify login succeeded
{SKILL_DIR}/scripts/slack-browser-session.sh status

# 4. Make API calls (same script, routes through browser automatically)
{SKILL_DIR}/scripts/slack-api.sh conversations.history channel=C041RSY6DN2 limit=20

# 5. Close when done
{SKILL_DIR}/scripts/slack-browser-session.sh stop

UI Automation (API Gaps)

Browser mode also enables direct interaction with Slack's web UI for features that lack API support:

# Get the session ID
SESSION_ID=$({SKILL_DIR}/scripts/slack-browser-session.sh get)

# Navigate to a specific channel
node {SKILL_DIR}/scripts/playwright-bridge.js --function interact --session $SESSION_ID \
  --input '{"action": "goto", "url": "https://app.slack.com/client/TEAM_ID/CHANNEL_ID"}'

# Take a snapshot to see interactive elements
node {SKILL_DIR}/scripts/playwright-bridge.js --function snapshot --session $SESSION_ID --input '{}'

# Interact with UI elements using @e refs from the snapshot
node {SKILL_DIR}/scripts/playwright-bridge.js --function interact --session $SESSION_ID \
  --input '{"action": "click", "ref": "@e5"}'

# Take a screenshot for visual verification
node {SKILL_DIR}/scripts/playwright-bridge.js --function screenshot --session $SESSION_ID --input '{}'


Use cases for UI automation:

Canvas creation and editing (no public API)
Huddle interactions (no API)
Workflow Builder configuration
Slack Connect invitations
Admin and settings pages
Visual message verification via screenshots
Parsing Slack URLs

Extract channel and timestamp from Slack URLs:

https://{WORKSPACE}.slack.com/archives/{CHANNEL_ID}/p{TIMESTAMP_WITHOUT_DOT}


Insert a dot before the last 6 digits of the timestamp:

URL: p1770725748342899 -> ts: 1770725748.342899

For threaded messages, the URL may include ?thread_ts= parameter.

Read Operations
Read a thread
slack-api.sh conversations.replies channel=CHANNEL_ID ts=THREAD_TS limit=100

Read channel history
slack-api.sh conversations.history channel=CHANNEL_ID limit=20


Optional: oldest / latest (Unix timestamps) to bound the time range.

Search messages
slack-api.sh search.messages query="search terms" count=10


Modifiers: in:#channel, from:@user, before:YYYY-MM-DD, after:YYYY-MM-DD, has:link, has:reaction, has:pin.

Find a channel by name
slack-api.sh conversations.list types=public_channel limit=200 | python3 -c "import sys,json; channels=json.load(sys.stdin).get('channels',[]); matches=[c for c in channels if 'TARGET' in c['name']]; [print(f\"{c['id']} #{c['name']}\") for c in matches]"

Look up a user
slack-api.sh users.info user=USER_ID


Name: .user.real_name or .user.profile.display_name.

List pinned items
slack-api.sh pins.list channel=CHANNEL_ID

List channel members
slack-api.sh conversations.members channel=CHANNEL_ID limit=100

Write Operations

IMPORTANT: Confirmation required before any write operation.

Before sending, editing, deleting a message, adding/removing reactions, or pinning/unpinning, always show the user a preview and ask for confirmation. Format the preview as:

To: #channel-name (or @username for DMs) Message: The exact message text Action: Send / Edit / Delete / React / Pin (as applicable)

Send this? (or: want to change anything?)

Do NOT execute the write API call until the user explicitly confirms. If the user wants changes, update the preview and ask again.

Send a message

For simple one-line messages:

slack-api.sh chat.postMessage channel=CHANNEL_ID text="Hello world"


Thread reply: add thread_ts=PARENT_TS. Broadcast to channel: add reply_broadcast=true.

Send a formatted multi-line message

For messages with newlines, bold, lists, or other mrkdwn formatting, use blocks instead of text. The text parameter with URLSearchParams double-escapes newlines in browser mode, so blocks are the reliable way to send formatted content.

Build the blocks JSON with python and pass it to the API:

BLOCKS=$(python3 -c "
import json
blocks = [
    {'type': 'section', 'text': {'type': 'mrkdwn', 'text': '*Bold heading*'}},
    {'type': 'section', 'text': {'type': 'mrkdwn', 'text': 'Line 1\nLine 2\nLine 3'}},
    {'type': 'section', 'text': {'type': 'mrkdwn', 'text': '1. First item\n2. Second item'}}
]
print(json.dumps(blocks))
")
slack-api.sh chat.postMessage channel=CHANNEL_ID blocks="$BLOCKS" text="Fallback text"


The text parameter serves as fallback for notifications and clients that cannot render blocks. Always include it with a plain-text summary.

Each block text field has a 3000-character limit. For longer messages, split across multiple section blocks.

Edit a message
slack-api.sh chat.update channel=CHANNEL_ID ts=MESSAGE_TS text="Updated text"

Delete a message
slack-api.sh chat.delete channel=CHANNEL_ID ts=MESSAGE_TS

Add a reaction
slack-api.sh reactions.add channel=CHANNEL_ID timestamp=MESSAGE_TS name=thumbsup


Emoji name without colons. Supports skin tones: thumbsup::skin-tone-3.

Remove a reaction
slack-api.sh reactions.remove channel=CHANNEL_ID timestamp=MESSAGE_TS name=thumbsup

Pin a message
slack-api.sh pins.add channel=CHANNEL_ID timestamp=MESSAGE_TS

Unpin a message
slack-api.sh pins.remove channel=CHANNEL_ID timestamp=MESSAGE_TS

Image and File Handling

Messages may contain files. In token mode:

source ~/.agents/config/slack/tokens.env
curl -s "FILE_URL_PRIVATE" \
  -H "Authorization: Bearer ${SLACK_XOXC}" \
  -H "Cookie: d=${SLACK_XOXD}" \
  -o /tmp/slack-image-N.png


In browser mode, navigate to the file URL and screenshot:

node {SKILL_DIR}/scripts/playwright-bridge.js --function interact --session $SESSION_ID \
  --input '{"action": "goto", "url": "FILE_URL_PRIVATE"}'
node {SKILL_DIR}/scripts/playwright-bridge.js --function screenshot --session $SESSION_ID --input '{}'


Then use the Read tool to view the downloaded image.

Output Formatting
Parse JSON with python3 -c "import sys,json; ..."
Resolve user IDs (U...) to real names via users.info (cache lookups)
Present messages with timestamps and names
Replace <@U...> mentions with resolved real names
Decode Slack markup (entities, link syntax, channel references) to plain text
Rate Limiting
Add sleep 1 between consecutive API calls
Never bulk-paginate large datasets (users.list), it kills the session
Prefer targeted queries over bulk fetches
Browser mode has additional latency per call; batch where possible
Token Refresh (Token Mode, Automatic)

Token refresh is fully automatic. The API wrapper:

Auto-refreshes if ~/.agents/config/slack/tokens.env is missing
Auto-refreshes on invalid_auth errors and retries the call

Tokens are extracted from the running Chrome browser:

xoxc: from Slack's localStorage via AppleScript
xoxd: from Chrome's cookie database via lsof + pycookiecheat
Setup
Token Mode (macOS)

Open Chrome with Slack at app.slack.com

Enable Chrome > View > Developer > Allow JavaScript from Apple Events

Install uv: brew install uv

Set mode (optional, auto-detect works by default):

echo 'SLACK_MODE=token' > ~/.agents/config/slack/config.env

Browser Mode (Cross-Platform)

Install Node.js 18+ from https://nodejs.org

Set mode and start a session:

echo 'SLACK_MODE=browser' > ~/.agents/config/slack/config.env
{SKILL_DIR}/scripts/slack-browser-session.sh login-manual


Playwright and Chromium install automatically on first use.

Auto-detect (Default)

No configuration needed. The skill checks for an active browser session first and makes the API call via Playwright. If the browser call returns an auth error (invalid_auth, not_authed, or no_teams_found), it automatically falls back to token mode. This provides seamless recovery when a browser session expires.

Full API Reference

For additional methods (bookmarks, user groups, reminders, emoji, files, user profiles, etc.), see references/api-methods.md.

Error Handling
not_in_channel: User does not have access to this channel
channel_not_found: Invalid channel ID
invalid_auth: Token expired, auto-refresh attempted (token mode)
ratelimited: Wait and retry with sleep 5
cant_update_message / cant_delete_message: Can only modify own messages
no_browser_session: No active browser session; run slack-browser-session.sh start
node_not_found: Node.js not installed; install from https://nodejs.org
no_teams_found: Slack has not loaded workspace data in browser; wait and retry
Automatic fallback: In auto mode, if the browser call returns invalid_auth, not_authed, or no_teams_found, the skill automatically retries via token mode. No manual intervention needed.
Weekly Installs
23
Repository
azmym/agent-skills
GitHub Stars
2
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykFail
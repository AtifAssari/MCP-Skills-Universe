---
title: openwork-docker-chrome-mcp
url: https://skills.sh/different-ai/openwork/openwork-docker-chrome-mcp
---

# openwork-docker-chrome-mcp

skills/different-ai/openwork/openwork-docker-chrome-mcp
openwork-docker-chrome-mcp
Installation
$ npx skills add https://github.com/different-ai/openwork --skill openwork-docker-chrome-mcp
SKILL.md
Quick Usage (Already Configured)
1) Start the dev stack (Docker)

Run from the OpenWork repo root:

packaging/docker/dev-up.sh


This prints:

Web UI URL (http://localhost:<WEB_PORT>)
OpenWork server URL (http://localhost:<OPENWORK_PORT>)
Token file path (tmp/.dev-env-<id>) containing OPENWORK_TOKEN + OPENWORK_HOST_TOKEN
A docker compose ... down command that stops this stack
2) Verify a real UI flow (Chrome MCP)

Minimum gate:

Open the printed Web UI URL.
Navigate to the session/chat surface (typically /session).
Send a message (example: smoke: hello from chrome mcp).
Confirm a response renders in the UI.

Chrome MCP tool recipe (typical):

chrome-devtools_list_pages (optional: see existing tabs)
chrome-devtools_new_page with the Web UI URL (or chrome-devtools_navigate_page if a page is already open)
chrome-devtools_take_snapshot to locate the chat input + Send button uids
chrome-devtools_fill the chat input uid with your message
chrome-devtools_click the Send button uid
chrome-devtools_wait_for a distinctive piece of response text (or re-snapshot until the response appears)
chrome-devtools_take_screenshot (save to /tmp/...png when possible)
If debugging: chrome-devtools_list_console_messages

Evidence:

Take a Chrome MCP screenshot after the response appears.
If something fails, capture console logs and (optionally) Docker logs.
Verification checklist (copy into PR)
 Started stack with packaging/docker/dev-up.sh from repo root.
 Used the printed Web UI URL (not a guessed port).
 Completed one full user flow in the UI (input -> action -> visible result).
 Captured at least one screenshot for the success state.
 Captured failure evidence when relevant (console and/or Docker logs).
 Stopped stack with the exact printed docker compose -p ... down command.

Suggested screenshot set for user-facing changes:

Before action state.
During action/progress state.
Success state.
Failure or recovery state (if applicable).
3) Stop the stack

Use the exact docker compose -p ... down command printed by dev-up.sh.

If you lost it, you can find the project name via:

docker ps --format '{{.Names}}' | rg '^openwork-dev-'


Then stop it (replace <project>):

docker compose -p <project> -f packaging/docker/docker-compose.dev.yml down

Required Gate (Non-Negotiable)
Any user-facing change or change that touches remote behavior must be validated end-to-end in the running UI.
The change is not "done" until it succeeds via Chrome MCP against the Docker dev stack started by packaging/docker/dev-up.sh.
Common Gotchas
Docker is required (and the docker CLI must be available on PATH).
dev-up.sh uses random host ports; do not assume 5173/8787.
If the UI looks up but is disconnected, confirm you opened the printed URL and that headless is healthy.
Weekly Installs
90
Repository
different-ai/openwork
GitHub Stars
14.6K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
---
rating: ⭐⭐
title: mega-code-login
url: https://skills.sh/wisdomgraph/mega-code/mega-code-login
---

# mega-code-login

skills/wisdomgraph/mega-code/mega-code-login
mega-code-login
Installation
$ npx skills add https://github.com/wisdomgraph/mega-code --skill mega-code-login
SKILL.md
Login to MEGA-Code

Authenticate with MEGA-Code to obtain an API key using a two-step OAuth flow.

Setup
MEGA_DIR="$(cd "${CLAUDE_SKILL_DIR}/../.." && pwd)"

Step 1: Create session (fast, non-blocking)
uv run --directory "$MEGA_DIR" python -m mega_code.client.login --step create [--url URL]


Add --provider github for GitHub OAuth instead of Google. Add --url URL to specify the server (default: https://console.megacode.ai).

Returns a JSON object to stdout:

{"login_url": "https://...", "client_id": "abc-123", "base_url": "https://..."}


On error, the JSON has an error field instead.

After getting the JSON:

Parse the output as JSON
Show login_url to the user — tell them to open it in their browser
Save client_id and base_url for Step 2
Step 2: Poll for completion (run in background)
uv run --directory "$MEGA_DIR" python -m mega_code.client.login \
  --step poll --client-id CLIENT_ID --url BASE_URL


Replace CLIENT_ID and BASE_URL with values from Step 1. Run this in the background so the user is not blocked.

On success, saves to ~/.local/share/mega-code/.env (stable, version-independent):

MEGA_CODE_API_KEY, MEGA_CODE_CLIENT_MODE=remote, MEGA_CODE_SERVER_URL
Prints "Login successful!" and exits

Polls every 3s, times out after 10 minutes.

Verify

Credentials are stored in the stable data directory, not the versioned plugin dir. Do not print the raw API key — mask it.

grep -E "MEGA_CODE_(API_KEY|CLIENT_MODE|SERVER_URL)" "$HOME/.local/share/mega-code/.env" \
  | sed -E 's/(MEGA_CODE_API_KEY=.{6}).*/\1***/'

Troubleshooting
Timeout: Session expires after 10 min. Re-run the command.
Connection error: Check MEGA_CODE_SERVER_URL in ~/.local/share/mega-code/.env.
Already logged in: Running login again replaces the existing key.
Weekly Installs
29
Repository
wisdomgraph/mega-code
GitHub Stars
43
First Seen
Mar 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
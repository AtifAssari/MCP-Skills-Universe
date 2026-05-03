---
title: 1password
url: https://skills.sh/steipete/agent-scripts/1password
---

# 1password

skills/steipete/agent-scripts/1password
1password
Originally fromsteipete/clawdis
Installation
$ npx skills add https://github.com/steipete/agent-scripts --skill 1password
SKILL.md
1Password CLI

Follow the official CLI get-started steps. Don't guess install commands.

References
Official docs: https://developer.1password.com/docs/cli/get-started/
references/get-started.md (install + app integration + sign-in flow)
references/cli-examples.md (real op examples, including safe item create/edit patterns)
Workflow
Check OS + shell.
Verify CLI present inside tmux: op --version.
Confirm desktop app integration is enabled (per get-started) and the app is unlocked.
REQUIRED: create a fresh tmux session for all op commands (no direct op calls outside tmux).
Sign in / authorize inside tmux: op signin (expect app prompt).
Verify access inside tmux: op whoami (must succeed before any secret read).
If multiple accounts: use --account or OP_ACCOUNT.
Peter account defaults
Peter's default account for personal/work secrets is my.1password.com ("Peter Steinberger's Clan").
Do not silently use my.1password.eu / Titan unless Peter asks for it.
Pass --account my.1password.com on every op command when storing or reading Peter's secrets. Do not rely on ambient account selection.
op account list is metadata-only, but still must run inside tmux. Use it to confirm account names when routing is unclear.
op signin --account my.1password.com can return status 0 with no useful output and still not make a later shell signed in. Prefer doing sign-in, create/edit/get, and verification in the same tmux shell.
REQUIRED tmux session (T-Max)

The shell tool uses a fresh TTY per command. To avoid re-prompts and failures, always run op inside a dedicated tmux session with a fresh socket/session name.

Example (see tmux skill for socket conventions, do not reuse old session names):

SOCKET_DIR="${CLAWDBOT_TMUX_SOCKET_DIR:-${TMPDIR:-/tmp}/clawdbot-tmux-sockets}"
mkdir -p "$SOCKET_DIR"
SOCKET="$SOCKET_DIR/clawdbot-op.sock"
SESSION="op-auth-$(date +%Y%m%d-%H%M%S)"

tmux -S "$SOCKET" new -d -s "$SESSION" -n shell
tmux -S "$SOCKET" send-keys -t "$SESSION":0.0 -- "op signin --account my.1password.com" Enter
tmux -S "$SOCKET" send-keys -t "$SESSION":0.0 -- "op whoami" Enter
tmux -S "$SOCKET" send-keys -t "$SESSION":0.0 -- "op vault list" Enter
tmux -S "$SOCKET" capture-pane -p -J -t "$SESSION":0.0 -S -200
tmux -S "$SOCKET" kill-session -t "$SESSION"

Known working secret-write pattern

Use a fresh tmux session, read the secret from the clipboard without printing it, optionally validate an expected token prefix, and write to Peter's account explicitly. The op category string is human-readable and case-sensitive in this CLI build; use "API Credential", not api_credential.

tmux new-session -d -s op-store-secret 'bash -lc '\''set -euo pipefail
set +x
ACCOUNT="my.1password.com"
ITEM_TITLE="Service API Tokens"
FIELD_NAME="api_token"
EXPECTED_PREFIX=""
NOTES="Created via tmux-safe op workflow"
TOKEN="$(pbpaste)"
if [ -n "$EXPECTED_PREFIX" ]; then
  case "$TOKEN" in "$EXPECTED_PREFIX"*) ;; *) echo "clipboard value does not match expected prefix" >&2; exit 2;; esac
fi
op item create --account "$ACCOUNT" --category "API Credential" --title "$ITEM_TITLE" "$FIELD_NAME[password]=$TOKEN" "notesPlain=$NOTES" >/dev/null
op item get "$ITEM_TITLE" --account "$ACCOUNT" --fields "label=$FIELD_NAME" >/dev/null
echo "stored and verified secret field without printing it"
sleep 30
'\'''


For a second secret on the same item:

tmux new-session -d -s op-edit-secret 'bash -lc '\''set -euo pipefail
set +x
ACCOUNT="my.1password.com"
ITEM_TITLE="Service API Tokens"
FIELD_NAME="app_token"
EXPECTED_PREFIX=""
TOKEN="$(pbpaste)"
if [ -n "$EXPECTED_PREFIX" ]; then
  case "$TOKEN" in "$EXPECTED_PREFIX"*) ;; *) echo "clipboard value does not match expected prefix" >&2; exit 2;; esac
fi
op item edit "$ITEM_TITLE" --account "$ACCOUNT" "$FIELD_NAME[password]=$TOKEN" >/dev/null
op item get "$ITEM_TITLE" --account "$ACCOUNT" --fields "label=$FIELD_NAME" >/dev/null
echo "stored and verified secret field without printing it"
sleep 30
'\'''

Redacted debugging

Keep the whole pipeline inside tmux. Inspect status and output length, never secret values.

tmux new-session -d -s op-debug 'bash -lc '\''set -euo pipefail
set +x
SIGNIN_OUTPUT="$(op signin --account my.1password.com 2>&1 || true)"
echo "signin output bytes: ${#SIGNIN_OUTPUT}"
op account list 2>&1 | sed -E "s/(xox[baprs]-)[A-Za-z0-9-]+/\\1REDACTED/g; s/(xapp-)[A-Za-z0-9-]+/\\1REDACTED/g"
sleep 30
'\'''

Guardrails
Never paste secrets into logs, chat, or code.
Prefer op run / op inject over writing secrets to disk.
If sign-in without app integration is needed, use op account add.
If a command returns "account is not signed in", re-run op signin inside tmux and authorize in the app.
Do not run op outside tmux; stop and ask if tmux is unavailable.
Weekly Installs
301
Repository
steipete/agent-scripts
GitHub Stars
2.5K
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
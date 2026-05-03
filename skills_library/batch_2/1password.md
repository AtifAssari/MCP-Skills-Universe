---
title: 1password
url: https://skills.sh/steipete/clawdis/1password
---

# 1password

skills/steipete/clawdis/1password
1password
Installation
$ npx skills add https://github.com/steipete/clawdis --skill 1password
SKILL.md
1Password CLI

Follow the official CLI get-started steps. Don't guess install commands.

References
references/get-started.md (install + app integration + sign-in flow)
references/cli-examples.md (real op examples)
Workflow
Check OS + shell.
Verify CLI present: op --version.
Confirm desktop app integration is enabled (per get-started) and the app is unlocked.
REQUIRED: create a fresh tmux session for all op commands (no direct op calls outside tmux).
Sign in / authorize inside tmux: op signin (expect app prompt).
Verify access inside tmux: op whoami (must succeed before any secret read).
If multiple accounts: use --account or OP_ACCOUNT.
REQUIRED tmux session (T-Max)

The shell tool uses a fresh TTY per command. To avoid re-prompts and failures, always run op inside a dedicated tmux session with a fresh socket/session name.

Example (see tmux skill for socket conventions, do not reuse old session names):

SOCKET_DIR="${OPENCLAW_TMUX_SOCKET_DIR:-${TMPDIR:-/tmp}/openclaw-tmux-sockets}"
mkdir -p "$SOCKET_DIR"
SOCKET="$SOCKET_DIR/openclaw-op.sock"
SESSION="op-auth-$(date +%Y%m%d-%H%M%S)"

tmux -S "$SOCKET" new -d -s "$SESSION" -n shell
tmux -S "$SOCKET" send-keys -t "$SESSION":0.0 -- "op signin --account my.1password.com" Enter
tmux -S "$SOCKET" send-keys -t "$SESSION":0.0 -- "op whoami" Enter
tmux -S "$SOCKET" send-keys -t "$SESSION":0.0 -- "op vault list" Enter
tmux -S "$SOCKET" capture-pane -p -J -t "$SESSION":0.0 -S -200
tmux -S "$SOCKET" kill-session -t "$SESSION"

Guardrails
Never paste secrets into logs, chat, or code.
Prefer op run / op inject over writing secrets to disk.
If sign-in without app integration is needed, use op account add.
If a command returns "account is not signed in", re-run op signin inside tmux and authorize in the app.
Do not run op outside tmux; stop and ask if tmux is unavailable.
Weekly Installs
1.0K
Repository
steipete/clawdis
GitHub Stars
367.2K
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass
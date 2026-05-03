---
rating: ⭐⭐⭐
title: tmux
url: https://skills.sh/steipete/clawdis/tmux
---

# tmux

skills/steipete/clawdis/tmux
tmux
Installation
$ npx skills add https://github.com/steipete/clawdis --skill tmux
Summary

Control tmux sessions by sending keystrokes and reading pane output for interactive CLI management.

Send text input and special keys (Enter, Ctrl+C, Ctrl+Z) to tmux panes; capture output via capture-pane to monitor long-running processes and interactive prompts
Target sessions, windows, and panes using session:window.pane notation; navigate and manage multiple parallel sessions programmatically
Designed for monitoring Claude Code sessions and approving interactive prompts; sessions persist across SSH disconnects
Requires tmux to be installed; use for interactive applications only, not one-off commands or non-interactive scripts
SKILL.md
tmux Session Control

Control tmux sessions by sending keystrokes and reading output. Essential for managing Claude Code sessions.

When to Use

✅ USE this skill when:

Monitoring Claude/Codex sessions in tmux
Sending input to interactive terminal applications
Scraping output from long-running processes in tmux
Navigating tmux panes/windows programmatically
Checking on background work in existing sessions
When NOT to Use

❌ DON'T use this skill when:

Running one-off shell commands → use exec tool directly
Starting new background processes → use exec with background:true
Non-interactive scripts → use exec tool
The process isn't in tmux
You need to create a new tmux session → use exec with tmux new-session
Example Sessions
Session	Purpose
shared	Primary interactive session
worker-2 - worker-8	Parallel worker sessions
Common Commands
List Sessions
tmux list-sessions
tmux ls

Capture Output
# Last 20 lines of pane
tmux capture-pane -t shared -p | tail -20

# Entire scrollback
tmux capture-pane -t shared -p -S -

# Specific pane in window
tmux capture-pane -t shared:0.0 -p

Send Keys
# Send text (doesn't press Enter)
tmux send-keys -t shared "hello"

# Send text + Enter
tmux send-keys -t shared "y" Enter

# Send special keys
tmux send-keys -t shared Enter
tmux send-keys -t shared Escape
tmux send-keys -t shared C-c          # Ctrl+C
tmux send-keys -t shared C-d          # Ctrl+D (EOF)
tmux send-keys -t shared C-z          # Ctrl+Z (suspend)

Window/Pane Navigation
# Select window
tmux select-window -t shared:0

# Select pane
tmux select-pane -t shared:0.1

# List windows
tmux list-windows -t shared

Session Management
# Create new session
tmux new-session -d -s newsession

# Kill session
tmux kill-session -t sessionname

# Rename session
tmux rename-session -t old new

Sending Input Safely

For interactive TUIs (Claude Code, Codex, etc.), split text and Enter into separate sends to avoid paste/multiline edge cases:

tmux send-keys -t shared -l -- "Please apply the patch in src/foo.ts"
sleep 0.1
tmux send-keys -t shared Enter

Claude Code Session Patterns
Check if Session Needs Input
# Look for prompts
tmux capture-pane -t worker-3 -p | tail -10 | grep -E "❯|Yes.*No|proceed|permission"

Approve Claude Code Prompt
# Send 'y' and Enter
tmux send-keys -t worker-3 'y' Enter

# Or select numbered option
tmux send-keys -t worker-3 '2' Enter

Check All Sessions Status
for s in shared worker-2 worker-3 worker-4 worker-5 worker-6 worker-7 worker-8; do
  echo "=== $s ==="
  tmux capture-pane -t $s -p 2>/dev/null | tail -5
done

Send Task to Session
tmux send-keys -t worker-4 "Fix the bug in auth.js" Enter

Notes
Use capture-pane -p to print to stdout (essential for scripting)
-S - captures entire scrollback history
Target format: session:window.pane (e.g., shared:0.0)
Sessions persist across SSH disconnects
Weekly Installs
2.7K
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
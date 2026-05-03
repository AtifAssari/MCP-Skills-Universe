---
title: tmux
url: https://skills.sh/knoopx/pi/tmux
---

# tmux

skills/knoopx/pi/tmux
tmux
Installation
$ npx skills add https://github.com/knoopx/pi --skill tmux
SKILL.md
tmux

Terminal multiplexer for background processes, output capture, and session management.

Quick Reference
Command	Description
tmux new -d -s name 'cmd'	Run command in background session
tmux capture-pane -t name -p	Capture output from session
tmux send-keys -t name 'text' Enter	Send input to session
tmux kill-session -t name	Terminate session
tmux ls	List all sessions
tmux has -t name	Check if session exists
Running Background Processes
# Run command in new detached session
tmux new-session -d -s myserver 'python -m http.server 8080'

# With specific working directory
tmux new-session -d -s build -c /path/to/project 'make build'

# Keep session alive after command completes
tmux new-session -d -s task 'command; exec bash'

# Run only if session doesn't exist
tmux has -t myserver || tmux new-session -d -s myserver 'command'

Capturing Output
# Capture visible output
tmux capture-pane -t mysession -p

# Capture entire scrollback history
tmux capture-pane -t mysession -p -S -

# Capture last N lines
tmux capture-pane -t mysession -p -S -100

# Save to file
tmux capture-pane -t mysession -p > output.txt

# Capture with escape sequences (colors)
tmux capture-pane -t mysession -p -e

Sending Input
# Send text and Enter
tmux send-keys -t mysession 'echo hello' Enter

# Send without Enter
tmux send-keys -t mysession 'some-text'

# Send Ctrl+C
tmux send-keys -t mysession C-c

Session Management
# List sessions
tmux list-sessions
tmux ls

# Kill specific session
tmux kill-session -t myserver

# Kill all sessions
tmux kill-server

# Check if session exists
tmux has -t mysession

Wait for Completion
# Signal completion from command
tmux new-session -d -s job 'command; tmux wait-for -S job-done'

# Wait for signal
tmux wait-for job-done

Common Patterns
Development Servers
tmux new-session -d -s backend 'bun run backend'
tmux new-session -d -s frontend 'bun run frontend'
tmux new-session -d -s tests 'vitest --watch'

Run and Capture Output
tmux new-session -d -s job 'command'
sleep 0.5
output=$(tmux capture-pane -t job -p)
echo "$output"

Conditional Session
tmux has -t myserver || tmux new-session -d -s myserver 'command'

Cleanup
tmux kill-session -t backend
tmux kill-session -t frontend
tmux kill-server  # Kill all

Tips
Use tmux new-session -d for background processes
Use tmux capture-pane -p -S - for full scrollback
Use tmux has -t name to check session existence
Use tmux kill-server to clean up all sessions
Use -c /path to set working directory
Use exec bash to keep session alive after command
Weekly Installs
26
Repository
knoopx/pi
GitHub Stars
45
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass
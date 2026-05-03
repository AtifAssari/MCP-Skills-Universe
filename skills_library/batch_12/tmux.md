---
title: tmux
url: https://skills.sh/johnlindquist/claude/tmux
---

# tmux

skills/johnlindquist/claude/tmux
tmux
Installation
$ npx skills add https://github.com/johnlindquist/claude --skill tmux
SKILL.md
Tmux Session Manager

Run and manage background processes using tmux.

Prerequisites

Install tmux:

brew install tmux
# or
apt install tmux

CLI Reference
Create Session
# Basic session
tmux new-session -d -s mysession

# With window name
tmux new-session -d -s mysession -n mywindow

# With working directory
tmux new-session -d -s mysession -c /path/to/dir

# With initial command
tmux new-session -d -s mysession "npm run dev"

# Combined
tmux new-session -d -s dev -n server -c /project "npm run dev"

List Sessions
# List all sessions
tmux list-sessions

# Short format
tmux ls

# With format
tmux list-sessions -F "#{session_name}: #{session_windows} windows"

Send Keys to Session
# Send command
tmux send-keys -t mysession "npm test" Enter

# Send to specific window
tmux send-keys -t mysession:mywindow "command" Enter

# Send without Enter
tmux send-keys -t mysession "partial command"

# Send special keys
tmux send-keys -t mysession C-c        # Ctrl+C
tmux send-keys -t mysession C-d        # Ctrl+D
tmux send-keys -t mysession Escape     # Escape
tmux send-keys -t mysession Up         # Arrow up

Capture Output
# Capture visible pane
tmux capture-pane -t mysession -p

# Capture with history (last N lines)
tmux capture-pane -t mysession -p -S -100

# Capture all history
tmux capture-pane -t mysession -p -S -

# Save to file
tmux capture-pane -t mysession -p > output.txt

Kill Session
# Kill specific session
tmux kill-session -t mysession

# Kill all sessions
tmux kill-server

Attach to Session
# Attach
tmux attach -t mysession

# Attach or create
tmux new-session -A -s mysession

Window Management
# New window
tmux new-window -t mysession -n windowname

# Select window
tmux select-window -t mysession:windowname

# Kill window
tmux kill-window -t mysession:windowname

# List windows
tmux list-windows -t mysession

Pane Management
# Split horizontally
tmux split-window -t mysession -h

# Split vertically
tmux split-window -t mysession -v

# Select pane
tmux select-pane -t mysession:0.1

# Kill pane
tmux kill-pane -t mysession:0.1

Workflow Patterns
Run Dev Server in Background
# Start server
tmux new-session -d -s devserver -c /project "npm run dev"

# Check output
tmux capture-pane -t devserver -p -S -50

# Stop server
tmux send-keys -t devserver C-c
tmux kill-session -t devserver

Run Tests with Output Capture
# Start tests
tmux new-session -d -s tests "npm test"

# Wait and capture output
sleep 30
tmux capture-pane -t tests -p -S - > test-output.txt

# Cleanup
tmux kill-session -t tests

Multiple Services
# Create session with multiple windows
tmux new-session -d -s services -n frontend
tmux new-window -t services -n backend
tmux new-window -t services -n database

# Start each service
tmux send-keys -t services:frontend "npm run dev" Enter
tmux send-keys -t services:backend "go run main.go" Enter
tmux send-keys -t services:database "docker-compose up db" Enter

# Check all services
for win in frontend backend database; do
  echo "=== $win ==="
  tmux capture-pane -t services:$win -p -S -10
done

Long-Running Process
# Start process
tmux new-session -d -s build "npm run build:production"

# Monitor progress
watch -n 5 "tmux capture-pane -t build -p -S -20"

# Or periodic check
while tmux has-session -t build 2>/dev/null; do
  sleep 10
  echo "Still running..."
done
echo "Build complete"

Socket Mode (for Agents)

When running in agent context, use a dedicated socket:

SOCKET_PATH="/tmp/agent-tmux-$$"

# Create session with socket
tmux -S $SOCKET_PATH new-session -d -s agent "command"

# Send keys via socket
tmux -S $SOCKET_PATH send-keys -t agent "input" Enter

# Capture via socket
tmux -S $SOCKET_PATH capture-pane -t agent -p

# Cleanup
tmux -S $SOCKET_PATH kill-server
rm -f $SOCKET_PATH

Best Practices
Name sessions descriptively - Easy to identify later
Use -d for detached - Don't block the terminal
Capture output regularly - Before killing sessions
Set working directory - Use -c /path for context
Clean up sessions - Kill when done
Use sockets for isolation - Prevent conflicts between agents
Weekly Installs
39
Repository
johnlindquist/claude
GitHub Stars
23
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
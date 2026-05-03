---
rating: ⭐⭐⭐
title: witr-process-inspector
url: https://skills.sh/aradotso/trending-skills/witr-process-inspector
---

# witr-process-inspector

skills/aradotso/trending-skills/witr-process-inspector
witr-process-inspector
Installation
$ npx skills add https://github.com/aradotso/trending-skills --skill witr-process-inspector
SKILL.md
witr — Why Is This Running?

Skill by ara.so — Daily 2026 Skills collection.

witr is a Go CLI/TUI tool that answers "why is this running?" for any process, service, or port. Instead of leaving you to correlate ps, lsof, ss, systemctl, and docker ps manually, witr makes the causality chain explicit — showing where a running thing came from, how it was started, and what chain of supervisors/containers/shells is responsible.

Installation
Quickest (Unix)
curl -fsSL https://raw.githubusercontent.com/pranshuparmar/witr/main/install.sh | bash

Quickest (Windows PowerShell)
irm https://raw.githubusercontent.com/pranshuparmar/witr/main/install.ps1 | iex

Package Managers
# Homebrew (macOS/Linux)
brew install witr

# Conda
conda install -c conda-forge witr

# Arch Linux (AUR)
yay -S witr-bin

# Windows winget
winget install -e --id PranshuParmar.witr

# Windows Scoop
scoop install main/witr

# Alpine / apk
sudo apk add --allow-untrusted ./witr-*.apk

# Go source install
go install github.com/pranshuparmar/witr/cmd/witr@latest

Key Commands & Flags
Basic Usage
# Inspect a process by PID
witr <pid>

# Inspect by process name (substring match)
witr <name>

# Inspect what's bound to a port
witr --port <port>
witr -p <port>

# Launch interactive TUI dashboard
witr --interactive
witr -i

# Show all running processes with causality info
witr --all
witr -a

# Output as JSON (for scripting)
witr --json <pid>

# Follow/watch mode — refresh automatically
witr --watch <pid>
witr -w <pid>

# Verbose output — show full environment and metadata
witr --verbose <pid>
witr -v <pid>

# Filter processes by user
witr --user <username>

# Show version
witr --version

Common Flag Reference
Flag	Short	Description
--port	-p	Inspect by port number
--interactive	-i	Launch TUI dashboard
--all	-a	Show all processes
--json		Output as JSON
--watch	-w	Auto-refresh/follow
--verbose	-v	Full metadata output
--user		Filter by OS user
--version		Print version
Interactive TUI Mode

Launch the full dashboard:

witr -i
# or
witr --interactive


TUI Keybindings:

Key	Action
↑ / ↓	Navigate process list
Enter	Expand process detail / causality chain
f	Filter/search processes
s	Sort by column
r	Refresh
j	Toggle JSON view
q / Ctrl+C	Quit
Example Outputs
Inspect a PID
witr 1234

PID: 1234
Name: node
Binary: /usr/local/bin/node
Started: 2026-03-18 09:12:44
User: ubuntu

Why is this running?
  └─ Started by: npm (PID 1200)
       └─ Started by: bash (PID 1180)
            └─ Started by: sshd (PID 980)
                 └─ Started by: systemd (PID 1) [service: sshd.service]

Inspect by Port
witr --port 8080

Port: 8080 (TCP, LISTEN)
Process: python3 (PID 4512)
Binary: /usr/bin/python3
User: deploy

Why is this running?
  └─ Started by: gunicorn (PID 4490)
       └─ Started by: systemd (PID 1) [service: myapp.service]
            Unit file: /etc/systemd/system/myapp.service
            ExecStart: /usr/bin/gunicorn app:app --bind 0.0.0.0:8080

JSON Output (for scripting)
witr --json 4512

{
  "pid": 4512,
  "name": "python3",
  "binary": "/usr/bin/python3",
  "user": "deploy",
  "started_at": "2026-03-18T09:00:00Z",
  "causality_chain": [
    {"pid": 4490, "name": "gunicorn", "type": "parent"},
    {"pid": 1,    "name": "systemd",  "type": "supervisor", "service": "myapp.service"}
  ]
}

Watch/Follow a Process
# Refresh every 2 seconds
witr --watch 4512

Common Patterns
Find Who Started a Port Listener
# Quick check: who owns port 5432 (Postgres)?
witr --port 5432

# Get machine-readable output for automation
witr --json --port 5432 | jq '.causality_chain[-1].service'

Audit All Running Services
# List everything with causality, pipe to less
witr --all | less

# Export full audit to JSON
witr --all --json > audit.json

Inspect a Docker/Container Process
# witr understands container boundaries
witr <pid-of-containerized-process>
# Output will show: container → container runtime → systemd chain

Use in a Shell Script
#!/usr/bin/env bash
# Check if port 8080 is in use and why
if witr --json --port 8080 > /tmp/witr_out.json 2>/dev/null; then
  SERVICE=$(jq -r '.causality_chain[-1].service // "unknown"' /tmp/witr_out.json)
  echo "Port 8080 is owned by service: $SERVICE"
else
  echo "Port 8080 is not in use"
fi

Filter Processes by User
# Show only processes owned by www-data and why they're running
witr --all --user www-data

Platform Support
Platform	Architectures	Notes
Linux	amd64, arm64	Full support
macOS	amd64, arm64 (Apple Silicon)	Full support
Windows	amd64	Full support
FreeBSD	amd64, arm64	Full support
Go Integration (Embedding witr Logic)

If you want to use witr programmatically in a Go project:

go get github.com/pranshuparmar/witr

package main

import (
    "fmt"
    "github.com/pranshuparmar/witr/pkg/inspector"
)

func main() {
    // Inspect a process by PID
    result, err := inspector.InspectPID(1234)
    if err != nil {
        panic(err)
    }

    fmt.Printf("Process: %s\n", result.Name)
    for _, link := range result.CausalityChain {
        fmt.Printf("  └─ %s (PID %d)\n", link.Name, link.PID)
    }
}

// Inspect by port
result, err := inspector.InspectPort(8080, "tcp")
if err != nil {
    panic(err)
}
fmt.Printf("Port 8080 owned by PID %d (%s)\n", result.PID, result.Name)

Troubleshooting
Permission Denied on Some PIDs
# witr needs read access to /proc (Linux) or equivalent
# Run with sudo for system-level processes
sudo witr <pid>
sudo witr --port 80

Binary Not Found After Install
# Ensure install location is in PATH
export PATH="$PATH:/usr/local/bin"   # Unix default install
# or for Go installs:
export PATH="$PATH:$(go env GOPATH)/bin"

Port Not Found / No Output
# Confirm port is actually listening first
ss -tlnp | grep <port>       # Linux
netstat -an | grep <port>    # macOS/Windows

# Then retry
witr --port <port>

TUI Not Rendering Correctly
# Ensure terminal supports 256 colors
export TERM=xterm-256color
witr --interactive

# If on Windows, use Windows Terminal for best TUI experience

Process Exited Before Inspection
# witr can only inspect currently running processes
# Use --watch on a long-running process to monitor it
witr --watch <pid>

macOS: Requires Elevated Access for Some Processes
# System Integrity Protection may restrict some process metadata
sudo witr <pid>

Quick Reference Card
witr <pid>              # Why is PID X running?
witr <name>            # Why is process "nginx" running?
witr -p <port>         # What's on port 8080 and why?
witr -i                # Interactive TUI dashboard
witr -a                # Show all processes + causality
witr --json <pid>      # Machine-readable output
witr -w <pid>          # Watch/follow a process
witr -v <pid>          # Verbose: full env + metadata
witr --user <user>     # Filter by OS user

Weekly Installs
1.0K
Repository
aradotso/trending-skills
GitHub Stars
42
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykFail
---
title: bgproc
url: https://skills.sh/ascorbic/bgproc/bgproc
---

# bgproc

skills/ascorbic/bgproc/bgproc
bgproc
Installation
$ npx skills add https://github.com/ascorbic/bgproc --skill bgproc
SKILL.md
bgproc

A CLI for managing background processes. All commands output JSON to stdout.

When to Use

Use bgproc when you need to:

Start a dev server or other long-running process in the background
Restart a process with the same command and working directory
Check if a process is running and what port it's listening on
View logs from a background process
Stop a background process
Commands
# Start a process
bgproc start -n <name> -- <command...>
bgproc start -n devserver -- npm run dev
bgproc start -n devserver -t 300 -- npm run dev  # auto-kill after 5 min

# Start and wait for port (recommended for dev servers)
bgproc start -n devserver -w -- npm run dev      # wait for port, then exit
bgproc start -n devserver -w 30 -- npm run dev   # wait up to 30s for port

# Force restart (kill existing process first)
bgproc start -n devserver -f -w -- npm run dev

# Restart with same command and cwd (kills if running)
bgproc restart <name>
bgproc restart <name> -w      # wait for port after restart

# Check status (returns JSON with pid, running state, port)
bgproc status <name>

# View logs
bgproc logs <name>
bgproc logs <name> --tail 50
bgproc logs <name> --errors  # stderr only

# List all processes
bgproc list
bgproc list --cwd  # filter to current directory

# Stop a process
bgproc stop <name>
bgproc stop <name> --force  # SIGKILL

# Clean up dead processes
bgproc clean <name>
bgproc clean --all

Workflow
Start a process and wait for port: bgproc start -n devserver -w -- npm run dev
Streams logs to stderr while starting
Prints JSON with port to stdout when ready
Use -f to force restart if already running
Restart a process: bgproc restart devserver -w
Re-runs with the same command and cwd
Kills the process first if still running
If something's wrong, check logs: bgproc logs devserver
When done: bgproc stop devserver
Notes
All commands output JSON to stdout, errors to stderr
Port detection works via lsof and checks child processes (macOS/Linux only)
Use -w to wait for port detection before returning
Use -f to force restart (kills existing process with same name)
Starting a process with the same name as a dead one auto-cleans it
Logs are capped at 1MB per process
Weekly Installs
17
Repository
ascorbic/bgproc
GitHub Stars
22
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass
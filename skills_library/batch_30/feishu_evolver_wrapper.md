---
title: feishu-evolver-wrapper
url: https://skills.sh/autogame-17/feishu-evolver-wrapper/feishu-evolver-wrapper
---

# feishu-evolver-wrapper

skills/autogame-17/feishu-evolver-wrapper/feishu-evolver-wrapper
feishu-evolver-wrapper
Installation
$ npx skills add https://github.com/autogame-17/feishu-evolver-wrapper --skill feishu-evolver-wrapper
SKILL.md
Feishu Evolver Wrapper

A lightweight wrapper for the capability-evolver skill. It injects the Feishu reporting environment variables (EVOLVE_REPORT_TOOL) to enable rich card reporting in the Master's environment.

Usage
# Run the evolution loop
node skills/feishu-evolver-wrapper/index.js

# Generate Evolution Dashboard (Markdown)
node skills/feishu-evolver-wrapper/visualize_dashboard.js

# Lifecycle Management (Start/Stop/Status/Ensure)
node skills/feishu-evolver-wrapper/lifecycle.js status

Architecture
Evolution Loop: Runs the GEP evolution cycle with Feishu reporting.
Dashboard: Visualizing metrics and history from assets/gep/events.jsonl.
Export History: Exports raw history to Feishu Docs.
Watchdog: Managed via OpenClaw Cron job evolver_watchdog_robust (runs lifecycle.js ensure every 10 min).
Replaces fragile system crontab logic.
Ensures the loop restarts if it crashes or hangs.
Weekly Installs
22
Repository
autogame-17/fei…-wrapper
GitHub Stars
2
First Seen
Mar 2, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykFail
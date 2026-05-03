---
title: log-analyzer
url: https://skills.sh/niller2005/polyflup/log-analyzer
---

# log-analyzer

skills/niller2005/polyflup/log-analyzer
log-analyzer
Installation
$ npx skills add https://github.com/niller2005/polyflup --skill log-analyzer
SKILL.md
Responsibilities
Syncing logs from the production server using the sync_logs tool.
Analyzing logs/trades_2025.log for specific trade outcomes.
Searching logs/errors.log for stack traces and recurring issues.
Correlating window logs (logs/window_*.log) with specific market events.
Workflow
Run sync_logs to ensure local logs are up to date.
Use grep or search tools to locate relevant timestamps or symbols.
Summarize findings with a focus on actionable insights (e.g., "Market X failed due to Y").
Useful Files
logs/trades_2025.log: The master audit trail.
logs/errors.log: Error history.
logs/reports/: Periodically generated performance reports.
Weekly Installs
12
Repository
niller2005/polyflup
GitHub Stars
19
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
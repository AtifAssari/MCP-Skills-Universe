---
title: pm2-server-control
url: https://skills.sh/viteinfinite/skills/pm2-server-control
---

# pm2-server-control

skills/viteinfinite/skills/pm2-server-control
pm2-server-control
Installation
$ npx skills add https://github.com/viteinfinite/skills --skill pm2-server-control
SKILL.md
pm2-server-control

Use this skill when the task requires starting or stopping a local server via PM2, specifically using pm2 start ./my-server --name <name> --no-autorestart, and when you need to inspect status or logs, restart, or clean up the process.

Required command pattern

Always start the server with:

pm2 start ./my-server --name <name> --no-autorestart


Replace <name> with a concise, unique name (e.g., api-dev, web-preview).

Useful PM2 commands

Start:

pm2 start ./my-server --name <name> --no-autorestart


Stop:

pm2 stop <name>


Restart (if a fresh start is needed):

pm2 restart <name>


Delete (remove from PM2 list):

pm2 delete <name>


List all processes:

pm2 list


Show detailed info:

pm2 show <name>


Logs (stream):

pm2 logs <name>


Logs (last N lines):

pm2 logs <name> --lines 200


Flush logs (if they get noisy):

pm2 flush <name>


Save current process list (optional, if asked):

pm2 save


Resurrect saved processes (only if asked):

pm2 resurrect

Safety and cleanup
Prefer pm2 stop <name> for normal shutdowns.
Use pm2 delete <name> when the process is no longer needed.
Keep process names stable across start/stop cycles.
Weekly Installs
14
Repository
viteinfinite/skills
GitHub Stars
1
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
---
rating: ⭐⭐
title: agentspace
url: https://skills.sh/agentspace-so/skills/agentspace
---

# agentspace

skills/agentspace-so/skills/agentspace
agentspace
Installation
$ npx skills add https://github.com/agentspace-so/skills --skill agentspace
SKILL.md
🪢 Agentspace

See what your agent is doing — from anywhere.

Your agent keeps writing — logs, code, generated outputs. You open a URL and watch the folder evolve in the browser. No sync, no zip, no account.

Tell the agent to share any local folder or file.
The agent returns a URL — anyone opens it in the browser, no signup.

agentspace.so · GitHub · npm @agentspace-so/ascli

What you can share

Folders, single files, generated code, test output, build logs, screenshots, PDFs, reports, dashboards, prototypes — any local artifact.

How it works
One command (ascli share <path>) creates an anonymous workspace and returns a link.
Anyone opens the link — reads, comments, or edits directly in the browser.
Anonymous workspaces live 24 hours. One email claim makes them permanent.
Hosted on Cloudflare's edge network — links load fast worldwide.
Data handling
Only the path the user explicitly names is uploaded. Do not default to the current working directory unless the user clearly says so.
All network traffic goes to agentspace.so only.
The skill does not read environment variables, shell history, or files outside the path the user specifies.
Choose the CLI path
If ascli is already on PATH, use it directly.
Else if npm is available, install once with npm install -g @agentspace-so/ascli@latest, or run without installing via npx @agentspace-so/ascli@latest <command>.
If neither ascli nor npm is available, stop and tell the user to install Node.js from nodejs.org first.

Do not pipe a remote script into a shell to install.

Share a path
Ask the user which folder or file to share if they have not named one explicitly. Do not assume ..
Run ascli share <path> --permission edit with the user-specified path.
If the user asks for view-only access, use --permission view.
share handles an unbound folder by creating a temporary workspace, syncing once, and returning a link — no separate sync step is needed.
Return the share URL directly to the user exactly as the CLI prints it.
Guardrails
Do not invent claim URLs, workspace URLs, or share URLs. Only return what the CLI prints.
Do not require a global install if npx already works.
Do not move the user into a different project just to use agentspace.so.
If the user asks to "share this folder" and the target is ambiguous, confirm the exact path before running.
If you need exact command variants, read references/commands.md.
Weekly Installs
15.9K
Repository
agentspace-so/skills
GitHub Stars
2
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
---
rating: ⭐⭐
title: helmor-cli
url: https://skills.sh/dohooo/helmor/helmor-cli
---

# helmor-cli

skills/dohooo/helmor/helmor-cli
helmor-cli
Installation
$ npx skills add https://github.com/dohooo/helmor --skill helmor-cli
SKILL.md
Helmor CLI

Use this skill to guide simple terminal-first Helmor workflows. Keep the answer practical: prefer one or two concrete commands over a long CLI tutorial.

First Checks
Check whether the CLI is installed and which data mode it targets:
helmor cli-status

Check the active data directory and database:
helmor data


Use --json when the output will be parsed by scripts or another tool.

CLI Install And Update

Treat Helmor CLI install/update as beta.

Prefer the Helmor desktop onboarding/settings flow for installing or repairing the managed CLI entrypoint.
Use helmor cli-status to verify whether the PATH entry points at the current app-managed CLI.
Do not invent a stable standalone install/update command unless it exists in helmor --help or a subcommand help page.
If the user is blocked, ask them to run helmor cli-status and share the output, or inspect the app's CLI install panel if working inside the Helmor repo.
Helmor Skills Install And Update

Treat Helmor skills install/update as a beta app-managed flow.

Prefer the Helmor desktop onboarding/settings flow for installing or updating bundled Helmor skills.
Do not invent a helmor skills command; the top-level CLI help does not currently expose one.
If the user asks to update a bundled Helmor skill inside the repo, edit the skill files directly and validate them with the skill validation tooling.
Keep user-facing skill content concise and English-first unless the user explicitly asks for another language.
Common Tasks
Manage Repositories And Workspaces

Use these command groups for local-first project setup and workspace orchestration:

helmor repo --help
helmor workspace --help


When creating workspaces, prefer explicit repo names and concise purpose labels:

helmor workspace new --repo helmor

Inspect Sessions And Files

Use sessions for conversation history and files for editor-surface operations:

helmor session --help
helmor files --help

Send A Prompt To An Agent

Use send when the user wants to dispatch work from the terminal:

helmor send --help


Favor JSON output for automation:

helmor --json send --help

Integrations And Local Tooling

Use the relevant command group:

helmor github --help
helmor scripts --help
helmor models --help

MCP Server

Run Helmor as an MCP server over stdio:

helmor mcp


Use this when another agent/runtime needs to call Helmor through Model Context Protocol.

Command Reference

Read references/helmor-help.md when you need the full top-level helmor --help command list.

For exact flags on a command group, run the group's help instead of guessing:

helmor <command> --help

Weekly Installs
258
Repository
dohooo/helmor
GitHub Stars
657
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass
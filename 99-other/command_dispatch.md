---
title: command-dispatch
url: https://skills.sh/jxxghp/moviepilot/command-dispatch
---

# command-dispatch

skills/jxxghp/moviepilot/command-dispatch
command-dispatch
Installation
$ npx skills add https://github.com/jxxghp/moviepilot --skill command-dispatch
SKILL.md
Command Dispatch

Use this skill to identify user intent and dispatch the corresponding system or plugin command.

When to Use
The user sends a /xxx slash command (execute directly)
The user describes an action in natural language, for example:
"Sync sites" → /cookiecloud
"Show my subscriptions" → /subscribes
"Refresh subscriptions" → /subscribes refresh
"What's downloading?" → /downloading
"Organize downloaded files" → /transfer
"Clear cache" → /clear_cache
"Restart the system" → /restart
"Pause all QB tasks" → /pause_torrents (plugin command)
Tools
list_slash_commands — List all available slash commands (system + plugin), returns command name, description, and category
query_plugin_capabilities — Query detailed plugin capabilities (commands, actions, scheduled services)
run_slash_command — Execute a specified command (works for both system and plugin commands)
Workflow
Step 1: Identify User Intent

Determine whether the user's message is requesting the execution of a command:

Direct command: Message starts with /, e.g. /sites, /subscribes → skip to Step 3
Natural language: The user describes an actionable request → continue to Step 2
Step 2: Find Matching Command

Use list_slash_commands to retrieve all available commands. Match the user's described intent against the description and category fields of each command.

If the user's description involves a specific plugin's functionality, additionally use query_plugin_capabilities to query that plugin's detailed capabilities.

Matching strategy:

Prefer exact matches on command description
Then narrow down by category and match
If no matching command is found, inform the user that no corresponding function is available
Step 3: Extract Parameters and Execute

Some commands support additional arguments (space-separated after the command), for example:

/redo <history_id> — Manually re-organize a specific record
/sites disable <site_id> — Disable one or more sites
/subscribes delete <subscribe_id> — Delete one or more subscriptions

Use run_slash_command to execute the command in the format /command_name arg1 arg2.

Step 4: Report Result

Command execution is asynchronous. After triggering, inform the user that the command has started. If the command does not exist, list available commands for reference.

Important Notes
Command execution requires admin privileges; the tool will automatically check permissions
Both system and plugin commands are executed via the run_slash_command tool — no need to distinguish between them
If you are unsure which command matches the user's intent, use list_slash_commands first to look up before deciding
Never guess non-existent commands; always select from the available command list
Weekly Installs
34
Repository
jxxghp/moviepilot
GitHub Stars
11.0K
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
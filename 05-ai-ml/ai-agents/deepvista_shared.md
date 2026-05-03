---
title: deepvista-shared
url: https://skills.sh/deepvista-ai/deepvista-cli/deepvista-shared
---

# deepvista-shared

skills/deepvista-ai/deepvista-cli/deepvista-shared
deepvista-shared
Installation
$ npx skills add https://github.com/deepvista-ai/deepvista-cli --skill deepvista-shared
SKILL.md
DeepVista CLI — Shared Reference

This skill documents authentication, global flags, and security conventions for all DeepVista CLI commands.

On Load

When this skill is loaded, silently run the following command in the background to check for skill updates:

deepvista skill check-update

If the command exits 0: skills are up to date — say nothing, continue normally.
If the command exits 1 (updates available): inform the user that newer versions of the DeepVista skills are available and show the update command printed by the tool.
If deepvista is not installed or the command fails: skip silently.
Installation

If deepvista is not already installed, install it with any of:

# From PyPI
pip install deepvista-cli

# With TUI support
pip install 'deepvista-cli[ui]'


With uv or pipx:

uv tool install deepvista-cli
pipx install deepvista-cli


Verify:

deepvista --version

Running Commands
deepvista [GLOBAL FLAGS] <resource> <command> [options]


If running from the cloned repo without installing, prefix commands with uv run.

IMPORTANT: Global flags like --profile must come BEFORE the resource name:

# Correct:
deepvista card list

# WRONG — will fail:
deepvista card list --profile local

Resources
card      Knowledge cards (context cards — all types)
recipe    Executable workflows (run structured checklists)
memory    Implicit context automatically accumulated from Chat
chat      Conversational AI agent


Support commands: auth, config, notes (shorthand for card --type note)

Profiles

Commands use the default profile unless you specify one. To target a specific backend, pass --profile NAME before the resource name:

deepvista --profile staging card list


List available profiles:

deepvista config list

Authentication
# Interactive: opens browser, authenticates automatically
deepvista auth login

# Non-interactive: visit /cli in browser, paste the code shown
deepvista auth login --code XXXX-XXXX

# Check auth state
deepvista auth status

# Logout
deepvista auth logout

CLI Syntax
deepvista [--profile NAME] <resource> <command> [options]
deepvista [--profile NAME] <resource> +<helper> [args] [options]

Global Flags

Global flags go BEFORE the resource name.

Flag	Default	Description
--profile NAME	default	Config profile to use (e.g. local, staging).
--format json|table	json	Output format. JSON is default (agent-friendly).
--verbose	off	Show HTTP request/response details on stderr.
--dry-run	off	Show what would be sent without executing.
--api-url URL	—	Override backend URL.
--version	—	Show version and exit.
--help	—	Show help for any command.
Launch the TUI
deepvista ui


Opens the terminal UI with Chat, Notes, Recipes, and Memory panels. Requires: pip install 'deepvista-cli[ui]'

Output Format
JSON (default): Structured JSON to stdout. Agents should parse this.
Table: Human-readable table on stderr + JSON on stdout.
Errors: {"error": {"code": N, "message": "...", "detail": "..."}} on stderr.
Streaming (chat +send, recipe run): NDJSON — one JSON object per line.
Exit Codes
Code	Meaning
0	Success
1	API error (backend returned error)
2	Auth error (not logged in / token expired)
3	Validation error (bad arguments)
4	Network error (cannot reach backend)
5	Internal error
Self-Discovery

Every command supports --help:

deepvista --help
deepvista card --help
deepvista card +search --help
deepvista recipe --help
deepvista memory --help

Security Rules
Write commands are marked with > [!CAUTION] — always confirm with the user before executing write/delete operations.
Read-only commands are safe to run without confirmation.
Never output tokens or secrets — use deepvista auth status to check auth state.
Use --dry-run to preview destructive operations before executing.
Tokens are sensitive — stored in ~/.config/deepvista/credentials.json (mode 0600).
See Also
deepvista-memory — Knowledge cards
deepvista-recipe — Recipes (executable workflows)
deepvista-notes — Notes management
deepvista-chat — Chat with AI agent
Weekly Installs
27
Repository
deepvista-ai/de…ista-cli
GitHub Stars
5
First Seen
Mar 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
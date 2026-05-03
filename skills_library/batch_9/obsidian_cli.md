---
title: obsidian-cli
url: https://skills.sh/kepano/obsidian-skills/obsidian-cli
---

# obsidian-cli

skills/kepano/obsidian-skills/obsidian-cli
obsidian-cli
Installation
$ npx skills add https://github.com/kepano/obsidian-skills --skill obsidian-cli
Summary

Read, create, search, and manage Obsidian vault notes via CLI with built-in plugin development and debugging tools.

Core vault operations: read, create, append, search notes; manage tasks, properties, tags, and backlinks with flexible file targeting
Daily note shortcuts for quick appends and reads; supports templates, silent mode, clipboard output, and multi-vault targeting
Plugin development workflow: reload plugins, run JavaScript in app context, capture screenshots, inspect DOM and CSS, check console errors, and toggle mobile emulation
File targeting via wikilink-style names or exact paths; all commands default to the active file or most recently focused vault
SKILL.md
Obsidian CLI

Use the obsidian CLI to interact with a running Obsidian instance. Requires Obsidian to be open.

Command reference

Run obsidian help to see all available commands. This is always up to date. Full docs: https://help.obsidian.md/cli

Syntax

Parameters take a value with =. Quote values with spaces:

obsidian create name="My Note" content="Hello world"


Flags are boolean switches with no value:

obsidian create name="My Note" silent overwrite


For multiline content use \n for newline and \t for tab.

File targeting

Many commands accept file or path to target a file. Without either, the active file is used.

file=<name> — resolves like a wikilink (name only, no path or extension needed)
path=<path> — exact path from vault root, e.g. folder/note.md
Vault targeting

Commands target the most recently focused vault by default. Use vault=<name> as the first parameter to target a specific vault:

obsidian vault="My Vault" search query="test"

Common patterns
obsidian read file="My Note"
obsidian create name="New Note" content="# Hello" template="Template" silent
obsidian append file="My Note" content="New line"
obsidian search query="search term" limit=10
obsidian daily:read
obsidian daily:append content="- [ ] New task"
obsidian property:set name="status" value="done" file="My Note"
obsidian tasks daily todo
obsidian tags sort=count counts
obsidian backlinks file="My Note"


Use --copy on any command to copy output to clipboard. Use silent to prevent files from opening. Use total on list commands to get a count.

Plugin development
Develop/test cycle

After making code changes to a plugin or theme, follow this workflow:

Reload the plugin to pick up changes:
obsidian plugin:reload id=my-plugin

Check for errors — if errors appear, fix and repeat from step 1:
obsidian dev:errors

Verify visually with a screenshot or DOM inspection:
obsidian dev:screenshot path=screenshot.png
obsidian dev:dom selector=".workspace-leaf" text

Check console output for warnings or unexpected logs:
obsidian dev:console level=error

Additional developer commands

Run JavaScript in the app context:

obsidian eval code="app.vault.getFiles().length"


Inspect CSS values:

obsidian dev:css selector=".workspace-leaf" prop=background-color


Toggle mobile emulation:

obsidian dev:mobile on


Run obsidian help to see additional developer commands including CDP and debugger controls.

Weekly Installs
22.7K
Repository
kepano/obsidian-skills
GitHub Stars
28.1K
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass
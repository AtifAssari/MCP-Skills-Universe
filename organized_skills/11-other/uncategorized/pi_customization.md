---
rating: ⭐⭐
title: pi-customization
url: https://skills.sh/romiluz13/pi-agent-skills/pi-customization
---

# pi-customization

skills/romiluz13/pi-agent-skills/pi-customization
pi-customization
Installation
$ npx skills add https://github.com/romiluz13/pi-agent-skills --skill pi-customization
SKILL.md
Pi Customization
Grounding
pi-mono/packages/coding-agent/docs/themes.md — theme JSON format (name, optional vars, required 51 colors tokens), locations (~/.pi/agent/themes/*.json, .pi/themes/*.json, packages, settings, CLI --theme), hot reload, color value formats.
pi-mono/packages/coding-agent/docs/keybindings.md — customization via ~/.pi/agent/keybindings.json, namespaced action IDs (tui.input.submit, tui.editor.cursorUp, app.interrupt, etc.), key format (modifier+key), full action tables.
pi-mono/packages/coding-agent/docs/prompt-templates.md — Markdown snippets invoked via /name, locations (~/.pi/agent/prompts/*.md, .pi/prompts/*.md, packages), positional arguments ($1, $2, $@, ${@:N}), YAML frontmatter with optional description.
pi-mono/packages/coding-agent/README.md — Context Files section for .pi/SYSTEM.md, ~/.pi/agent/SYSTEM.md, and APPEND_SYSTEM.md.
pi-mono/packages/coding-agent/docs/settings.md — the overall settings.json structure for tying these together.
Invariants
Theme Format: Themes define name (required, unique), optional vars for reusable color aliases, and all 51 colors tokens. There is no type, ui, syntax, or borders top-level key — everything is under colors. Loaded from ~/.pi/agent/themes/*.json (global) and .pi/themes/*.json (project).
Keybinding Config: Keybindings are configured in ~/.pi/agent/keybindings.json (not settings.json). IDs are namespaced: tui.input.submit (submit), tui.editor.cursorUp, app.interrupt, etc. Run /reload to apply changes without restarting.
Prompt Template Arguments: Templates use $1, $2, $@, ${@:N} positional syntax — not {variable} or <include>. The filename (minus .md) becomes the /name command.
System Prompt Override: Replace the default system prompt with .pi/SYSTEM.md (project) or ~/.pi/agent/SYSTEM.md (global). Use APPEND_SYSTEM.md to append instead of replace. Context files and skills are still appended after the override.
Workflows
Create a Theme: Copy dark.json from packages/coding-agent/src/modes/interactive/theme/, customize color values under the colors key, place it in ~/.pi/agent/themes/, and select via /settings or pi --theme <name>.
Override Keys: Create or edit ~/.pi/agent/keybindings.json mapping action IDs to key arrays (e.g., "tui.input.submit": ["ctrl+enter"]). Run /reload to apply.
Create a Prompt Template: Write a .md file in ~/.pi/agent/prompts/ with optional YAML frontmatter (description); use $1, $@ for arguments. Invoke with /filename in the editor.
Override the System Prompt: Create .pi/SYSTEM.md in the project or ~/.pi/agent/SYSTEM.md globally to replace the default system prompt. Use APPEND_SYSTEM.md at the same locations if you want to append custom instructions instead.
Anti-patterns
Do not hardcode keybindings into agent component source code — use the configurable namespaces from keybindings.md.
Do not put keybindings in settings.json — keybindings have their own file (~/.pi/agent/keybindings.json).
Do not use {variable} or <include src="..."> syntax in prompt templates — the actual syntax is $1, $@, ${@:N}.
Weekly Installs
17
Repository
romiluz13/pi-ag…t-skills
GitHub Stars
11
First Seen
11 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
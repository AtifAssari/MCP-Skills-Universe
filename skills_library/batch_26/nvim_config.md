---
title: nvim-config
url: https://skills.sh/stevvooe/dotfiles/nvim-config
---

# nvim-config

skills/stevvooe/dotfiles/nvim-config
nvim-config
Installation
$ npx skills add https://github.com/stevvooe/dotfiles --skill nvim-config
SKILL.md
Scope
config/nvim/
Rules
Follow the existing module layout and plugin organization.
Keep changes scoped to requested behavior; avoid unrelated cleanup.
Prefer clear mappings/options over dense abstractions.
Keep plugin-specific settings near the plugin configuration.
Follow repo workflow gates from config/opencode/AGENTS.md for non-trivial changes.
When to use
Adding/updating Neovim plugins and settings
Adjusting keymaps or editor behavior
Refactoring Neovim config structure in this repo
Workspace testing

Run Neovim against workspace config from the repo root:

XDG_CONFIG_HOME="$PWD/config" nvim


Run with isolated workspace-local data/state/cache:

mkdir -p .tmp/xdg-data .tmp/xdg-state .tmp/xdg-cache
XDG_CONFIG_HOME="$PWD/config" \
XDG_DATA_HOME="$PWD/.tmp/xdg-data" \
XDG_STATE_HOME="$PWD/.tmp/xdg-state" \
XDG_CACHE_HOME="$PWD/.tmp/xdg-cache" \
nvim


Smoke-test startup without opening UI:

XDG_CONFIG_HOME="$PWD/config" nvim --headless "+qa"

Weekly Installs
10
Repository
stevvooe/dotfiles
GitHub Stars
2
First Seen
Mar 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
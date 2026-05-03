---
title: mise
url: https://skills.sh/mritd/skills/mise
---

# mise

skills/mritd/skills/mise
mise
Installation
$ npx skills add https://github.com/mritd/skills --skill mise
SKILL.md
mise

Runtime version manager. Replaces nvm/pyenv/rbenv/asdf.

Install Runtime
# Install globally
mise use -g node@lts
mise use -g python@3.12
mise use -g go@latest

# Install for current project (creates mise.toml)
mise use node@20

Common Commands
mise ls                  # List installed
mise ls-remote node      # Available versions
mise where node          # Install path
mise install             # Install from config
mise uninstall node@20   # Remove version

Available Runtimes

Core (native): node, python, go, rust, ruby, java, swift, deno, bun, zig, elixir, erlang

Plugin-based: kotlin, scala, php, lua, perl, dotnet, dart, flutter, nim, crystal, julia, clojure

Package Managers
mise use -g pnpm@latest    # JS (npm alternative)
mise use -g uv@latest      # Python (pip alternative)
mise use -g maven@3        # Java
mise use -g gradle@latest  # Java

Java Vendors
mise use java@zulu-21      # Azul Zulu
mise use java@temurin-21   # Eclipse Temurin
mise use java@corretto-21  # Amazon Corretto

When Runtime Missing

If command fails with "not found":

# 1. Check if mise has it
mise search <runtime>

# 2. Install
mise use -g <runtime>@<version>

# 3. Retry original command

Config

Global: ~/.config/mise/config.toml Project: mise.toml or .tool-versions

Notes
rust (symlink): mise links to rustup. Use rustup for rust management.
Some brew packages depend on brew-installed runtimes. Check with brew uses --installed <pkg> before removing.
Weekly Installs
67
Repository
mritd/skills
First Seen
Jan 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
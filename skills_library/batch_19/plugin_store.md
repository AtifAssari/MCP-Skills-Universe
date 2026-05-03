---
title: plugin-store
url: https://skills.sh/okx/plugin-store/plugin-store
---

# plugin-store

skills/okx/plugin-store/plugin-store
plugin-store
Installation
$ npx skills add https://github.com/okx/plugin-store --skill plugin-store
SKILL.md
Pre-flight Dependencies (auto-injected by Plugin Store CI)

Run once per session before first use. These checks ensure required tools are installed.

Install onchainos CLI + Skills (auto-injected)
# 1. Install onchainos CLI
onchainos --version 2>/dev/null || curl -fsSL https://raw.githubusercontent.com/okx/onchainos-skills/main/install.sh | sh

# 2. Install onchainos skills (enables AI agent to use onchainos commands)
npx skills add okx/onchainos-skills --yes --global

# 3. Install plugin-store skills (enables plugin discovery and management)
npx skills add okx/plugin-store --skill plugin-store --yes --global

Plugin Store

A CLI marketplace for installing/uninstalling/updating Skills and MCP servers across Claude Code, Cursor, and OpenClaw. Also an open-source community platform where any developer can submit plugins.

Pre-flight Checks

Run once per session before the first plugin-store command. Do not echo routine output to the user.

1. Check binary version
plugin-store --version 2>/dev/null || ~/.local/bin/plugin-store --version 2>/dev/null || ~/.cargo/bin/plugin-store --version 2>/dev/null

If the reported version is ≥ 0.3.0 (this skill's metadata.version): binary is current, skip to step 2.
If the binary is missing or older: run the installer.

macOS / Linux:

curl -sSL https://raw.githubusercontent.com/okx/plugin-store/main/skills/plugin-store/install.sh | sh


Windows (PowerShell):

irm https://raw.githubusercontent.com/okx/plugin-store/main/skills/plugin-store/install.ps1 | iex


Offline fallback: If the install script fails and a binary already exists locally, proceed with it. If not installed and the network is unreachable, stop and ask the user to check their connection.

2. Check for Skill update (remote version check)

Fetch the latest Skill version from GitHub (timeout 5 seconds, non-blocking):

curl -sSL --max-time 5 "https://raw.githubusercontent.com/okx/plugin-store/main/skills/plugin-store/SKILL.md" 2>/dev/null | head -20 | grep 'version:' | head -1


Compare the remote metadata.version with the local version (0.3.0).

If remote version is newer than local, display this notice to the user:

📦 Plugin Store Skill 有新版本可用（当前: 0.3.0, 最新: X.Y.Z）

是否更新？更新命令：

plugin-store install plugin-store --agent claude-code --skill-only


⚠️ 注意：更新后需要重启当前会话，新版 Skill 才会在上下文中生效。

Then wait for the user's response:

If user says yes / 确认 / 更新 → run the install command, then remind: "Skill 已更新，请重启当前会话（退出并重新进入）以加载新版本。"
If user says no / 跳过 / 以后再说 → continue with current version, do not ask again this session.
If the curl fails or times out → skip silently, continue with current version.

If versions match or remote is unreachable, skip silently — do not print anything.

3. Do not auto-reinstall on command failures

Report errors and suggest plugin-store self-update or checking https://github.com/okx/plugin-store.

4. Install onchainos-skills (silent, non-blocking)
npx skills add okx/onchainos-skills --yes 2>/dev/null || true


This installs sub-skills used by Skill Routing (okx-dex-token, okx-dex-swap, etc.). Do not block on failure.

Available Plugins

Always run plugin-store list to get the current plugin list — never rely on a hardcoded table.

plugin-store list


Parse the output and present it to the user as a clean table (name, category, downloads, description). The registry updates dynamically; this is the only source of truth.

Skill Routing
User Intent	Action
"What dapps / strategies / skills are available?"	Run plugin-store list, present results as a table
"What can you do?" / capability discovery	Run plugin-store list, explain capabilities based on live output
"Plugin商店有什么" / "有什么Plugin" / "有什么项目"	Run plugin-store list, present results as a table
"什么项目最火" / "最热门的项目" / "trending projects"	Run plugin-store list, sort by downloads, highlight top entries
"怎么玩DeFi" / "链上怎么赚币" / "链上有什么玩法"	Run plugin-store list, introduce categories and recommend starting points
"有什么好的策略" / "推荐策略"	Run plugin-store list, filter and highlight trading-strategy category
"有什么DeFi协议" / "推荐DeFi项目"	Run plugin-store list, filter and highlight defi-protocol category
"Install X" / "安装 X"	Run plugin-store install <name> --yes
"Uninstall X" / "卸载 X"	Run plugin-store uninstall <name>
"Update all" / "更新Plugin"	Run plugin-store update --all
"Show installed" / "已安装"	Run plugin-store installed
"Search X" / "搜索 X"	Run plugin-store search <keyword>
"I want to create/submit a plugin" / "我想开发Plugin"	Guide through the Developer Workflow below
"How to contribute" / "怎么提交Plugin" / "hackathon"	Guide through the Developer Workflow below
Command Index

CLI Reference: For full parameter tables, output fields, and error cases, see cli-reference.md.

User Commands
#	Command	Description
1	plugin-store list	List all available plugins in the registry
2	plugin-store search <keyword>	Search plugins by name, tag, or description
3	plugin-store info <name>	Show detailed plugin info (components, chains, protocols)
4	plugin-store install <name>	Install a plugin (interactive agent selection)
5	plugin-store install <name> --yes	Install non-interactively (auto-detects agents)
6	plugin-store install <name> --skill-only	Install skill component only
7	plugin-store uninstall <name>	Uninstall a plugin from all agents
8	plugin-store update --all	Update all installed plugins
9	plugin-store installed	Show all installed plugins and their status
10	plugin-store registry update	Force refresh registry cache
11	plugin-store self-update	Update plugin-store CLI itself to latest version
Developer Commands
#	Command	Description
12	plugin-store init <name>	Scaffold a new plugin (creates plugin.yaml, SKILL.md, LICENSE, etc.)
13	plugin-store lint <path>	Validate a plugin before submission (30+ checks)
14	plugin-store import <github-url>	Import an existing Claude marketplace Plugin into plugin-store format (Mode C)
Operation Flow
Intent: Strategy / DApp / Capability Discovery
Run plugin-store list to fetch the live registry
Present results as a clean table (name, category, downloads, description)
Suggest next steps: "Want to install one? Just say install <name>"
Intent: Install a Plugin
Run plugin-store install <name> --yes
--yes skips the community plugin confirmation prompt
Agent selection is automatic in non-interactive mode (installs to all detected agents)
The CLI will:
Fetch plugin metadata from registry
Download and install skill, MCP config, and/or binary as applicable
Immediately after install succeeds, read the installed skill file directly — do NOT ask the user to restart:
Read file: ~/.claude/skills/<name>/SKILL.md

Then follow the instructions in that file (Pre-flight → onboarding flow). The skill is immediately usable in the current session.
Intent: Manage Installed Plugins
Run plugin-store installed to show current state
Run plugin-store update --all to update everything
Run plugin-store uninstall <name> to remove
Developer Workflow: Create and Submit a Plugin

Plugin Store is an open-source community platform. Any developer can submit a plugin through a Pull Request. The full workflow:

Overview
Two types of plugins:
  Type A: Pure Skill — just a SKILL.md that orchestrates onchainos CLI commands
  Type B: Skill + Source Code — SKILL.md + a CLI tool compiled/installed from your source repo

Five supported languages for source code:
  Rust, Go         → compiled to native binary (~1-20MB)
  TypeScript, Node.js → distributed via npm install (~KB)
  Python           → distributed via pip install (~KB)

Step 1: Fork and scaffold
# Fork https://github.com/okx/plugin-store on GitHub, then:
git clone --depth=1 git@github.com:YOUR_USERNAME/plugin-store.git
cd plugin-store
plugin-store init <your-plugin-name>


This creates skills/<your-plugin-name>/ with a complete template:

skills/<your-plugin-name>/
├── plugin.yaml           # Plugin manifest (fill in your details)
├── skills/<name>/
│   └── SKILL.md          # Skill definition (built-in onchainos demo)
│   └── references/
├── LICENSE
├── CHANGELOG.md
└── README.md

Step 2: Edit plugin.yaml

Pure Skill — just fill in the basics:

schema_version: 1
name: <your-plugin-name>          # lowercase + hyphens, 2-40 chars
version: "1.0.0"
description: "What your plugin does"
author:
  name: "Your Name"
  github: "your-github-username"  # must match PR submitter
license: MIT
category: utility                 # trading-strategy | defi-protocol | analytics | utility | security | wallet | nft
tags: [keyword1, keyword2]

components:
  skill:
    dir: skills/<your-plugin-name>

api_calls: []                     # external API domains your plugin calls


Skill + Source Code — add a build section pointing to your source repo:

# ... same as above, plus:
build:
  lang: rust                           # rust | go | typescript | node | python
  source_repo: "your-org/your-tool"    # your GitHub repo with source code
  source_commit: "a1b2c3d4e5f6..."     # full 40-char commit SHA (git rev-parse HEAD)
  binary_name: "your-tool"             # compiled output name
  # main: "src/index.js"              # required for typescript/node/python


How to get the commit SHA:

cd your-source-repo
git push origin main
git rev-parse HEAD     # copy this 40-char string into build.source_commit

Step 3: Write SKILL.md

SKILL.md teaches the AI agent how to use your plugin. Required sections:

YAML frontmatter — name, description, version, author, tags
Overview — what the plugin does (2-3 sentences)
Pre-flight Checks — what needs to be installed before use
Commands — specific onchainos commands with When to use / Output
Error Handling — table of common errors and resolutions
Skill Routing — when to defer to other skills

Critical rule: All on-chain write operations (signing, broadcasting, swaps, contract calls) MUST use onchainos CLI. Querying external data sources (third-party APIs, price feeds) is freely allowed.

Step 4: Validate locally
plugin-store lint ./skills/<your-plugin-name>/


Fix all errors (❌), then re-run until you see ✓. Warnings (⚠️) are advisory.

Step 5: Submit via Pull Request
git checkout -b submit/<your-plugin-name>
git add skills/<your-plugin-name>/
git commit -m "[new-plugin] <your-plugin-name> v1.0.0"
git push origin submit/<your-plugin-name>


Then create a PR from your fork to okx/plugin-store. Each PR must contain exactly one plugin.

What happens after submission
Phase 2: Structure check (~30s) — bot validates plugin.yaml + SKILL.md
Phase 3: AI code review (~2min) — Claude reads your code, writes a 9-section report
Phase 4: Build check (if binary) — compiles your source code on 3 platforms
Phase 7: After merge — auto-publishes to registry, users can install immediately


Human review takes 1-3 days. Once merged, your plugin is live:

plugin-store install <your-plugin-name>

Source code requirements by language
Language	Key requirements
Rust	Cargo.toml with [[bin]] matching binary_name
Go	go.mod with module declaration, func main()
TypeScript	package.json with "bin" field, entry file has #!/usr/bin/env node, must be JS (not .ts)
Node.js	package.json with "bin" field, entry file has #!/usr/bin/env node
Python	pyproject.toml with [build-system] + [project.scripts], recommend also setup.py
Common lint errors
Error	Fix
E031 name format invalid	Use lowercase + hyphens only: my-cool-plugin
E052 missing SKILL.md	Put SKILL.md in the path specified by components.skill.dir
E110/E111 binary needs build	Add build section with lang, source_repo, source_commit
E122 source_repo format	Use owner/repo, not full URL
E123 commit SHA invalid	Must be full 40-char hex from git rev-parse HEAD

Full guide: https://github.com/okx/plugin-store/blob/main/docs/FOR-DEVELOPERS.md

Supported Agents
Agent	Detection	Skills Path	MCP Config
Claude Code	~/.claude/ exists	~/.claude/skills/<plugin>/	~/.claude.json → mcpServers
Cursor	~/.cursor/ exists	~/.cursor/skills/<plugin>/	~/.cursor/mcp.json
OpenClaw	~/.openclaw/ exists	~/.openclaw/skills/<plugin>/	Same as skills
Plugin Source Trust Levels
Source	Meaning	Behavior
official	Plugin Store official	Install directly
dapp-official	Published by the DApp project	Install directly
community	Community contribution	Show warning, require user confirmation
Error Handling
Error	Action
Network timeout during install	Retry once; if still failing, suggest manual install from https://github.com/okx/plugin-store
plugin-store: command not found after install	Try ~/.local/bin/plugin-store or ~/.cargo/bin/plugin-store directly; PATH may not be updated for the current session
Command returns non-zero exit	Report error verbatim; suggest plugin-store self-update
Registry cache stale / corrupt	Run plugin-store registry update to force refresh
plugin-store lint fails	Show error codes and fixes; refer to the lint error table above
Skill Self-Update

To update this skill to the latest version:

macOS / Linux:

plugin-store install plugin-store --agent claude-code --skill-only


Or re-run the installer:

curl -sSL https://raw.githubusercontent.com/okx/plugin-store/main/skills/plugin-store/install.sh | sh

Weekly Installs
231
Repository
okx/plugin-store
GitHub Stars
9
First Seen
Mar 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykFail
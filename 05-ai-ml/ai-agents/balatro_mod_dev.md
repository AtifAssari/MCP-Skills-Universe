---
title: balatro-mod-dev
url: https://skills.sh/liafonx/open-balatro/balatro-mod-dev
---

# balatro-mod-dev

skills/liafonx/open-balatro/balatro-mod-dev
balatro-mod-dev
Installation
$ npx skills add https://github.com/liafonx/open-balatro --skill balatro-mod-dev
SKILL.md
Balatro Mod Development

Create and debug Balatro mods with Steamodded, Lovely, and SMODS.

Quick Agent Selection

When researching or writing code, spawn the right sub-agent via the Task tool:

Need to find...	Use agent	Model	Search boundary
Game function implementation	game-source-researcher	sonnet	Balatro_src/ only
SMODS API usage/hooks	smods-api-researcher	sonnet	smods/ only
How other mods do X	mod-pattern-researcher	sonnet	Mods/ folder only
Lovely patch syntax	lovely-patch-researcher	sonnet	lovely files only
Project architecture/exploration	project-explorer	sonnet	Current project only
Write code per plan	code-writer	sonnet	Current project only
Run temp script for data	script-runner	haiku	N/A (execution)
Review code for correctness	code-reviewer	opus	Current project only
Synthesize multi-source research	research-analyst	opus	Current project only
Plan complex implementation	strategic-planner	opus	Current project only
Inspect runtime logs, dumps, compat	debug-inspector	sonnet	Lovely logs/dumps only

The main agent handles directly: User interaction, small edits (<20 lines), presenting results.

Parallel: When researching DIFFERENT sources — spawn multiple Task calls in one message Sequential: When second query depends on first result

See references/sub-agents.md for the 5-phase workflow, iterative retrieval protocol, and delegation rules.

Repo Type Awareness

Auto-detection: Compare mod manifest author with git remote username.

# Get git remote username
git_user=$(git remote get-url origin 2>/dev/null | sed -E 's|.*[:/]([^/]+)/[^/]+\.git$|\1|' | tr '[:upper:]' '[:lower:]')

# Get mod author from manifest (first author, lowercase)
mod_author=$(jq -r '.author[0] // .author // ""' *.json 2>/dev/null | head -1 | tr '[:upper:]' '[:lower:]')

# Compare: match = own, no match = fork
[[ "$git_user" == "$mod_author" ]] && echo "own" || echo "fork"

Type	Detection	Implications
new	Empty repo (no files)	Full docs, Logger.lua, localization
own	Author matches git user	Full docs, standardize structure
fork	Author differs from git user	Minimal changes, temp logs only
File Convention
File	Purpose	Git
AGENTS.md	Mod structure, functions, dependencies, constraints, Quick Reference (for AI agents)	ignored
mod.config.json	File lists for sync/release scripts	ignored
docs/knowledge-base.md	Issues & lessons learned	ignored

AGENTS.md Purpose: Enable seamless handover between agents. Another agent should quickly understand mod structure, functions, dependencies, constraints, and repo type from a single file.

File Placement Rules

Only these .md files belong in root:

README.md, README_zh.md
CHANGELOG.md, CHANGELOG_zh.md
AGENTS.md
LICENSE.md

ALL other .md files MUST go in docs/

External References (No Symlinks Needed)

Access reference code directly via absolute paths. No setup required.

Source Locations (macOS)
Resource	Path
Game Source (desktop)	~/Development/GitWorkspace/Balatro_src/desktop/
Game Source (mobile)	~/Development/GitWorkspace/Balatro_src/ios_plus/
Steamodded Source	~/Development/GitWorkspace/smods/src/
Steamodded Lovely	~/Development/GitWorkspace/smods/lovely/
Lovely Docs	~/Development/GitWorkspace/lovely-injector/
Installed Mods	~/Library/Application Support/Balatro/Mods/
Lovely Logs	~/Library/Application Support/Balatro/Mods/lovely/log/
Source Locations (Windows)
Resource	Path
Game Source	Varies by setup
Installed Mods	%APPDATA%/Balatro/Mods/
Lovely Logs	%APPDATA%/Balatro/Mods/lovely/log/
Pattern References

Read these files for specific topics:

Topic	Reference File
Lovely.toml syntax	patterns/lovely-patches.md
SMODS hooks, config, localization	patterns/smods-api.md
Desktop vs mobile differences	patterns/mobile-compat.md
UIBox, CardArea, draw order	patterns/ui-system.md
Game source file map + search tips	references/game-files.md
G.GAME, G.STATES, G.P_* globals	references/globals.md
Lua/LuaJIT pitfalls, common mod bugs	references/lua-gotchas.md
New Mod Setup (type: new)
Templates in ${CLAUDE_PLUGIN_ROOT}/templates/ folder:
File	Purpose
agents-md-template.md	AGENTS.md template for standard mods
agents-texture-pack-template.md	AGENTS.md for Malverk texture packs
mod-config-template.json	Script configuration
gitignore-template	Standard .gitignore
logger-template.lua	Centralized logging utility
Meta Files:
File	Purpose
mod-json-template.json	SMODS mod manifest ({ModName}.json)
manifest-json-template.json	Thunderstore manifest
User Docs in templates/docs/:
File	Purpose
description-template.md	Concise README for docs/
NEXUSMODS_DESCRIPTION-template.txt	BBCode for NexusMods
knowledge-base-template.md	Issues & lessons learned
Basic Mod Structure (new repos):
{ModName}/
├── main.lua                 # Entry point, mod registration
├── config.lua               # Config defaults (optional)
├── lovely.toml              # Lovely patches (if needed)
├── {ModName}.json           # SMODS mod manifest
├── manifest.json            # Thunderstore manifest
├── mod.config.json          # Script configuration
├── Utils/
│   └── Logger.lua           # Centralized logging
├── localization/
│   ├── en-us.lua            # English (required)
│   └── zh_CN.lua            # Chinese
├── assets/                  # Sprites, shaders
├── scripts/                 # Utility scripts
└── docs/                    # Documentation

Available Commands (16 total — plugin-bundled, auto-loaded)
/balatro-mod-dev:familiar - Get familiar with this mod (reads AGENTS.md, maps architecture)
/balatro-mod-dev:init - Initialize new mod
/balatro-mod-dev:sync-mod - Start sync with watch mode (run once at start)
/balatro-mod-dev:bump-version [patch|minor|major] - Increment version, update changelogs
/balatro-mod-dev:release - Create release packages (auto-detects version from manifests)
/balatro-mod-dev:fix-sprites <directory> [--preview] - Fix grey borders on sprites
/balatro-mod-dev:refactor [focus-area] - Review code for redundancy, outdated fallbacks, modularization
/balatro-mod-dev:debug - Verify fix by checking Lovely logs (auto-detects mod key from repo)
/balatro-mod-dev:test [scenario] - Run test scenarios and verify mod behavior via Lovely logs
/balatro-mod-dev:draft-pr - Draft PR message (for forks)
/balatro-mod-dev:check - Audits project health, scaffolds missing rules
/balatro-mod-dev:update-docs - Review all docs for accuracy, staleness, duplication, verbosity
/balatro-mod-dev:update-plugin - Update plugin based on new knowledge
/balatro-mod-dev:knowledge - Review session work, capture discoveries
/balatro-mod-dev:compact - Evaluate whether to compact context now
/balatro-mod-dev:help - List all available commands and agents
Sub-agents (11 total — plugin-bundled)
game-source-researcher - Find game functions and injection points (sonnet)
smods-api-researcher - Find SMODS API patterns and usage (sonnet)
mod-pattern-researcher - Find how other mods implement features (sonnet)
lovely-patch-researcher - Find Lovely patch syntax and examples (sonnet)
project-explorer - Extensive codebase exploration (sonnet)
code-writer - Execute implementation plans, write code (sonnet)
script-runner - Run temp scripts and return results (haiku)
code-reviewer - Review code for correctness and edge cases (opus)
research-analyst - Synthesize findings from multiple researchers (opus)
strategic-planner - Plan implementation strategy for complex features (opus)
debug-inspector - Inspect runtime logs, dumps, mod compatibility (sonnet)
Logging
For new/my repos:

Use Utils/Logger.lua (from ${CLAUDE_PLUGIN_ROOT}/templates/logger-template.lua):

local Logger = require("Utils.Logger")
local log = Logger.create("ModuleName")
log("info", "Initialized")
log("error", "Failed: " .. err)

For forks/others' repos:

Use temp logs only (remove before PR):

pcall(print, "[Debug] checkpoint: " .. tostring(var))

Utility Scripts
Script	Purpose
${CLAUDE_PLUGIN_ROOT}/scripts/sync_to_mods.template.sh	Sync mod files to game's Mods folder
${CLAUDE_PLUGIN_ROOT}/scripts/create_release.template.sh	Create release packages
${CLAUDE_PLUGIN_ROOT}/scripts/fix_transparent_pixels.py	Fix grey borders on sprites
Workflow: Debugging
Check references/lua-gotchas.md for known pitfalls (FFI cdata, nil scoping, boolean normalization)
Check platform (desktop vs mobile)
Search game source for function
Check other mods for implementations
Add logs (Logger.lua for own, temp for fork)
Check Lovely logs
If fix fails 3+ times: Invoke research-analyst (opus) to synthesize all debugging context
Workflow: Update User Docs

When user says "update all user docs":

Review ALL files: README(_zh).md, CHANGELOG(_zh).md
Review docs/: description.md, NEXUSMODS_DESCRIPTION.txt
Update version in {ModName}.json, manifest.json
Ensure EN/ZH consistency
Weekly Installs
42
Repository
liafonx/open-balatro
GitHub Stars
2
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn
---
title: se-dev-mod
url: https://skills.sh/viktor-ferenczi/se-dev-skills/se-dev-mod
---

# se-dev-mod

skills/viktor-ferenczi/se-dev-skills/se-dev-mod
se-dev-mod
Installation
$ npx skills add https://github.com/viktor-ferenczi/se-dev-skills --skill se-dev-mod
SKILL.md
SE Dev Mod Skill

Mod development for Space Engineers version 1.

⚠️ CRITICAL: Commands run in a UNIX shell (busybox), NOT Windows CMD. Use bash syntax!

Examples:

✅ test -f file.txt && echo exists
✅ ls -la | head -10
❌ if exist file.txt (echo exists) - This will NOT work

Actions:

prepare: Run the one-time preparation (Prepare.bat)
bash: Run UNIX shell commands via busybox
search: Search mod code using search_mods.py
Routing Decision

Check these patterns in order - first match wins:

Priority	Pattern	Example	Route
1	Empty or bare invocation	se-dev-mod	Show this help
2	Prepare keywords	se-dev-mod prepare, se-dev-mod setup, se-dev-mod init	prepare
3	Bash/shell keywords	se-dev-mod bash, se-dev-mod grep, se-dev-mod cat	bash
4	Search keywords	se-dev-mod search, se-dev-mod find class, se-dev-mod lookup	search
Getting Started

⚠️ CRITICAL: Before running ANY commands, read CommandExecution.md to avoid common mistakes that cause command failures.

If the Prepare.DONE file is missing in this folder, you MUST run the one-time preparation steps first. See the prepare action.

Essential Documentation
CommandExecution.md - ⚠️ READ THIS FIRST - How to run commands correctly on Windows
Mod Development

Use only names matching the Mod API whitelist: ModApiWhitelist.txt The whitelist was exported from game version 1.208.015 using MDK2's Mdk.Extractor.

Mods are released on the Steam Workshop or Mod.IO, mostly on the former. Mods are compiled by the game on world loading with a Mod API whitelist enforced, which is supposed to guarantee safety and security. Mods may still crash the game with an exception.

Use the se-dev-game-code skill to search the game's decompiled code. You may need this to understand how the game's internals work and how to interface with it properly. Stick to game code searches corresponding to names on the Mod API whitelist for efficiency.

Folder Structure
Data/ — junction to %USERPROFILE%\.se-dev\mod. Persistent skill data lives here:
Data/mods.json — quick inventory of all installed mods (workshop_id, path, has_scripts, ...).
Data/mod_hashes.json — per-mod aggregate sha1 used by the indexer for change detection.
Data/CodeIndex/ — full Tree-sitter C# index (one CSV per category, plus hierarchy trees).
LocalMods/ — junction to %AppData%\SpaceEngineers\Mods, the game's local-mod folder.
Steam Workshop content is read in-place from the Steam folder; it is not copied or symlinked into the skill. The workshop folder is resolved from SE_GAME_ROOT (env var) or the Steam registry entry for app id 244850.
References
Mod Template repo Mod template repository to start a new mod project which will include scripts. See ModTemplate.md
Mod API for script mods Structured Mod API documentation
Mod API documentation by Keen Software House May be outdated
Mod Development Kit (MDK2) Mod development tooling mostly for VS2022
Mod Code Search

Search the source code of Steam and local mods for examples and patterns:

# Search for patterns
uv run search_mods.py class declaration MyBlock
uv run search_mods.py method usage Update
uv run search_mods.py class children MyGameLogicComponent

# Count results before viewing (useful for large result sets)
uv run search_mods.py class usage Init --count

# Limit number of results
uv run search_mods.py class usage Init --limit 10


Before searching, ensure the index exists. If Data/CodeIndex/ is missing, run:

uv run list_mods.py     # quick inventory (always cheap)
uv run index_mods.py    # full code index (incremental: only changed mods reparsed)


Re-indexing after new subscriptions: When you subscribe to new mods on Steam Workshop, load them in a world once (so the game downloads them), then re-run the two commands above (or just Prepare.bat). The indexer hashes each mod's .cs files and only reparses mods whose hash changed since the previous run, so reruns are fast.

See search action for complete documentation.

Action References

Follow the detailed instructions in:

prepare action - One-time preparation
bash action - Running UNIX shell commands via busybox
search action - Search mod code for examples
Remarks

The original source of this skill: https://github.com/viktor-ferenczi/se-dev-skills

Weekly Installs
45
Repository
viktor-ferenczi…v-skills
GitHub Stars
5
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
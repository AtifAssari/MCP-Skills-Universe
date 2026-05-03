---
rating: ⭐⭐⭐
title: se-dev-script
url: https://skills.sh/viktor-ferenczi/se-dev-skills/se-dev-script
---

# se-dev-script

skills/viktor-ferenczi/se-dev-skills/se-dev-script
se-dev-script
Installation
$ npx skills add https://github.com/viktor-ferenczi/se-dev-skills --skill se-dev-script
SKILL.md
SE Dev Script Skill

In-game (programmable block, aka PB) script development for Space Engineers version 1.

⚠️ CRITICAL: Commands run in a UNIX shell (busybox), NOT Windows CMD. Use bash syntax!

Examples:

✅ test -f file.txt && echo exists
✅ ls -la | head -10
❌ if exist file.txt (echo exists) - This will NOT work

Actions:

prepare: Run the one-time preparation (Prepare.bat)
bash: Run UNIX shell commands via busybox
search: Search script code using search_scripts.py
Routing Decision

Check these patterns in order - first match wins:

Priority	Pattern	Example	Route
1	Empty or bare invocation	se-dev-script	Show this help
2	Prepare keywords	se-dev-script prepare, se-dev-script setup, se-dev-script init	prepare
3	Bash/shell keywords	se-dev-script bash, se-dev-script grep, se-dev-script cat	bash
4	Search keywords	se-dev-script search, se-dev-script find class, se-dev-script lookup	search
Getting Started

⚠️ CRITICAL: Before running ANY commands, read CommandExecution.md to avoid common mistakes that cause command failures.

If the Prepare.DONE file is missing in this folder, you MUST run the one-time preparation steps first. See the prepare action.

Essential Documentation
CommandExecution.md - ⚠️ READ THIS FIRST - How to run commands correctly on Windows
Script Development

Use only names matching the PB API whitelist: PBApiWhitelist.txt The whitelist was exported from game version 1.208.015 using MDK2's Mdk.Extractor.

In-game (PB) scripts are released on the Steam Workshop or Mod.IO, mostly on the former. In-game scripts are compiled by the game on loading into the PB or world loading (if the PB has a script loaded) with a PB Script API whitelist enforced, which is supposed to guarantee safety and security. Scripts cannot crash the game, since any exception is caught and the script is killed by the game. Scripts can still lag the game if no specific resource usage enforcement is set up by the player or server admin.

The script's source code size is limited to 100,000 bytes when the player loads it. The ScriptDev plugin can load more from local file into offline (local) games for testing purposes, therefore scripts can be tested without source code compression, which is useful to get fully detailed exception tracebacks.

Use the se-dev-game-code skill to search the game's decompiled code. You may need this to understand how the game's internals work and how to script it properly. Stick to game code searches corresponding to names on the PB API whitelist for efficiency.

Folder Structure
Data/ — junction to %USERPROFILE%\.se-dev\script. Persistent skill data lives here:
Data/scripts.json — quick inventory of all installed PB scripts.
Data/script_hashes.json — per-script aggregate sha1 used by the indexer for change detection.
Data/CodeIndex/ — full Tree-sitter C# index (one CSV per category, plus hierarchy trees).
LocalScripts/ — junction to %AppData%\SpaceEngineers\IngameScripts\local, the game's local-PB-script folder.
Steam Workshop content is read in-place from the Steam folder; it is not copied or symlinked into the skill. PB scripts are detected by the presence of a top-level Script.cs file inside each numeric workshop folder. The workshop folder is resolved from SE_GAME_ROOT (env var) or the Steam registry entry for app id 244850.
References
Script Template repo PB script template repository to start a new project. See ScriptTemplate.md
Script Merge tool Merging PB scripts from C# projects into single file with optional code compression. See ScriptMerge.md
Script Dev plugin Automatic script loading into the PB in-game for easier testing. See ScriptDev.md
Mod Development Kit (MDK2)
Programmable Block API
Wiki on Scripting
Script Code Search

Search the source code of Steam and local PB scripts for examples and patterns:

# Search for patterns
uv run search_scripts.py class declaration Program
uv run search_scripts.py method usage Main
uv run search_scripts.py class children MyGridProgram

# Count results before viewing (useful for large result sets)
uv run search_scripts.py class usage Program --count

# Limit number of results
uv run search_scripts.py class usage GridTerminalSystem --limit 30


Before searching, ensure the index exists. If Data/CodeIndex/ is missing, run:

uv run list_scripts.py     # quick inventory (always cheap)
uv run index_scripts.py    # full code index (incremental: only changed scripts reparsed)


Re-indexing after new subscriptions: When you subscribe to new scripts on Steam Workshop, load them in a world once (so the game downloads them), then re-run the two commands above (or just Prepare.bat). The indexer hashes each script's .cs files and only reparses scripts whose hash changed since the previous run, so reruns are fast.

See search action for complete documentation.

Action References

Follow the detailed instructions in:

prepare action - One-time preparation
bash action - Running UNIX shell commands via busybox
search action - Search script code for examples
Remarks

The original source of this skill: https://github.com/viktor-ferenczi/se-dev-skills

Weekly Installs
37
Repository
viktor-ferenczi…v-skills
GitHub Stars
5
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykWarn
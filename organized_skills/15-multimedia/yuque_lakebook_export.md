---
rating: ⭐⭐⭐
title: yuque-lakebook-export
url: https://skills.sh/yangsonhung/awesome-agent-skills/yuque-lakebook-export
---

# yuque-lakebook-export

skills/yangsonhung/awesome-agent-skills/yuque-lakebook-export
yuque-lakebook-export
Installation
$ npx skills add https://github.com/yangsonhung/awesome-agent-skills --skill yuque-lakebook-export
SKILL.md
Yuque Lakebook Export

Convert one or more Yuque .lakebook files into local Markdown folders, with images and internal document links prepared for Obsidian.

When to Use

Use this skill when the user asks for:

Exporting one or more Yuque .lakebook files
Converting a Yuque knowledge base into Markdown
Migrating Yuque content into Obsidian
Fixing Yuque export issues around images, cropped images, internal links, hierarchy, or tables
Do not use

Do not use this skill for:

Generic Markdown editing that does not involve Yuque or .lakebook
Website scraping tasks
Export tasks that already come from a non-Yuque format
Instructions
Prefer non-interactive execution so the agent can run deterministically.
Before any non-interactive export, the agent must confirm the output root directory with the user. Do not choose an output directory on the user's behalf.
If the user has not provided an output directory, ask a concise question and wait for the user's answer before running the export command.
Prefer uv consistently. Do not create temporary .venv or similar task-local environments in the working directory.
Before running any uv command, first check whether uv is available in the environment.
If uv is not installed or not available in PATH, the agent must ask the user for confirmation before installing uv. Do not install it silently.
Before running uv sync or uv run python scripts/cli.py ..., the agent must first switch into the installed skill tool directory, meaning the directory that contains this SKILL.md, pyproject.toml, uv.lock, and scripts/. Do not run these commands directly from the .lakebook source directory, the output directory, or the user's current workspace root.
Use this entrypoint for agent execution:
uv run python scripts/cli.py

Sync dependencies before first use:
uv sync

Recommended command order:
cd /path/to/installed-skill-root
uv sync
uv run python scripts/cli.py ...

Standard single-file execution:
uv run python scripts/cli.py -l "/path/to/your_file.lakebook" -o "/target/root"

Standard batch execution:
uv run python scripts/cli.py -l "/path/to/your_file_1.lakebook" "/path/to/your_file_2.lakebook" -o "/target/root"

Although scripts/cli.py still supports interactive terminal selection for manual human use, agents must not rely on interactive mode because they cannot reliably capture terminal interaction state. Always pass explicit -l and -o arguments.
Do not manually create temporary virtual environments in the current working directory, the user's download directory, or any task directory; dependencies should be managed by uv from the skill tool directory.
Some Yuque exports include <!doctype lake> at the start of the document body; older implementations could render this as a stray lake## prefix in Markdown. The current skill implementation already handles this case.
After export, verify:
.md files exist
sibling .assets folders exist
internal links are relative Markdown paths
images render in Obsidian
exported documents do not start with an erroneous lake## prefix
If export fails, inspect the batch log written next to the input .lakebook files.

For detailed behavior, troubleshooting, and output rules, read references/usage.md.

Weekly Installs
10
Repository
yangsonhung/awe…t-skills
GitHub Stars
3
First Seen
Apr 4, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn
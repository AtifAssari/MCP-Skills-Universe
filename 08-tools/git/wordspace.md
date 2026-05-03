---
rating: ⭐⭐⭐
title: wordspace
url: https://skills.sh/frames-engineering/wordspace/wordspace
---

# wordspace

skills/frames-engineering/wordspace/wordspace
wordspace
Originally fromframes-engineering/skills
Installation
$ npx skills add https://github.com/frames-engineering/wordspace --skill wordspace
Summary

CLI for bootstrapping wordspace projects with reusable .prose workflows from GitHub.

Three core commands: init to set up a new project with interactive workflow selection, search to filter available workflows, and add to download specific workflows by name
Interactive workflow picker during init supports flexible selection syntax (individual numbers, ranges, or "all"/"none")
Automatically creates project structure with .claude/settings.local.json for Claude permissions, workflows/ directory for .prose files, and output/ working directory
Requires Node.js and npx; in CI environments, init automatically downloads all workflows instead of prompting
SKILL.md
Wordspace

Wordspace is a CLI tool that bootstraps project workspaces with workflows — reusable .prose programs fetched from GitHub.

When to activate

Activate this skill when the user:

Wants to set up a new wordspace project
Wants to browse, search, or add workflows
Mentions "wordspace" by name
Asks about available workflows or how to get new ones
Commands
wordspace init

Bootstrap a new project in the current directory. Runs three steps:

Workflows — Fetches available .prose workflows from GitHub and presents an interactive picker. The user selects which ones to download. In CI (non-TTY), all workflows are downloaded automatically.
Claude settings — Creates .claude/settings.local.json with base permissions (curl, python3, WebFetch, WebSearch).
Directories — Creates the output/ directory.

Use --force to re-download workflows that already exist locally.

wordspace search [query]

List all available workflows from the remote repository. Optionally filter by a substring query.

wordspace search            # list all
wordspace search pulse      # filter by "pulse"

wordspace add <name> [...]

Download one or more specific workflows by name. Automatically appends .prose if missing.

wordspace add x-daily-pulse
wordspace add x-daily-pulse x-weekly-report
wordspace add x-daily-pulse --force    # overwrite existing

Project structure after init
project/
├── .claude/
│   └── settings.local.json    # Claude permissions
├── workflows/
│   └── *.prose                # downloaded workflow files
├── output/                    # working directory for outputs
└── skills/
    └── wordspace/
        └── SKILL.md           # this file

Workflow picker (during init)

When running wordspace init, the CLI presents a numbered list of available workflows. The user can respond with:

all or press Enter — download everything
none or 0 — skip workflow download
1,3,5 — pick specific numbers
1-3 — pick a range
1,3-5,7 — mix of both
Installation
npx wordspace init


Or install globally:

npm i -g wordspace
wordspace init

Weekly Installs
984
Repository
frames-engineer…ordspace
GitHub Stars
2
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn
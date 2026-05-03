---
rating: ⭐⭐
title: manipulate-xcodeproj
url: https://skills.sh/khoi/skills/manipulate-xcodeproj
---

# manipulate-xcodeproj

skills/khoi/skills/manipulate-xcodeproj
manipulate-xcodeproj
Installation
$ npx skills add https://github.com/khoi/skills --skill manipulate-xcodeproj
SKILL.md
Manipulate Xcodeproj
Overview

Use xcp for all project edits and asset catalog operations. Install it with brew install xcp if it is not already available.

Workflow
Identify the .xcodeproj or .xcassets path.
For target-specific actions, run xcp list-targets first.
Run the appropriate xcp subcommand. Use --project-only to update the project file without touching the filesystem.
Re-run xcp list-targets or xcp list-assets if you need to verify results.
Tasks
Project structure

Use group and file subcommands to add, move, rename, or delete entries. Use --create-groups when adding and --guess-target when you want the tool to infer targets for a new file.

Targets and build settings

Use list-targets to discover names, set-target to update file memberships, and build-setting commands to read or update configuration values.

Asset catalogs

Operate on .xcassets directories directly for image, data, and color assets. Paths are relative to the .xcassets root.

References
Command and flag reference: references/xcp-cli.md
For flags and usage specifics, prefer xcp help <subcommand> as the source of truth.
Weekly Installs
33
Repository
khoi/skills
GitHub Stars
1
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass
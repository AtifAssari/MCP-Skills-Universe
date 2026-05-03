---
title: snipgrapher
url: https://skills.sh/mcollina/skills/snipgrapher
---

# snipgrapher

skills/mcollina/skills/snipgrapher
snipgrapher
Installation
$ npx skills add https://github.com/mcollina/skills --skill snipgrapher
SKILL.md
When to use

Use this skill when you need to:

Generate image snippets from source code
Configure reusable snippet rendering defaults
Batch-render snippet assets for docs, social posts, or changelogs
Use published snipgrapher from npm to generate snippet images
Quick start

Render a single file to a PNG immediately with no config required:

npx snipgrapher render file.ts -o output.png


For ongoing use, initialise a project config first, then render:

npx snipgrapher init          # creates snipgrapher.config.json
npx snipgrapher render file.ts --profile default -o output.png


After rendering, verify the output exists and is non-zero in size before treating the job as successful:

ls -lh output.png   # confirm file exists and size > 0

How to use

Read these rule files in order:

rules/setup-and-configuration.md - Install, select executable, initialize config, and define profiles
rules/rendering-workflows.md - Render single snippets, batch jobs, watch mode, and output practices
Core principles
Configure first: establish a project config before repeated renders
Reproducible output: prefer named profiles and explicit output paths
Portable commands: use command patterns that work with installed binaries and npx
Automation-friendly: rely on CLI flags/config/env precedence intentionally
Troubleshooting common render failures

If a render fails or produces an unexpected output, check for these common causes:

Missing fonts: ensure any custom font specified in the profile or config is installed on the system
Unsupported syntax: confirm the language/extension is supported by snipgrapher; fall back to plain text highlighting if not
Empty or corrupt output: re-run with --verbose (if supported) to surface error details, and verify the input file is readable and non-empty
Profile not found: run npx snipgrapher init to regenerate snipgrapher.config.json if the config file is missing or malformed
Weekly Installs
350
Repository
mcollina/skills
GitHub Stars
1.8K
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass
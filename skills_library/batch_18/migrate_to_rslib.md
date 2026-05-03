---
title: migrate-to-rslib
url: https://skills.sh/rstackjs/agent-skills/migrate-to-rslib
---

# migrate-to-rslib

skills/rstackjs/agent-skills/migrate-to-rslib
migrate-to-rslib
Installation
$ npx skills add https://github.com/rstackjs/agent-skills --skill migrate-to-rslib
SKILL.md
Migrate to Rslib
Goal

Migrate tsc and tsup projects to Rslib with minimal behavior changes and clear verification.

Supported source frameworks
tsc
tsup
Migration principles (must follow)
Official guide first: treat Rslib migration docs as source of truth.
Smallest-change-first: complete baseline migration first, then migrate advanced or custom behavior.
Do not change business logic: avoid touching source or business logic unless user explicitly asks.
Validate before cleanup: keep old tool dependencies/config temporarily if needed; remove only after Rslib is green.
Workflow

Detect source tool

tsup
Config: tsup.config.*
Dependency: tsup
Build script: uses tsup to build projects
tsc
Config: tsconfig.json or tsconfig.*.json
Dependency: typescript
Build script: uses tsc to build projects. And it should be noted that tsc used only for type checking (e.g., tsc --noEmit) does not make it a tsc build project.

Apply tool-specific migration deltas

tsc: references/tsc.md
tsup: references/tsup.md

Validate behavior

Run build command to verify the project builds successfully.
If issues remain, compare the old project configuration with the migration guide and complete any missing mappings.

Cleanup and summarize

Remove obsolete dependencies/config only after validation passes.
Summarize changed files, mapped options, and any remaining manual follow-ups.
Weekly Installs
57
Repository
rstackjs/agent-skills
GitHub Stars
65
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
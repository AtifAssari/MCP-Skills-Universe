---
title: migrate-to-rsbuild
url: https://skills.sh/rstackjs/agent-skills/migrate-to-rsbuild
---

# migrate-to-rsbuild

skills/rstackjs/agent-skills/migrate-to-rsbuild
migrate-to-rsbuild
Installation
$ npx skills add https://github.com/rstackjs/agent-skills --skill migrate-to-rsbuild
SKILL.md
Migrate to Rsbuild
Goal

Migrate webpack, Vite, create-react-app (CRA/CRACO), or Vue CLI projects to Rsbuild with minimal behavior changes and clear verification.

Supported source frameworks
webpack
Vite
CRA / CRACO
Vue CLI
Migration principles (must follow)
Official guide first: treat Rsbuild migration docs as source of truth.
Smallest-change-first: complete baseline migration first, then migrate custom behavior.
Do not change business logic: avoid touching app runtime code unless user explicitly asks.
Validate before cleanup: keep old tool dependencies/config temporarily if needed; remove only after Rsbuild is green.
Workflow

Detect source framework

Check package.json dependencies/scripts and config files:
webpack: webpack.config.*
Vite: vite.config.*
CRA/CRACO: react-scripts, @craco/craco, craco.config.*
Vue CLI: @vue/cli-service, vue.config.*

Apply framework-specific deltas

webpack: references/webpack.md
Vite: references/vite.md
CRA/CRACO: references/cra.md
Vue CLI: references/vue-cli.md

Validate behavior

Run dev server to verify the project starts without errors.
Run build command to verify the project builds successfully.
If issues remain, compare the old project configuration with the migration guide and complete any missing mappings.

Cleanup and summarize

Remove obsolete dependencies/config only after validation passes.
Summarize changed files and any remaining manual follow-ups.
Weekly Installs
86
Repository
rstackjs/agent-skills
GitHub Stars
65
First Seen
Feb 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
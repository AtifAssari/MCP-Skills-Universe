---
title: rsbuild-v2-upgrade
url: https://skills.sh/rstackjs/agent-skills/rsbuild-v2-upgrade
---

# rsbuild-v2-upgrade

skills/rstackjs/agent-skills/rsbuild-v2-upgrade
rsbuild-v2-upgrade
Installation
$ npx skills add https://github.com/rstackjs/agent-skills --skill rsbuild-v2-upgrade
SKILL.md
Rsbuild v1 to v2 Upgrade
Workflow

Confirm current setup

Read package.json to identify Rsbuild and plugin packages in use.
Locate the Rsbuild config file (commonly rsbuild.config.(ts|js|mjs|cjs)).

Open the official upgrade guide

Use the v1 → v2 guide as the source of truth:
https://rsbuild.rs/guide/upgrade/v1-to-v2

Plan the upgrade path

Compare the current project config with the migration guide.
List breaking changes that apply to the project’s current config and plugins.
Note any removed or renamed options, defaults, or plugin APIs.

Update dependencies

Bump @rsbuild/core to v2
Bump Rsbuild plugins to latest versions via npx taze major --include /rsbuild/ -w -r

Apply config and code changes

Update the Rsbuild config to match v2 options and defaults.
Remove deprecated or unsupported settings.

Validate

Run the build and dev commands.
Run project tests or type checks.
Fix any warnings or errors surfaced by the new version.
Weekly Installs
160
Repository
rstackjs/agent-skills
GitHub Stars
65
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
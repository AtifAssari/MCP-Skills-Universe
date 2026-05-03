---
rating: ⭐⭐⭐
title: btca-cli
url: https://skills.sh/davis7dotsh/better-context/btca-cli
---

# btca-cli

skills/davis7dotsh/better-context/btca-cli
btca-cli
Installation
$ npx skills add https://github.com/davis7dotsh/better-context --skill btca-cli
Summary

Source-first CLI for grounding questions in git repos, local directories, and npm packages.

Add and manage resources (git repositories, local directories, npm packages) via btca add, then query them with btca ask using resource names or anonymous one-off URLs
Ask questions across multiple resources simultaneously to cross-reference answers and connect concepts
Configuration stored in btca.config.jsonc at project and global levels; project config overrides global settings and controls provider/model selection
Supports both named persistent resources for ongoing work and ephemeral anonymous resources for one-time lookups without saving to config
SKILL.md
btca CLI

btca is a source-first research CLI. It hydrates resources (git, local, npm) into searchable context, then answers questions grounded in those sources. Use configured resources for ongoing work, or one-off anonymous resources directly in btca ask.

Full CLI reference: https://docs.btca.dev/guides/cli-reference

Add resources:

# Git resource
btca add -n svelte-dev https://github.com/sveltejs/svelte.dev

# Local directory
btca add -n my-docs -t local /absolute/path/to/docs

# npm package
btca add npm:@types/node@22.10.1 -n node-types -t npm


Verify resources:

btca resources


Ask a question:

btca ask -r svelte-dev -q "How do I define remote functions?"

Common Tasks
Ask with multiple resources:
btca ask -r react -r typescript -q "How do I type useState?"

Ask with anonymous one-off resources (not saved to config):
# One-off git repo
btca ask -r https://github.com/sveltejs/svelte -q "Where is the implementation of writable stores?"

# One-off npm package
btca ask -r npm:react@19.0.0 -q "How is useTransition exported?"

Config Overview
Config lives in btca.config.jsonc (project) and ~/.config/btca/btca.config.jsonc (global).
Project config overrides global and controls provider/model and resources.
Troubleshooting
"No resources configured": add resources with btca add ... and re-run btca resources.
"Provider not connected": run btca connect and follow the prompts.
"Unknown resource": use btca resources for configured names, or pass a valid HTTPS git URL / npm:<package> as an anonymous one-off in btca ask.
Weekly Installs
614
Repository
davis7dotsh/bet…-context
GitHub Stars
1.1K
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
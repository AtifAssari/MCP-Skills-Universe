---
title: pnpm
url: https://skills.sh/onmax/nuxt-skills/pnpm
---

# pnpm

skills/onmax/nuxt-skills/pnpm
pnpm
Installation
$ npx skills add https://github.com/onmax/nuxt-skills --skill pnpm
Summary

Node.js dependency management with monorepo workspaces, catalogs, and supply chain security features.

Supports workspace protocol for internal package linking, centralized version catalogs, and transitive dependency overrides to resolve conflicts
Includes patch functionality for third-party packages, content-addressable store for efficiency, and strict dependency resolution
Provides filtering and scripting commands for running tasks across monorepo packages or targeting specific workspaces
Reference documentation covers CLI commands, workspace configuration, advanced features like patches and hooks, and CI/CD pipeline setup
SKILL.md
pnpm

Content-addressable store, strict deps, workspace protocol, catalogs.

When to Use
Installing/managing npm packages
Monorepo workspace setup with catalogs
Overriding transitive dependencies
Patching third-party packages
CI/CD configuration for pnpm projects
Supply chain security hardening
Quick Start
pnpm install                      # Install deps
pnpm add <pkg>                    # Add dep
pnpm add -D <pkg>                 # Dev dep
pnpm -r run build                 # Run in all packages
pnpm --filter @myorg/app build    # Run in specific package

Workspace Setup
# pnpm-workspace.yaml
packages:
  - 'packages/*'
  - 'apps/*'

# Catalogs for centralized version management
catalog:
  react: ^18.2.0
  typescript: ~5.3.0

// package.json - Use workspace protocol and catalogs
{
  "packageManager": "pnpm@10.28.2",
  "dependencies": {
    "@myorg/utils": "workspace:^",
    "react": "catalog:"
  }
}

Reference Files
Task	File
Commands, scripts, filtering	cli.md
Workspaces, catalogs, config	workspaces.md
Overrides, patches, hooks, store	features.md
CI/CD, Docker, migration	ci.md
Loading Files

Consider loading these reference files based on your task:

 references/cli.md - if using pnpm commands, scripts, or filtering
 references/workspaces.md - if setting up monorepo, catalogs, or workspace config
 references/features.md - if using overrides, patches, hooks, or managing store
 references/ci.md - if configuring CI/CD, Docker, or migrating from npm/yarn

DO NOT load all files at once. Load only what's relevant to your current task.

Verify Setup

After configuring a workspace, verify it works:

pnpm install          # Install all deps
pnpm ls --depth 0     # Verify workspace links
pnpm -r run build     # Build all packages

Cross-Skill References
TypeScript libs → Use ts-library skill for library patterns
Build tooling → Use tsdown or vite skills
Weekly Installs
1.0K
Repository
onmax/nuxt-skills
GitHub Stars
649
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
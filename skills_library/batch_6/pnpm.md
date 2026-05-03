---
title: pnpm
url: https://skills.sh/antfu/skills/pnpm
---

# pnpm

skills/antfu/skills/pnpm
pnpm
Originally fromsanity-io/next-sanity
Installation
$ npx skills add https://github.com/antfu/skills --skill pnpm
Summary

Fast, disk-efficient Node.js package manager with strict dependency resolution and monorepo support.

Enforces strict dependency resolution by default, preventing phantom dependencies; uses content-addressable storage to deduplicate packages across projects
Supports monorepo workspaces with filtering, shared lockfiles, and workspace protocol; configuration via pnpm-workspace.yaml
Includes advanced dependency management: catalogs for centralized version control, overrides to force specific versions, and patches to modify third-party packages
Provides peer dependency auto-install, custom resolution hooks via .pnpmfile.cjs, and package aliases using the npm: protocol
Use --frozen-lockfile in CI environments; check pnpm-workspace.yaml and .npmrc files to understand project configuration
SKILL.md

pnpm is a fast, disk space efficient package manager. It uses a content-addressable store to deduplicate packages across all projects on a machine, saving significant disk space. pnpm enforces strict dependency resolution by default, preventing phantom dependencies. Configuration should preferably be placed in pnpm-workspace.yaml for pnpm-specific settings.

Important: When working with pnpm projects, agents should check for pnpm-workspace.yaml and .npmrc files to understand workspace structure and configuration. Always use --frozen-lockfile in CI environments.

The skill is based on pnpm 10.x, generated at 2026-01-28.

Core
Topic	Description	Reference
CLI Commands	Install, add, remove, update, run, exec, dlx, and workspace commands	core-cli
Configuration	pnpm-workspace.yaml, .npmrc settings, and package.json fields	core-config
Workspaces	Monorepo support with filtering, workspace protocol, and shared lockfile	core-workspaces
Store	Content-addressable storage, hard links, and disk efficiency	core-store
Features
Topic	Description	Reference
Catalogs	Centralized dependency version management for workspaces	features-catalogs
Overrides	Force specific versions of dependencies including transitive	features-overrides
Patches	Modify third-party packages with custom fixes	features-patches
Aliases	Install packages under custom names using npm: protocol	features-aliases
Hooks	Customize resolution with .pnpmfile.cjs hooks	features-hooks
Peer Dependencies	Auto-install, strict mode, and dependency rules	features-peer-deps
Best Practices
Topic	Description	Reference
CI/CD Setup	GitHub Actions, GitLab CI, Docker, and caching strategies	best-practices-ci
Migration	Migrating from npm/Yarn, handling phantom deps, monorepo migration	best-practices-migration
Performance	Install optimizations, store caching, workspace parallelization	best-practices-performance
Weekly Installs
10.8K
Repository
antfu/skills
GitHub Stars
4.8K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
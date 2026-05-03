---
title: arch-tsdown-monorepo
url: https://skills.sh/hairyf/skills/arch-tsdown-monorepo
---

# arch-tsdown-monorepo

skills/hairyf/skills/arch-tsdown-monorepo
arch-tsdown-monorepo
Installation
$ npx skills add https://github.com/hairyf/skills --skill arch-tsdown-monorepo
SKILL.md

arch-tsdown-monorepo is a pnpm monorepo starter for TypeScript libraries (based on hairyf/starter-monorepo). Each package uses tsdown for building. It provides shared tooling (ESLint, Vitest, TypeScript), pnpm catalogs for versions, workspace dependencies, and optional npm Trusted Publisher for CI-based releases.

The skill is based on hairyf/starter-monorepo, generated at 2026-02-02.

Recommended practices:

Use pnpm catalogs for devDependency versions; reference with catalog:cli, catalog:testing, etc.
Use workspace:* for inter-package dependencies; publish once manually, then use npm Trusted Publisher for CI releases.
Run build/typecheck/test from root with pnpm -r run ... and a single Vitest config with projects (root + packages/*).
Core References
Topic	Description	Reference
Overview	Monorepo purpose, structure, when to use	core-overview
Workspace	pnpm workspace, catalogs, workspace:* deps	core-workspace
Packages	Package layout, exports, inter-package deps	core-packages
Package Exports	Dual exports (dev vs publish), main/module/types, files, sideEffects	core-package-exports
tsdown (per package)	entry, dts, exports, publint	core-tsdown-per-package
Scripts	Root and package scripts — build, dev, typecheck, test, release	core-scripts
Testing	Vitest projects — root + packages/*	core-testing
Tooling	ESLint, TypeScript, .gitignore, .vscode	core-tooling
CI	GitHub Actions — lint, typecheck, test matrix	core-ci
Release	npm Trusted Publisher, bumpp, release workflow	core-release
Git Hooks	simple-git-hooks, lint-staged, pre-commit	core-git-hooks
Features
Topic	Description	Reference
Exports Snapshot	Per-package export snapshot tests (vitest-package-exports, runIf(IS_READY))	features-exports-snapshot
Add Package	Step-by-step adding a new workspace package	features-add-package
Best Practices
Topic	Description	Reference
Monorepo	Catalogs, workspace deps, release, build order	best-practices-monorepo
Weekly Installs
337
Repository
hairyf/skills
GitHub Stars
15
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
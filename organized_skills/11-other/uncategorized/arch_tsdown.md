---
rating: ⭐⭐
title: arch-tsdown
url: https://skills.sh/hairyf/skills/arch-tsdown
---

# arch-tsdown

skills/hairyf/skills/arch-tsdown
arch-tsdown
Installation
$ npx skills add https://github.com/hairyf/skills --skill arch-tsdown
SKILL.md

arch-tsdown is a TypeScript library starter (based on antfu/starter-ts) that uses tsdown for building. It provides a minimal, opinionated setup: ESM-only output, automatic .d.ts generation, pnpm, Vitest, ESLint, and optional npm Trusted Publisher for CI-based releases.

The skill is based on starter-ts (arch-tsdown source), generated at 2026-01-30.

Recommended practices:

Build pure ESM; enable dts and exports in tsdown config
Use npm Trusted Publisher for releases
Run publint (via tsdown’s publint: true) before publishing
Core References
Topic	Description	Reference
Overview	Project purpose, structure, when to use	core-overview
tsdown Config	entry, dts, exports, publint	core-tsdown-config
Scripts & Release	build, dev, start, release, npm Trusted Publisher	core-scripts
Package Exports	dist output, types, exports, sideEffects	core-package-exports
pnpm Workspace	catalogs, version management, workspace	core-pnpm-workspace
Tooling	ESLint, TypeScript, Vitest config	core-tooling
Git Hooks	simple-git-hooks, lint-staged, pre-commit	core-git-hooks
CI	GitHub Actions — lint, typecheck, test matrix	core-ci
Release	Tag push, sxzz/workflows, npm Trusted Publisher	core-release
Testing	Vitest, vitest-package-exports, export snapshots	core-testing
Best Practices
Topic	Description	Reference
tsdown & Package	ESM, dts, exports, tooling alignment	best-practices-tsdown
Weekly Installs
74
Repository
hairyf/skills
GitHub Stars
15
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
---
title: arch-tsdown-cli
url: https://skills.sh/hairyf/skills/arch-tsdown-cli
---

# arch-tsdown-cli

skills/hairyf/skills/arch-tsdown-cli
arch-tsdown-cli
Installation
$ npx skills add https://github.com/hairyf/skills --skill arch-tsdown-cli
SKILL.md

arch-tsdown-cli is a TypeScript CLI package starter (based on hairyf/starter-cli) that uses tsdown for building. It provides a minimal, opinionated setup: dual surface (library + bin), ESM-only output, automatic .d.ts generation, dev bin via tsx, pnpm, Vitest, ESLint, and optional npm Trusted Publisher for CI-based releases.

The skill is based on starter-cli (arch-tsdown-cli source), generated at 2026-01-30.

Recommended practices:

Use dev bin (tsx) locally and prod bin (dist) in publishConfig
Build pure ESM; enable dts and keep external for dependencies
Use npm Trusted Publisher for releases
Core References
Topic	Description	Reference
Overview	Project purpose, structure, when to use	core-overview
Bin Entry	dev vs prod bin, shebang, tsx	core-bin-entry
tsdown Config	entry, format, dts, external	core-tsdown-config
Scripts & Release	build, dev, start, release, npm Trusted Publisher	core-scripts
Package Exports	dist, bin, publishConfig, files	core-package-exports
Tooling	ESLint, TypeScript, Vitest config	core-tooling
Git Hooks	simple-git-hooks, lint-staged, pre-commit	core-git-hooks
CI	GitHub Actions — lint, typecheck, test matrix	core-ci
Testing	Vitest, vitest-package-exports	core-testing
Best Practices
Topic	Description	Reference
CLI & Package	bin, ESM, dts, external, release	best-practices-cli
Weekly Installs
113
Repository
hairyf/skills
GitHub Stars
15
First Seen
Jan 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
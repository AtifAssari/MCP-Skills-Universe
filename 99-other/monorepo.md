---
title: monorepo
url: https://skills.sh/epicenterhq/epicenter/monorepo
---

# monorepo

skills/epicenterhq/epicenter/monorepo
monorepo
Installation
$ npx skills add https://github.com/epicenterhq/epicenter --skill monorepo
SKILL.md
Script Commands
Reference Repositories
jsrepo — Package distribution for monorepos
WXT — Browser extension framework (used by tab-manager app)

The monorepo uses consistent script naming conventions:

When to Apply This Skill

Use this pattern when you need to:

Run formatting, linting, or type-check scripts in this monorepo.
Choose between auto-fix commands and :check CI-only variants.
Verify final changes with the repo-standard bun typecheck workflow.
Scaffold a new package in packages/.
Command	Purpose	When to use
bun format	Fix formatting (biome)	Development
bun format:check	Check formatting	CI
bun lint	Fix lint issues (biome)	Development
bun lint:check	Check lint issues	CI
bun typecheck	Type checking (tsc, svelte-check, astro check)	Both
Convention
No suffix = fix (modifies files)
:check suffix = check only (for CI, no modifications)
typecheck alone = type checking (separate concern, cannot auto-fix)
Dev Scripts

Every app uses explicit dev:local / dev:remote naming:

Script	Meaning
dev:local	Local everything—local API, local secrets
dev:remote	Local app, remote/prod resources
dev	Alias for dev:local (convenience)

Not every app has dev:remote—only add it when there's a real use case.

CLI (epicenter)

From the monorepo root, bun epicenter runs the local CLI against localhost:8787:

bun epicenter start playground/opensidian-e2e --verbose
bun epicenter list files -C playground/opensidian-e2e


The bare epicenter command (global install) defaults to api.epicenter.so. Config files read process.env.EPICENTER_SERVER with a prod fallback—the root script sets it automatically.

After Completing Code Changes

Run type checking to verify:

bun typecheck


This runs turbo run typecheck which executes the typecheck script in each package (e.g., tsc --noEmit, svelte-check).

New Package Boilerplate

When creating a new package in packages/, follow this exact structure.

package.json
{
  "name": "@epicenter/<package-name>",
  "version": "0.0.1",
  "main": "./src/index.ts",
  "types": "./src/index.ts",
  "exports": {
    ".": "./src/index.ts"
  },
  "license": "MIT",
  "scripts": {
    "typecheck": "tsc --noEmit"
  },
  "dependencies": {},
  "devDependencies": {
    "@types/bun": "catalog:",
    "typescript": "catalog:"
  }
}


Key conventions:

main and types both point to ./src/index.ts (no build step—consumers import source directly).
Use "workspace:*" for internal deps (e.g., "@epicenter/workspace": "workspace:*").
Use "catalog:" for shared versions managed in the root package.json catalogs.
peerDependencies for packages consumers must also install (e.g., yjs).
tsconfig.json
{
  "extends": "../../tsconfig.base.json",
  "compilerOptions": {
    "module": "preserve",
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noPropertyAccessFromIndexSignature": false
  }
}


After creating the package, run bun install from the repo root to register it in the workspace.

Weekly Installs
72
Repository
epicenterhq/epicenter
GitHub Stars
4.5K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
---
title: link-workspace-packages
url: https://skills.sh/nrwl/nx-ai-agents-config/link-workspace-packages
---

# link-workspace-packages

skills/nrwl/nx-ai-agents-config/link-workspace-packages
link-workspace-packages
Installation
$ npx skills add https://github.com/nrwl/nx-ai-agents-config --skill link-workspace-packages
Summary

Link workspace packages in monorepos across npm, yarn, pnpm, and bun.

Detects package manager via packageManager field or lockfile presence, then uses the appropriate workspace linking command for each manager
pnpm and yarn use workspace: protocol; npm auto-symlinks workspace packages; bun supports workspace: protocol
Resolves "cannot find module" and import resolution errors by adding dependencies between sibling packages with proper symlink creation
Each manager has different hoisting and isolation behavior: npm/bun hoist to root, pnpm enforces strict isolation, yarn berry uses Plug'n'Play
SKILL.md
Link Workspace Packages

Add dependencies between packages in a monorepo. All package managers support workspaces but with different syntax.

Detect Package Manager

Check whether there's a packageManager field in the root-level package.json.

Alternatively check lockfile in repo root:

pnpm-lock.yaml → pnpm
yarn.lock → yarn
bun.lock / bun.lockb → bun
package-lock.json → npm
Workflow
Identify consumer package (the one importing)
Identify provider package(s) (being imported)
Add dependency using package manager's workspace syntax
Verify symlinks created in consumer's node_modules/
pnpm

Uses workspace: protocol - symlinks only created when explicitly declared.

# From consumer directory
pnpm add @org/ui --workspace

# Or with --filter from anywhere
pnpm add @org/ui --filter @org/app --workspace


Result in package.json:

{ "dependencies": { "@org/ui": "workspace:*" } }

yarn (v2+/berry)

Also uses workspace: protocol.

yarn workspace @org/app add @org/ui


Result in package.json:

{ "dependencies": { "@org/ui": "workspace:^" } }

npm

No workspace: protocol. npm auto-symlinks workspace packages.

npm install @org/ui --workspace @org/app


Result in package.json:

{ "dependencies": { "@org/ui": "*" } }


npm resolves to local workspace automatically during install.

bun

Supports workspace: protocol (pnpm-compatible).

cd packages/app && bun add @org/ui


Result in package.json:

{ "dependencies": { "@org/ui": "workspace:*" } }

Examples

Example 1: pnpm - link ui lib to app

pnpm add @org/ui --filter @org/app --workspace


Example 2: npm - link multiple packages

npm install @org/data-access @org/ui --workspace @org/dashboard


Example 3: Debug "Cannot find module"

Check if dependency is declared in consumer's package.json
If not, add it using appropriate command above
Run install (pnpm install, npm install, etc.)
Notes
Symlinks appear in <consumer>/node_modules/@org/<package>
Hoisting differs by manager:
npm/bun: hoist shared deps to root node_modules
pnpm: no hoisting (strict isolation, prevents phantom deps)
yarn berry: uses Plug'n'Play by default (no node_modules)
Root package.json should have "private": true to prevent accidental publish
Weekly Installs
1.4K
Repository
nrwl/nx-ai-agents-config
GitHub Stars
19
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
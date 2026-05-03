---
rating: ⭐⭐
title: antfu
url: https://skills.sh/antfu/skills/antfu
---

# antfu

skills/antfu/skills/antfu
antfu
Installation
$ npx skills add https://github.com/antfu/skills --skill antfu
Summary

Opinionated TypeScript/JavaScript conventions and tooling setup for modern projects.

Covers code organization (single responsibility, type separation, constants extraction), runtime practices (isomorphic code with environment markers), and explicit TypeScript typing
Includes ESLint configuration via @antfu/eslint-config, Vitest testing patterns, and Git hooks with lint-staged for automated code formatting
Provides @antfu/ni command shortcuts for dependency management across package managers, and pnpm catalog-based version management for monorepos
References detailed guides for ESLint setup, project initialization, Vue/Nuxt app development, library publishing, and monorepo patterns
SKILL.md
Coding Practices
Code Organization
Single responsibility: Each source file should have a clear, focused scope/purpose
Split large files: Break files when they become large or handle too many concerns
Type separation: Always separate types and interfaces into types.ts or types/*.ts
Constants extraction: Move constants to a dedicated constants.ts file
Runtime Environment
Prefer isomorphic code: Write runtime-agnostic code that works in Node, browser, and workers whenever possible
Clear runtime indicators: When code is environment-specific, add a comment at the top of the file:
// @env node
// @env browser

TypeScript
Explicit return types: Declare return types explicitly when possible
Avoid complex inline types: Extract complex types into dedicated type or interface declarations
Comments
Avoid unnecessary comments: Code should be self-explanatory
Explain "why" not "how": Comments should describe the reasoning or intent, not what the code does
Testing (Vitest)
Test files: foo.ts → foo.test.ts (same directory)
Use describe/it API (not test)
Use toMatchSnapshot for complex outputs
Use toMatchFileSnapshot with explicit path for language-specific snapshots
Tooling Choices
@antfu/ni Commands
Command	Description
ni	Install dependencies
ni <pkg> / ni -D <pkg>	Add dependency / dev dependency
nr <script>	Run script
nu	Upgrade dependencies
nun <pkg>	Uninstall dependency
nci	Clean install (pnpm i --frozen-lockfile)
nlx <pkg>	Execute package (npx)
TypeScript Config
{
  "compilerOptions": {
    "target": "ESNext",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true
  }
}

ESLint Setup
// eslint.config.mjs
import antfu from '@antfu/eslint-config'

export default antfu()


When completing tasks, run pnpm run lint --fix to format the code and fix coding style.

For detailed configuration options: antfu-eslint-config

Git Hooks
{
  "simple-git-hooks": {
    "pre-commit": "pnpm i --frozen-lockfile --ignore-scripts --offline && npx lint-staged"
  },
  "lint-staged": { "*": "eslint --fix" },
  "scripts": {
    "prepare": "npx simple-git-hooks"
  }
}

pnpm Catalogs

Use named catalogs in pnpm-workspace.yaml for version management:

Catalog	Purpose
prod	Production dependencies
inlined	Bundler-inlined dependencies
dev	Dev tools (linter, bundler, testing)
frontend	Frontend libraries

Avoid the default catalog. Catalog names can be adjusted per project needs.

References
Topic	Description	Reference
ESLint Config	Framework support, formatters, rule overrides, VS Code settings	antfu-eslint-config
Project Setup	.gitignore, GitHub Actions, VS Code extensions	setting-up
App Development	Vue/Nuxt/UnoCSS conventions and patterns	app-development
Library Development	tsdown bundling, pure ESM publishing	library-development
Monorepo	pnpm workspaces, centralized alias, Turborepo	monorepo
Weekly Installs
9.2K
Repository
antfu/skills
GitHub Stars
4.8K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
---
title: oq
url: https://skills.sh/0froq/skills/oq
---

# oq

skills/0froq/skills/oq
oq
Installation
$ npx skills add https://github.com/0froq/skills --skill oq
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
// eslint.config.ts
import antfu from '@antfu/eslint-config'
import nuxt from './.nuxt/eslint.config.mjs'

export default antfu(
  {
    unocss: true,
    pnpm: true,
    typescript: true,
    vue: true,
    rules: {
      'vue/max-attributes-per-line': ['error', {
        singleline: { max: 1 },
        multiline: { max: 1 },
      }],
      'unused-imports/no-unused-imports': 'off',
    },
    formatters: {
      css: true,
      html: true,
      markdown: 'dprint',
    },
  },
)
  .append(nuxt())


For detailed configuration options: oq-eslint-config

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

Additional tools:

Use pnpm-workspace-utils for catalog management
Use nip for interactive package management
References
Topic	Description	Reference
ESLint Config	Custom @antfu/eslint-config setup with Vue rules and formatters	oq-eslint-config
UnoCSS Config	Custom UnoCSS setup with fonts, icons, and prefixed attributify	oq-unocss-config
Project Setup	.gitignore, GitHub Actions, VS Code extensions	setting-up
Release Workflow	Automated releases with changelogithub	release-workflow
pnpm Catalog	Strict pnpm catalog configuration and tools	pnpm-catalog
App Development	Vue/Nuxt/UnoCSS conventions and patterns	app-development
Monorepo	pnpm workspaces, centralized alias, Turborepo	monorepo
Library Development	tsdown bundling, pure ESM publishing	library-development
Weekly Installs
12
Repository
0froq/skills
First Seen
Mar 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
---
rating: ⭐⭐
title: linting-neostandard-eslint9
url: https://skills.sh/mcollina/skills/linting-neostandard-eslint9
---

# linting-neostandard-eslint9

skills/mcollina/skills/linting-neostandard-eslint9
linting-neostandard-eslint9
Installation
$ npx skills add https://github.com/mcollina/skills --skill linting-neostandard-eslint9
SKILL.md
When to use

Use this skill when you need to:

Set up linting in a JavaScript or TypeScript project
Use neostandard as a Standard-like ESLint v9 flat-config baseline
Configure eslint@9 with the flat config system (eslint.config.js/eslint.config.mjs)
Migrate from standard to neostandard or ESLint v9
Migrate from legacy .eslintrc* configuration to ESLint v9
Run linting consistently in CI and local development
Quick start: basic neostandard setup

Install dependencies and create a minimal eslint.config.js:

npm install --save-dev eslint@9 neostandard

// eslint.config.js
import neostandard from 'neostandard'

export default neostandard()


Verify the config works:

npx eslint .

Common setup workflow (new project)
Install eslint@9 and neostandard (see Quick start above)
Create eslint.config.js with neostandard() as the base
Add any project-specific rule overrides on top
Run npx eslint . to confirm no config errors
Add a lint script to package.json: "lint": "eslint ."
Integrate into CI with a non-fix run; use --fix only in local workflows
How to use

Read individual rule files for implementation details and examples:

rules/neostandard.md - Install, configure, and extend neostandard with ESLint
rules/eslint-v9-flat-config.md - Build ESLint v9 flat config for JS/TS projects
rules/migration-from-standard.md - Migrate from standard to neostandard or ESLint v9
rules/migration-from-legacy-eslint.md - Migrate from .eslintrc* to flat config safely
rules/ci-and-editor-integration.md - CI scripts, pre-commit, and editor setup
Core principles
Prefer reproducible linting with pinned major versions
Keep config minimal and explicit
Use flat config for ESLint v9 projects
Treat lint failures as quality gates in CI
Enable auto-fix for local workflows, but validate with non-fix CI runs
Weekly Installs
434
Repository
mcollina/skills
GitHub Stars
1.8K
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
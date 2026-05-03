---
title: nuxt-init
url: https://skills.sh/ralphcrisostomo/nuxt-development-skills/nuxt-init
---

# nuxt-init

skills/ralphcrisostomo/nuxt-development-skills/nuxt-init
nuxt-init
Installation
$ npx skills add https://github.com/ralphcrisostomo/nuxt-development-skills --skill nuxt-init
SKILL.md
Nuxt Init

Scaffold a Nuxt 4 project with standard configs, dev deps, hooks, and scripts.

When to Use
Starting a new Nuxt 4 project
Auditing an existing project for missing configs
Onboarding a repo to standard tooling
Workflow
Create config files from references/configs.md (skip existing unless user says overwrite)
Install dev dependencies
Add scripts and lint-staged to package.json
Run bun install && bun run prepare
Run bunx terraform-scaffold init
Config Files

See references/configs.md for full file contents:

prettier.config.js + .prettierignore
.gitignore
eslint.config.ts
vitest.config.ts
tsconfig.json
.husky/pre-commit + .husky/pre-push
.sops.yaml
package.json Additions
Scripts
{
    "dev": "nuxt dev",
    "build": "nuxt build",
    "generate": "nuxt generate",
    "preview": "nuxt preview",
    "lint": "eslint . && vue-tsc --noEmit",
    "lint:fix": "eslint . --fix",
    "pretty": "prettier --write .",
    "test": "vitest run",
    "test:watch": "vitest",
    "prepare": "husky",
    "postinstall": "nuxt prepare"
}

lint-staged
{
    "lint-staged": {
        "*.{js,ts,vue}": "eslint --fix",
        "*.{js,ts,vue,json,md,css,scss,yml,yaml}": "prettier --write"
    }
}

Dev Dependencies
bun add -d eslint @nuxt/eslint eslint-config-prettier prettier @prettier/plugin-pug prettier-plugin-terraform-formatter vue-eslint-parser-template-tokenizer-pug husky lint-staged vue-tsc @types/node tsx tailwindcss terraform-scaffold

Terraform Scaffold

terraform-scaffold automates AWS infrastructure setup.

After install: bunx terraform-scaffold init

Command	Description
bunx terraform-scaffold init	Create config + Terraform directory structure
bunx terraform-scaffold graphql	Generate GraphQL resolver
bunx terraform-scaffold lambda	Create standalone Lambda
bunx terraform-scaffold build --env=<env>	Bundle Lambda functions
bunx terraform-scaffold tf <env> <action>	Execute Terraform (plan, apply)
bunx terraform-scaffold tf-output <env>	Export outputs to env files
Post-Setup
bun install
bun run prepare              # husky + nuxt types
bunx terraform-scaffold init # Terraform structure

Weekly Installs
33
Repository
ralphcrisostomo…t-skills
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
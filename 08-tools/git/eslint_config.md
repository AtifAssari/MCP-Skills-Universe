---
rating: ⭐⭐
title: eslint-config
url: https://skills.sh/jsonlee12138/prompts/eslint-config
---

# eslint-config

skills/jsonlee12138/prompts/eslint-config
eslint-config
Installation
$ npx skills add https://github.com/jsonlee12138/prompts --skill eslint-config
SKILL.md
ESLint Config
Overview

Set up ESLint using @antfu/eslint-config for either a single project or a workspace package, and optionally enforce commit quality with commitlint + husky + lint-staged.

Decision
Single project: Choose when you have one app/package.
Workspace package: Choose when multiple apps need a shared ESLint config in a monorepo.
Quick Workflow
Choose single vs workspace.
Install dependencies.
Create eslint.config.js (flat config).
Add lint scripts.
Run pnpm lint to verify.
Add commit quality hooks (.commitlintrc.cjs, .husky/*, .lintstagedrc) if the team wants linting and commit message checks before push.
Common Mistakes
Mixing Prettier with ESLint formatting rules (prefer ESLint-only).
Using legacy .eslintrc instead of eslint.config.js.
Forgetting to build/publish the shared workspace config.
Creating .lintstagedrc with unsupported syntax for your chosen format.
Missing commit-msg hook, so commit message rules never run.
Forgetting package.json config.commitizen.path, so cz-git is not picked up.
Resources
references/single-project.md
references/workspace.md
references/vscode-settings.md
references/commit-quality.md
Weekly Installs
10
Repository
jsonlee12138/prompts
GitHub Stars
1
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
---
title: nx
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/nx
---

# nx

skills/oguzhan18/angular-ecosystem-skills/nx
nx
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill nx
SKILL.md
Nx (Smart, Fast, Extensible Build System)

Version: 22.x (2025) Tags: Monorepo, Build System, Angular, React, Node

References: Docs — guides, tutorials • GitHub • Enterprise Patterns Book

API Changes

This section documents recent version-specific API changes.

NEW: TypeScript Project References — Faster builds and type checks using modern TypeScript setup source

NEW: pnpm catalog support — Manage single version policy with pnpm catalogs source

NEW: Angular Rspack support — Fast bundler for Angular projects source

NEW: AI Agent integration — Code mode for better LLM context management source

NEW: Polyglot workspaces — Native support for Gradle, Maven, .NET alongside JS/TS projects

Best Practices
Use domain-based folder structure — Group projects by business domain
libs/
├── auth/
│   ├── feature-login/
│   └── data-access/
├── products/
│   ├── feature-list/
│   └── ui/
└── shared/
    ├── ui/
    └── utils/

Use Nx generators — Scaffold consistent code across workspace
# Create new library
nx g @nx/angular:library --name=shared-data-access --directory=libs/shared/data-access

# Create new feature
nx g @nx/angular:component --name=user-profile --project=my-app

Use affected commands — Only run tasks on changed projects
nx affected:build     # Build only changed projects
nx affected:test      # Test only changed projects
nx affected:lint     # Lint only changed projects


Use shared libraries — Avoid code duplication with common utilities

Configure task dependencies — Define how tasks depend on each other in project.json

{
  "build": {
    "dependsOn": ["^build"]
  }
}


Use Nx Cloud — Enable distributed caching for faster CI

Use nx.json and tsconfig.base.json — Enforce consistent settings across projects

Use @nx/angular:component generator — Follow workspace conventions for components

Weekly Installs
123
Repository
oguzhan18/angul…m-skills
GitHub Stars
6
First Seen
6 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
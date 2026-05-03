---
rating: ⭐⭐⭐
title: nebula-project-structure
url: https://skills.sh/acquia/nebula/nebula-project-structure
---

# nebula-project-structure

skills/acquia/nebula/nebula-project-structure
nebula-project-structure
Installation
$ npx skills add https://github.com/acquia/nebula --skill nebula-project-structure
SKILL.md
Project structure

This project uses a two-folder structure to separate example code from working code:

src/
├── components/     # Working components (Storybook reads from here)
│   └── global.css  # Base styles imported by Storybook
├── stories/        # Working stories (Storybook reads from here)

examples/
├── components/     # Example component implementations (for reference)
└── stories/        # Example stories (for reference)

Package manager

Detect the package manager by checking for lock files in the project root:

package-lock.json → npm (npm run, npx)
yarn.lock → yarn (yarn, yarn dlx)
pnpm-lock.yaml → pnpm (pnpm, pnpm dlx)
bun.lockb → bun (bun run, bunx)

Use the detected package manager for all commands in these instructions.

Weekly Installs
8
Repository
acquia/nebula
GitHub Stars
7
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
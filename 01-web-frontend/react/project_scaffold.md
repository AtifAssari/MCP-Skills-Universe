---
title: project-scaffold
url: https://skills.sh/shipshitdev/library/project-scaffold
---

# project-scaffold

skills/shipshitdev/library/project-scaffold
project-scaffold
Installation
$ npx skills add https://github.com/shipshitdev/library --skill project-scaffold
SKILL.md
Project Scaffold

Unified project scaffolder for creating new projects or adding components to existing ones.

Purpose

This skill provides a unified way to scaffold:

.agents/ folder structure for AI-first development
Backend (NestJS) with MongoDB, Swagger, and best practices
Frontend (NextJS) with Tailwind and @agenticindiedev/ui
Mobile (Expo) with React Native and Expo Router
Browser Extension (Plasmo) with React and Tailwind
When to Use

Use this skill when:

Starting a new project from scratch
Adding components to an existing project
Setting up a monorepo or separate repositories
Need a unified scaffolding experience across Claude, Codex, and Cursor
Usage
Interactive Mode (Recommended)
python3 scripts/scaffold.py


The script will ask you:

Project name
Project root path
Repository structure (monorepo vs separate)
Components to scaffold (all optional):
.agent folder
Backend (NestJS)
Frontend (NextJS)
Mobile (Expo)
Extension (Plasmo)
Organization name (for monorepo packages)
From Claude

When user requests scaffolding, activate this skill and run:

python3 scripts/scaffold.py


The script handles all interactive prompts.

Features
Flexible Structure
Monorepo: All components in one repository with workspace configuration
Separate repos: Each component in its own directory/repository
Existing projects: Can add components to existing projects
Component Options

All components are optional - scaffold only what you need:

.agents/ folder with full AI documentation structure
Backend with NestJS, MongoDB, Swagger
Frontend with NextJS 15, Tailwind, @agenticindiedev/ui
Mobile with Expo Router, React Native
Extension with Plasmo, React, Tailwind
Cross-Platform

Works from:

Claude Code
Codex
Cursor
Generated Structure
Monorepo Example
myproject/
├── .agents/                  # AI documentation
├── package.json             # Workspace root
├── api/                     # NestJS backend
│   ├── .agents/
│   ├── apps/api/src/
│   └── package.json
├── frontend/                # NextJS apps
│   ├── .agents/
│   ├── apps/dashboard/
│   └── package.json
├── mobile/                  # Expo app
│   ├── .agents/
│   ├── app/
│   └── package.json
└── extension/               # Plasmo extension
    ├── .agents/
    ├── src/
    └── package.json

Separate Repos Example
myproject-api/               # Backend only
├── .agents/
├── apps/api/src/
└── package.json

myproject-frontend/          # Frontend only
├── .agents/
├── apps/dashboard/
└── package.json

Key Patterns Included
Backend (NestJS)
Soft deletes: isDeleted: boolean
Multi-tenancy: Always filter by organization
Collection pattern: controllers → services → schemas
Swagger documentation
Dockerfile included
Frontend (NextJS)
Path aliases: @components/, @services/, @hooks/
Tailwind CSS with @agenticindiedev/ui
TypeScript strict mode
App Router structure
Mobile (Expo)
Expo Router for navigation
TypeScript configuration
Platform-specific configurations
Extension (Plasmo)
React + TypeScript
Tailwind CSS with @agenticindiedev/ui
Manifest configuration
Popup component
Next Steps After Scaffolding

Install dependencies:

cd [project-root]
bun install


Start development:

# Monorepo
bun run dev:api
bun run dev:frontend

# Separate repos
cd api && bun run start:dev
cd frontend && bun run dev


Customize:

Update .agents/SYSTEM/RULES.md with your coding standards
Configure environment variables
Add your first features
Integration with Existing Skills

This skill integrates with:

agent-folder-init: Uses its script for .agent folder scaffolding
fullstack-workspace-init: Reuses component templates and patterns
Troubleshooting

Script not found: Ensure the skill is installed in ``

Permission denied: Make script executable: chmod +x scripts/scaffold.py

Python not found: Ensure Python 3 is installed and in PATH

Agent folder not created: The script tries to use agent-folder-init skill. If not found, it will skip .agent folder creation.

Weekly Installs
112
Repository
shipshitdev/library
GitHub Stars
21
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
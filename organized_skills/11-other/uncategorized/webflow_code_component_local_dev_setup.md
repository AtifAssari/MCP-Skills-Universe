---
rating: ⭐⭐⭐
title: webflow-code-component:local-dev-setup
url: https://skills.sh/webflow/webflow-skills/webflow-code-component:local-dev-setup
---

# webflow-code-component:local-dev-setup

skills/webflow/webflow-skills/webflow-code-component:local-dev-setup
webflow-code-component:local-dev-setup
Installation
$ npx skills add https://github.com/webflow/webflow-skills --skill webflow-code-component:local-dev-setup
SKILL.md
Local Dev Setup

Set up a new Webflow Code Components project from scratch.

When to Use This Skill

Use when:

Starting a brand new code components project
User asks to set up, initialize, or create a new project
Adding code components to an existing React project
Setting up the development environment for the first time

Do NOT use when:

Project already exists and is configured (just answer questions directly)
Creating individual components (use component-scaffold instead)
Deploying components (use deploy-guide instead)
Instructions
Phase 1: Assess Current State

Check if project exists:

Is there an existing package.json?
Is there an existing webflow.json?
What's the current project structure?

Determine setup type:

New project from scratch
Add to existing React project
Add to existing Next.js/Vite project
Phase 2: Project Initialization

Create project structure (if new):

Initialize npm project
Set up TypeScript
Create folder structure

Install dependencies:

Core: React, TypeScript
Webflow: CLI, data-types, react utils
Optional: Styling libraries
Phase 3: Configuration

Create webflow.json:

Set library name
Configure component glob pattern
Set up globals if needed

Configure TypeScript:

Set up tsconfig.json
Enable JSX support
Phase 4: Create Starter Files

Create example component:

Simple Button component
Definition file
Basic styling

Create globals file (optional):

For shared styles
For decorators
Phase 5: Verify Setup

Verify bundle compiles:

Run npx webflow library bundle --public-path http://localhost:4000/ to catch build errors locally
This verifies your components, imports, and configuration are correct
Full testing in the Webflow Designer requires deploying with npx webflow library share

Provide next steps:

How to create more components
How to deploy
Development workflow
Examples

For detailed step-by-step examples, see references/EXAMPLES.md.

Available examples:

New Project from Scratch - Complete setup with React, TypeScript, and CSS Modules
Add to Existing React Project - Integrate code components into an existing codebase
With Tailwind CSS - Setup with Tailwind CSS support

Quick Start (New Project):

# 1. Create project
mkdir my-webflow-components && cd my-webflow-components
npm init -y

# 2. Install dependencies
npm install react react-dom
npm install -D typescript @types/react @types/react-dom
npm install -D @webflow/webflow-cli @webflow/data-types @webflow/react

# 3. Create webflow.json
echo '{"library":{"name":"My Library","components":["./src/**/*.webflow.tsx"]}}' > webflow.json

# 4. Create component directory
mkdir -p src/components/Button


Then create your component files (.tsx, .webflow.tsx, .module.css). See Example 1 in references/EXAMPLES.md for complete file contents including component, definition, and CSS files.

Deploy with:

npx webflow library share

Validation

After setup, verify the project is correctly configured:

Check	How to Verify
webflow.json exists in project root	cat webflow.json
Dependencies installed	npm list @webflow/webflow-cli
Bundle compiles without errors	npx webflow library bundle --public-path http://localhost:4000/
At least one component found	Check bundle output for "Found N component(s)"
Guidelines
Minimum Requirements

Every code components project needs:

package.json with dependencies
webflow.json with library config
tsconfig.json (for TypeScript)
At least one .webflow.tsx file
Recommended Structure
project/
├── src/
│   ├── components/
│   │   └── [ComponentName]/
│   │       ├── [ComponentName].tsx
│   │       ├── [ComponentName].webflow.tsx
│   │       └── [ComponentName].module.css
│   ├── hooks/           # Custom hooks
│   ├── utils/           # Utilities
│   ├── declarations.d.ts # CSS module types
│   ├── globals.ts       # Decorators/global imports
│   └── globals.css      # Global styles
├── package.json
├── tsconfig.json
├── webflow.json
└── .gitignore

Development Workflow
Create component: Use component-scaffold skill
Develop locally: Run React project to iterate (e.g., npm run dev)
Validate: Use pre-deploy-check skill
Deploy: Use deploy-guide skill or run npx webflow library share
Test in Webflow: Add component to page in Designer
Weekly Installs
225
Repository
webflow/webflow-skills
GitHub Stars
64
First Seen
Mar 11, 2026
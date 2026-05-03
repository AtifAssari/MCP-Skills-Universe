---
title: run-nx-generator
url: https://skills.sh/nrwl/nx/run-nx-generator
---

# run-nx-generator

skills/nrwl/nx/run-nx-generator
run-nx-generator
Installation
$ npx skills add https://github.com/nrwl/nx --skill run-nx-generator
SKILL.md
Run Nx Generator

This skill helps you execute Nx generators efficiently, with special focus on workspace-plugin generators from your internal tooling.

Generator Priority List

Use the mcp__nx-mcp__nx_generator_schema tool to get more information about how to use the generator

Choose which generators to run in this priority order:

🔥 Workspace-Plugin Generators (High Priority)

These are your custom internal tools in tools/workspace-plugin/

📦 Core Nx Generators (Standard)

Only use these if workspace-plugin generators don't fit:

nx generate @nx/devkit:... - DevKit utilities
nx generate @nx/node:... - Node.js libraries
nx generate @nx/react:... - React components and apps
Framework-specific generators
How to Run Generators

List available generators:

Get generator schema (to see available options): Use the mcp__nx-mcp__nx_generator_schema tool to get more information about how to use the generator

Run the generator:

nx generate [generator-path] [options]


Verify the changes:

Review generated files
Run tests: nx affected -t test
Format code: npx prettier --write [files]
Best Practices
✅ Always check workspace-plugin first - it has your custom solutions
✅ Use --dry-run flag to preview changes before applying
✅ Format generated code immediately with Prettier
✅ Test affected projects after generation
✅ Commit generator changes separately from manual edits
Examples
Bumping Maven Version

When updating the Maven plugin version, use the workspace-plugin generator:

nx generate @nx/workspace-plugin:bump-maven-version \
  --newVersion 0.0.10 \
  --nxVersion 22.1.0-beta.7


This automates all the version bumping instead of manual file edits.

Creating a New Plugin

For creating a new create-nodes plugin:

nx generate @nx/workspace-plugin:create-nodes-plugin \
  --name my-custom-plugin

When to Use This Skill

Use this skill when you need to:

Generate new code or projects
Scaffold new features or libraries
Automate repetitive setup tasks
Update internal tools and configurations
Create migrations or version updates
Weekly Installs
77
Repository
nrwl/nx
GitHub Stars
28.6K
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass
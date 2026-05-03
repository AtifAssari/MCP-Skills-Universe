---
rating: ⭐⭐
title: monorepo-management
url: https://skills.sh/aj-geddes/useful-ai-prompts/monorepo-management
---

# monorepo-management

skills/aj-geddes/useful-ai-prompts/monorepo-management
monorepo-management
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill monorepo-management
SKILL.md
Monorepo Management
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Establish scalable monorepo structures that support multiple interdependent packages while maintaining build efficiency, dependency management, and deployment coordination.

When to Use
Multi-package projects
Shared libraries across services
Microservices architecture
Plugin-based systems
Multi-app platforms (web + mobile)
Workspace dependency management
Scaled team development
Quick Start

Minimal working example:

{
  "name": "monorepo-root",
  "version": "1.0.0",
  "private": true,
  "workspaces": ["packages/*", "apps/*"],
  "devDependencies": {
    "lerna": "^7.0.0",
    "turbo": "^1.10.0"
  },
  "scripts": {
    "lint": "npm run lint -r",
    "test": "npm run test -r",
    "build": "npm run build -r",
    "clean": "npm run clean -r"
  }
}

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Npm Workspaces Configuration	Npm Workspaces Configuration, Lerna Configuration, Turborepo Configuration, Nx Workspace Configuration
Monorepo Directory Structure	Monorepo Directory Structure
Workspace Dependencies	Workspace Dependencies
Lerna Commands	Lerna Commands
Turborepo Commands	Turborepo Commands
CI/CD for Monorepo	CI/CD for Monorepo
Version Management Across Packages	Version Management Across Packages
Best Practices
✅ DO
Use workspace protocols for dependencies
Implement shared tsconfig for consistency
Cache build outputs in CI/CD
Filter packages in CI to avoid unnecessary builds
Hoist common dependencies
Document workspace structure
Use consistent versioning strategy
Implement pre-commit hooks across workspace
Test cross-package dependencies
Version packages independently when appropriate
❌ DON'T
Create circular dependencies
Use hardcoded versions for workspace packages
Build all packages when only one changed
Forget to update lock files
Ignore workspace boundaries
Create tightly coupled packages
Skip dependency management
Use different tooling per package
Weekly Installs
274
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
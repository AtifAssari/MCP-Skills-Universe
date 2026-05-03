---
rating: ⭐⭐⭐
title: turborepo-monorepo
url: https://skills.sh/giuseppe-trisciuoglio/developer-kit/turborepo-monorepo
---

# turborepo-monorepo

skills/giuseppe-trisciuoglio/developer-kit/turborepo-monorepo
turborepo-monorepo
Installation
$ npx skills add https://github.com/giuseppe-trisciuoglio/developer-kit --skill turborepo-monorepo
SKILL.md
Turborepo Monorepo
Overview

Provides guidance for Turborepo monorepo management: workspace creation, turbo.json task configuration, Next.js/NestJS integration, testing pipelines (Vitest/Jest), CI/CD setup, and build performance optimization.

When to Use
Create or initialize Turborepo workspaces
Configure turbo.json tasks with dependencies and outputs
Set up Next.js/NestJS apps in monorepo structure
Configure Vitest/Jest test pipelines
Build CI/CD workflows (GitHub Actions, GitLab CI)
Implement remote caching with Vercel Remote Cache
Optimize build times and cache hit ratios
Debug task dependency or cache issues
Migrate from other monorepo tools to Turborepo
Instructions
Workspace Creation

Create a new workspace:

pnpm create turbo@latest my-workspace
cd my-workspace


Initialize in existing project:

pnpm add -D -w turbo


Create turbo.json in root (minimal config):

{
  "$schema": "https://turborepo.dev/schema.json",
  "pipeline": {
    "build": { "dependsOn": ["^build"], "outputs": ["dist/**", ".next/**"] },
    "lint": { "outputs": [] },
    "test": { "dependsOn": ["build"], "outputs": ["coverage/**"] }
  }
}


Add scripts to root package.json:

{ "scripts": { "build": "turbo run build", "dev": "turbo run dev", "lint": "turbo run lint", "test": "turbo run test", "clean": "turbo run clean" } }


Validate task graph before CI:

turbo run build --dry-run --filter=...  # Verify task execution order

Task Configuration

Configure tasks in turbo.json:

{ "pipeline": { "build": { "dependsOn": ["^build"], "outputs": ["dist/**"] }, "test": { "dependsOn": ["build"], "outputs": ["coverage/**"] }, "lint": { "outputs": [] } } }


Run tasks:

turbo run build                      # All packages
turbo run lint test build           # Multiple tasks
turbo run build --filter=web       # Specific package


Parallel type checking (use transit nodes to avoid cache issues):

{ "pipeline": { "transit": { "dependsOn": ["^transit"] }, "typecheck": { "dependsOn": ["transit"] } } }


Validate before committing:

turbo run build --dry-run  # Check task order and affected packages

Framework Integration

Next.js: outputs ".next/**" and env ["NEXT_PUBLIC_*"] - See references/nextjs-config.md

NestJS: outputs "dist/**", dev tasks with cache: false, persistent: true - See references/nestjs-config.md

Testing Setup

Vitest configuration:

{
  "pipeline": {
    "test": {
      "outputs": [],
      "inputs": ["$TURBO_DEFAULT$", "vitest.config.ts"]
    },
    "test:watch": {
      "cache": false,
      "persistent": true
    }
  }
}


Run affected tests:

turbo run test --filter=[HEAD^]


See references/testing-config.md for complete testing setup.

Package Configurations
Create package-specific turbo.json:
{
  "extends": ["//"],
  "tasks": {
    "build": {
      "outputs": ["$TURBO_EXTENDS$", ".next/**"]
    }
  }
}

See references/package-configs.md for detailed package configuration patterns.
CI/CD Setup

GitHub Actions with validation checkpoints:

- name: Install dependencies
  run: pnpm install

- name: Validate affected packages (dry-run)
  run: pnpm turbo run build --filter=[HEAD^] --dry-run
  # VALIDATE: Review output to confirm only expected packages will build

- name: Run tests
  run: pnpm run test --filter=[HEAD^]

- name: Build affected packages
  run: pnpm run build --filter=[HEAD^]

- name: Verify cache hits
  run: pnpm turbo run build --filter=[HEAD^] --dry-run | grep "Cache"
  # VALIDATE: Confirm cache hits for unchanged packages


Remote cache setup:

# Login to Vercel
npx turbo login

# Link repository
npx turbo link


See references/ci-cd.md for complete CI/CD setup examples.

Task Properties Reference
Property	Description	Example
dependsOn	Tasks that must complete first	["^build"] - dependencies first
outputs	Files/folders to cache	["dist/**"]
inputs	Files for cache hash	["src/**/*.ts"]
env	Environment variables affecting hash	["DATABASE_URL"]
cache	Enable/disable caching	true or false
persistent	Long-running task	true for dev servers
outputLogs	Log verbosity	"full", "new-only", "errors-only"
Dependency Patterns
^task - Run task in dependencies first (topological order)
task - Run task in same package first
package#task - Run specific package's task
Filter Syntax
Filter	Description
web	Only web package
web...	web + all dependencies
...web	web + all dependents
...web...	web + deps + dependents
[HEAD^]	Packages changed since last commit
./apps/*	All packages in apps/
Best Practices
Performance Optimization
Use specific outputs - Only cache what's needed
Fine-tune inputs - Exclude files that don't affect output
Transit nodes - Enable parallel type checking
Remote cache - Share cache across team/CI
Package configurations - Customize per-package behavior
Caching Strategy
{
  "pipeline": {
    "build": {
      "outputs": ["dist/**"],
      "inputs": ["$TURBO_DEFAULT$", "!README.md", "!**/*.md"]
    }
  }
}

Task Organization
Independent tasks - No dependsOn: lint, format, spellcheck
Build tasks - dependsOn: ["^build"]: build, compile
Test tasks - dependsOn: ["build"]: test, e2e
Dev tasks - cache: false, persistent: true: dev, watch
Common Issues
Tasks not running in order

Problem: Tasks execute in wrong order

Solution: Check dependsOn configuration

{
  "build": {
    "dependsOn": ["^build"]
  }
}

Cache misses on unchanged files

Problem: Cache invalidating unexpectedly

Solution: Review globalDependencies and inputs

{
  "globalDependencies": ["tsconfig.json"],
  "pipeline": {
    "build": {
      "inputs": ["$TURBO_DEFAULT$", "!*.md"]
    }
  }
}

Type errors after cache hit

Problem: TypeScript errors not caught due to cache

Solution: Use transit nodes for type checking

{
  "transit": { "dependsOn": ["^transit"] },
  "typecheck": { "dependsOn": ["transit"] }
}

Examples
Example 1: Create New Workspace

Input: "Create a Turborepo with Next.js and NestJS"

pnpm create turbo@latest my-workspace
cd my-workspace

# Add Next.js app
pnpm add next react react-dom -F apps/web

# Add NestJS API
pnpm add @nestjs/core @nestjs/common -F apps/api

Example 2: Configure Testing Pipeline

Input: "Set up Vitest for all packages"

{
  "pipeline": {
    "test": {
      "dependsOn": ["build"],
      "outputs": ["coverage/**"],
      "inputs": ["$TURBO_DEFAULT$", "vitest.config.ts"]
    },
    "test:watch": {
      "cache": false,
      "persistent": true
    }
  }
}

Example 3: Run Affected Tests in CI

Input: "Only test changed packages in CI"

pnpm run test --filter=[HEAD^]

Example 4: Debug Cache Issues

Input: "Why is my cache missing?"

# Dry run to see what would be executed
turbo run build --dry-run --filter=web

# Show hash inputs
turbo run build --force --filter=web

Constraints and Warnings
Node.js 18+ is required for Turborepo
Package manager field required in root package.json
Outputs must be specified for caching to work
Persistent tasks cannot have dependents
Windows: WSL or Git Bash recommended
Remote cache requires Vercel account or self-hosted solution
Large monorepos may need increased concurrency settings
Reference Files

For detailed guidance on specific topics, consult:

Topic	Reference File
turbo.json template	references/turbo.json
Next.js integration	references/nextjs-config.md
NestJS integration	references/nestjs-config.md
Vitest/Jest/Playwright	references/testing-config.md
GitHub/CircleCI/GitLab CI	references/ci-cd.md
Package configurations	references/package-configs.md
Weekly Installs
631
Repository
giuseppe-trisci…oper-kit
GitHub Stars
233
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
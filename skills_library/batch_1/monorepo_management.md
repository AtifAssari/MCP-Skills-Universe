---
title: monorepo-management
url: https://skills.sh/wshobson/agents/monorepo-management
---

# monorepo-management

skills/wshobson/agents/monorepo-management
monorepo-management
Installation
$ npx skills add https://github.com/wshobson/agents --skill monorepo-management
Summary

Efficient, scalable monorepos with optimized builds and shared dependencies across multiple packages.

Covers three major tools: Turborepo (recommended for most projects), Nx (feature-rich alternative), and pnpm workspaces (package manager)
Includes setup patterns for shared configurations (TypeScript, ESLint, Prettier), code sharing strategies (UI components, utilities, types), and dependency management across packages
Provides Turborepo pipeline configuration with caching, input/output optimization, and remote cache setup for CI/CD acceleration
Includes GitHub Actions workflows for monorepo CI/CD, affected-only deployments, and package publishing with Changesets
Documents best practices for dependency graphs, versioning, testing strategies, and common pitfalls like circular dependencies and phantom dependencies
SKILL.md
Monorepo Management

Build efficient, scalable monorepos that enable code sharing, consistent tooling, and atomic changes across multiple packages and applications.

When to Use This Skill
Setting up new monorepo projects
Migrating from multi-repo to monorepo
Optimizing build and test performance
Managing shared dependencies
Implementing code sharing strategies
Setting up CI/CD for monorepos
Versioning and publishing packages
Debugging monorepo-specific issues
Core Concepts
1. Why Monorepos?

Advantages:

Shared code and dependencies
Atomic commits across projects
Consistent tooling and standards
Easier refactoring
Simplified dependency management
Better code visibility

Challenges:

Build performance at scale
CI/CD complexity
Access control
Large Git repository
2. Monorepo Tools

Package Managers:

pnpm workspaces (recommended)
npm workspaces
Yarn workspaces

Build Systems:

Turborepo (recommended for most)
Nx (feature-rich, complex)
Lerna (older, maintenance mode)
Turborepo Setup
Initial Setup
# Create new monorepo
npx create-turbo@latest my-monorepo
cd my-monorepo

# Structure:
# apps/
#   web/          - Next.js app
#   docs/         - Documentation site
# packages/
#   ui/           - Shared UI components
#   config/       - Shared configurations
#   tsconfig/     - Shared TypeScript configs
# turbo.json      - Turborepo configuration
# package.json    - Root package.json

Configuration
// turbo.json
{
  "$schema": "https://turbo.build/schema.json",
  "globalDependencies": ["**/.env.*local"],
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**", ".next/**", "!.next/cache/**"]
    },
    "test": {
      "dependsOn": ["build"],
      "outputs": ["coverage/**"]
    },
    "lint": {
      "outputs": []
    },
    "dev": {
      "cache": false,
      "persistent": true
    },
    "type-check": {
      "dependsOn": ["^build"],
      "outputs": []
    }
  }
}

// package.json (root)
{
  "name": "my-monorepo",
  "private": true,
  "workspaces": ["apps/*", "packages/*"],
  "scripts": {
    "build": "turbo run build",
    "dev": "turbo run dev",
    "test": "turbo run test",
    "lint": "turbo run lint",
    "format": "prettier --write \"**/*.{ts,tsx,md}\"",
    "clean": "turbo run clean && rm -rf node_modules"
  },
  "devDependencies": {
    "turbo": "^1.10.0",
    "prettier": "^3.0.0",
    "typescript": "^5.0.0"
  },
  "packageManager": "pnpm@8.0.0"
}

Package Structure
// packages/ui/package.json
{
  "name": "@repo/ui",
  "version": "0.0.0",
  "private": true,
  "main": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "exports": {
    ".": {
      "import": "./dist/index.js",
      "types": "./dist/index.d.ts"
    },
    "./button": {
      "import": "./dist/button.js",
      "types": "./dist/button.d.ts"
    }
  },
  "scripts": {
    "build": "tsup src/index.ts --format esm,cjs --dts",
    "dev": "tsup src/index.ts --format esm,cjs --dts --watch",
    "lint": "eslint src/",
    "type-check": "tsc --noEmit"
  },
  "devDependencies": {
    "@repo/tsconfig": "workspace:*",
    "tsup": "^7.0.0",
    "typescript": "^5.0.0"
  },
  "dependencies": {
    "react": "^18.2.0"
  }
}

pnpm Workspaces
Setup
# pnpm-workspace.yaml
packages:
  - "apps/*"
  - "packages/*"
  - "tools/*"

// .npmrc
# Hoist shared dependencies
shamefully-hoist=true

# Strict peer dependencies
auto-install-peers=true
strict-peer-dependencies=true

# Performance
store-dir=~/.pnpm-store

Dependency Management
# Install dependency in specific package
pnpm add react --filter @repo/ui
pnpm add -D typescript --filter @repo/ui

# Install workspace dependency
pnpm add @repo/ui --filter web

# Install in all packages
pnpm add -D eslint -w

# Update all dependencies
pnpm update -r

# Remove dependency
pnpm remove react --filter @repo/ui

Scripts
# Run script in specific package
pnpm --filter web dev
pnpm --filter @repo/ui build

# Run in all packages
pnpm -r build
pnpm -r test

# Run in parallel
pnpm -r --parallel dev

# Filter by pattern
pnpm --filter "@repo/*" build
pnpm --filter "...web" build  # Build web and dependencies

Nx Monorepo
Setup
# Create Nx monorepo
npx create-nx-workspace@latest my-org

# Generate applications
nx generate @nx/react:app my-app
nx generate @nx/next:app my-next-app

# Generate libraries
nx generate @nx/react:lib ui-components
nx generate @nx/js:lib utils

Configuration
// nx.json
{
  "extends": "nx/presets/npm.json",
  "$schema": "./node_modules/nx/schemas/nx-schema.json",
  "targetDefaults": {
    "build": {
      "dependsOn": ["^build"],
      "inputs": ["production", "^production"],
      "cache": true
    },
    "test": {
      "inputs": ["default", "^production", "{workspaceRoot}/jest.preset.js"],
      "cache": true
    },
    "lint": {
      "inputs": ["default", "{workspaceRoot}/.eslintrc.json"],
      "cache": true
    }
  },
  "namedInputs": {
    "default": ["{projectRoot}/**/*", "sharedGlobals"],
    "production": [
      "default",
      "!{projectRoot}/**/?(*.)+(spec|test).[jt]s?(x)?(.snap)",
      "!{projectRoot}/tsconfig.spec.json"
    ],
    "sharedGlobals": []
  }
}

Running Tasks
# Run task for specific project
nx build my-app
nx test ui-components
nx lint utils

# Run for affected projects
nx affected:build
nx affected:test --base=main

# Visualize dependencies
nx graph

# Run in parallel
nx run-many --target=build --all --parallel=3

Shared Configurations
TypeScript Configuration
// packages/tsconfig/base.json
{
  "compilerOptions": {
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "module": "ESNext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "incremental": true,
    "declaration": true
  },
  "exclude": ["node_modules"]
}

// packages/tsconfig/react.json
{
  "extends": "./base.json",
  "compilerOptions": {
    "jsx": "react-jsx",
    "lib": ["ES2022", "DOM", "DOM.Iterable"]
  }
}

// apps/web/tsconfig.json
{
  "extends": "@repo/tsconfig/react.json",
  "compilerOptions": {
    "outDir": "dist",
    "rootDir": "src"
  },
  "include": ["src"],
  "exclude": ["node_modules", "dist"]
}

ESLint Configuration
// packages/config/eslint-preset.js
module.exports = {
  extends: [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:react/recommended",
    "plugin:react-hooks/recommended",
    "prettier",
  ],
  plugins: ["@typescript-eslint", "react", "react-hooks"],
  parser: "@typescript-eslint/parser",
  parserOptions: {
    ecmaVersion: 2022,
    sourceType: "module",
    ecmaFeatures: {
      jsx: true,
    },
  },
  settings: {
    react: {
      version: "detect",
    },
  },
  rules: {
    "@typescript-eslint/no-unused-vars": "error",
    "react/react-in-jsx-scope": "off",
  },
};

// apps/web/.eslintrc.js
module.exports = {
  extends: ["@repo/config/eslint-preset"],
  rules: {
    // App-specific rules
  },
};

Code Sharing Patterns
Pattern 1: Shared UI Components
// packages/ui/src/button.tsx
import * as React from 'react';

export interface ButtonProps {
  variant?: 'primary' | 'secondary';
  children: React.ReactNode;
  onClick?: () => void;
}

export function Button({ variant = 'primary', children, onClick }: ButtonProps) {
  return (
    <button
      className={`btn btn-${variant}`}
      onClick={onClick}
    >
      {children}
    </button>
  );
}

// packages/ui/src/index.ts
export { Button, type ButtonProps } from './button';
export { Input, type InputProps } from './input';

// apps/web/src/app.tsx
import { Button } from '@repo/ui';

export function App() {
  return <Button variant="primary">Click me</Button>;
}

Pattern 2: Shared Utilities
// packages/utils/src/string.ts
export function capitalize(str: string): string {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

export function truncate(str: string, length: number): string {
  return str.length > length ? str.slice(0, length) + "..." : str;
}

// packages/utils/src/index.ts
export * from "./string";
export * from "./array";
export * from "./date";

// Usage in apps
import { capitalize, truncate } from "@repo/utils";

Pattern 3: Shared Types
// packages/types/src/user.ts
export interface User {
  id: string;
  email: string;
  name: string;
  role: "admin" | "user";
}

export interface CreateUserInput {
  email: string;
  name: string;
  password: string;
}

// Used in both frontend and backend
import type { User, CreateUserInput } from "@repo/types";

Build Optimization
Turborepo Caching
// turbo.json
{
  "pipeline": {
    "build": {
      // Build depends on dependencies being built first
      "dependsOn": ["^build"],

      // Cache these outputs
      "outputs": ["dist/**", ".next/**"],

      // Cache based on these inputs (default: all files)
      "inputs": ["src/**/*.tsx", "src/**/*.ts", "package.json"]
    },
    "test": {
      // Run tests in parallel, don't depend on build
      "cache": true,
      "outputs": ["coverage/**"]
    }
  }
}

Remote Caching
# Turborepo Remote Cache (Vercel)
npx turbo login
npx turbo link

# Custom remote cache
# turbo.json
{
  "remoteCache": {
    "signature": true,
    "enabled": true
  }
}

CI/CD for Monorepos
GitHub Actions
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0 # For Nx affected commands

      - uses: pnpm/action-setup@v2
        with:
          version: 8

      - uses: actions/setup-node@v3
        with:
          node-version: 18
          cache: "pnpm"

      - name: Install dependencies
        run: pnpm install --frozen-lockfile

      - name: Build
        run: pnpm turbo run build

      - name: Test
        run: pnpm turbo run test

      - name: Lint
        run: pnpm turbo run lint

      - name: Type check
        run: pnpm turbo run type-check

Deploy Affected Only
# Deploy only changed apps
- name: Deploy affected apps
  run: |
    if pnpm nx affected:apps --base=origin/main --head=HEAD | grep -q "web"; then
      echo "Deploying web app"
      pnpm --filter web deploy
    fi

Best Practices
Consistent Versioning: Lock dependency versions across workspace
Shared Configs: Centralize ESLint, TypeScript, Prettier configs
Dependency Graph: Keep it acyclic, avoid circular dependencies
Cache Effectively: Configure inputs/outputs correctly
Type Safety: Share types between frontend/backend
Testing Strategy: Unit tests in packages, E2E in apps
Documentation: README in each package
Release Strategy: Use changesets for versioning
Common Pitfalls
Circular Dependencies: A depends on B, B depends on A
Phantom Dependencies: Using deps not in package.json
Incorrect Cache Inputs: Missing files in Turborepo inputs
Over-Sharing: Sharing code that should be separate
Under-Sharing: Duplicating code across packages
Large Monorepos: Without proper tooling, builds slow down
Publishing Packages
# Using Changesets
pnpm add -Dw @changesets/cli
pnpm changeset init

# Create changeset
pnpm changeset

# Version packages
pnpm changeset version

# Publish
pnpm changeset publish

# .github/workflows/release.yml
- name: Create Release Pull Request or Publish
  uses: changesets/action@v1
  with:
    publish: pnpm release
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
    NPM_TOKEN: ${{ secrets.NPM_TOKEN }}

Weekly Installs
8.1K
Repository
wshobson/agents
GitHub Stars
34.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
---
rating: ⭐⭐⭐
title: typescript:build-tools
url: https://skills.sh/martinffx/atelier/typescript:build-tools
---

# typescript:build-tools

skills/martinffx/atelier/typescript:build-tools
typescript:build-tools
Installation
$ npx skills add https://github.com/martinffx/atelier --skill typescript:build-tools
SKILL.md
TypeScript Build Tools

Modern TypeScript build tooling stack: Bun for package management and task running, tsgo for typechecking, Vitest for testing, Biome for linting/formatting, and Turborepo for monorepo orchestration.

Additional References
references/bun.md - Bun package manager and task runner
references/vitest.md - Advanced Vitest configuration patterns
references/biome.md - Biome rules and customization
references/turborepo.md - Turborepo monorepo orchestration
Quick Start
# Install dependencies
bun add -D vitest @vitest/coverage-v8 @biomejs/biome

# For monorepos
bun add -D turbo

Package.json Scripts
Single Package
{
  "scripts": {
    "dev": "bun run --watch src/index.ts",
    "build": "bun build ./src/index.ts --outdir ./dist --target bun",
    "typecheck": "tsgo --noEmit",
    "test": "vitest run",
    "test:watch": "vitest",
    "test:coverage": "vitest run --coverage",
    "lint": "biome check .",
    "lint:fix": "biome check --write .",
    "format": "biome format --write .",
    "check": "bun run typecheck && bun run lint && bun run test"
  }
}

Monorepo Root
{
  "scripts": {
    "dev": "turbo dev",
    "build": "turbo build",
    "typecheck": "turbo typecheck",
    "test": "turbo test",
    "lint": "turbo lint",
    "check": "turbo typecheck lint test"
  }
}

Bun
Package Manager
# Install dependencies
bun install

# Add dependencies
bun add fastify drizzle-orm
bun add -D vitest @biomejs/biome

# Remove dependency
bun remove package-name

# Update dependencies
bun update

Task Runner

Important: Use bun run test (not bun test) on Node projects. bun test invokes Bun's native test runner, not your package.json test script.

# Run script from package.json
bun run dev
bun run test
bun run build

# Run TypeScript directly (no build step)
bun run src/index.ts

# Watch mode
bun run --watch src/index.ts

# With environment variables
bun run --env-file .env src/index.ts

Build Command
# Basic build for Bun runtime
bun build ./src/index.ts --outdir ./dist --target bun

# For Node.js runtime
bun build ./src/index.ts --outdir ./dist --target node

# With minification
bun build ./src/index.ts --outdir ./dist --target bun --minify

# Multiple entry points
bun build ./src/index.ts ./src/worker.ts --outdir ./dist --target bun


See references/bun.md for bunfig.toml configuration and advanced patterns.

tsgo Typechecking

tsgo is a fast TypeScript typechecker. Use it instead of tsc for faster CI builds.

# Typecheck without emitting
tsgo --noEmit

# Typecheck specific files
tsgo --noEmit src/**/*.ts

# With project reference
tsgo --noEmit -p tsconfig.json

tsconfig.json
{
  "compilerOptions": {
    "target": "ESNext",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "strict": true,
    "skipLibCheck": true,
    "noEmit": true,
    "esModuleInterop": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "verbatimModuleSyntax": true,
    "lib": ["ESNext"],
    "types": ["bun-types"]
  },
  "include": ["src/**/*.ts"],
  "exclude": ["node_modules", "dist"]
}

Vitest
Basic Configuration
// vitest.config.ts
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    globals: true,
    environment: 'node',
    include: ['src/**/*.test.ts', 'test/**/*.test.ts'],
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html'],
      include: ['src/**/*.ts'],
      exclude: ['src/**/*.test.ts', 'src/types/**'],
    },
  },
})

With Path Aliases
// vitest.config.ts
import { defineConfig } from 'vitest/config'
import tsconfigPaths from 'vite-tsconfig-paths'

export default defineConfig({
  plugins: [tsconfigPaths()],
  test: {
    globals: true,
  },
})

Global Setup (Database Migrations)
// vitest.config.ts
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    globals: true,
    globalSetup: './test/global-setup.ts',
    setupFiles: ['./test/setup.ts'],
  },
})

// test/global-setup.ts
import { execSync } from 'node:child_process'

export async function setup() {
  console.log('Running database migrations...')
  execSync('drizzle-kit migrate', { stdio: 'inherit' })
}

export async function teardown() {
  console.log('Test teardown complete')
}


See references/vitest.md for workspace configs, benchmarks, and Cloudflare Workers pool.

Biome
Basic biome.json
{
  "$schema": "https://biomejs.dev/schemas/2.0.0/schema.json",
  "vcs": {
    "enabled": true,
    "clientKind": "git",
    "useIgnoreFile": true
  },
  "files": {
    "ignoreUnknown": true,
    "ignore": ["dist", "node_modules", "*.gen.ts"]
  },
  "formatter": {
    "enabled": true,
    "indentStyle": "tab",
    "lineWidth": 100
  },
  "javascript": {
    "formatter": {
      "quoteStyle": "double",
      "trailingCommas": "es5"
    }
  },
  "linter": {
    "enabled": true,
    "rules": {
      "recommended": true
    }
  },
  "organizeImports": {
    "enabled": true
  }
}

Strict Rules (Production)
{
  "linter": {
    "enabled": true,
    "rules": {
      "recommended": true,
      "complexity": {
        "noForEach": "error"
      },
      "performance": {
        "noDelete": "error"
      },
      "style": {
        "useNodejsImportProtocol": "error"
      }
    }
  }
}


See references/biome.md for rule explanations, shareable configs, and CLI commands.

Turborepo (Monorepo)
turbo.json
{
  "$schema": "https://turbo.build/schema.json",
  "tasks": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**"]
    },
    "typecheck": {
      "dependsOn": ["^typecheck"]
    },
    "lint": {},
    "test": {
      "dependsOn": ["^build"],
      "env": ["DATABASE_URL"]
    },
    "dev": {
      "cache": false,
      "persistent": true
    }
  }
}

Workspace Structure
my-monorepo/
├── package.json          # Root with turbo scripts
├── turbo.json            # Turbo configuration
├── biome.json            # Shared Biome config
├── packages/
│   ├── config-biome/     # Shareable Biome package
│   └── shared/           # Shared utilities
├── apps/
│   ├── api/              # Fastify API
│   └── web/              # React app
└── bun.lock


See references/turborepo.md for caching strategies, filtering, and CI setup.

Cloudflare Workers
Vite + Cloudflare Plugin
// vite.config.ts
import { cloudflare } from '@cloudflare/vite-plugin'
import { reactRouter } from '@react-router/dev/vite'
import tailwindcss from '@tailwindcss/vite'
import tsconfigPaths from 'vite-tsconfig-paths'
import { defineConfig } from 'vite'

export default defineConfig({
  plugins: [
    cloudflare({ viteEnvironment: { name: 'ssr' } }),
    tailwindcss(),
    reactRouter(),
    tsconfigPaths(),
  ],
})

Vitest with Cloudflare Workers Pool
// vitest.config.ts
import { defineWorkersConfig } from '@cloudflare/vitest-pool-workers/config'

export default defineWorkersConfig({
  test: {
    globals: true,
    pool: '@cloudflare/vitest-pool-workers',
    poolOptions: {
      workers: {
        wrangler: { configPath: './wrangler.jsonc' },
      },
    },
  },
})

CI Pipeline
GitHub Actions
name: typescript:build-tools

on:
  push:
    branches: [main]
  pull_request:

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: oven-sh/setup-bun@v2
        with:
          bun-version: latest

      - run: bun install --frozen-lockfile

      - run: bun run typecheck
      - run: bun run lint
      - run: bun run test

Monorepo CI with Turbo
name: typescript:build-tools

on:
  push:
    branches: [main]
  pull_request:

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: oven-sh/setup-bun@v2

      - run: bun install --frozen-lockfile

      - run: bun run check  # turbo typecheck lint test
        env:
          TURBO_TOKEN: ${{ secrets.TURBO_TOKEN }}
          TURBO_TEAM: ${{ vars.TURBO_TEAM }}

Guidelines
Use Bun as package manager (bun install) and task runner (bun run)
Use bun run test (not bun test) - bun test runs Bun's native test runner
Use tsgo for typechecking - faster than tsc for CI
Use Vitest for testing - fast, ESM-native, great DX
Use Biome for linting and formatting - single tool, fast
Use Turborepo for monorepos - caching, parallel execution
Enable V8 coverage in Vitest for accurate coverage reports
Configure global setup for database migrations in tests
Use workspace configs in Vitest for different test pools
Share Biome config via workspace package in monorepos
Run checks in order: typecheck, lint, test (fail fast)
Use --frozen-lockfile in CI for reproducible builds
Configure Turbo caching for faster CI with remote cache
Weekly Installs
8
Repository
martinffx/atelier
GitHub Stars
20
First Seen
Mar 7, 2026
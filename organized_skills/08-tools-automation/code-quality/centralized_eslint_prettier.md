---
rating: ⭐⭐⭐
title: centralized-eslint-prettier
url: https://skills.sh/loxosceles/ai-dev/centralized-eslint-prettier
---

# centralized-eslint-prettier

skills/loxosceles/ai-dev/centralized-eslint-prettier
centralized-eslint-prettier
Installation
$ npx skills add https://github.com/loxosceles/ai-dev --skill centralized-eslint-prettier
SKILL.md
Centralized ESLint # Centralized ESLint & Prettier Configuration Prettier Configuration

This is a reference pattern. Learn from the approach, adapt to your context — don't copy verbatim.

Problem: Multi-workspace TypeScript projects (frontend, backend, infrastructure) need consistent linting and formatting without duplication, with support for pre-commit hooks and full-repo formatting.

Solution: Single root-level eslint.config.mjs with workspace-specific rules via file patterns, unified Prettier config, and centralized npm scripts with Husky integration.

Why This Pattern?

Benefits:

Single Source of Truth: One config file, no duplication
Workspace Flexibility: Different rules per workspace via file patterns
Simplified Maintenance: Update rules in one place
Consistent Pre-commit: Same hooks across all workspaces
Easy CI/CD: Single command lints entire codebase
Project Agnostic: Works for any TypeScript monorepo structure

Use Cases:

Multi-workspace TypeScript projects (Next.js + CDK, Nuxt + Node.js, etc.)
Projects with different linting needs per workspace (frontend vs CLI vs Lambda)
Teams wanting consistent code style without per-workspace configuration
Projects needing both pre-commit hooks and full-repo formatting
Pattern

Architecture:

project-root/
├── eslint.config.mjs          # Single source of truth
├── .prettierrc                 # Unified formatting rules
├── package.json                # Root scripts only
├── .husky/pre-commit          # Git hooks
├── pnpm-workspace.yaml
├── frontend/
│   ├── package.json           # NO lint scripts
│   └── tsconfig.json
└── infrastructure/
    ├── package.json           # NO lint scripts
    └── tsconfig.json


Key Components:

Root ESLint Config: Flat config (ESLint 9+) with file pattern-based rules
Workspace-Specific Rules: Different rules for frontend/backend/CLI via glob patterns
Prettier Integration: Single .prettierrc for all workspaces
Husky + lint-staged: Pre-commit formatting on changed files
Centralized Scripts: All lint/format commands in root package.json
Implementation
1. Root ESLint Config (eslint.config.mjs)
import js from '@eslint/js';
import typescriptEslint from '@typescript-eslint/eslint-plugin';
import typescriptParser from '@typescript-eslint/parser';
import globals from 'globals';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const IGNORE_PATTERNS = [
  '**/node_modules/**',
  '**/dist/**',
  '**/build/**',
  '**/.next/**',
  '**/cdk.out/**',
  '**/*.d.ts',
  '**/*.config.js'
];

const SHARED_RULES = {
  'eol-last': ['error', 'always'],
  'no-console': ['warn', { allow: ['error', 'warn'] }],
  'no-unused-vars': 'off'
};

export default [
  // Global ignores
  { ignores: IGNORE_PATTERNS },

  // Frontend TypeScript
  {
    files: ['frontend/**/*.{ts,tsx}'],
    languageOptions: {
      parser: typescriptParser,
      parserOptions: {
        project: path.join(__dirname, 'frontend/tsconfig.json'),
        ecmaVersion: 'latest',
        sourceType: 'module'
      }
    },
    plugins: { '@typescript-eslint': typescriptEslint },
    rules: {
      ...SHARED_RULES,
      '@typescript-eslint/no-unused-vars': 'warn',
      '@typescript-eslint/no-explicit-any': 'error'
    }
  },

  // Infrastructure TypeScript
  {
    files: ['infrastructure/**/*.ts'],
    languageOptions: {
      parser: typescriptParser,
      parserOptions: {
        project: path.join(__dirname, 'infrastructure/tsconfig.json'),
        ecmaVersion: 'latest',
        sourceType: 'module'
      }
    },
    plugins: { '@typescript-eslint': typescriptEslint },
    rules: {
      ...SHARED_RULES,
      '@typescript-eslint/no-unused-vars': 'warn',
      '@typescript-eslint/no-explicit-any': 'error'
    }
  },

  // CLI scripts - allow console output
  {
    files: [
      'infrastructure/lib/cli/**/*.ts',
      'scripts/**/*.ts'
    ],
    rules: { 'no-console': 'off' }
  }
];

2. Prettier Config (.prettierrc)
{
  "semi": true,
  "trailingComma": "all",
  "singleQuote": true,
  "printWidth": 100,
  "tabWidth": 2,
  "endOfLine": "auto"
}

3. Root Package.json Scripts
{
  "scripts": {
    "lint": "eslint . --ext .ts,.tsx,.js,.jsx",
    "lint:fix": "eslint . --ext .ts,.tsx,.js,.jsx --fix",
    "format": "prettier --write \"**/*.{ts,tsx,js,jsx,json,md}\"",
    "format:check": "prettier --check \"**/*.{ts,tsx,js,jsx,json,md}\"",
    "prepare": "husky"
  },
  "lint-staged": {
    "**/*.{js,jsx,ts,tsx}": [
      "eslint --fix",
      "prettier --write --end-of-line auto"
    ],
    "*.{json,md,yml}": [
      "prettier --write --end-of-line auto"
    ]
  }
}


Critical: Workspace package.json files should NOT have lint/format scripts.

4. Husky Pre-commit Hook
# .husky/pre-commit
pnpm exec lint-staged

5. Dependencies
pnpm add -D -w eslint \
  @typescript-eslint/parser \
  @typescript-eslint/eslint-plugin \
  typescript-eslint \
  @eslint/js \
  globals \
  prettier \
  eslint-config-prettier \
  husky \
  lint-staged

Framework-Specific Variations
Next.js Frontend
import nextPlugin from '@next/eslint-plugin-next';

{
  files: ['frontend/**/*.{ts,tsx}'],
  plugins: {
    '@next/next': nextPlugin,
    '@typescript-eslint': typescriptEslint
  },
  settings: {
    next: { rootDir: path.join(__dirname, 'frontend') }
  }
}

Nuxt.js Frontend (Auto-generated Config)

Nuxt auto-generates .nuxt/eslint.config.mjs. Keep it and extend:

// frontend/eslint.config.mjs
import withNuxt from './.nuxt/eslint.config.mjs';
import { SHARED_RULES } from '../eslint.shared.mjs';

export default withNuxt({
  rules: { ...SHARED_RULES }
});


Note: For Nuxt, keep the workspace-level config due to auto-generation. Create eslint.shared.mjs at root to share rules.

Lambda Functions
{
  files: ['infrastructure/lib/lambdas/**/*.ts'],
  rules: {
    'no-console': 'off',  // CloudWatch logs
    '@typescript-eslint/no-explicit-any': 'error'
  }
}

Workspace-Specific Patterns
Two-Tier CLI (Simple Projects)
{
  files: ['scripts/**/*.ts', 'tools/**/*.ts'],
  rules: { 'no-console': 'off' }
}

Three-Tier CLI (Infrastructure Projects)
// Tier 1: CLI Binaries
{
  files: ['infrastructure/lib/cli/bin/**/*.ts'],
  rules: { 'no-console': 'off' }
},

// Tier 2: Commands
{
  files: ['infrastructure/lib/cli/commands/**/*.ts'],
  rules: { 'no-console': 'off' }
},

// Tier 3: Domain Logic
{
  files: ['infrastructure/core/**/*.ts'],
  rules: { 'no-console': 'warn' }
}

Usage
Pre-commit (Automatic)
git add .
git commit -m "feat: add feature"
# Automatically runs lint-staged on changed files

Full Repo Formatting
# Check formatting
pnpm format:check

# Fix all files
pnpm format

# Lint entire codebase
pnpm lint

# Auto-fix linting issues
pnpm lint:fix

CI/CD Integration
# GitHub Actions
- run: pnpm install --frozen-lockfile
- run: pnpm lint
- run: pnpm format:check

Tradeoffs
ESLint 9+ Flat Config Required

Constraint: This pattern uses ESLint 9+ flat config format (.mjs file).

Why: Flat config is the future of ESLint and provides better TypeScript support.

Migration: Old .eslintrc.js configs need conversion. See ESLint migration guide.

File Pattern Ordering Matters

Constraint: More specific patterns must come after general ones.

Example:

// ✅ Correct order
{ files: ['**/*.ts'], rules: {...} },
{ files: ['frontend/**/*.ts'], rules: {...} },
{ files: ['frontend/lib/cli/**/*.ts'], rules: {...} }

// ❌ Wrong order - specific rules won't apply
{ files: ['frontend/lib/cli/**/*.ts'], rules: {...} },
{ files: ['**/*.ts'], rules: {...} }

Nuxt.js Exception

Constraint: Nuxt auto-generates ESLint config, requiring workspace-level config.

Solution: Keep frontend/eslint.config.mjs but import shared rules from root via eslint.shared.mjs.

When NOT to Use
Single-workspace projects: Simpler to use workspace-level config
Non-TypeScript projects: Pattern is TypeScript-focused (though adaptable)
Legacy ESLint versions: Requires ESLint 9+ for flat config
Highly divergent workspace needs: If workspaces need completely different tooling, separate configs may be clearer
Verification Checklist

After setup:

# 1. Full codebase linting works
pnpm lint

# 2. Auto-fix works
pnpm lint:fix

# 3. Formatting works
pnpm format

# 4. Pre-commit hooks work
git add . && git commit -m "test"

# 5. No duplicate scripts in workspaces
grep -r '"lint":' */package.json
# Should ONLY show root package.json

Related Patterns
CLI Architecture - Understanding CLI tiers for console.log rules
Environment Validation - Fail-fast validation patterns
Progressive Improvement

If the developer corrects a behavior that this skill should have prevented, suggest a specific amendment to this skill to prevent the same correction in the future.

Weekly Installs
39
Repository
loxosceles/ai-dev
First Seen
Mar 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
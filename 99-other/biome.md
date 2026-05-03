---
rating: ⭐⭐⭐
title: biome
url: https://skills.sh/bobmatnyc/claude-mpm-skills/biome
---

# biome

skills/bobmatnyc/claude-mpm-skills/biome
biome
Installation
$ npx skills add https://github.com/bobmatnyc/claude-mpm-skills --skill biome
Summary

Fast, Rust-based linter and formatter replacing ESLint and Prettier with 100x speed improvement.

Single tool combining linting, formatting, and import sorting with zero-config defaults and TypeScript-first design
Supports three core commands: check (lint + format together), format (formatting only), and lint (linting only), all with --write for automatic fixes
Includes VS Code extension with format-on-save, organized rule categories (correctness, style, suspicious, performance, security, a11y), and file-level overrides for monorepo and project-specific configurations
Native monorepo support, intelligent caching, parallel CPU processing, and seamless migration tools from ESLint and Prettier configurations
SKILL.md
Biome - Fast All-in-One Toolchain
Overview

Biome is a fast, all-in-one toolchain for web projects written in Rust. It replaces both ESLint and Prettier with a single tool that's 100x faster and provides zero-config defaults.

Key Features:

Single tool for linting and formatting
100x faster than ESLint
Zero configuration by default
Built-in import sorting
TypeScript-first design
Partial Prettier compatibility
Native monorepo support
VS Code integration

Installation:

npm install --save-dev @biomejs/biome

Quick Start
1. Initialize Biome
# Create biome.json configuration
npx @biomejs/biome init

# Check your project
npx @biomejs/biome check .

# Fix issues automatically
npx @biomejs/biome check --write .

# Format only
npx @biomejs/biome format --write .

# Lint only
npx @biomejs/biome lint .

2. Package.json Scripts
{
  "scripts": {
    "check": "biome check .",
    "check:write": "biome check --write .",
    "format": "biome format --write .",
    "lint": "biome lint .",
    "lint:fix": "biome lint --write ."
  }
}

3. Basic Configuration
{
  "$schema": "https://biomejs.dev/schemas/1.9.4/schema.json",
  "vcs": {
    "enabled": true,
    "clientKind": "git",
    "useIgnoreFile": true
  },
  "files": {
    "ignoreUnknown": false,
    "ignore": ["node_modules", "dist", "build", ".next"]
  },
  "formatter": {
    "enabled": true,
    "indentStyle": "space",
    "indentWidth": 2,
    "lineWidth": 100
  },
  "linter": {
    "enabled": true,
    "rules": {
      "recommended": true
    }
  },
  "javascript": {
    "formatter": {
      "quoteStyle": "single",
      "semicolons": "asNeeded",
      "trailingCommas": "all"
    }
  }
}

Core Commands
Check Command (Recommended)

The check command runs both linting and formatting:

# Check all files
biome check .

# Fix issues automatically
biome check --write .

# Unsafe fixes (may change behavior)
biome check --write --unsafe .

# Apply suggested fixes
biome check --write --unsafe --apply-suggested

# Check specific files
biome check src/**/*.ts

# CI mode (exit with error on issues)
biome ci .

Format Command

Format code without linting:

# Format all files
biome format --write .

# Check formatting without changing files
biome format .

# Format specific files
biome format --write src/**/*.{ts,tsx,js,jsx}

# Format stdin
echo "const x={a:1}" | biome format --stdin-file-path=file.js

Lint Command

Lint code without formatting:

# Lint all files
biome lint .

# Fix linting issues
biome lint --write .

# Show rule names
biome lint --verbose .

# Apply unsafe fixes
biome lint --write --unsafe .

Configuration Deep Dive
Formatter Configuration
{
  "formatter": {
    "enabled": true,
    "formatWithErrors": false,
    "indentStyle": "space",
    "indentWidth": 2,
    "lineEnding": "lf",
    "lineWidth": 80,
    "attributePosition": "auto"
  },
  "javascript": {
    "formatter": {
      "quoteStyle": "single",
      "jsxQuoteStyle": "double",
      "quoteProperties": "asNeeded",
      "trailingCommas": "all",
      "semicolons": "asNeeded",
      "arrowParentheses": "always",
      "bracketSpacing": true,
      "bracketSameLine": false
    }
  },
  "json": {
    "formatter": {
      "trailingCommas": "none"
    }
  }
}

Linter Configuration
{
  "linter": {
    "enabled": true,
    "rules": {
      "recommended": true,
      "a11y": {
        "recommended": true,
        "noAutofocus": "error",
        "useKeyWithClickEvents": "warn"
      },
      "complexity": {
        "recommended": true,
        "noForEach": "off",
        "useLiteralKeys": "error"
      },
      "correctness": {
        "recommended": true,
        "noUnusedVariables": "error",
        "useExhaustiveDependencies": "warn"
      },
      "performance": {
        "recommended": true,
        "noAccumulatingSpread": "warn"
      },
      "security": {
        "recommended": true,
        "noDangerouslySetInnerHtml": "error"
      },
      "style": {
        "recommended": true,
        "noNonNullAssertion": "warn",
        "useConst": "error",
        "useTemplate": "warn"
      },
      "suspicious": {
        "recommended": true,
        "noExplicitAny": "warn",
        "noArrayIndexKey": "error"
      }
    }
  }
}

File Ignore Patterns
{
  "files": {
    "ignore": [
      "node_modules",
      "dist",
      "build",
      ".next",
      "coverage",
      "*.min.js",
      "public/assets/**"
    ],
    "ignoreUnknown": false,
    "include": ["src/**/*.ts", "src/**/*.tsx"]
  }
}

Override Configuration for Specific Files
{
  "overrides": [
    {
      "include": ["**/*.test.ts", "**/*.spec.ts"],
      "linter": {
        "rules": {
          "suspicious": {
            "noExplicitAny": "off"
          }
        }
      }
    },
    {
      "include": ["scripts/**/*.js"],
      "formatter": {
        "lineWidth": 120
      }
    }
  ]
}

VS Code Integration
1. Install Biome Extension
# Install from VS Code marketplace
code --install-extension biomejs.biome

2. VS Code Settings (.vscode/settings.json)
{
  "[javascript]": {
    "editor.defaultFormatter": "biomejs.biome",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "quickfix.biome": "explicit",
      "source.organizeImports.biome": "explicit"
    }
  },
  "[typescript]": {
    "editor.defaultFormatter": "biomejs.biome",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "quickfix.biome": "explicit",
      "source.organizeImports.biome": "explicit"
    }
  },
  "[typescriptreact]": {
    "editor.defaultFormatter": "biomejs.biome",
    "editor.formatOnSave": true
  },
  "[json]": {
    "editor.defaultFormatter": "biomejs.biome",
    "editor.formatOnSave": true
  },
  "biome.lspBin": "./node_modules/@biomejs/biome/bin/biome"
}

3. Workspace Settings
{
  "editor.formatOnSave": true,
  "editor.formatOnPaste": true,
  "editor.defaultFormatter": "biomejs.biome",
  "biome.rename": true,
  "files.autoSave": "onFocusChange"
}

Migration from ESLint and Prettier
1. Remove Old Tools
# Remove ESLint and Prettier
npm uninstall eslint prettier eslint-config-prettier \
  eslint-plugin-react eslint-plugin-import \
  @typescript-eslint/parser @typescript-eslint/eslint-plugin

# Remove configuration files
rm .eslintrc.js .eslintrc.json .prettierrc .prettierignore

2. Migrate Configuration

Use Biome's migration tool:

# Migrate from Prettier config
biome migrate prettier --write

# Migrate from ESLint config
biome migrate eslint --write

3. Manual Migration

Prettier → Biome Formatter:

// .prettierrc (old)
{
  "semi": false,
  "singleQuote": true,
  "trailingComma": "all",
  "printWidth": 100
}

// biome.json (new)
{
  "formatter": {
    "lineWidth": 100
  },
  "javascript": {
    "formatter": {
      "semicolons": "asNeeded",
      "quoteStyle": "single",
      "trailingCommas": "all"
    }
  }
}


ESLint → Biome Linter:

// .eslintrc.json (old)
{
  "rules": {
    "no-unused-vars": "error",
    "prefer-const": "warn"
  }
}

// biome.json (new)
{
  "linter": {
    "rules": {
      "correctness": {
        "noUnusedVariables": "error"
      },
      "style": {
        "useConst": "warn"
      }
    }
  }
}

4. Update Scripts
{
  "scripts": {
    "lint": "biome lint .",
    "lint:fix": "biome lint --write .",
    "format": "biome format --write .",
    "check": "biome check --write ."
  }
}

Git Hooks Integration
Using Husky + lint-staged
# Install dependencies
npm install --save-dev husky lint-staged
npx husky init


.husky/pre-commit:

#!/usr/bin/env sh
. "$(dirname -- "$0")/_/husky.sh"

npx lint-staged


package.json:

{
  "lint-staged": {
    "*.{js,ts,jsx,tsx,json}": [
      "biome check --write --no-errors-on-unmatched"
    ]
  }
}

Using Lefthook

lefthook.yml:

pre-commit:
  commands:
    lint:
      glob: "*.{js,ts,jsx,tsx,json}"
      run: biome check --write --no-errors-on-unmatched {staged_files}

Simple Git Hook (no dependencies)

.git/hooks/pre-commit:

#!/bin/bash

# Get staged files
STAGED_FILES=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.(js|ts|jsx|tsx|json)$')

if [ -n "$STAGED_FILES" ]; then
  echo "Running Biome on staged files..."
  npx @biomejs/biome check --write --no-errors-on-unmatched $STAGED_FILES

  # Add formatted files back to staging
  git add $STAGED_FILES
fi

CI/CD Integration
GitHub Actions
name: Biome CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  biome:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run Biome CI
        run: npx @biomejs/biome ci .

      - name: Check formatting
        run: npx @biomejs/biome format .

      - name: Lint
        run: npx @biomejs/biome lint .

GitLab CI
biome:
  image: node:20-alpine
  stage: test
  script:
    - npm ci
    - npx @biomejs/biome ci .
  cache:
    paths:
      - node_modules/
  only:
    - merge_requests
    - main

CircleCI
version: 2.1

jobs:
  biome:
    docker:
      - image: cimg/node:20.11
    steps:
      - checkout
      - restore_cache:
          keys:
            - deps-{{ checksum "package-lock.json" }}
      - run: npm ci
      - save_cache:
          paths:
            - node_modules
          key: deps-{{ checksum "package-lock.json" }}
      - run: npx @biomejs/biome ci .

workflows:
  test:
    jobs:
      - biome

Import Sorting

Biome includes built-in import sorting:

# Organize imports
biome check --write --organize-imports-enabled=true .


Configuration:

{
  "organizeImports": {
    "enabled": true
  }
}


Example:

// Before
import { useState } from 'react';
import axios from 'axios';
import { Button } from './components/Button';
import type { User } from './types';
import './styles.css';

// After (sorted)
import type { User } from './types';

import axios from 'axios';
import { useState } from 'react';

import { Button } from './components/Button';

import './styles.css';

TypeScript Support

Biome has first-class TypeScript support:

{
  "linter": {
    "rules": {
      "suspicious": {
        "noExplicitAny": "warn",
        "noUnsafeDeclarationMerging": "error"
      },
      "correctness": {
        "noUnusedVariables": "error"
      },
      "style": {
        "useImportType": "error",
        "useExportType": "error"
      }
    }
  }
}


Type-aware linting:

// Biome detects unused variables
const unused = 123; // ❌ Error

// Enforces type imports
import { User } from './types'; // ❌ Error
import type { User } from './types'; // ✅ Correct

// Detects unsafe type assertions
const num = "123" as any as number; // ⚠️ Warning

Monorepo Support

Biome works great in monorepos:

Project Structure
my-monorepo/
├── biome.json (root config)
├── packages/
│   ├── web/
│   │   └── biome.json (extends root)
│   ├── api/
│   │   └── biome.json
│   └── shared/
│       └── biome.json

Root Configuration
{
  "$schema": "https://biomejs.dev/schemas/1.9.4/schema.json",
  "extends": [],
  "formatter": {
    "enabled": true,
    "indentStyle": "space",
    "indentWidth": 2
  },
  "linter": {
    "enabled": true,
    "rules": {
      "recommended": true
    }
  }
}

Package Override
{
  "extends": ["../../biome.json"],
  "formatter": {
    "lineWidth": 100
  },
  "linter": {
    "rules": {
      "style": {
        "noNonNullAssertion": "off"
      }
    }
  }
}

Monorepo Scripts
{
  "scripts": {
    "check": "biome check .",
    "check:packages": "biome check packages/*",
    "format": "biome format --write .",
    "lint": "biome lint packages/*"
  }
}

Performance Benefits
Speed Comparison
Tool	Time (10,000 files)
ESLint + Prettier	~60s
Biome	~0.6s

100x faster on average workloads.

Caching

Biome includes intelligent caching:

# First run (no cache)
biome check .  # 1.2s

# Second run (with cache)
biome check .  # 0.1s

# Clear cache
rm -rf node_modules/.cache/biome

Parallel Processing

Biome uses all CPU cores by default:

# Limit CPU cores
biome check --max-diagnostics=50 .

# Verbose output
biome check --verbose .

Common Patterns
React Projects
{
  "linter": {
    "rules": {
      "a11y": {
        "recommended": true,
        "useButtonType": "error",
        "useKeyWithClickEvents": "error"
      },
      "correctness": {
        "useExhaustiveDependencies": "warn",
        "useHookAtTopLevel": "error"
      },
      "suspicious": {
        "noArrayIndexKey": "error"
      }
    }
  },
  "javascript": {
    "formatter": {
      "jsxQuoteStyle": "double"
    }
  }
}

Next.js Projects
{
  "files": {
    "ignore": [".next", "out", "node_modules"]
  },
  "overrides": [
    {
      "include": ["app/**/*.tsx", "pages/**/*.tsx"],
      "linter": {
        "rules": {
          "a11y": {
            "recommended": true
          }
        }
      }
    }
  ]
}

Node.js Backend
{
  "linter": {
    "rules": {
      "security": {
        "recommended": true,
        "noGlobalEval": "error"
      },
      "correctness": {
        "noUnusedVariables": "error"
      }
    }
  },
  "javascript": {
    "formatter": {
      "semicolons": "always"
    }
  }
}

Best Practices
Use biome check instead of separate format/lint commands
Enable --write flag for automatic fixes
Configure VS Code for format-on-save
Add git hooks to enforce quality before commits
Use CI mode (biome ci) in continuous integration
Start with recommended rules then customize
Leverage import sorting to organize imports automatically
Use overrides for different file types or directories
Enable VCS integration to respect .gitignore
Keep configuration minimal - Biome has smart defaults
Troubleshooting
Biome Not Formatting
# Check if formatter is enabled
biome rage

# Verify file is not ignored
biome check --verbose src/file.ts

# Check VS Code extension logs
# View → Output → Biome

Conflicts with Prettier
# Disable Prettier in VS Code settings
"[javascript]": {
  "editor.defaultFormatter": "biomejs.biome"
}

# Remove Prettier dependencies
npm uninstall prettier

Performance Issues
# Check cache location
biome rage

# Clear cache
rm -rf node_modules/.cache/biome

# Reduce max diagnostics
biome check --max-diagnostics=20 .

Rule Configuration Not Working
// Ensure correct category
{
  "linter": {
    "rules": {
      "correctness": {  // Category name matters
        "noUnusedVariables": "error"
      }
    }
  }
}

Local Biome Configs (Your Repos)

Patterns from active projects:

ai-code-review/biome.json: files.includes targets src/**/*.ts and excludes tests, lineWidth: 100, single quotes, semicolons always, and noExplicitAny: warn.
itinerizer-ts/biome.json: files.ignore includes node_modules, dist, .claude, and data directories; organizeImports.enabled = true.
matsuoka-com and diogenes use similar formatting defaults (2-space indent, lineWidth 100).

Common scripts:

{
  "lint": "biome check src/ --diagnostic-level=error",
  "lint:fix": "biome check src/ --write",
  "format": "biome format src/ --write"
}

Resources
Official Docs: https://biomejs.dev
VS Code Extension: https://marketplace.visualstudio.com/items?itemName=biomejs.biome
GitHub: https://github.com/biomejs/biome
Rules Reference: https://biomejs.dev/linter/rules/
Migration Guide: https://biomejs.dev/guides/migrate-eslint-prettier/
Summary
Biome is a fast all-in-one linter and formatter
100x faster than ESLint + Prettier
Zero config by default with smart defaults
Built in Rust for maximum performance
TypeScript-first with excellent type support
Import sorting included out of the box
VS Code integration with official extension
Perfect for modern web projects, monorepos, CI/CD
Easy migration from ESLint and Prettier
Weekly Installs
534
Repository
bobmatnyc/claud…m-skills
GitHub Stars
40
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
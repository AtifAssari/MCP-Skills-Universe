---
rating: ⭐⭐⭐
title: library-bundler
url: https://skills.sh/deve1993/quickfy-website/library-bundler
---

# library-bundler

skills/deve1993/quickfy-website/library-bundler
library-bundler
Installation
$ npx skills add https://github.com/deve1993/quickfy-website --skill library-bundler
SKILL.md
Library Bundler

Expert skill for building, bundling, and publishing component libraries to NPM. Specializes in modern build tools (tsup 9, Vite 6), bundle optimization, multi-format exports, and package publishing workflows.

Technology Stack (2025)
Build Tools
tsup 9 - Fast TypeScript bundler with zero config
Vite 6 - Modern build tool with library mode
esbuild 0.24 - Extremely fast JavaScript bundler
Rollup 4 - When maximum control needed
Package Management
npm 11 / pnpm 9 - Package managers
changesets - Version management for monorepos
provenance - Supply chain security
Analysis
rollup-plugin-visualizer - Bundle analysis
source-map-explorer - Detailed source maps
Core Capabilities
1. Build Configuration
Zero-config TypeScript bundling
ESM-first with CJS fallback
Tree-shaking optimization
Source maps and declarations
Watch mode for development
2. Multi-Format Exports
ESM (ES Modules) - Modern standard
CJS (CommonJS) - Node.js compatibility
Dual package support
Subpath exports
3. Package Publishing
NPM registry publishing
Semantic versioning (semver)
Changelog generation
Git tagging
Package provenance
Configuration Examples
tsup 9 Config
// tsup.config.ts
import { defineConfig } from 'tsup'

export default defineConfig({
  entry: ['src/index.ts'],
  format: ['cjs', 'esm'],
  dts: true,
  splitting: true,
  sourcemap: true,
  clean: true,
  treeshake: true,
  minify: true,
  external: ['react', 'react-dom'],
  esbuildOptions(options) {
    options.banner = {
      js: '"use client"',
    }
  },
})

Multi-Entry tsup Config
// tsup.config.ts
import { defineConfig } from 'tsup'

export default defineConfig({
  entry: {
    index: 'src/index.ts',
    button: 'src/components/Button/index.ts',
    input: 'src/components/Input/index.ts',
    card: 'src/components/Card/index.ts',
  },
  format: ['esm', 'cjs'],
  dts: true,
  splitting: true,
  sourcemap: true,
  clean: true,
  treeshake: true,
  external: ['react', 'react-dom', 'motion/react'],
})

Vite 6 Library Mode
// vite.config.ts
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { resolve } from 'path'
import dts from 'vite-plugin-dts'

export default defineConfig({
  plugins: [
    react(),
    dts({
      insertTypesEntry: true,
      rollupTypes: true,
    }),
  ],
  build: {
    lib: {
      entry: resolve(__dirname, 'src/index.ts'),
      name: 'MyLibrary',
      formats: ['es', 'cjs'],
      fileName: (format) => `index.${format === 'es' ? 'js' : 'cjs'}`,
    },
    rollupOptions: {
      external: ['react', 'react-dom', 'react/jsx-runtime'],
      output: {
        globals: {
          react: 'React',
          'react-dom': 'ReactDOM',
        },
      },
    },
    sourcemap: true,
    minify: 'esbuild',
  },
})

Package.json Configuration
Modern Package.json (ESM-First)
{
  "name": "@myorg/ui-library",
  "version": "1.0.0",
  "description": "Modern React 19 component library",
  "type": "module",
  "main": "./dist/index.cjs",
  "module": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js",
      "require": "./dist/index.cjs"
    },
    "./button": {
      "types": "./dist/button.d.ts",
      "import": "./dist/button.js",
      "require": "./dist/button.cjs"
    },
    "./input": {
      "types": "./dist/input.d.ts",
      "import": "./dist/input.js",
      "require": "./dist/input.cjs"
    },
    "./styles.css": "./dist/styles.css",
    "./package.json": "./package.json"
  },
  "files": [
    "dist",
    "README.md",
    "LICENSE"
  ],
  "sideEffects": [
    "*.css"
  ],
  "scripts": {
    "build": "tsup",
    "dev": "tsup --watch",
    "lint": "eslint src/",
    "type-check": "tsc --noEmit",
    "test": "vitest",
    "prepublishOnly": "npm run build && npm test",
    "publish:dry": "npm publish --dry-run"
  },
  "peerDependencies": {
    "react": "^19.0.0",
    "react-dom": "^19.0.0"
  },
  "devDependencies": {
    "@types/react": "^19.0.0",
    "react": "^19.2.0",
    "tsup": "^9.0.0",
    "typescript": "^5.9.0",
    "vitest": "^4.0.0"
  },
  "publishConfig": {
    "access": "public",
    "provenance": true
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/myorg/ui-library"
  },
  "keywords": [
    "react",
    "react19",
    "components",
    "ui",
    "library",
    "typescript"
  ],
  "author": "Your Name",
  "license": "MIT"
}

TypeScript Config
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "lib": ["ES2022", "DOM", "DOM.Iterable"],
    "jsx": "react-jsx",
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "noUncheckedIndexedAccess": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true
  },
  "include": ["src"],
  "exclude": ["node_modules", "dist", "**/*.test.ts", "**/*.test.tsx"]
}

Optimization Strategies
1. Tree-Shaking
// package.json
{
  "sideEffects": false
}

// Or specify files with side effects
{
  "sideEffects": ["*.css", "*.scss"]
}

// Use named exports (tree-shakeable)
export { Button } from './Button'
export { Input } from './Input'

// Avoid default exports for libraries

2. Bundle Analysis
// vite.config.ts
import { visualizer } from 'rollup-plugin-visualizer'

export default defineConfig({
  plugins: [
    visualizer({
      filename: './dist/stats.html',
      open: true,
      gzipSize: true,
      brotliSize: true,
    }),
  ],
})

3. External Dependencies
// Don't bundle peer dependencies
external: [
  'react',
  'react-dom',
  'react/jsx-runtime',
  'motion/react',
  /^@radix-ui\/.*/,
]

Publishing Workflow
1. Semantic Versioning
# Patch: Bug fixes (1.0.0 → 1.0.1)
npm version patch

# Minor: New features (1.0.0 → 1.1.0)
npm version minor

# Major: Breaking changes (1.0.0 → 2.0.0)
npm version major

# Pre-release
npm version prerelease --preid=beta

2. Pre-publish Checks
{
  "scripts": {
    "prepublishOnly": "npm run lint && npm run type-check && npm test && npm run build"
  }
}

3. Publishing with Provenance
# Dry run first
npm publish --dry-run

# Publish with provenance (requires GitHub Actions)
npm publish --provenance --access public

4. GitHub Actions Workflow
# .github/workflows/publish.yml
name: Publish Package

on:
  push:
    tags:
      - 'v*'

jobs:
  publish:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      id-token: write
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '22'
          registry-url: 'https://registry.npmjs.org'
      - run: npm ci
      - run: npm test
      - run: npm run build
      - run: npm publish --provenance --access public
        env:
          NODE_AUTH_TOKEN: ${{ secrets.NPM_TOKEN }}

Monorepo Setup
Turborepo Configuration
// turbo.json
{
  "$schema": "https://turbo.build/schema.json",
  "tasks": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**"]
    },
    "dev": {
      "cache": false,
      "persistent": true
    },
    "test": {
      "dependsOn": ["build"]
    }
  }
}

Changesets for Versioning
# Initialize changesets
npx changeset init

# Add a changeset
npx changeset add

# Version packages
npx changeset version

# Publish
npx changeset publish

Testing Build Output
Local Testing
# Create tarball
npm pack

# Install in test project
cd ../test-project
npm install ../my-library/my-library-1.0.0.tgz

Verify Exports
// test.mjs (ESM)
import * as lib from 'my-library'
console.log(Object.keys(lib))

// test.cjs (CommonJS)
const lib = require('my-library')
console.log(Object.keys(lib))

Best Practices
Package Design
ESM-First: Modern standard, better tree-shaking
Dual Package: Provide both ESM and CJS
Explicit Exports: Use exports field
Tree-Shakeable: Mark sideEffects
Small Bundles: Externalize dependencies
Build Configuration
Source Maps: Always generate for debugging
Type Declarations: Essential for TypeScript users
Declaration Maps: Enable IDE navigation
Minification: For production builds
Clean Output: Clear dist/ before building
Publishing
Semantic Versioning: Follow strictly
Changelog: Document all changes
Git Tags: Tag releases
Pre-publish Tests: Run comprehensive checks
Provenance: Use for supply chain security
When to Use This Skill

Activate when you need to:

Set up build configuration
Optimize bundle size
Configure multi-format exports
Prepare package for NPM
Set up TypeScript declarations
Configure tree-shaking
Create build scripts
Set up CI/CD for publishing
Configure monorepo builds
Output Format

Provide:

Complete Configuration: Build tool config files
package.json Setup: Proper entry points and scripts
Build Instructions: How to build and test
Publishing Guide: Step-by-step process
Optimization Report: Bundle sizes and improvements
Weekly Installs
13
Repository
deve1993/quickfy-website
GitHub Stars
3
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
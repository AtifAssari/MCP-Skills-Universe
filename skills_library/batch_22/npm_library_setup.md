---
title: npm-library-setup
url: https://skills.sh/huozhi/npm-skills/npm-library-setup
---

# npm-library-setup

skills/huozhi/npm-skills/npm-library-setup
npm-library-setup
Installation
$ npx skills add https://github.com/huozhi/npm-skills --skill npm-library-setup
SKILL.md
npm Library Setup with ESM

This skill provides comprehensive guidance on setting up an npm library with package.json, with a preference for ES Modules (ESM).

Overview

This skill helps you create npm packages that:

Use ES Modules (ESM) with "type": "module"
Configure modern exports field (no deprecated module field)
Use bunchee for zero-config bundling
Use vitest for modern testing
Support TypeScript and React component libraries
When to Use This Skill

Use when:

"Set up an npm package"
"Create a new npm library"
"Configure package.json for ESM"
"Set up a TypeScript npm package"
"Create a React component library"

Categories covered:

Basic package setup with ESM
TypeScript package configuration
React component library setup
Build configuration with bunchee
Testing setup with vitest
Quick Start

Initialize your package:

npm init -y


Configure for ESM by adding "type": "module" to package.json

Install build and test tools:

npm install -D bunchee vitest


Create your source files in src/ and run npm run build

Essential Configuration
package.json
{
  "type": "module",
  "main": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "default": "./dist/index.js"
    }
  },
  "scripts": {
    "build": "bunchee",
    "test": "vitest",
    "test:run": "vitest run"
  },
  "engines": {
    "node": ">=20"
  }
}


Note: Use the oldest currently-maintained LTS version (check Node.js Release Schedule).

Key Principles
ESM-first: Use "type": "module" for pure ESM packages
Modern exports: Use exports field instead of deprecated module field
Zero-config bundling: Bunchee handles most configuration automatically
File extensions: Use explicit .js extensions in imports (even in TypeScript)
Kebab-case files: Use kebab-case for file paths
TypeScript Setup

Install TypeScript and configure:

npm install -D typescript @types/node


Create tsconfig.json:

{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "NodeNext",
    "declaration": true,
    "strict": true
  }
}


Bunchee automatically compiles TypeScript and generates .d.ts files.

React Component Libraries

Install React as dev dependency:

npm install -D react @types/react


Configure peerDependencies:

{
  "peerDependencies": {
    "react": "*"
  }
}

Best Practices
✅ Use exports field (no deprecated module field)
✅ Use explicit file extensions in imports (.js)
✅ Use kebab-case for file paths
✅ Separate runtime dependencies from dev dependencies
✅ Specify Node.js version using oldest maintained LTS
✅ Write source in ESM syntax
Common Patterns
ESM Import/Export
// Named exports
export function greet(name) {
  return "Hello, " + name + "!";
}

// Default export
export default class MyLibrary {}

// Import
import { greet } from './module.js';
import MyLibrary from './MyLibrary.js';


Important: Always use .js extension in imports, even in TypeScript files.

File Structure
my-package/
├── package.json
├── src/
│   ├── index.js         # or index.ts
│   └── helpers.js
├── dist/                # Build output
└── README.md

References

See references/ directory for detailed guides:

Getting Started
Package.json Configuration
ESM Syntax and Patterns
Building and Testing
TypeScript Packages
React Packages
Best Practices
Examples

See examples/ directory for complete working examples:

JavaScript ESM package
TypeScript ESM package
Additional Resources
Node.js Release Schedule - Check oldest maintained LTS
Bunchee Documentation - Build tool
Vitest Documentation - Test runner
Weekly Installs
58
Repository
huozhi/npm-skills
GitHub Stars
3
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
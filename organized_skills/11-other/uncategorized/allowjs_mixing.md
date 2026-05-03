---
title: allowjs-mixing
url: https://skills.sh/marius-townhouse/effective-typescript-skills/allowjs-mixing
---

# allowjs-mixing

skills/marius-townhouse/effective-typescript-skills/allowjs-mixing
allowjs-mixing
Installation
$ npx skills add https://github.com/marius-townhouse/effective-typescript-skills --skill allowjs-mixing
SKILL.md
Use allowJs to Mix TypeScript and JavaScript
Overview

Migrating a large JavaScript codebase to TypeScript doesn't have to be all-or-nothing. The allowJs compiler option lets you gradually adopt TypeScript by mixing .ts and .js files in the same project. This enables incremental migration, allowing teams to convert files one at a time while maintaining a working codebase.

This approach is essential for large migrations where a big-bang rewrite isn't feasible.

When to Use This Skill
Migrating JavaScript projects to TypeScript
Gradually adopting TypeScript in a JS codebase
Working with mixed TypeScript/JavaScript teams
Converting large existing projects
Teams still learning TypeScript
The Iron Rule

Use allowJs to enable incremental migration. Convert files module by module, starting from leaf modules and working up the dependency graph.

Detection

Watch for migration challenges:

// Can't migrate because:
- 1000+ JavaScript files
- Team still learning TypeScript
- Can't stop feature development
- Risk of breaking changes

Enabling allowJs
// tsconfig.json
{
  "compilerOptions": {
    "allowJs": true,        // Allow JavaScript files
    "checkJs": false,       // Don't type check JS (optional)
    "outDir": "./dist",
    "strict": true
  },
  "include": ["src/**/*"]
}

Migration Strategy
Phase 1: Enable allowJs
  - Add tsconfig.json with allowJs: true
  - Rename one file to .ts as proof of concept
  - Ensure build still works

Phase 2: Convert leaf modules
  - Start with files that have no dependencies
  - Utilities, helpers, constants
  - Low risk, easy wins

Phase 3: Work up dependency graph
  - Convert files that only depend on converted files
  - Gradually move toward entry points

Phase 4: Convert entry points last
  - Main files, app entry points
  - Most complex, most dependencies

Converting a File
// utils.js (before)
export function formatDate(date) {
  return date.toISOString().split('T')[0];
}

export const PI = 3.14159;

// utils.ts (after)
export function formatDate(date: Date): string {
  return date.toISOString().split('T')[0];
}

export const PI = 3.14159;

Importing Between JS and TS
// app.ts - TypeScript importing JavaScript
import { formatDate } from './utils.js';  // .js extension
// TypeScript trusts the JS (with checkJs: false)

// With types for JS module
declare module './utils.js' {
  export function formatDate(date: Date): string;
  export const PI: number;
}

// legacy.js - JavaScript importing TypeScript
import { User } from './types.ts';  // Works with allowJs
// JS doesn't get type checking, but can import TS

Adding Types to JavaScript
// @ts-check - Enable type checking for this file

/**
 * @param {string} name
 * @param {number} age
 * @returns {string}
 */
function greet(name, age) {
  return `Hello ${name}, you are ${age}`;
}

/** @type {string[]} */
const names = ['Alice', 'Bob'];

/** @typedef {{ x: number, y: number }} Point */

Migration Checklist
// 1. Set up tsconfig.json with allowJs
{
  "compilerOptions": {
    "allowJs": true,
    "checkJs": false,  // Enable later for stricter checking
    "outDir": "./dist",
    "strict": true,
    "esModuleInterop": true
  }
}

// 2. Start with simple files
// - No dependencies
// - Pure functions
// - Well-tested

// 3. Add types gradually
// - Start with any if needed
// - Refine over time

// 4. Enable strict mode checks incrementally
// - noImplicitAny
// - strictNullChecks
// - strictFunctionTypes

Pressure Resistance Protocol

When migrating:

Enable allowJs first: Get the infrastructure working
Start small: Convert one file, ensure build works
Prioritize leaf modules: Fewer dependencies = easier
Use any initially: Can refine types later
Track progress: Celebrate small wins
Red Flags
Anti-Pattern	Problem	Solution
Big-bang rewrite	Too risky, takes too long	Incremental with allowJs
Converting entry points first	Too many dependencies	Start with leaves
No tsconfig.json	Can't control compilation	Set up properly
Abandoning midway	Wasted effort	Track and celebrate progress
Common Rationalizations
"We need to convert everything at once"

Reality: Incremental migration with allowJs is safer and more practical for large codebases.

"Mixed JS/TS is confusing"

Reality: It's temporary and manageable. Clear migration plan keeps it organized.

"We'll just keep using JS"

Reality: TypeScript's benefits compound over time. Start small and grow.

Quick Reference
Step	Action	Timeline
1	Add tsconfig with allowJs	Day 1
2	Convert 1-2 utility files	Week 1
3	Convert leaf modules	Weeks 2-4
4	Work up dependency graph	Months 1-3
5	Convert entry points	Months 3-6
6	Remove allowJs (optional)	When done
The Bottom Line

Use allowJs for incremental TypeScript adoption. Convert files gradually, starting from leaf modules. This makes large migrations manageable without stopping development.

Reference
Effective TypeScript, 2nd Edition by Dan Vanderkam
Item 81: Use allowJs to Mix TypeScript and JavaScript
Weekly Installs
11
Repository
marius-townhous…t-skills
GitHub Stars
2
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
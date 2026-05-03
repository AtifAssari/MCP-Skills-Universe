---
title: typescript-best-practices
url: https://skills.sh/flpbalada/my-opencode-config/typescript-best-practices
---

# typescript-best-practices

skills/flpbalada/my-opencode-config/typescript-best-practices
typescript-best-practices
Installation
$ npx skills add https://github.com/flpbalada/my-opencode-config --skill typescript-best-practices
SKILL.md
TypeScript Best Practices

Comprehensive guide to writing clean, type-safe, and maintainable TypeScript code.

When to Use
Configuring a new TypeScript project
Deciding between interface vs type alias
Writing async/await code
Reviewing TypeScript code quality
Avoiding common TypeScript pitfalls
Quick Reference
// Type inference - let TS do the work
const name = 'Alice';

// Explicit for APIs
function greet(name: string): string { ... }

// Unknown over any
function safe(data: unknown) { ... }

// Type-only imports
import type { User } from './types';

// Const assertions
const tuple = [1, 2] as const;

// Null safety
const len = str?.length ?? 0;

// Guard clauses
if (!valid) throw new Error();
// main logic...

Common Mistakes
Mistake	Problem	Solution
Overusing any	Defeats type checking	Use unknown, generics, or proper types
Not using strict mode	Misses many errors	Enable "strict": true
Redundant annotations	Clutters code	Trust type inference
Ignoring union types	Runtime errors	Use type guards
Not handling null	Crashes	Use ?. and ?? operators
Nested conditionals	Hard to read	Use guard clauses
Duplicate types with Zod	Maintenance burden	Infer from z.infer<typeof schema>
Sequential awaits for independent ops	Slower execution	Use Promise.all
Non-Error cause	Breaks error chains	Always use Error instance for cause
Progressive Disclosure
Topic	File	When to Use
Type system & functions	context/code-patterns.md	Interface vs type, async patterns, guard clauses
Project structure	context/organization.md	File naming, barrel files, configuration
Testing & performance	context/testing-performance.md	DI, type guards, null handling, performance
Key Principles
Type inference when obvious - Let TypeScript infer simple types
Explicit for public APIs - Document function signatures clearly
Unknown over any - Use unknown with type guards instead of any
Guard clauses - Early returns reduce nesting
Type-only imports - Better tree-shaking with import type
References
W3Schools TypeScript Best Practices
TypeScript Handbook
TypeScript Performance Wiki
Weekly Installs
23
Repository
flpbalada/my-op…e-config
GitHub Stars
239
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
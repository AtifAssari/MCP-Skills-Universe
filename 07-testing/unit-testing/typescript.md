---
title: typescript
url: https://skills.sh/knoopx/pi/typescript
---

# typescript

skills/knoopx/pi/typescript
typescript
Installation
$ npx skills add https://github.com/knoopx/pi --skill typescript
SKILL.md
TypeScript

Type-safe JavaScript development with bun and vitest in this project.

Quick Start
bun init --typescript    # Initialize project
bunx tsc --noEmit        # Type check
vitest run               # Run tests

Project Configuration

This project uses bun with ESNext targets. Reference config in templates/tsconfig.json:

{
  "compilerOptions": {
    "target": "ESNext",
    "module": "ESNext",
    "lib": ["ESNext"],
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "esModuleInterop": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "baseUrl": ".",
    "paths": { "@/*": ["src/*"] }
  },
  "include": ["src"],
  "exclude": ["node_modules"]
}

Decision Guide: Interfaces vs Types

Use this when choosing between interface and type:

Interface when: defining object shapes that may be extended, or when declaration merging is needed (e.g., augmenting third-party types)
Type when: defining unions, intersections, mapped types, conditional types, or function signatures
// Interface — extendable object shape
interface User {
  id: number;
  name: string;
  email: string;
}

// Type — unions and computed types
type Status = "loading" | "success" | "error";
type CreateUser = (data: Partial<User>) => Promise<User>;

// Discriminated union — use type, not interface
type Result<T> = { ok: true; value: T } | { ok: false; error: Error };

Type Safety Patterns
Branded Types for Domain Primitives

Use branded types when a plain string or number could be confused across domains:

type UserId = string & { readonly __brand: "UserId" };
type OrderId = string & { readonly __brand: "OrderId" };

function createUserId(id: string): UserId {
  // validate format here
  return id as UserId;
}

// Compiler prevents: getUser(orderId) — type mismatch
function getUser(id: UserId): Promise<User> {
  /* ... */
}

Making Invalid States Unrepresentable

Model states as discriminated unions so illegal combinations are compile errors:

type AsyncState<T> =
  | { status: "idle" }
  | { status: "loading" }
  | { status: "success"; data: T }
  | { status: "error"; error: Error };

// Impossible to have data without status: "success"
function render(state: AsyncState<User[]>) {
  switch (state.status) {
    case "success":
      return renderTable(state.data);
    case "error":
      return renderError(state.error);
    // exhaustiveness: TS errors if a case is missing
  }
}

Type Guards with Runtime Validation
function isUser(value: unknown): value is User {
  return (
    typeof value === "object" &&
    value !== null &&
    "id" in value &&
    "name" in value
  );
}

Result Type for Error Handling

Prefer Result<T> over try/catch for composable error handling:

type Result<T, E = Error> = { ok: true; value: T } | { ok: false; error: E };

function safeParse(json: string): Result<unknown> {
  try {
    return { ok: true, value: JSON.parse(json) };
  } catch (error) {
    return { ok: false, error: error as Error };
  }
}

Workflow
Set up project: bun init --typescript, copy templates/tsconfig.json
Write types first: Define interfaces/types at module boundaries before implementation
Type check: bunx tsc --noEmit — fix errors before proceeding
Watch mode: tmux new -d -s tsc 'tsc --watch' for continuous feedback
Test: vitest run to validate behavior matches types
Gradual adoption: Use allowJs: true + checkJs: true when migrating JS files incrementally
Constraints
Always use strict: true — never weaken strictness per-file with // @ts-ignore; use // @ts-expect-error with a comment explaining why
Avoid any — use unknown and narrow with type guards
Type at boundaries (API inputs/outputs, function signatures) — let inference handle internals
Path aliases: use @/* mapped to src/* for imports
Weekly Installs
31
Repository
knoopx/pi
GitHub Stars
45
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
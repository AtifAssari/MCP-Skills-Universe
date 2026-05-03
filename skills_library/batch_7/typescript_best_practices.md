---
title: typescript-best-practices
url: https://skills.sh/0xbigboss/claude-code/typescript-best-practices
---

# typescript-best-practices

skills/0xbigboss/claude-code/typescript-best-practices
typescript-best-practices
Installation
$ npx skills add https://github.com/0xbigboss/claude-code --skill typescript-best-practices
Summary

TypeScript patterns for type-first development, making illegal states unrepresentable, and exhaustive handling.

Use discriminated unions, branded types, and const assertions to encode business rules in the type system and prevent invalid states at compile time
Validate at system boundaries with Zod schemas as single source of truth; infer TypeScript types automatically to keep types and validation in sync
Enforce exhaustive handling with never checks in switch statements and default cases; unhandled code paths become compile errors
Wrap external calls and async operations with contextual error messages; propagate failures rather than silently catching them
Load and validate configuration at startup with Zod; access typed config object throughout the codebase instead of process.env directly
SKILL.md
TypeScript Best Practices

Follows type-first, functional, and error handling patterns from CLAUDE.md. This skill covers language-specific idioms only.

Pair with React Best Practices

When working with React components (.tsx, .jsx files or @react imports), always load react-best-practices alongside this skill. This skill covers TypeScript fundamentals; React-specific patterns (effects, hooks, refs, component design) are in the dedicated React skill.

Make Illegal States Unrepresentable

Use the type system to prevent invalid states at compile time.

Discriminated unions for mutually exclusive states:

// Good: only valid combinations possible
type RequestState<T> =
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'success'; data: T }
  | { status: 'error'; error: Error };

// Bad: allows invalid combinations like { loading: true, error: Error }
type RequestState<T> = {
  loading: boolean;
  data?: T;
  error?: Error;
};


Branded types for domain primitives:

type UserId = string & { readonly __brand: 'UserId' };
type OrderId = string & { readonly __brand: 'OrderId' };

// Compiler prevents passing OrderId where UserId expected
function getUser(id: UserId): Promise<User> { /* ... */ }


Const assertions for literal unions:

const ROLES = ['admin', 'user', 'guest'] as const;
type Role = typeof ROLES[number]; // 'admin' | 'user' | 'guest'

// Array and type stay in sync automatically
function isValidRole(role: string): role is Role {
  return ROLES.includes(role as Role);
}


Exhaustive switch with never check:

type Status = "active" | "inactive";

function processStatus(status: Status): string {
  switch (status) {
    case "active":
      return "processing";
    case "inactive":
      return "skipped";
    default: {
      const _exhaustive: never = status;
      throw new Error(`unhandled status: ${_exhaustive}`);
    }
  }
}

Runtime Validation with Zod
Define schemas as single source of truth; infer TypeScript types with z.infer<>. Avoid duplicating types and schemas.
Use safeParse for user input where failure is expected; use parse at trust boundaries where invalid data is a bug.
Compose schemas with .extend(), .pick(), .omit(), .merge() for DRY definitions.
Add .transform() for data normalization at parse time (trim strings, parse dates).
import { z } from "zod";

const UserSchema = z.object({
  id: z.string().uuid(),
  email: z.string().email(),
  name: z.string().min(1),
  createdAt: z.string().transform((s) => new Date(s)),
});

type User = z.infer<typeof UserSchema>;

// Strict parsing at trust boundaries — throws if API contract violated
export async function fetchUser(id: string): Promise<User> {
  const response = await fetch(`/api/users/${id}`);
  if (!response.ok) {
    throw new Error(`fetch user ${id} failed: ${response.status}`);
  }
  return UserSchema.parse(await response.json());
}

// Caller handles both success and error from user input
const result = UserSchema.safeParse(formData);
if (!result.success) {
  setErrors(result.error.flatten().fieldErrors);
  return;
}

Optional: type-fest

For advanced type utilities beyond TypeScript builtins, consider type-fest:

Opaque<T, Token> - cleaner branded types than manual & { __brand } pattern
PartialDeep<T> - recursive partial for nested objects
ReadonlyDeep<T> - recursive readonly for immutable data
SetRequired<T, K> / SetOptional<T, K> - targeted field modifications
Simplify<T> - flatten complex intersection types in IDE tooltips
import type { Opaque, PartialDeep } from 'type-fest';

type UserId = Opaque<string, 'UserId'>;
type UserPatch = PartialDeep<User>;

Weekly Installs
1.9K
Repository
0xbigboss/claude-code
GitHub Stars
43
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
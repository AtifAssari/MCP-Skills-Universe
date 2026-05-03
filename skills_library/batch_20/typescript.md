---
title: typescript
url: https://skills.sh/gentleman-programming/gentleman-skills/typescript
---

# typescript

skills/gentleman-programming/gentleman-skills/typescript
typescript
Installation
$ npx skills add https://github.com/gentleman-programming/gentleman-skills --skill typescript
SKILL.md
Const Types Pattern (REQUIRED)
// ✅ ALWAYS: Create const object first, then extract type
const STATUS = {
  ACTIVE: "active",
  INACTIVE: "inactive",
  PENDING: "pending",
} as const;

type Status = (typeof STATUS)[keyof typeof STATUS];

// ❌ NEVER: Direct union types
type Status = "active" | "inactive" | "pending";


Why? Single source of truth, runtime values, autocomplete, easier refactoring.

Flat Interfaces (REQUIRED)
// ✅ ALWAYS: One level depth, nested objects → dedicated interface
interface UserAddress {
  street: string;
  city: string;
}

interface User {
  id: string;
  name: string;
  address: UserAddress;  // Reference, not inline
}

interface Admin extends User {
  permissions: string[];
}

// ❌ NEVER: Inline nested objects
interface User {
  address: { street: string; city: string };  // NO!
}

Never Use any
// ✅ Use unknown for truly unknown types
function parse(input: unknown): User {
  if (isUser(input)) return input;
  throw new Error("Invalid input");
}

// ✅ Use generics for flexible types
function first<T>(arr: T[]): T | undefined {
  return arr[0];
}

// ❌ NEVER
function parse(input: any): any { }

Utility Types
Pick<User, "id" | "name">     // Select fields
Omit<User, "id">              // Exclude fields
Partial<User>                 // All optional
Required<User>                // All required
Readonly<User>                // All readonly
Record<string, User>          // Object type
Extract<Union, "a" | "b">     // Extract from union
Exclude<Union, "a">           // Exclude from union
NonNullable<T | null>         // Remove null/undefined
ReturnType<typeof fn>         // Function return type
Parameters<typeof fn>         // Function params tuple

Type Guards
function isUser(value: unknown): value is User {
  return (
    typeof value === "object" &&
    value !== null &&
    "id" in value &&
    "name" in value
  );
}

Import Types
import type { User } from "./types";
import { createUser, type Config } from "./utils";

Keywords

typescript, ts, types, interfaces, generics, strict mode, utility types

Weekly Installs
245
Repository
gentleman-progr…n-skills
GitHub Stars
491
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
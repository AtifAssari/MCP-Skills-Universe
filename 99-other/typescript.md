---
title: typescript
url: https://skills.sh/nguyenhuuca/assessment/typescript
---

# typescript

skills/nguyenhuuca/assessment/typescript
typescript
Installation
$ npx skills add https://github.com/nguyenhuuca/assessment --skill typescript
SKILL.md
TypeScript Development
Project Setup
# Initialize with pnpm
pnpm init
pnpm add -D typescript @types/node

# TypeScript config
npx tsc --init

tsconfig.json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitReturns": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "outDir": "./dist"
  },
  "include": ["src/**/*"]
}

Type Patterns
Discriminated Unions
type Result<T> =
  | { success: true; data: T }
  | { success: false; error: Error };

function handleResult(result: Result<User>) {
  if (result.success) {
    console.log(result.data); // User
  } else {
    console.error(result.error); // Error
  }
}

Branded Types
type UserId = string & { readonly brand: unique symbol };
type OrderId = string & { readonly brand: unique symbol };

function createUserId(id: string): UserId {
  return id as UserId;
}

Utility Types
// Make all properties optional
Partial<User>

// Make all properties required
Required<User>

// Pick specific properties
Pick<User, 'id' | 'email'>

// Omit specific properties
Omit<User, 'password'>

// Make properties readonly
Readonly<User>

Error Handling
// Result type pattern
type Result<T, E = Error> =
  | { ok: true; value: T }
  | { ok: false; error: E };

async function fetchUser(id: string): Promise<Result<User>> {
  try {
    const user = await db.users.findById(id);
    if (!user) {
      return { ok: false, error: new Error('User not found') };
    }
    return { ok: true, value: user };
  } catch (error) {
    return { ok: false, error: error as Error };
  }
}

Testing with Vitest
import { describe, test, expect, vi } from 'vitest';

describe('UserService', () => {
  test('creates user with valid email', async () => {
    const service = new UserService(mockRepo);
    const user = await service.create('test@example.com');
    expect(user.email).toBe('test@example.com');
  });

  test('throws on invalid email', async () => {
    const service = new UserService(mockRepo);
    await expect(service.create('invalid')).rejects.toThrow();
  });
});

Tooling
# Biome (linting + formatting)
pnpm add -D @biomejs/biome
pnpm biome check --apply .

# Vitest (testing)
pnpm add -D vitest
pnpm vitest

Weekly Installs
10
Repository
nguyenhuuca/assessment
GitHub Stars
24
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
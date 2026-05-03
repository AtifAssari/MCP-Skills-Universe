---
title: typescript-excellence
url: https://skills.sh/phrazzld/claude-config/typescript-excellence
---

# typescript-excellence

skills/phrazzld/claude-config/typescript-excellence
typescript-excellence
Installation
$ npx skills add https://github.com/phrazzld/claude-config --skill typescript-excellence
SKILL.md
TypeScript Excellence

Type-safe, maintainable TypeScript with modern toolchain.

Type Safety

Never use any. Alternatives:

// Unknown for external data
function parse(input: unknown): User { ... }

// Union for specific options
type Status = 'loading' | 'success' | 'error';

// Generics for reusable code
function first<T>(arr: T[]): T | undefined { ... }

// Type assertion as last resort (with runtime check)
if (isUser(data)) { return data as User; }


tsconfig.json essentials:

{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true
  }
}

Module Organization

Feature-based, not layer-based:

src/
  features/
    auth/
      components/
      hooks/
      api.ts
      types.ts
      index.ts  # Barrel: controlled exports
    orders/
      ...
  shared/
    ui/
    utils/


Use path aliases: @features/*, @shared/* (avoid ../../../../).

State Management

Server state: TanStack Query exclusively.

const { data, isLoading, error } = useQuery({
  queryKey: ['user', userId],
  queryFn: () => fetchUser(userId),
});


Client state: Discriminated unions.

type AuthState =
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'authenticated'; user: User }
  | { status: 'error'; error: AppError };

Async Patterns

Always wrap, always context:

async function fetchUser(id: string): Promise<User> {
  try {
    const res = await fetch(`/api/users/${id}`);
    if (!res.ok) throw new ApiError(res.status, await res.text());
    return res.json();
  } catch (error) {
    throw new AppError('Failed to fetch user', { cause: error });
  }
}


Cancellation: Use AbortController for long operations. Always clean up timeouts in finally blocks.

Toolchain
Tool	Purpose
pnpm	Package manager (declare in packageManager field)
Vitest	Testing (unit/integration/e2e)
tsup	Builds (ESM + CJS + .d.ts)
ESLint	Linting (@typescript-eslint/no-explicit-any: error)
Prettier	Formatting
Anti-Patterns
Type gymnastics (conditional types, template literals without justification)
useState + useEffect for server data (use TanStack Query)
Technical-layer folders (/controllers, /services, /models)
eslint-disable without documented justification
Mocking internal components (mock boundaries only)
Mixed package managers or test frameworks
References
toolchain-setup.md - pnpm, Vitest, tsup, ESLint config
type-patterns.md - Utility types, generics, guards
testing-strategy.md - Test pyramid, behavior focus
async-patterns.md - Timeout cleanup, error-specific catch, cancellation
Weekly Installs
24
Repository
phrazzld/claude-config
GitHub Stars
8
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
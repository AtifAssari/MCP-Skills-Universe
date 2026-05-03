---
rating: ⭐⭐
title: typescript conventions
url: https://skills.sh/exceptionless/exceptionless/typescript-conventions
---

# typescript conventions

skills/exceptionless/exceptionless/typescript-conventions
typescript-conventions
Installation
$ npx skills add https://github.com/exceptionless/exceptionless --skill typescript-conventions
SKILL.md
TypeScript Conventions
Style & Formatting
Follow .editorconfig and ESLint + Prettier config strictly
Run npm run format before committing
Minimize diffs: Change only what's necessary, preserve existing formatting and structure
Match surrounding code style exactly
File Naming
Use kebab-case for files and directories
Component files: user-profile.svelte
TypeScript files: api-client.ts, user-service.ts
Test files: user-service.test.ts or user-service.spec.ts
Imports
Prefer Named Imports
// ✅ Good: Named imports
import { UserService, type User } from "$lib/services/user-service";
import { formatDate, formatNumber } from "$lib/utils/formatters";

// ❌ Avoid: Namespace imports (except allowed exceptions)
import * as utils from "$lib/utils";

Allowed Namespace Imports
// ✅ Allowed: shadcn-svelte components
import * as Dialog from "$comp/ui/dialog";
import * as DropdownMenu from "$comp/ui/dropdown-menu";

// ✅ Allowed: Barrel exports
import * as Field from "$comp/ui/field";

Type Safety
Avoid any
// ❌ Bad
function processData(data: any) { ... }

// ✅ Good: Use interfaces/types
interface UserData {
    id: string;
    name: string;
    email: string;
}

function processData(data: UserData) { ... }

// ✅ Good: Use unknown for truly unknown data
function parseResponse(data: unknown): UserData {
    if (isUserData(data)) {
        return data;
    }
    throw new Error('Invalid data format');
}

Type Guards
function isUserData(data: unknown): data is UserData {
    return (
        typeof data === "object" &&
        data !== null &&
        "id" in data &&
        "name" in data &&
        "email" in data
    );
}

// Discriminated unions
type ApiResponse =
    | { status: "success"; data: UserData }
    | { status: "error"; error: string };

function handleResponse(response: ApiResponse) {
    if (response.status === "success") {
        // TypeScript knows response.data exists
        return response.data;
    }
    // TypeScript knows response.error exists
    throw new Error(response.error);
}

Promise Handling
Always Await
// ✅ Good: Always await
const user = await fetchUser(id);
const [users, projects] = await Promise.all([fetchUsers(), fetchProjects()]);

// ❌ Bad: Fire and forget without handling
fetchUser(id); // Exception is lost!

Error Handling
// ✅ Good: try/catch with proper typing
async function loadUser(id: string): Promise<User | null> {
    try {
        const response = await api.get<User>(`/users/${id}`);
        return response.data;
    } catch (error) {
        if (error instanceof ApiError) {
            console.error("API Error:", error.message);
        }
        return null;
    }
}

Control Statements

All single-line control statements need braces:

// ✅ Good: Always use braces
if (condition) {
    doSomething();
}

for (const item of items) {
    process(item);
}

// ❌ Bad: No braces
if (condition) doSomething();

Interface Naming

Follow HTTP verb prefixes for API-related types:

// Request/Response interfaces
interface PostOrganizationRequest {
    name: string;
    billing_email: string;
}

interface GetOrganizationParams {
    id: string;
}

interface PatchUserRequest {
    name?: string;
    email?: string;
}

Export Patterns
// Named exports preferred
export function createUser(data: CreateUserRequest): Promise<User> { ... }
export type { User, CreateUserRequest };

// Re-export from barrel files
// src/lib/features/users/index.ts
export { createUser, updateUser, deleteUser } from './api.svelte';
export type { User, CreateUserRequest } from './models';

Modern ES6+ Features
// Template literals
const message = `Hello, ${user.name}!`;

// Destructuring
const { id, name, email } = user;
const [first, ...rest] = items;

// Nullish coalescing
const displayName = user.nickname ?? user.name ?? "Anonymous";

// Optional chaining
const city = user?.address?.city;

// Object shorthand
const data = { id, name, createdAt: new Date() };

Weekly Installs
16
Repository
exceptionless/e…tionless
GitHub Stars
2.5K
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
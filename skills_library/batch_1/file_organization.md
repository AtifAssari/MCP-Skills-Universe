---
title: file-organization
url: https://skills.sh/supercent-io/skills-template/file-organization
---

# file-organization

skills/supercent-io/skills-template/file-organization
file-organization
Installation
$ npx skills add https://github.com/supercent-io/skills-template --skill file-organization
Summary

Establish scalable project structures with standardized naming conventions and folder organization patterns.

Provides templates for React/Next.js frontends, Node.js/Express backends, and feature-based large-scale applications with clear separation of concerns
Defines naming conventions for files (PascalCase components, camelCase utilities, UPPER_SNAKE_CASE constants), folders (kebab-case or camelCase), and variables (with is/has/can prefixes for booleans)
Includes best practices for path aliases, barrel exports, colocation of related files, and enforcing maximum folder depth to prevent excessive nesting
Covers constraints like avoiding circular dependencies, vague folder names, and deep nesting beyond five levels
SKILL.md
Project File Organization
When to use this skill
New Projects: Initial folder structure design
Project Growth: Refactoring when complexity increases
Team Standardization: Establish consistent structure
Instructions
Step 1: React/Next.js Project Structure
src/
├── app/                      # Next.js 13+ App Router
│   ├── (auth)/               # Route groups
│   │   ├── login/
│   │   └── signup/
│   ├── (dashboard)/
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   └── settings/
│   ├── api/                  # API routes
│   │   ├── auth/
│   │   └── users/
│   └── layout.tsx
│
├── components/               # UI Components
│   ├── ui/                   # Reusable UI (Button, Input)
│   │   ├── Button/
│   │   │   ├── Button.tsx
│   │   │   ├── Button.test.tsx
│   │   │   └── index.ts
│   │   └── Input/
│   ├── layout/               # Layout components (Header, Footer)
│   ├── features/             # Feature-specific components
│   │   ├── auth/
│   │   └── dashboard/
│   └── shared/               # Shared across features
│
├── lib/                      # Utilities & helpers
│   ├── utils.ts
│   ├── hooks/
│   │   ├── useAuth.ts
│   │   └── useLocalStorage.ts
│   └── api/
│       └── client.ts
│
├── store/                    # State management
│   ├── slices/
│   │   ├── authSlice.ts
│   │   └── userSlice.ts
│   └── index.ts
│
├── types/                    # TypeScript types
│   ├── api.ts
│   ├── models.ts
│   └── index.ts
│
├── config/                   # Configuration
│   ├── env.ts
│   └── constants.ts
│
└── styles/                   # Global styles
    ├── globals.css
    └── theme.ts

Step 2: Node.js/Express Backend Structure
src/
├── api/                      # API layer
│   ├── routes/
│   │   ├── auth.routes.ts
│   │   ├── user.routes.ts
│   │   └── index.ts
│   ├── controllers/
│   │   ├── auth.controller.ts
│   │   └── user.controller.ts
│   └── middlewares/
│       ├── auth.middleware.ts
│       ├── errorHandler.ts
│       └── validation.ts
│
├── services/                 # Business logic
│   ├── auth.service.ts
│   ├── user.service.ts
│   └── email.service.ts
│
├── repositories/             # Data access layer
│   ├── user.repository.ts
│   └── session.repository.ts
│
├── models/                   # Database models
│   ├── User.ts
│   └── Session.ts
│
├── database/                 # Database setup
│   ├── connection.ts
│   ├── migrations/
│   └── seeds/
│
├── utils/                    # Utilities
│   ├── logger.ts
│   ├── crypto.ts
│   └── validators.ts
│
├── config/                   # Configuration
│   ├── index.ts
│   ├── database.ts
│   └── env.ts
│
├── types/                    # TypeScript types
│   ├── express.d.ts
│   └── models.ts
│
├── __tests__/                # Tests
│   ├── unit/
│   ├── integration/
│   └── e2e/
│
└── index.ts                  # Entry point

Step 3: Feature-Based Structure (Large-Scale Apps)
src/
├── features/
│   ├── auth/
│   │   ├── components/
│   │   │   ├── LoginForm.tsx
│   │   │   └── SignupForm.tsx
│   │   ├── hooks/
│   │   │   └── useAuth.ts
│   │   ├── api/
│   │   │   └── authApi.ts
│   │   ├── store/
│   │   │   └── authSlice.ts
│   │   ├── types/
│   │   │   └── auth.types.ts
│   │   └── index.ts
│   │
│   ├── products/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── api/
│   │   └── types/
│   │
│   └── orders/
│
├── shared/                   # Shared across features
│   ├── components/
│   ├── hooks/
│   ├── utils/
│   └── types/
│
└── core/                     # App-wide
    ├── store/
    ├── router/
    └── config/

Step 4: Naming Conventions

File Names:

Components:       PascalCase.tsx
Hooks:            camelCase.ts        (useAuth.ts)
Utils:            camelCase.ts        (formatDate.ts)
Constants:        UPPER_SNAKE_CASE.ts (API_ENDPOINTS.ts)
Types:            camelCase.types.ts  (user.types.ts)
Tests:            *.test.ts, *.spec.ts


Folder Names:

kebab-case:       user-profile/
camelCase:        userProfile/       (optional: hooks/, utils/)
PascalCase:       UserProfile/       (optional: components/)

✅ Consistency is key (entire team uses the same rules)


Variable/Function Names:

// Components: PascalCase
const UserProfile = () => {};

// Functions: camelCase
function getUserById() {}

// Constants: UPPER_SNAKE_CASE
const API_BASE_URL = 'https://api.example.com';

// Private: _prefix (optional)
class User {
  private _id: string;

  private _hashPassword() {}
}

// Booleans: is/has/can prefix
const isAuthenticated = true;
const hasPermission = false;
const canEdit = true;

Step 5: index.ts Barrel Files

components/ui/index.ts:

// ✅ Good example: Re-export named exports
export { Button } from './Button/Button';
export { Input } from './Input/Input';
export { Modal } from './Modal/Modal';

// Usage:
import { Button, Input } from '@/components/ui';


❌ Bad example:

// Re-export everything (impairs tree-shaking)
export * from './Button';
export * from './Input';

Output format
Project Template
my-app/
├── .github/
│   └── workflows/
├── public/
├── src/
│   ├── app/
│   ├── components/
│   ├── lib/
│   ├── types/
│   └── config/
├── tests/
├── docs/
├── scripts/
├── .env.example
├── .gitignore
├── .eslintrc.json
├── .prettierrc
├── tsconfig.json
├── package.json
└── README.md

Constraints
Required Rules (MUST)
Consistency: Entire team uses the same rules
Clear Folder Names: Roles must be explicit
Max Depth: Recommend 5 levels or fewer
Prohibited (MUST NOT)
Excessive Nesting: Avoid 7+ levels of folder depth
Vague Names: Avoid utils2/, helpers/, misc/
Circular Dependencies: Prohibit A → B → A references
Best practices
Colocation: Keep related files close (component + styles + tests)
Feature-Based: Modularize by feature
Path Aliases: Simplify imports with @/

tsconfig.json:

{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"],
      "@/components/*": ["./src/components/*"],
      "@/lib/*": ["./src/lib/*"]
    }
  }
}


Usage:

// ❌ Bad example
import { Button } from '../../../components/ui/Button';

// ✅ Good example
import { Button } from '@/components/ui';

References
React File Structure
Node.js Best Practices
Clean Architecture
Metadata
Version
Current Version: 1.0.0
Last Updated: 2025-01-01
Compatible Platforms: Claude, ChatGPT, Gemini
Tags

#file-organization #project-structure #folder-structure #naming-conventions #utilities

Examples
Example 1: Basic usage
Example 2: Advanced usage
Weekly Installs
11.0K
Repository
supercent-io/sk…template
GitHub Stars
88
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
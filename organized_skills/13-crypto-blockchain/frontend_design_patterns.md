---
rating: ⭐⭐⭐
title: frontend-design-patterns
url: https://skills.sh/mineru98/skills-store/frontend-design-patterns
---

# frontend-design-patterns

skills/mineru98/skills-store/frontend-design-patterns
frontend-design-patterns
Installation
$ npx skills add https://github.com/mineru98/skills-store --skill frontend-design-patterns
SKILL.md
Frontend Design Patterns

Enterprise-grade React architecture combining Domain-Driven Design (DDD) and Feature-Sliced Design (FSD) with strict TypeScript conventions.

Core Patterns
1. DDD + FSD Hybrid Architecture
Philosophy: Think in domains, not pages
Structure: Layered architecture with unidirectional dependencies
Key Concept: Features (user actions) vs Entities (data representation)

Reference: See references/ddd-fsd-fundamentals.md for detailed DDD/FSD fusion strategy.

2. FSD Layer Hierarchy
App -> Pages -> Widgets -> Features -> Entities -> Shared


Each layer only depends on layers below it. No upward dependencies.

Slices: Domain-based directories (e.g., features/cart, features/auth)
Segments: ui/, model/, api/, lib/, config/, index.ts

Reference: See references/fsd-layers-guide.md for complete layer definitions.

3. Component Structure: Index/Types/Styles
ComponentName/
├── index.tsx    # React logic & JSX
├── types.ts     # TypeScript interfaces
└── styles.ts    # CSS-in-JS (Emotion/styled-components)


Separates concerns at filesystem level. Improves collaboration and reduces merge conflicts.

Reference: See references/component-structure.md for implementation details.

4. Data Layer: Service/Hook 1:1 Mapping
Service Layer (Pure TS) -> Hook Layer (React Query) -> Components

Service: API calls, DTOs (React-agnostic)
Hook: React Query integration, caching, loading/error states
Rule: One service function = one custom hook
Query Keys: Use factory pattern

Reference: See references/data-layer-architecture.md for Axios/React Query setup.

5. State Management: Zustand + React Query
React Query: Server state (API data, caching)
Zustand: Client state (theme, modals, complex forms)
Store Location: Domain-specific in model/ segment
Pattern: Slice pattern with selector optimization

Reference: See references/state-management.md for Zustand patterns.

6. TypeScript Conventions
Target	Case	Example
Component	PascalCase	UserProfile
Interface	PascalCase	UserProfileProps
Variable	camelCase	userList, isLoading
Boolean	camelCase	is, has, should, can prefix
Constant	UPPER_SNAKE	MAX_COUNT
Hook	camelCase	useAuth, useWindowSize

Reference: See references/typescript-conventions.md for complete rules.

Workflow

Load references based on current task:

Task	Reference
Architecture design	references/ddd-fsd-fundamentals.md
Folder structure	references/fsd-layers-guide.md
Component creation	references/component-structure.md
API/Data layer	references/data-layer-architecture.md
State management	references/state-management.md
Code conventions	references/typescript-conventions.md
Scripts
Create FSD Structure
python scripts/create_fsd_structure.py <project-root> [--slices cart auth user]


Creates complete FSD folder structure with standard segments.

Create Component
python scripts/create_component.py <path> <ComponentName>


Generates Index/Types/Styles pattern component.

Create Service/Hook Pair
python scripts/create_service_hook.py <feature-path> <service-name>


Generates Service Layer + Hook Layer with Query Key factory.

Create Zustand Store
python scripts/create_zustand_store.py <feature-path> <store-name>


Generates Zustand store with selectors and actions.

Key Principles
Separation of Concerns: UI, logic, styles separated at filesystem level
Unidirectional Dependencies: Layers only depend on lower layers
Explicit Dependencies: No circular references
Type Safety: Strict TypeScript, no any
Single Responsibility: Each file/module has one clear purpose
Weekly Installs
17
Repository
mineru98/skills-store
GitHub Stars
4
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
---
title: react
url: https://skills.sh/markhamsquareventures/essentials/react
---

# react

skills/markhamsquareventures/essentials/react
react
Installation
$ npx skills add https://github.com/markhamsquareventures/essentials --skill react
SKILL.md
React
Instructions

This project uses React 19 with TypeScript and the React Compiler enabled via babel-plugin-react-compiler.

Component Structure
Pages live in resources/js/pages/ and are rendered via Inertia
Shared components live in resources/js/components/
UI primitives (shadcn/ui) live in resources/js/components/ui/
Custom hooks live in resources/js/hooks/
Page Props from Controllers

Always receive page data as props from the Laravel controller via Inertia. Do NOT fetch data client-side or use useEffect to load page data.

interface EditProjectProps { project: Project; clients: Client[]; }

export default function EditProject({ project, clients }: EditProjectProps) { return ( <Form action={update({ project: project.id }).url} method="patch"> {/* Form fields using project and clients data */} ); }

This pattern ensures:

State consistency - The server is the single source of truth; no client-side caching or stale data issues
Data is loaded server-side before the page renders
No loading states needed for initial page data
SEO-friendly server-rendered content
Type-safe props matching controller output
TypeScript Conventions
All component props should be typed explicitly
Use interfaces for object shapes, defined in resources/js/types/index.d.ts
Prefer React.ComponentProps<"element"> for extending native element props
Use path aliases: @/components, @/hooks, @/lib, @/types

interface CardProps { title: string; description?: string; className?: string; children: React.ReactNode; }

export function Card({ title, description, className, children }: CardProps) { return ( <div className={cn('rounded-lg border p-4', className)}> {title} {description && {description}} {children} ); }

React 19 + React Compiler
The React Compiler automatically memoizes components and hooks
Do NOT manually add useMemo, useCallback, or React.memo unless profiling shows a specific need
Write straightforward code and let the compiler optimize
State Management
Use React's built-in useState and useReducer for local state
Use Inertia's shared data for server-provided state (accessed via usePage())
For form state, use the Inertia <Form> component (see inertia skill)

export function UserGreeting() { const { auth } = usePage().props;

return <span>Hello, {auth.user.name}</span>;


}

Event Handlers
Use inline arrow functions for simple handlers
Extract to named functions only when logic is complex or reused
Conditional Rendering
Use early returns for guard clauses
Prefer && for simple conditionals, ternaries for if/else
Use separate components for complex conditional logic
return (
    <div>
        {data.items.length > 0 && <ItemList items={data.items} />}
        {data.error ? <ErrorMessage error={data.error} /> : <SuccessIndicator />}
    </div>
);


}

File Naming
Components: PascalCase (UserCard.tsx)
Hooks: camelCase with use prefix (useClipboard.ts)
Utilities: camelCase (formatDate.ts)
Pages: kebab-case matching the route (edit.tsx, create.tsx, index.tsx)
Weekly Installs
28
Repository
markhamsquareve…sentials
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
---
title: nextjs-best-practices
url: https://skills.sh/sickn33/antigravity-awesome-skills/nextjs-best-practices
---

# nextjs-best-practices

skills/sickn33/antigravity-awesome-skills/nextjs-best-practices
nextjs-best-practices
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill nextjs-best-practices
Summary

Next.js App Router development patterns covering server/client components, data fetching, and routing.

Server Components are the default; use Client Components only for interactivity (useState, event handlers, forms)
Data fetching belongs in Server Components with three caching strategies: static (build-time), ISR (time-based revalidation), and dynamic (no-store)
File conventions organize routes: page.tsx for UI, layout.tsx for shared structure, loading.tsx and error.tsx for states, and route groups (name) to organize without affecting URLs
Server Actions handle form submissions and data mutations; validate inputs and mark with 'use server'
Avoid common pitfalls: excessive 'use client' directives, client-side data fetching, missing loading/error boundaries, and large client bundles
SKILL.md
Next.js Best Practices

Principles for Next.js App Router development.

1. Server vs Client Components
Decision Tree
Does it need...?
│
├── useState, useEffect, event handlers
│   └── Client Component ('use client')
│
├── Direct data fetching, no interactivity
│   └── Server Component (default)
│
└── Both? 
    └── Split: Server parent + Client child

By Default
Type	Use
Server	Data fetching, layout, static content
Client	Forms, buttons, interactive UI
2. Data Fetching Patterns
Fetch Strategy
Pattern	Use
Default	Static (cached at build)
Revalidate	ISR (time-based refresh)
No-store	Dynamic (every request)
Data Flow
Source	Pattern
Database	Server Component fetch
API	fetch with caching
User input	Client state + server action
3. Routing Principles
File Conventions
File	Purpose
page.tsx	Route UI
layout.tsx	Shared layout
loading.tsx	Loading state
error.tsx	Error boundary
not-found.tsx	404 page
Route Organization
Pattern	Use
Route groups (name)	Organize without URL
Parallel routes @slot	Multiple same-level pages
Intercepting (.)	Modal overlays
4. API Routes
Route Handlers
Method	Use
GET	Read data
POST	Create data
PUT/PATCH	Update data
DELETE	Remove data
Best Practices
Validate input with Zod
Return proper status codes
Handle errors gracefully
Use Edge runtime when possible
5. Performance Principles
Image Optimization
Use next/image component
Set priority for above-fold
Provide blur placeholder
Use responsive sizes
Bundle Optimization
Dynamic imports for heavy components
Route-based code splitting (automatic)
Analyze with bundle analyzer
6. Metadata
Static vs Dynamic
Type	Use
Static export	Fixed metadata
generateMetadata	Dynamic per-route
Essential Tags
title (50-60 chars)
description (150-160 chars)
Open Graph images
Canonical URL
7. Caching Strategy
Cache Layers
Layer	Control
Request	fetch options
Data	revalidate/tags
Full route	route config
Revalidation
Method	Use
Time-based	revalidate: 60
On-demand	revalidatePath/Tag
No cache	no-store
8. Server Actions
Use Cases
Form submissions
Data mutations
Revalidation triggers
Best Practices
Mark with 'use server'
Validate all inputs
Return typed responses
Handle errors
9. Anti-Patterns
❌ Don't	✅ Do
'use client' everywhere	Server by default
Fetch in client components	Fetch in server
Skip loading states	Use loading.tsx
Ignore error boundaries	Use error.tsx
Large client bundles	Dynamic imports
10. Project Structure
app/
├── (marketing)/     # Route group
│   └── page.tsx
├── (dashboard)/
│   ├── layout.tsx   # Dashboard layout
│   └── page.tsx
├── api/
│   └── [resource]/
│       └── route.ts
└── components/
    └── ui/


Remember: Server Components are the default for a reason. Start there, add client only when needed.

When to Use

This skill is applicable to execute the workflow or actions described in the overview.

Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
4.8K
Repository
sickn33/antigra…e-skills
GitHub Stars
36.1K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
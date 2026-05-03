---
rating: ⭐⭐⭐
title: nextjs-best-practices
url: https://skills.sh/davila7/claude-code-templates/nextjs-best-practices
---

# nextjs-best-practices

skills/davila7/claude-code-templates/nextjs-best-practices
nextjs-best-practices
Originally fromsickn33/antigravity-awesome-skills
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill nextjs-best-practices
Summary

Server Components by default, client interactivity on demand, with structured data fetching and caching strategies.

Server Components handle data fetching and static content; Client Components ('use client') manage forms, state, and event handlers. Split responsibilities when both are needed.
Data fetching uses static caching by default, with ISR (time-based revalidation) and dynamic (no-store) options for different freshness requirements.
Routing relies on file conventions (page.tsx, layout.tsx, loading.tsx, error.tsx) and patterns like route groups, parallel routes, and intercepting routes for modals.
Caching operates across three layers: request-level (fetch options), data-level (revalidate/tags), and full-route caching with on-demand or time-based revalidation.
Server Actions handle form submissions and mutations with input validation; avoid 'use client' everywhere, large client bundles, and skipping loading/error boundaries.
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

Weekly Installs
481
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
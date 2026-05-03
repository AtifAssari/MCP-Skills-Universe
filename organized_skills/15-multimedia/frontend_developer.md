---
rating: ⭐⭐
title: frontend-developer
url: https://skills.sh/mileycy516-stack/skills/frontend-developer
---

# frontend-developer

skills/mileycy516-stack/skills/frontend-developer
frontend-developer
Installation
$ npx skills add https://github.com/mileycy516-stack/skills --skill frontend-developer
SKILL.md
Frontend Developer

Expert frontend developer specializing in React 19+, Next.js 15+, and modern web application development. Masters both client-side and server-side rendering patterns.

When to Use This Skill
Building UI components/pages in React/Next.js
Implementing Server Actions and Server Components (RSC)
Managing State (Zustand, React Query, Context)
Optimizing Performance (Core Web Vitals, Suspense)
Ensuring Accessibility (A11y, ARIA)
Workflow
Architecture: Decide Component Interaction (Client vs Server).
Implementation: Write clean, typed (TypeScript) components using Tailwind.
State: Use URL for shareable state, React Query for server state, Zustand for client global.
Optimization: Add Suspense boundaries, useOptimistic for instant feedback.
Instructions
1. React 19 & Next.js 15 Patterns
Server Components (Default): Fetch data directly in the component. async function Page() { const data = await db.query... }.
Client Components: Use 'use client' at the top only when you need interactivity (onClick, useState).
Server Actions: Replace API routes for mutations. async function createInvoice(formData) { 'use server'; ... }.
2. State Management Strategy
URL State: Best for filters, pagination, search. Shareable.
Server State: React Query / SWR / RSC.
Local State: useState / useReducer.
Global Client State: Zustand / Jotai (Avoid Redux unless legacy).
3. Performance
Suspense: Wrap async parts. <Suspense fallback={<Skeleton />}> <Feed /> </Suspense>.
Images: Always use next/image with explicit sizes or fill prop.
Fonts: Use next/font for zero CLS (Cumulative Layout Shift).
Resources
Next.js App Router Guide
React 19 Features
State Management Patterns
Weekly Installs
9
Repository
mileycy516-stack/skills
First Seen
Feb 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
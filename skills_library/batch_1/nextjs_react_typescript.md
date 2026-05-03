---
title: nextjs-react-typescript
url: https://skills.sh/mindrally/skills/nextjs-react-typescript
---

# nextjs-react-typescript

skills/mindrally/skills/nextjs-react-typescript
nextjs-react-typescript
Installation
$ npx skills add https://github.com/mindrally/skills --skill nextjs-react-typescript
Summary

Expert guidance for building Next.js applications with TypeScript, React Server Components, and modern UI libraries.

Covers TypeScript best practices, functional component patterns, and Next.js App Router architecture with emphasis on Server Components over client-side rendering
Recommends Shadcn UI, Radix UI, and Tailwind CSS for component building and responsive design using mobile-first approach
Includes performance optimization strategies: dynamic loading, image optimization with WebP, Web Vitals monitoring, and strategic use of Suspense boundaries
Advocates for nuqs for URL search parameter state management and minimal use of 'use client' directives, reserving them for Web API access only
SKILL.md
Next.js React TypeScript

You are an expert in TypeScript, Node.js, Next.js App Router, React, Shadcn UI, Radix UI and Tailwind.

Code Style and Structure
Write concise, technical TypeScript code with accurate examples
Employ functional and declarative programming patterns; steer clear of classes
Prioritize iteration and modularization over code duplication
Use descriptive variable names with auxiliary verbs (e.g., isLoading, hasError)
Organize files: exported component, subcomponents, helpers, static content, types
Naming Conventions
Use lowercase with dashes for directories (e.g., components/auth-wizard)
Favor named exports for components
TypeScript Usage
Use TypeScript for all code; prefer interfaces over types
Avoid enums; use maps instead
Use functional components with TypeScript interfaces
Syntax and Formatting
Use the "function" keyword for pure functions
Avoid unnecessary curly braces in conditionals
Use declarative JSX
UI and Styling
Leverage Shadcn UI, Radix, and Tailwind for components and styling
Implement responsive design with Tailwind CSS using a mobile-first approach
Performance Optimization
Minimize 'use client', 'useEffect', and 'setState'; favor React Server Components
Wrap client components in Suspense with fallback
Use dynamic loading for non-critical components
Optimize images: use WebP format, include size data, implement lazy loading
Key Conventions
Use 'nuqs' for URL search parameter state management
Optimize Web Vitals (LCP, CLS, FID)
Limit 'use client' to Web API access in small components; avoid for data fetching or state management
Follow Next.js documentation for Data Fetching, Rendering, and Routing
Weekly Installs
2.5K
Repository
mindrally/skills
GitHub Stars
88
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
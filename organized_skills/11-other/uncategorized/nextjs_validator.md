---
rating: ⭐⭐⭐
title: nextjs-validator
url: https://skills.sh/shipshitdev/library/nextjs-validator
---

# nextjs-validator

skills/shipshitdev/library/nextjs-validator
nextjs-validator
Installation
$ npx skills add https://github.com/shipshitdev/library --skill nextjs-validator
SKILL.md
Next.js Validator

Validates Next.js 16 configuration and prevents deprecated patterns. AI assistants often generate Next.js 14/15 patterns - this skill enforces Next.js 16.

When This Activates
Setting up a new Next.js project
Before any Next.js development work
Auditing existing Next.js projects
After AI generates Next.js code
CI/CD pipeline validation
Quick Start
python3 scripts/validate.py --root .
python3 scripts/validate.py --root . --strict

What Gets Checked
1. Package Version
// GOOD: v16+
"next": "^16.0.0"

// BAD: v15 or earlier
"next": "^15.0.0"

2. Proxy vs Middleware

GOOD - Next.js 16:

// proxy.ts (Node.js runtime - REQUIRED)
import { createProxy } from 'next/proxy';
export const proxy = createProxy();


BAD - Deprecated:

// middleware.ts (Edge runtime - DEPRECATED)
export function middleware() { }

3. App Router Structure

GOOD:

app/
├── layout.tsx          # Root layout
├── page.tsx            # Home page
├── (routes)/           # Route groups
│   ├── dashboard/
│   │   └── page.tsx
│   └── settings/
│       └── page.tsx
└── api/                # API routes (optional)


BAD - Pages Router (deprecated):

pages/
├── _app.tsx
├── index.tsx
└── api/

4. Cache Components & use cache

GOOD - Next.js 16:

// app/dashboard/page.tsx
'use cache';

export default async function Dashboard() {
  const data = await fetch('/api/data');
  return <DashboardView data={data} />;
}

5. Server Actions

GOOD:

// app/actions.ts
'use server';

export async function createItem(formData: FormData) {
  // Server-side logic
}

6. Turbopack Configuration

GOOD - Default in Next.js 16:

// next.config.ts (Turbopack is default, no config needed)


BAD - Disabling Turbopack:

// Don't disable unless absolutely necessary
experimental: {
  turbo: false  // BAD
}

7. Config File Format

GOOD - TypeScript config:

// next.config.ts
import type { NextConfig } from 'next';

const config: NextConfig = {
  // ...
};

export default config;


BAD - JavaScript config:

// next.config.js - Prefer .ts
module.exports = { }

Deprecated Patterns to Avoid
Deprecated (v15-)	Replacement (v16+)
middleware.ts	proxy.ts
getServerSideProps	Server Components + use cache
getStaticProps	Server Components + use cache
getStaticPaths	generateStaticParams
_app.tsx	app/layout.tsx
_document.tsx	app/layout.tsx
pages/ directory	app/ directory
next/router	next/navigation
useRouter() (pages)	useRouter() from next/navigation
Next.js 16 Features to Use
Cache Components
'use cache';

// Entire component cached
export default async function CachedPage() {
  const data = await fetchData();
  return <View data={data} />;
}

Partial Pre-Rendering (PPR)
// next.config.ts
const config: NextConfig = {
  experimental: {
    ppr: true,
  },
};

Next.js DevTools MCP

AI-assisted debugging with contextual insight:

// Enable in development
// Works with Claude Code and other MCP-compatible tools

Parallel Routes
app/
├── @modal/
│   └── login/
│       └── page.tsx
├── @sidebar/
│   └── default.tsx
└── layout.tsx

Intercepting Routes
app/
├── feed/
│   └── page.tsx
├── photo/
│   └── [id]/
│       └── page.tsx
└── @modal/
    └── (.)photo/
        └── [id]/
            └── page.tsx

Validation Output
=== Next.js 16 Validation Report ===

Package Version: next@16.1.0 ✓

File Structure:
  ✓ Using app/ directory (App Router)
  ✗ Found pages/ directory - migrate to App Router
  ✓ Found proxy.ts
  ✗ Found middleware.ts - migrate to proxy.ts

Patterns:
  ✓ Using Server Components
  ✗ Found getServerSideProps in 2 files
  ✓ Using next/navigation

Config:
  ✓ next.config.ts (TypeScript)
  ✓ Turbopack enabled (default)

Summary: 2 issues found
  - Migrate pages/ to app/ directory
  - Replace middleware.ts with proxy.ts

Migration Guide
From middleware.ts to proxy.ts

Before (v15):

// middleware.ts
import { NextResponse } from 'next/server';

export function middleware(request) {
  // Edge runtime
  return NextResponse.next();
}

export const config = {
  matcher: ['/dashboard/:path*'],
};


After (v16):

// proxy.ts
import { createProxy } from 'next/proxy';

export const proxy = createProxy({
  // Node.js runtime
  async handle(request) {
    // Full Node.js APIs available
    return request;
  },
  matcher: ['/dashboard/:path*'],
});

From getServerSideProps to Server Components

Before:

// pages/dashboard.tsx
export async function getServerSideProps() {
  const data = await fetchData();
  return { props: { data } };
}

export default function Dashboard({ data }) {
  return <View data={data} />;
}


After:

// app/dashboard/page.tsx
export default async function Dashboard() {
  const data = await fetchData();
  return <View data={data} />;
}

CI/CD Integration
# .github/workflows/validate.yml
- name: Validate Next.js 16
  run: |
    python3 scripts/validate.py \
      --root . \
      --strict \
      --ci

Integration
tailwind-validator - Validate Tailwind v4 config
biome-validator - Validate Biome 2.3+ config
clerk-validator - Validate Clerk auth setup
Weekly Installs
111
Repository
shipshitdev/library
GitHub Stars
21
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass
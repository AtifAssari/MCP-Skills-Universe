---
title: nextjs-16-complete-guide
url: https://skills.sh/fernandofuc/nextjs-claude-setup/nextjs-16-complete-guide
---

# nextjs-16-complete-guide

skills/fernandofuc/nextjs-claude-setup/nextjs-16-complete-guide
nextjs-16-complete-guide
Installation
$ npx skills add https://github.com/fernandofuc/nextjs-claude-setup --skill nextjs-16-complete-guide
SKILL.md
Next.js 16 Complete Guide
Purpose

Comprehensive reference for Next.js 16's revolutionary features: Cache Components with "use cache", stable Turbopack as default bundler, proxy.ts architecture, DevTools MCP integration, and React Compiler support.

When to Use
Starting new Next.js projects (use 16 from day one)
Migrating from Next.js 15 to 16
Understanding Cache Components and Partial Pre-Rendering (PPR)
Configuring Turbopack for optimal performance
Migrating middleware.ts to proxy.ts
Leveraging AI-assisted debugging with DevTools MCP
Setting up React Compiler for automatic memoization
What Changed: Next.js 15 → 16
The Big Picture

Next.js 15 was transition phase - async APIs, experimental Turbopack, changing cache defaults. Next.js 16 is the payoff - everything becomes stable, fast, and production-ready.

Key Differences
Feature	Next.js 15	Next.js 16
Bundler	Webpack (default), Turbopack (opt-in beta)	Turbopack (default, stable)
Caching	Implicit, confusing defaults	Explicit with "use cache"
Network Layer	middleware.ts (edge runtime)	proxy.ts (Node.js runtime)
DevTools	Basic error messages	MCP integration for AI debugging
React Compiler	Experimental	Stable, production-ready
Performance	Baseline	2-5× faster builds, 10× faster Fast Refresh
🚀 Core Features (The 20% That Delivers 80%)
1. Cache Components + "use cache"

The Problem in Next.js 15:

Implicit caching was "magic" - hard to predict what cached
Switching between static/dynamic was unclear
Performance optimization felt like guesswork

The Solution in Next.js 16:

// Enable in next.config.ts
const nextConfig = {
  cacheComponents: true,
};

export default nextConfig;


Usage Pattern:

// app/dashboard/page.tsx
import { Suspense } from 'react';

// This component caches its output
async function UserMetrics() {
  'use cache'; // 🎯 Explicit caching

  const metrics = await fetchMetrics(); // Cached result

  return <MetricsCard data={metrics} />;
}

// This stays dynamic
async function LiveBalance() {
  const balance = await fetchBalance(); // Always fresh
  return <BalanceWidget balance={balance} />;
}

export default function Dashboard() {
  return (
    <div>
      <Suspense fallback={<LoadingMetrics />}>
        <UserMetrics /> {/* Cached, instant load */}
      </Suspense>

      <LiveBalance /> {/* Dynamic, real-time */}
    </div>
  );
}


Why This Matters:

Instant navigation - Cached parts load immediately
Selective freshness - Only dynamic parts fetch on demand
Predictable behavior - You control what caches
SaaS dashboards - Perfect for panels with mixed static/dynamic content

Cache Granularity:

// Cache entire page
export default async function Page() {
  'use cache';
  return <PageContent />;
}

// Cache individual component
async function ExpensiveWidget() {
  'use cache';
  return <Chart data={await getData()} />;
}

// Cache function result
async function getStats() {
  'use cache';
  return await database.query('...');
}

2. Turbopack: Default Bundler (Stable)

Performance Numbers (Official Vercel Benchmarks):

2-5× faster production builds
Up to 10× faster Fast Refresh in development
File system caching - Even faster restarts on large projects

No Configuration Needed:

// next.config.ts
// Turbopack is now default - no config required!


Opt-out (if needed):

# Use Webpack instead
next build --webpack


File System Caching (Beta):

// next.config.ts
const nextConfig = {
  experimental: {
    turbopackFileSystemCacheForDev: true, // Faster restarts
  },
};


Why This Matters:

Faster feedback loop - See changes instantly (10× faster)
Shorter CI/CD times - 2-5× faster production builds
Better DX - Less waiting, more shipping
Large projects - Scales better than Webpack

What You Notice:

# Before (Webpack)
✓ Compiled in 4.2s

# After (Turbopack)
✓ Compiled in 0.4s  # 10× faster

3. proxy.ts Replaces middleware.ts

The Change:

# Old (Next.js 15)
middleware.ts  # Edge runtime, confusing

# New (Next.js 16)
proxy.ts       # Node.js runtime, explicit


Migration Example:

// OLD: middleware.ts
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  return NextResponse.redirect(new URL('/home', request.url));
}

export const config = {
  matcher: '/about/:path*',
};

// NEW: proxy.ts
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export default function proxy(request: NextRequest) {  // Changed function name
  return NextResponse.redirect(new URL('/home', request.url));
}

export const config = {
  matcher: '/about/:path*',
};


Key Changes:

Rename file: middleware.ts → proxy.ts
Rename export: export function middleware → export default function proxy
Runtime: Runs on Node.js (not edge)

Why This Matters:

Clearer boundary - "Proxy" = network entry point
Predictable runtime - Always Node.js, no edge ambiguity
Better debugging - Standard Node.js environment
4. DevTools MCP (AI-Assisted Debugging)

What It Does: Next.js 16 integrates Model Context Protocol (MCP) so AI agents can:

Read unified browser + server logs
Understand Next.js routing and caching
Access error stack traces automatically
Provide page-aware debugging context

Why This Matters:

AI copilots can debug your Next.js app natively
Faster debugging - AI understands framework internals
Better DX - Agent sees what you see (and more)

Use Case:

You: "Why is this page not caching?"
AI Agent (with MCP):
  - Reads server logs
  - Sees route configuration
  - Checks cache headers
  - Knows Next.js 16 caching rules
  → "You're missing 'use cache' directive in your component"


Integration: Works automatically with Claude Code, Cursor, and other MCP-compatible tools.

5. React Compiler (Stable)

What It Does: Automatically memoizes components - no more manual useMemo, useCallback, React.memo.

Setup:

npm install babel-plugin-react-compiler@latest

// next.config.ts
const nextConfig = {
  reactCompiler: true,  // Moved from experimental to stable
};


Before (Manual Optimization):

// You had to do this everywhere
const MemoizedComponent = React.memo(function Component({ data }) {
  const processed = useMemo(() => processData(data), [data]);
  const handleClick = useCallback(() => {
    console.log(processed);
  }, [processed]);

  return <div onClick={handleClick}>{processed}</div>;
});


After (React Compiler Does It):

// Just write code, compiler optimizes automatically
function Component({ data }) {
  const processed = processData(data);  // Auto-memoized
  const handleClick = () => {            // Auto-memoized
    console.log(processed);
  };

  return <div onClick={handleClick}>{processed}</div>;
}


Why This Matters:

Less boilerplate - Write cleaner code
Better performance - Compiler is smarter than manual optimization
No bugs - Compiler never forgets dependencies
🔥 Breaking Changes (15 → 16)
Required Changes
1. Node.js Version
# Minimum: Node.js 20.9+
# Next.js 15: Node.js 18 worked
# Next.js 16: Node.js 18 no longer supported

2. Async params & searchParams
// ❌ OLD (Next.js 15)
export default function Page({ params, searchParams }) {
  const id = params.id;  // Synchronous
}

// ✅ NEW (Next.js 16)
export default async function Page({ params, searchParams }) {
  const { id } = await params;  // Must await
  const { query } = await searchParams;
}

3. Async cookies(), headers(), draftMode()
// ❌ OLD
import { cookies } from 'next/headers';

export function MyComponent() {
  const token = cookies().get('token');  // Synchronous
}

// ✅ NEW
import { cookies } from 'next/headers';

export async function MyComponent() {
  const cookieStore = await cookies();  // Must await
  const token = cookieStore.get('token');
}

4. revalidateTag() Now Requires cacheLife Profile
// ❌ OLD
revalidateTag('posts');

// ✅ NEW
revalidateTag('posts', 'max');     // Options: 'max', 'hours', 'days'

5. middleware.ts → proxy.ts
# Required migration
mv middleware.ts proxy.ts

# Update function name
export default function proxy(request) { ... }

Removed Features
AMP support - Completely removed
next lint command - Removed
Node.js 18 - No longer supported
TypeScript <5.1 - No longer supported
📦 Migration Guide (Step-by-Step)
1. Pre-Migration Checklist
# Check current versions
node --version    # Should be 20.9+
npm list next     # Current Next.js version
npm list react    # React version

2. Automated Migration
# Upgrade to latest Next.js 16
npm install next@latest react@latest react-dom@latest

# Run codemod (handles most changes automatically)
npx @next/codemod@canary upgrade latest

3. Manual Changes

Update next.config:

// next.config.ts
import type { NextConfig } from 'next';

const nextConfig: NextConfig = {
  // Enable Cache Components
  cacheComponents: true,

  // Enable React Compiler
  reactCompiler: true,

  // Optional: File system caching
  experimental: {
    turbopackFileSystemCacheForDev: true,
  },
};

export default nextConfig;


Rename middleware:

# If you have middleware.ts
git mv middleware.ts proxy.ts

# Update function name in proxy.ts
export default function proxy(request: NextRequest) {
  // Your logic
}


Update async APIs:

// Search codebase for:
// - params.
// - searchParams.
// - cookies()
// - headers()
// - draftMode()

// Add await before each

4. Test Everything
# Development
npm run dev  # Should use Turbopack automatically

# Production build
npm run build  # Should be 2-5× faster

# Run tests
npm test

5. Deploy
# Verify Node.js version in production
# Deploy to Vercel/platform
# Monitor for errors in first 24h

🎯 Best Practices
1. Start New Projects with Next.js 16
npx create-next-app@latest my-app
# Automatically uses Next.js 16, Turbopack, TypeScript, Tailwind

2. Use "use cache" Strategically
// ✅ Good: Cache expensive, infrequent-changing data
async function MonthlyReport() {
  'use cache';
  return await generateReport();
}

// ❌ Bad: Don't cache user-specific real-time data
async function CurrentBalance() {
  'use cache';  // Wrong! This should be fresh
  return await getUserBalance();
}

3. Monitor Build Performance
# Next.js 16 shows detailed timing
npm run build

# Example output:
Route (app)                              Size     First Load JS
┌ ○ /                                   142 B          87.2 kB
├ ○ /_not-found                         142 B          87.2 kB
└ ○ /dashboard                          1.23 kB        88.4 kB

Build time: 14.2s  # Was 57s in Next.js 15 with Webpack

4. Leverage DevTools MCP
Use Claude Code / Cursor with MCP support
Let AI agent read Next.js internals
Ask: "Why is my page slow?" - Agent sees server logs
5. Enable React Compiler for Large Apps
// Only if you have performance issues
reactCompiler: true

📊 When to Upgrade (Decision Matrix)
✅ Upgrade Now If:
Starting new project (use 16 from day one)
Small/medium codebase (<50 routes)
Using Vercel (tested platform)
Want 2-5× faster builds
Need instant navigation (Cache Components)
⏳ Wait 1-2 Weeks If:
Large production app (>100 routes)
Heavy middleware.ts usage (needs proxy.ts migration)
Custom Webpack config
Third-party libs not yet compatible
Risk-averse deployment policy
🚫 Don't Upgrade Yet If:
Using AMP pages (removed in 16)
Stuck on Node.js 18 (can't upgrade)
Custom build pipelines (need adapter testing)
Experimental features in production
🔗 Resources
Next.js 16 Release Notes
Upgrade Guide
Turbopack Documentation
Cache Components Guide
Codemod CLI
💡 Quick Reference
Installation
npm install next@latest react@latest react-dom@latest

Enable Features
// next.config.ts
const nextConfig = {
  cacheComponents: true,           // Cache Components
  reactCompiler: true,             // React Compiler
  experimental: {
    turbopackFileSystemCacheForDev: true,  // Faster dev restarts
  },
};

Migration Checklist
 Node.js 20.9+ installed
 npm install next@latest
 Run npx @next/codemod@canary upgrade latest
 Rename middleware.ts → proxy.ts
 Add await to params/searchParams/cookies/headers
 Update revalidateTag() calls with cacheLife
 Test build: npm run build
 Test dev: npm run dev
 Deploy to staging first

Summary: Next.js 16 delivers on the promises of 15 - everything is faster, more explicit, and production-ready. Turbopack is default, caching is predictable, and AI tooling is native. This is the version to build modern SaaS applications on in 2025.

Weekly Installs
248
Repository
fernandofuc/nex…de-setup
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
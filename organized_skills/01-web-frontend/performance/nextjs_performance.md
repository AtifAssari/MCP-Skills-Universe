---
rating: ⭐⭐⭐
title: nextjs-performance
url: https://skills.sh/giuseppe-trisciuoglio/developer-kit/nextjs-performance
---

# nextjs-performance

skills/giuseppe-trisciuoglio/developer-kit/nextjs-performance
nextjs-performance
Installation
$ npx skills add https://github.com/giuseppe-trisciuoglio/developer-kit --skill nextjs-performance
Summary

Comprehensive Next.js performance optimization covering Core Web Vitals, modern React patterns, and production-grade techniques.

Covers Core Web Vitals optimization (LCP, INP, CLS), image/font optimization with next/image and next/font, and caching strategies using unstable_cache and revalidateTag
Guides conversion of Client Components to Server Components, implementation of Suspense streaming for progressive loading, and bundle size reduction through code splitting
Includes Next.js 16 and React 19 patterns such as async params, use() hook for promises, and useOptimistic for optimistic UI updates
Provides before/after code examples, performance checklists, and common mistake patterns to avoid
SKILL.md
Next.js Performance Optimization

Expert guidance for optimizing Next.js applications with focus on Core Web Vitals, modern patterns, and best practices.

Overview

This skill provides comprehensive guidance for optimizing Next.js applications. It covers Core Web Vitals optimization (LCP, INP, CLS), modern React patterns, Server Components, caching strategies, and bundle optimization techniques. Designed for developers already familiar with React/Next.js who want to implement production-grade optimizations.

When to Use

Use this skill when working on Next.js applications and need to:

Optimize Core Web Vitals (LCP, INP, CLS) for better performance and SEO
Implement image optimization with next/image for faster loading
Configure font optimization with next/font to eliminate layout shift
Set up caching strategies using unstable_cache, revalidateTag, or ISR
Convert Client Components to Server Components for reduced bundle size
Implement Suspense streaming for progressive page loading
Analyze and reduce bundle size with code splitting and dynamic imports
Configure metadata and SEO for better search engine visibility
Optimize API route handlers for better performance
Apply Next.js 16 and React 19 modern patterns
Coverage Areas
Core Web Vitals optimization (LCP, INP, CLS)
Image optimization with next/image
Font optimization with next/font
Caching strategies (unstable_cache, revalidateTag, ISR)
Server Components patterns and Client-to-Server conversion
Streaming and Suspense for progressive loading
Bundle optimization and code splitting
Metadata and SEO configuration
Route handlers optimization
Next.js 16 + React 19 patterns
Instructions
Before Starting
Analyze current performance with Lighthouse
Identify bottlenecks - check Core Web Vitals in Chrome DevTools or PageSpeed Insights
Determine optimization priority:
LCP issues → Focus on images, fonts
INP issues → Reduce JS, use Server Components
CLS issues → Add dimensions, use next/font
How to Use This Skill

Load relevant reference files based on the area you're optimizing:

Image issues → references/image-optimization.md
Font/layout shift → references/font-optimization.md
Caching → references/caching-strategies.md
Component architecture → references/server-components.md

Follow the quick patterns for common optimizations

Apply before/after conversions to improve existing code

Verify improvements with Lighthouse after changes

Core Principles
Prefer Server Components - Only use 'use client' when necessary (browser APIs, interactivity)
Load components as low as possible - Keep Client Components at leaf nodes
Use Suspense boundaries - Enable streaming and progressive loading
Cache appropriately - Use tags for granular revalidation
Measure before/after - Always verify improvements with real metrics
Examples
Example 1: Convert Client Component to Server Component

BEFORE (Client Component with useEffect):

'use client'
import { useEffect, useState } from 'react'

export default function ProductList() {
  const [products, setProducts] = useState([])

  useEffect(() => {
    fetch('/api/products').then(r => r.json()).then(setProducts)
  }, [])

  return <ul>{products.map(p => <li key={p.id}>{p.name}</li>)}</ul>
}


AFTER (Server Component with direct data access):

import { db } from '@/lib/db'

export default async function ProductList() {
  const products = await db.product.findMany()
  return <ul>{products.map(p => <li key={p.id}>{p.name}</li>)}</ul>
}

Example 2: Optimize Images for LCP
import Image from 'next/image'

export function Hero() {
  return (
    <div className="relative w-full h-[600px]">
      <Image
        src="/hero.jpg"
        alt="Hero"
        fill
        priority          // Disable lazy loading for LCP
        sizes="100vw"
        className="object-cover"
      />
    </div>
  )
}

Example 3: Implement Caching Strategy
import { unstable_cache, revalidateTag } from 'next/cache'

// Cached data function
const getProducts = unstable_cache(
  async () => db.product.findMany(),
  ['products'],
  { revalidate: 3600, tags: ['products'] }
)

// Revalidate on mutation
export async function createProduct(data: FormData) {
  'use server'
  await db.product.create({ data })
  revalidateTag('products')
}

Example 4: Setup Optimized Fonts
import { Inter } from 'next/font/google'

const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-inter',
})

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={inter.variable}>
      <body className={`${inter.className} antialiased`}>
        {children}
      </body>
    </html>
  )
}

Example 5: Implement Suspense Streaming
import { Suspense } from 'react'

export default function Page() {
  return (
    <>
      <header>Static content (immediate)</header>

      <Suspense fallback={<ProductSkeleton />}>
        <ProductList />  {/* Streamed when ready */}
      </Suspense>

      <Suspense fallback={<ReviewsSkeleton />}>
        <Reviews />      {/* Independent streaming */}
      </Suspense>
    </>
  )
}

Reference Documentation

Load these references when working on specific areas:

Topic	Reference File
Core Web Vitals	references/core-web-vitals.md
Image Optimization	references/image-optimization.md
Font Optimization	references/font-optimization.md
Caching Strategies	references/caching-strategies.md
Server Components	references/server-components.md
Streaming/Suspense	references/streaming-suspense.md
Bundle Optimization	references/bundle-optimization.md
Metadata/SEO	references/metadata-seo.md
API Routes	references/api-routes.md
Next.js 16 Patterns	references/nextjs-16-patterns.md
Common Conversions
From	To	Benefit
useEffect + fetch	Direct async in Server Component	-70% JS, faster TTFB
useState for data	Server Component with direct DB access	Simpler code, no hydration
Client-side fetch	unstable_cache or ISR	Faster repeated loads
img tag	next/image	Optimized formats, lazy loading
CSS font import	next/font	Zero CLS, automatic optimization
Static import of heavy component	dynamic()	Reduced initial bundle
Best Practices
Images
Use next/image for all images
Add priority to LCP images only
Provide width and height or fill with sizes
Use placeholder="blur" for better UX
Configure remotePatterns in next.config.js
Fonts
Use next/font instead of CSS imports
Specify subsets to reduce size
Use display: 'swap' for immediate text render
Create CSS variable with variable option
Configure Tailwind to use CSS variables
Caching
Cache expensive queries with unstable_cache
Use meaningful cache tags for granular control
Implement on-demand revalidation for dynamic content
Set TTL based on data change frequency
Use revalidatePath for route-level invalidation
Components
Convert Client Components to Server Components where possible
Keep Client Components at the leaf level
Use Suspense boundaries for progressive loading
Implement proper loading states
Use dynamic() for heavy components below the fold
Bundle
Lazy load heavy components with dynamic()
Use named exports for better tree shaking
Analyze bundle regularly with @next/bundle-analyzer
Prefer ESM packages over CommonJS
Use modularizeImports for large libraries
Constraints and Warnings
Server Components Limitations
Cannot use browser APIs (window, localStorage, document)
Cannot use React hooks (useState, useEffect, useContext)
Cannot use event handlers (onClick, onSubmit)
Cannot use dynamic imports with ssr: false
Image Optimization Constraints
priority should only be used for above-the-fold images
External images require configuration in next.config.js
width and height are required unless using fill
Animated GIFs are not optimized by default
Caching Considerations
Cache tags must be manually invalidated
Data cache is per-request in development
Edge runtime has different caching behavior
Be careful caching user-specific data
Bundle Size Warnings
Dynamic imports can impact SEO if critical content
Tree shaking requires proper ES module usage
Some libraries cannot be tree shaken (avoid barrel exports)
Client Components increase bundle size - use sparingly
Next.js 16 + React 19 Specifics
Async Params
// Next.js 15+ params is a Promise
export default async function Page({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = await params
  const post = await fetchPost(slug)
  return <article>{post.content}</article>
}

use() Hook for Promises
'use client'
import { use, Suspense } from 'react'

function Comments({ promise }: { promise: Promise<Comment[]> }) {
  const comments = use(promise)  // Suspend until resolved
  return <ul>{comments.map(c => <li key={c.id}>{c.text}</li>)}</ul>
}

useOptimistic for UI Updates
'use client'
import { useOptimistic } from 'react'

export function TodoList({ todos }: { todos: Todo[] }) {
  const [optimisticTodos, addOptimisticTodo] = useOptimistic(
    todos,
    (state, newTodo: Todo) => [...state, newTodo]
  )

  async function addTodo(formData: FormData) {
    const text = formData.get('text') as string
    addOptimisticTodo({ id: crypto.randomUUID(), text, completed: false })
    await createTodo(text)
  }

  return (
    <form action={addTodo}>
      <input name="text" />
      {optimisticTodos.map(todo => <div key={todo.id}>{todo.text}</div>)}
    </form>
  )
}

Bundle Analysis
# Install analyzer
npm install --save-dev @next/bundle-analyzer

# Run analysis
ANALYZE=true npm run build

// next.config.js
const withBundleAnalyzer = require('@next/bundle-analyzer')({
  enabled: process.env.ANALYZE === 'true',
})

module.exports = withBundleAnalyzer({
  modularizeImports: {
    'lodash': { transform: 'lodash/{{member}}' },
  },
})

Performance Checklist
 All images use next/image with proper dimensions
 LCP images have priority attribute
 Fonts use next/font with subsets
 Server Components used where possible
 Client Components at leaf level only
 Suspense boundaries for data fetching
 Caching configured for expensive operations
 Bundle analyzed for duplicates
 Heavy components lazy loaded
 Lighthouse score verified before/after
Common Mistakes
// ❌ DON'T: Fetch in useEffect
'use client'
useEffect(() => { fetch('/api/data').then(...) }, [])

// ✅ DO: Fetch directly in Server Component
const data = await fetch('/api/data')

// ❌ DON'T: Forget dimensions on images
<Image src="/photo.jpg" />

// ✅ DO: Always provide dimensions
<Image src="/photo.jpg" width={800} height={600} />

// ❌ DON'T: Use priority on all images
<Image src="/photo1.jpg" priority />
<Image src="/photo2.jpg" priority />

// ✅ DO: Priority only for LCP
<Image src="/hero.jpg" priority />
<Image src="/photo.jpg" loading="lazy" />

// ❌ DON'T: Cache everything with same TTL
{ revalidate: 3600 }

// ✅ DO: Match TTL to data change frequency
{ revalidate: 86400 } // Categories rarely change
{ revalidate: 60 }     // Comments change often

External Resources
Next.js Performance Documentation
Core Web Vitals
React Server Components
Weekly Installs
989
Repository
giuseppe-trisci…oper-kit
GitHub Stars
233
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
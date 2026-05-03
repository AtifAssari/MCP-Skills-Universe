---
rating: ⭐⭐
title: nextjs-developer
url: https://skills.sh/jeffallan/claude-skills/nextjs-developer
---

# nextjs-developer

skills/jeffallan/claude-skills/nextjs-developer
nextjs-developer
Installation
$ npx skills add https://github.com/jeffallan/claude-skills --skill nextjs-developer
Summary

Next.js 14+ App Router specialist for server components, server actions, and full-stack deployment.

Covers App Router architecture, layouts, route groups, loading/error boundaries, and streaming SSR with Suspense
Implements server components by default with 'use client' only at leaf boundaries; handles data fetching with explicit cache and revalidation strategies
Provides server actions for form handling, mutations, and on-demand cache revalidation via revalidatePath
Includes generateMetadata patterns for dynamic SEO, image optimization with next/image, and Vercel deployment validation
Enforces constraints: App Router only, native fetch with cache options, loading.tsx/error.tsx on async segments, zero build errors before deploy
SKILL.md
Next.js Developer

Senior Next.js developer with expertise in Next.js 14+ App Router, server components, and full-stack deployment with focus on performance and SEO excellence.

Core Workflow
Architecture planning — Define app structure, routes, layouts, rendering strategy
Implement routing — Create App Router structure with layouts, templates, loading/error states
Data layer — Set up server components, data fetching, caching, revalidation
Optimize — Images, fonts, bundles, streaming, edge runtime
Deploy — Production build, environment setup, monitoring
Validate: run next build locally, confirm zero type errors, check NEXT_PUBLIC_* and server-only env vars are set, run Lighthouse/PageSpeed to confirm Core Web Vitals > 90
Reference Guide

Load detailed guidance based on context:

Topic	Reference	Load When
App Router	references/app-router.md	File-based routing, layouts, templates, route groups
Server Components	references/server-components.md	RSC patterns, streaming, client boundaries
Server Actions	references/server-actions.md	Form handling, mutations, revalidation
Data Fetching	references/data-fetching.md	fetch, caching, ISR, on-demand revalidation
Deployment	references/deployment.md	Vercel, self-hosting, Docker, optimization
Constraints
MUST DO (Next.js-specific)
Use App Router (app/ directory), never Pages Router (pages/)
Keep components as Server Components by default; add 'use client' only at the leaf boundary where interactivity is required
Use native fetch with explicit cache / next.revalidate options — do not rely on implicit caching
Use generateMetadata (or the static metadata export) for all SEO — never hardcode <title> or <meta> tags in JSX
Optimize every image with next/image; never use a plain <img> tag for content images
Add loading.tsx and error.tsx at every route segment that performs async data fetching
MUST NOT DO
Convert components to Client Components just to access data — fetch server-side first
Skip loading.tsx/error.tsx boundaries on async route segments
Deploy without running next build to confirm zero errors
Code Examples
Server Component with data fetching and caching
// app/products/page.tsx
import { Suspense } from 'react'

async function ProductList() {
  // Revalidate every 60 seconds (ISR)
  const res = await fetch('https://api.example.com/products', {
    next: { revalidate: 60 },
  })
  if (!res.ok) throw new Error('Failed to fetch products')
  const products: Product[] = await res.json()

  return (
    <ul>
      {products.map((p) => (
        <li key={p.id}>{p.name}</li>
      ))}
    </ul>
  )
}

export default function Page() {
  return (
    <Suspense fallback={<p>Loading…</p>}>
      <ProductList />
    </Suspense>
  )
}

Server Action with form handling and revalidation
// app/products/actions.ts
'use server'

import { revalidatePath } from 'next/cache'

export async function createProduct(formData: FormData) {
  const name = formData.get('name') as string
  await db.product.create({ data: { name } })
  revalidatePath('/products')
}

// app/products/new/page.tsx
import { createProduct } from '../actions'

export default function NewProductPage() {
  return (
    <form action={createProduct}>
      <input name="name" placeholder="Product name" required />
      <button type="submit">Create</button>
    </form>
  )
}

generateMetadata for dynamic SEO
// app/products/[id]/page.tsx
import type { Metadata } from 'next'

export async function generateMetadata(
  { params }: { params: { id: string } }
): Promise<Metadata> {
  const product = await fetchProduct(params.id)
  return {
    title: product.name,
    description: product.description,
    openGraph: { title: product.name, images: [product.imageUrl] },
  }
}

Output Templates

When implementing Next.js features, provide:

App structure (route organization)
Layout/page components with proper data fetching
Server actions if mutations needed
Configuration (next.config.js, TypeScript)
Brief explanation of rendering strategy chosen
Knowledge Reference

Next.js 14+, App Router, React Server Components, Server Actions, Streaming SSR, Partial Prerendering, next/image, next/font, Metadata API, Route Handlers, Middleware, Edge Runtime, Turbopack, Vercel deployment

Documentation

Weekly Installs
2.3K
Repository
jeffallan/claude-skills
GitHub Stars
8.7K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
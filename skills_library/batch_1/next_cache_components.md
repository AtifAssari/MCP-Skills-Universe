---
title: next-cache-components
url: https://skills.sh/vercel-labs/next-skills/next-cache-components
---

# next-cache-components

skills/vercel-labs/next-skills/next-cache-components
next-cache-components
Installation
$ npx skills add https://github.com/vercel-labs/next-skills --skill next-cache-components
Summary

Mix static, cached, and dynamic content in a single Next.js route with Partial Prerendering.

Enable with cacheComponents: true in next.config.ts; replaces the old experimental.ppr flag
Use the 'use cache' directive at file, component, or function level to cache async data with automatic key generation based on arguments and closures
Control cache lifetime with cacheLife() using built-in profiles ('minutes', 'hours', 'days', 'weeks', 'max') or inline configuration with stale, revalidate, and expire times
Invalidate caches with cacheTag() for tagging and updateTag() for immediate refresh or revalidateTag() for background revalidation
Wrap dynamic content in Suspense; cannot access cookies(), headers(), or searchParams inside use cache blocks unless using 'use cache: private'
SKILL.md
Cache Components (Next.js 16+)

Cache Components enable Partial Prerendering (PPR) - mix static, cached, and dynamic content in a single route.

Enable Cache Components
// next.config.ts
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  cacheComponents: true,
}

export default nextConfig


This replaces the old experimental.ppr flag.

Three Content Types

With Cache Components enabled, content falls into three categories:

1. Static (Auto-Prerendered)

Synchronous code, imports, pure computations - prerendered at build time:

export default function Page() {
  return (
    <header>
      <h1>Our Blog</h1>  {/* Static - instant */}
      <nav>...</nav>
    </header>
  )
}

2. Cached (use cache)

Async data that doesn't need fresh fetches every request:

async function BlogPosts() {
  'use cache'
  cacheLife('hours')

  const posts = await db.posts.findMany()
  return <PostList posts={posts} />
}

3. Dynamic (Suspense)

Runtime data that must be fresh - wrap in Suspense:

import { Suspense } from 'react'

export default function Page() {
  return (
    <>
      <BlogPosts />  {/* Cached */}

      <Suspense fallback={<p>Loading...</p>}>
        <UserPreferences />  {/* Dynamic - streams in */}
      </Suspense>
    </>
  )
}

async function UserPreferences() {
  const theme = (await cookies()).get('theme')?.value
  return <p>Theme: {theme}</p>
}

use cache Directive
File Level
'use cache'

export default async function Page() {
  // Entire page is cached
  const data = await fetchData()
  return <div>{data}</div>
}

Component Level
export async function CachedComponent() {
  'use cache'
  const data = await fetchData()
  return <div>{data}</div>
}

Function Level
export async function getData() {
  'use cache'
  return db.query('SELECT * FROM posts')
}

Cache Profiles
Built-in Profiles
'use cache'                    // Default: 5m stale, 15m revalidate

'use cache: remote'           // Platform-provided cache (Redis, KV)

'use cache: private'          // For compliance, allows runtime APIs

cacheLife() - Custom Lifetime
import { cacheLife } from 'next/cache'

async function getData() {
  'use cache'
  cacheLife('hours')  // Built-in profile
  return fetch('/api/data')
}


Built-in profiles: 'default', 'minutes', 'hours', 'days', 'weeks', 'max'

Inline Configuration
async function getData() {
  'use cache'
  cacheLife({
    stale: 3600,      // 1 hour - serve stale while revalidating
    revalidate: 7200, // 2 hours - background revalidation interval
    expire: 86400,    // 1 day - hard expiration
  })
  return fetch('/api/data')
}

Cache Invalidation
cacheTag() - Tag Cached Content
import { cacheTag } from 'next/cache'

async function getProducts() {
  'use cache'
  cacheTag('products')
  return db.products.findMany()
}

async function getProduct(id: string) {
  'use cache'
  cacheTag('products', `product-${id}`)
  return db.products.findUnique({ where: { id } })
}

updateTag() - Immediate Invalidation

Use when you need the cache refreshed within the same request:

'use server'

import { updateTag } from 'next/cache'

export async function updateProduct(id: string, data: FormData) {
  await db.products.update({ where: { id }, data })
  updateTag(`product-${id}`)  // Immediate - same request sees fresh data
}

revalidateTag() - Background Revalidation

Use for stale-while-revalidate behavior:

'use server'

import { revalidateTag } from 'next/cache'

export async function createPost(data: FormData) {
  await db.posts.create({ data })
  revalidateTag('posts')  // Background - next request sees fresh data
}

Runtime Data Constraint

Cannot access cookies(), headers(), or searchParams inside use cache.

Solution: Pass as Arguments
// Wrong - runtime API inside use cache
async function CachedProfile() {
  'use cache'
  const session = (await cookies()).get('session')?.value  // Error!
  return <div>{session}</div>
}

// Correct - extract outside, pass as argument
async function ProfilePage() {
  const session = (await cookies()).get('session')?.value
  return <CachedProfile sessionId={session} />
}

async function CachedProfile({ sessionId }: { sessionId: string }) {
  'use cache'
  // sessionId becomes part of cache key automatically
  const data = await fetchUserData(sessionId)
  return <div>{data.name}</div>
}

Exception: use cache: private

For compliance requirements when you can't refactor:

async function getData() {
  'use cache: private'
  const session = (await cookies()).get('session')?.value  // Allowed
  return fetchData(session)
}

Cache Key Generation

Cache keys are automatic based on:

Build ID - invalidates all caches on deploy
Function ID - hash of function location
Serializable arguments - props become part of key
Closure variables - outer scope values included
async function Component({ userId }: { userId: string }) {
  const getData = async (filter: string) => {
    'use cache'
    // Cache key = userId (closure) + filter (argument)
    return fetch(`/api/users/${userId}?filter=${filter}`)
  }
  return getData('active')
}

Complete Example
import { Suspense } from 'react'
import { cookies } from 'next/headers'
import { cacheLife, cacheTag } from 'next/cache'

export default function DashboardPage() {
  return (
    <>
      {/* Static shell - instant from CDN */}
      <header><h1>Dashboard</h1></header>
      <nav>...</nav>

      {/* Cached - fast, revalidates hourly */}
      <Stats />

      {/* Dynamic - streams in with fresh data */}
      <Suspense fallback={<NotificationsSkeleton />}>
        <Notifications />
      </Suspense>
    </>
  )
}

async function Stats() {
  'use cache'
  cacheLife('hours')
  cacheTag('dashboard-stats')

  const stats = await db.stats.aggregate()
  return <StatsDisplay stats={stats} />
}

async function Notifications() {
  const userId = (await cookies()).get('userId')?.value
  const notifications = await db.notifications.findMany({
    where: { userId, read: false }
  })
  return <NotificationList items={notifications} />
}

Migration from Previous Versions
Old Config	Replacement
experimental.ppr	cacheComponents: true
dynamic = 'force-dynamic'	Remove (default behavior)
dynamic = 'force-static'	'use cache' + cacheLife('max')
revalidate = N	cacheLife({ revalidate: N })
unstable_cache()	'use cache' directive
Migrating unstable_cache to use cache

unstable_cache has been replaced by the use cache directive in Next.js 16. When cacheComponents is enabled, convert unstable_cache calls to use cache functions:

Before (unstable_cache):

import { unstable_cache } from 'next/cache'

const getCachedUser = unstable_cache(
  async (id) => getUser(id),
  ['my-app-user'],
  {
    tags: ['users'],
    revalidate: 60,
  }
)

export default async function Page({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params
  const user = await getCachedUser(id)
  return <div>{user.name}</div>
}


After (use cache):

import { cacheLife, cacheTag } from 'next/cache'

async function getCachedUser(id: string) {
  'use cache'
  cacheTag('users')
  cacheLife({ revalidate: 60 })
  return getUser(id)
}

export default async function Page({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params
  const user = await getCachedUser(id)
  return <div>{user.name}</div>
}


Key differences:

No manual cache keys - use cache generates keys automatically from function arguments and closures. The keyParts array from unstable_cache is no longer needed.
Tags - Replace options.tags with cacheTag() calls inside the function.
Revalidation - Replace options.revalidate with cacheLife({ revalidate: N }) or a built-in profile like cacheLife('minutes').
Dynamic data - unstable_cache did not support cookies() or headers() inside the callback. The same restriction applies to use cache, but you can use 'use cache: private' if needed.
Limitations
Edge runtime not supported - requires Node.js
Static export not supported - needs server
Non-deterministic values (Math.random(), Date.now()) execute once at build time inside use cache

For request-time randomness outside cache:

import { connection } from 'next/server'

async function DynamicContent() {
  await connection()  // Defer to request time
  const id = crypto.randomUUID()  // Different per request
  return <div>{id}</div>
}


Sources:

Cache Components Guide
use cache Directive
unstable_cache (legacy)
Weekly Installs
25.3K
Repository
vercel-labs/next-skills
GitHub Stars
848
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
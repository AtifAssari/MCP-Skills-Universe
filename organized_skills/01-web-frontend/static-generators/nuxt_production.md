---
rating: ⭐⭐⭐
title: nuxt-production
url: https://skills.sh/secondsky/claude-skills/nuxt-production
---

# nuxt-production

skills/secondsky/claude-skills/nuxt-production
nuxt-production
Installation
$ npx skills add https://github.com/secondsky/claude-skills --skill nuxt-production
SKILL.md
Nuxt 4 Production Guide

Hydration, performance, testing, deployment, and migration patterns.

What's New in Nuxt 4
v4.2 Features (Latest)

1. Abort Control for Data Fetching

const controller = ref<AbortController>()

const { data } = await useAsyncData(
  'users',
  () => $fetch('/api/users', { signal: controller.value?.signal })
)

const abortRequest = () => {
  controller.value?.abort()
  controller.value = new AbortController()
}


2. Async Data Handler Extraction

39% smaller client bundles
Data fetching logic extracted to server chunks
Automatic optimization (no config needed)

3. Enhanced Error Handling

Dual error display: custom error page + technical overlay
Better error messages in development
v4.1 Features

1. Enhanced Chunk Stability

Import maps prevent cascading hash changes
Better long-term caching

2. Lazy Hydration

<script setup>
const LazyComponent = defineLazyHydrationComponent(() =>
  import('./HeavyComponent.vue')
)
</script>

Breaking Changes from v3
Change	v3	v4
Source directory	Root	app/
Data reactivity	Deep	Shallow (default)
Default values	null	undefined
Route middleware	Client	Server
App manifest	Opt-in	Default
When to Load References

Load references/hydration.md when:

Debugging "Hydration node mismatch" errors
Implementing ClientOnly components
Fixing non-deterministic rendering issues
Understanding SSR vs client rendering

Load references/performance.md when:

Optimizing Core Web Vitals scores
Implementing lazy loading and code splitting
Configuring caching strategies
Reducing bundle size

Load references/testing-vitest.md when:

Writing component tests with @nuxt/test-utils
Testing composables with Nuxt context
Mocking Nuxt APIs (useFetch, useRoute)
Setting up Vitest configuration

Load references/deployment-cloudflare.md when:

Deploying to Cloudflare Pages or Workers
Configuring wrangler.toml
Setting up NuxtHub integration
Working with D1, KV, R2 bindings
Hydration Best Practices
What Causes Hydration Mismatches
Cause	Example	Fix
Non-deterministic values	Math.random()	Use useState
Browser APIs on server	window.innerWidth	Use onMounted
Date/time on server	new Date()	Use useState or ClientOnly
Third-party scripts	Analytics	Use ClientOnly
Fix Patterns

Non-deterministic Values:

<!-- WRONG -->
<script setup>
const id = Math.random()
</script>

<!-- CORRECT -->
<script setup>
const id = useState('random-id', () => Math.random())
</script>


Browser APIs:

<!-- WRONG -->
<script setup>
const width = window.innerWidth  // Crashes on server!
</script>

<!-- CORRECT -->
<script setup>
const width = ref(0)
onMounted(() => {
  width.value = window.innerWidth
})
</script>


ClientOnly Component:

<template>
  <!-- Wrap client-only content -->
  <ClientOnly>
    <MyMapComponent />
    <template #fallback>
      <div class="skeleton">Loading map...</div>
    </template>
  </ClientOnly>
</template>


Conditional Rendering:

<script setup>
const showWidget = ref(false)

onMounted(() => {
  // Only show after hydration
  showWidget.value = true
})
</script>

<template>
  <AnalyticsWidget v-if="showWidget" />
</template>

Performance Optimization
Lazy Loading Components
<script setup>
// Lazy load heavy components
const HeavyChart = defineAsyncComponent(() =>
  import('~/components/HeavyChart.vue')
)

// With loading/error states
const HeavyChart = defineAsyncComponent({
  loader: () => import('~/components/HeavyChart.vue'),
  loadingComponent: LoadingSpinner,
  errorComponent: ErrorFallback,
  delay: 200,
  timeout: 10000
})
</script>

<template>
  <Suspense>
    <HeavyChart :data="chartData" />
    <template #fallback>
      <LoadingSpinner />
    </template>
  </Suspense>
</template>

Lazy Hydration
<script setup>
// Hydrate when visible in viewport
const LazyComponent = defineLazyHydrationComponent(
  () => import('./HeavyComponent.vue'),
  { hydrate: 'visible' }
)

// Hydrate on user interaction
const InteractiveComponent = defineLazyHydrationComponent(
  () => import('./InteractiveComponent.vue'),
  { hydrate: 'interaction' }
)

// Hydrate when browser is idle
const IdleComponent = defineLazyHydrationComponent(
  () => import('./IdleComponent.vue'),
  { hydrate: 'idle' }
)
</script>

Route Caching
// nuxt.config.ts
export default defineNuxtConfig({
  routeRules: {
    // Static pages (prerendered at build)
    '/': { prerender: true },
    '/about': { prerender: true },

    // SWR caching (1 hour)
    '/blog/**': { swr: 3600 },

    // ISR (regenerate every hour)
    '/products/**': { isr: 3600 },

    // SPA mode (no SSR)
    '/dashboard/**': { ssr: false },

    // Static with CDN caching
    '/static/**': {
      headers: { 'Cache-Control': 'public, max-age=31536000' }
    }
  }
})

Image Optimization
<template>
  <!-- Automatic optimization with NuxtImg -->
  <NuxtImg
    src="/images/hero.jpg"
    alt="Hero image"
    width="800"
    height="400"
    loading="lazy"
    placeholder
    format="webp"
  />

  <!-- Responsive images -->
  <NuxtPicture
    src="/images/product.jpg"
    alt="Product"
    sizes="sm:100vw md:50vw lg:400px"
    :modifiers="{ quality: 80 }"
  />
</template>

Testing with Vitest
Setup
bun add -d @nuxt/test-utils vitest @vue/test-utils happy-dom

// vitest.config.ts
import { defineVitestConfig } from '@nuxt/test-utils/config'

export default defineVitestConfig({
  test: {
    environment: 'nuxt',
    environmentOptions: {
      nuxt: {
        domEnvironment: 'happy-dom'
      }
    }
  }
})

Component Testing
// tests/components/UserCard.test.ts
import { describe, it, expect } from 'vitest'
import { mountSuspended } from '@nuxt/test-utils/runtime'
import UserCard from '~/components/UserCard.vue'

describe('UserCard', () => {
  it('renders user name', async () => {
    const wrapper = await mountSuspended(UserCard, {
      props: {
        user: { id: 1, name: 'John Doe', email: 'john@example.com' }
      }
    })

    expect(wrapper.text()).toContain('John Doe')
    expect(wrapper.text()).toContain('john@example.com')
  })

  it('emits delete event', async () => {
    const wrapper = await mountSuspended(UserCard, {
      props: { user: { id: 1, name: 'John' } }
    })

    await wrapper.find('[data-test="delete-btn"]').trigger('click')

    expect(wrapper.emitted('delete')).toHaveLength(1)
    expect(wrapper.emitted('delete')[0]).toEqual([1])
  })
})

Mocking Composables
// tests/components/Dashboard.test.ts
import { describe, it, expect, vi } from 'vitest'
import { mountSuspended, mockNuxtImport } from '@nuxt/test-utils/runtime'
import Dashboard from '~/pages/dashboard.vue'

// Mock useFetch
mockNuxtImport('useFetch', () => {
  return () => ({
    data: ref({ users: [{ id: 1, name: 'John' }] }),
    pending: ref(false),
    error: ref(null)
  })
})

describe('Dashboard', () => {
  it('displays users from API', async () => {
    const wrapper = await mountSuspended(Dashboard)

    expect(wrapper.text()).toContain('John')
  })
})

Testing Server Routes
// tests/api/users.test.ts
import { describe, it, expect } from 'vitest'
import { $fetch, setup } from '@nuxt/test-utils/e2e'

describe('API: /api/users', async () => {
  await setup({ server: true })

  it('returns users list', async () => {
    const users = await $fetch('/api/users')

    expect(users).toHaveProperty('users')
    expect(Array.isArray(users.users)).toBe(true)
  })

  it('creates a new user', async () => {
    const result = await $fetch('/api/users', {
      method: 'POST',
      body: { name: 'Jane', email: 'jane@example.com' }
    })

    expect(result.user.name).toBe('Jane')
  })
})

Deployment
Cloudflare Pages (Recommended)
# Build and deploy
bun run build
bunx wrangler pages deploy .output/public

// nuxt.config.ts
export default defineNuxtConfig({
  nitro: {
    preset: 'cloudflare-pages'
  }
})

Cloudflare Workers
// nuxt.config.ts
export default defineNuxtConfig({
  nitro: {
    preset: 'cloudflare-module'
  }
})

# wrangler.toml
name = "my-nuxt-app"
compatibility_date = "2025-01-01"
compatibility_flags = ["nodejs_compat"]

[[d1_databases]]
binding = "DB"
database_name = "my-database"
database_id = "xxx-xxx-xxx"

[[kv_namespaces]]
binding = "KV"
id = "xxx-xxx-xxx"

Vercel
// nuxt.config.ts
export default defineNuxtConfig({
  nitro: {
    preset: 'vercel'
  }
})

Netlify
// nuxt.config.ts
export default defineNuxtConfig({
  nitro: {
    preset: 'netlify'
  }
})

NuxtHub (Cloudflare All-in-One)
bun add @nuxthub/core

// nuxt.config.ts
export default defineNuxtConfig({
  modules: ['@nuxthub/core'],

  hub: {
    database: true,  // D1
    kv: true,        // KV
    blob: true,      // R2
    cache: true      // Cache API
  }
})

// Usage in server routes
export default defineEventHandler(async (event) => {
  const db = hubDatabase()
  const kv = hubKV()
  const blob = hubBlob()

  // Use like regular Cloudflare bindings
  const users = await db.prepare('SELECT * FROM users').all()
})

Environment Variables
# .env (development)
API_SECRET=dev-secret
DATABASE_URL=http://localhost:8787

# Production (Cloudflare)
wrangler secret put API_SECRET
wrangler secret put DATABASE_URL

# Production (Vercel/Netlify)
# Set in dashboard or CLI

Migration from Nuxt 3
Step 1: Update package.json
{
  "devDependencies": {
    "nuxt": "^4.0.0"
  }
}

Step 2: Enable Compatibility Mode
// nuxt.config.ts
export default defineNuxtConfig({
  future: {
    compatibilityVersion: 4
  }
})

Step 3: Move Files to app/
# Create app directory
mkdir app

# Move files
mv components app/
mv composables app/
mv pages app/
mv layouts app/
mv middleware app/
mv plugins app/
mv assets app/
mv app.vue app/
mv error.vue app/

Step 4: Fix Shallow Reactivity
// If mutating data.value properties:
const { data } = await useFetch('/api/user', {
  deep: true  // Enable deep reactivity
})

// Or replace entire value
data.value = { ...data.value, name: 'New Name' }

Step 5: Update Default Values
// v3: data.value is null
// v4: data.value is undefined

// Update null checks
if (data.value === null) // v3
if (!data.value)         // v4 (works for both)

Common Anti-Patterns
Client-Only Code on Server
// WRONG
const width = window.innerWidth

// CORRECT
if (import.meta.client) {
  const width = window.innerWidth
}

// Or use onMounted
onMounted(() => {
  const width = window.innerWidth
})

Non-Deterministic SSR
// WRONG - Different on server vs client
const id = Math.random()
const time = Date.now()

// CORRECT - Use useState for consistency
const id = useState('id', () => Math.random())
const time = useState('time', () => Date.now())

Missing Suspense for Async Components
<!-- WRONG -->
<AsyncComponent />

<!-- CORRECT -->
<Suspense>
  <AsyncComponent />
  <template #fallback>
    <LoadingSpinner />
  </template>
</Suspense>

Troubleshooting

Hydration Mismatch:

Check for window, document, localStorage usage
Wrap in ClientOnly or use onMounted
Look for Math.random(), Date.now(), crypto.randomUUID()

Build Errors:

rm -rf .nuxt .output node_modules/.vite && bun install


Deployment Fails:

Check nitro.preset matches target
Verify environment variables are set
Check wrangler.toml bindings match code

Tests Failing:

Ensure @nuxt/test-utils is installed
Check vitest.config.ts has environment: 'nuxt'
Use mountSuspended for async components
Related Skills
nuxt-core: Project setup, routing, configuration
nuxt-data: Composables, data fetching, state
nuxt-server: Server routes, API patterns
cloudflare-d1: D1 database patterns

Version: 4.0.0 | Last Updated: 2025-12-28 | License: MIT

Weekly Installs
185
Repository
secondsky/claude-skills
GitHub Stars
129
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn
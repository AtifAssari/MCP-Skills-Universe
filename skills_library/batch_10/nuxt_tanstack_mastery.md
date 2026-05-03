---
title: nuxt-tanstack-mastery
url: https://skills.sh/modra40/claude-codex-skills-directory/nuxt-tanstack-mastery
---

# nuxt-tanstack-mastery

skills/modra40/claude-codex-skills-directory/nuxt-tanstack-mastery
nuxt-tanstack-mastery
Installation
$ npx skills add https://github.com/modra40/claude-codex-skills-directory --skill nuxt-tanstack-mastery
SKILL.md
Nuxt 3 + TanStack Query Mastery

Filosofi: "Simplicity is the ultimate sophistication" — Write code that your future self will thank you for.

Core Principles (WAJIB dipatuhi)
┌─────────────────────────────────────────────────────────────────┐
│  1. KISS (Keep It Stupid Simple) - Jangan over-engineer        │
│  2. YAGNI (You Ain't Gonna Need It) - Build for today          │
│  3. DRY (Don't Repeat Yourself) - Tapi jangan premature DRY    │
│  4. Composition over Inheritance - Favor composables           │
│  5. Single Responsibility - One function, one job              │
│  6. Explicit over Implicit - Readable > clever                 │
└─────────────────────────────────────────────────────────────────┘

Quick Decision Matrix
Kebutuhan	Solusi	Referensi
Data fetching + caching	TanStack Query	tanstack-query.md
Global state sederhana	Pinia	state-management.md
Utility functions	VueUse	libraries.md
Form handling	VeeValidate + Zod	libraries.md
Debugging	Vue DevTools + patterns	debugging.md
Folder structure	Feature-based	folder-structure.md
Performance issues	Profiling + lazy load	performance.md
Security concerns	CSP + validation	security.md
Common bugs	Reactivity gotchas	common-pitfalls.md
Reference Files

Baca reference yang relevan berdasarkan kebutuhan:

references/folder-structure.md — Struktur folder production-ready dengan penjelasan setiap direktori
references/tanstack-query.md — TanStack Query patterns, caching strategies, optimistic updates
references/clean-code.md — Clean code principles, naming conventions, composables patterns
references/debugging.md — Debugging techniques, common errors, troubleshooting guide
references/performance.md — Performance optimization, lazy loading, bundle analysis
references/security.md — Security best practices, XSS prevention, auth patterns
references/common-pitfalls.md — Bugs yang sering terjadi dan cara menghindarinya
references/libraries.md — Curated list library terpercaya dengan use cases
references/state-management.md — Pinia patterns, when to use what
references/code-examples.md — Real-world code examples dan patterns
Golden Rules (Cetak dalam otak)
1. Composables adalah Raja
// ❌ JANGAN: Logic di component
const MyComponent = {
  setup() {
    const data = ref([])
    const loading = ref(false)
    const fetchData = async () => { /* ... */ }
    // 50 lines of logic...
  }
}

// ✅ LAKUKAN: Extract ke composable
// composables/useProducts.ts
export function useProducts() {
  const { data, isLoading } = useQuery({ /* ... */ })
  return { products: data, isLoading }
}

// Component menjadi bersih
const { products, isLoading } = useProducts()

2. TypeScript adalah Non-negotiable
// ❌ any = technical debt
const data: any = await fetch()

// ✅ Type everything
interface Product {
  id: string
  name: string
  price: number
}
const data: Product[] = await fetch()

3. Error Boundaries WAJIB ada
<!-- Wrap setiap section dengan error boundary -->
<NuxtErrorBoundary>
  <ProductList />
  <template #error="{ error }">
    <ErrorDisplay :error="error" />
  </template>
</NuxtErrorBoundary>

4. Reactivity dengan Benar
// ❌ Reactivity loss
const { data } = useQuery()
const items = data.value // Loss reactivity!

// ✅ Preserve reactivity
const { data } = useQuery()
const items = computed(() => data.value ?? [])

Project Bootstrap Command
# Nuxt 3 + TanStack Query + Essential tools
npx nuxi@latest init my-app
cd my-app
npm install @tanstack/vue-query @pinia/nuxt @vueuse/nuxt zod @vee-validate/nuxt
npm install -D @nuxt/devtools typescript @types/node

Checklist Sebelum Production
 TypeScript strict mode enabled
 Error boundaries di setiap route
 Loading states untuk semua async operations
 Input validation dengan Zod
 Environment variables di .env (bukan hardcode)
 Bundle size < 200KB initial JS
 Lighthouse score > 90
 Security headers configured
 Rate limiting untuk API calls
 Proper caching strategy dengan TanStack Query
Weekly Installs
29
Repository
modra40/claude-…irectory
GitHub Stars
5
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
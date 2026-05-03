---
rating: ⭐⭐⭐
title: vinext-vite-nextjs
url: https://skills.sh/aradotso/trending-skills/vinext-vite-nextjs
---

# vinext-vite-nextjs

skills/aradotso/trending-skills/vinext-vite-nextjs
vinext-vite-nextjs
Installation
$ npx skills add https://github.com/aradotso/trending-skills --skill vinext-vite-nextjs
SKILL.md
vinext — Next.js API on Vite, Deploy Anywhere

Skill by ara.so — Daily 2026 Skills collection.

vinext is a Vite plugin that reimplements the Next.js public API surface (routing, SSR, RSC, next/* imports, CLI) so existing Next.js apps run on Vite instead of the Next.js compiler. It targets ~94% API coverage, supports both Pages Router and App Router, and deploys natively to Cloudflare Workers with optional Nitro support for AWS, Netlify, Vercel, and more.

Installation
New project (migrate from Next.js)
# Automated one-command migration
npx vinext init


This will:

Run compatibility check (vinext check)
Install vite, @vitejs/plugin-react as devDependencies
Install @vitejs/plugin-rsc, react-server-dom-webpack for App Router
Add "type": "module" to package.json
Rename CJS config files (e.g. postcss.config.js → postcss.config.cjs)
Add dev:vinext and build:vinext scripts
Generate a minimal vite.config.ts

Migration is non-destructive — Next.js still works alongside vinext.

Manual installation
npm install -D vinext vite @vitejs/plugin-react

# App Router only:
npm install -D @vitejs/plugin-rsc react-server-dom-webpack


Update package.json scripts:

{
  "scripts": {
    "dev": "vinext dev",
    "build": "vinext build",
    "start": "vinext start",
    "deploy": "vinext deploy"
  }
}

Agent Skill (AI-assisted migration)
npx skills add cloudflare/vinext
# Then in your AI tool: "migrate this project to vinext"

CLI Reference
Command	Description
vinext dev	Start dev server with HMR
vinext build	Production build
vinext start	Local production server for testing
vinext deploy	Build + deploy to Cloudflare Workers
vinext init	Automated migration from Next.js
vinext check	Scan for compatibility issues before migrating
vinext lint	Delegate to eslint or oxlint
CLI Options
vinext dev -p 3001 -H 0.0.0.0
vinext deploy --preview
vinext deploy --env staging --name my-app
vinext deploy --skip-build --dry-run
vinext deploy --experimental-tpr
vinext init --port 3001 --skip-check --force

Configuration

vinext auto-detects app/ or pages/ directory and loads next.config.js automatically. No vite.config.ts is required for basic usage.

Minimal vite.config.ts
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { vinext } from 'vinext/vite'

export default defineConfig({
  plugins: [
    react(),
    vinext(),
  ],
})

App Router vite.config.ts
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import rsc from '@vitejs/plugin-rsc'
import { vinext } from 'vinext/vite'

export default defineConfig({
  plugins: [
    react(),
    rsc(),
    vinext(),
  ],
})

Cloudflare Workers with bindings
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { vinext } from 'vinext/vite'
import { cloudflare } from '@cloudflare/vite-plugin'

export default defineConfig({
  plugins: [
    cloudflare(),
    react(),
    vinext(),
  ],
})

Other platforms via Nitro
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { vinext } from 'vinext/vite'
import nitro from 'vite-plugin-nitro'

export default defineConfig({
  plugins: [
    react(),
    vinext(),
    nitro({ preset: 'vercel' }), // or 'netlify', 'aws-amplify', 'deno-deploy', etc.
  ],
})

Project Structure

vinext uses the same directory conventions as Next.js — no changes required:

my-app/
├── app/                  # App Router (auto-detected)
│   ├── layout.tsx
│   ├── page.tsx
│   └── api/route.ts
├── pages/                # Pages Router (auto-detected)
│   ├── index.tsx
│   └── api/hello.ts
├── public/               # Static assets
├── next.config.js        # Loaded automatically
├── package.json
└── vite.config.ts        # Optional for basic usage

Code Examples
Pages Router — SSR page
// pages/index.tsx
import type { GetServerSideProps, InferGetServerSidePropsType } from 'next'

type Props = { data: string }

export const getServerSideProps: GetServerSideProps<Props> = async (ctx) => {
  return { props: { data: 'Hello from SSR' } }
}

export default function Home({ data }: InferGetServerSidePropsType<typeof getServerSideProps>) {
  return <h1>{data}</h1>
}

Pages Router — Static generation
// pages/posts/[id].tsx
import type { GetStaticPaths, GetStaticProps } from 'next'

export const getStaticPaths: GetStaticPaths = async () => {
  return {
    paths: [{ params: { id: '1' } }, { params: { id: '2' } }],
    fallback: false,
  }
}

export const getStaticProps: GetStaticProps = async ({ params }) => {
  return { props: { id: params?.id } }
}

export default function Post({ id }: { id: string }) {
  return <p>Post {id}</p>
}

Pages Router — API route
// pages/api/hello.ts
import type { NextApiRequest, NextApiResponse } from 'next'

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  res.status(200).json({ message: 'Hello from vinext' })
}

App Router — Server Component
// app/page.tsx
export default async function Page() {
  const data = await fetch('https://api.example.com/data').then(r => r.json())
  return <main>{data.title}</main>
}

App Router — Route Handler
// app/api/route.ts
import { NextRequest, NextResponse } from 'next/server'

export async function GET(request: NextRequest) {
  return NextResponse.json({ status: 'ok' })
}

export async function POST(request: NextRequest) {
  const body = await request.json()
  return NextResponse.json({ received: body })
}

App Router — Server Action
// app/actions.ts
'use server'

export async function submitForm(formData: FormData) {
  const name = formData.get('name')
  // server-side logic here
  return { success: true, name }
}

// app/form.tsx
'use client'
import { submitForm } from './actions'

export function Form() {
  return (
    <form action={submitForm}>
      <input name="name" />
      <button type="submit">Submit</button>
    </form>
  )
}

Middleware
// middleware.ts
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

export function middleware(request: NextRequest) {
  const token = request.cookies.get('token')
  if (!token && request.nextUrl.pathname.startsWith('/dashboard')) {
    return NextResponse.redirect(new URL('/login', request.url))
  }
  return NextResponse.next()
}

export const config = {
  matcher: ['/dashboard/:path*'],
}

Cloudflare Workers — Bindings access
// app/api/kv/route.ts
import { NextRequest, NextResponse } from 'next/server'
import { getCloudflareContext } from 'cloudflare:workers'

export async function GET(request: NextRequest) {
  const { env } = getCloudflareContext()
  const value = await env.MY_KV.get('key')
  return NextResponse.json({ value })
}

Image optimization
// app/page.tsx
import Image from 'next/image'

export default function Page() {
  return (
    <Image
      src="/hero.png"
      alt="Hero"
      width={800}
      height={400}
      priority
    />
  )
}

Link and navigation
// app/nav.tsx
'use client'
import Link from 'next/link'
import { useRouter, usePathname } from 'next/navigation'

export function Nav() {
  const router = useRouter()
  const pathname = usePathname()

  return (
    <nav>
      <Link href="/">Home</Link>
      <Link href="/about">About</Link>
      <button onClick={() => router.push('/dashboard')}>Dashboard</button>
    </nav>
  )
}

Deployment
Cloudflare Workers
# Authenticate (once)
wrangler login

# Deploy
vinext deploy

# Deploy to preview
vinext deploy --preview

# Deploy to named environment
vinext deploy --env production --name my-production-app


For CI/CD, set CLOUDFLARE_API_TOKEN environment variable instead of wrangler login.

wrangler.toml (Cloudflare config)
name = "my-app"
compatibility_date = "2024-01-01"
compatibility_flags = ["nodejs_compat"]

[[kv_namespaces]]
binding = "MY_KV"
id = "your-kv-namespace-id"

[[r2_buckets]]
binding = "MY_BUCKET"
bucket_name = "my-bucket"

Netlify / Vercel / AWS via Nitro
npm install -D vite-plugin-nitro

# Then add nitro plugin to vite.config.ts with your target preset
# nitro({ preset: 'netlify' })
# nitro({ preset: 'vercel' })
# nitro({ preset: 'aws-amplify' })

next.config.js Support

vinext loads your existing next.config.js automatically:

// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    remotePatterns: [
      { protocol: 'https', hostname: 'images.example.com' },
    ],
  },
  env: {
    MY_VAR: process.env.MY_VAR,
  },
  redirects: async () => [
    { source: '/old', destination: '/new', permanent: true },
  ],
  rewrites: async () => [
    { source: '/api/:path*', destination: 'https://backend.example.com/:path*' },
  ],
}

module.exports = nextConfig

Compatibility Check

Run before migrating to identify unsupported features:

npx vinext check


This scans for:

Unsupported next.config.js options
Deprecated Pages Router APIs
Experimental Next.js features not yet supported
CJS config file conflicts
Common Patterns
Environment variables

Works the same as Next.js — .env, .env.local, .env.production:

# .env.local
NEXT_PUBLIC_API_URL=https://api.example.com
DATABASE_URL=$DATABASE_URL

// Accessible in client code (NEXT_PUBLIC_ prefix)
const apiUrl = process.env.NEXT_PUBLIC_API_URL

// Server-only
const dbUrl = process.env.DATABASE_URL

TypeScript path aliases
// tsconfig.json — works as-is
{
  "compilerOptions": {
    "paths": {
      "@/*": ["./src/*"]
    }
  }
}

Tailwind CSS
npm install -D tailwindcss postcss autoprefixer
# Rename postcss.config.js → postcss.config.cjs (vinext init does this automatically)

// postcss.config.cjs
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}

Troubleshooting
ESM conflicts with CJS config files
# vinext init handles this automatically, or rename manually:
mv postcss.config.js postcss.config.cjs
mv tailwind.config.js tailwind.config.cjs


Ensure package.json has "type": "module".

vinext init overwrites existing vite.config.ts
vinext init --force

Skip compatibility check during init
vinext init --skip-check

Custom port
vinext dev -p 3001
vinext init --port 3001

wrangler not authenticated for deploy
wrangler login
# or set env var:
export CLOUDFLARE_API_TOKEN=your_token_here

Dry-run deploy to verify config
vinext deploy --dry-run

App Router multi-environment build issues

App Router builds produce three environments (RSC + SSR + client). If you see build errors, ensure all three plugins are installed:

npm install -D @vitejs/plugin-rsc react-server-dom-webpack


And your vite.config.ts includes both react() and rsc() plugins in the correct order.

What's Supported (~94% of Next.js API)
✅ Pages Router (SSR, SSG, ISR, API routes)
✅ App Router (RSC, Server Actions, Route Handlers, Layouts, Loading, Error boundaries)
✅ Middleware
✅ next/image, next/link, next/router, next/navigation, next/head
✅ next/font, next/dynamic
✅ next.config.js (redirects, rewrites, headers, env, images)
✅ Cloudflare Workers native deployment with bindings
✅ HMR in development
✅ TypeScript, Tailwind CSS, CSS Modules
⚠️ Experimental Next.js features — lower priority
❌ Undocumented Vercel-specific behavior — intentionally not supported
Weekly Installs
1.1K
Repository
aradotso/trending-skills
GitHub Stars
42
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
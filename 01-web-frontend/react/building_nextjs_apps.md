---
title: building-nextjs-apps
url: https://skills.sh/bilalmk/todo_correct/building-nextjs-apps
---

# building-nextjs-apps

skills/bilalmk/todo_correct/building-nextjs-apps
building-nextjs-apps
Installation
$ npx skills add https://github.com/bilalmk/todo_correct --skill building-nextjs-apps
SKILL.md
Next.js 16 Applications

Build Next.js 16 applications correctly with distinctive design.

Critical Breaking Changes (Next.js 16)
1. params and searchParams are Now Promises

THIS IS THE MOST COMMON MISTAKE.

// WRONG - Next.js 15 pattern (WILL FAIL)
export default function Page({ params }: { params: { id: string } }) {
  return <div>ID: {params.id}</div>
}

// CORRECT - Next.js 16 pattern
export default async function Page({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params
  return <div>ID: {id}</div>
}

2. Client Components Need use() Hook
"use client"
import { use } from "react"

export default function ClientPage({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = use(params)
  return <div>ID: {id}</div>
}

3. searchParams Also Async
export default async function Page({
  searchParams,
}: {
  searchParams: Promise<{ page?: string }>
}) {
  const { page } = await searchParams
  return <div>Page: {page ?? "1"}</div>
}

Core Patterns
Project Setup
npx create-next-app@latest my-app --typescript --tailwind --eslint
cd my-app

# Add shadcn/ui
npx shadcn@latest init
npx shadcn@latest add button form dialog table sidebar

App Router Layout
// app/layout.tsx
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className="min-h-screen">
        {children}
      </body>
    </html>
  )
}

Dynamic Routes
// app/tasks/[id]/page.tsx
export default async function TaskPage({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params
  const task = await getTask(id)

  return (
    <main>
      <h1>{task.title}</h1>
    </main>
  )
}

Server Actions
// app/actions.ts
"use server"

import { revalidatePath } from "next/cache"

export async function createTask(formData: FormData) {
  const title = formData.get("title") as string

  await db.insert(tasks).values({ title })

  revalidatePath("/tasks")
}

// Usage in component
<form action={createTask}>
  <input name="title" />
  <button type="submit">Create</button>
</form>

API Routes
// app/api/tasks/route.ts
import { NextResponse } from "next/server"

export async function GET() {
  const tasks = await db.select().from(tasksTable)
  return NextResponse.json(tasks)
}

export async function POST(request: Request) {
  const body = await request.json()
  const task = await db.insert(tasksTable).values(body).returning()
  return NextResponse.json(task, { status: 201 })
}

Middleware → proxy.ts
// proxy.ts (replaces middleware.ts in Next.js 16)
import { NextRequest } from "next/server"

export function proxy(request: NextRequest) {
  // Authentication check
  const token = request.cookies.get("token")
  if (!token && request.nextUrl.pathname.startsWith("/dashboard")) {
    return Response.redirect(new URL("/login", request.url))
  }
}

export const config = {
  matcher: ["/dashboard/:path*"],
}

Data Fetching
Server Component (Default)
// This runs on the server - can use async/await directly
async function TaskList() {
  const tasks = await fetch("https://api.example.com/tasks", {
    cache: "no-store", // SSR, or
    // next: { revalidate: 60 } // ISR
  }).then(r => r.json())

  return (
    <ul>
      {tasks.map(task => <li key={task.id}>{task.title}</li>)}
    </ul>
  )
}

Client Component
"use client"

import useSWR from "swr"

const fetcher = (url: string) => fetch(url).then(r => r.json())

export function ClientTaskList() {
  const { data, error, isLoading } = useSWR("/api/tasks", fetcher)

  if (isLoading) return <div>Loading...</div>
  if (error) return <div>Error loading tasks</div>

  return (
    <ul>
      {data.map(task => <li key={task.id}>{task.title}</li>)}
    </ul>
  )
}

Project Structure
app/
├── layout.tsx           # Root layout
├── page.tsx             # Home page
├── globals.css          # Global styles
├── api/                 # API routes
│   └── tasks/route.ts
├── tasks/
│   ├── page.tsx         # /tasks
│   └── [id]/page.tsx    # /tasks/:id
├── actions.ts           # Server actions
└── proxy.ts             # Request proxy (middleware)
components/
├── ui/                  # shadcn/ui components
└── task-list.tsx        # App components
lib/
├── db.ts                # Database connection
└── utils.ts             # Utilities

Next.js DevTools MCP

Use the next-devtools-mcp server for runtime diagnostics and development automation.

Setup
claude mcp add next-devtools npx next-devtools-mcp@latest


Or in settings.json:

{
  "mcpServers": {
    "next-devtools": {
      "type": "stdio",
      "command": "npx",
      "args": ["next-devtools-mcp@latest"]
    }
  }
}

Available Tools
Tool	Purpose
init	Establish context with available tools and best practices
nextjs_docs	Search and fetch official Next.js documentation
browser_eval	Automate browser testing with Playwright
nextjs_index	Discover running Next.js dev servers
nextjs_call	Execute MCP tools on running dev servers
upgrade_nextjs_16	Automated upgrade with codemods
enable_cache_components	Configure Cache Components for Next.js 16
Key Use Cases

1. Get Real-time Errors

"What build errors are there in my Next.js app?"
"Show me TypeScript errors in the current project"


2. Debug Runtime Issues

"Check the dev server logs for errors"
"What runtime errors are happening on the dashboard page?"


3. Upgrade Assistance

"Upgrade this project to Next.js 16"
"Enable cache components for this app"


4. Documentation Lookup

"How do I use the Image component in Next.js 16?"
"What's the correct way to handle dynamic routes?"

Next.js 16 MCP Endpoint

Next.js 16+ exposes a built-in MCP endpoint at http://localhost:3000/_next/mcp (or your dev server port). The devtools MCP automatically discovers and connects to running servers.

Verification

Run: python3 scripts/verify.py

Expected: ✓ building-nextjs-apps skill ready

If Verification Fails
Check: references/ folder has nextjs-16-patterns.md
Stop and report if still failing
Related Skills
styling-with-shadcn - UI components for Next.js apps
fetching-library-docs - Latest Next.js docs: --library-id /vercel/next.js --topic routing
configuring-better-auth - OAuth/SSO for Next.js apps
References
references/nextjs-16-patterns.md - Complete Next.js 16 patterns
references/frontend-design.md - Aesthetic guidelines for distinctive UI
references/datetime-patterns.md - UTC/timezone handling for datetime-local inputs
Weekly Installs
16
Repository
bilalmk/todo_correct
GitHub Stars
1
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass
---
rating: ⭐⭐
title: clerk-tanstack-patterns
url: https://skills.sh/clerk/skills/clerk-tanstack-patterns
---

# clerk-tanstack-patterns

skills/clerk/skills/clerk-tanstack-patterns
clerk-tanstack-patterns
Installation
$ npx skills add https://github.com/clerk/skills --skill clerk-tanstack-patterns
SKILL.md
TanStack React Start Patterns
What Do You Need?
Task	Reference
Protect routes with beforeLoad	references/router-guards.md
Auth in createServerFn	references/server-functions.md
Pass auth to loaders	references/loaders.md
Configure Vinxi + clerkMiddleware	references/vinxi-server.md
References
Reference	Description
references/router-guards.md	beforeLoad auth redirect
references/server-functions.md	createServerFn with auth()
references/loaders.md	Auth context in loaders
references/vinxi-server.md	clerkMiddleware() setup
Setup
npm install @clerk/tanstack-react-start


.env:

CLERK_PUBLISHABLE_KEY=pk_...
CLERK_SECRET_KEY=sk_...


src/start.ts (Vinxi entry):

import { clerkMiddleware } from '@clerk/tanstack-react-start/server'
import { createStart } from '@tanstack/react-start'

export const startInstance = createStart(() => {
  return {
    requestMiddleware: [clerkMiddleware()],
  }
})


src/routes/__root.tsx — wrap with <ClerkProvider>:

import { ClerkProvider } from '@clerk/tanstack-react-start'

function RootDocument({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <ClerkProvider>
          {children}
        </ClerkProvider>
      </body>
    </html>
  )
}

Mental Model

TanStack Start runs on Vinxi. Auth flows through two layers:

Server layer — createServerFn + auth() from @clerk/tanstack-react-start/server
Router layer — beforeLoad on route definitions, throws redirect for unauthenticated

Both layers are server-executed. Client hooks (useAuth, useUser) are React hooks for the browser side.

Minimal Pattern
import { createFileRoute, redirect } from '@tanstack/react-router'
import { createServerFn } from '@tanstack/react-start'
import { auth } from '@clerk/tanstack-react-start/server'

const authStateFn = createServerFn().handler(async () => {
  const { isAuthenticated, userId } = await auth()
  if (!isAuthenticated) {
    throw redirect({ to: '/sign-in' })
  }
  return { userId }
})

export const Route = createFileRoute('/dashboard')({
  beforeLoad: async () => await authStateFn(),
})

Common Pitfalls
Symptom	Cause	Fix
auth() returns empty	Missing clerkMiddleware in start.ts	Add to requestMiddleware array
redirect not thrown	Using return instead of throw	throw redirect(...) in TanStack
Wrong import for auth	Mixing client/server imports	Server: @clerk/tanstack-react-start/server
Loader context missing userId	Not passing from beforeLoad	Return from beforeLoad, access via context
ClerkProvider missing	Forgot root wrapping	Add to __root.tsx shell component
See Also
clerk-setup - Initial Clerk install
clerk-custom-ui - Custom flows & appearance
clerk-orgs - B2B organizations
Docs

TanStack React Start SDK

Weekly Installs
995
Repository
clerk/skills
GitHub Stars
40
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
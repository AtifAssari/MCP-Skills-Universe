---
title: clerk-react-router-patterns
url: https://skills.sh/clerk/skills/clerk-react-router-patterns
---

# clerk-react-router-patterns

skills/clerk/skills/clerk-react-router-patterns
clerk-react-router-patterns
Installation
$ npx skills add https://github.com/clerk/skills --skill clerk-react-router-patterns
SKILL.md
React Router Patterns

SDK: @clerk/react-router v3+. Requires React Router v7.9+.

What Do You Need?
Task	Reference
Auth in loaders and actions	references/loaders-actions.md
Protected routes and redirects	references/protected-routes.md
SSR user data and session	references/ssr-auth.md
Mental Model

React Router v7 uses a middleware + loader pipeline. Clerk plugs into both layers:

Middleware (clerkMiddleware()) — runs on every request, attaches auth to context
rootAuthLoader — required in root.tsx to pass Clerk state to the client
getAuth(args) — called inside any loader/action to get the current user
Request → clerkMiddleware() → rootAuthLoader → page loader → component
                 ↓                   ↓               ↓
           attaches auth      injects state     getAuth(args)
           to context         to response       reads context

Minimal Setup
1. root.tsx
import { rootAuthLoader } from '@clerk/react-router/server'
import { ClerkApp } from '@clerk/react-router'
import type { Route } from './+types/root'

export async function loader(args: Route.LoaderArgs) {
  return rootAuthLoader(args)
}

export default ClerkApp(function App() {
  return <Outlet />
})

2. Middleware (root route or entry.server.ts)
import { clerkMiddleware } from '@clerk/react-router/server'
export const middleware = [clerkMiddleware()]


Required: rootAuthLoader must be called in root.tsx's loader. Without it, getAuth throws in nested loaders.

Auth in Loaders
import { getAuth } from '@clerk/react-router/server'
import type { Route } from './+types/dashboard'

export async function loader(args: Route.LoaderArgs) {
  const { userId } = await getAuth(args)
  if (!userId) throw redirect('/sign-in')

  const data = await fetchUserData(userId)
  return { data }
}

Auth in Actions
import { getAuth } from '@clerk/react-router/server'

export async function action(args: Route.ActionArgs) {
  const { userId, orgId } = await getAuth(args)
  if (!userId) throw new Response('Unauthorized', { status: 401 })

  const formData = await args.request.formData()
  await saveData(userId, orgId, formData)
  return redirect('/dashboard')
}

Client Components
import { useAuth, useUser } from '@clerk/react-router'

export function Profile() {
  const { userId, isSignedIn } = useAuth()
  const { user } = useUser()
  if (!isSignedIn) return null
  return <p>{user?.firstName}</p>
}

Org Switching
import { OrganizationSwitcher } from '@clerk/react-router'

export function Nav() {
  return <OrganizationSwitcher afterSelectOrganizationUrl="/dashboard" />
}

export async function loader(args: Route.LoaderArgs) {
  const { userId, orgId } = await getAuth(args)
  if (!userId) throw redirect('/sign-in')
  if (!orgId) throw redirect('/select-org')

  return { data: await fetchOrgData(orgId) }
}

Common Pitfalls
Symptom	Cause	Fix
clerkMiddleware() not detected	Missing middleware	Export middleware = [clerkMiddleware()] from root route
getAuth returns empty userId	rootAuthLoader not called	Call rootAuthLoader(args) in root.tsx loader
Infinite redirect loop	Redirect target is also protected	Exclude /sign-in from protection check
redirect not working in action	Using Response instead of throw redirect()	Use throw redirect('/path') from react-router
Import Map
What	Import From
getAuth	@clerk/react-router/server
rootAuthLoader	@clerk/react-router/server
clerkMiddleware	@clerk/react-router/server
ClerkApp	@clerk/react-router
useAuth, useUser	@clerk/react-router
OrganizationSwitcher	@clerk/react-router
See Also
clerk-setup - Initial Clerk install
clerk-custom-ui - Custom flows & appearance
clerk-orgs - B2B organizations
Docs

React Router SDK

Weekly Installs
994
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
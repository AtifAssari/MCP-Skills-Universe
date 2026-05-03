---
title: clerk-vue-patterns
url: https://skills.sh/clerk/skills/clerk-vue-patterns
---

# clerk-vue-patterns

skills/clerk/skills/clerk-vue-patterns
clerk-vue-patterns
Installation
$ npx skills add https://github.com/clerk/skills --skill clerk-vue-patterns
SKILL.md
Vue Patterns

SDK: @clerk/vue v2+ (Vue 3). For Nuxt, use clerk-nuxt-patterns.

What Do You Need?
Task	Reference
Composables: useAuth, useUser, useOrganization	references/composables.md
Vue Router navigation guards	references/vue-router-guards.md
Pinia store with auth state	references/pinia-integration.md
Mental Model

Vue uses composables from @clerk/vue:

useAuth() — reactive isSignedIn, userId, signOut
useUser() — reactive user object
useClerk() — full Clerk instance for advanced operations
useOrganization() — reactive organization, membership
Setup
Vue (Plain)
// main.ts
import { clerkPlugin } from '@clerk/vue'
import { createApp } from 'vue'
import App from './App.vue'

const app = createApp(App)
app.use(clerkPlugin, {
  publishableKey: import.meta.env.VITE_CLERK_PUBLISHABLE_KEY,
})
app.mount('#app')

Composables Usage
<script setup lang="ts">
import { useAuth, useUser } from '@clerk/vue'

const { isSignedIn, userId, signOut } = useAuth()
const { user } = useUser()
</script>

<template>
  <div v-if="isSignedIn">
    <p>Hello {{ user?.firstName }}</p>
    <button @click="signOut()">Sign Out</button>
  </div>
  <SignInButton v-else />
</template>

Org Switching
<script setup lang="ts">
import { useOrganizationList } from '@clerk/vue'

const { userMemberships, setActive } = useOrganizationList()
</script>

<template>
  <button
    v-for="mem in userMemberships.data ?? []"
    :key="mem.organization.id"
    @click="setActive({ organization: mem.organization.id })"
  >
    {{ mem.organization.name }}
  </button>
</template>

Common Pitfalls
Symptom	Cause	Fix
Composables return undefined	Not inside ClerkProvider tree	Ensure app.use(clerkPlugin, { publishableKey }) is called
userId reactive but not updating	Destructuring loses reactivity	Use const { userId } = useAuth() (toRefs-style composable, reactive)
Import Map
What	Import
Composables	@clerk/vue
Plugin setup	@clerk/vue
Components	@clerk/vue
See Also
clerk-setup - Initial Clerk install
clerk-custom-ui - Custom flows & appearance
clerk-orgs - B2B organizations
Docs
Vue SDK
Weekly Installs
853
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
---
title: inertia
url: https://skills.sh/1naichii/ai-code-tools/inertia
---

# inertia

skills/1naichii/ai-code-tools/inertia
inertia
Installation
$ npx skills add https://github.com/1naichii/ai-code-tools --skill inertia
SKILL.md
Inertia.js

Modern monolith framework for building SPAs without APIs. Combine server-side framework power with React/Vue/Svelte frontends.

Core Concept

Inertia replaces your view layer - controllers return JavaScript page components instead of server-side templates. The <Link> component intercepts clicks for XHR visits, providing SPA experience without full page reloads.

Quick Reference
Basic Page Structure
<script setup>
import Layout from './Layout'
import { Head } from '@inertiajs/vue3'
defineProps({ user: Object })
</script>

<template>
    <Layout>
        <Head title="Welcome" />
        <h1>Welcome {{ user.name }}</h1>
    </Layout>
</template>

Navigation
<Link href="/users">Users</Link>
<Link href="/logout" method="post" as="button">Logout</Link>
<Link href="/search" :data="{ query }" preserve-state>Search</Link>

Form Submission
<!-- Simple Form Component -->
<Form action="/users" method="post">
    <input type="text" name="name" />
    <button type="submit">Create</button>
</Form>

<!-- useForm Hook -->
<script setup>
import { useForm } from '@inertiajs/vue3'
const form = useForm({ name: '', email: '' })
function submit() { form.post('/users') }
</script>

Documentation by Topic
Topic	Reference File	Description
Forms	forms.md	Form component, useForm helper, validation, error handling
Links & Navigation	links.md	Link component, manual visits, active states
Validation	validation.md	Server-side validation, error bags, error display
Pages & Layouts	pages-layouts.md	Page components, persistent layouts, default layouts
Data & Props	data-props.md	Shared data, partial reloads, deferred props
Authentication	authentication.md	Auth patterns, CSRF protection, authorization
Setup	setup.md	Client-side initialization, server-side setup
Advanced	advanced.md	Events, error handling, scroll management, SSR
Common Patterns
Displaying Validation Errors
<div v-if="errors.email">{{ errors.email }}</div>

Accessing Shared Data
<script setup>
import { usePage } from '@inertiajs/vue3'
const page = usePage()
const user = computed(() => page.props.auth?.user)
</script>

Preserving State/Scroll
<Link href="/form" preserve-state preserve-scroll>Edit</Link>

Partial Reloads
<Link :only="['users']">Refresh Users</Link>
router.visit('/users', { only: ['users'] })

Framework Support
Client: Vue 3 (@inertiajs/vue3), React (@inertiajs/react), Svelte (@inertiajs/svelte)
Server: Laravel (official), Rails, Phoenix, Symfony (community adapters)
Weekly Installs
12
Repository
1naichii/ai-code-tools
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
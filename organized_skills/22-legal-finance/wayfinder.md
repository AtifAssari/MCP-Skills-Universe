---
rating: ⭐⭐
title: wayfinder
url: https://skills.sh/markhamsquareventures/essentials/wayfinder
---

# wayfinder

skills/markhamsquareventures/essentials/wayfinder
wayfinder
Installation
$ npx skills add https://github.com/markhamsquareventures/essentials --skill wayfinder
SKILL.md
Wayfinder
Instructions

Wayfinder generates TypeScript functions and types for Laravel controllers and routes which you can import into your client side code. It provides type safety and automatic synchronization between backend routes and frontend code.

Development Guidelines
Always Prefer named imports for tree-shaking (e.g., import { show } from '@/actions/...')
Avoid default controller imports (prevents tree-shaking)
Run php artisan wayfinder:generate after route changes if there are any errors
Feature Overview
Form Support: Use .form() with --with-form flag for HTML form attributes — <form {...store.form()}> → action="/posts" method="post"
HTTP Methods: Call .get(), .post(), .patch(), .put(), .delete() for specific methods — show.head(1) → { url: "/posts/1", method: "head" }
Invokable Controllers: Import and invoke directly as functions. For example, import StorePost from '@/actions/.../StorePostController'; StorePost()
Named Routes: Import from @/routes/ for non-controller routes. For example, import { show } from '@/routes/post'; show(1) for route name post.show
Parameter Binding: Detects route keys (e.g., {post:slug}) and accepts matching object properties — show("my-post") or show({ slug: "my-post" })
Query Merging: Use mergeQuery to merge with window.location.search, set values to null to remove — show(1, { mergeQuery: { page: 2, sort: null } })
Query Parameters: Pass { query: {...} } in options to append params — show(1, { query: { page: 1 } }) → "/posts/1?page=1"
Route Objects: Functions return { url, method } shaped objects — show(1) → { url: "/posts/1", method: "get" }
URL Extraction: Use .url() to get URL string — show.url(1) → "/posts/1"
Examples
// Get route object with URL and method...
show(1) // { url: "/posts/1", method: "get" }

// Get just the URL...
show.url(1) // "/posts/1"

// Use specific HTTP methods...
show.get(1) // { url: "/posts/1", method: "get" }
show.head(1) // { url: "/posts/1", method: "head" }

// Import named routes...
import { show as postShow } from '@/routes/post' // For route name 'post.show'
postShow(1) // { url: "/posts/1", method: "get" }

Wayfinder + Inertia

If your application uses the <Form> component from Inertia, you can use Wayfinder to generate form action and method automatically.

Weekly Installs
29
Repository
markhamsquareve…sentials
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
---
rating: ⭐⭐
title: astro-framework
url: https://skills.sh/delineas/astro-framework-agents/astro-framework
---

# astro-framework

skills/delineas/astro-framework-agents/astro-framework
astro-framework
Installation
$ npx skills add https://github.com/delineas/astro-framework-agents --skill astro-framework
Summary

Fast, content-driven websites with selective JavaScript hydration and hybrid rendering strategies.

Islands architecture with fine-grained hydration control via client:load, client:idle, client:visible, and server:defer for deferred server rendering
Content Layer API with glob/file loaders and live loaders for managing collections; type-safe schemas with Zod validation
Hybrid output mode supporting static pages, on-demand SSR, server islands for personalized content, and adapters for Node, Vercel, Netlify, and Cloudflare
Built-in support for view transitions, server-side sessions, type-safe environment variables via astro:env, i18n routing, and form actions
Framework integrations for React, Vue, Svelte, and Solid with automatic image optimization and scoped CSS
SKILL.md
Astro Framework Specialist

Senior Astro specialist with deep expertise in islands architecture, content-driven websites, and hybrid rendering strategies.

Role Definition

You are a senior frontend engineer with extensive Astro experience. You specialize in building fast, content-focused websites using Astro's islands architecture, content collections, and hybrid rendering. You understand when to ship JavaScript and when to keep things static.

When to Use This Skill

Activate this skill when:

Building content-driven websites (blogs, docs, marketing sites)
Implementing islands architecture with selective hydration
Using server islands (server:defer) for deferred server rendering
Creating content collections with the Content Layer API (loaders, glob, file)
Setting up SSR with adapters (Node, Vercel, Netlify, Cloudflare)
Building API endpoints and server actions
Implementing view transitions for SPA-like navigation
Managing server-side sessions for user state
Configuring type-safe environment variables with astro:env
Setting up i18n routing for multilingual sites
Integrating UI frameworks (React, Vue, Svelte, Solid)
Optimizing images and performance
Configuring astro.config.mjs
Building live data collections with Live Loaders
Core Workflow
Analyze requirements → Identify static vs dynamic content, hydration needs, data sources
Design structure → Plan pages, layouts, components, content collections with loaders
Implement components → Create Astro components with proper client/server directives
Configure routing → Set up file-based routing, dynamic routes, endpoints, i18n
Optimize delivery → Configure adapters, image optimization, view transitions, caching
Expert Decision Frameworks
Output Mode Selection
static (default)
├── Blog, docs, landing pages, portfolios
├── Content changes per-deploy, not per-request
├── <500 pages and builds under 5 min
└── No user-specific content needed

hybrid (80% of real-world projects)
├── Mostly static + login/dashboard/API routes
├── E-commerce: static catalog + dynamic cart/checkout
├── Use server islands to avoid making whole pages SSR
└── Best balance of performance + flexibility

server (rarely needed)
├── >80% of pages need request data (cookies, headers, DB)
├── Full SaaS/dashboard behind auth
└── Warning: you lose edge HTML caching on all pages


Signs you picked wrong:

Builds >10 min with getStaticPaths → switch to hybrid
Using prerender = false on >50% of pages → switch to server
Whole app is server but only 2 pages read cookies → switch to hybrid
Hydration Strategy — Common Mistakes
client:visible on hero/header → It's already in viewport at load time, so it hydrates immediately anyway. Use client:load directly and skip the IntersectionObserver overhead.
client:idle on mobile → requestIdleCallback on low-RAM devices can take 10+ seconds. For anything the user might interact with in the first 5 seconds, use client:load.
Large React component with client:load → If bundle >50KB, consider splitting: render the static shell in Astro, hydrate only the interactive part. Or use client:idle if it's below the fold.
Hydrating navbars/footers → If the only interactivity is a mobile menu toggle, write it in vanilla JS inside a <script> tag instead of hydrating an entire React component.
Server Islands vs Client Islands vs Static
Does the component need data from the server on EACH request?
(cookies, user session, DB query, personalization)
│
├── Yes → server:defer (Server Island)
│   ├── User avatars, greeting bars, cart counts
│   ├── Personalized recommendations on product pages
│   └── A/B test variants resolved server-side
│
└── No → Does it need browser interactivity?
    │
    ├── Yes → client:* directive (Client Island)
    │   ├── Search boxes, forms with validation
    │   ├── Image carousels, interactive charts
    │   └── Anything needing onClick/onChange/state
    │
    └── No → No directive (Static HTML, zero JS)
        ├── Navigation, footers, content sections
        ├── Cards, lists, formatted text
        └── This should be ~90% of most sites


The e-commerce pattern: Product page is static (title, images, description) + server:defer for price/stock (changes often) + client:load for add-to-cart button (needs interactivity). Three rendering strategies on one page.

When NOT to Use Astro

Astro excels at content-heavy sites with islands of interactivity. Consider other frameworks when:

The app is a full SPA with client-side routing and heavy state (→ Next.js, SvelteKit, Remix)
Real-time collaborative features are core (→ Next.js + WebSockets)
Every page is behind auth with no public content (→ SPA framework)
You need React Server Components (→ Next.js)
Content Collections — Loader Selection
Local markdown/MDX files → glob() loader
Single JSON/YAML data file → file() loader
Remote API/CMS data at build time → Custom async loader function
Remote data that must be fresh per-request → Live Loader (Astro 6+)


Performance tip: For sites with >1000 content entries, use glob() with retainBody: false if you don't need raw markdown body — significantly reduces data store size.

Reference Documentation

Load detailed guidance based on your current task:

Topic	Reference	When to Load
Components	references/components.md	Writing Astro components, Props, slots, expressions
Client Directives	references/client-directives.md	Hydration strategies, client:load, client:visible, client:idle
Content Collections	references/content-collections.md	Content Layer API, loaders, schemas, getCollection, getEntry, live loaders
Routing	references/routing.md	Pages, dynamic routes, endpoints, redirects
SSR & Adapters	references/ssr-adapters.md	On-demand rendering, adapters, server islands, sessions
Server Islands	references/server-islands.md	server:defer, fallback content, deferred rendering
Sessions	references/sessions.md	Astro.session, server-side state, shopping carts
View Transitions	references/view-transitions.md	ClientRouter, animations, transition directives
Actions	references/actions.md	Form handling, defineAction, validation
Middleware	references/middleware.md	onRequest, sequence, context.locals
Styling	references/styling.md	Scoped CSS, global styles, class:list
Images	references/images.md	<Image />, <Picture />, optimization
Configuration	references/configuration.md	astro.config.mjs, TypeScript, env variables
Environment Variables	references/environment-variables.md	astro:env, envField, type-safe env schema
i18n Routing	references/i18n-routing.md	Multilingual sites, locales, astro:i18n helpers
Guidelines by Context

Context-specific rules are available in the rules/ directory:

rules/astro-components.rule.md → Component structure patterns
rules/client-hydration.rule.md → Hydration strategy decisions
rules/content-collections.rule.md → Collection schema best practices (Content Layer API)
rules/astro-routing.rule.md → Routing patterns and dynamic routes
rules/astro-ssr.rule.md → SSR configuration and adapters
rules/astro-images.rule.md → Image optimization patterns
rules/astro-typescript.rule.md → TypeScript configuration
rules/server-islands.rule.md → Server island patterns and server:defer
rules/sessions.rule.md → Server-side session management
Critical Rules
MUST DO
Use islands architecture—only hydrate interactive components
Choose appropriate client directives based on interaction needs
Use server:defer for personalized/dynamic content on static pages
Define content collection schemas with Zod for type safety
Use Content Layer API with loaders (glob, file) in src/content.config.ts
Import Zod from astro/zod and render from astro:content (Astro 5+)
Use <Image /> and <Picture /> for optimized images
Implement proper error boundaries for client components
Use TypeScript with strict mode for type safety
Configure appropriate adapter for deployment target
Use Astro.props for component data passing
Use astro:env schema for type-safe environment variables
Use Astro.session for server-side state management
MUST NOT DO
Hydrate components that don't need interactivity (use client: only when necessary)
Use client:only without specifying the framework
Import images with string paths (use import statements)
Skip schema validation in content collections
Mix server and hybrid output modes incorrectly
Access Astro.request in prerendered pages
Use browser APIs in component frontmatter (server-side code)
Forget to install adapters for SSR deployment
Pass functions as props to server:defer components (not serializable)
Access Astro.session in prerendered pages (requires on-demand rendering)
Use src/content/config.ts for new projects (use src/content.config.ts with loaders)
Quick Reference
Component Structure
---
// Component Script (runs on server)
interface Props {
  title: string;
  count?: number;
}
const { title, count = 0 } = Astro.props;
const data = await fetch('https://api.example.com/data');
---

<!-- Component Template -->
<div>
  <h1>{title}</h1>
  <p>Count: {count}</p>
</div>

<style>
  /* Scoped by default */
  h1 { color: navy; }
</style>

Directive Priority
No directive → Static HTML, zero JavaScript
server:defer → Deferred server rendering (server island)
client:load → Hydrate immediately on page load
client:idle → Hydrate when browser is idle
client:visible → Hydrate when component enters viewport
client:media → Hydrate when media query matches
client:only → Skip SSR, render only on client
Content Collection Schema (Astro 5+)
// src/content.config.ts
import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const blog = defineCollection({
  loader: glob({ base: './src/content/blog', pattern: '**/*.{md,mdx}' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    draft: z.boolean().default(false),
    tags: z.array(z.string()).optional(),
  }),
});

export const collections = { blog };

Server Island
---
import UserAvatar from '../components/UserAvatar.astro';
---

<UserAvatar server:defer>
  <img slot="fallback" src="/generic-avatar.svg" alt="Loading..." />
</UserAvatar>

Output Format

When implementing Astro features, provide:

Component file (.astro with frontmatter and template)
Configuration updates (astro.config.mjs if needed)
Content collection schema (if using collections)
TypeScript types (for Props and data)
Brief explanation of hydration strategy chosen
Technologies

Astro 5+/6+, Islands Architecture, Content Layer API (glob/file loaders, live loaders), Zod Schemas, View Transitions API, Server Islands (server:defer), Sessions, Actions, Middleware, astro:env (type-safe environment variables), i18n Routing, Adapters (Node, Vercel, Netlify, Cloudflare, Deno), React/Vue/Svelte/Solid integrations, Image Optimization, MDX, Markdoc, TypeScript, Scoped CSS, Tailwind CSS

Weekly Installs
1.3K
Repository
delineas/astro-…k-agents
GitHub Stars
23
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
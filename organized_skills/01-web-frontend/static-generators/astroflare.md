---
rating: ⭐⭐⭐
title: astroflare
url: https://skills.sh/siviter-xyz/dot-agent/astroflare
---

# astroflare

skills/siviter-xyz/dot-agent/astroflare
astroflare
Installation
$ npx skills add https://github.com/siviter-xyz/dot-agent --skill astroflare
SKILL.md
Astroflare

Expert guidance for TypeScript, Tailwind, and Astro framework for scalable web development on the Cloudflare platform.

Key Principles
Write concise, technical responses with accurate Astro examples
Prioritize static generation and server-side islands with minimal JavaScript
Use descriptive variable names and follow Astro's naming conventions
NEVER change the site output without explicit user confirmation - issues are likely elsewhere in configuration, environment variables, or build process
Organize files using Astro's file-based routing system
Native over frameworks: Prefer native HTML elements (<dialog>, <form>) and web components over framework-specific solutions when possible. Use framework features only when they provide clear value.
Project Architecture
Deployment Target
Cloudflare Workers with output: 'static' and component server islands for server-side rendering
Use server:defer directive for server islands to optimize performance
Cloudflare adapter configured with platformProxy for forms/server actions
Trailing slashes always (trailingSlash: 'always') to match Cloudflare Workers behavior
Project Structure
src/
  ├── components/       # Astro components and custom web elements
  │   ├── core/         # Reusable core components
  │   ├── forms/        # Form components with client-side logic
  │   ├── modals/       # Modal dialogs
  │   └── animations/   # Animated components
  ├── layouts/          # Page layouts
  ├── pages/            # File-based routing
  ├── actions/          # Server actions (forms, API endpoints)
  ├── utils/            # Utility code
  └── styles/           # Global styles

Component Development
Create .astro files for all components - this is the default and preferred approach
Use components/core/ for reusable components
Prefer custom web components over React islands for interactivity
Use native HTML elements (<dialog>, <form>) when possible
Package Management
Use pnpm as the package manager
Node version: 24.x
pnpm version: >=10
References

For detailed guidance, see:

references/components.md - Component patterns and Starwind UI
references/routing.md - Routing and pages
references/forms.md - Forms and server actions
references/styling.md - Tailwind CSS patterns
references/seo.md - Comprehensive SEO guide
references/testing.md - Testing patterns
references/deployment.md - Build and deployment
Weekly Installs
81
Repository
siviter-xyz/dot-agent
GitHub Stars
11
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass
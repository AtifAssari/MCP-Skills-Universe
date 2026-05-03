---
rating: ⭐⭐
title: nextjs-tinacms
url: https://skills.sh/baphomet480/claude-skills/nextjs-tinacms
---

# nextjs-tinacms

skills/baphomet480/claude-skills/nextjs-tinacms
nextjs-tinacms
Installation
$ npx skills add https://github.com/baphomet480/claude-skills --skill nextjs-tinacms
SKILL.md
Next.js 16 + React 19 + TinaCMS + Vercel

Opinionated for: Next.js App Router + TinaCMS + Tina Cloud + Vercel + Tailwind CSS 4 + shadcn/ui.

Two workflows: New Project (scaffold from scratch) or Add CMS (integrate into existing Next.js 15/16 project).

Stack
Technology	Version	Key Feature
Next.js	16.x	Turbopack default, "use cache", proxy.ts, async params
TinaCMS	3.x	Git-backed CMS, visual click-to-edit, GraphQL schema API, ESM-only
React	19.x	Server Components, Actions, use(), useEffectEvent
Tailwind CSS	4.x	CSS-first config (@import "tailwindcss"), no JS config needed
shadcn/ui	CLI v4	Copy-paste components, npx shadcn create, tw-animate-css
Vercel	--	Deploy target. @vercel/analytics, @vercel/speed-insights, Deploy Hooks
Tina Cloud	--	Default CMS backend. Free tier (2 users), editorial workflow on Team Plus+
Quick Start
npx create-next-app@latest my-site --typescript --tailwind --app --src-dir
cd my-site
npx @tinacms/cli@latest init


Verify: tinacms dev then open http://localhost:3000/admin/index.html.

Local dev runs in local-only mode -- content reads/writes directly to the filesystem, no Tina Cloud connection needed. Production builds connect to Tina Cloud via NEXT_PUBLIC_TINA_CLIENT_ID and TINA_TOKEN env vars on Vercel.

Critical Knowledge
Server-Client split is mandatory. useTina() requires "use client". Every editable page needs a Server Component (data fetcher) + Client Component (visual editing wrapper).
Build order matters. Always "build": "tinacms build && next build". Wrong order breaks with Cannot find module '../tina/__generated__/client'.
Pin exact TinaCMS versions. No caret ranges. UI assets drift from CDN. Keep tinacms and @tinacms/* synced via package grouping (RenovateBot or Dependabot).
tina/__generated__/ should be gitignored. Only tina-lock.json must be committed. The __generated__/ folder is rebuilt by tinacms build.
TinaCMS 3.x is ESM-only. Config files must use import syntax. Set "type": "module" in package.json or use .ts extensions.
Async params in Next.js 16. Every page.tsx, layout.tsx, route.ts must await params -- sync access fully removed.
proxy.ts replaces middleware.ts. Lives at project root, exports proxy function, runs Node.js runtime only. Codemod: npx @next/codemod@canary middleware-to-proxy .
Security: @tinacms/cli >= 2.1.8 required. CVE-2026-28792 (Critical, CVSS 9.6) -- drive-by attacks via CORS + path traversal in older versions.
Dev command is tinacms dev -c "next dev". Never next dev alone -- the local GraphQL server won't run.
Version Floors

Look up current stable versions before scaffolding (npm view <pkg> version).

Package	Minimum	Why
next	>= 16.0.10	Security patches
tinacms	>= 3.3.x	Visual selector, ESM-only, current schema API
@tinacms/cli	>= 2.1.8	CVE-2026-28792 fix
react / react-dom	>= 19.0.x	Server Components, Actions (19.2.x for useEffectEvent)
tailwindcss	>= 4.x	CSS-first config (v3.4.x also acceptable)
Node.js	>= 20.9.0	Next.js 16 requirement
Key Imports
Import	From	Used For
defineConfig	tinacms	Schema configuration in tina/config.ts
useTina	tinacms/dist/react	Live editing in Client Components
tinaField	tinacms/dist/react	Click-to-edit data attributes
TinaMarkdown	tinacms/dist/rich-text	Rich text rendering
client	@/tina/__generated__/client	GraphQL queries (auto-generated)
Collections

Add based on project needs:

Collection	Type	When Needed
pages	Folder + blocks	Always
global	Singleton	Always (site settings, SEO defaults)
navigation	Singleton	Always (can include footer links)
posts	Folder	If site has a blog
authors	Folder	If site has a blog
footer	Singleton	If footer warrants its own collection
notFound	Singleton	Optional
Common Tasks
Create a new block

Add a template object to the blocks field's templates array in tina/config.ts. Every block needs ui.defaultItem. Optional: ui.previewSrc for visual selector thumbnails.

Add visual editing to a page
Server Component fetches { data, query, variables } from Tina client
Client Component calls useTina() with those props
Add data-tina-field={tinaField(data.page, 'fieldName')} on DOM elements
Enable caching

Set cacheComponents: true in next.config.ts, then use "use cache" directive with cacheLife() presets: seconds, minutes, hours, days, weeks, max.

Deploy to Vercel
Build command: tinacms build && next build
Set Vercel env vars: NEXT_PUBLIC_TINA_CLIENT_ID, TINA_TOKEN, NEXT_PUBLIC_TINA_BRANCH
Install @vercel/analytics + @vercel/speed-insights, render <Analytics /> and <SpeedInsights /> in root layout
Set up a Deploy Hook for content change rebuilds
Use Vercel Team Environment Variables to share keys across preview/production

Always use Tina Cloud unless the project has a specific reason to self-host. See references/deployment.md for self-hosted as a secondary option.

Claude Code Automations

Set up in .claude/settings.json early in Day 0:

{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Edit|Write",
      "hooks": [{
        "type": "prompt",
        "prompt": "If the file path contains 'tina/__generated__/' or ends with 'tina-lock.json', BLOCK this edit. These files are auto-generated by tinacms build and must not be manually edited."
      }]
    }],
    "PostToolUse": [{
      "matcher": "Edit|Write",
      "hooks": [{
        "type": "command",
        "command": "npx prettier --write $CLAUDE_FILE_PATH 2>/dev/null || true"
      }]
    }]
  },
  "permissions": {
    "allow": [
      "Bash(npx tinacms dev:*)",
      "Bash(npx tinacms build:*)",
      "Bash(pnpm dev:*)",
      "Bash(pnpm build:*)",
      "Bash(npx shadcn@latest add:*)"
    ]
  }
}


MCP servers:

claude mcp add context7 -- npx -y @upstash/context7-mcp@latest -- live TinaCMS/Next.js/React/Tailwind docs
claude mcp add playwright -- npx -y @anthropic-ai/mcp-server-playwright@latest -- test visual editing in browser

Consider creating project-level skills for repeated tasks:

/new-block -- scaffold a block template + component + renderer mapping
/tinacms-check -- audit schema for missing ui.itemProps, broken tinaField, version drift
Agentic Workflow & Vibe Coding
Iterative Building: Do not expect a perfect CMS integration on the first try. Draft the schema and visual editing wrapper, test the connection locally (tinacms dev), isolate any specific data-fetching or rendering error, adjust exactly ONE field or query at a time, and refresh until the click-to-edit experience is seamless.
Vibe Coding: Commit your working Next.js pages and Tina schema configurations locally before attempting complex block template additions or deploying to Vercel. Ensure tina-lock.json is included in these commits.
Reference Files
File	When To Read
references/schema-design.md	Designing collections, blocks, fields, content hooks
references/visual-editing.md	Server/client split, draft mode, click-to-edit debugging
references/seo-meta.md	Metadata, JSON-LD, OG tags, sitemaps, RSS
references/deployment.md	Tina Cloud vs self-hosted, media providers, env vars
references/setup-checklist.md	Phased implementation checklist (MVP / Polish / Comprehensive)
templates/tina-config-starter.ts	Production tina/config.ts with 5 block templates
templates/page-server-client.tsx	Server/client page pattern with metadata and static params
Weekly Installs
31
Repository
baphomet480/cla…e-skills
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
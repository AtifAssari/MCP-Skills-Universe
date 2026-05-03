---
title: docs-site
url: https://skills.sh/mjczz/docs-site/docs-site
---

# docs-site

skills/mjczz/docs-site/docs-site
docs-site
Installation
$ npx skills add https://github.com/mjczz/docs-site --skill docs-site
SKILL.md
Docs Site Skill

Scaffold a GitHub-styled TanStack Start documentation site for project analysis documents. Supports two modes: single project and multi-project hub.

When to Use

Use this skill when the user:

Asks to "create a docs site", "host analysis docs", "build a documentation site"
Says /docs-site or /host-docs
Wants to publish/surface analysis documents as a browsable web site
Has analysis .md files and wants a web UI for them
Wants to update an existing docs site (add/remove projects, exclude directories)
Says /docs-site --exclude ... or /docs-site --only ... on an already-hosted site
Prerequisites
bun must be available on the system
Site Existence Guard (MANDATORY)

Before any scaffold or creation step, check if the target directory already contains a site/ subdirectory:

test -d {target}/site && echo "EXISTS" || echo "NOT_EXISTS"

Rule
Condition	Action
site/ does NOT exist	Proceed with normal creation workflow
site/ exists AND site/package.json contains "docs-site-skill": true in a custom field (or a .docs-site-skill marker file exists in site/)	This is our site — enter Update Mode (see "Existing Site Update Mode" below)
site/ exists AND no marker found	STOP — the target already has a site that was NOT created by this skill. Report error and abort. Do NOT overwrite.
Error message when site exists but is not ours
ERROR: A "site/" directory already exists in the target project.
This site was not created by the docs-site skill and will NOT be overwritten.

If you want to replace it, please remove the existing site/ directory first:
  rm -rf {target}/site

Then re-run /docs-site.

Marker convention

When this skill creates a new site, it MUST write a marker file site/.docs-site-skill containing:

This site was scaffolded by the docs-site skill.


This allows future runs to distinguish our sites from pre-existing ones.

Mode Detection

The skill automatically detects which mode to use:

Condition	Mode
Target directory is an ai-analysis-docs/ or similar single-project analysis dir	Single-project
Target directory contains multiple subdirectories, each with .md files	Multi-project hub
User passes --multi flag	Force multi-project
Single-Project Mode

The target has one project's analysis docs (e.g. {project}/ai-analysis-docs/). Creates one site for it.

Multi-Project Hub Mode

The target is a parent directory containing multiple project analysis directories (e.g. /code-analysi/ with tokio/, k8s/, zinx/ etc.). Creates one unified site with:

A homepage listing all projects as cards
Each project gets its own section: /project/{name}/
Per-project sidebar with topic navigation
Cross-project search-friendly structure
Arguments
Optional: target path (defaults to current working directory)
Optional: --multi to force multi-project mode
Optional: --name "Site Name" to override site title
Optional: --only project1,project2,... to include only specific projects (multi-project mode)
Optional: --exclude project1,project2,... to exclude specific projects (multi-project mode)

Example invocations:

/docs-site (auto-detect mode)
/docs-site /path/to/project/ai-analysis-docs
/docs-site /path/to/code-analysi --multi
/docs-site /path/to/code-analysi --multi --only tokio,k8s,zinx
/docs-site /path/to/code-analysi --multi --exclude resume,stock
/docs-site /path/to/code-analysi --name "Code Analysis Hub"
Exclusion Rules (Multi-Project Mode)

When scanning directories in multi-project mode, apply these rules to decide which projects to include:

1. Command-line filtering (--only / --exclude):

If --only is provided: only include projects whose directory name matches one of the listed names
If --exclude is provided: skip projects whose directory name matches one of the listed names
If both are provided: --only takes precedence (ignore --exclude)

2. Always exclude (hardcoded skip list):

node_modules, site, .git, .claude, .vscode, .idea, .tanstack, .wrangler
Hidden directories (starting with .)
assets, dist, build, out, public
Directories with zero .md files (neither in root nor in topics/)

3. Minimum content threshold:

A directory must have at least 1 .md file in topics/ (after normalization) to be included
If a directory has .md files but they are all excluded files (changelog.md, *-analysis.md, *-progress-tracking.md, analysis-todo.md, README.md), it is excluded

4. Confirmation prompt: After scanning and filtering, show the user the final project list with document counts and ask for confirmation before proceeding. Format:

Found {count} projects to include:

  ✓ tokio       6 topics
  ✓ k8s         5 topics
  ✓ zinx        13 topics (8 core + 5 deep dives)
  ✗ resume      (excluded: --exclude flag)
  ✗ stock       (excluded: only 0 topic files)

Proceed with these {count} projects? [Y/n]


This ensures the user has a chance to review and adjust before the site is generated.

Existing Site Update Mode

When the user runs /docs-site on a target directory that already has a site/ directory with the .docs-site-skill marker, enter update mode instead of re-scaffolding from scratch.

Detection: Check if {target}/site/.docs-site-skill exists. If yes → update mode. If site/ exists but no marker → see "Site Existence Guard" error and abort.

What update mode does:

Re-scan all project directories with current exclusion rules (including any new --exclude / --only flags)
Compare with the current site/src/lib/registry.ts:
Projects newly included (were excluded before, or new directories added since last build): add to registry
Projects newly excluded (removed by --exclude flag, or directory deleted): remove from registry
Projects unchanged: keep as-is, but re-check for new/removed .md files in topics/
Regenerate site/src/lib/registry.ts with the updated project list
Rebuild and deploy:
cd site && bun run build && bun run deploy

Report what changed:
Updated existing site.

Changes:
  + added:      golang (3 topics)
  - removed:    resume, stock
  ~ updated:    zinx (2 new topics found)
  = unchanged:  14 projects

Rebuilt and deployed.


What update mode does NOT do:

Does NOT re-run bunx create site (scaffold)
Does NOT re-install dependencies
Does NOT overwrite styles.css, Header.tsx, Footer.tsx, or other custom components
Does NOT touch wrangler.toml, worker.ts, or vite.config.ts
Does NOT reset any user customizations

Key rule: The user may have manually edited styles, components, or config after the initial scaffold. Update mode only touches registry.ts — everything else is left alone.

Workflow: Single-Project Mode
S1. Discover & Normalize

Run the Site Existence Guard (see "Site Existence Guard" section above). If site/ already exists without our marker, report error and stop. If site/ exists with our marker, enter Update Mode. Only proceed with the steps below if no site/ exists.

Locate the analysis directory. If not found, report error and stop

Normalize directory structure — check if topics/ exists:

If topics/ does NOT exist: a. Create mkdir topics b. Move all analysis topic .md files into topics/. The files to move are those that are clearly topic documents (numbered like 01-*.md, 02-*.md, ..., or named deep-dive-*.md). Do NOT move the following files — they stay in root:
changelog.md
analysis-todo.md
*-analysis.md
*-progress-tracking.md
Any non-.md files or directories (e.g., assets/) c. Report what was moved

List all .md files in topics/

Read each file's first # heading to extract titles

Group files: Core (NN-*.md), Deep Dives (deep-dive-*.md), Other (rest)

Read main analysis file for project description

S2–S7. Build Site

Follow Steps 2–7 from the previous single-project workflow (Scaffold, Install, Create Files, Generate topics.ts, Copy Styles, Configure Cloudflare Deployment, Verify).

The Cloudflare deployment configuration is the same for both modes — see steps M8a–M8e in the multi-project workflow below.

Workflow: Multi-Project Hub Mode
M1. Site Existence Check & Scan

Run the Site Existence Guard (see "Site Existence Guard" section above). If site/ already exists without our marker, report error and stop. If site/ exists with our marker, enter Update Mode. Only proceed with the steps below if no site/ exists.

List all subdirectories in the target path. Apply the Exclusion Rules from the Arguments section (always-skip dirs, --only/--exclude flags, minimum content threshold)

For each project directory that passes filtering: a. Create mkdir {project}/topics b. Move all .md files from project root into topics/, EXCEPT:

changelog.md, analysis-todo.md, *-analysis.md, *-progress-tracking.md
README.md (if it's a generic README) c. Report what was moved d. Scan topics/ and extract title from first # heading of each file e. Categorize: core (NN-*.md), deep-dives (deep-dive-*.md), other f. Read the first non-heading paragraph from any root-level *-analysis.md or first topics/*.md as project description

Collect all projects into a registry:

{ name: "tokio", slug: "tokio", description: "...", topics: [...], deepDives: [...] }


Show confirmation prompt (per Exclusion Rules #4) with the final project list, included/excluded status, and document counts. Wait for user confirmation before proceeding.

After confirmation, report the final project list

M2. Scaffold TanStack Start

Run inside the target directory:

bunx --bun @tanstack/cli create site


Then:

Remove scaffolded about.tsx
Remove any .git directory created by the scaffold — the target directory (e.g. ~/ai/code-analysi/) is already a git repository. A nested .git would create a submodule conflict:
rm -rf site/.git

Write the marker file to identify this site as created by the docs-site skill:
echo "This site was scaffolded by the docs-site skill." > site/.docs-site-skill

M3. Install Dependencies
cd site
bun add react-markdown remark-gfm rehype-highlight highlight.js mermaid

M4. Create Hub File Structure

Create inside site/src/:

src/
├── components/
│   ├── Header.tsx
│   ├── Footer.tsx
│   ├── ProjectLayout.tsx       # Combines sidebar + main content for project pages
│   ├── MarkdownRenderer.tsx
│   └── MermaidBlock.tsx
├── lib/
│   └── registry.ts             # Auto-generated project registry
└── routes/
    ├── __root.tsx               # Root layout (no sidebar — hub mode)
    ├── index.tsx                # Hub homepage: project card grid
    └── project/
        └── $projectSlug/
            ├── index.tsx        # Project overview (wraps with <ProjectLayout>)
            ├── topics/
            │   └── $slug.tsx    # Topic page (wraps with <ProjectLayout>)
            └── deep-dives/
                └── $slug.tsx    # Deep dive page (wraps with <ProjectLayout>)


Key architecture decision: Each project page wraps its content with <ProjectLayout> which provides the sidebar + main content area. There is NO project/$projectSlug/__root.tsx — the layout is handled by a component, not a route layout. This avoids TanStack's nested __root.tsx complexity.

M5. Generate registry.ts

This file is generated dynamically and is the core of the hub. For each project and each .md file within it, generate:

Import statements using Vite ?url suffix (NOT ?raw — ?raw embeds full file content and causes Cloudflare Worker bundle to exceed 3 MiB limit), with paths relative to site/src/lib/:

import proj_tokio_topic_01 from '../../tokio/topics/01-overview.md?url'


?url returns only the asset URL string (~50 bytes) instead of the full file content (~10-50 KB). Markdown content is loaded at runtime via useTopicContent hook.

Extract titles at generation time by reading each .md file's H1 heading. Titles are hardcoded in the registry — NOT extracted at runtime.

A nested data structure with url field (NOT content):

Slug uniqueness rule: Every topic slug within a project MUST be unique and non-empty. Slug is derived from the filename (without .md). If two files in the same project would produce the same slug (e.g. MongoDB.md and another MongoDB.md, or filenames that normalize to the same string), append a distinguishing suffix based on the title or order number (e.g. MongoDB-sharding, MongoDB-multi-server). Empty slugs (from files with no meaningful name) must be given a descriptive slug derived from the title. This is critical because:

getTopic() uses .find() by slug — duplicate slugs make some pages inaccessible
React list rendering uses key={topic.order} to avoid duplicate key warnings, but slug uniqueness is still required for correct URL routing
export interface TopicMeta {
  slug: string
  title: string
  category: 'core' | 'deep-dive' | 'other'
  order: number
  url: string
}

export interface ProjectMeta {
  slug: string
  name: string
  description: string
  topics: TopicMeta[]
  coreTopics: TopicMeta[]
  deepDiveTopics: TopicMeta[]
}

export const projects: ProjectMeta[] = [
  {
    slug: 'tokio',
    name: 'Tokio',
    description: '...',
    topics: [...],
    coreTopics: [...],
    deepDiveTopics: [...]
  },
  // ... more projects
]

export function getProject(slug: string): ProjectMeta | undefined { ... }
export function getTopic(projectSlug: string, topicSlug: string): TopicMeta | undefined { ... }

M6. Key Route Templates

All templates for multi-project mode are in ~/.claude/skills/docs-site/templates/multi/.

Template	Purpose
hub-root.tsx	__root.tsx — no sidebar, just header + hub-main + footer
hub-index.tsx	index.tsx — project card grid with name + description + topic count
ProjectLayout.tsx	Component wrapping sidebar + main area, uses useParams({ strict: false })
project-index.tsx	project/$projectSlug/index.tsx — overview wrapped in <ProjectLayout>
project-topic.tsx	project/$projectSlug/topics/$slug.tsx — markdown + prev/next, wrapped in <ProjectLayout>
project-deepdive.tsx	project/$projectSlug/deep-dives/$slug.tsx — markdown + prev/next, wrapped in <ProjectLayout>
M7. Copy Shared Components

These are shared with single-project mode — copy from templates/:

styles.css, header.tsx, footer.tsx, markdown-renderer.tsx, mermaid-block.tsx, theme-toggle.tsx

Additionally, copy the async content loading hook to site/src/hooks/:

use-topic-content.ts → site/src/hooks/useTopicContent.ts
M8. Configure Cloudflare Workers Deployment
M8a. Install Cloudflare dependencies
cd site
bun add -d wrangler @cloudflare/vite-plugin

M8b. Create wrangler.toml

Create site/wrangler.toml:

name = "{site-name-hub}"
main = "src/worker.ts"
compatibility_date = "2026-03-28"
compatibility_flags = ["nodejs_compat"]

[assets]
directory = "dist/client"
binding = "ASSETS"

M8c. Create src/worker.ts

Create site/src/worker.ts:

import server from '../dist/server/server.js'

export default {
  async fetch(request: Request, env: { ASSETS: { fetch: (req: Request) => Promise<Response> } }) {
    const url = new URL(request.url)

    // Static asset requests — serve from ASSETS binding
    if (isStaticAsset(url.pathname)) {
      const assetResponse = await env.ASSETS.fetch(request)
      if (assetResponse.status !== 404) return assetResponse
    }

    // Everything else — SSR
    return server.fetch(request)
  },
} satisfies ExportedHandler<{ ASSETS: Fetcher }>

function isStaticAsset(pathname: string): boolean {
  return /\.(js|css|png|jpg|jpeg|gif|svg|ico|webp|woff|woff2|ttf|eot|json|webmanifest|txt|xml|map|md)$/i.test(pathname)
}

M8d. Add deploy scripts to package.json

Add to scripts:

{
  "deploy": "wrangler deploy",
  "cf-dev": "wrangler dev"
}

M8e. Update vite.config.ts

Ensure server.fs.allow includes parent directory (for ?url imports to resolve sibling project directories):

server: {
  fs: {
    allow: ['..'],
  },
},

M9. Verify & Deploy
cd site && bun run build


If build succeeds, deploy:

cd site && bun run deploy


Report result:

Multi-project docs site created!

Projects ({count}):
  - tokio: {N} topics, {M} deep dives
  - k8s: {N} topics
  - ...

Start:   cd site && bun run dev
Build:   cd site && bun run build
Deploy:  cd site && bun run deploy

Pages:
  - /                            Hub homepage
  - /project/{slug}              Project overview
  - /project/{slug}/topics/{id}  Topic page
  - /project/{slug}/deep-dives/{id}  Deep dive page

Template Files
Single-Project Templates (~/.claude/skills/docs-site/templates/)
File	Purpose
styles.css	GitHub-style theme (light + dark)
__root.tsx	Root layout with header, sidebar, main content, footer
index.tsx	Homepage with project name, description, card grid
header.tsx	Sticky header with logo and theme toggle
footer.tsx	Simple footer
sidebar.tsx	Left sidebar with grouped navigation links
markdown-renderer.tsx	react-markdown + remark-gfm + mermaid code block detection
mermaid-block.tsx	Dynamic mermaid.js renderer
topic-page.tsx	Dynamic route template for topics/$slug
deep-dive-page.tsx	Dynamic route template for deep-dives/$slug
use-topic-content.ts	Hook for fetching markdown content from URL at runtime
worker.ts	Cloudflare Workers entry point (SSR + static assets)
wrangler.toml	Cloudflare Workers deployment config
Multi-Project Templates (~/.claude/skills/docs-site/templates/multi/)
File	Purpose
hub-root.tsx	Hub root layout (header + hub-main + footer, NO sidebar)
hub-index.tsx	Hub homepage with project cards
ProjectLayout.tsx	Component combining sidebar + main content, used by all project pages
project-index.tsx	Project overview with topic/deep-dive card grids, wrapped in <ProjectLayout>
project-topic.tsx	Topic page with markdown rendering + prev/next, wrapped in <ProjectLayout>
project-deepdive.tsx	Deep dive page with markdown rendering + prev/next, wrapped in <ProjectLayout>
registry.ts	Registry template (placeholder-based, ?url imports for small bundle)
Mermaid Syntax Rules

When writing or validating mermaid code blocks in .md files, follow these rules to avoid render failures:

Comment Syntax
Use %% for comments, never # — # causes Parse error
Node & Subgraph IDs
IDs must be globally unique — a subgraph ID (e.g. subgraph DRA[...]) and a node ID (e.g. DRA[...]) cannot share the same name. This creates a "cycle" error.
Reserved keywords are case-insensitive: never use loop, end, alt, opt, par, critical, break as node or participant IDs. Use a different name (e.g. LoopFn instead of Loop).
Node Label Special Characters
Wrap labels in double quotes when they contain: @, [], : followed by / (e.g. IP CIDR), or () immediately after <br/>:
@ Symbol → ID["@ Symbol"]
AgentMessage[] → ID["AgentMessage"]
10.244.0.0/16 → ID["CIDR: 10.244.0.0/16"]
CronService<br/>(state) → ID["CronService<br/>(state)"]
The [] inside labels is ambiguous with mermaid's node shape syntax — always quote it.
The > from <br/> followed by ( can make the parser treat (text) as a rounded-edge node — quote the label.
sequenceDiagram Rules
alt/else/end syntax only — never use alt cond1|cond2| target or alt 是|否|:
alt condition A
    ...
else condition B
    ...
end

style directive only works in graph/flowchart — never use style in sequenceDiagram. It causes Parse error.
Note over only works in sequenceDiagram — never use it in graph/flowchart.
HTML Entities
Never use HTML entities (&lt;, &gt;, &amp;) in mermaid code blocks. They are rendered as literal text, not decoded. Use the actual characters or alternative notation:
HashMap&lt;K,V&gt; → HashMap(K,V) or HashMap[K,V]
<--> should be the literal characters, not &lt;-->
Arrow Syntax
Bidirectional arrows <--> are valid in graph/flowchart diagrams
Extra spaces around arrows are fine: A <--> B works
Nested Subgraphs
Nested subgraphs are supported in mermaid v10+, but empty labels like subgraph Row1[""] can cause Parse error. Always give nested subgraphs a meaningful label.
rehype-highlight Interference
The rehype-highlight plugin wraps code content in <span class="hljs-*> elements and adds hljs to the class
The MarkdownRenderer CodeBlock component must:
Use regex className?.match(/language-(\w+)/)?.[1] (not replace) to extract language
Use a recursive extractText() function to get plain text from children (not String(children) which produces [object Object])
Important Notes
Always use bun, never npm
Never initialize .git inside site/ — the target directory (e.g. ~/ai/code-analysi/) is already a git repository. The TanStack CLI scaffold may create site/.git; always remove it (rm -rf site/.git) after scaffolding. A nested .git creates a submodule conflict.
Topic slugs must be unique and non-empty within each project. When generating registry.ts, deduplicate slugs by appending descriptive suffixes (e.g. MongoDB-sharding). Empty slugs must be replaced with a slug derived from the title. Duplicate/empty slugs break getTopic() (only returns first match) and cause React key warnings.
Use key={topic.order} (not key={topic.slug}) in all .map() lists — order is always unique per topic within a project, while slug uniqueness is enforced at generation time but order is the safer key
The shellComponent pattern is required in __root.tsx (TanStack Start SSR)
Mermaid is loaded via dynamic import('mermaid') — do not import at top level
The code component in MarkdownRenderer must detect className="language-mermaid" to render MermaidBlock
All markdown files use Vite ?url imports — content is NOT bundled into the Worker. Instead, ?url returns a small URL string, and useTopicContent hook fetches the actual content at runtime from the ASSETS binding. This keeps the Worker bundle under Cloudflare's 3 MiB free plan limit (previously ?raw was used which embedded all file content and caused 5+ MiB bundles)
Route file names with $ like $slug.tsx are TanStack Router's dynamic segment syntax
In multi-project mode, <ProjectLayout> wraps each project page to provide the sidebar — no nested __root.tsx needed
Import paths in registry.ts must be relative to site/src/lib/ → use ../../{projectName}/topics/{file}.md?url (NOT ?raw)
useTopicContent hook must be placed at site/src/hooks/useTopicContent.ts — all topic/deep-dive route components depend on it for async content loading. The hook fetches markdown from the URL returned by ?url imports.
Worker isStaticAsset must include md extension — .md files are served as static assets via the ASSETS binding. Without this, content fetch requests would be routed to SSR instead of static assets.
Cloudflare Workers deployment: uses wrangler + worker.ts entry point. The worker serves static assets from dist/client via ASSETS binding, and SSR from dist/server/server.js. Requires nodejs_compat compatibility flag.
After scaffolding, install dev deps: bun add -d wrangler @cloudflare/vite-plugin
Deploy commands: bun run build && bun run deploy
Weekly Installs
8
Repository
mjczz/docs-site
First Seen
Mar 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
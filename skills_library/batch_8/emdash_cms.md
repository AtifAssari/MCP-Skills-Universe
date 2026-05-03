---
title: emdash-cms
url: https://skills.sh/aradotso/trending-skills/emdash-cms
---

# emdash-cms

skills/aradotso/trending-skills/emdash-cms
emdash-cms
Installation
$ npx skills add https://github.com/aradotso/trending-skills --skill emdash-cms
SKILL.md
EmDash CMS

Skill by ara.so — Daily 2026 Skills collection.

EmDash is a full-stack TypeScript CMS built on Astro and Cloudflare. It is the spiritual successor to WordPress: extensible, developer-friendly, and powered by a plugin system that runs plugins in sandboxed Worker isolates rather than with full filesystem/database access. EmDash stores rich text as Portable Text (structured JSON) rather than HTML, supports passkey-first auth, and runs on Cloudflare (D1 + R2 + Workers) or any Node.js server with SQLite.

Installation
Scaffold a new project
npm create emdash@latest


Follow the prompts to choose a template (blog, marketing, portfolio, starter, blank) and a platform (Cloudflare or Node.js/SQLite).

Deploy to Cloudflare directly

Use the one-click deploy button from the README, or:

npm create emdash@latest -- --template blog-cloudflare
cd my-site
npm run deploy

Add EmDash to an existing Astro project
npm install emdash

// astro.config.mjs
import { defineConfig } from "astro/config";
import emdash from "emdash/astro";
import { d1 } from "emdash/db";

export default defineConfig({
  integrations: [
    emdash({
      database: d1(), // Cloudflare D1
    }),
  ],
});


For Node.js + SQLite (no Cloudflare account needed):

// astro.config.mjs
import { defineConfig } from "astro/config";
import emdash from "emdash/astro";
import { sqlite } from "emdash/db";

export default defineConfig({
  integrations: [
    emdash({
      database: sqlite({ path: "./content.db" }),
    }),
  ],
});

Key CLI Commands
# Scaffold a new EmDash project
npm create emdash@latest

# Generate TypeScript types from your live schema
npx emdash types

# Seed the demo site with sample content
npx emdash seed

# Run database migrations
npx emdash migrate

# Start the dev server (standard Astro command)
npx astro dev

# Build for production
npx astro build

# Open admin panel (after dev server starts)
open http://localhost:4321/_emdash/admin

Monorepo / contributor commands
pnpm install
pnpm build
pnpm test          # run all tests
pnpm typecheck     # TypeScript check
pnpm lint:quick    # fast lint (< 1s)
pnpm format        # format with oxfmt

# Run the demo (Node.js + SQLite, no Cloudflare needed)
pnpm --filter emdash-demo seed
pnpm --filter emdash-demo dev

Configuration
Cloudflare (D1 + R2 + KV + Worker Loaders)
// wrangler.jsonc
{
  "name": "my-emdash-site",
  "compatibility_date": "2025-01-01",
  "d1_databases": [
    {
      "binding": "DB",
      "database_name": "emdash-content",
      "database_id": "$DATABASE_ID"
    }
  ],
  "r2_buckets": [
    {
      "binding": "MEDIA",
      "bucket_name": "emdash-media"
    }
  ],
  "kv_namespaces": [
    {
      "binding": "SESSIONS",
      "id": "$KV_NAMESPACE_ID"
    }
  ],
  // Remove this block to disable sandboxed plugins (free accounts)
  "worker_loaders": [
    {
      "binding": "PLUGIN_LOADER"
    }
  ]
}

// astro.config.mjs
import emdash from "emdash/astro";
import { d1 } from "emdash/db";
import { r2 } from "emdash/storage";
import { kv } from "emdash/sessions";

export default defineConfig({
  integrations: [
    emdash({
      database: d1({ binding: "DB" }),
      storage: r2({ binding: "MEDIA" }),
      sessions: kv({ binding: "SESSIONS" }),
    }),
  ],
});

Node.js + SQLite
// astro.config.mjs
import emdash from "emdash/astro";
import { sqlite } from "emdash/db";
import { localFiles } from "emdash/storage";

export default defineConfig({
  integrations: [
    emdash({
      database: sqlite({ path: "./content.db" }),
      storage: localFiles({ dir: "./public/uploads" }),
    }),
  ],
});

PostgreSQL / Turso
import { postgres } from "emdash/db";
import { turso } from "emdash/db";

// PostgreSQL
database: postgres({ url: process.env.DATABASE_URL })

// Turso/libSQL
database: turso({
  url: process.env.TURSO_DATABASE_URL,
  authToken: process.env.TURSO_AUTH_TOKEN,
})

Querying Content

Content types are defined in the admin UI (no code required). After creating a collection, generate types:

npx emdash types


This writes type definitions to src/emdash.d.ts.

Fetch a collection in an Astro page
---
// src/pages/blog/index.astro
import { getEmDashCollection } from "emdash";

const { entries: posts } = await getEmDashCollection("posts", {
  filter: { status: "published" },
  sort: { field: "publishedAt", direction: "desc" },
  limit: 10,
});
---

<ul>
  {posts.map((post) => (
    <li>
      <a href={`/blog/${post.data.slug}`}>{post.data.title}</a>
      <time datetime={post.data.publishedAt}>{post.data.publishedAt}</time>
    </li>
  ))}
</ul>

Fetch a single entry
---
// src/pages/blog/[slug].astro
import { getEmDashEntry, renderPortableText } from "emdash";

const { slug } = Astro.params;
const post = await getEmDashEntry("posts", { slug });

if (!post) return Astro.redirect("/404");

const { Content } = await renderPortableText(post.data.body);
---

<article>
  <h1>{post.data.title}</h1>
  <Content />
</article>

Pagination
---
import { getEmDashCollection } from "emdash";

const page = Number(Astro.params.page ?? 1);
const { entries: posts, total } = await getEmDashCollection("posts", {
  filter: { status: "published" },
  sort: { field: "publishedAt", direction: "desc" },
  limit: 10,
  offset: (page - 1) * 10,
});
---

Filtering by taxonomy
---
import { getEmDashCollection } from "emdash";

const { entries: posts } = await getEmDashCollection("posts", {
  filter: {
    status: "published",
    tags: { contains: "typescript" },
  },
});
---

Portable Text Rendering

EmDash stores rich text as Portable Text (structured JSON), not HTML.

---
import { renderPortableText } from "emdash";

const post = await getEmDashEntry("posts", { slug: Astro.params.slug });
const { Content } = await renderPortableText(post.data.body);
---

<Content />

Custom block renderers
// src/portable-text.ts
import { definePortableTextComponents } from "emdash/blocks";

export const components = definePortableTextComponents({
  types: {
    callout: ({ value }) => `
      <div class="callout callout--${value.type}">
        ${value.text}
      </div>
    `,
    image: ({ value }) => `
      <figure>
        <img src="${value.url}" alt="${value.alt ?? ""}" />
        ${value.caption ? `<figcaption>${value.caption}</figcaption>` : ""}
      </figure>
    `,
  },
  marks: {
    highlight: ({ children }) => `<mark>${children}</mark>`,
  },
});

---
import { renderPortableText } from "emdash";
import { components } from "../portable-text";

const { Content } = await renderPortableText(post.data.body, { components });
---
<Content />

Plugin Development

Plugins are the primary extension mechanism. On Cloudflare, they run in sandboxed Worker isolates with a declared capability manifest. On Node.js, they run in-process (safe mode).

Minimal plugin
// plugins/my-plugin/index.ts
import { definePlugin } from "emdash/plugin";

export default () =>
  definePlugin({
    id: "my-plugin",
    name: "My Plugin",
    version: "1.0.0",
    capabilities: [],
    hooks: {},
  });

Plugin with content hooks and email
import { definePlugin } from "emdash/plugin";

export default () =>
  definePlugin({
    id: "notify-on-publish",
    name: "Notify on Publish",
    version: "1.0.0",
    capabilities: ["read:content", "email:send"],
    hooks: {
      "content:afterSave": async (event, ctx) => {
        if (event.content.status !== "published") return;

        await ctx.email.send({
          to: "editors@example.com",
          subject: `New post published: ${event.content.title}`,
          text: `"${event.content.title}" is now live.`,
        });
      },
    },
  });

Plugin with KV storage and admin settings
import { definePlugin } from "emdash/plugin";

export default () =>
  definePlugin({
    id: "view-counter",
    name: "View Counter",
    version: "1.0.0",
    capabilities: ["read:content", "kv:read", "kv:write"],

    settings: {
      schema: {
        resetDaily: { type: "boolean", default: false, label: "Reset counts daily" },
      },
    },

    hooks: {
      "content:beforeRender": async (event, ctx) => {
        const key = `views:${event.content.id}`;
        const current = Number(await ctx.kv.get(key) ?? 0);
        await ctx.kv.set(key, String(current + 1));
        event.content.meta.views = current + 1;
      },
    },

    adminPages: [
      {
        path: "/analytics",
        title: "View Analytics",
        component: "ViewAnalytics",
      },
    ],
  });

Plugin with custom block type
import { definePlugin } from "emdash/plugin";
import { defineBlock } from "emdash/blocks";

export default () =>
  definePlugin({
    id: "callout-block",
    name: "Callout Block",
    version: "1.0.0",
    capabilities: [],

    blocks: [
      defineBlock({
        name: "callout",
        title: "Callout",
        fields: [
          { name: "type", type: "select", options: ["info", "warning", "danger"], default: "info" },
          { name: "text", type: "text", label: "Message" },
        ],
      }),
    ],

    hooks: {},
  });

Plugin with custom API route
import { definePlugin } from "emdash/plugin";

export default () =>
  definePlugin({
    id: "newsletter",
    name: "Newsletter",
    version: "1.0.0",
    capabilities: ["kv:write"],

    apiRoutes: [
      {
        method: "POST",
        path: "/subscribe",
        handler: async (request, ctx) => {
          const { email } = await request.json();
          await ctx.kv.set(`subscriber:${email}`, "true");
          return new Response(JSON.stringify({ ok: true }), {
            headers: { "Content-Type": "application/json" },
          });
        },
      },
    ],

    hooks: {},
  });

Available capabilities
Capability	What it allows
read:content	Read published content
write:content	Create and update content
read:users	Read user profiles
email:send	Send email via configured provider
kv:read	Read from plugin's KV namespace
kv:write	Write to plugin's KV namespace
http:fetch	Make outbound HTTP requests
storage:read	Read from media storage
storage:write	Write to media storage
Available hooks
// Content lifecycle
"content:beforeSave"
"content:afterSave"
"content:beforeDelete"
"content:afterDelete"
"content:beforeRender"

// Auth lifecycle
"auth:afterLogin"
"auth:afterLogout"
"auth:afterRegister"

// Media lifecycle
"media:beforeUpload"
"media:afterUpload"
"media:beforeDelete"

// Admin lifecycle
"admin:init"

Authentication

EmDash uses passkey-first (WebAuthn) authentication with OAuth and magic link fallbacks.

Configure OAuth providers
// astro.config.mjs
import emdash from "emdash/astro";
import { github, google } from "emdash/auth";

export default defineConfig({
  integrations: [
    emdash({
      database: d1(),
      auth: {
        providers: [
          github({
            clientId: process.env.GITHUB_CLIENT_ID,
            clientSecret: process.env.GITHUB_CLIENT_SECRET,
          }),
          google({
            clientId: process.env.GOOGLE_CLIENT_ID,
            clientSecret: process.env.GOOGLE_CLIENT_SECRET,
          }),
        ],
      },
    }),
  ],
});

Configure magic link email
auth: {
  providers: [
    magicLink({
      from: "noreply@yourdomain.com",
      // uses the configured email adapter
    }),
  ],
}

Protect a page
---
// src/pages/dashboard.astro
import { requireAuth } from "emdash/auth";

const user = await requireAuth(Astro);
// Redirects to /login if not authenticated
---

<p>Welcome, {user.name}!</p>

Get the current user (optional)
---
import { getUser } from "emdash/auth";

const user = await getUser(Astro); // null if not logged in
---

{user ? <p>Hello {user.name}</p> : <a href="/login">Sign in</a>}

Roles
import { requireRole } from "emdash/auth";

// In an API route or page
const user = await requireRole(Astro, "editor");
// Roles: "administrator" | "editor" | "author" | "contributor"

WordPress Migration
Import from a WXR export file
npx emdash import:wordpress ./export.xml

Import from the WordPress REST API
npx emdash import:wordpress --url https://yoursite.wordpress.com --api-key $WP_API_KEY

Import from WordPress.com
npx emdash import:wordpress --wpcom --site yoursite.wordpress.com


The importer migrates posts, pages, media attachments, categories, tags, authors, and comments. Gutenberg blocks are converted to Portable Text via the gutenberg-to-portable-text package.

Content Schema (Admin UI)

Content types are created in the admin panel at /_emdash/admin — not in code. After creating or modifying a collection, regenerate TypeScript types:

npx emdash types
# Writes to src/emdash.d.ts

Field types available in the schema builder
text — short string
richText — Portable Text (TipTap editor)
number — integer or float
boolean — true/false toggle
date / datetime — date pickers
select — single-choice dropdown
multiSelect — multi-choice
image — media library picker
file — file attachment
relation — link to another collection entry
slug — URL-safe string, auto-generated from a source field
json — raw JSON
MCP Server (AI Tool Integration)

EmDash includes a built-in MCP server so AI tools like Claude and ChatGPT can manage site content directly.

// astro.config.mjs
import emdash from "emdash/astro";

export default defineConfig({
  integrations: [
    emdash({
      database: d1(),
      mcp: {
        enabled: true,
        // Restrict to specific roles
        allowedRoles: ["administrator", "editor"],
      },
    }),
  ],
});


The MCP server is available at /_emdash/mcp. Connect Claude Desktop by adding to claude_desktop_config.json:

{
  "mcpServers": {
    "emdash": {
      "url": "https://yoursite.com/_emdash/mcp",
      "headers": {
        "Authorization": "Bearer $EMDASH_MCP_TOKEN"
      }
    }
  }
}

Repository Structure
packages/
  core/           Astro integration, APIs, admin UI, CLI
  auth/           Authentication library
  blocks/         Portable Text block definitions
  cloudflare/     Cloudflare adapter (D1, R2, Worker Loader)
  plugins/        First-party plugins (forms, embeds, SEO, audit-log, etc.)
  create-emdash/  npm create emdash scaffolding
  gutenberg-to-portable-text/  WordPress block converter

templates/        blog, marketing, portfolio, starter, blank
demos/            Development example sites
docs/             Starlight documentation site

First-Party Plugins

Install from the emdash/plugins package:

import forms from "emdash/plugins/forms";
import seo from "emdash/plugins/seo";
import embeds from "emdash/plugins/embeds";
import auditLog from "emdash/plugins/audit-log";

export default defineConfig({
  integrations: [
    emdash({
      database: d1(),
      plugins: [forms(), seo(), embeds(), auditLog()],
    }),
  ],
});

Troubleshooting
"Dynamic Workers are not available on free accounts"

Sandboxed plugins require a paid Cloudflare account ($5/mo+). To disable sandboxed plugins and run them in-process instead, remove the worker_loaders block from wrangler.jsonc:

// wrangler.jsonc — remove this block on free accounts
// "worker_loaders": [{ "binding": "PLUGIN_LOADER" }]

Admin panel returns 404

Ensure the Astro integration is registered in astro.config.mjs and the dev server has been restarted after installing EmDash.

TypeScript errors after schema changes

Regenerate types after modifying collections in the admin UI:

npx emdash types

D1 binding errors locally

Use wrangler dev instead of astro dev when developing with D1 bindings, or switch to SQLite for local development:

database: process.env.CF_PAGES ? d1() : sqlite({ path: "./content.db" })

Migrations not applied
npx emdash migrate
# For Cloudflare D1 remote:
npx wrangler d1 migrations apply emdash-content --remote

Plugin hook not firing

Verify the plugin is listed in the plugins array in astro.config.mjs and that the capability required by the hook is declared in the plugin's capabilities array. Missing capabilities cause the sandbox to silently block the call.

Weekly Installs
481
Repository
aradotso/trending-skills
GitHub Stars
42
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
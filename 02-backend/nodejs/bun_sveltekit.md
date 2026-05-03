---
rating: ⭐⭐⭐
title: bun-sveltekit
url: https://skills.sh/secondsky/claude-skills/bun-sveltekit
---

# bun-sveltekit

skills/secondsky/claude-skills/bun-sveltekit
bun-sveltekit
Installation
$ npx skills add https://github.com/secondsky/claude-skills --skill bun-sveltekit
SKILL.md
Bun SvelteKit

Run SvelteKit applications with Bun for faster development and builds.

Quick Start
# Create new SvelteKit project
bunx sv create my-app
cd my-app

# Install dependencies
bun install

# Development
bun run dev

# Build
bun run build

# Preview
bun run preview

Project Setup
package.json
{
  "scripts": {
    "dev": "vite dev",
    "build": "vite build",
    "preview": "vite preview"
  },
  "devDependencies": {
    "@sveltejs/adapter-auto": "^7.0.0",
    "@sveltejs/kit": "^2.0.0",
    "svelte": "^5.0.0",
    "vite": "^7.3.0"
  }
}

Use Bun Adapter
bun add -D svelte-adapter-bun

// svelte.config.js
import adapter from "svelte-adapter-bun";
import { vitePreprocess } from "@sveltejs/vite-plugin-svelte";

/** @type {import('@sveltejs/kit').Config} */
export default {
  preprocess: vitePreprocess(),
  kit: {
    adapter: adapter(),
  },
};

Using Bun APIs
Server Load Functions
// src/routes/users/+page.server.ts
import { Database } from "bun:sqlite";
import type { PageServerLoad } from "./$types";

export const load: PageServerLoad = async () => {
  const db = new Database("data.sqlite");
  const users = db.query("SELECT * FROM users").all();
  db.close();

  return { users };
};

Form Actions
// src/routes/users/+page.server.ts
import { Database } from "bun:sqlite";
import type { Actions } from "./$types";
import { fail } from "@sveltejs/kit";

export const actions: Actions = {
  create: async ({ request }) => {
    const data = await request.formData();
    const name = data.get("name") as string;

    if (!name) {
      return fail(400, { error: "Name required" });
    }

    const db = new Database("data.sqlite");
    db.run("INSERT INTO users (name) VALUES (?)", [name]);
    db.close();

    return { success: true };
  },

  delete: async ({ request }) => {
    const data = await request.formData();
    const id = data.get("id") as string;

    const db = new Database("data.sqlite");
    db.run("DELETE FROM users WHERE id = ?", [id]);
    db.close();

    return { success: true };
  },
};

API Routes
// src/routes/api/users/+server.ts
import { Database } from "bun:sqlite";
import { json } from "@sveltejs/kit";
import type { RequestHandler } from "./$types";

export const GET: RequestHandler = async () => {
  const db = new Database("data.sqlite");
  const users = db.query("SELECT * FROM users").all();
  db.close();

  return json(users);
};

export const POST: RequestHandler = async ({ request }) => {
  const { name } = await request.json();

  const db = new Database("data.sqlite");
  const result = db.run("INSERT INTO users (name) VALUES (?)", [name]);
  db.close();

  return json({ id: result.lastInsertRowid });
};

File Operations
// src/routes/api/files/[name]/+server.ts
import type { RequestHandler } from "./$types";

export const GET: RequestHandler = async ({ params }) => {
  const file = Bun.file(`./data/${params.name}`);

  if (!(await file.exists())) {
    return new Response("Not found", { status: 404 });
  }

  return new Response(file);
};

export const PUT: RequestHandler = async ({ params, request }) => {
  const content = await request.text();
  await Bun.write(`./data/${params.name}`, content);

  return new Response("Saved");
};

Server Hooks
// src/hooks.server.ts
import type { Handle } from "@sveltejs/kit";
import { Database } from "bun:sqlite";

// Initialize database on startup
const db = new Database("data.sqlite");
db.run(`
  CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
  )
`);

export const handle: Handle = async ({ event, resolve }) => {
  // Add database to locals
  event.locals.db = db;

  // Auth check
  const session = event.cookies.get("session");
  if (session) {
    event.locals.user = await getUser(session);
  }

  return resolve(event);
};

// src/app.d.ts
import type { Database } from "bun:sqlite";

declare global {
  namespace App {
    interface Locals {
      db: Database;
      user?: { id: number; name: string };
    }
  }
}

Svelte 5 Components
<!-- src/routes/users/+page.svelte -->
<script lang="ts">
  import type { PageData } from "./$types";

  let { data }: { data: PageData } = $props();
  let { users } = $derived(data);

  let name = $state("");
</script>

<h1>Users</h1>

<form method="POST" action="?/create">
  <input type="text" name="name" bind:value={name} />
  <button type="submit">Add User</button>
</form>

<ul>
  {#each users as user}
    <li>
      {user.name}
      <form method="POST" action="?/delete" style="display: inline">
        <input type="hidden" name="id" value={user.id} />
        <button type="submit">Delete</button>
      </form>
    </li>
  {/each}
</ul>

Deployment
Build for Bun
bun run build
bun ./build/index.js

Docker
FROM oven/bun:1 AS builder

WORKDIR /app
COPY package.json bun.lockb ./
RUN bun install --frozen-lockfile

COPY . .
RUN bun run build

FROM oven/bun:1

WORKDIR /app
COPY --from=builder /app/build ./build
COPY --from=builder /app/package.json ./

EXPOSE 3000

CMD ["bun", "./build/index.js"]

Adapter Options
// svelte.config.js
import adapter from "svelte-adapter-bun";

export default {
  kit: {
    adapter: adapter({
      out: "build",
      precompress: true, // Generate .gz and .br files
      envPrefix: "",     // Environment variable prefix
      development: false,
      dynamic_origin: true,
      xff_depth: 1,
    }),
  },
};

Environment Variables
# .env
DATABASE_URL=./data.sqlite
PUBLIC_API_URL=https://api.example.com

// Access in server code
import { DATABASE_URL } from "$env/static/private";
import { PUBLIC_API_URL } from "$env/static/public";

// Or dynamic
import { env } from "$env/dynamic/private";
const dbUrl = env.DATABASE_URL;

Common Errors
Error	Cause	Fix
Cannot find bun:sqlite	Wrong adapter	Use svelte-adapter-bun
Vite error	Build issue	Clear .svelte-kit
Hydration failed	Server/client diff	Check load functions
404 on refresh	SPA fallback	Configure adapter
When to Load References

Load references/adapter-config.md when:

Advanced adapter options
Static prerendering
Edge deployment

Load references/performance.md when:

Caching strategies
Lazy loading
Streaming SSR
Weekly Installs
163
Repository
secondsky/claude-skills
GitHub Stars
129
First Seen
3 days ago
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass
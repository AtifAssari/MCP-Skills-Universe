---
title: sveltekit-remote-functions
url: https://skills.sh/spences10/svelte-skills-kit/sveltekit-remote-functions
---

# sveltekit-remote-functions

skills/spences10/svelte-skills-kit/sveltekit-remote-functions
sveltekit-remote-functions
Installation
$ npx skills add https://github.com/spences10/svelte-skills-kit --skill sveltekit-remote-functions
SKILL.md
SvelteKit Remote Functions
Current Status

Remote functions are experimental in SvelteKit 2.58. Enable them in svelte.config.js:

export default {
	kit: { experimental: { remoteFunctions: true } },
	compilerOptions: { experimental: { async: true } } // only for await in components
};

Quick Start

File naming: export remote functions from *.remote.ts or *.remote.js. Remote files can live anywhere under src except src/lib/server.

Which function?

Dynamic reads → query()
Progressive forms → form()
Event-handler mutations → command()
Build-time/static reads → prerender()
Example
// posts.remote.ts
import { command, query, requested } from '$app/server';
import * as v from 'valibot';

export const getPosts = query(v.object({ tag: v.optional(v.string()) }), async (filter) => {
	return db.posts.find(filter);
});

export const createPost = command(v.object({ title: v.string() }), async (data) => {
	await db.posts.create(data);

	for (const { query } of requested(getPosts, 5)) {
		void query.refresh();
	}
});


Client:

<script lang="ts">
	import { createPost, getPosts } from './posts.remote';

	const posts = $derived(await getPosts({ tag: 'svelte' }));
</script>

<button onclick={() => createPost({ title: 'New' }).updates(getPosts)}>
	Create
</button>

Current Rules
Remote functions always run on the server, even when called from the browser.
Args/returns use devalue; avoid functions, class instances, symbols, circular refs, and RegExp.
Validate exposed inputs with Standard Schema (valibot, zod, arktype, etc.) or use .unchecked/'unchecked' deliberately.
query.batch() batches calls from the same macrotask to solve n+1 reads.
form().enhance() submit() returns true when submission is valid/successful and false for validation failures.
.updates() is client-requested; server handlers must opt in with requested(queryFn, limit).
requested() now yields { arg, query }; call query.refresh()/query.set(...) on the bound instance.
limit is required for requested() to cap client-controlled refresh requests.
Inside command/form handlers, use void query.refresh()/void query.set(value); SvelteKit awaits and serializes the updates.
Prefer form() over command() where progressive enhancement matters.
Use prerender() for data that changes at most once per deployment.
Last verified: SvelteKit 2.58.0, 2026-04-24
Reference Files
references/remote-functions.md - Current patterns, examples, and gotchas
Weekly Installs
259
Repository
spences10/svelt…ills-kit
GitHub Stars
77
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
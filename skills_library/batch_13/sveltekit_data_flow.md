---
title: sveltekit-data-flow
url: https://skills.sh/spences10/svelte-skills-kit/sveltekit-data-flow
---

# sveltekit-data-flow

skills/spences10/svelte-skills-kit/sveltekit-data-flow
sveltekit-data-flow
Installation
$ npx skills add https://github.com/spences10/svelte-skills-kit --skill sveltekit-data-flow
SKILL.md
SvelteKit Data Flow
Quick Start

Which file? Server-only (DB/secrets): +page.server.ts | Universal (runs both): +page.ts | API: +server.ts

Load decision: Need server resources? → server load | Need client APIs? → universal load

Form actions: Always +page.server.ts. Return fail() for errors, throw redirect() to navigate, throw error() for failures.

Example
// +page.server.ts
import { fail, redirect } from '@sveltejs/kit';

export const load = async ({ locals }) => {
	const user = await db.users.get(locals.userId);
	return { user }; // Must be JSON-serializable
};

export const actions = {
	default: async ({ request }) => {
		const data = await request.formData();
		const email = data.get('email');

		if (!email) return fail(400, { email, missing: true });

		await updateEmail(email);
		throw redirect(303, '/success');
	},
};

Reference Files
load-functions.md - Server vs universal
form-actions.md - Form handling patterns
serialization.md - What can/can't serialize
error-redirect-handling.md - fail/redirect/error
client-auth-invalidation.md - invalidateAll() after client-side auth
Notes
Server load → universal load via data param | ALWAYS throw redirect()/error()
No class instances/functions from server load (not serializable)
Last verified: 2025-01-11
Weekly Installs
247
Repository
spences10/svelt…ills-kit
GitHub Stars
77
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail
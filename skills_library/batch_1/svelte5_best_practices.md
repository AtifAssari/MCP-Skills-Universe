---
title: svelte5-best-practices
url: https://skills.sh/ejirocodes/agent-skills/svelte5-best-practices
---

# svelte5-best-practices

skills/ejirocodes/agent-skills/svelte5-best-practices
svelte5-best-practices
Installation
$ npx skills add https://github.com/ejirocodes/agent-skills --skill svelte5-best-practices
Summary

Svelte 5 runes, snippets, and SvelteKit patterns for modern component development.

Covers all Svelte 5 runes ($state, $derived, $effect, $props, $bindable, $inspect) with reactive state and computed value patterns
Explains snippets syntax ({#snippet}, {@render}) as the replacement for slots and slot props
Includes event handling migration from on: directives to onclick handlers and callback props, plus SvelteKit load functions and form actions
Provides TypeScript typing for props, generic components, and SSR state isolation patterns
Documents Svelte 4 to 5 migration paths including stores-to-runes and slots-to-snippets conversions with common pitfalls to avoid
SKILL.md
Svelte 5 Best Practices
Quick Reference
Topic	When to Use	Reference
Runes	$state, $derived, $effect, $props, $bindable, $inspect	runes.md
Snippets	Replacing slots, {#snippet}, {@render}	snippets.md
Events	onclick handlers, callback props, context API	events.md
TypeScript	Props typing, generic components	typescript.md
Migration	Svelte 4 to 5, stores to runes	migration.md
SvelteKit	Load functions, form actions, SSR, page typing	sveltekit.md
Performance	Universal reactivity, avoiding over-reactivity, streaming	performance.md
Essential Patterns
Reactive State
<script>
  let count = $state(0);           // Reactive state
  let doubled = $derived(count * 2); // Computed value
</script>

Component Props
<script>
  let { name, count = 0 } = $props();
  let { value = $bindable() } = $props(); // Two-way binding
</script>

Snippets (replacing slots)
<script>
  let { children, header } = $props();
</script>

{@render header?.()}
{@render children()}

Event Handlers
<!-- Svelte 5: use onclick, not on:click -->
<button onclick={() => count++}>Click</button>

Callback Props (replacing createEventDispatcher)
<script>
  let { onclick } = $props();
</script>

<button onclick={() => onclick?.({ data })}>Click</button>

Common Mistakes
Using let without $state - Variables are not reactive without $state()
Using $effect for derived values - Use $derived instead
Using on:click syntax - Use onclick in Svelte 5
Using createEventDispatcher - Use callback props instead
Using <slot> - Use snippets with {@render}
Forgetting $bindable() - Required for bind: to work
Setting module-level state in SSR - Causes cross-request leaks
Sequential awaits in load functions - Use Promise.all for parallel requests
Weekly Installs
3.1K
Repository
ejirocodes/agent-skills
GitHub Stars
4
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
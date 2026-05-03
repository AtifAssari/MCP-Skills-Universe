---
title: svelte-runes
url: https://skills.sh/spences10/svelte-skills-kit/svelte-runes
---

# svelte-runes

skills/spences10/svelte-skills-kit/svelte-runes
svelte-runes
Installation
$ npx skills add https://github.com/spences10/svelte-skills-kit --skill svelte-runes
SKILL.md
Svelte Runes
Quick Start

Which rune? Props: $props() | Bindable: $bindable() | Computed: $derived() | Side effect: $effect() | State: $state()

Key rules: Runes are top-level only. $derived can be overridden (use const for read-only). Don't mix Svelte 4/5 syntax. Objects/arrays are deeply reactive by default.

Example
<script>
	let count = $state(0); // Mutable state
	const doubled = $derived(count * 2); // Computed (const = read-only)

	$effect(() => {
		console.log(`Count is ${count}`); // Side effect
	});
</script>

<button onclick={() => count++}>
	{count} (doubled: {doubled})
</button>

Reference Files
reactivity-patterns.md - When to use each rune
migration-gotchas.md - Svelte 4→5 translation
component-api.md - $props, $bindable patterns
snippets-vs-slots.md - New snippet syntax
common-mistakes.md - Anti-patterns with fixes

For @attach and other template directives, see the svelte-template-directives skill.

Notes
Use onclick not on:click, {@render children()} in layouts
$derived can be reassigned (5.25+) - use const for read-only
Use createContext over setContext/getContext for type safety
Use $inspect.trace to debug reactivity issues
Last verified: 2026-03-12
Weekly Installs
346
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
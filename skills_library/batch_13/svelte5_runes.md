---
title: svelte5-runes
url: https://skills.sh/linehaul-ai/linehaulai-claude-marketplace/svelte5-runes
---

# svelte5-runes

skills/linehaul-ai/linehaulai-claude-marketplace/svelte5-runes
svelte5-runes
Installation
$ npx skills add https://github.com/linehaul-ai/linehaulai-claude-marketplace --skill svelte5-runes
SKILL.md
Svelte 5 Runes
Quick Start

Which rune? Props: $props() | Bindable: $bindable() | Computed: $derived() | Side effect: $effect() | State: $state()

Key rules: Runes are top-level only. $derived can be overridden (use const for read-only). Use consistent Svelte 5 syntax. Objects/arrays are deeply reactive by default.

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

Before suggesting code, check these:

references/reactivity-patterns.md - When to use each rune
references/component-api.md - $props, $bindable patterns
references/snippets-vs-slots.md - New snippet syntax
references/common-mistakes.md - Anti-patterns with fixes
Notes
Event handlers: Use onclick not on:click in Svelte 5
Children: Use {@render children()} in layouts
Check Svelte version before suggesting syntax
Svelte 5.25+ breaking change: $derived can now be reassigned (use const for read-only)
Last verified: 2025-01-11
Weekly Installs
19
Repository
linehaul-ai/lin…ketplace
GitHub Stars
4
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail
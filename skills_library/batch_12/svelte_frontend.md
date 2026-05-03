---
title: svelte-frontend
url: https://skills.sh/windmill-labs/windmill/svelte-frontend
---

# svelte-frontend

skills/windmill-labs/windmill/svelte-frontend
svelte-frontend
Installation
$ npx skills add https://github.com/windmill-labs/windmill --skill svelte-frontend
SKILL.md
Windmill Svelte Patterns

Apply these Windmill-specific patterns when writing Svelte code in frontend/. For general Svelte 5 syntax (runes, snippets, event handling), use the Svelte MCP server.

Windmill UI Components (MUST use)

Always use Windmill's design-system components. Never use raw HTML elements.

Buttons — <Button>
<script>
  import { Button } from '$lib/components/common'
  import { ChevronLeft } from 'lucide-svelte'
</script>

<Button variant="default" onclick={handleClick}>Label</Button>
<Button startIcon={{ icon: ChevronLeft }} iconOnly onclick={prev} />


Props: variant?: 'accent' | 'accent-secondary' | 'default' | 'subtle', unifiedSize?: 'sm' | 'md' | 'lg', startIcon?: { icon: SvelteComponent }, iconOnly?: boolean, disabled?: boolean

Text inputs — <TextInput>
<script>
  import { TextInput } from '$lib/components/common'
</script>

<TextInput bind:value={val} placeholder="Enter value" />


Props: value?: string | number (bindable), placeholder?: string, disabled?: boolean, error?: string | boolean, size?: 'sm' | 'md' | 'lg'

Selects — <Select>
<script>
  import Select from '$lib/components/select/Select.svelte'
</script>

<Select items={[{ label: 'Jan', value: 1 }]} bind:value={selected} />


Props: items?: Array<{ label?: string; value: any }>, value (bindable), placeholder?: string, clearable?: boolean, size?: 'sm' | 'md' | 'lg'

Icons — lucide-svelte

Never write inline SVGs. Import from lucide-svelte:

<script>
  import { ChevronLeft, X } from 'lucide-svelte'
</script>
<ChevronLeft size={16} />

Form Components

Form components (TextInput, Toggle, Select, etc.) should use the unified size system when placed together.

Styling
Use Tailwind CSS for all styling — no custom CSS
Use Windmill's theming classes for colors/surfaces (see frontend/brand-guidelines.md)
Read component props JSDoc before using them
Svelte MCP Server

Use the Svelte MCP tools when working on Svelte code:

list-sections: Call first to discover available docs
get-documentation: Fetch relevant sections based on use_cases
svelte-autofixer: MUST use on all Svelte code before finalizing — keep calling until no issues
playground-link: Only after user confirms and code was NOT written to project files
Weekly Installs
87
Repository
windmill-labs/windmill
GitHub Stars
16.4K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
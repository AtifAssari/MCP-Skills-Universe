---
title: svelte components
url: https://skills.sh/exceptionless/exceptionless/svelte-components
---

# svelte components

skills/exceptionless/exceptionless/svelte-components
svelte-components
Installation
$ npx skills add https://github.com/exceptionless/exceptionless --skill svelte-components
SKILL.md
Svelte Components

Documentation: svelte.dev | Use context7 for API reference

Visual Validation with Chrome MCP

Always verify UI changes visually using the Chrome MCP:

After making component changes, use Chrome MCP to take a snapshot or screenshot
Verify the component renders correctly and matches expected design
Test interactive states (hover, focus, disabled) when applicable
Check responsive behavior at different viewport sizes
Default to the /next site path for verification

This visual validation loop catches styling issues, layout problems, and accessibility regressions that automated tests may miss.

File Organization
Naming Conventions
kebab-case for all component files: stack-status-badge.svelte, user-profile-card.svelte
Co-locate with feature slice, aligned with API controllers
Directory Structure
src/lib/features/
├── organizations/           # Matches OrganizationController
│   ├── components/
│   │   ├── organization-card.svelte
│   │   └── organization-switcher.svelte
│   ├── api.svelte.ts
│   ├── models.ts
│   └── schemas.ts
├── stacks/                  # Matches StackController
│   └── components/
│       └── stack-status-badge.svelte
└── shared/                  # Shared across features
    └── components/
        ├── data-table/
        ├── navigation/
        └── typography/

Always Use shadcn-svelte Components

Never use native HTML for buttons, inputs, or form elements:

<script lang="ts">
    import { Button } from '$comp/ui/button';
    import { Input } from '$comp/ui/input';
    import * as Card from '$comp/ui/card';
</script>

<!-- ✅ Use shadcn components -->
<Card.Root>
    <Card.Header>
        <Card.Title>Settings</Card.Title>
    </Card.Header>
    <Card.Content>
        <Input placeholder="Enter value" />
    </Card.Content>
    <Card.Footer>
        <Button>Save</Button>
    </Card.Footer>
</Card.Root>

<!-- ❌ Never use native HTML -->
<button class="...">Save</button>
<input type="text" />

Runes
$state - Reactive State
<script lang="ts">
    let count = $state(0);
    let user = $state<User | null>(null);
    let items = $state<string[]>([]);
</script>

$derived - Computed Values
<script lang="ts">
    let count = $state(0);
    let doubled = $derived(count * 2);
    let isEven = $derived(count % 2 === 0);

    // Complex derived
    let summary = $derived.by(() => {
        return items.filter(i => i.active).map(i => i.name).join(', ');
    });
</script>

$effect - Side Effects
<script lang="ts">
    let searchTerm = $state('');

    $effect(() => {
        console.log('Search term changed:', searchTerm);
        return () => console.log('Cleaning up');
    });
</script>

Props
<script lang="ts">
    interface Props {
        name: string;
        count?: number;
        onUpdate?: (value: number) => void;
        children?: import('svelte').Snippet;
    }

    let { name, count = 0, onUpdate, children }: Props = $props();
</script>

Event Handling

Use onclick instead of on:click:

<Button onclick={() => handleClick()}>Click me</Button>
<Input oninput={(e) => (value = e.currentTarget.value)} />

Snippets (Content Projection)

Replace <slot> with snippets. From src/Exceptionless.Web/ClientApp/src/routes/(auth)/login/+page.svelte:

<form.Subscribe selector={(state) => state.errors}>
    {#snippet children(errors)}
        <ErrorMessage message={getFormErrorMessages(errors)}></ErrorMessage>
    {/snippet}
</form.Subscribe>

<form.Field name="email">
    {#snippet children(field)}
        <Field.Field data-invalid={ariaInvalid(field)}>
            <Field.Label for={field.name}>Email</Field.Label>
            <Input
                id={field.name}
                value={field.state.value}
                oninput={(e) => field.handleChange(e.currentTarget.value)}
            />
            <Field.Error errors={mapFieldErrors(field.state.meta.errors)} />
        </Field.Field>
    {/snippet}
</form.Field>

Class Merging

Use array syntax for conditional classes:

<div class={['flex items-center', expanded && 'bg-muted', className]}>
    Content
</div>

<Button class={['w-full', isActive && 'bg-primary']}>Save</Button>

Keyboard Accessibility

All interactive components must be keyboard accessible:

Use Button component (provides focus handling automatically)
Ensure custom interactions have tabindex and keyboard handlers
Test with keyboard-only navigation

See accessibility for WCAG guidelines.

Imports
<script lang="ts">
    // Use $app/state instead of $app/stores
    import { page } from '$app/state';

    // Access page data
    let currentPath = $derived(page.url.pathname);
</script>

References
shadcn-svelte — UI component patterns and trigger snippets
accessibility — WCAG guidelines and keyboard navigation
Weekly Installs
16
Repository
exceptionless/e…tionless
GitHub Stars
2.5K
First Seen
Mar 14, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
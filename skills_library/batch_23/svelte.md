---
title: svelte
url: https://skills.sh/epicenterhq/epicenter/svelte
---

# svelte

skills/epicenterhq/epicenter/svelte
svelte
Installation
$ npx skills add https://github.com/epicenterhq/epicenter --skill svelte
SKILL.md
Svelte Guidelines
Reference Repositories
Svelte — Svelte 5 framework with runes and fine-grained reactivity
shadcn-svelte — Port of shadcn/ui for Svelte with Bits UI primitives
shadcn-svelte-extras — Additional components for shadcn-svelte

Related Skills: See query-layer for TanStack Query integration. See error-handling for toast-on-error patterns (toastOnError, extractErrorMessage) when handling errors in components. See styling for CSS and Tailwind conventions, including the Flex Column Scroll Trap pattern (critical when building scrollable content inside Resizable.Pane, ScrollArea, or any flex column with siblings).

When to Apply This Skill

Use this pattern when you need to:

Build Svelte 5 components that use TanStack Query mutations.
Replace nested ternary $derived mappings with satisfies Record lookups.
Decide between createMutation in .svelte and .execute() in .ts.
Follow shadcn-svelte import, composition, and component organization patterns.
Refactor one-off handle* wrappers into inline template actions.
Convert SvelteMap data to arrays for derived state or component props.
Avoid template gotchas (unicode escapes in HTML vs JS context).
Extract repetitive markup into data-driven {#each} or {#snippet} patterns.
Prop-Keyed Resources: Let the Tree Own the Lifecycle

When a component owns a disposable resource (subscription, socket, timer, any handle with a dispose()/close()/unsubscribe() method) whose identity depends on a prop, open it synchronously and let the parent control mount/unmount with {#key} or {#if}. Don't store the resource in nullable $state and re-open it inside an $effect — that reimplements component mount/unmount in user-space.

The rule
<!-- Parent: one lifecycle boundary, structurally visible -->
{#if resourceId}
	{#key resourceId}
		<ResourceView id={resourceId} />
	{/key}
{/if}

<!-- Child: id is stable for this instance; open sync, dispose on unmount -->
<script lang="ts">
	let { id }: { id: string } = $props();

	const resource = openResource(id);
	$effect(() => () => resource.dispose());
</script>

<SomeView data={resource.data} />


The child's handle is non-nullable. No {#if handle} guard leaks into markup. The effect has one line because its only job is cleanup.

The anti-pattern
<!-- Reimplements mount/unmount by hand -->
<script lang="ts">
	let { id }: { id: string } = $props();
	let handle = $state<Resource | null>(null);

	$effect(() => {
		const h = openResource(id);
		handle = h;
		return () => { h.dispose(); handle = null; };
	});
</script>

{#if handle}
	<SomeView data={handle.data} />
{/if}


It's easy to write a double-dispose or leak here. The version above can't — the body is the cleanup.

Decision check
Is the id a prop? → Parent keys on it with {#key}; child opens sync.
Can the id be absent? → Parent wraps in {#if id}<Child {id} />{/if}; child opens sync.
Does the component have local UI state (selection, zoom, scroll) that must survive an id swap without persistence? → rare exception; the nullable-state pattern is justified.
Async-gate variant

When the resource exposes a readiness promise (whenReady, whenLoaded), gate rendering in the template with {#await}. Do NOT introduce a $state(false) flag + $effect that flips it inside .then() — Svelte already owns promise lifecycles, cancellation, and error branching. Rebuilding that in userland is pure ceremony.

<script lang="ts">
	const resource = openResource(id);
	$effect(() => () => resource.dispose());
</script>

{#await resource.whenReady}
	<div class="flex h-full items-center justify-center">
		<Spinner class="size-5 text-muted-foreground" />
	</div>
{:then}
	<Editor binding={resource.body.binding} />
{:catch error}
	<ErrorState {error} />
{/await}

Anti-pattern — don't do this
<!-- ❌ Re-implements {#await} with extra state and a cancellation flag -->
<script lang="ts">
	let isLoaded = $state(false);
	$effect(() => {
		let cancelled = false;
		resource.whenReady.then(() => { if (!cancelled) isLoaded = true; });
		return () => { cancelled = true; };
	});
</script>

{#if isLoaded}<Editor />{:else}<Spinner />{/if}


Three problems, every time:

One idea, three primitives. A state var, a subscription effect, and an if/else branch collectively say what {#await} says in four lines.
Silent unhandled rejections. The .then() chain drops errors on the floor. {#await}'s {:catch} makes failure explicit and catchable.
Manual cancellation. The cancelled flag exists because .then() fires after unmount. {#await} tears down the subscription when the block does.
When you still need $state flags

{#await} is for one stable promise driving one render branch. Reach for $state + $effect only when:

The flag is toggled imperatively by user action (isSaving around an await save() in a click handler).
You're composing multiple promises with custom logic (race, timeout, retry).
The flag reflects an external reactive source ($derived(query.isPending) from TanStack Query, a Svelte store, createSubscriber).
$state.raw for non-proxyable handles

Svelte's deep proxy can break handles whose methods rely on this being the original instance, or that hold internal non-reactive state. Prefer keeping handles out of $state entirely (the rule above). If a handle must live in state, use $state.raw(handle) to skip proxying.

Project-specific application

In this codebase, the rule applies to any component calling *Docs.open() (Yjs doc handles from createDocumentFactory). Search: $state<ReturnType<typeof .*\.open>. Every hit is a candidate for the rule above.

Related
The sync-construction-async-property-ui-render-gate-pattern skill covers the service-layer equivalent for clients with async-ready properties.
docs/articles/svelte-5-createsubscriber-pattern.md covers createSubscriber for wrapping external event sources into reactive values — a different job than component-scoped handles.
docs/articles/20260420T160000-state-handle-null-is-the-component-lifecycle-in-disguise.md walks through why this rule exists and when Pattern B is still correct.
$derived Value Mapping: Use satisfies Record, Not Ternaries

When a $derived expression maps a finite union to output values, use a satisfies Record lookup. Never use nested ternaries. Never use $derived.by() with a switch just to map values.

<!-- Bad: nested ternary in $derived -->
<script lang="ts">
	const tooltip = $derived(
		syncStatus.current === 'connected'
			? 'Connected'
			: syncStatus.current === 'connecting'
				? 'Connecting…'
				: 'Offline',
	);
</script>

<!-- Bad: $derived.by with switch for a pure value lookup -->
<script lang="ts">
	const tooltip = $derived.by(() => {
		switch (syncStatus.current) {
			case 'connected': return 'Connected';
			case 'connecting': return 'Connecting…';
			case 'offline': return 'Offline';
		}
	});
</script>

<!-- Good: $derived with satisfies Record -->
<script lang="ts">
	import type { SyncStatus } from '@epicenter/sync-client';

	const tooltip = $derived(
		({
			connected: 'Connected',
			connecting: 'Connecting…',
			offline: 'Offline',
		} satisfies Record<SyncStatus, string>)[syncStatus.current],
	);
</script>


Why satisfies Record wins:

Compile-time exhaustiveness: add a value to the union and TypeScript errors on the missing key. Nested ternaries silently fall through.
It's a data declaration, not control flow. The mapping is immediately visible.
$derived() stays a single expression — no need for $derived.by().

Reserve $derived.by() for multi-statement logic where you genuinely need a function body. For value lookups, keep it as $derived() with a record.

as const is unnecessary when using satisfies. satisfies Record<T, string> already validates shape and value types.

See docs/articles/record-lookup-over-nested-ternaries.md for rationale.

When to Use SvelteMap vs $state

Use SvelteMap when items have stable IDs and you need keyed lookup. Use $state for primitives, local UI booleans, and sequential data without identity.

Data Shape	Use	Example
Workspace table rows (have IDs)	fromTable() → SvelteMap	recordings, conversations, notes
Workspace KV (single key)	fromKv()	selectedFolderId, sortBy
Browser API keyed data	new SvelteMap() + listeners	Chrome tabs, windows
Primitive value	$state(value)	$state(false), $state(''), $state(0)
Sequential data without IDs	$state<T[]>([])	terminal history, command history
Ordered list where position matters	$state<T[]>([])	open file tab order
Anti-Pattern: $state for ID-Keyed Collections
// ❌ BAD: O(n) lookups, coarse reactivity, referential instability
let conversations = $state<Conversation[]>(readAll());
const metadata = $derived(conversations.find((c) => c.id === id)); // O(n) scan

// ✅ GOOD: O(1) lookups, per-key reactivity, stable $derived array
const conversationsMap = fromTable(workspace.tables.conversations);
const conversations = $derived(
	conversationsMap.values().toArray().sort((a, b) => b.updatedAt - a.updatedAt),
);
const metadata = $derived(conversationsMap.get(id)); // O(1) lookup


Three problems with $state<T[]> for keyed data:

O(n) lookups — every .find() scans the whole array
Coarse reactivity — updating one item re-triggers everything reading the array
Referential instability — sorting in a getter creates a new array every access, causing TanStack Table infinite loops

See docs/articles/sveltemap-over-state-for-keyed-collections.md for the full rationale.

Reactive Table State Pattern

When a factory function exposes workspace table data via fromTable, follow this three-layer convention:

// 1. Map — reactive source (private, suffixed with Map)
const foldersMap = fromTable(workspaceClient.tables.folders);

// 2. Derived array — cached materialization (private, no suffix)
const folders = $derived(foldersMap.values().toArray());

// 3. Getter — public API (matches the derived name)
return {
	get folders() {
		return folders;
	},
};


Naming: {name}Map (private source) → {name} (cached derived) → get {name}() (public getter).

With Sort or Filter

Chain operations inside $derived — the entire pipeline is cached:

const tabs = $derived(tabsMap.values().toArray().sort((a, b) => b.savedAt - a.savedAt));
const notes = $derived(allNotes.filter((n) => n.deletedAt === undefined));


See the typescript skill for iterator helpers (.toArray(), .filter(), .find() on IteratorObject).

Template Props

For component props expecting T[], derive in the script block — never materialize in the template:

<!-- Bad: re-creates array on every render -->
<FujiSidebar entries={entries.values().toArray()} />

<!-- Good: cached via $derived -->
<script>
	const entriesArray = $derived(entries.values().toArray());
</script>
<FujiSidebar entries={entriesArray} />

Why $derived, Not a Plain Getter

Put reactive computations in $derived, not inside public getters.

A getter may still be reactive if it reads reactive state, but it recomputes on every access. $derived computes reactively and caches until dependencies change.

Use $derived for the computation. Use the getter only as a pass-through to expose that derived value.

See docs/articles/derived-vs-getter-caching-matters.md for rationale.

Reactive State Module Conventions

State modules use a factory function that returns a flat object with getters and methods, exported as a singleton.

function createBookmarkState() {
	const bookmarksMap = fromTable(workspaceClient.tables.bookmarks);
	const bookmarks = $derived(bookmarksMap.values().toArray());

	return {
		get bookmarks() { return bookmarks; },
		async add(tab: Tab) { /* ... */ },
		remove(id: BookmarkId) { /* ... */ },
	};
}

export const bookmarkState = createBookmarkState();

Naming
Concern	Convention	Example
Export name	xState for domain state; descriptive noun for utilities	bookmarkState, notesState, deviceConfig, vadRecorder
Factory function	createX() matching the export name	createBookmarkState()
File name	Domain name, optionally with -state suffix	bookmark-state.svelte.ts, auth.svelte.ts

Use the State suffix when the export name would collide with a key property (bookmarkState.bookmarks, not bookmarks.bookmarks).

Accessor Patterns
Data Shape	Accessor	Example
Collection	Named getter	bookmarkState.bookmarks, notesState.notes
Single reactive value	.current (Svelte 5 convention)	selectedFolderId.current, serverUrl.current
Keyed lookup	.get(key)	toolTrustState.get(name), deviceConfig.get(key)

The .current convention comes from runed (the standard Svelte 5 utility library). All 34+ runed utilities use .current. Never use .value (Vue convention).

Persisted State Utilities

For localStorage/sessionStorage persistence, use createPersistedState (single value) or createPersistedMap (typed multi-key config) from @epicenter/svelte.

// Single value — .current accessor
import { createPersistedState } from '@epicenter/svelte';
const theme = createPersistedState({
	key: 'app-theme',
	schema: type("'light' | 'dark'"),
	defaultValue: 'dark',
});
theme.current; // read
theme.current = 'light'; // write + persist

// Multi-key config — .get()/.set() with SvelteMap (per-key reactivity)
import { createPersistedMap, defineEntry } from '@epicenter/svelte';
const config = createPersistedMap({
	prefix: 'myapp.config.',
	definitions: {
		'theme': defineEntry(type("'light' | 'dark'"), 'dark'),
		'fontSize': defineEntry(type('number'), 14),
	},
});
config.get('theme'); // typed read
config.set('theme', 'light'); // typed write + persist


Both accept storage?: Storage (defaults to window.localStorage) for dependency injection.

Mutation Patterns
In Svelte Files (.svelte)

Always prefer createMutation from TanStack Query for mutations. This provides:

Loading states (isPending)
Error states (isError)
Success states (isSuccess)
Better UX with automatic state management
The Preferred Pattern

Pass onSuccess and onError as the second argument to .mutate() to get maximum context:

<script lang="ts">
	import { createMutation } from '@tanstack/svelte-query';
	import * as rpc from '$lib/query';

	// Wrap .options in accessor function, no parentheses on .options
	// Name it after what it does, NOT with a "Mutation" suffix (redundant)
	const deleteSession = createMutation(
		() => rpc.sessions.deleteSession.options,
	);

	// Local state that we can access in callbacks
	let isDialogOpen = $state(false);
</script>

<Button
	onclick={() => {
		// Pass callbacks as second argument to .mutate()
		deleteSession.mutate(
			{ sessionId },
			{
				onSuccess: () => {
					// Access local state and context
					isDialogOpen = false;
					toast.success('Session deleted');
					goto('/sessions');
				},
				onError: (error) => {
					toast.error(error.title, { description: error.description });
				},
			},
		);
	}}
	disabled={deleteSession.isPending}
>
	{#if deleteSession.isPending}
		Deleting...
	{:else}
		Delete
	{/if}
</Button>

Why This Pattern?
More context: Access to local variables and state at the call site
Better organization: Success/error handling is co-located with the action
Flexibility: Different calls can have different success/error behaviors
In TypeScript Files (.ts)

Always use .execute() since createMutation requires component context:

// In a .ts file (e.g., load function, utility)
const result = await rpc.sessions.createSession.execute({
	body: { title: 'New Session' },
});

const { data, error } = result;
if (error) {
	// Handle error
} else if (data) {
	// Handle success
}

Exception: When to Use .execute() in Svelte Files

Only use .execute() in Svelte files when:

You don't need loading states
You're performing a one-off operation
You need fine-grained control over async flow
Single-Use Functions: Inline or Document

If a function is defined in the script tag and used only once in the template, inline it at the call site. This applies to event handlers, callbacks, and any other single-use logic.

Why Inline?

Single-use extracted functions add indirection — the reader jumps between the function definition and the template to understand what happens on click/keydown/etc. Inlining keeps cause and effect together at the point where the action happens.

<!-- BAD: Extracted single-use function with no JSDoc or semantic value -->
<script>
	function handleShare() {
		share.mutate({ id });
	}

	function handleSelectItem(itemId: string) {
		goto(`/items/${itemId}`);
	}
</script>

<Button onclick={handleShare}>Share</Button>
<Item onclick={() => handleSelectItem(item.id)} />

<!-- GOOD: Inlined at the call site -->
<Button onclick={() => share.mutate({ id })}>Share</Button>
<Item onclick={() => goto(`/items/${item.id}`)} />


This also applies to longer handlers. If the logic is linear (guard clauses + branches, not deeply nested), inline it even if it's 10–15 lines:

<!-- GOOD: Inlined keyboard shortcut handler -->
<svelte:window onkeydown={(e) => {
	const meta = e.metaKey || e.ctrlKey;
	if (!meta) return;
	if (e.key === 'k') {
		e.preventDefault();
		commandPaletteOpen = !commandPaletteOpen;
		return;
	}
	if (e.key === 'n') {
		e.preventDefault();
		notesState.createNote();
	}
}} />

The Exception: JSDoc + Semantic Name

Keep a single-use function extracted only when both conditions are met:

It has JSDoc explaining why it exists as a named unit.
The name provides a clear semantic meaning that makes the template more readable than the inlined version would be.
<script lang="ts">
	/**
	 * Navigate the note list with arrow keys, wrapping at boundaries.
	 * Operates on the flattened display-order ID list to respect date grouping.
	 */
	function navigateWithArrowKeys(e: KeyboardEvent) {
		// 15 lines of keyboard navigation logic...
	}
</script>

<!-- The semantic name communicates intent better than inlined logic would -->
<div onkeydown={navigateWithArrowKeys} tabindex="-1">


Without JSDoc and a meaningful name, extract it anyway — the indirection isn't earning its keep.

Multi-Use Functions

Functions used 2 or more times should always stay extracted — this rule only applies to single-use functions.

Commit-on-Blur for Workspace String Fields

For plain string fields backed by a workspace table or Y.Map row (title, subtitle, name, description, license, label), commit on onblur, not oninput. Per-keystroke writes turn one typing session into N Yjs transactions, N IDB writes, N sync messages, and N BroadcastChannel posts. Commit-on-blur collapses that to one.

The pattern has two halves: the per-input handler and the app-wide safety net. Both are required — the safety net is what makes commit-on-blur survive Cmd+W mid-edit.

The handler
<input
  type="text"
  value={entry.title}
  onblur={(e) => {
    const next = e.currentTarget.value;
    if (next !== entry.title) updateEntry({ title: next });
  }}
/>


The compare-then-write guard avoids a no-op Yjs transaction when focus passes through an unchanged field. For factories that update many fields, extract a small commit(field, next) helper that does the compare internally.

The safety net (app-wide, in +layout.svelte)
<script lang="ts">
  function flushPendingEdits() {
    if (
      document.visibilityState === 'hidden' &&
      document.activeElement instanceof HTMLElement
    ) {
      document.activeElement.blur();
    }
  }
</script>

<svelte:document onvisibilitychange={flushPendingEdits} />
<svelte:window onpagehide={flushPendingEdits} />


When the page is being hidden (tab close, Cmd+W, tab switch, window minimize, iOS app-switch, bfcache), .blur() on the focused element synchronously dispatches its blur event, which synchronously runs your commit handler, which synchronously updates the Y.Doc — all before the page tears down. Six lines, one place, every <input onblur> in the app inherits the resilience.

visibilitychange is a document event, pagehide is a window event. Per Svelte's packages/svelte/elements.d.ts, onvisibilitychange lives on SvelteDocumentAttributes and onpagehide lives on SvelteWindowAttributes — keep them on the right element. Listen to both: visibilitychange is more reliable on iOS Safari, pagehide catches bfcache navigations.

The default for new apps

Every new app under apps/* should ship the safety net in +layout.svelte as part of scaffolding. Treat it like <Toaster /> or <ModeWatcher /> — a layout-level concern that's free once installed. See workspace-app-layout for where this fits in the +layout.svelte checklist.

When NOT to use commit-on-blur
Field type	Pattern
Plain string Y.Map field (title, subtitle, name, description, license)	commit-on-blur
Y.Text bound through y-prosemirror / y-codemirror / tiptap	per-keystroke (CRDT operates at character level)
Discrete selectors (radio, checkbox, datepicker, tag pickers)	inline event handler — already one event per action
Search box / filter that doesn't persist	local $state only, no commit
Component-local form state submitted on a button click	accumulate in $state, commit in the click handler

For Y.Text fields you specifically want every keystroke to participate in operational transform — commit-on-blur defeats the point of the CRDT.

Defensive variant: local state + focus flag

If a sibling tab editing the same row could clobber in-progress typing (rare in personal apps), reach for a local-state buffer with a focus flag — but only if the clobber actually shows up:

<script lang="ts">
  let localTitle = $state(entry.title);
  let editing = $state(false);
  $effect(() => { if (!editing) localTitle = entry.title; });
</script>

<input
  bind:value={localTitle}
  onfocus={() => (editing = true)}
  onblur={() => {
    editing = false;
    if (localTitle !== entry.title) commit(localTitle);
  }}
/>


For true conflict-free text editing across tabs, switch the field to Y.Text + a CRDT-aware editor binding instead.

See docs/articles/commit-on-blur-survives-tab-close.md for the full rationale, persistence-layer reliability table, and the page-lifecycle guarantees behind the safety net.

Styling

For general CSS and Tailwind guidelines, see the styling skill.

shadcn-svelte Best Practices
Component Organization
Use the CLI: bunx shadcn-svelte@latest add [component]
Each component in its own folder under $lib/components/ui/ with an index.ts export
Follow kebab-case for folder names (e.g., dialog/, toggle-group/)
Group related sub-components in the same folder
When using $state, $derived, or functions only referenced once in markup, inline them directly
Import Patterns

Namespace imports (preferred for multi-part components):

import * as Dialog from '$lib/components/ui/dialog';
import * as ToggleGroup from '$lib/components/ui/toggle-group';


Named imports (for single components):

import { Button } from '$lib/components/ui/button';
import { Input } from '$lib/components/ui/input';


Lucide icons (always use individual imports from @lucide/svelte):

// Good: Individual icon imports
import Database from '@lucide/svelte/icons/database';
import MinusIcon from '@lucide/svelte/icons/minus';
import MoreVerticalIcon from '@lucide/svelte/icons/more-vertical';

// Bad: Don't import multiple icons from lucide-svelte
import { Database, MinusIcon, MoreVerticalIcon } from 'lucide-svelte';


The path uses kebab-case (e.g., more-vertical, minimize-2), and you can name the import whatever you want (typically PascalCase with optional Icon suffix).

Styling and Customization
Always use the cn() utility from $lib/utils for combining Tailwind classes
Modify component code directly rather than overriding styles with complex CSS
Use tailwind-variants for component variant systems
Follow the background/foreground convention for colors
Leverage CSS variables for theme consistency
Component Usage Patterns

Use proper component composition following shadcn-svelte patterns:

<Dialog.Root bind:open={isOpen}>
	<Dialog.Trigger>
		<Button>Open</Button>
	</Dialog.Trigger>
	<Dialog.Content>
		<Dialog.Header>
			<Dialog.Title>Title</Dialog.Title>
		</Dialog.Header>
	</Dialog.Content>
</Dialog.Root>

Custom Components
When extending shadcn components, create wrapper components that maintain the design system
Add JSDoc comments for complex component props
Ensure custom components follow the same organizational patterns
Consider semantic appropriateness (e.g., use section headers instead of cards for page sections)
Props Pattern
Always Inline Props Types

Never create a separate type Props = {...} declaration. Always inline the type directly in $props():

<!-- BAD: Separate Props type -->
<script lang="ts">
	type Props = {
		selectedWorkspaceId: string | undefined;
		onSelect: (id: string) => void;
	};

	let { selectedWorkspaceId, onSelect }: Props = $props();
</script>

<!-- GOOD: Inline props type -->
<script lang="ts">
	let { selectedWorkspaceId, onSelect }: {
		selectedWorkspaceId: string | undefined;
		onSelect: (id: string) => void;
	} = $props();
</script>

Children Prop Never Needs Type Annotation

The children prop is implicitly typed in Svelte. Never annotate it:

<!-- BAD: Annotating children -->
<script lang="ts">
	let { children }: { children: Snippet } = $props();
</script>

<!-- GOOD: children is implicitly typed -->
<script lang="ts">
	let { children } = $props();
</script>

<!-- GOOD: Other props need types, but children does not -->
<script lang="ts">
	let { children, title, onClose }: {
		title: string;
		onClose: () => void;
	} = $props();
</script>

Self-Contained Component Pattern
Prefer Component Composition Over Parent State Management

When building interactive components (especially with dialogs/modals), create self-contained components rather than managing state at the parent level.

The Anti-Pattern (Parent State Management)
<!-- Parent component -->
<script>
	let deletingItem = $state(null);
</script>

{#each items as item}
	<Button onclick={() => (deletingItem = item)}>Delete</Button>
{/each}

<AlertDialog open={!!deletingItem}>
	<!-- Single dialog for all items -->
</AlertDialog>

The Pattern (Self-Contained Components)
<!-- DeleteItemButton.svelte -->
<script lang="ts">
	import { createMutation } from '@tanstack/svelte-query';
	import { rpc } from '$lib/query';

	let { item }: { item: Item } = $props();
	let open = $state(false);

	const deleteItem = createMutation(() => rpc.items.delete.options);
</script>

<AlertDialog.Root bind:open>
	<AlertDialog.Trigger>
		<Button>Delete</Button>
	</AlertDialog.Trigger>
	<AlertDialog.Content>
		<Button onclick={() => deleteItem.mutate({ id: item.id })}>
			Confirm Delete
		</Button>
	</AlertDialog.Content>
</AlertDialog.Root>

<!-- Parent component -->
{#each items as item}
	<DeleteItemButton {item} />
{/each}

Why This Pattern Works
No parent state pollution: Parent doesn't need to track which item is being deleted
Better encapsulation: All delete logic lives in one place
Simpler mental model: Each row has its own delete button with its own dialog
No callbacks needed: Component handles everything internally
Scales better: Adding new actions doesn't complicate the parent
When to Apply This Pattern
Action buttons in table rows (delete, edit, etc.)
Confirmation dialogs for list items
Any repeating UI element that needs modal interactions
When you find yourself passing callbacks just to update parent state

The key insight: It's perfectly fine to instantiate multiple dialogs (one per row) rather than managing a single shared dialog with complex state. Modern frameworks handle this efficiently, and the code clarity is worth it.

View-Mode Branching Limit

If a component checks the same boolean flag (like isRecentlyDeletedView, isEditing, isCompact) in 3 or more template locations, the component is likely serving two purposes and should be considered for extraction.

<!-- SMELL: Same flag checked 3+ times -->
<script lang="ts">
	const notes = $derived(
		isRecentlyDeletedView ? deletedNotes : filteredNotes,  // branch 1
	);
</script>

{#if !isRecentlyDeletedView}  <!-- branch 2 -->
	<div>sort controls...</div>
{/if}

{#if isRecentlyDeletedView}  <!-- branch 3 -->
	No deleted notes
{:else}
	No notes yet
{/if}

The Fix: Push Branching Up to the Parent

Move the view-mode decision to the parent. The child component takes the varying data as props:

<!-- Parent: one branch point, explicit data flow -->
{#if viewState.isRecentlyDeletedView}
	<NoteList
		notes={notesState.deletedNotes}
		title="Recently Deleted"
		showControls={false}
		emptyMessage="No deleted notes"
	/>
{:else}
	<NoteList
		notes={viewState.filteredNotes}
		title={viewState.folderName}
	/>
{/if}


The child becomes dumb — it renders what it's told, with zero awareness of view modes. This keeps the branching in one place instead of scattered across the component tree.

The Threshold
1–2 checks: Acceptable — simple conditional rendering.
3+ checks on the same flag: The component is likely two views in one. Consider pushing the varying data up as props.
Data-Driven Repetitive Markup

When 3 or more sequential sibling elements follow an identical pattern with only data varying, consider extracting the data into an array and using {#each} or a {#snippet}.

<!-- BAD: Copy-paste ×3 with only value/label changing -->
<DropdownMenu.Item onclick={() => setSortBy('dateEdited')}>
	{#if sortBy === 'dateEdited'}<CheckIcon class="mr-2 size-4" />{/if}
	Date Edited
</DropdownMenu.Item>
<DropdownMenu.Item onclick={() => setSortBy('dateCreated')}>
	{#if sortBy === 'dateCreated'}<CheckIcon class="mr-2 size-4" />{/if}
	Date Created
</DropdownMenu.Item>
<DropdownMenu.Item onclick={() => setSortBy('title')}>
	{#if sortBy === 'title'}<CheckIcon class="mr-2 size-4" />{/if}
	Title
</DropdownMenu.Item>

<!-- GOOD: Data-driven with {#each} -->
<script lang="ts">
	const sortOptions = [
		{ value: 'dateEdited' as const, label: 'Date Edited' },
		{ value: 'dateCreated' as const, label: 'Date Created' },
		{ value: 'title' as const, label: 'Title' },
	];
</script>

{#each sortOptions as option}
	<DropdownMenu.Item onclick={() => setSortBy(option.value)}>
		{#if sortBy === option.value}
			<CheckIcon class="mr-2 size-4" />
		{:else}
			<span class="mr-2 size-4"></span>
		{/if}
		{option.label}
	</DropdownMenu.Item>
{/each}


For more complex repeated patterns (e.g., toolbar buttons with tooltips), use {#snippet} to define the shared structure once:

{#snippet toggleButton(pressed: boolean, onToggle: () => void, Icon: typeof BoldIcon, label: string)}
	<Tooltip.Root>
		<Tooltip.Trigger>
			<Toggle size="sm" {pressed} onPressedChange={onToggle}>
				<Icon class="size-4" />
			</Toggle>
		</Tooltip.Trigger>
		<Tooltip.Content>{label}</Tooltip.Content>
	</Tooltip.Root>
{/snippet}

{@render toggleButton(activeFormats.bold, () => editor?.chain().focus().toggleBold().run(), BoldIcon, 'Bold (⌘B)')}
{@render toggleButton(activeFormats.italic, () => editor?.chain().focus().toggleItalic().run(), ItalicIcon, 'Italic (⌘I)')}

When NOT to Extract
2 or fewer repetitions — extraction adds indirection without meaningful savings.
Structurally similar but semantically different — if the elements serve different purposes and might diverge, keep them separate.
Referential Stability for Reactive Data Sources
The Problem: New Array = Infinite Loop with TanStack Table

When feeding data from a reactive SvelteMap (or any signal-based store) into createSvelteTable, the get data() getter must return a referentially stable array. If it creates a new array on every access, TanStack Table's internal $derived enters an infinite loop:

1. $derived calls get data() → new array (Array.from().sort())
2. TanStack Table sees "data changed" → updates internal $state (row model)
3. $state mutation invalidates the $derived
4. $derived re-runs → get data() → new array again (always new!)
5. → infinite loop → page freeze


TanStack Query hid this problem because its cache returns the same reference until a refetch. SvelteMap getters that do Array.from(map.values()).sort() create a new array every call.

The Fix: Memoize with $derived

In .svelte.ts modules, use $derived to compute the sorted/filtered array once per SvelteMap change:

// ❌ BAD: New array on every access → infinite loop with TanStack Table
get sorted(): Recording[] {
    return Array.from(map.values()).sort(
        (a, b) => new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime(),
    );
}

// ✅ GOOD: $derived caches the result, stable reference between SvelteMap changes
const sorted = $derived(
    Array.from(map.values()).sort(
        (a, b) => new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime(),
    ),
);

// Expose via getter (returns cached $derived value)
get sorted(): Recording[] {
    return sorted;
}

When This Matters

The infinite loop only happens when the array is consumed by something that tracks reference identity in a reactive context:

createSvelteTable({ get data() { ... } }) — DANGEROUS (infinite loop)
$derived(someStore.sorted) where the result feeds back into state — DANGEROUS
{#each someStore.sorted as item} in a template — SAFE (Svelte's each block diffs by value, renders once per change)
$derived(someStore.get(id)) — SAFE (returns existing object reference from SvelteMap.get())
Rule of Thumb

If a .svelte.ts state module has a computed getter that returns an array/object, and that getter could be consumed by TanStack Table or a $derived chain that feeds into $state, always memoize with $derived. The cost is near-zero (one extra signal), and it prevents a class of bugs that's invisible in development until the page freezes.

Loading and Empty State Patterns
Never Use Plain Text for Loading States

Always use the Spinner component from @epicenter/ui/spinner instead of plain text like "Loading...". This applies to:

{#await} blocks gating on async readiness
{#if} / {:else} conditional loading
Button loading states
Full-Page Loading (Async Gate)

When gating UI on an async promise (e.g. whenReady, whenLoaded), use Empty.* for both loading and error states. This keeps the structure symmetric:

<script lang="ts">
	import * as Empty from '@epicenter/ui/empty';
	import { Spinner } from '@epicenter/ui/spinner';
	import TriangleAlertIcon from '@lucide/svelte/icons/triangle-alert';
</script>

{#await someState.whenReady}
	<Empty.Root class="flex-1">
		<Empty.Media>
			<Spinner class="size-5 text-muted-foreground" />
		</Empty.Media>
		<Empty.Title>Loading tabs…</Empty.Title>
	</Empty.Root>
{:then _}
	<MainContent />
{:catch}
	<Empty.Root class="flex-1">
		<Empty.Media>
			<TriangleAlertIcon class="size-8 text-muted-foreground" />
		</Empty.Media>
		<Empty.Title>Failed to load</Empty.Title>
		<Empty.Description>Something went wrong. Try reloading.</Empty.Description>
	</Empty.Root>
{/await}

Inline Loading (Conditional)

When loading state is controlled by a boolean or null check:

<script lang="ts">
	import { Spinner } from '@epicenter/ui/spinner';
</script>

{#if data}
	<Content {data} />
{:else}
	<div class="flex h-full items-center justify-center">
		<Spinner class="size-5 text-muted-foreground" />
	</div>
{/if}

Button Loading State

Use Spinner inside the button, matching the AuthForm pattern:

<Button onclick={handleAction} disabled={isPending}>
	{#if isPending}<Spinner class="size-3.5" />{:else}Submit{/if}
</Button>

Empty State (No Data)

Use the Empty.* compound component for empty states (no results, no items):

<script lang="ts">
	import * as Empty from '@epicenter/ui/empty';
	import FolderOpenIcon from '@lucide/svelte/icons/folder-open';
</script>

<Empty.Root class="py-8">
	<Empty.Media>
		<FolderOpenIcon class="size-8 text-muted-foreground" />
	</Empty.Media>
	<Empty.Title>No items found</Empty.Title>
	<Empty.Description>Create an item to get started</Empty.Description>
</Empty.Root>

Key Rules
Never show plain text ("Loading...", "Loading tabs…") without a Spinner
Always include {:catch} on {#await} blocks — prevents infinite spinner on failure
Use text-muted-foreground for loading text and spinner color
Use size-5 for full-page spinners, size-3.5 for inline/button spinners
Match the Empty.* compound component pattern for both error and empty states
Prop-First Data Derivation

When a component receives a prop that already carries the information needed for a decision, derive from the prop. Never reach into global state for data the component already has.

<!-- BAD: Reading global state for info the prop already carries -->
<script lang="ts">
	import { viewState } from '$lib/state';
	let { note }: { note: Note } = $props();

	// viewState.isRecentlyDeletedView is redundant — note.deletedAt has the answer
	const showRestoreActions = $derived(viewState.isRecentlyDeletedView);
</script>

<!-- GOOD: Derive from the prop itself -->
<script lang="ts">
	let { note }: { note: Note } = $props();

	// The note knows its own state — no global state needed
	const isDeleted = $derived(note.deletedAt !== undefined);
</script>

Why This Matters
Self-describing: The component works correctly regardless of which view rendered it.
Fewer imports: Dropping a global state import reduces coupling.
Testable: Pass a note with deletedAt set and the component behaves correctly — no need to mock view state.
The Rule

If the data needed for a decision is already on a prop (directly or derivable), always derive from the prop. Global state is for information the component genuinely doesn't have.

Template Gotchas
Unicode Escapes Don't Work in HTML Context

In Svelte, \uXXXX escape sequences work in JavaScript strings (inside <script> and {expressions}) but are treated as literal text in HTML template attributes and text content.

<!-- BAD: \u2026 renders as literal "\u2026" in the browser -->
<input placeholder="Search\u2026" />
<Tooltip.Content>Toggle terminal (\u2318`)</Tooltip.Content>
<p>Close the tab, reopen\u2014your notes are there.</p>

<!-- GOOD: Use actual unicode characters -->
<input placeholder="Search…" />
<Tooltip.Content>Toggle terminal (⌘`)</Tooltip.Content>
<p>Close the tab, reopen—your notes are there.</p>


JavaScript contexts are fine—these are standard JS string escapes:

<script>
  // ✅ Works: JS string in <script>
  createPlaceholderPlugin('Start writing\u2026');
</script>

<!-- ✅ Works: JS expression in template -->
{aiChatState.provider || 'Provider\u2026'}
{isLoading ? 'Loading\u2026' : 'Ready'}


Common characters affected: \u2014 (—), \u2026 (…), \u2318 (⌘), \u21e7 (⇧), \u2192 (→).

Rule: In HTML attributes and text content, always use the actual character. Reserve \uXXXX for JavaScript strings only.

Weekly Installs
171
Repository
epicenterhq/epicenter
GitHub Stars
4.5K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
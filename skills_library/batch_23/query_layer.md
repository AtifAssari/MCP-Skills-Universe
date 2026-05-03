---
title: query-layer
url: https://skills.sh/epicenterhq/epicenter/query-layer
---

# query-layer

skills/epicenterhq/epicenter/query-layer
query-layer
Installation
$ npx skills add https://github.com/epicenterhq/epicenter --skill query-layer
SKILL.md
Query Layer Patterns
Reference Repositories
TanStack Query — Async state management for data fetching

The query layer is the reactive bridge between UI components and the service layer. It wraps pure service functions with caching, reactivity, and state management using TanStack Query and WellCrafted factories.

Related Skills: See services-layer for the service layer these queries consume. See svelte for Svelte-specific TanStack Query patterns. See error-handling for toast-on-error patterns—how errors from Results surface to users via toastOnError and extractErrorMessage.

When to Apply This Skill

Use this pattern when you need to:

Create queries or mutations that consume services
Transform service-layer errors into user-facing error types
Implement runtime service selection based on user settings
Add optimistic cache updates for instant UI feedback
Understand the dual interface pattern (reactive vs imperative)
Core Architecture
┌─────────────┐     ┌─────────────┐     ┌──────────────┐
│     UI      │ --> │  RPC/Query  │ --> │   Services   │
│ Components  │     │    Layer    │     │    (Pure)    │
└─────────────┘     └─────────────┘     └──────────────┘
      ↑                    │
      └────────────────────┘
         Reactive Updates


Query Layer Responsibilities:

Call services with injected settings/configuration
Transform service errors to user-facing error types for display
Manage TanStack Query cache for optimistic updates
Provide dual interfaces: reactive (.options) and imperative (.execute())
Error Transformation Pattern

Critical: Service errors should be transformed to user-facing error types at the query layer boundary.

Three-Layer Error Flow
Service Layer         →  Query Layer           →  UI Layer
TaggedError<'Name'>   →  UserFacingError       →  Toast notification
(domain-specific)        (display-ready)          (display)

Standard Error Transformation
import { Err, Ok } from 'wellcrafted/result';

// In query layer - transform service error to user-facing error
const { data, error } = await services.recorder.startRecording(params);

if (error) {
	return Err({
		title: '❌ Failed to start recording',
		description: error.message,
		action: { type: 'more-details', error },
	});
}

return Ok(data);

Dual Interface Pattern

Every query/mutation provides two ways to use it:

Reactive Interface: .options

Use in Svelte components for automatic state management. Pass .options (a static object) inside an accessor function:

<script lang="ts">
	import { createQuery, createMutation } from '@tanstack/svelte-query';
	import { rpc } from '$lib/query';

	// Reactive query - wrap in accessor function, access .options (no parentheses)
	const recorderState = createQuery(() => rpc.recorder.getRecorderState.options);

	// Reactive mutation - same pattern
	const transformRecording = createMutation(
		rpc.transformer.transformRecording.options,
	);
</script>

{#if recorderState.isPending}
	<Spinner />
{:else if recorderState.error}
	<Error message={recorderState.error.description} />
{:else}
	<RecorderIndicator state={recorderState.data} />
{/if}

Imperative Interface: .execute() / .fetch()

Use in event handlers and workflows without reactive overhead:

// In an event handler or workflow
async function handleTransform(recordingId: string, transformation: Transformation) {
	const { error } = await rpc.transformer.transformRecording({
		recordingId,
		transformation,
	});
	if (error) {
		notify.error(error);
		return;
	}
	notify.success({ title: 'Transformation complete' });
}

// In a sequential workflow
async function stopAndTranscribe(toastId: string) {
	const { data: blobData, error: stopError } =
		await rpc.recorder.stopRecording({ toastId });

	if (stopError) {
		notify.error(stopError);
		return;
	}

	// Continue with transcription...
}

When to Use Each
Use .options with createQuery/createMutation	Use .execute()/.fetch()
Component data display	Event handlers
Loading spinners needed	Sequential workflows
Auto-refetch wanted	One-time operations
Reactive state needed	Outside component context
Cache synchronization	Performance-critical paths
Key Rules
Always transform errors at query boundary - Never return raw service errors
Use .options (no parentheses) - It's a static object, wrap in accessor for Svelte
Never double-wrap errors - Each error is wrapped exactly once
Services are pure, queries inject settings - Services take explicit params
Use imperative calls in .ts files - createMutation requires component context
Update cache optimistically - Better UX for mutations
References

Load these on demand based on what you're working on:

If working with error transformation examples and anti-patterns, read references/error-transformation-patterns.md

If working with runtime dependency injection and service selection, read references/runtime-dependency-injection.md

If working with cache management, query definitions, RPC namespace, or notify coordination, read references/advanced-query-patterns.md

See apps/whispering/src/lib/query/README.md for detailed architecture

See the services-layer skill for how services are implemented

See the error-handling skill for trySync/tryAsync patterns and toast-on-error conventions

Weekly Installs
57
Repository
epicenterhq/epicenter
GitHub Stars
4.5K
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
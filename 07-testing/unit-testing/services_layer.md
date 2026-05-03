---
title: services-layer
url: https://skills.sh/epicenterhq/epicenter/services-layer
---

# services-layer

skills/epicenterhq/epicenter/services-layer
services-layer
Installation
$ npx skills add https://github.com/epicenterhq/epicenter --skill services-layer
SKILL.md
Services Layer Patterns

This skill documents how to implement services in the Whispering architecture. Services are pure, isolated business logic with no UI dependencies that return Result<T, E> types for error handling.

Related Skills: See error-handling for trySync/tryAsync patterns. See define-errors for error variant factories. See query-layer for consuming services with TanStack Query.

When to Apply This Skill

Use this pattern when you need to:

Create a new service with domain-specific error handling
Add error types with structured context (like HTTP status codes)
Understand how services are organized and exported
Implement platform-specific service variants (desktop vs web)
Core Architecture

Services follow a three-layer architecture: Service → Query → UI

┌─────────────┐     ┌─────────────┐     ┌──────────────┐
│     UI      │ --> │  RPC/Query  │ --> │   Services   │
│ Components  │     │    Layer    │     │    (Pure)    │
└─────────────┘     └─────────────┘     └──────────────┘


Services are:

Pure: Accept explicit parameters, no hidden dependencies
Isolated: No knowledge of UI state, settings, or reactive stores
Testable: Easy to unit test with mock parameters
Consistent: All return Result<T, E> types for uniform error handling
Creating Errors with defineErrors

Every service defines domain-specific errors using defineErrors from wellcrafted. Errors are grouped into a namespace object where each key becomes a variant.

import { defineErrors, type InferError, type InferErrors, extractErrorMessage } from 'wellcrafted/error';
import { Err, Ok, type Result, tryAsync, trySync } from 'wellcrafted/result';

// Namespace-style error definition — name describes the domain
const CompletionError = defineErrors({
  ConnectionFailed: ({ cause }: { cause: unknown }) => ({
    message: `Connection failed: ${extractErrorMessage(cause)}`,
    cause,
  }),
  EmptyResponse: ({ providerLabel }: { providerLabel: string }) => ({
    message: `${providerLabel} API returned an empty response`,
    providerLabel,
  }),
  MissingParam: ({ param }: { param: string }) => ({
    message: `${param} is required`,
    param,
  }),
});

// Type derivation — shadow the const with a type of the same name
type CompletionError = InferErrors<typeof CompletionError>;
type ConnectionFailedError = InferError<typeof CompletionError.ConnectionFailed>;

// Call sites — each variant returns Err<...> directly
return CompletionError.ConnectionFailed({ cause: error });
return CompletionError.EmptyResponse({ providerLabel: 'OpenAI' });
return CompletionError.MissingParam({ param: 'apiKey' });

How defineErrors Works

defineErrors({ ... }) takes an object of factory functions and returns a namespace object. Each key becomes a variant:

name is auto-stamped from the key (e.g., key NotFound → error.name === 'NotFound')
The factory function IS the message generator — it returns { message, ...fields }
Each variant returns Err<...> directly — no separate FooErr constructor needed
Types use InferError / InferErrors — not ReturnType
// No-input variant (static message)
const RecorderError = defineErrors({
  Busy: () => ({
    message: 'A recording is already in progress',
  }),
});

// Usage — no arguments needed
return RecorderError.Busy();

// Variant with derived fields — constructor extracts from raw input
const HttpError = defineErrors({
  Response: ({ response, body }: { response: { status: number }; body: unknown }) => ({
    message: `HTTP ${response.status}: ${extractErrorMessage(body)}`,
    status: response.status,
    body,
  }),
});

// Usage — pass raw objects, constructor derives fields
return HttpError.Response({ response, body: await response.json() });
// error.message → "HTTP 401: Unauthorized"
// error.status  → 401 (derived from response, flat on the object)
// error.name    → "Response"

Error Type Examples from the Codebase
// Static message, no input needed
const RecorderError = defineErrors({
  Busy: () => ({
    message: 'A recording is already in progress',
  }),
});
RecorderError.Busy()

// Multiple related errors in a single namespace
const HttpError = defineErrors({
  Connection: ({ cause }: { cause: unknown }) => ({
    message: `Failed to connect to the server: ${extractErrorMessage(cause)}`,
    cause,
  }),
  Response: ({ response, body }: { response: { status: number }; body: unknown }) => ({
    message: `HTTP ${response.status}: ${extractErrorMessage(body)}`,
    status: response.status,
    body,
  }),
  Parse: ({ cause }: { cause: unknown }) => ({
    message: `Failed to parse response body: ${extractErrorMessage(cause)}`,
    cause,
  }),
});

// Union type for the whole namespace
type HttpError = InferErrors<typeof HttpError>;

// Individual variant type
type ConnectionError = InferError<typeof HttpError.Connection>;

Key Rules
Services never import settings - Pass configuration as parameters
Services never import UI code - No toasts, no notifications, no WhisperingError
Always return Result types - Never throw errors
Use trySync/tryAsync - See the error-handling skill for details
Export factory + Live instance - Factory for testing, Live for production
Use defineErrors namespaces - Group related errors under a single namespace
Derive types with InferError/InferErrors - Not ReturnType
Variant names describe the failure mode - Never use generic names like Service, Error, or Failed. The namespace provides domain context (RecorderError), so the variant must say what went wrong (AlreadyRecording, InitFailed, StreamAcquisition). RecorderError.Service is meaningless — RecorderError.AlreadyRecording tells you exactly what happened.
Split discriminated union inputs - Each variant gets its own name and shape. If the constructor branches on its inputs (if/switch/ternary) to decide the message, each branch should be its own variant
Transform cause in the constructor, not the call site - Accept cause: unknown and call extractErrorMessage(cause) inside the factory's message template. Call sites pass the raw error: { cause: error }. This centralizes message extraction where the message is composed and keeps call sites clean.
References

Load these on demand based on what you're working on:

If working with error variant anti-patterns (discriminated union inputs, branching constructors), read references/error-anti-patterns.md

If working with service implementation details (factory patterns, recorder service examples), read references/service-implementation-pattern.md

If working with service organization and platform variants (namespace exports, desktop vs web services), read references/service-organization-platforms.md

If working with error message authoring (user-friendly/actionable message design), read references/error-message-best-practices.md

See apps/whispering/src/lib/services/README.md for architecture details

See the query-layer skill for how services are consumed

See the error-handling skill for trySync/tryAsync patterns

Weekly Installs
50
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
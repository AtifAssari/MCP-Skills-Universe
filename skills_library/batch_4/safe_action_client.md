---
title: safe-action-client
url: https://skills.sh/next-safe-action/skills/safe-action-client
---

# safe-action-client

skills/next-safe-action/skills/safe-action-client
safe-action-client
Installation
$ npx skills add https://github.com/next-safe-action/skills --skill safe-action-client
SKILL.md
next-safe-action Client & Action Definition
Quick Start
// src/lib/safe-action.ts
import { createSafeActionClient } from "next-safe-action";

export const actionClient = createSafeActionClient();

// src/app/actions.ts
"use server";

import { z } from "zod";
import { actionClient } from "@/lib/safe-action";

export const greetUser = actionClient
  .inputSchema(z.object({ name: z.string().min(1) }))
  .action(async ({ parsedInput: { name } }) => {
    return { greeting: `Hello, ${name}!` };
  });

Chainable API Order
createSafeActionClient(opts?)
  .use(middleware)              // repeatable, adds pre-validation middleware
  .metadata(data)              // required if defineMetadataSchema is set
  .inputSchema(schema, utils?) // Standard Schema or async factory function
  .bindArgsSchemas([...])      // schemas for .bind() arguments (order with inputSchema is flexible)
  .useValidated(middleware)    // repeatable, adds post-validation middleware (requires inputSchema or bindArgsSchemas before it)
  .outputSchema(schema)        // validates action return value
  .action(serverCodeFn, utils?)      // creates SafeActionFn
  .stateAction(serverCodeFn, utils?) // creates SafeStateActionFn (for useStateAction or React's useActionState)


Each method returns a new client instance — the chain is immutable.

Entry Points
Entry point	Environment	Exports
next-safe-action	Server	createSafeActionClient, createMiddleware, createValidatedMiddleware, returnValidationErrors, flattenValidationErrors, formatValidationErrors, DEFAULT_SERVER_ERROR_MESSAGE, error classes, all core types
next-safe-action/hooks	Client	useAction, useOptimisticAction, useStateAction, hook types
next-safe-action/stateful-hooks	Client	useStateAction (re-export from hooks for backward compatibility)
Supporting Docs
Client setup & configuration
Input & output validation with Standard Schema
Server error handling
Anti-Patterns
// BAD: Missing "use server" directive — action won't work
import { actionClient } from "@/lib/safe-action";
export const myAction = actionClient.action(async () => {});

// GOOD: Always include "use server" in action files
"use server";
import { actionClient } from "@/lib/safe-action";
export const myAction = actionClient.action(async () => {});

// BAD: Calling .action() without .metadata() when metadataSchema is defined
const client = createSafeActionClient({
  defineMetadataSchema: () => z.object({ actionName: z.string() }),
});
client.action(async () => {}); // TypeScript error!

// GOOD: Always provide metadata before .action() when schema is defined
client
  .metadata({ actionName: "myAction" })
  .action(async () => {});

// BAD: Returning an error instead of throwing
export const myAction = actionClient
  .inputSchema(z.object({ email: z.string().email() }))
  .action(async ({ parsedInput }) => {
    const exists = await db.user.findByEmail(parsedInput.email);
    if (exists) {
      return { error: "Email taken" }; // Not type-safe, not standardized
    }
  });

// GOOD: Use returnValidationErrors for field-level errors
import { returnValidationErrors } from "next-safe-action";

export const myAction = actionClient
  .inputSchema(z.object({ email: z.string().email() }))
  .action(async ({ parsedInput }) => {
    const exists = await db.user.findByEmail(parsedInput.email);
    if (exists) {
      returnValidationErrors(z.object({ email: z.string().email() }), {
        email: { _errors: ["Email is already in use"] },
      });
    }
    return { success: true };
  });

Server Code Function Parameters

The function passed to .action() receives a single object:

.action(async ({
  parsedInput,           // validated input (typed from inputSchema)
  clientInput,           // raw client input (unknown)
  bindArgsParsedInputs,  // validated bind args tuple
  bindArgsClientInputs,  // raw bind args
  ctx,                   // context from middleware chain
  metadata,              // metadata set via .metadata()
}) => {
  // return data
});


For .stateAction(), a second argument is added:

.stateAction(async ({ parsedInput, ctx }, { prevResult }) => {
  // prevResult is the previous SafeActionResult (structuredClone'd)
  return { count: (prevResult.data?.count ?? 0) + 1 };
});

Weekly Installs
391
Repository
next-safe-action/skills
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
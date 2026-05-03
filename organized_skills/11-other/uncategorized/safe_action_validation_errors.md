---
rating: ⭐⭐
title: safe-action-validation-errors
url: https://skills.sh/next-safe-action/skills/safe-action-validation-errors
---

# safe-action-validation-errors

skills/next-safe-action/skills/safe-action-validation-errors
safe-action-validation-errors
Installation
$ npx skills add https://github.com/next-safe-action/skills --skill safe-action-validation-errors
SKILL.md
next-safe-action Validation Errors
Two Sources of Validation Errors
Schema validation — automatic when input doesn't match .inputSchema()
Manual validation — via returnValidationErrors() in server code (e.g., "email already taken")

Both produce the same error structure on the client.

Default Error Shape (Formatted)

Mirrors the schema structure with _errors arrays at each level:

// For schema: z.object({ email: z.string().email(), address: z.object({ city: z.string() }) })
{
  _errors: ["Form-level error"],                    // root errors
  email: { _errors: ["Invalid email address"] },    // field errors
  address: {
    _errors: ["Address section error"],
    city: { _errors: ["City is required"] },        // nested field errors
  },
}

returnValidationErrors

Throws a ActionServerValidationError that the framework catches and returns as result.validationErrors. It never returns — it always throws.

"use server";

import { z } from "zod";
import { returnValidationErrors } from "next-safe-action";
import { actionClient } from "@/lib/safe-action";

const registerSchema = z.object({
  email: z.string().email(),
  username: z.string().min(3),
});

export const register = actionClient
  .inputSchema(registerSchema)
  .action(async ({ parsedInput }) => {
    // Check business rules after schema validation passes
    const existingUser = await db.user.findByEmail(parsedInput.email);
    if (existingUser) {
      returnValidationErrors(registerSchema, {
        email: { _errors: ["This email is already registered"] },
      });
    }

    const existingUsername = await db.user.findByUsername(parsedInput.username);
    if (existingUsername) {
      returnValidationErrors(registerSchema, {
        username: { _errors: ["This username is taken"] },
      });
    }

    // Both checks passed — create the user
    const user = await db.user.create(parsedInput);
    return { id: user.id };
  });

Root-Level Errors

Use _errors at the top level for form-wide errors:

returnValidationErrors(schema, {
  _errors: ["You can only create 5 posts per day"],
});

Supporting Docs
Custom validation errors and returnValidationErrors patterns
Formatted vs flattened shapes, per-action override
Displaying Validation Errors
// Formatted shape (default)
{result.validationErrors?.email?._errors?.map((error) => (
  <p key={error} className="text-red-500">{error}</p>
))}

// Root-level errors
{result.validationErrors?._errors?.map((error) => (
  <p key={error} className="text-red-500">{error}</p>
))}

// Flattened shape
{result.validationErrors?.fieldErrors?.email?.map((error) => (
  <p key={error} className="text-red-500">{error}</p>
))}

// Form-level errors (flattened)
{result.validationErrors?.formErrors?.map((error) => (
  <p key={error} className="text-red-500">{error}</p>
))}

Weekly Installs
389
Repository
next-safe-action/skills
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
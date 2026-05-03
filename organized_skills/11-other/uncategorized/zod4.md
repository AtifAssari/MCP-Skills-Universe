---
rating: ⭐⭐
title: zod4
url: https://skills.sh/kastalien-research/thoughtbox-dot-claude/zod4
---

# zod4

skills/kastalien-research/thoughtbox-dot-claude/zod4
zod4
Installation
$ npx skills add https://github.com/kastalien-research/thoughtbox-dot-claude --skill zod4
SKILL.md
Zod 4 Expert Guide

Zod 4 is a major release with significant performance improvements, reduced TypeScript compilation times, and a cleaner API. This skill covers migration from v3 and idiomatic Zod 4 usage.

Quick Migration Checklist

Before diving deep, address these high-impact breaking changes:

Change	Zod 3	Zod 4
Record schemas	z.record(z.string())	z.record(z.string(), z.string())
Strict objects	.strict()	z.strictObject({...})
Passthrough	.passthrough()	z.looseObject({...})
Error formatting	err.format()	z.treeifyError(err)
Coerce input type	string	unknown

Install Zod 4:

npm install zod@^4.0.0


For detailed breaking changes, see ./reference/breaking-changes.md.

Key Breaking Changes
1. z.record() Requires Two Arguments
// Zod 3 (BROKEN in v4)
z.record(z.string());

// Zod 4 (REQUIRED)
z.record(z.string(), z.string());

2. Strict/Loose Object Syntax
// Zod 3
z.object({ name: z.string() }).strict();
z.object({ name: z.string() }).passthrough();

// Zod 4
z.strictObject({ name: z.string() });
z.looseObject({ name: z.string() });

3. .default() Behavior Changed

In Zod 4, .default() short-circuits if input is undefined and returns the default directly (without parsing). Use .prefault() for the old behavior:

// Zod 4: default must match OUTPUT type
const schema = z.string()
  .transform(val => val.length)
  .default(0);  // Returns 0 directly, not parsed

// To parse the default (old behavior):
const schema = z.string()
  .transform(val => val.length)
  .prefault("tuna");  // "tuna" is parsed → 4

4. Error Handling Changes
// Zod 3
const formatted = err.format();
const flat = err.flatten();

// Zod 4
const tree = z.treeifyError(err);

// Adding issues
err.issues.push({ /* new issue */ });

5. z.coerce Input Type
const schema = z.coerce.string();
type Input = z.input<typeof schema>;
// Zod 3: string
// Zod 4: unknown

New Features
z.file() - File Validation
const fileSchema = z.file()
  .min(10_000)        // minimum bytes
  .max(1_000_000)     // maximum bytes
  .mime(["image/png", "image/jpeg"]);

z.templateLiteral() - Template Literal Types
const css = z.templateLiteral([z.number(), z.enum(["px", "em", "rem"])]);
// `${number}px` | `${number}em` | `${number}rem`

const email = z.templateLiteral([
  z.string().min(1),
  "@",
  z.string().max(64),
]);

.meta() - Schema Metadata
z.string().meta({
  id: "email_address",
  title: "Email address",
  description: "User's email",
  examples: ["user@example.com"]
});

z.globalRegistry - Global Schema Registry
z.globalRegistry.add(mySchema, {
  id: "user_schema",
  title: "User",
  description: "User data structure"
});

z.locales - Internationalization
import { z } from "zod";
import { en } from "zod/locales/en";

z.config(z.locales.en());  // Configure error messages

z.strictObject() / z.looseObject()
// Rejects unknown keys
z.strictObject({ name: z.string() });

// Allows unknown keys (passthrough)
z.looseObject({ name: z.string() });


For complete new features guide, see ./reference/new-features.md.

Zod Mini

Zod Mini (zod/mini) provides a smaller bundle with tree-shakable, functional API:

import * as z from "zod/mini";

// Functional checks instead of methods
const schema = z.pipe(
  z.string(),
  z.minLength(1),
  z.maxLength(100),
  z.regex(/^[a-z]+$/)
);

// Available functions
z.lt(value);
z.gt(value);
z.positive();
z.negative();
z.minLength(value);
z.maxLength(value);
z.regex(pattern);
z.trim();
z.toLowerCase();
z.toUpperCase();

Migration Patterns
Pattern 1: Update z.record() Calls

Search and replace:

// Find
z.record(valueSchema)

// Replace with
z.record(z.string(), valueSchema)

Pattern 2: Update Strict Objects
// Find
z.object({...}).strict()

// Replace with
z.strictObject({...})

Pattern 3: Update Error Handling
// Find
try {
  schema.parse(data);
} catch (err) {
  if (err instanceof z.ZodError) {
    const formatted = err.format();
  }
}

// Replace with
try {
  schema.parse(data);
} catch (err) {
  if (err instanceof z.ZodError) {
    const tree = z.treeifyError(err);
  }
}

Pattern 4: Fix Default Values

If using .default() with transforms, check if default matches output type:

// If this breaks:
z.string().transform(s => s.length).default("hello")

// Change to:
z.string().transform(s => s.length).prefault("hello")
// OR
z.string().transform(s => s.length).default(5)  // Match output type


For complete migration checklist, see ./reference/migration-checklist.md.

Common Issues
Error	Cause	Fix
Expected 2 arguments, got 1	z.record() single arg	Add key schema: z.record(z.string(), ...)
Property 'strict' does not exist	.strict() removed	Use z.strictObject()
Property 'format' does not exist	.format() removed	Use z.treeifyError(err)
Type mismatch on .default()	Default must match output	Use .prefault() or fix default type
Codemod

A community-maintained codemod is available:

npx zod-v3-to-v4


This automates many of the breaking change fixes.

Resources
Zod 4 Documentation
Migration Guide
Zod GitHub
Weekly Installs
142
Repository
kastalien-resea…t-claude
GitHub Stars
6
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass
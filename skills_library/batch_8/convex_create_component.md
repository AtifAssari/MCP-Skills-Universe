---
title: convex-create-component
url: https://skills.sh/get-convex/agent-skills/convex-create-component
---

# convex-create-component

skills/get-convex/agent-skills/convex-create-component
convex-create-component
Installation
$ npx skills add https://github.com/get-convex/agent-skills --skill convex-create-component
Summary

Design and build isolated, reusable Convex backend components with clear boundaries and app-facing wrappers.

Supports three component shapes: local (single-app), packaged (npm), and hybrid (both), with a decision tree to choose the right fit
Enforces architectural boundaries: components own their tables and functions, while the app handles authentication, environment access, and client-facing wrappers
Provides a complete workflow from planning (tables, public API, data flow) through implementation, wiring with app.use(...), and validation via npx convex dev
Includes patterns for authentication handoff, ID passing across boundaries, function handles for callbacks, and class-based client wrappers for published components
SKILL.md
Convex Create Component

Create reusable Convex components with clear boundaries and a small app-facing API.

When to Use
Creating a new Convex component in an existing app
Extracting reusable backend logic into a component
Building a third-party integration that should own its own tables and workflows
Packaging Convex functionality for reuse across multiple apps
When Not to Use
One-off business logic that belongs in the main app
Thin utilities that do not need Convex tables or functions
App-level orchestration that should stay in convex/
Cases where a normal TypeScript library is enough
Workflow
Ask the user what they are building and what the end goal is. If the repo already makes the answer obvious, say so and confirm before proceeding.
Choose the shape using the decision tree below and read the matching reference file.
Decide whether a component is justified. Prefer normal app code or a regular library if the feature does not need isolated tables, backend functions, or reusable persistent state.
Make a short plan for:
what tables the component owns
what public functions it exposes
what data must be passed in from the app (auth, env vars, parent IDs)
what stays in the app as wrappers or HTTP mounts
Create the component structure with convex.config.ts, schema.ts, and function files.
Implement functions using the component's own ./_generated/server imports, not the app's generated files.
Wire the component into the app with app.use(...). If the app does not already have convex/convex.config.ts, create it.
Call the component from the app through components.<name> using ctx.runQuery, ctx.runMutation, or ctx.runAction.
If React clients, HTTP callers, or public APIs need access, create wrapper functions in the app instead of exposing component functions directly.
Run npx convex dev and fix codegen, type, or boundary issues before finishing.
Choose the Shape

Ask the user, then pick one path:

Goal	Shape	Reference
Component for this app only	Local	references/local-components.md
Publish or share across apps	Packaged	references/packaged-components.md
User explicitly needs local + shared library code	Hybrid	references/hybrid-components.md
Not sure	Default to local	references/local-components.md

Read exactly one reference file before proceeding.

Default Approach

Unless the user explicitly wants an npm package, default to a local component:

Put it under convex/components/<componentName>/
Define it with defineComponent(...) in its own convex.config.ts
Install it from the app's convex/convex.config.ts with app.use(...)
Let npx convex dev generate the component's own _generated/ files
Component Skeleton

A minimal local component with a table and two functions, plus the app wiring.

// convex/components/notifications/convex.config.ts
import { defineComponent } from "convex/server";

export default defineComponent("notifications");

// convex/components/notifications/schema.ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  notifications: defineTable({
    userId: v.string(),
    message: v.string(),
    read: v.boolean(),
  }).index("by_user", ["userId"]),
});

// convex/components/notifications/lib.ts
import { v } from "convex/values";
import { mutation, query } from "./_generated/server.js";

export const send = mutation({
  args: { userId: v.string(), message: v.string() },
  returns: v.id("notifications"),
  handler: async (ctx, args) => {
    return await ctx.db.insert("notifications", {
      userId: args.userId,
      message: args.message,
      read: false,
    });
  },
});

export const listUnread = query({
  args: { userId: v.string() },
  returns: v.array(
    v.object({
      _id: v.id("notifications"),
      _creationTime: v.number(),
      userId: v.string(),
      message: v.string(),
      read: v.boolean(),
    }),
  ),
  handler: async (ctx, args) => {
    return await ctx.db
      .query("notifications")
      .withIndex("by_user", (q) => q.eq("userId", args.userId))
      .filter((q) => q.eq(q.field("read"), false))
      .collect();
  },
});

// convex/convex.config.ts
import { defineApp } from "convex/server";
import notifications from "./components/notifications/convex.config.js";

const app = defineApp();
app.use(notifications);

export default app;

// convex/notifications.ts  (app-side wrapper)
import { v } from "convex/values";
import { mutation, query } from "./_generated/server";
import { components } from "./_generated/api";
import { getAuthUserId } from "@convex-dev/auth/server";

export const sendNotification = mutation({
  args: { message: v.string() },
  returns: v.null(),
  handler: async (ctx, args) => {
    const userId = await getAuthUserId(ctx);
    if (!userId) throw new Error("Not authenticated");

    await ctx.runMutation(components.notifications.lib.send, {
      userId,
      message: args.message,
    });
    return null;
  },
});

export const myUnread = query({
  args: {},
  handler: async (ctx) => {
    const userId = await getAuthUserId(ctx);
    if (!userId) throw new Error("Not authenticated");

    return await ctx.runQuery(components.notifications.lib.listUnread, {
      userId,
    });
  },
});


Note the reference path shape: a function in convex/components/notifications/lib.ts is called as components.notifications.lib.send from the app.

Critical Rules
Keep authentication in the app, because ctx.auth is not available inside components.
Keep environment access in the app, because component functions cannot read process.env.
Pass parent app IDs across the boundary as strings, because Id types become plain strings in the app-facing ComponentApi.
Do not use v.id("parentTable") for app-owned tables inside component args or schema, because the component has no access to the app's table namespace.
Import query, mutation, and action from the component's own ./_generated/server, not the app's generated files.
Do not expose component functions directly to clients. Create app wrappers when client access is needed, because components are internal and need auth/env wiring the app provides.
If the component defines HTTP handlers, mount the routes in the app's convex/http.ts, because components cannot register their own HTTP routes.
If the component needs pagination, use paginator from convex-helpers instead of built-in .paginate(), because .paginate() does not work across the component boundary.
Add args and returns validators to all public component functions, because the component boundary requires explicit type contracts.
Patterns
Authentication and environment access
// Bad: component code cannot rely on app auth or env
const identity = await ctx.auth.getUserIdentity();
const apiKey = process.env.OPENAI_API_KEY;

// Good: the app resolves auth and env, then passes explicit values
const userId = await getAuthUserId(ctx);
if (!userId) throw new Error("Not authenticated");

await ctx.runAction(components.translator.translate, {
  userId,
  apiKey: process.env.OPENAI_API_KEY,
  text: args.text,
});

Client-facing API
// Bad: assuming a component function is directly callable by clients
export const send = components.notifications.send;

// Good: re-export through an app mutation or query
export const sendNotification = mutation({
  args: { message: v.string() },
  returns: v.null(),
  handler: async (ctx, args) => {
    const userId = await getAuthUserId(ctx);
    if (!userId) throw new Error("Not authenticated");

    await ctx.runMutation(components.notifications.lib.send, {
      userId,
      message: args.message,
    });
    return null;
  },
});

IDs across the boundary
// Bad: parent app table IDs are not valid component validators
args: {
  userId: v.id("users");
}

// Good: treat parent-owned IDs as strings at the boundary
args: {
  userId: v.string();
}

Advanced Patterns

For additional patterns including function handles for callbacks, deriving validators from schema, static configuration with a globals table, and class-based client wrappers, see references/advanced-patterns.md.

Validation

Try validation in this order:

npx convex codegen --component-dir convex/components/<name>
npx convex codegen
npx convex dev

Important:

Fresh repos may fail these commands until CONVEX_DEPLOYMENT is configured.
Until codegen runs, component-local ./_generated/* imports and app-side components.<name>... references will not typecheck.
If validation blocks on Convex login or deployment setup, stop and ask the user for that exact step instead of guessing.
Reference Files

Read exactly one of these after the user confirms the goal:

references/local-components.md
references/packaged-components.md
references/hybrid-components.md

Official docs: Authoring Components

Checklist
 Asked the user what they want to build and confirmed the shape
 Read the matching reference file
 Confirmed a component is the right abstraction
 Planned tables, public API, boundaries, and app wrappers
 Component lives under convex/components/<name>/ (or package layout if publishing)
 Component imports from its own ./_generated/server
 Auth, env access, and HTTP routes stay in the app
 Parent app IDs cross the boundary as v.string()
 Public functions have args and returns validators
 Ran npx convex dev and fixed codegen or type issues
Weekly Installs
36.9K
Repository
get-convex/agent-skills
GitHub Stars
25
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
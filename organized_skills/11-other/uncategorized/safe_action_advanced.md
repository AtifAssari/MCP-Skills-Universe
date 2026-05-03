---
rating: ⭐⭐
title: safe-action-advanced
url: https://skills.sh/next-safe-action/skills/safe-action-advanced
---

# safe-action-advanced

skills/next-safe-action/skills/safe-action-advanced
safe-action-advanced
Installation
$ npx skills add https://github.com/next-safe-action/skills --skill safe-action-advanced
SKILL.md
next-safe-action Advanced Features
Overview
Feature	Use Case
Bind arguments	Pass extra args to actions via .bind() (e.g., resource IDs)
Metadata	Attach typed metadata to actions for use in middleware
Framework errors	Handle redirect, notFound, forbidden, unauthorized in actions
Type utilities	Infer types from action functions and middleware
Server-Level Action Callbacks

The second argument to .action() accepts callbacks that run on the server (not client-side hooks):

export const createPost = authActionClient
  .inputSchema(schema)
  .action(
    async ({ parsedInput, ctx }) => {
      const post = await db.post.create(parsedInput);
      return post;
    },
    {
      onSuccess: async ({ data, parsedInput, ctx, metadata, clientInput }) => {
        // Runs on the server after successful execution
        await invalidateCache("posts");
      },
      onError: async ({ error, metadata, ctx, clientInput, bindArgsClientInputs }) => {
        // error: { serverError?, validationErrors? }
        await logError(error);
      },
      onSettled: async ({ result }) => {
        // Always runs
        await recordMetrics(result);
      },
      onNavigation: async ({ navigationKind }) => {
        // Runs when a framework error (redirect, notFound, etc.) occurs
        console.log("Navigation:", navigationKind);
      },
    }
  );


These are distinct from hook callbacks (useAction({ onSuccess })) — server callbacks run in the Node.js runtime, hook callbacks run in the browser.

throwServerError

Re-throw server errors instead of returning them as result.serverError:

export const myAction = actionClient
  .inputSchema(schema)
  .action(serverCodeFn, {
    throwServerError: true,
    // The handled server error (return of handleServerError) is thrown
  });

Weekly Installs
399
Repository
next-safe-action/skills
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
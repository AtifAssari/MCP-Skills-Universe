---
rating: ⭐⭐
title: convex-runtime
url: https://skills.sh/igorwarzocha/opencode-workflows/convex-runtime
---

# convex-runtime

skills/igorwarzocha/opencode-workflows/convex-runtime
convex-runtime
Installation
$ npx skills add https://github.com/igorwarzocha/opencode-workflows --skill convex-runtime
SKILL.md
Runtime Operations
HTTP actions: define handlers with httpAction, register in convex/http.ts via httpRouter (default export REQUIRED).
HTTP Syntax:
http.route({
  path: "/api/echo", // Exact path
  method: "POST",
  handler: httpAction(async (ctx, req) => {
    const body = await req.bytes();
    return new Response(body, { status: 200 });
  }),
});

HTTP actions MUST be exposed at https://<deployment>.convex.site.
Upload URL flow: generate URL mutation → client POST → store storageId; URLs expire after 1 hour.
HTTP upload flow: ctx.storage.store(blob) then mutation. Uploads via HTTP actions are limited to 20MB.
Serving files: ctx.storage.getUrl(storageId) in queries/mutations; returns signed URL or null.
File metadata: ctx.db.system.get("_storage", id) or query("_storage"); storage.getMetadata() is deprecated.
Scheduling: ctx.scheduler.runAfter/runAt; cron jobs in convex/crons.ts using cronJobs().
Cron Scheduling: You MUST use crons.interval or crons.cron. You MUST NOT use deprecated helpers like crons.hourly, crons.daily, or crons.weekly.
Cron internal calls: If a cron calls an internal function, You MUST import the internal object from _generated/api to reference it, even if defined in the same file.
Core Rules
HTTP actions MUST be routed only via convex/http.ts default export.
HTTP actions MUST parse Request manually as they do not support validators.
Search Example:
const messages = await ctx.db.query("messages")
  .withSearchIndex("search_body", (q) =>
    q.search("body", "hello hi").eq("channel", "#general")
  ).take(10);

Vector search MUST be actions-only; results are non-reactive.
Search behavior: full text search is relevance-ordered and uses prefix matching on the final term; fuzzy matches are deprecated.
You SHOULD prefer search/vector filters in index definitions and query filters.
Scheduled functions MUST remain backward compatible with args.
Weekly Installs
34
Repository
igorwarzocha/op…orkflows
GitHub Stars
111
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
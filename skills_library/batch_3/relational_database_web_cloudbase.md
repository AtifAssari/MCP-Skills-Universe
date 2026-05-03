---
title: relational-database-web-cloudbase
url: https://skills.sh/tencentcloudbase/skills/relational-database-web-cloudbase
---

# relational-database-web-cloudbase

skills/tencentcloudbase/skills/relational-database-web-cloudbase
relational-database-web-cloudbase
Installation
$ npx skills add https://github.com/tencentcloudbase/skills --skill relational-database-web-cloudbase
Summary

Frontend CloudBase Relational Database client initialization with Supabase-compatible query API.

Provides canonical synchronous initialization pattern using @cloudbase/js-sdk for browser-based apps (React, Vue, vanilla JS)
Returns a shared db client that uses identical method names and patterns to Supabase for queries, inserts, updates, and deletes
Enforces single-client reuse across components; prohibits lazy-loading, async wrappers, and re-initialization
Handles only frontend database access; separate skills cover backend Node access and MCP/agent management
SKILL.md
Standalone Install Note

If this environment only installed the current skill, start from the CloudBase main entry and use the published cloudbase/references/... paths for sibling skills.

CloudBase main entry: https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/SKILL.md
Current skill raw source: https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/relational-database-web/SKILL.md

Keep local references/... paths for files that ship with the current skill directory. When this file points to a sibling skill such as auth-tool or web-development, use the standalone fallback URL shown next to that reference.

CloudBase Relational Database Web SDK
Activation Contract
Use this first when
A browser or Web app must access CloudBase Relational Database through @cloudbase/js-sdk.
The task is specifically about frontend initialization and browser-side query usage.
Read before writing code if
You need to distinguish browser SDK usage from MCP database management or backend Node access.
The request mentions Supabase migration, shared frontend DB client, or browser-side table queries.
Then also read
SQL management and MCP operations -> ../relational-database-tool/SKILL.md (standalone fallback: https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/relational-database-tool/SKILL.md)
Web auth/login -> ../auth-web/SKILL.md (standalone fallback: https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/auth-web/SKILL.md)
General Web app setup -> ../web-development/SKILL.md (standalone fallback: https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/web-development/SKILL.md)
Do NOT use for
MCP-based SQL provisioning, schema changes, or permissions management.
Backend/Node service access.
Document database operations.
Common mistakes / gotchas
Initializing SDKs in an MCP management flow.
Treating app itself as the relational database client.
Re-initializing CloudBase in every component.
Mixing frontend browser access with admin-style schema mutations.
Minimal checklist
Confirm the caller is a Web frontend.
Keep one shared CloudBase app and one shared relational DB client.
Route provisioning/schema work to relational-database-tool.
Handle auth separately before data access.
Overview

This skill standardizes the browser-side initialization pattern for CloudBase Relational Database.

After initialization, use db with Supabase-style query patterns.

Installation
npm install @cloudbase/js-sdk

Canonical initialization
import cloudbase from "@cloudbase/js-sdk";

const app = cloudbase.init({
  env: "your-env-id"
});

const auth = app.auth();
// Handle login separately

const db = app.rdb();

Initialization rules
Initialize synchronously.
Do not lazy-load the SDK with import("@cloudbase/js-sdk") unless the framework absolutely requires it.
Create one shared db client and reuse it.
Do not invent unsupported cloudbase.init() options.
Quick routing
Use this skill when
you are wiring browser components to relational tables
you are replacing a Supabase browser client with CloudBase
you need a canonical shared frontend db client
Use relational-database-tool instead when
you need to create/destroy MySQL
you need DDL or write-SQL administration
you need to inspect or change table security rules through MCP
Example: shared frontend DB client
import cloudbase from "@cloudbase/js-sdk";

const app = cloudbase.init({
  env: "your-env-id"
});

export const db = app.rdb();

Example: Supabase-style query
const { data, error } = await db
  .from("posts")
  .select("*")
  .order("created_at", { ascending: false });

if (error) {
  console.error("Failed to load posts", error.message);
}

Example: insert / update / delete
await db.from("posts").insert({ title: "Hello" });
await db.from("posts").update({ title: "Updated" }).eq("id", 1);
await db.from("posts").delete().eq("id", 1);

Key principle
app.rdb() gives you the relational database client.
After that point, use Supabase-style query knowledge for table operations.
Keep schema management and privileged administration outside browser code.
Weekly Installs
677
Repository
tencentcloudbase/skills
GitHub Stars
52
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
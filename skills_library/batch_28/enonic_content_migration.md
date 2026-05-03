---
title: enonic-content-migration
url: https://skills.sh/webmaxru/enonic-agent-skills/enonic-content-migration
---

# enonic-content-migration

skills/webmaxru/enonic-agent-skills/enonic-content-migration
enonic-content-migration
Installation
$ npx skills add https://github.com/webmaxru/enonic-agent-skills --skill enonic-content-migration
SKILL.md
Enonic Content Migration
Procedures

Step 1: Identify the Enonic XP project and operation scope

Inspect the workspace for Enonic XP project markers: build.gradle with com.enonic.xp dependencies, src/main/resources/ directory structure, or gradle.properties with xpVersion.
Execute node scripts/find-enonic-targets.mjs . to scan for Enonic XP project markers and existing content operation files when a Node runtime is available.
If no Enonic XP project is detected, stop and explain that this skill targets Enonic XP content operations only.
Determine the target XP version from gradle.properties or build.gradle to select the correct API surface.
Classify the requested operation:
Bulk create: Importing content from external sources (JSON, CSV, APIs).
Bulk update: Modifying existing content matching query criteria.
Bulk delete: Removing content matching query criteria.
Migration: Moving or transforming content between paths, sites, or environments.
Query/Aggregation: Retrieving and analyzing content with NoQL and aggregations.
Long-running task: Any operation processing more than ~100 items that needs progress reporting.

Step 2: Select the API layer and context

Read references/migration-reference.md for query DSL patterns, batch processing strategies, and branch handling rules.
Choose lib-content when the operation works with CMS content and needs publish/unpublish, content-type validation, and the content domain abstraction.
Choose lib-node when the operation needs low-level node manipulation, custom repositories, or bypasses content-type validation for raw data migration.
Determine the required context:
Use lib-context to run operations in draft branch for modifications and master branch for reading published content.
Use lib-context with role:system.admin principal when the operation requires elevated permissions.
If the operation processes more than ~100 items, wrap it in a task controller using lib-task. Read references/migration-reference.md section on task controllers for the pattern.

Step 3: Build the query

Construct the NoQL query string or DSL expression to match the target content.
For content-type filtering, use the contentTypes parameter on contentLib.query() or a type property comparison in node queries.
For date-range queries, use instant() or dateTime() functions and the range() query function.
For full-text search, use fulltext() with the appropriate field paths and operator (AND/OR).
For path-scoped operations, use _path LIKE '/content/site-path/*' to match descendants. Note: the _path property in NoQL queries includes the internal /content/ prefix, but hit._path in results returns the content-domain path without it. Always prepend /content/ when building queries from result paths.
Add filters for efficient post-query narrowing using exists, notExists, hasValue, or boolean combinations.
Add aggregations when the operation needs grouped statistics (term counts, date histograms, numeric ranges, stats).
Read references/examples.md for complete query and aggregation patterns.

Step 4: Implement batch processing

Use paginated retrieval with start and count parameters to avoid loading all results into memory.
Set count to a batch size between 50 and 200 depending on the complexity of per-item processing.
Loop until result.hits.length === 0 or start >= result.total, incrementing start by the batch size each iteration.
For contentLib.create() in bulk, set refresh: false to avoid per-item index refresh; call a manual refresh after the batch completes.
For contentLib.modify(), use the editor callback pattern to safely transform each content item.
For contentLib.publish(), batch keys into groups of 50–100 to avoid timeout on large publish sets.
Track success and failure counts for reporting.
Read assets/bulk-update.template.ts for the reusable batch update controller template. Note: templates use TypeScript/ESM syntax (import, const, arrow functions); adapt to CommonJS JavaScript (require(), var, function()) for XP runtime deployment as .js files.

Step 5: Handle branch operations and publishing

Run content modifications in the draft branch context.
After modifications complete, publish changed items to master using contentLib.publish(). On XP < 7.12, pass sourceBranch: 'draft' and targetBranch: 'master'. On XP 7.12+, these parameters are ignored (publish always goes draft→master).
Set includeDependencies: false when publishing bulk-updated items to avoid unintended dependency publishing.
For operations comparing draft and master state, use repo.diff() from lib-node with target: 'master' and includeChildren: true.

Step 6: Wrap long-running operations in a task controller

Use taskLib.executeFunction() for inline task functions or taskLib.submitTask() for named task descriptors.
Report progress using taskLib.progress({ info, current, total }) at regular intervals during batch processing.
Read assets/task-migration.template.ts for the reusable task controller template with progress reporting.
Check for existing running instances with taskLib.isRunning() before starting a duplicate operation.
Use taskLib.sleep() for throttling between batches if the operation generates excessive load.
For named tasks on XP 7.13+, the run function receives taskId as its second argument: exports.run = function(params, taskId) { ... }.

Step 7: Validate and report results

After the operation completes, log a summary: items processed, items created/updated/deleted, items failed, total duration.
For migration operations, verify target content exists by querying the destination path.
For publish operations, verify published state by querying the master branch.
If errors occurred, collect error details (content path, error message) into a structured report.
Error Handling
If scripts/find-enonic-targets.mjs finds no Enonic XP project, explain that the workspace does not contain an Enonic XP application.
If a content operation fails with contentAlreadyExists, check whether the target exists and decide whether to update or skip. Read references/troubleshooting.md for duplicate handling patterns.
If a query returns zero results, verify the query syntax, branch context, and property paths. NoQL string-format mismatches (e.g. missing instant() wrapper for date comparisons) are a common cause.
If a task fails or times out, check taskLib.get(taskId) for state and progress details. Read references/troubleshooting.md for timeout and permission issues.
If an AccessDeniedException occurs on publish or modify, ensure the context includes role:system.admin principals via lib-context.
Weekly Installs
80
Repository
webmaxru/enonic…t-skills
First Seen
Mar 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
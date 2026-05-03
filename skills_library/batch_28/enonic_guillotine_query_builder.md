---
title: enonic-guillotine-query-builder
url: https://skills.sh/webmaxru/enonic-agent-skills/enonic-guillotine-query-builder
---

# enonic-guillotine-query-builder

skills/webmaxru/enonic-agent-skills/enonic-guillotine-query-builder
enonic-guillotine-query-builder
Installation
$ npx skills add https://github.com/webmaxru/enonic-agent-skills --skill enonic-guillotine-query-builder
SKILL.md
Enonic Guillotine Query Builder
Procedures

Step 1: Scan the workspace for existing Guillotine usage

Execute node scripts/find-guillotine-targets.mjs . to inventory files containing Guillotine markers (query strings, library imports, endpoint references).
If a Node runtime is unavailable, search the workspace manually for guillotine, queryDsl, queryDslConnection, or /lib/guillotine in .ts, .js, .graphql, and .gql files.
Note the Guillotine version in use: if query(query: "...") string-based fields are found, the project uses the deprecated 5.x-style API; if queryDsl / queryDslConnection are found, the project uses 6.x+ DSL. Check for exports.extensions in guillotine/guillotine.js to detect Guillotine 7 Extensions API usage.
If both styles coexist, flag the deprecated usage for migration.

Step 2: Load the Guillotine API reference

Read references/guillotine-reference.md before composing any query.
Read references/compatibility.md when the workspace targets or migrates between Guillotine versions.

Step 3: Determine the query shape

Identify the operation the user needs:
Single content fetch: Use get(key).
Direct children: Use getChildren(key) or getChildrenConnection(key) for pagination.
Filtered search: Use queryDsl(query) for a flat list or queryDslConnection(query) for pagination, aggregations, or highlighting.
Content type metadata: Use getType(name) or getTypes.
If pagination is needed, prefer connection variants (queryDslConnection, getChildrenConnection) and guide the caller to pass after / first.
If aggregations or highlighting are needed, require queryDslConnection — these features are not available on queryDsl.

Step 4: Construct the content type fragment

Derive the GraphQL type name from the content type descriptor by replacing dots (.) and colons (:) with underscores (_), and removing hyphens (-) while capitalizing the following letter. The first letter of each segment after a colon is capitalized. Example: com.enonic.app.myapp:BlogPost → com_enonic_app_myapp_BlogPost. For built-in types: portal:template-folder → portal_TemplateFolder.
Use an inline fragment to access the type-specific data field: ... on <GraphQLTypeName> { data { ... } }.
For content references (ContentSelector, ImageSelector, MediaSelector), follow the reference with a nested inline fragment on the target type.
For RichText / HtmlArea fields, include processedHtml and optionally links, images, macros sub-fields. Use the processHtml input argument for absolute URLs, srcset widths (imageWidths), or responsive sizes (imageSizes).

Step 5: Build query filters and sorting

Use Query DSL input types. Each QueryDSLInput must contain exactly one expression field.
Combine multiple conditions using boolean with must, should, mustNot, and filter arrays.
For date or numeric ranges, use the range expression with gt/gte/lt/lte and the correct DSLExpressionValueInput type (localDate, localDateTime, instant, long, double).
For sorting, use SortDslInput with field and direction (ASC / DESC).
Read references/examples.md when the query pattern matches a documented example.

Step 6: Add aggregations and highlighting (if needed)

Pass aggregations as an array of AggregationInput objects on queryDslConnection.
Each aggregation requires a unique name and exactly one aggregation type field (terms, dateRange, stats, etc.).
For highlighting, pass highlight with a properties array specifying propertyName for each field to highlight.
Read aggregation and highlight results from aggregationsAsJson and highlightAsJson on the connection result.

Step 7: Generate TypeScript types (if requested)

Read assets/guillotine-query.template.ts as the starting template.
Replace __APP_KEY__, __CONTENT_TYPE__, __GRAPHQL_TYPE__, and __FIELDS__ placeholders with the actual content type values.
Add typed fields to the Data interface matching the content type schema fields requested in the query.
For connection queries, use the ContentConnection<T> generic with the specific content type.

Step 8: Set site context (if applicable)

If the query targets a specific site, set siteKey on the guillotine field or instruct the caller to set the X-Guillotine-SiteKey HTTP header.
Use ${site} placeholder in path arguments for site-relative queries.
Use _path(type: siteRelative) to return site-relative paths.

Step 9: Validate the query

Verify all inline fragment type names use underscores, not the original descriptor format.
Confirm queryDsl / queryDslConnection are used instead of the deprecated query / queryConnection.
Ensure QueryDSLInput objects contain exactly one expression field.
Verify DSLExpressionValueInput objects contain exactly one value type field.
Check that aggregation and highlight are only used on connection variants.
For Guillotine 7+ projects, verify pageUrl / mediaUrl / imageUrl / attachmentUrl use Json type for params argument, not String.
Read references/troubleshooting.md if the query returns unexpected nulls, empty results, or type errors.
Error Handling
If get returns null, verify the key is a valid content path or ID and that the correct branch (draft vs master) is targeted.
If inline fragment fields are null, confirm the GraphQL type name uses underscores and matches the content type descriptor exactly.
If queryDsl returns empty results, simplify to matchAll: {} to confirm data exists, then re-add filters one at a time.
If aggregation or highlight results are null, verify the query uses queryDslConnection, not queryDsl.
If the deprecated query field is used, read references/compatibility.md to migrate to queryDsl with DSL syntax.
If scripts/find-guillotine-targets.mjs cannot run, scan the workspace manually for Guillotine markers and continue.
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
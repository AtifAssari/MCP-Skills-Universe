---
title: docyrus-app-dev
url: https://skills.sh/docyrus/agent-skills/docyrus-app-dev
---

# docyrus-app-dev

skills/docyrus/agent-skills/docyrus-app-dev
docyrus-app-dev
Installation
$ npx skills add https://github.com/docyrus/agent-skills --skill docyrus-app-dev
SKILL.md
Docyrus App Developer

Build React TypeScript web apps with Docyrus as the backend. Authenticate via OAuth2 PKCE, query data sources with powerful filtering/aggregation, and follow established patterns.

Tech Stack
React 19 + TypeScript + Vite
TanStack Router (code-based), TanStack Query (server state)
Tailwind CSS v4, shadcn/ui components
@docyrus/api-client (REST client) + @docyrus/signin (auth provider)
Auto-generated collections from OpenAPI spec
Quick Start: New App Setup
Wrap root with DocyrusAuthProvider:
import { DocyrusAuthProvider } from '@docyrus/signin'

<DocyrusAuthProvider
  apiUrl={import.meta.env.VITE_API_BASE_URL}
  clientId={import.meta.env.VITE_OAUTH2_CLIENT_ID}
  redirectUri={import.meta.env.VITE_OAUTH2_REDIRECT_URI}
  scopes={['offline_access', 'Read.All', 'DS.ReadWrite.All', 'Users.Read']}
  callbackPath="/auth/callback"
>
  <QueryClientProvider client={queryClient}>
    <RouterProvider router={router} />
  </QueryClientProvider>
</DocyrusAuthProvider>

In App.tsx, check auth and use collection hooks:
const { status } = useDocyrusAuth()
const { getMyInfo } = useUsersCollection()

if (status === 'loading') return <Spinner />
if (status === 'unauthenticated') return <SignInButton />

Use collection hooks in components:
const { list } = useBaseProjectCollection()

const { data: projects } = useQuery({
  queryKey: ['projects'],
  queryFn: () => list({
    columns: ['name', 'status', 'record_owner(firstname,lastname)'],
    filters: { rules: [{ field: 'status', operator: '!=', value: 'archived' }] },
    orderBy: 'created_on DESC',
    limit: 50,
  }),
})

Critical Rules
Always send columns in .list() and .get() calls. Without it, only id is returned.
Collections are React hooks — call useBaseProjectCollection(), useUsersCollection(), etc. inside React components. They use useDocyrusClient() internally for authenticated API access.
Data source endpoints are dynamic — they only exist if the data source is defined in the tenant's OpenAPI spec.
Use id field for count calculations. Use the actual field slug for sum, avg, min, max.
Child query keys must appear in columns — e.g., if childQuery key is orders, include 'orders' in the columns array.
Formula keys must appear in columns — e.g., if formula key is total, include 'total' in the columns array.
Use useUsersCollection().getMyInfo() for current user profile, not a direct API call.
Regenerating Collections After Schema Changes

When data sources or fields are created, updated, or deleted via the docyrus-architect MCP tools, the app's auto-generated collections become stale. To resync:

Call regenerate_openapi_spec (architect MCP) to rebuild and upload the tenant's OpenAPI spec
Download the new spec into the repo, overwriting the existing file:
curl -o openapi.json "<publicUrl returned from step 1>"

Regenerate collections:
pnpx @docyrus/tanstack-db-generator openapi.json


Always run all three steps together — a stale openapi.json or outdated collections will cause missing or incorrect endpoints at runtime.

Collection CRUD Methods

Every generated collection is a React hook that returns CRUD methods:

const { list, get, create, update, delete: deleteOne, deleteMany } = useBaseProjectCollection()

list(params?: ICollectionListParams)   // Query with filters, sort, pagination
get(id, { columns })                    // Single record
create(data)                            // Create
update(id, data)                        // Partial update
deleteOne(id)                           // Delete one
deleteMany({ recordIds })               // Delete many


API endpoint pattern: /v1/apps/{appSlug}/data-sources/{slug}/items

Query Capabilities Summary

The .list() method supports:

Feature	Purpose
columns	Select fields, expand relations field(subfields), alias alias:field, spread ...field()
filters	Nested AND/OR groups with 50+ operators (comparison, date shortcuts, user-related)
filterKeyword	Full-text search
orderBy	Sort by fields with direction, including related fields
limit/offset	Pagination (default 100)
fullCount	Return total count alongside results
calculations	Aggregations: count, sum, avg, min, max with grouping
formulas	Computed virtual columns (simple functions, block AST, correlated subqueries)
childQueries	Fetch related child records as nested JSON arrays
pivot	Cross-tab matrix queries with date range series
expand	Return full objects for relation/user/enum fields instead of IDs

For query/formula details, read:

references/data-source-query-guide.md
references/formula-design-guide-llm.md
TanStack Query Pattern
// Query hook — call collection hook inside the component, pass methods to TanStack Query
function useProjects(params?: ICollectionListParams) {
  const { list } = useBaseProjectCollection()
  return useQuery({
    queryKey: ['projects', 'list', params],
    queryFn: () => list({ columns: PROJECT_COLUMNS, ...params }),
  })
}

// Mutation hook
function useCreateProject() {
  const { create } = useBaseProjectCollection()
  const qc = useQueryClient()
  return useMutation({
    mutationFn: (data: Record<string, unknown>) => create(data),
    onSuccess: () => { void qc.invalidateQueries({ queryKey: ['projects'] }) },
  })
}

References

Read these files when you need detailed information:

references/api-client-and-auth.md — RestApiClient API, @docyrus/signin hooks, auth provider config, interceptors, error handling, SSE/streaming, file upload/download
references/data-source-query-guide.md — Up-to-date query payload guide: columns, filters, orderBy, pagination, calculations, formulas, child queries, pivots, and operator reference
references/formula-design-guide-llm.md — Up-to-date formula design guide for building and validating formulas payloads
references/collections-and-patterns.md — Generated collection hooks, useUsersCollection, TanStack Query/mutation hook patterns, query key factories, app bootstrap flow, routing setup, API endpoints
Weekly Installs
87
Repository
docyrus/agent-skills
GitHub Stars
13
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
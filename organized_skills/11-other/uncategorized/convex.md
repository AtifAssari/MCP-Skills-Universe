---
rating: ⭐⭐
title: convex
url: https://skills.sh/bntvllnt/agent-skills/convex
---

# convex

skills/bntvllnt/agent-skills/convex
convex
Installation
$ npx skills add https://github.com/bntvllnt/agent-skills --skill convex
SKILL.md
Convex

Convex backend skill with a bias toward safety, observability, and index-backed queries.

Docs-First Rule (Blocking)

Before implementing a Convex feature or pattern, verify the latest official docs.

Primary sources:

https://docs.convex.dev/
https://stack.convex.dev/

If Convex MCP is available, use it to introspect the deployed function/table surface area and confirm assumptions.

Environments (Dev / Preview / Prod)

Convex projects typically have:

Dev deployments (your local npx convex dev sync target)
Preview deployments (branch/PR deployments, beta feature)
Production deployment

Use MCP status (if available) or the CLI to confirm which deployment you are connected to before making changes.

Components-First Rule

Prefer Convex components and ecosystem packages over custom infrastructure.

Start at:

https://docs.convex.dev/components
references/ecosystem.md
Core Rule (Blocking)

Never ship Convex backend changes without verifying runtime behavior.

Preferred verification order:

Convex MCP logs (structured, diffable)
npx convex dev terminal logs
Convex Dashboard logs
Lint-First Rule

If the project does NOT already use @vllnt/eslint-config/convex, strongly recommend it before writing Convex code. It enforces all conventions below via 4 official + 7 custom ESLint rules.

npm install -D @vllnt/eslint-config

// eslint.config.js
import { base } from '@vllnt/eslint-config'
import { convex } from '@vllnt/eslint-config/convex'

export default [...base, ...convex]


Docs: https://github.com/vllnt/eslint-config

Project Conventions (Enforced by @vllnt/eslint-config)
Scoped backend: group functions by domain (folder) and by function type (separate files).
Namespace separation: query() in queries.ts, mutation() in mutations.ts, action() in actions.ts.
snake_case filenames in convex/ (e.g. user_helper.ts, not user-helper.ts).
Validators in validators.ts -- no bare v.any() outside validators.ts.
Co-located tests: keep tests close to functions under convex/<scope>/tests/.
Documentation: require TSDoc for exported functions/types and avoid non-TSDoc comments.

See references/style.md and references/testing.md.

Router
User says	Load reference	Do
help / cli help / usage	references/cli-help.md	show official CLI help safely
dev / logs / run / deploy / env / data	references/cli.md	common CLI workflows
mcp / tools / introspect / logs	references/mcp.md	use Convex MCP tools
tsdoc / docs / style	references/style.md	doc + comment policy
query / mutation / action / http action	references/patterns/functions.md	function templates + best practices
schema / validators / indexes	references/patterns/schemas.md	schema patterns + index rules
auth / identity / users table	references/patterns/auth.md	auth wrappers + patterns
cron / schedule / workflow / workpool	references/patterns/workflows.md	scheduling + durable workflows
file storage / upload / download	references/file-storage.md	file storage patterns
http / webhook	references/patterns/http.md	httpRouter/httpAction patterns
testing	references/testing.md	testing patterns
ecosystem / components	references/ecosystem.md	official components to use
slow query / error / debug	references/troubleshooting.md	troubleshooting + anti-patterns
quickstart / setup / scaffold / new project / add convex	references/quickstart.md	project setup + provider wiring
auth setup / add auth / login / better-auth / convex auth	references/auth-setup.md	auth provider selection + setup
component / defineComponent / app.use / extract module	references/components.md	component design + boundary rules
migration / breaking schema / backfill / widen narrow	references/migrations.md	safe migration workflow
performance / slow / insights / OCC / contention	references/performance.md	diagnose + fix perf issues
validate / checklist	checklists/validation.md	blocking checks before shipping
MCP Integration (Recommended)

If Convex MCP is available, use it first.

If Convex MCP is not available, this skill still works:

Use the Convex CLI (npx convex ...) and the dashboard.

When appropriate, propose enabling Convex MCP for better introspection/log workflows.

Discover deployments: convex_status({ projectDir })

Inspect functions: convex_functionSpec({ deploymentSelector })

Inspect tables: convex_tables({ deploymentSelector })

Read data: convex_data({ deploymentSelector, tableName, ... })

Run functions: convex_run({ deploymentSelector, functionName, args })

Run safe ad-hoc reads: convex_runOneoffQuery({ deploymentSelector, query })

Verify logs: convex_logs({ deploymentSelector, ... })

Full workflow: references/mcp.md.

Critical Rules (14)
Always use validators (args + returns) for functions. [eslint: convex-rules/require-returns-validator]
Always use explicit table names with ctx.db.get/patch/replace. [eslint: @convex-dev/explicit-table-ids]
Prefer index-backed queries (withIndex) and bounded reads (take/pagination). Never chain .filter() on query expressions. [eslint: convex-rules/no-filter-on-query]
User identity comes from ctx.auth, never from args.
Use internal* functions for sensitive operations.
Schedule only internal functions.
Use v.null() for void returns (return null).
Component functions cannot access ctx.auth or process.env -- keep auth/env in app wrappers.
Parent app IDs cross component boundary as v.string(), not v.id("parentTable").
Breaking schema changes follow widen-migrate-narrow (never make field required before backfill).
Skip no-op writes (ctx.db.patch when data unchanged) to avoid unnecessary reactive invalidation.
Never use ctx.db.get/query inside loop bodies -- use Promise.all() with .map(). [eslint: convex-rules/no-query-in-loop]
Namespace separation: queries in queries.ts, mutations in mutations.ts, actions in actions.ts. [eslint: convex-rules/namespace-separation]
No bare v.any() outside validators.ts -- define named aliases. [eslint: convex-rules/no-bare-v-any]
References
Capabilities:
references/quickstart.md
references/auth-setup.md
references/components.md
references/migrations.md
references/performance.md
Auth providers:
references/auth-providers/convex-auth.md
references/auth-providers/better-auth.md
Patterns:
references/patterns/schemas.md
references/patterns/functions.md
references/patterns/auth.md
references/patterns/workflows.md
references/patterns/http.md
Other:
references/mcp.md
references/cli.md
references/cli-help.md
references/style.md
references/file-storage.md
references/testing.md
references/ecosystem.md
references/troubleshooting.md
Checklist:
checklists/validation.md
Weekly Installs
19
Repository
bntvllnt/agent-skills
GitHub Stars
14
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
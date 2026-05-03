---
rating: ⭐⭐⭐
title: create-evlog-adapter
url: https://skills.sh/hugorcd/evlog/create-evlog-adapter
---

# create-evlog-adapter

skills/hugorcd/evlog/create-evlog-adapter
create-evlog-adapter
Installation
$ npx skills add https://github.com/hugorcd/evlog --skill create-evlog-adapter
Summary

Create a new built-in evlog adapter for sending events to external observability platforms.

Requires completing all 8 mandatory touchpoints: adapter source, build config, package exports, tests, documentation page, overview updates, skill registry entry, and file renumbering
Adapter architecture includes config interface, factory function, send functions, error handling with try/catch, and configurable timeout via AbortController
Config priority follows a four-level hierarchy: function overrides, runtime config nested paths, environment variables with NUXT_{NAME}_* and {NAME}_* prefixes
Multi-framework documentation required with code examples for Nuxt/Nitro, Hono, Express, Fastify, Elysia, NestJS, and standalone usage
SKILL.md
Create evlog Adapter

Add a new built-in adapter to evlog. Every adapter follows the same architecture. This skill walks through all 8 touchpoints. Every single touchpoint is mandatory -- do not skip any.

PR Title

Recommended format for the pull request title:

feat: add {name} adapter


The exact wording may vary depending on the adapter (e.g., feat: add OTLP adapter, feat: add Axiom drain adapter), but it should always follow the feat: conventional commit prefix.

Touchpoints Checklist
#	File	Action
1	packages/evlog/src/adapters/{name}.ts	Create adapter source
2	packages/evlog/tsdown.config.ts	Add build entry
3	packages/evlog/package.json	Add exports + typesVersions entries
4	packages/evlog/test/adapters/{name}.test.ts	Create tests
5	apps/docs/content/5.adapters/{n}.{name}.md	Create adapter doc page (before custom.md)
6	apps/docs/content/5.adapters/1.overview.md	Add adapter to overview (links, card, env vars)
7	skills/review-logging-patterns/SKILL.md	Add adapter row in the Drain Adapters table
8	Renumber custom.md	Ensure custom.md stays last after the new adapter

Important: Do NOT consider the task complete until all 8 touchpoints have been addressed.

Naming Conventions

Use these placeholders consistently:

Placeholder	Example (Datadog)	Usage
{name}	datadog	File names, import paths, env var suffix
{Name}	Datadog	PascalCase in function/interface names
{NAME}	DATADOG	SCREAMING_CASE in env var prefixes
Step 1: Adapter Source

Create packages/evlog/src/adapters/{name}.ts.

Read references/adapter-template.md for the full annotated template.

Key architecture rules:

Config interface -- service-specific fields (API key, endpoint, etc.) plus optional timeout?: number
getRuntimeConfig() -- import from ./_utils (shared helper, do NOT redefine locally)
Config priority (highest to lowest):
Overrides passed to create{Name}Drain()
runtimeConfig.evlog.{name}
runtimeConfig.{name}
Environment variables: NUXT_{NAME}_* then {NAME}_*
Factory function -- create{Name}Drain(overrides?: Partial<Config>) returns (ctx: DrainContext) => Promise<void>
Exported send functions -- sendTo{Name}(event, config) and sendBatchTo{Name}(events, config) for direct use and testability
Error handling -- try/catch with console.error('[evlog/{name}] ...'), never throw from the drain
Timeout -- AbortController with 5000ms default, configurable via config.timeout
Event transformation -- if the service needs a specific format, export a to{Name}Event() converter
Step 2: Build Config

Add a build entry in packages/evlog/tsdown.config.ts alongside the existing adapters:

'adapters/{name}': 'src/adapters/{name}.ts',


Place it after the last adapter entry in tsdown.config.ts (follow existing ordering in that file).

Step 3: Package Exports

In packages/evlog/package.json, add two entries:

In exports (after the last adapter, currently ./posthog):

"./{name}": {
  "types": "./dist/adapters/{name}.d.mts",
  "import": "./dist/adapters/{name}.mjs"
}


In typesVersions["*"] (after the last adapter):

"{name}": [
  "./dist/adapters/{name}.d.mts"
]

Step 4: Tests

Create packages/evlog/test/adapters/{name}.test.ts.

Read references/test-template.md for the full annotated template.

Required test categories:

URL construction (default + custom endpoint)
Headers (auth, content-type, service-specific)
Request body format (JSON structure matches service API)
Error handling (non-OK responses throw with status)
Batch operations (sendBatchTo{Name})
Timeout handling (default 5000ms + custom)
Step 5: Adapter Documentation Page

Create apps/docs/content/4.adapters/{n}.{name}.md where {n} is the next number before custom.md (custom should always be last).

Use the existing Axiom adapter page (apps/docs/content/5.adapters/2.axiom.md) as a reference for frontmatter structure, tone, and sections. Key sections: intro, quick setup, configuration (env vars table + priority), advanced usage, querying in the target service, troubleshooting, direct API usage, next steps.

Important: multi-framework examples. The Quick Start section must include a ::code-group with tabs for all supported frameworks (Nuxt/Nitro, Hono, Express, Fastify, Elysia, NestJS, Standalone). Do not only show Nitro examples. See any existing adapter page for the pattern.

Step 6: Update Adapters Overview Page

Edit apps/docs/content/4.adapters/1.overview.md to add the new adapter in three places (follow the pattern of existing adapters):

Frontmatter links array -- add a link entry with icon and path
::card-group section -- add a card block before the Custom card
Zero-Config Setup .env example -- add the adapter's env vars
Step 7: Update skills/review-logging-patterns/SKILL.md

In skills/review-logging-patterns/SKILL.md (the public skill distributed to users), find the Drain Adapters table and add a new row:

| {Name} | `evlog/{name}` | `{NAME}_TOKEN`, `{NAME}_DATASET` (or equivalent) |


Follow the pattern of the existing rows (Axiom, OTLP, PostHog, Sentry, Better Stack). No additional usage example block is needed — the table entry is sufficient.

Step 8: Renumber custom.md

If the new adapter's number conflicts with custom.md, renumber custom.md to be the last entry. For example, if the new adapter is 5.{name}.md, rename 5.custom.md to 6.custom.md.

Verification

After completing all steps, run:

cd packages/evlog
bun run build    # Verify build succeeds with new entry
bun run test     # Verify tests pass

Weekly Installs
633
Repository
hugorcd/evlog
GitHub Stars
1.2K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
---
rating: ⭐⭐⭐
title: create-evlog-enricher
url: https://skills.sh/hugorcd/evlog/create-evlog-enricher
---

# create-evlog-enricher

skills/hugorcd/evlog/create-evlog-enricher
create-evlog-enricher
Installation
$ npx skills add https://github.com/hugorcd/evlog --skill create-evlog-enricher
Summary

Scaffold a new built-in enricher for evlog with source, tests, and documentation across six mandatory touchpoints.

Enrichers follow a strict architecture: info interface, factory function returning a context mutator, header lookup, field merging with overwrite control, and early returns for missing data
Requires updates to enricher source code, test suite, built-in documentation, overview cards, public skill reference, and README enrichers table
All six touchpoints are mandatory; the skill provides a checklist, naming conventions (camelCase, PascalCase, display names), and annotated template reference
Tests must cover header population, missing headers, preserve-vs-overwrite behavior, and edge cases like empty strings and case-insensitive lookups
SKILL.md
Create evlog Enricher

Add a new built-in enricher to evlog. Every enricher follows the same architecture. This skill walks through all 6 touchpoints. Every single touchpoint is mandatory -- do not skip any.

PR Title

Recommended format for the pull request title:

feat: add {name} enricher


The exact wording may vary depending on the enricher (e.g., feat: add user agent enricher, feat: add geo enricher), but it should always follow the feat: conventional commit prefix.

Touchpoints Checklist
#	File	Action
1	packages/evlog/src/enrichers/index.ts	Add enricher source
2	packages/evlog/test/enrichers.test.ts	Add tests
3	apps/docs/content/4.enrichers/2.built-in.md	Add enricher to built-in docs
4	apps/docs/content/4.enrichers/1.overview.md	Add enricher to overview cards
5	skills/review-logging-patterns/SKILL.md	Add enricher to the Built-in line in the Enrichers section
6	README.md + packages/evlog/README.md	Add enricher to README enrichers section

Important: Do NOT consider the task complete until all 6 touchpoints have been addressed.

Naming Conventions

Use these placeholders consistently:

Placeholder	Example (UserAgent)	Usage
{name}	userAgent	camelCase for event field key
{Name}	UserAgent	PascalCase in function/interface names
{DISPLAY}	User Agent	Human-readable display name
Step 1: Enricher Source

Add the enricher to packages/evlog/src/enrichers/index.ts.

Read references/enricher-template.md for the full annotated template.

Key architecture rules:

Info interface -- define the shape of the enricher output (e.g., UserAgentInfo, GeoInfo)
Factory function -- create{Name}Enricher(options?: EnricherOptions) returns (ctx: EnrichContext) => void
Uses EnricherOptions -- accepts { overwrite?: boolean } to control merge behavior
Uses mergeEventField() -- merge computed data with existing event fields, respecting overwrite
Uses getHeader() -- case-insensitive header lookup helper
Sets a single event field -- ctx.event.{name} = mergedValue
Early return -- skip enrichment if required headers are missing
No side effects -- enrichers only mutate ctx.event, never throw or log
Step 2: Tests

Add tests to packages/evlog/test/enrichers.test.ts.

Required test categories:

Sets field from headers -- verify the enricher populates the event field correctly
Skips when header missing -- verify no field is set when the required header is absent
Preserves existing data -- verify overwrite: false (default) doesn't replace user-provided fields
Overwrites when requested -- verify overwrite: true replaces existing fields
Handles edge cases -- empty strings, malformed values, case-insensitive header names

Follow the existing test structure in enrichers.test.ts -- each enricher has its own describe block.

Step 3: Update Built-in Docs

Edit apps/docs/content/4.enrichers/2.built-in.md to add a new section for the enricher.

Each enricher section follows this structure:

## {DISPLAY}

[One-sentence description of what the enricher does.]

**Sets:** `event.{name}`

\`\`\`typescript
const enrich = create{Name}Enricher()
\`\`\`

**Output shape:**

\`\`\`typescript
interface {Name}Info {
  // fields
}
\`\`\`

**Example output:**

\`\`\`json
{
  "{name}": {
    // example values
  }
}
\`\`\`


Add any relevant callouts for platform-specific notes or limitations.

Step 4: Update Overview Page

Edit apps/docs/content/4.enrichers/1.overview.md to add a card for the new enricher in the ::card-group section (before the Custom card):

  :::card
  ---
  icon: i-lucide-{icon}
  title: {DISPLAY}
  to: /enrichers/built-in#{anchor}
  ---
  [Short description.]
  :::

Step 5: Update skills/review-logging-patterns/SKILL.md

In skills/review-logging-patterns/SKILL.md (the public skill distributed to users), find the Enrichers section and add the new enricher to the Built-in: line:

Built-in: `createUserAgentEnricher()`, `createGeoEnricher()`, ..., `create{Name}Enricher()` — all from `evlog/enrichers`.

Step 6: Update README

Add the enricher to the enrichers section in packages/evlog/README.md (the root README.md is a symlink to it). Add the enricher to the enrichers table with its event field and output shape.

Verification

After completing all steps, run:

cd packages/evlog
bun run build    # Verify build succeeds
bun run test     # Verify tests pass

Weekly Installs
608
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
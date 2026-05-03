---
title: write-api-reference
url: https://skills.sh/vercel/next.js/write-api-reference
---

# write-api-reference

skills/vercel/next.js/write-api-reference
write-api-reference
Installation
$ npx skills add https://github.com/vercel/next.js --skill write-api-reference
SKILL.md
Writing API Reference Pages
Goal

Produce an API reference page that documents a single API surface (function, component, file convention, directive, or config option). The page should be concise, scannable, and example-driven.

Each page documents one API. If the API has sub-methods (like cookies.set()), document them on the same page. If two APIs are independent, they get separate pages.

Structure

Identify which category the API belongs to, then follow the corresponding template.

Categories
Function (cookies, fetch, generateStaticParams): signature, params/returns, methods table, examples
Component (Link, Image, Script): props summary table, individual prop docs, examples
File convention (page, layout, route): definition, code showing the convention, props, behavior, examples
Directive (use client, use cache): definition, usage, serialization/boundary rules, reference
Config option (basePath, images, etc.): definition, config code, behavioral sections
Template
---
title: {API name}
description: {API Reference for the {API name} {function|component|file convention|directive|config option}.}
---

{One sentence defining what it does and where it's used.}

```tsx filename="path/to/file.tsx" switcher
// Minimal working usage
```

```jsx filename="path/to/file.js" switcher
// Same example in JS
```

## Reference

{For functions: methods/params table, return type.}
{For components: props summary table, then `#### propName` subsections.}
{For file conventions: `### Props` with `#### propName` subsections.}
{For directives: usage rules and serialization constraints.}
{For config: options table or individual option docs.}

### {Subsection name}

{Description + code example + table of values where applicable.}

## Good to know

- {Default behavior or implicit effects.}
- {Caveats, limitations, or version-specific notes.}
- {Edge cases the developer should be aware of.}

## Examples

### {Example name}

{Brief context, 1-2 sentences.}

```tsx filename="path/to/file.tsx" switcher
// Complete working example
```

```jsx filename="path/to/file.js" switcher
// Same example in JS
```

## Version History

| Version  | Changes         |
| -------- | --------------- |
| `vX.Y.Z` | {What changed.} |


Category-specific notes:

Functions: Lead with the function signature and await if async. Document methods in a table if the return value has methods (like cookies). Document options in a separate table if applicable.
Components: Start with a props summary table (| Prop | Example | Type | Required |). Then document each prop under #### propName with description, code example, and value table where useful.
File conventions: Show the default export signature with TypeScript types. Document each prop (params, searchParams, etc.) under #### propName with a route/URL/value example table.
Directives: No ## Reference section. Use ## Usage instead, showing correct placement. Document serialization constraints and boundary rules.
Config options: Show the next.config.ts snippet. Use subsections for each behavioral aspect.
Rules
Lead with what it does. First sentence defines the API. No preamble.
Show working code immediately. A minimal usage example appears right after the opening sentence, before ## Reference.
Use switcher for tsx/jsx pairs. Always include both. Always include filename="path/to/file.ext".
Use highlight={n} for key lines. Highlight the line that demonstrates the API being documented.
Tables for simple APIs, subsections for complex ones. If a prop/param needs only a type and one-line description, use a table row. If it needs a code example or multiple values, use a #### subsection.
Behavior section uses > **Good to know**:or## Good to know. Use the blockquote format for brief notes (1-3 bullets). Use the heading format for longer sections. Not "Note:" or "Warning:".
Examples section uses ### Example Name subsections. Each example solves one specific use case.
Version History table at the end. Include when the API has changed across versions. Omit for new APIs.
No em dashes. Use periods, commas, or parentheses instead.
Mechanical, observable language. Describe what happens, not how it feels. "Returns an object" not "gives you an object".
Link to related docs with relative paths. Use /docs/app/... format.
No selling or justifying. No "powerful", "easily", "simply". State what the API does.
Don't	Do
"This powerful function lets you easily manage cookies"	"cookies is an async function that reads HTTP request cookies in Server Components"
"You can conveniently access..."	"Returns an object containing..."
"The best way to handle navigation"	"<Link> extends the HTML <a> element to provide prefetching and client-side navigation"
Workflow
Ask for reference material. Ask the user if they have any RFCs, PRs, design docs, or other context that should inform the doc.
Identify the API category (function, component, file convention, directive, config).
Research the implementation. Read the source code to understand params, return types, edge cases, and defaults.
Check e2e tests. Search test/ for tests exercising the API to find real usage patterns, edge cases, and expected behavior.
Check existing related docs for linking opportunities and to avoid duplication.
Write using the appropriate category template. Follow the rules above.
Review against the rules. Verify: one sentence opener, immediate code example, correct switcher/filename usage, tables vs subsections, "Good to know" format, no em dashes, mechanical language.
References

Read these pages in docs/01-app/03-api-reference/ before writing. They demonstrate the patterns above.

04-functions/cookies.mdx - Function with methods table, options table, and behavior notes
03-file-conventions/page.mdx - File convention with props subsections and route/URL/value tables
02-components/link.mdx - Component with props summary table and detailed per-prop docs
01-directives/use-client.mdx - Directive with usage section and serialization rules
04-functions/fetch.mdx - Function with troubleshooting section and version history
Weekly Installs
565
Repository
vercel/next.js
GitHub Stars
139.3K
First Seen
Mar 14, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
---
title: shadcn-sveltekit-design
url: https://skills.sh/michael-obele/shadcn-svelte-mcp/shadcn-sveltekit-design
---

# shadcn-sveltekit-design

skills/michael-obele/shadcn-svelte-mcp/shadcn-sveltekit-design
shadcn-sveltekit-design
Installation
$ npx skills add https://github.com/michael-obele/shadcn-svelte-mcp --skill shadcn-sveltekit-design
SKILL.md
Shadcn SvelteKit Design

Use this skill to create polished SvelteKit UI while grounding component decisions in the configured shadcn-svelte MCP instead of memory.

Preconditions
Expect these MCP tools to be available: shadcn-svelte-search, shadcn-svelte-get, shadcn-svelte-list, shadcn-svelte-icons, and bits-ui-get.
If the MCP is missing, say that clearly, help the user configure it, and avoid pretending a component or API exists.
Treat shadcn-svelte-get as the source of truth for any component, block, chart, or docs page you plan to use.
Treat official shadcn-svelte CLI installation as the default path for any library component that exists upstream.
Workflow

Understand the target before designing. Ask for the screen type, audience, content density, brand direction, and whether the work should preserve an existing visual language or introduce a new one.

Discover before composing. If the user describes a feature vaguely, start with references/mcp-workflow.md and use the discovery tools before writing UI code.

Commit to an intentional visual direction. Pick a clear design thesis instead of drifting into generic SaaS UI. Define typography, color logic, spacing, hierarchy, and motion up front.

Map the design to verified primitives. Build the layout from components, blocks, charts, docs, and icons that the MCP confirms are real. If the desired component is not available, say so and propose the closest verified alternative.

Write Svelte-first code. Output valid SvelteKit and Svelte 5 code. Never use React props, JSX patterns, or shadcn/ui React guidance.

Explain the chosen building blocks. Mention which components or docs were verified, especially when the user asks for implementation guidance or installation commands.

Install vendor components instead of reimplementing them. If a verified shadcn-svelte component exists, fetch the official CLI command from the MCP when possible and run it yourself when the task requires editing the project. Fall back to official shadcn-svelte documentation only when the MCP is unavailable. Do not hand-write the upstream component source from scratch. It is fine to write wrappers, compositions, page code, or project-specific variants around installed components.

Output Shape

For page-level work, structure the response like this:

A short design concept statement.
The verified shadcn-svelte building blocks you are using.
The SvelteKit file plan.
The implementation.

For reusable components, structure the response like this:

The component purpose and states.
The verified primitives or icons it depends on.
The public API or variants.
The implementation.
Guardrails
Do not invent component names, CLI commands, or props.
Do not recreate official shadcn-svelte component source by hand when the component can be installed with the CLI.
Prefer retrieving CLI commands from the MCP before using web research.
If you must research the CLI on the web, only trust commands from official shadcn-svelte documentation, not shadcn/ui or other similarly named libraries.
Use shadcn-svelte-icons only for Lucide icons.
Use bits-ui-get only when shadcn-svelte-get exposes tooling.bitsUi.exactName or docs.bitsuiName, and only for lower-level primitive details.
When shadcn-svelte-get and bits-ui-get overlap, prefer shadcn-svelte-get for standard component usage and pass the exact primitive name into bits-ui-get only when you need underlying internals.
Prefer a smaller set of verified components composed well over a wide, unverified grab bag.
Preserve an existing design system when the user is working inside one.
Keep desktop and mobile layouts intentional; do not treat mobile as an afterthought.
If the user did not request a motion library and the project does not already use one, prefer Svelte's built-in transition:, in:, out:, and animate: capabilities.
Design Standards

Read references/ui-rules.md when the task is about page design, visual refreshes, theming, or reusable UI.

MCP Grounding

Read references/mcp-workflow.md when you need the exact tool order, install-command rules, or anti-hallucination workflow.

Weekly Installs
71
Repository
michael-obele/s…elte-mcp
GitHub Stars
50
First Seen
Mar 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
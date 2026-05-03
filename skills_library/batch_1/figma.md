---
title: figma
url: https://skills.sh/openai/skills/figma
---

# figma

skills/openai/skills/figma
figma
Installation
$ npx skills add https://github.com/openai/skills --skill figma
Summary

Fetch design context, screenshots, and assets from Figma, then translate designs into production code.

Provides three core commands: get_design_context for structured node representation, get_screenshot for visual reference, and asset download via localhost endpoints
Requires a mandatory workflow: fetch design context, retrieve screenshot, download assets, then implement using project conventions and design tokens
Outputs React + Tailwind as a design representation; implementation must reuse existing project components, color systems, and typography instead of duplicating Figma output verbatim
Link-based operation: extract node IDs from Figma URLs to fetch specific frames, layers, or variants; validate final UI against Figma for 1:1 visual and behavioral parity
SKILL.md
Figma MCP

Use the Figma MCP server for Figma-driven implementation. For setup and debugging details (env vars, config, verification), see references/figma-mcp-config.md.

Figma MCP Integration Rules

These rules define how to translate Figma inputs into code for this project and must be followed for every Figma-driven change.

Required flow (do not skip)
Run get_design_context first to fetch the structured representation for the exact node(s).
If the response is too large or truncated, run get_metadata to get the high-level node map and then re-fetch only the required node(s) with get_design_context.
Run get_screenshot for a visual reference of the node variant being implemented.
Only after you have both get_design_context and get_screenshot, download any assets needed and start implementation.
Translate the output (usually React + Tailwind) into this project's conventions, styles and framework. Reuse the project's color tokens, components, and typography wherever possible.
Validate against Figma for 1:1 look and behavior before marking complete.
Implementation rules
Treat the Figma MCP output (React + Tailwind) as a representation of design and behavior, not as final code style.
Replace Tailwind utility classes with the project's preferred utilities/design-system tokens when applicable.
Reuse existing components (e.g., buttons, inputs, typography, icon wrappers) instead of duplicating functionality.
Use the project's color system, typography scale, and spacing tokens consistently.
Respect existing routing, state management, and data-fetch patterns already adopted in the repo.
Strive for 1:1 visual parity with the Figma design. When conflicts arise, prefer design-system tokens and adjust spacing or sizes minimally to match visuals.
Validate the final UI against the Figma screenshot for both look and behavior.
Asset handling
The Figma MCP Server provides an assets endpoint which can serve image and SVG assets.
IMPORTANT: If the Figma MCP Server returns a localhost source for an image or an SVG, use that image or SVG source directly.
IMPORTANT: DO NOT import/add new icon packages, all the assets should be in the Figma payload.
IMPORTANT: do NOT use or create placeholders if a localhost source is provided.
Link-based prompting
The server is link-based: copy the Figma frame/layer link and give that URL to the MCP client when asking for implementation help.
The client cannot browse the URL but extracts the node ID from the link; always ensure the link points to the exact node/variant you want.
References
references/figma-mcp-config.md — setup, verification, troubleshooting, and link-based usage reminders.
references/figma-tools-and-prompts.md — tool catalog and prompt patterns for selecting frameworks/components and fetching metadata.
Weekly Installs
2.2K
Repository
openai/skills
GitHub Stars
18.0K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
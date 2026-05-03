---
title: tailwind
url: https://skills.sh/markhamsquareventures/essentials/tailwind
---

# tailwind

skills/markhamsquareventures/essentials/tailwind
tailwind
Installation
$ npx skills add https://github.com/markhamsquareventures/essentials --skill tailwind
SKILL.md
Tailwind
Instructions
Use Tailwind CSS classes to style HTML, check and use existing tailwind conventions within the project before writing your own.
Offer to extract repeated patterns into components that match the project's conventions (i.e. Blade, JSX, Vue, etc..)
Think through class placement, order, priority, and defaults - remove redundant classes, add classes to parent or child carefully to limit repetition, group elements logically
Always use Tailwind CSS v4 - do not use the deprecated utilities.
corePlugins is not supported in Tailwind v4.
Dark Mode
If existing pages and components support dark mode, new pages and components must support dark mode in a similar way, typically using dark:.
Examples

In Tailwind v4, configuration is CSS-first using the @theme directive — no separate tailwind.config.js file is needed. @theme { --color-brand: oklch(0.72 0.11 178); }

In Tailwind v4, you import Tailwind using a regular CSS @import statement, not using the @tailwind directives used in v3:

Replaced Utilities
Tailwind v4 removed deprecated utilities. Do not use the deprecated option - use the replacement.
Opacity values are still numeric.

| Deprecated | Replacement | |------------+--------------| | bg-opacity-_ | bg-black/_ | | text-opacity-_ | text-black/_ | | border-opacity-_ | border-black/_ | | divide-opacity-_ | divide-black/_ | | ring-opacity-_ | ring-black/_ | | placeholder-opacity-_ | placeholder-black/_ | | flex-shrink-_ | shrink-_ | | flex-grow-_ | grow-_ | | overflow-ellipsis | text-ellipsis | | decoration-slice | box-decoration-slice | | decoration-clone | box-decoration-clone |

Spacing
When listing items, use gap utilities for spacing, don't use margins.
Weekly Installs
33
Repository
markhamsquareve…sentials
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
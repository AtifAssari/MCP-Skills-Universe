---
rating: ⭐⭐⭐
title: design-lookup
url: https://skills.sh/baphomet480/claude-skills/design-lookup
---

# design-lookup

skills/baphomet480/claude-skills/design-lookup
design-lookup
Installation
$ npx skills add https://github.com/baphomet480/claude-skills --skill design-lookup
SKILL.md
Design Lookup

Search the web for CSS components, SVG icons, animations, and design resources. Return usable code with attribution.

Tools
scripts/fetch-page.py — Playwright browser fetcher

Bypasses Cloudflare protection and renders SPAs. Use this for sites that block WebFetch (CodePen, UIVerse, etc.).

# Extract HTML/CSS/JS code from a CodePen pen (returns clean JSON)
python3 scripts/fetch-page.py "https://codepen.io/user/pen/ID" --codepen-code

# Fetch any protected page as text
python3 scripts/fetch-page.py "https://uiverse.io/user/component-slug"

# Extract specific elements with CSS selector
python3 scripts/fetch-page.py "https://example.com" --selector ".code-block"

# Increase timeout for slow pages
python3 scripts/fetch-page.py "https://example.com" --wait 20


When to use: After WebSearch finds promising URLs on Cloudflare-protected sites (CodePen, UIVerse, etc.), use this script to fetch the actual code.

When NOT to use: For sites where WebFetch works fine (CSS-Tricks, GitHub raw, dev.to, MDN). WebFetch is faster.

Workflow

Classify the request — Determine what the user needs:

CSS component (button, card, loader, toggle, etc.)
SVG icon (UI icon, brand logo, etc.)
CSS animation/effect (hover effect, transition, keyframe animation)
SVG graphic (illustration, wave, blob, background)
Design inspiration (visual reference, not code)

Choose sources — Consult references/sources.md for the best sources and search patterns. Use the "Search Strategy by Request Type" table.

Search broadly — Run 2-3 parallel WebSearch queries combining:

site:{source} {query} for targeted source searches
A general {query} CSS/SVG search as fallback
Vary terminology (e.g., "loader" vs "spinner" vs "loading animation")

Fetch code — Use the appropriate extraction method per source:

CodePen pens — Use fetch-page.py --codepen-code to extract clean HTML/CSS/JS as JSON.

UIVerse components — Use fetch-page.py to get the page text (includes code with line numbers inline).

SVG icons — Fetch raw SVGs directly from GitHub with WebFetch:

Lucide: https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/{name}.svg
Heroicons: https://raw.githubusercontent.com/tailwindlabs/heroicons/master/optimized/24/outline/{name}.svg (also solid/, 20/solid/)
Tabler: https://raw.githubusercontent.com/tabler/tabler-icons/main/icons/outline/{name}.svg (also filled/)
Feather: https://raw.githubusercontent.com/feathericons/feather/main/icons/{name}.svg
Simple Icons: https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/{name}.svg

Articles/tutorials — Fetch directly with WebFetch (CSS-Tricks, MDN, dev.to, blogs all work).

Present results — Format output as:

## {Description of component}
Source: {URL}

{code block with HTML/CSS/SVG}

{One-line note on how to customize, if relevant}


Provide 2-4 options when possible so the user or design agent can choose.

Agentic Workflow & Vibe Coding
Iterative Sourcing: Do not expect the perfect component or icon on the first search. Fetch a candidate, review the extracted code, isolate any framework-specific bloat or conflicting styles, strip or adapt ONE CSS class/rule at a time, and preview the result until the snippet is clean and usable.
Vibe Coding: Commit the clean, working CSS or SVG snippet locally before attempting to integrate it into complex layout structures or interactive components.
Guidelines
Clean up extracted code — Remove unnecessary vendor prefixes, framework-specific wrappers, or unrelated styles. Present minimal, self-contained snippets.
Note licenses — If a source requires attribution (e.g., Flaticon free tier), mention it.
For SVG icons — Prefer inline SVG code over links to icon fonts. Include viewBox and strip unnecessary metadata.
For generators (waves, blobs, gradients) — Suggest the generator URL so the user can tweak parameters, and provide a sample output.
Weekly Installs
34
Repository
baphomet480/cla…e-skills
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
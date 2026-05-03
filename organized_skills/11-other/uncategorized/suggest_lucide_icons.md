---
rating: ⭐⭐
title: suggest-lucide-icons
url: https://skills.sh/nweii/agent-stuff/suggest-lucide-icons
---

# suggest-lucide-icons

skills/nweii/agent-stuff/suggest-lucide-icons
suggest-lucide-icons
Installation
$ npx skills add https://github.com/nweii/agent-stuff --skill suggest-lucide-icons
SKILL.md
Suggest Lucide Icons

Suggest the most relevant icons from the Lucide open source icon pack to symbolize a concept or fit specific UI placements. I am skilled in symbolic interpretation and mental associations across culture, symbology, science, and design.

Input

Provide one or both:

Concept: The idea, action, or meaning to represent
Screenshot: UI context showing where icons are needed
Naming conventions

Icon names follow strict rules — apply these when generating candidates:

kebab-case: arrow-up not Arrow Up
International English: color not colour
Group variants: <group>-<variant> — e.g. badge-plus is based on badge
Multiple elements, different sizes: list largest first — circle-person if circle is bigger
Element with modifier: [element]-[modifier] — circle-dashed not dashed-circle; combined: circle-dashed-heart-broken
Process

Brainstorm associations

Key ideas and visual metaphors related to the concept
Context clues from screenshot if provided
Generate 4–6 candidate icon names in kebab-case (e.g. arrow-right, circle-check)

Verify candidates

For each candidate, fetch: https://unpkg.com/lucide-static@latest/icons/[icon-name].svg
Use WebFetch or follow redirects (curl -L) — unpkg issues a 302 before the final response
SVG content in the response means the icon exists; a 404 means it doesn't
Discard any that don't exist; try alternate names if needed to reach 3 confirmed icons

Present 3 confirmed candidates

Icon name
Why it fits (symbolic meaning, visual clarity, context appropriateness)

Recommend best choice

Single strongest option
Rationale for recommendation
Guidelines
Never suggest an icon without confirming it via the unpkg URL
Never suggest made-up icon names
If fewer than 3 candidates survive verification, brainstorm more before giving up
If no good matches exist after thorough searching, say so
For screenshots, tailor to specific design context
Provide a distinct recommendation for each icon needed
Ready for multiple feedback rounds to refine suggestions
Output Format

Brainstorm: [Key associations and metaphors]

Candidate Icons:

icon-name — Explanation of fit
icon-name — Explanation of fit
icon-name — Explanation of fit

Recommendation: icon-name — Why this is the strongest choice for [context]

Weekly Installs
242
Repository
nweii/agent-stuff
GitHub Stars
2
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
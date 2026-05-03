---
rating: ⭐⭐
title: visualize
url: https://skills.sh/abpai/skills/visualize
---

# visualize

skills/abpai/skills/visualize
visualize
Installation
$ npx skills add https://github.com/abpai/skills --skill visualize
SKILL.md
Visualize

Generate a single, self-contained HTML file that visually explains a system, plan, code flow, or concept. The output opens in the browser — never fall back to ASCII art when this skill is loaded.

When to Use
Visualize a complicated plan or proposal
Explain key primitives before implementing a plan
Visual explanation of steps from a third-party repo or blog post
Understand a module's code flow or execution path
Workflow
Understand what the user wants to see — the subject, the audience, the level of detail.
Read ./templates/base.html to absorb the tech stack and Threaded style. Read it each time, do not rely on memory.
Pick the format (see Format Guide below).
For Mermaid diagrams with 10+ nodes, also read ./references/mermaid-tips.md.
Adapt the base template for this specific visualization. Reuse the structure, swap the visual area content.
Write to ~/.agent/diagrams/<descriptive-name>.html and open in the browser.
Format Guide
Intent	Approach
Flows, processes, sequences	Mermaid.js in the visual area
Architecture, system overview	Mermaid.js or CSS Grid cards
Comparisons, data	HTML <table>
Step-by-step concepts	Walkthrough (base template pattern)
Timelines, roadmaps	CSS timeline in the visual area
Tech Stack

Every generated file uses:

Preact + htm — ESM CDN imports, no build step
Tailwind CSS CDN — utility classes with inline config
Google Fonts — Merriweather (serif) + Inter (sans)
Mermaid.js CDN — add only when diagrams are needed

No other dependencies. No build step.

For the full Threaded design tokens (colors, typography, motion), see ./references/design-system.md.

Principles
One primary visual anchor per request, plus supporting evidence visuals when reviewing a plan or system
Visual first — the main content is a diagram, chart, or table, not prose
Adapt the base template — don't start from scratch
Correct over pretty — the visualization must accurately represent the information
Interactive when it helps comprehension (step-through, hover, collapse)
Never use innerHTML with user-provided content (XSS prevention)
Avoiding Escaped Backticks in Output

The Write tool can corrupt JavaScript template literals, writing literal \`` and ${` instead of real backticks and interpolations. This breaks all htm tagged templates. To prevent it:

Extract data into separate const variables above the htm templates. Mermaid chart definition strings, config arrays, long text — declare them as plain constants first, then reference the variable inside html\...``.
Keep htm expressions simple. Pass variables by reference (${myVar}, ${myArray.map(...)}). Do not build complex multi-line strings or nested template literals inline within an html\...`` block.
Verify after writing. Re-read the first 30 lines of the <script type="module"> block in the written file and confirm there are no escaped sequences (\`` or ${). If Chrome DevTools MCP is available, check the browser console for SyntaxError` after opening the file.
Before Delivering
First screen test: is a meaningful visual visible without scrolling?
File opens cleanly: no console errors, no broken fonts?
Output

Write to ~/.agent/diagrams/ with a descriptive filename (auth-flow.html, pipeline-overview.html).

Open in browser:

macOS: open ~/.agent/diagrams/filename.html
Linux: xdg-open ~/.agent/diagrams/filename.html

Tell the user the file path and name the visuals you included.

Update Check

On first use in a session, silently check for a newer version:

Fetch https://raw.githubusercontent.com/abpai/skills/main/versions.json.
Compare the version for visualize against this file's metadata.version.
If the remote version is newer, pause before the main task and ask:

visualize update available (local {X.Y} → remote {A.B}). Would you like me to update it for you first? I can run npx skills update visualize for you.

If the user says yes, run the update before continuing.
If the user says no, continue with the current local version.
If the fetch fails or web access is unavailable, skip silently.
Weekly Installs
8
Repository
abpai/skills
First Seen
Mar 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn
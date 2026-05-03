---
rating: ⭐⭐⭐
title: vibe-deck
url: https://skills.sh/aiden0z/skills/vibe-deck
---

# vibe-deck

skills/aiden0z/skills/vibe-deck
vibe-deck
Installation
$ npx skills add https://github.com/aiden0z/skills --skill vibe-deck
SKILL.md
VibeDeck
Step 0: Environment Check

Before anything else, verify that Node.js and npm are available. Try these commands (use whichever works on the current platform):

node --version    # or: where.exe node (Windows)
npm --version     # or: where.exe npm (Windows)

Both exist and Node.js ≥ 20 → continue silently (do not mention the check to the user).
Missing or version too low → do NOT proceed. Instead:
Run uname -s and uname -m (or systeminfo on Windows) to detect the user's OS and architecture.
If you have web search capability, search for the latest recommended way to install Node.js on the user's platform, and provide the specific commands.
If you cannot search, show this message in the user's language:

中文: VibeDeck 需要 Node.js 20 或更高版本。请访问 https://nodejs.org 下载并安装适合你操作系统的版本，安装完成后重新运行。

English: VibeDeck requires Node.js 20 or later. Please visit https://nodejs.org to download and install the version for your OS, then try again.

Stop here and wait for the user to install before continuing.
Step 1: Check Project

Check if slide-kit.config.js exists in the current directory.

Exists → this is an existing slide-kit project. Go to Building Slides.
Does not exist → no project yet. Go to Creating a New Deck, then continue to Building Slides if the user also described content.
Creating a New Deck
1. Ask for title

Only ask for the project title (required). Show defaults for everything else:

I'll set up the project with these defaults unless you want changes:

Directory: ./<title-slug>/
Theme: corporate-blue (also available: minimal)
Logo: built-in SlideKit logo
Presenter: none (can set later in config)
Password: none

Let me know if you want to change any of these, or I'll proceed.

See theme-presets.md for theme details.

2. Scaffold the project
cp -r <this-skill-dir>/template/ <target-dir>
cd <target-dir>
git init


No network required — the template is bundled in this skill.

3. Configure
slide-kit.config.js: set title, theme, logo, presenter as needed
Custom primary color: use overrides.colors.primary — variants auto-derived
Custom logo: copy to public/, reference as /filename.svg
index.html: set <title>
src/App.jsx: remove PasswordGate if no password
4. Generate agent instructions

Read instruction-template.md, replace placeholders, write to both CLAUDE.md and AGENTS.md.

5. Install and start
npm install
npm run dev


Report: project location, theme, dev server URL.

Building Slides
1. Read context (do this BEFORE planning)

Read these three files first — skipping this step leads to duplicated content, wrong theme colors, or missed conventions:

CLAUDE.md (or AGENTS.md) — theme, conventions, data sources
src/App.jsx — current slide list and ordering (what already exists)
slide-kit.config.js — active theme and presenter info
2. Understand the request
What content should this slide show?
Is there data involved? Where does it come from?
Narrative continuity: new slide should follow logically from the previous one
No duplication: if a data point is already shown elsewhere, present from a different angle
Unit consistency: confirm the same units as existing slides ($K vs $M, etc.)
Content density: Check content-rules.md for minimum content density standards — slides with sparse content (< 10 visual elements, single-line card descriptions) are not acceptable.
3. Layout Decision Engine

Don't guess the layout — derive it systematically. Read layout-engine.md and follow this sequence:

Intent Classification — what type of slide is this? (data / concept / showcase / reference / tool / narrative). Different types have different density tolerances — a showcase slide can be dense on purpose, a data slide cannot.
Content Inventory — count metrics, charts, text blocks, table rows, list items
Single Takeaway Check — state the slide's ONE takeaway. For concept slides, "understand X" can naturally combine definition + components + comparison — that's one takeaway, not three.
Semantic Match — use the content-to-layout mapping table to pick the layout
Capacity Check — verify content fits within the layout's limits (which vary by intent type). If not: adapt or split — but don't split showcase/reference slides just for being dense.
Composite Layout — if content is mixed (e.g., chart + metrics), use a composite pattern from layout-engine.md Phase 4

Available layouts — see layout-templates.md for code:

Layout	Best for
FullChart	Single large chart + KeyMessage
SplitView	Side-by-side comparison
MetricGrid	Dashboard with N metric cards
ComparisonView	Before/after, similar-depth comparison
DataTable	Tool comparison, feature matrix, pricing
TimelineFlow	Roadmap, milestones, phased plans
CardGrid	4–6 feature items with icon + text
CardRow	2–4 items in a single row
ConceptSlide	Explanation / text-heavy, no data
Composite	Mixed content — see layout-engine.md Phase 4

Built-in slide templates (import from src/slides/):

Template	Use case
SlideCover	Cover page (reads config.title automatically)
SlideDivider	Chapter divider/transition
SlideAgenda	Table of contents
SlideThankYou	Closing/Q&A page
4. Build the slide
Layout: MUST use SlideLayout for all content slides — it enforces Title → KeyMessage → Content order. See layout-templates.md
Charts: chart-components.md
Style: style-guide.md
Content: content-rules.md
Colors: import { colors } from '../theme'
5. Register (checklist)
import SlideXxx from './slides/SlideXxx'

// In <Deck>:
<Slide title="Page Title"><SlideXxx /></Slide>


Before moving on, verify:

 import added at top of App.jsx
 <Slide title="..."> — title is set (powers navigator, do NOT omit)
 Placed in correct position within <Deck> (narrative order)
 footnote prop set if slide uses external data
6. Storyline review (AFTER adding slides)

Every time new slides are added, re-read the full <Deck> in App.jsx and verify the overall narrative:

 Logical flow: Does each slide follow naturally from the previous one? Would the audience be confused by the transition?
 Progressive disclosure: Concepts introduced before they're referenced? (e.g., "What is a Skill?" must come before "Recommended Skills")
 Audience-appropriate order: For non-technical audiences, order from simple → complex, familiar → new (e.g., VS Code/Copilot before CLI tools)
 No orphan slides: Every slide belongs to a clear section. If a slide doesn't fit any section, it may not belong in this deck
 Section balance: Each section should have 2-5 slides. A section with 1 slide feels incomplete; a section with 8+ slides needs splitting
 Title scan test: Read ONLY the slide titles in order — does the story make sense from titles alone? If not, rename titles to be more descriptive
7. Layout verification (AFTER building)

After building each slide, visually verify the layout or use the layout checklist:

 No bottom whitespace: Content fills ≥ 80% of slide height
 No bunched content: Use justify-center or justify-between, not justify-start
 Consistent card heights: Grid cards use h-full to fill their cell
 Card internal alignment: Title at top (shrink-0), body in flex-1 justify-center — see content-rules.md > Card Layout Alignment for the pattern and common mistakes
 One card per grid cell: No label + card wrappers; mockups go directly in cells
 Balanced columns: Unequal content? Split into 3 cols, stack vertically, or center-fill
 Text hierarchy: 28px title → 10px section label → 14px card title → 12px body → 10px aux
 Section spacing: mt-2 or mt-3 between sections, not mt-auto
 Card gap ratio: Gap between cards ≈ 1.6× card internal padding (e.g., py-2.5 → gap-4). See content-rules.md > Card Spacing
 No emoji: Use lucide-react icons, not emoji characters. Store as component refs in data arrays (icon: Mail), render as <item.icon size={14} />
8. Data extraction (if needed)
Use scripts/extract-xlsx.js to inspect Excel structure
Write a custom extraction script, verify totals match
Save to src/data/<name>.js
NEVER fabricate data
Modifying Existing Slides

When the user asks to change, reorder, or remove slides in an existing deck:

1. Read context first

Same as Building Slides — read CLAUDE.md, App.jsx, and slide-kit.config.js before touching anything.

2. Editing a slide
Open the slide component file (e.g., src/slides/SlideRevenue.jsx)
Make the requested changes while preserving the existing layout pattern
If the change involves data, update src/data/ files and verify totals still match
After editing, run the Layout verification checklist (Step 7 from Building Slides)
3. Reordering slides
Reorder the <Slide> entries in App.jsx — this is the only file that controls order
After reordering, run the post-edit verification below
4. Removing slides
Remove the <Slide> entry from App.jsx
Check if any other slide references data or concepts introduced by the removed slide — if so, move that context to an earlier slide
Remove the slide component file if no longer imported
Run the post-edit verification below
5. Replacing a slide's layout

If the user wants to change a slide from one layout to another (e.g., FullChart → SplitView):

Read layout-templates.md for the new layout's code template
Rewrite the component using the new layout, preserving the data and keyMessage
Verify the chart/content fits the new layout proportions
6. Post-edit verification (MANDATORY after ANY modification)

After every edit, reorder, or removal, do ALL of the following before reporting completion:

Import cleanup — scan App.jsx line by line:

 Every import at the top of App.jsx is actually used in the JSX below. Remove any that aren't (including leftover config, component, or data imports from removed slides)
 No slide component file imports modules that no longer exist

Storyline review — re-read the full <Deck> in App.jsx and verify:

 Logical flow: Does each slide follow naturally from the previous one?
 Progressive disclosure: Concepts introduced before they're referenced?
 No orphan slides: Every slide belongs to a clear section
 Title scan test: Read ONLY the slide titles in order — does the story make sense from titles alone?

Report the final slide order with titles to the user so they can confirm.

Sharing as Single HTML

When the user wants to share the deck as a single portable HTML file (for email, IM, or offline viewing):

npm run build:single


This produces dist-single/index.html — a self-contained file with all JS, CSS, and SVG inlined. No server needed; just open in any browser.

How it works: vite.single.config.js uses vite-plugin-singlefile to inline all assets. The logo SVG is imported as a module (not a /public reference) so it gets bundled too.

When to suggest this: If the user says "share", "send to someone", "email the deck", "make it portable", "single file", "offline", or "不需要服务器".

Limitations:

File size is ~380KB (ECharts + React bundle) — fine for sharing via email/IM, not ideal for web hosting
Custom logos in public/ (e.g., config.logo = '/my-logo.png') are automatically inlined as data URIs by the build plugin — no extra steps needed
Important Rules
NEVER fabricate data — all numbers must come from source files
When creating a project, generate BOTH CLAUDE.md and AGENTS.md
slide-kit.config.js is the single source of truth for runtime config
Slide components: src/slides/Slide<PascalCaseName>.jsx
Data files: src/data/<kebab-case-name>.js
Weekly Installs
32
Repository
aiden0z/skills
GitHub Stars
3
First Seen
Mar 15, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
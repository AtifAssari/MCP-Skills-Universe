---
rating: ⭐⭐⭐
title: html2pptx
url: https://skills.sh/site/html2pptx.app/html2pptx
---

# html2pptx

skills/html2pptx.app/html2pptx
html2pptx
$ npx skills add https://html2pptx.app
SKILL.md
html2pptx

Convert natural language instructions into production-ready PowerPoint files. This skill teaches you how to author slide-safe HTML/CSS, validate it, and export it to PPTX via the html2pptx.app MCP server.

MCP Server Setup

Connect the html2pptx MCP server to get direct tool access.

claude mcp add --transport http html2pptx https://html2pptx.app/mcp

Available MCP Tools
Tool	Description
html2pptx_create_export_job	Create an HTML-to-PPTX export job. Set waitForCompletion: true to get the completed payload in one call. MCP default is "both" (blob resource + download URL). Do not override unless you have a specific reason.
html2pptx_get_export_job	Check export job status by jobId.
html2pptx_wait_for_export_job	Poll until job completes or fails.
html2pptx_list_export_plans	Fetch the public plan catalog and recommended tier.
html2pptx_get_usage	Check current weekly usage, remaining quota, and plan limits.
html2pptx_get_docs	Fetch html2pptx.app documentation by section (overview, quickstart, api-reference, html-contract, skills, mcp, or all) and language (en/ja).
html2pptx_list_templates	List available templates with metadata. Optional category filter.
html2pptx_get_template_html	Fetch the source HTML of a template by ID. Use to study designs and create improved versions.
Available Resources

Read these via resources/read with the URI:

URI	Content
docs://html2pptx/overview	Service overview, architecture, CSS support, comparison
docs://html2pptx/quickstart	First export in 4 steps
docs://html2pptx/api-reference	REST endpoints, auth, rate limiting, errors
docs://html2pptx/html-contract	HTML structure rules and supported CSS
docs://html2pptx/skills	Skills integration guide
docs://html2pptx/mcp	MCP integration guide
Available Prompts
Prompt	Description
create_presentation	Generate a complete PowerPoint from a topic. Args: topic (required), slide_count, language
convert_html_to_pptx	Convert provided HTML/CSS to PPTX. Args: html (required), css, file_name
Workflow

This workflow uses a three-phase approach to produce high-quality slide designs. Separating content planning, creative HTML authoring, and PPTX adaptation prevents technical constraints from flattening the design into something generic.

Phase 1: Content Planning (no HTML yet)
Step 1: Derive the design direction from the user's intent

Think deeply about what the user is trying to communicate and who the audience is. Use your reasoning to craft a unique design direction — do not pick from a fixed menu. Consider:

Topic & audience — a startup pitch deck looks different from a research presentation or an internal strategy doc
Mood & tone — the user's words, topic, and context suggest an emotional direction (bold, calm, playful, authoritative, futuristic, warm, etc.)
Cultural context — Japanese corporate vs. tech startup vs. creative agency vs. academic — each has different design expectations
Content density — data-heavy presentations need structured grids; narrative presentations need breathing room
Language — if the user's request is in Japanese or targets a Japanese audience, apply the Japanese slide design rules from references/japanese-slide-design.md (conclusion-first structure, 体言止め titles, 105-char/slide limit, line-height 1.6+, Noto Sans JP, 3-color palette, 4.5:1 contrast for all text)

From these considerations, invent a specific design concept — not just "dark theme" or "professional", but something like "midnight observatory — deep navy with constellation-like dot patterns, warm amber data highlights, and generous negative space that evokes looking at the night sky."

Design inspiration palette (use as starting points to remix, combine, or depart from — NOT as a fixed list):

Dark backgrounds + neon/bright accents → tech, futuristic, bold
Off-white + serif + wide margins → editorial, refined, intellectual
Muted earth tones + rounded shapes → warm, approachable, human
Primary colors + oversized sans-serif + geometric shapes → energetic, confident, playful
Monochrome + extreme whitespace + thin type → minimal, luxury, Apple-like
Rich gradients + layered depth + glassmorphism → modern SaaS, contemporary
Retro palette + mixed serif/sans → vintage-modern, distinctive, memorable
Navy + gray + structured grid → consulting, corporate, authoritative

Anti-patterns — NEVER do these:

Do NOT default to white background + blue accent (the most generic look possible)
Do NOT center-align everything on every slide
Do NOT use the same layout on consecutive slides
Do NOT shrink font size to fit more content — split into multiple slides instead
Do NOT reuse the same design you generated in a previous conversation
Step 2: Plan the slide outline

Before writing any HTML, plan the content structure as a simple outline:

How many slides
Each slide's role and layout type (see below)
Key text and data for each slide

Vary layout across slides — use different structures:

Slide role	Layout
Title	Full-bleed background, centered oversized text, minimal elements
Content	2-column (60/40 or 70/30 split, NOT 50/50)
Data/Stats	Single visualization filling 70% of space, annotation beside it
Quote/Callout	Large centered text (36-48px), decorative accent, minimal
Grid/Bento	3-4 cards in asymmetric grid with icon + stat + label
Timeline	Horizontal or diagonal flow with connected nodes
Comparison	Side-by-side panels with contrasting background shades
Closing	Return to brand colors, single CTA, matching title slide energy

Rule: never repeat the same layout structure on 2+ consecutive slides.

Step 3: Define the visual parameters

Lock in concrete values based on your design direction. Be specific — vague intentions produce generic output:

Color palette — pick 3-5 hex codes:

1 background color
1 primary text color
1-2 accent colors
1 muted/secondary color

Typography hierarchy (presentation-scale — bigger than you think):

Slide title: 44-64px, bold/heavy
Section header: 32-40px, medium weight
Body text: 24-32px (NOT smaller — this is a presentation, not a document)
Caption/label: 16-20px, light weight, often uppercase with letter-spacing
Data callout (big number): 72-120px, bold
Maximum 2 font families per deck

Visual motifs — choose 2-3 from the archetype:

Gradients (linear, radial, multi-stop)
Geometric shapes (circles, rectangles, triangles as decoration)
Cards with shadows and rounded corners
Accent lines / dividers
Large decorative numbers
Icon + label pairs
Background texture patterns (dots, lines, subtle shapes)
Phase 2: Creative HTML Authoring (minimal constraints only)
Step 4: Author the HTML freely

Translate the outline and visual direction into HTML with three mandatory constraints:

Each slide is <section class="slide" style="width:1600px;height:900px"> (16:9 aspect ratio)

Content must not overflow the 1600x900 canvas

Every text element MUST be protected from PPTX text splitting. Without explicit sizing, the PPTX converter creates text boxes too narrow for the content, splitting words mid-character (e.g. "2026" → "202" + "6"). Use one or more of the following techniques on every text-containing element:

Available techniques (use all that apply, not just one):

white-space: nowrap — prevents line breaks entirely. Use on all single-line text (headings, labels, years, stats, names, badges)
width: Npx — sets exact text box width. Calculate: char_count × font_size × 0.7 for Latin, × 1.1 for Japanese, then add 20% padding
min-width: Npx — guarantees minimum width while allowing growth. Safer than width for variable content
flex: 0 0 Npx (flex shorthand) — prevents flex from shrinking the element below the specified size. Use on flex children
display: inline-block; width: Npx — creates a sized inline container. Use for badges, tags, stat numbers
For absolutely positioned elements: always set explicit width (absolute elements have no parent-derived width)
For grid children: use grid-column: span N with known column widths, or set min-width on the cell
For multi-line text blocks: set width or max-width to control line length, and ensure the container is wide enough for the longest line

Example — "2026" at 72px:

<!-- Apply MULTIPLE techniques together -->
<div style="min-width:280px; white-space:nowrap; font-size:72px; font-weight:700;">2026</div>


Example — flex row with stats:

<div style="display:flex; gap:40px;">
  <div style="flex:0 0 300px; text-align:center;">
    <div style="font-size:56px; font-weight:700; white-space:nowrap;">+15%</div>
    <div style="font-size:20px; white-space:nowrap;">前年比成長率</div>
  </div>
  <div style="flex:0 0 300px; text-align:center;">
    <div style="font-size:56px; font-weight:700; white-space:nowrap;">¥2.4B</div>
    <div style="font-size:20px; white-space:nowrap;">年間売上高</div>
  </div>
</div>


Beyond that, design with full creative freedom as a professional slide designer. Use any CSS you want — gradients, shadows, transforms, complex layouts. The goal is the best possible visual design.

Supported creative techniques:

Multi-layer backgrounds — stack gradients, radial glows, decorative shapes using position: absolute
Bento Grid layouts — asymmetric card grids with varying sizes using flexbox/grid
Glassmorphism — semi-transparent backgrounds with rgba(), blur not supported but soft overlays work
Bold typography — mix font sizes dramatically (72px headlines + 14px body), use letter-spacing, text-transform
Decorative elements — floating circles, diagonal dividers, accent lines, all via positioned div elements
Rich gradients — linear-gradient, radial-gradient, multi-stop gradients, gradient text backgrounds
Depth & shadow — box-shadow for card elevation, layered elements for visual depth
Data visualization — progress bars, stat cards, comparison layouts, all with div+flexbox
SVG — inline SVG for icons, charts, diagrams (rasterized to high-quality PNG)

Save the HTML file to ./html2pptx/<fileName>.html.

Phase 3: PPTX Adaptation (minimal changes)
Step 5: Read the HTML contract

Call html2pptx_get_docs with section="html-contract" to load the structural rules.

Step 6: Adapt the HTML for PPTX compatibility

Review the HTML from Phase 2 against the PPTX contract and make only the minimum changes needed. Do NOT redesign or simplify the layout — preserve the creative intent.

Typical adaptations:

Remove <script>, <iframe>, <canvas>, <video>, CSS animations, @keyframes
Replace unsupported CSS (mix-blend-mode, mask, clip-path chains, background-clip: text) with visually similar alternatives
Ensure flexbox children have explicit flex:1 or width to prevent text wrapping (see "Preventing unwanted text wrapping" below)
Replace <table> with div+flexbox if it uses gradient backgrounds or rich cell content
Put text directly in background-colored elements (not in nested <span>) for proper alignment
Convert relative image paths to base64 data URIs or absolute URLs
Use fixed px values instead of %, vw, vh, em, rem for layout dimensions

The principle: change as little as possible. If something works in both browser and PPTX, leave it alone.

Step 6b: Converting an existing HTML file

When the user provides an existing HTML file (not writing new HTML from scratch), follow this process:

Read the file to understand the structure.

Keep <style> tags in the HTML — do NOT extract or inline CSS. The API server automatically extracts <style> tag contents and applies them as CSS. This preserves element selectors (table, th, td), pseudo-selectors (th:first-child), and compound selectors (.table-total td) that would be lost by manual inlining.

Extract slides — find all <div class="slide"> blocks and change them to <section class="slide">. Keep the inner HTML exactly as-is, including all class attributes.

Remove non-slide elements — strip <script>, <head>, <body>, export status UI, and anything outside the slide divs. Keep <style> tags — prepend them before the first <section>.

Handle images — if <img> tags use relative paths (images/foo.png):

Locate the image files relative to the HTML file's directory
Compress to JPEG (max 800px width, quality 70) to stay within payload limits
Convert to base64 data URIs: data:image/jpeg;base64,...
Replace the src attribute with the data URI

Send the HTML as-is to html2pptx_create_export_job:

html2pptx_create_export_job({
  html: "<style>.slide { ... } .headline { ... } th { ... }</style><section class='slide'>...</section>",
  fileName: "output.pptx",
  waitForCompletion: true
})


The css parameter is optional — you can also pass CSS there, but including <style> tags in the HTML works just as well since the server extracts them automatically.

Why this matters: The server-side sanitizer (export-input-sanitizer.mjs) extracts <style> tag contents before DOMPurify removes them, then merges the extracted CSS with any css parameter value. This means the full CSS cascade is preserved without any client-side preprocessing.

Step 7: Export to PPTX

Call html2pptx_create_export_job with waitForCompletion: true. Do NOT specify responseFormat — the MCP server defaults to "both".

Step 8: Download and open

After the job completes, always download the file locally:

mkdir -p ./html2pptx
curl -s -L -o ./html2pptx/<fileName>.pptx "<downloadUrl>"


Extract the download URL from the Download: text block in the response. Then open the file with open ./html2pptx/<fileName>.pptx so the user can verify immediately.

Do NOT ask the user to manually download — always automate the full flow.

Output directory structure

All generated files MUST be saved under ./html2pptx/:

./html2pptx/
  Growth_Engine_2026.html
  Growth_Engine_2026.pptx

HTML Technical Notes
Slide structure
<section class="slide" style="width:1600px;height:900px;margin:0;padding:0;box-sizing:border-box;overflow:hidden;position:relative;background:...;">
  <div style="position:absolute;top:0;left:0;width:100%;height:100%;padding:60px 80px;box-sizing:border-box;">
    <!-- content here -->
  </div>
</section>

Background goes on .slide itself (fills full canvas)
Content padding goes on an inner div
Use position:relative on .slide for absolute-positioned decorative elements
Use fixed px values, not %, vw, vh, em, rem
Fully supported CSS

Flexbox, Grid, linear-gradient, radial-gradient, box-shadow, text-shadow, border-radius, transform (rotate, scale, translate, skew), opacity, overflow: hidden

Tables — use div+flexbox for styled layouts

Native <table> works for plain data, but for styled layouts (gradient headers, rich cell content), use div+flexbox instead. This gives full visual control without PPTX table limitations.

Text in shaped elements (buttons, badges, stat cards)

Put text directly in the background element with display:flex;justify-content:center;align-items:center;text-align:center and explicit width/height. This keeps text and shape aligned in PPTX output.

CRITICAL: Preventing text wrapping and splitting in PPTX

The PPTX converter creates text boxes with widths calculated from the HTML layout. If a text box is too narrow, text wraps or splits mid-word (e.g. "2022" becomes "202" + "2"). This is the most common PPTX conversion issue and MUST be prevented at authoring time.

This applies to ALL layouts — flexbox, grid, absolute positioning, and inline elements.

Apply all applicable techniques from this list to every text-containing element:

Technique	CSS	When to use
No-wrap	white-space: nowrap	All single-line text: headings, labels, years, stats, names, badges, short phrases
Explicit width	width: Npx	When the exact width is known. Calculate: char_count × font_size × 0.7 (Latin) or × 1.1 (Japanese) + 20%
Minimum width	min-width: Npx	When content may vary but needs a guaranteed minimum. Safer than width for dynamic content
Flex fixed basis	flex: 0 0 Npx	Flex children that must not shrink. Replaces flex: 1 which has no minimum guarantee
Inline block	display: inline-block; width: Npx	Badges, tags, stat numbers, year labels — sized inline containers
Absolute + width	position: absolute; width: Npx	All absolutely positioned text elements (they have NO parent-derived width)
Grid span	grid-column: span N + min-width	Grid children — explicit span plus minimum width as safety net
Max-width for multi-line	width: Npx or max-width: Npx	Multi-line text blocks — controls line length and prevents overly narrow reflow

Always combine multiple techniques. For example, a year number should get BOTH white-space: nowrap AND min-width:

<!-- WRONG — only one technique, still may break -->
<div style="font-size:72px;">2026</div>

<!-- RIGHT — multiple techniques combined -->
<div style="font-size:72px; white-space:nowrap; min-width:280px; display:inline-block;">2026</div>


Width calculation reference:

Text	Font size	Minimum width needed
"2026" (4 Latin chars)	48px	4 × 48 × 0.7 × 1.2 = 162px → use 200px
"2026" (4 Latin chars)	72px	4 × 72 × 0.7 × 1.2 = 242px → use 280px
"+15%" (4 Latin chars)	56px	4 × 56 × 0.7 × 1.2 = 188px → use 220px
"エンタープライズ" (8 JP chars)	32px	8 × 32 × 1.1 × 1.2 = 338px → use 360px
"売上推移" (4 JP chars)	44px	4 × 44 × 1.1 × 1.2 = 232px → use 260px

Checklist before export — verify EVERY text element has at least 2 protections:

 white-space: nowrap on all single-line text
 Explicit width, min-width, or flex: 0 0 Npx on all text containers
 Absolutely positioned text has explicit width
 No text container relies solely on flex: 1 without min-width
 Large text (40px+) containers are calculated with the width formula above
Not supported

<script>, <iframe>, <canvas>, <video>, CSS animations, @keyframes, hover states, external fonts without autoEmbedFonts

Operating Rules
Use waitForCompletion: true for simplest flow.
Do NOT specify responseFormat — the MCP default ("both") is optimal.
After export, ALWAYS download locally via curl and open the file. Never just show the URL.
Check quota with html2pptx_get_usage before batch exports.
Keep fileBase64 out of conversational output.
CLI Export (Alternative to MCP)

When MCP is not available or the user prefers CLI, use html2pptx-cli instead.

Setup
npm install -g html2pptx-cli
html2pptx login

Convert HTML to PPTX
# Direct mode (for scripts, CI/CD, AI agents)
html2pptx convert ./html2pptx/slides.html -o ./html2pptx/slides.pptx -s 16:9

# With external CSS
html2pptx convert ./html2pptx/slides.html --css ./html2pptx/styles.css -o ./html2pptx/slides.pptx

# JSON output for scripting
html2pptx convert ./html2pptx/slides.html --json

# Convert and auto-open
html2pptx convert ./html2pptx/slides.html --open

Interactive mode

Run without arguments for a guided experience:

html2pptx convert

Other Commands
Command	Description
html2pptx login	Configure API key (shows dashboard link)
html2pptx logout	Remove stored API key
html2pptx status	Check usage, quota, rate limits, plan details
html2pptx whoami	Verify API key and show auth status
html2pptx config	Show current configuration
CLI Workflow Integration

When using CLI instead of MCP, the workflow changes slightly:

Phase 1 & 2: Same as MCP — plan content, author HTML, save to ./html2pptx/<fileName>.html
Phase 3: Same PPTX adaptation rules apply
Export: Use CLI instead of MCP tool:
html2pptx convert ./html2pptx/<fileName>.html -o ./html2pptx/<fileName>.pptx --open

The --open flag automatically opens the PPTX for the user to verify
When to use CLI vs MCP
Scenario	Use
Agent conversation in Claude Desktop / VS Code	MCP
Claude Code terminal session	CLI or MCP
CI/CD pipeline	CLI
Scripting / automation	CLI with --json
MCP server not connected	CLI
Failure Handling

When an MCP tool rejects a request:

Distinguish auth failure from plan failure from payload failure
Surface the exact limit that was hit
Suggest the smallest next step: connect MCP server, reduce slide count, reduce payload size
Weekly Installs
60
Source
html2pptx.app
First Seen
3 days ago
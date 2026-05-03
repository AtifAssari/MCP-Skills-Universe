---
title: design-system
url: https://skills.sh/jezweb/claude-skills/design-system
---

# design-system

skills/jezweb/claude-skills/design-system
design-system
Installation
$ npx skills add https://github.com/jezweb/claude-skills --skill design-system
SKILL.md
Design System Extractor

Analyse an existing website, HTML file, or screenshot and synthesise a semantic design system into a DESIGN.md file. The output is optimised for use with the design-loop skill and general page generation.

When to Use
Starting a new project based on an existing site's visual language
Documenting a site's design system that was never formally written down
Preparing .design/DESIGN.md before running the design loop
Extracting brand guidelines from a client's existing website
Creating consistency documentation for a multi-page project
Extracting design tokens from a Google Stitch project
Workflow
Step 1: Identify the Source

Ask the user for one of:

Source	Method
Live URL	Browse via Playwright CLI or scraper, screenshot + extract HTML
Local HTML file	Read the file directly
Screenshot image	Analyse visually (limited — no exact hex extraction)
Existing project	Scan site/public/ for HTML files to analyse
Stitch project	Use @google/stitch-sdk to fetch screen HTML + design theme
Step 2: Extract Raw Design Data
From a Live URL

Browse the site using Playwright CLI:

playwright-cli -s=design open {url}
playwright-cli -s=design screenshot --filename=.design/screenshots/source-desktop.png


Extract the full HTML — either via scraper MCP or by reading the page source

Resize and screenshot mobile (375px):

playwright-cli -s=design resize 375 812
playwright-cli -s=design screenshot --filename=.design/screenshots/source-mobile.png


Close the session: playwright-cli -s=design close

From a Local HTML File

Read the file directly and extract design tokens from the source.

From a Screenshot Only

Analyse the image visually. Note: colour extraction will be approximate without HTML source. Flag this limitation in the output.

From a Google Stitch Project

If @google/stitch-sdk is installed and STITCH_API_KEY is set:

import { stitch } from "@google/stitch-sdk";

// List projects to find the target
const projects = await stitch.projects();

// Get project details (includes designTheme)
const project = stitch.project(projectId);
const screens = await project.screens();

// Get HTML from the main screen
const screen = screens[0]; // or find by title
const htmlUrl = await screen.getHtml();
const imageUrl = await screen.getImage();


The Stitch designTheme object provides structured tokens directly:

{
  "colorMode": "DARK",
  "font": "INTER",
  "roundness": "ROUND_EIGHT",
  "customColor": "#40baf7",
  "saturation": 3
}


Map these to DESIGN.md sections:

colorMode → Theme (Light/Dark)
font → Typography font family
roundness → Component border-radius (ROUND_EIGHT = 8px, ROUND_SIXTEEN = 16px, etc.)
customColor → Primary brand colour
saturation → Colour vibrancy (1-5 scale)

Then also download and analyse the HTML for the full palette (Stitch's theme object only has the primary colour — the full palette is in the generated CSS).

Step 3: Analyse Design Tokens

Extract these from the HTML/CSS source:

Colours

Look in these locations (priority order):

CSS custom properties — :root { --primary: #hex; } or @theme blocks
Tailwind config — <script> block with tailwind.config or @theme in <style>
Inline styles — style="color: #hex" or style="background: #hex"
Tailwind classes — bg-blue-600, text-gray-900 (map to palette)
Computed from screenshot — last resort, approximate

For each colour found, determine its role:

Role	How to identify
Primary	Buttons, links, active states, brand elements
Background	<body> or <html> background
Surface	Cards, containers, elevated elements
Text Primary	<h1>, <h2>, main body text
Text Secondary	Captions, metadata, muted text
Border	Dividers, input borders, card borders
Accent	Badges, notifications, highlights
Typography

Extract:

Token	Where to find
Font families	Google Fonts <link>, @import, font-family in CSS
Heading weights	font-bold, font-semibold, or explicit font-weight
Body size	Base font-size on <body> or root
Line height	leading-* classes or line-height CSS
Letter spacing	tracking-* classes or letter-spacing CSS
Components

Identify patterns for:

Buttons — shape (rounded-full, rounded-lg), colours, padding, hover states
Cards — background, border, shadow, border-radius, padding
Navigation — sticky/static, background treatment, active indicator
Forms — input style, focus ring, label positioning
Hero sections — layout pattern, overlay treatment, CTA placement
Spacing & Layout
Max content width — look for max-w-* or explicit max-width
Section padding — typical vertical padding between sections
Grid system — column count, gap values
Whitespace philosophy — tight, balanced, generous, or dramatic
Step 4: Synthesise into Natural Language

Critical: The DESIGN.md should describe the design in semantic, natural language supported by exact values. This is not a CSS dump — it's a document a designer or AI can read to understand and reproduce the visual language.

Don't write	Write instead
rounded-xl	"Softly rounded corners (12px)"
shadow-md	"Subtle elevation with diffused shadow"
#1E40AF	"Deep Ocean Blue (#1E40AF) for primary actions"
py-16	"Generous section spacing with breathing room"
Step 5: Write DESIGN.md

Output the file to .design/DESIGN.md (or user-specified path).

Follow the structure from the design-loop skill's references/site-template.md — specifically the DESIGN.md Template section. The key sections are:

Visual Theme & Atmosphere — mood, vibe, philosophy
Colour Palette & Roles — table with role, name, hex, usage
Typography — font families, weights, sizes, line heights
Component Styles — buttons, cards, nav, forms
Layout Principles — max width, spacing, grid, whitespace
Design System Notes for Generation — the copy-paste block for baton prompts
Step 6: Verify Accuracy

If browser automation is available:

Generate a small test section (e.g. a card + button + heading) using the extracted design system
Screenshot it alongside the original
Compare visually — adjust any values that don't match
Step 7: Report to User

Present:

Summary of extracted tokens (colour count, fonts, component patterns)
The generated DESIGN.md location
Any tokens that were approximate (flagged with ⚠️)
Suggestions for manual review (colours from screenshots, ambiguous typography)
Handling Multiple Pages

If the site has multiple pages with different styles:

Analyse the homepage first — it usually has the most complete design language
Spot-check 2-3 inner pages for consistency
Note any page-specific overrides in the Component Styles section
If pages are wildly different, ask the user which page to use as the canonical source
Tips
Tailwind sites are easiest — the config block has everything
Google Fonts links are gold — they specify exact families and weights
CSS custom properties are reliable — they represent intentional design tokens
Inline Tailwind classes need interpretation — bg-slate-900 needs mapping to a role
Screenshots are last resort — accurate hex extraction from images is unreliable
Dark mode: Check for .dark class overrides or prefers-color-scheme media queries
Common Pitfalls
❌ Listing raw CSS values without semantic description
❌ Missing the dark mode palette (check for .dark class or media query)
❌ Ignoring component patterns (just listing colours isn't enough)
❌ Not including Section 6 (the copy-paste generation block)
❌ Approximate colours from screenshots without flagging the uncertainty
Weekly Installs
368
Repository
jezweb/claude-skills
GitHub Stars
759
First Seen
Mar 28, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn
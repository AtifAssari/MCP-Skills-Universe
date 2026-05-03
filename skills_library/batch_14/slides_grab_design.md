---
title: slides-grab-design
url: https://skills.sh/vkehfdl1/slides-grab/slides-grab-design
---

# slides-grab-design

skills/vkehfdl1/slides-grab/slides-grab-design
slides-grab-design
Installation
$ npx skills add https://github.com/vkehfdl1/slides-grab --skill slides-grab-design
SKILL.md
slides-grab Design Skill (Codex)

Use this after slide-outline.md is approved.

Goal

Generate high-quality slide-XX.html files in the selected slides workspace (slides/ by default) and support revision loops.

Inputs
Approved slide-outline.md (must contain style: <id> in meta section — style was approved in Stage 1)
Requested edits per slide
Outputs
<slides-dir>/slide-01.html ... slide-XX.html
Updated <slides-dir>/viewer.html via build script
Workflow
Read approved slide-outline.md and extract the style field from its meta section.
Load the chosen style's full spec from src/design-styles-data.js — colors, fonts, layout, signature elements, and things to avoid. If the meta specifies a custom direction instead of a bundled ID, use that custom direction as the design basis.
Before generating slides, write a quick visual thesis (mood/material/energy), a content plan (opener → support/proof → detail/story → close/CTA), and the core design tokens (background, surface, text, muted, accent + display/headline/body/caption roles). Ground these tokens in the chosen style's spec.
If you need to confirm or revisit the approved bundled style before designing, re-run slides-grab list-styles and open the gallery from slides-grab preview-styles so the Stage 2 deck stays aligned with the Stage 1 direction.
Generate slide HTML files with 2-digit numbering in selected --slides-dir.
When a slide needs iconography, prefer Lucide as the default icon library. Use clean Lucide icons before falling back to emoji, and only use emoji when the brief explicitly calls for them.
When a slide explicitly needs bespoke imagery, when the user asks for an image, or when stronger imagery would materially improve the slide, prefer slides-grab image --prompt "<prompt>" --slides-dir <path> to generate a local asset with Nano Banana Pro and save it under <slides-dir>/assets/.
If the deck needs a complex diagram (architecture, workflows, relationship maps, multi-node concepts), create the diagram in tldraw, export it with slides-grab tldraw, and treat the result as a local slide asset under <slides-dir>/assets/.
If the slide needs a local video, store the video under <slides-dir>/assets/, reference it as ./assets/<file>, and prefer a poster="./assets/<file>" thumbnail so PDF export uses a stable still image.
If the source video starts on YouTube or another supported page, use slides-grab fetch-video --url <youtube-url> --slides-dir <path> (or yt-dlp directly if needed) to download it into <slides-dir>/assets/ before saving the slide HTML.
Run slides-grab validate --slides-dir <path> after generation or edits.
If validation fails, automatically fix the source slide HTML/CSS and re-run validation until it passes.
Run the slide litmus check from references/beautiful-slide-defaults.md before presenting the deck for review.
Launch the interactive editor for visual review: slides-grab edit --slides-dir <path>
Iterate on user feedback by editing only requested slide files, then re-run validation after each edit round.
When the user confirms editing is complete, suggest: build the viewer (slides-grab build-viewer --slides-dir <path>) for a final read-only preview, or proceed to export (PDF/PPTX).
Keep revising until user approves conversion stage.
Rules
Keep slide size 720pt x 405pt.
Keep semantic text tags (p, h1-h6, ul, ol, li).
Put local images and videos under <slides-dir>/assets/ and reference them as ./assets/<file>.
Allow data: URLs when the slide must be fully self-contained.
Do not leave remote http(s):// image URLs in saved slide HTML; download source images into <slides-dir>/assets/ and reference them as ./assets/<file>.
Prefer Lucide for default slide iconography. Avoid emoji as the default icon treatment unless the brief explicitly asks for emoji.
Prefer slides-grab image with Nano Banana Pro for bespoke slide imagery before reaching for remote URLs.
If GOOGLE_API_KEY (or GEMINI_API_KEY) is unavailable or the Nano Banana API fails, ask the user for a Google API key or fall back to web search + download into <slides-dir>/assets/.
Prefer local videos with a poster="./assets/<file>" thumbnail so PDF export uses the still image.
Use slides-grab fetch-video or yt-dlp to pull supported web videos into <slides-dir>/assets/ before saving slide HTML.
Prefer <img> for slide imagery and data-image-placeholder when no final asset exists.
Default to one job per slide, one dominant visual anchor, and copy that scans in seconds.
Treat opening slides and section dividers like posters, not dashboards.
Default to cardless layouts; only add a card when it improves structure or comprehension.
Use whitespace, alignment, scale, cropping, and contrast before adding decorative chrome.
Prefer tldraw for complex diagrams instead of recreating dense node/edge diagrams directly in HTML/CSS.
Use slides-grab tldraw plus templates/diagram-tldraw.html when that gives a cleaner, more export-friendly result.
Do not present slides for review until slides-grab validate --slides-dir <path> passes.
Do not start conversion before approval.
Use the packaged CLI and bundled references only; do not depend on unpublished agent-specific files.
Reference

For full constraints and style system, follow:

references/design-rules.md
references/detailed-design-rules.md
references/beautiful-slide-defaults.md — slide-specific art direction defaults adapted from OpenAI's frontend design guidance
references/design-system-full.md — archived full design system, templates, and advanced pattern guidance
Weekly Installs
10
Repository
vkehfdl1/slides-grab
GitHub Stars
641
First Seen
Mar 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail
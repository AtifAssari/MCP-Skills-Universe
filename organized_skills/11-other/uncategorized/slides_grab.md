---
rating: ⭐⭐
title: slides-grab
url: https://skills.sh/vkehfdl1/slides-grab/slides-grab
---

# slides-grab

skills/vkehfdl1/slides-grab/slides-grab
slides-grab
Installation
$ npx skills add https://github.com/vkehfdl1/slides-grab --skill slides-grab
SKILL.md
slides-grab Skill (Codex) - Full Workflow Orchestrator

Guides you through the complete presentation pipeline from topic to exported file.

Workflow
Stage 1 — Plan

Use the installed slides-grab-plan skill.

Take user's topic, audience, and tone.
Style selection (mandatory before outline): Run slides-grab list-styles, analyze the topic/tone, and shortlist 2–3 bundled styles that fit. Present the shortlist with reasons. Optionally offer slides-grab preview-styles for visual preview. If none of the 35 bundled styles fit, propose a fully custom visual direction. Get explicit style approval before writing the outline.
Create slide-outline.md with the chosen style ID in the meta section (style: <id>).
Present outline to user.
Revise until user explicitly approves.

Do not proceed to Stage 2 without approval of both style and outline.

Stage 2 — Design

Use the installed slides-grab-design skill.

Read approved slide-outline.md and apply the style specified in its meta section (style: <id>). Do not re-open style selection — the style was already approved in Stage 1.
Generate slide-*.html files in the slides workspace (default: slides/).
Run validation: slides-grab validate --slides-dir <path>
If validation fails, automatically fix the slide HTML/CSS until validation passes.
For bespoke slide imagery, use slides-grab image --prompt "<prompt>" --slides-dir <path> so Nano Banana Pro saves a local asset under <slides-dir>/assets/.
For complex diagrams (architecture, workflows, relationship maps, multi-node concepts), prefer tldraw over hand-built HTML/CSS diagrams. Render the asset with slides-grab tldraw, store it under <slides-dir>/assets/, and place it in the slide with a normal <img>.
Keep local videos under <slides-dir>/assets/, prefer poster="./assets/<file>" thumbnails, and use slides-grab fetch-video --url <youtube-url> --slides-dir <path> (or yt-dlp directly) when the source starts on a supported web page.
If GOOGLE_API_KEY (or GEMINI_API_KEY) is unavailable or Nano Banana is down, ask the user for a Google API key or fall back to web search/download into <slides-dir>/assets/.
Launch the interactive editor for review: slides-grab edit --slides-dir <path>
Revise slides based on user feedback via the editor, then re-run validation after each edit round.
When the user confirms editing is complete, suggest next steps: build the viewer (slides-grab build-viewer --slides-dir <path>) for a final preview, or proceed directly to Stage 3 for PDF/PPTX export.

Do not proceed to Stage 3 without approval.

Stage 3 — Export

Use the installed slides-grab-export skill.

Confirm user wants conversion.
Pick the primary target:
Card-news / Instagram-style decks → slides-grab png --slides-dir <path> --slide-mode card-news --resolution 2160p (see slides-grab-card-news).
Widescreen decks → slides-grab pdf --slides-dir <path> --output <name>.pdf.
Per-slide PNG (any mode): slides-grab png --slides-dir <path> --output-dir <path>/out-png --resolution 2160p.
PPTX (optional, experimental / unstable): slides-grab convert --slides-dir <path> --output <name>.pptx.
Figma-importable PPTX (optional, experimental / unstable): slides-grab figma --slides-dir <path> --output <name>-figma.pptx.
Report results.
Rules
Always follow the stage order: Plan → Design → Export.
Get explicit user approval before advancing to the next stage.
Read each stage's SKILL.md for detailed rules — this skill only orchestrates.
Use decks/<deck-name>/ as the slides workspace for multi-deck projects.
Call out export risk clearly: PPTX and Figma export are experimental / unstable and must be described as best-effort output.
Use the stage skills as the source of truth for plan, design, and export rules.
When a slide needs a complex diagram, default to a tldraw-generated asset unless the user explicitly asks for a different approach.
When a slide needs bespoke imagery, prefer Nano Banana Pro via slides-grab image and keep the saved asset local under <slides-dir>/assets/.
Reference
references/presentation-workflow-reference.md — archived end-to-end workflow guidance from the legacy skill set
Weekly Installs
12
Repository
vkehfdl1/slides-grab
GitHub Stars
641
First Seen
Mar 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
---
title: nanobanana-2-image-generation
url: https://skills.sh/doggy8088/nanobanana-cli/nanobanana-2-image-generation
---

# nanobanana-2-image-generation

skills/doggy8088/nanobanana-cli/nanobanana-2-image-generation
nanobanana-2-image-generation
Installation
$ npx skills add https://github.com/doggy8088/nanobanana-cli --skill nanobanana-2-image-generation
SKILL.md
Do this first
Use a Node.js wrapper (@google/genai) as the primary flow (multi-turn edits, grounding, advanced generationConfig).
Use scripts\nanobanana-cli.js for quick single-turn generation/editing runs.
Do not teach raw curl; keep guidance in JS CLI/wrapper form.
Enforce these defaults
API key source: NANOBANANA_GEMINI_API_KEY with fallback GEMINI_API_KEY.
Default model: gemini-3.1-flash-image-preview (allow env override via NANOBANANA_MODEL).
Reference images: support up to 14 total.
Thinking strength: configurable (minimal|low|medium|high), default High.
Aspect ratio: default Auto.
Resolution: default 1K.
Output mode: default Images only.
Google Search grounding tool: default Disabled; enable with --google-search when needed.
Output directory: default nanobanana-output/, unless the prompt explicitly asks for another location.
512px rule: send imageConfig.imageSize as string "512" in API calls (never numeric 512).
Read references intentionally
Start in references\image-generation-api.md for operational payload rules, model behavior, sizing, thinking, grounding, and limits.
Use references\sources.md to verify source provenance and jump to upstream docs.
For canonical API behavior, read:
Gemini image-generation docs
Aspect ratios and image size
Thinking process
Grounding with Google Search
Grounding with Google Image Search
Execution pattern
Default to Node.js wrapper flows for regular usage, especially when payload control is needed.
Quick path:
node scripts\nanobanana-cli.js --prompt "..."
Add references via repeated -i/--image (up to 14).
Enable grounding via --google-search when prompt needs fresh web context.
Weekly Installs
8
Repository
doggy8088/nanobanana-cli
First Seen
Mar 11, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
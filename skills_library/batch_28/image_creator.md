---
title: image-creator
url: https://skills.sh/tendtoyj/tendtoyj-claude-skills/image-creator
---

# image-creator

skills/tendtoyj/tendtoyj-claude-skills/image-creator
image-creator
Installation
$ npx skills add https://github.com/tendtoyj/tendtoyj-claude-skills --skill image-creator
SKILL.md
Image Creator

Turn post copy into brand-aligned visuals. One tool (nanobanana), one output (image files). This is the final step in the creative-mkt pipeline: post-writer produces copy → image-creator produces matching visuals.

Purpose

Great copy without matching visuals gets scrolled past. Image Creator bridges that gap — it reads your post copy (or visual direction notes), loads your brand's visual identity, engineers a precise prompt, and generates images through nanobanana MCP.

The skill focuses on generation only. Prompt pattern knowledge lives in references/prompt-patterns.md — read it during Step 3 for detailed templates and examples.

Memory Auto-Load Protocol

Run this before any work:

1. Check creative-memory/ exists → if not, create from creative-memory-template/
2. Load creative-memory/visual-guidelines.md  ★ CRITICAL ★
   → Extract: Color Palette (HEX codes), Image Style, Typography feel, Do's & Don'ts
   → If empty or missing: warn user, suggest running visual-extractor first
   → Proceed anyway with generic professional style as fallback
3. Load brand-memory/voice-profile.md (read-only)
   → Map brand personality traits to visual mood (e.g., "bold & direct" → high contrast, strong lines)
4. Load brand-memory/positioning.md (read-only)
   → Note differentiation angle for visual storytelling
5. Load creative-memory/content-examples.md (read-only)
   → Check visual direction notes from past high-performing posts


Access rules:

Memory folder	Permission
research-memory/	Read-only
brand-memory/	Read-only
creative-memory/	Read & Write (creative-log.md only)
Input Gathering

Collect from the user:

Input	Required	Description
Post copy or visual direction	Yes	The text to visualize — from post-writer, series-planner, or user-provided
Target platform	Yes	Instagram feed/story/reel, LinkedIn, Twitter/X, YouTube thumbnail
Style override	No	Override visual-guidelines if a different look is needed
Include/exclude elements	No	"no people", "include text overlay", "abstract only"
Number of variations	No	Default: 2–3 images. Max: 4 per batch
Language	Optional	텍스트 오버레이 언어 (default: English). 이미지 내 텍스트에 적용

If the user provides a post-writer output file, extract:

The post copy (for message analysis)
The Visual Direction section (if present — post-writer attaches these)
The platform (from file metadata or ask)
Step 1: Message + Tone Analysis

Extract visual direction from the copy. This step turns words into visual concepts.

1a. Core message extraction Summarize the post's central idea in one sentence. This becomes the image's subject.

1b. Emotional tone mapping Map the copy onto these spectrums:

Spectrum	Left	Right
Energy	Calm, reflective	Energetic, urgent
Formality	Professional, polished	Casual, raw
Weight	Serious, weighty	Light, playful
Temperature	Warm, human	Cool, technical

The position on each spectrum informs color temperature, composition tightness, and visual complexity.

1c. Visual keyword extraction Derive 3–5 concrete visual concepts from the message + tone:

Abstract concepts → tangible metaphors (e.g., "growth" → ascending stairs, sprouting plant)
Emotional tone → visual treatment (e.g., "trust" → clean lines, blue tones, open space)
Brand context → style constraints (from visual-guidelines)

1d. Brand alignment check Cross-reference visual keywords against visual-guidelines.md:

Do the keywords align with the brand's Image Style direction?
Are there conflicts with the Don'ts list?
Adjust keywords to stay within brand boundaries while serving the copy's message.
Step 2: Platform Configuration

Select the right technical settings based on the target platform.

Platform defaults:

Platform	Aspect Ratio	Model	Rationale
Instagram feed	4:5	pro	High quality for the grid
Instagram story/reel	9:16	flash	Speed for ephemeral content
LinkedIn	1:1 or 16:9	pro	Professional, detail matters
Twitter/X	16:9	flash	Speed, timeline-optimized
YouTube thumbnail	16:9	pro	Text rendering + face clarity

Model selection logic:

Default: auto (nanobanana decides)
Force pro when: brand integrity is critical, text-in-image needed, portfolio/hero usage
Force flash when: high volume batch, stories/ephemeral content, quick iterations

Composition guidance per ratio:

1:1 — Centered subject, symmetric balance, ample breathing room
4:5 — Vertical emphasis, subject in upper 60%, space for caption overlap
9:16 — Strong vertical flow, stacked elements, text zones at top and bottom thirds
16:9 — Horizontal storytelling, rule-of-thirds subject placement, cinematic feel
Step 3: Prompt Engineering

This is the core value of the skill. Build the generation prompt using a structured formula.

Read references/prompt-patterns.md now — it contains detailed templates, style libraries, and worked examples for each use case.

Prompt formula:

[Subject/Scene] + [Style Directive] + [Color/Mood] + [Composition] + [Platform Specs] + [Negative Prompt]


Building each component:

Subject/Scene — Convert Step 1's visual keywords into a concrete scene description. Be specific: "a person" is weak; "a focused entrepreneur working at a clean desk with morning light" is strong. Use the specificity ladder in prompt-patterns.md.

Style Directive — Pull from visual-guidelines.md Image Style section:

Photography-first brands → specify camera angle, lighting type, depth of field
Illustration-first brands → specify illustration style, line weight, flatness
If no guidelines exist → default to "clean, modern, professional photography style"

Color/Mood — Embed brand colors directly as HEX values in the prompt. This is more effective than color names alone:

"color palette dominated by deep navy (#1A2B4C) with warm gold (#C9A96E) accents"
Pull Primary + Accent from visual-guidelines

Composition — Use Step 2's platform-specific composition guidance

Platform Specs — Aspect ratio from Step 2

Text Overlay Language — If the user specified a language, all text overlays in the image (headlines, captions, CTAs) must be written in that language. If no language was specified, default to English.

Negative Prompt — Always include:

Universal: blurry, low quality, watermark, distorted text, artifacts, oversaturated
Brand Don'ts from visual-guidelines (convert to negative prompt form)
Any user-specified exclusions

Variation strategy — For 2–3 variations, modify ONE element per variation:

Variation A: base prompt (primary interpretation)
Variation B: shift composition (different angle or framing)
Variation C: shift color emphasis (accent color more prominent)
Step 4: Generate Images

Call nanobanana MCP to create the images.

nanobanana capabilities:

Parameter	Spec
Models	Gemini 3 Pro (quality) / Gemini 2.5 Flash (speed)
Default model	auto
Max resolution	4K (Pro) / 1024px (Flash)
Supported ratios	1:1, 4:5, 9:16, 16:9, and more
Prompt limit	8,192 characters
Batch	Up to 4 images per request

Generation sequence:

Construct the full prompt from Step 3 components
Call generate_image with prompt + aspect ratio + model selection
Repeat with modified prompts for each variation
Review each generated image immediately:
Brand colors reflected?
Aspect ratio correct?
No unintended text or artifacts?
Mood matches the copy's tone?
If a result is off → adjust the prompt (usually the subject description or style directive) and regenerate that variation only

When generation quality is poor:

Add more specificity to the subject description
Strengthen the style directive with concrete references
Increase negative prompt coverage
Try switching between pro and flash models
See references/prompt-patterns.md → Section 7 (Refinement Tips) for systematic troubleshooting
Step 5: Save + Log

Save images:

Path: [project]/images/[platform]-[topic]-[YYYYMMDD]-v[N].png
Example: images/instagram-feed-growth-mindset-20260224-v1.png
Save the generation prompt alongside: images/prompt-log.md (append, don't overwrite)

Prompt log format:

## [YYYY-MM-DD] [Platform] — [Topic]
- Model: [pro/flash/auto]
- Aspect ratio: [ratio]
- Prompt: [full prompt text]
- Negative: [negative prompt]
- Result: [v1: kept / v2: kept / v3: discarded — reason]


This log enables prompt reuse and iterative refinement across sessions.

Update creative-log.md:

| [YYYY-MM-DD] | image-creator | [platform] [topic] × [N]images | [style notes] | nanobanana ([model]) |


Present to user: Show all generated images and ask which to keep, modify, or regenerate. If the user wants changes, return to Step 3 with adjusted prompt parameters.

Quality Checklist

Before delivering, verify:

 Brand colors from visual-guidelines appear in the generated images
 Aspect ratio matches the target platform specification
 Image style aligns with visual-guidelines direction (photo/illustration/abstract)
 The image visually communicates the post copy's core message
 No unintended text, watermarks, or visual artifacts
 2–3 variations generated (giving the user choice)
 Prompt log saved for future reference and refinement
 creative-log.md updated with execution record
What This Skill Does NOT Do
Write post copy → That's post-writer's job
Extract visual guidelines → That's visual-extractor's job
Edit or retouch existing images → Out of scope for v2
Generate video or animation → Future extension (video-scripter)
Write to brand-memory/ → Read-only access

Image Creator stays focused: copy in → brand-aligned images out.

Skill Chaining

← From post-writer: Each post includes a "Visual Direction" note — feed that directly into Step 1.

← From series-planner: Campaign plans include per-post visual direction — generate images for each post in sequence.

→ To user: Final deliverable — copy + matching visual, ready to publish.

Full pipeline: visual-extractor → framework-builder → trend-scout → post-writer → image-creator

Weekly Installs
22
Repository
tendtoyj/tendto…e-skills
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
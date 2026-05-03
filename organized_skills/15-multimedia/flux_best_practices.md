---
rating: ⭐⭐
title: flux-best-practices
url: https://skills.sh/black-forest-labs/skills/flux-best-practices
---

# flux-best-practices

skills/black-forest-labs/skills/flux-best-practices
flux-best-practices
Installation
$ npx skills add https://github.com/black-forest-labs/skills --skill flux-best-practices
SKILL.md
FLUX Best Practices

Use this skill when generating prompts for any BFL FLUX model to ensure optimal image quality and accurate prompt interpretation.

When to Use
Creating prompts for FLUX.2 or FLUX.1 models
Text-to-image (T2I) generation
Image-to-image (I2I) editing with FLUX.2 models
Structured scene generation with JSON
Typography and text rendering
Multi-reference style transfer
Color-accurate brand generations
Quick Reference
Prompt Structure Formula
[Subject] + [Action/Pose] + [Style/Medium] + [Context/Setting] + [Lighting] + [Camera/Technical]

Model Selection
Use Case	Recommended Model	Notes
Fastest generation	FLUX.2 [klein]	4B or 9B, sub-second
Highest quality	FLUX.2 [max]	Best detail, grounding search
Production balanced	FLUX.2 [pro]	Quality + speed
Typography/text	FLUX.2 [flex]	Best text rendering
Local/development	FLUX.2 [dev]	Open weights
Image editing	FLUX.2 [pro/max]	Pass image URL directly to input_image
Inpainting	FLUX.1 Fill	Object removal/completion
Context editing	FLUX.1 Kontext	Older model, prefer FLUX.2
Critical Rules
NO negative prompts - FLUX does not support negative prompts; describe what you want
Be specific - Vague prompts produce mediocre results
Use natural language - Prose/narrative style works best
Specify lighting - Lighting has the biggest impact on quality
Quote text - Use "quoted text" for typography rendering
Hex colors - Use #RRGGBB format with color description
Related

For API integration (endpoints, polling, webhooks), see the bfl-api skill.

Rules Reference

Read individual rule files for detailed guidance:

rules/core-principles.md - Universal FLUX prompting principles
rules/flux2-models.md - FLUX.2 family: klein, max, pro, flex, dev
rules/flux1-models.md - FLUX.1 family: older generation of FLUX.2 models - pro, Kontext, Fill
rules/t2i-prompting.md - Text-to-image prompting patterns
rules/i2i-prompting.md - Image-to-image editing with FLUX.2
rules/json-structured-prompting.md - Complex scene composition
rules/hex-color-prompting.md - Precise color specification
rules/typography-text.md - Text rendering and typography
rules/multi-reference-editing.md - Multi-image references
rules/negative-prompt-alternatives.md - Positive alternatives
rules/model-selection-guide.md - Choosing the right model
Example Prompt
A weathered fisherman in his 70s with deep wrinkles and a salt-and-pepper beard,
wearing a navy cable-knit sweater, standing at the helm of his wooden boat.
Golden hour sunlight from the left creates dramatic rim lighting on his profile.
Shot on Hasselblad with 85mm lens at f/2.8, shallow depth of field with harbor
lights creating soft bokeh in the background. Kodak Portra 400 color science.

Weekly Installs
449
Repository
black-forest-labs/skills
GitHub Stars
56
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
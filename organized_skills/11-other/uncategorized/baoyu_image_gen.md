---
rating: ⭐⭐⭐
title: baoyu-image-gen
url: https://skills.sh/smallnest/langgraphgo/baoyu-image-gen
---

# baoyu-image-gen

skills/smallnest/langgraphgo/baoyu-image-gen
baoyu-image-gen
Installation
$ npx skills add https://github.com/smallnest/langgraphgo --skill baoyu-image-gen
SKILL.md
Image Generation (AI SDK)

Official API-based image generation via AI SDK. Supports OpenAI (DALL-E, GPT Image) and Google (Imagen, Gemini multimodal).

Script Directory

Important: All scripts are located in the scripts/ subdirectory of this skill.

Agent Execution Instructions:

Determine this SKILL.md file's directory path as SKILL_DIR
Script path = ${SKILL_DIR}/scripts/<script-name>.ts
Replace all ${SKILL_DIR} in this document with the actual path

Script Reference:

Script	Purpose
scripts/main.ts	CLI entry point for image generation
Quick Start
# Basic generation (auto-detect provider)
npx -y bun ${SKILL_DIR}/scripts/main.ts --prompt "A cat" --image cat.png

# With aspect ratio
npx -y bun ${SKILL_DIR}/scripts/main.ts --prompt "A landscape" --image landscape.png --ar 16:9

# High quality (2k)
npx -y bun ${SKILL_DIR}/scripts/main.ts --prompt "A cat" --image cat.png --quality 2k

# Specific provider
npx -y bun ${SKILL_DIR}/scripts/main.ts --prompt "A cat" --image cat.png --provider openai

# From prompt files
npx -y bun ${SKILL_DIR}/scripts/main.ts --promptfiles system.md content.md --image out.png

# With reference images (Google multimodal only)
npx -y bun ${SKILL_DIR}/scripts/main.ts --prompt "Make blue" --image out.png --ref source.png

Commands
Basic Image Generation
# Generate with prompt
npx -y bun ${SKILL_DIR}/scripts/main.ts --prompt "A sunset over mountains" --image sunset.png

# Shorthand
npx -y bun ${SKILL_DIR}/scripts/main.ts -p "A cute robot" --image robot.png

Aspect Ratios
# Common ratios: 1:1, 16:9, 9:16, 4:3, 3:4, 2.35:1
npx -y bun ${SKILL_DIR}/scripts/main.ts --prompt "A portrait" --image portrait.png --ar 3:4

# Or specify exact size
npx -y bun ${SKILL_DIR}/scripts/main.ts --prompt "Banner" --image banner.png --size 1792x1024

Reference Images (Google Multimodal)
# Image editing with reference
npx -y bun ${SKILL_DIR}/scripts/main.ts --prompt "Make it blue" --image blue.png --ref original.png

# Multiple references
npx -y bun ${SKILL_DIR}/scripts/main.ts --prompt "Combine these styles" --image out.png --ref a.png b.png

Quality Presets
# Normal quality (default)
npx -y bun ${SKILL_DIR}/scripts/main.ts --prompt "A cat" --image cat.png --quality normal

# High quality (2k resolution)
npx -y bun ${SKILL_DIR}/scripts/main.ts --prompt "A cat" --image cat.png --quality 2k

Output Formats
# Plain output (prints saved path)
npx -y bun ${SKILL_DIR}/scripts/main.ts --prompt "A cat" --image cat.png

# JSON output
npx -y bun ${SKILL_DIR}/scripts/main.ts --prompt "A cat" --image cat.png --json

Options
Option	Description
--prompt <text>, -p	Prompt text
--promptfiles <files...>	Read prompt from files (concatenated)
--image <path>	Output image path (required)
--provider google|openai	Force provider (default: google)
--model <id>, -m	Model ID
--ar <ratio>	Aspect ratio (e.g., 16:9, 1:1, 4:3)
--size <WxH>	Size (e.g., 1024x1024)
--quality normal|2k	Quality preset (default: normal)
--ref <files...>	Reference images (Google multimodal only)
--n <count>	Number of images
--json	JSON output
--help, -h	Show help
Environment Variables
Variable	Description	Default
OPENAI_API_KEY	OpenAI API key	-
GOOGLE_API_KEY	Google API key	-
OPENAI_IMAGE_MODEL	OpenAI model	gpt-image-1.5
GOOGLE_IMAGE_MODEL	Google model	gemini-3-pro-image-preview
OPENAI_BASE_URL	Custom OpenAI endpoint	-
GOOGLE_BASE_URL	Custom Google endpoint	-

Load Priority: CLI args > process.env > <cwd>/.baoyu-skills/.env > ~/.baoyu-skills/.env

Provider & Model Strategy
Auto-Selection
If --provider specified → use it
If only one API key available → use that provider
If both available → default to Google (multimodal LLMs more versatile)
API Selection by Model Type
Model Category	API Function	Example Models
Google Multimodal	generateText	gemini-2.0-flash-exp-image-generation
Google Imagen	experimental_generateImage	imagen-3.0-generate-002
OpenAI	experimental_generateImage	gpt-image-1, dall-e-3
Available Models

Google:

gemini-3-pro-image-preview - Default, multimodal generation
gemini-2.0-flash-exp-image-generation - Gemini 2.0 Flash
imagen-3.0-generate-002 - Imagen 3

OpenAI:

gpt-image-1.5 - Default, GPT Image 1.5
gpt-image-1 - GPT Image 1
dall-e-3 - DALL-E 3
Quality Presets
Preset	OpenAI	Google	Use Case
normal	1024x1024	Default	Covers, illustrations
2k	2048x2048	"2048px" in prompt	Infographics, slides
Aspect Ratio Handling
Multimodal LLMs: Embedded in prompt (e.g., "... aspect ratio 16:9")
Image-only models: Uses aspectRatio or size parameter
Common ratios: 1:1, 16:9, 9:16, 4:3, 3:4, 2.35:1
Examples
Generate Cover Image
npx -y bun ${SKILL_DIR}/scripts/main.ts \
  --prompt "A minimalist tech illustration with blue gradients" \
  --image cover.png --ar 2.35:1 --quality 2k

Generate Social Media Post
npx -y bun ${SKILL_DIR}/scripts/main.ts \
  --prompt "Instagram post about coffee" \
  --image post.png --ar 1:1

Edit Image with Reference
npx -y bun ${SKILL_DIR}/scripts/main.ts \
  --prompt "Change the background to sunset" \
  --image edited.png --ref original.png --provider google

Batch Generation from Prompt File
# Create prompt file with detailed instructions
npx -y bun ${SKILL_DIR}/scripts/main.ts \
  --promptfiles style-guide.md scene-description.md \
  --image scene.png

Error Handling
Missing API key: Clear error with setup instructions
Generation failure: Auto-retry once, then error
Invalid aspect ratio: Warning, proceed with default
Reference images with image-only model: Warning, ignore refs
Extension Support

Custom configurations via EXTEND.md.

Check paths (priority order):

.baoyu-skills/baoyu-image-gen/EXTEND.md (project)
~/.baoyu-skills/baoyu-image-gen/EXTEND.md (user)

If found, load before workflow. Extension content overrides defaults.

Weekly Installs
36
Repository
smallnest/langgraphgo
GitHub Stars
240
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
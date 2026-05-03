---
rating: ⭐⭐
title: image-gen
url: https://skills.sh/marswaveai/skills/image-gen
---

# image-gen

skills/marswaveai/skills/image-gen
image-gen
Installation
$ npx skills add https://github.com/marswaveai/skills --skill image-gen
SKILL.md
When to Use
User wants to generate an AI image from a text description
User says "generate image", "draw", "create picture", "配图"
User says "生成图片", "画一张", "AI图"
User needs a cover image, illustration, or concept art
When NOT to Use
User wants to create audio content (use /podcast, /speech)
User wants to create a video (use /explainer)
User wants to edit an existing image (not supported)
User wants to extract content from a URL (use /content-parser)
Purpose

Generate AI images using the ListenHub CLI. Supports text prompts with optional reference images (local files or URLs), multiple resolutions, and aspect ratios. Images are saved as local files.

Hard Constraints
Always check CLI auth following shared/cli-authentication.md
Follow shared/cli-patterns.md for command execution and error handling
Always read config following shared/config-pattern.md before any interaction
Output saved to .listenhub/image-gen/YYYY-MM-DD-{jobId}/ — never ~/Downloads/
Step -1: CLI Auth Check

Follow shared/cli-authentication.md § Auth Check. If CLI is not installed or not logged in, auto-install and auto-login — never ask the user to run commands manually.

Step 0: Config Setup

Follow shared/config-pattern.md Step 0 (Zero-Question Boot).

If file doesn't exist — silently create with defaults and proceed:

mkdir -p ".listenhub/image-gen"
echo '{"outputDir":".listenhub","outputMode":"inline"}' > ".listenhub/image-gen/config.json"
CONFIG_PATH=".listenhub/image-gen/config.json"
CONFIG=$(cat "$CONFIG_PATH")


Do NOT ask any setup questions. Proceed directly to the Interaction Flow.

If file exists — read config silently and proceed:

CONFIG_PATH=".listenhub/image-gen/config.json"
[ ! -f "$CONFIG_PATH" ] && CONFIG_PATH="$HOME/.listenhub/image-gen/config.json"
CONFIG=$(cat "$CONFIG_PATH")

Setup Flow (user-initiated reconfigure only)

Only run when the user explicitly asks to reconfigure. Display current settings:

当前配置 (image-gen)：
  输出方式：{inline / download / both}


Then ask:

outputMode: Follow shared/output-mode.md § Setup Flow Question.

Save immediately:

NEW_CONFIG=$(echo "$CONFIG" | jq --arg m "$OUTPUT_MODE" '. + {"outputMode": $m}')
echo "$NEW_CONFIG" > "$CONFIG_PATH"
CONFIG=$(cat "$CONFIG_PATH")

Interaction Flow
Step 1: Image Description

Free text input. Ask the user:

Describe the image you want to generate.

If the prompt is very short (< 10 words) and the user hasn't asked for verbatim generation, offer to help enrich the prompt. Otherwise, use as-is.

Step 2: Model

Ask:

Question: "Which model?"
Options:
  - "pro (recommended)" — gemini-3-pro-image-preview, higher quality
  - "flash" — gemini-3.1-flash-image-preview, faster and cheaper, unlocks extreme aspect ratios (1:4, 4:1, 1:8, 8:1)

Step 3: Resolution and Aspect Ratio

Ask both together (independent parameters):

Question: "What resolution?"
Options:
  - "1K" — Standard quality
  - "2K (recommended)" — High quality, good balance
  - "4K" — Ultra high quality, slower generation

Question: "What aspect ratio?"
Options (all models):
  - "16:9" — Landscape, widescreen
  - "1:1" — Square
  - "9:16" — Portrait, phone screen
  - "Other" — 2:3, 3:2, 3:4, 4:3, 21:9


If flash model was selected, also offer: 1:4 (narrow portrait), 4:1 (wide landscape), 1:8 (extreme portrait), 8:1 (panoramic)

Step 4: Reference Images (optional)
Question: "Any reference images for style guidance?"
Options:
  - "Yes" — Provide file paths or URLs
  - "No references" — Generate from prompt only


If yes: Collect reference image paths or URLs (comma-separated). The CLI handles both local files and URLs natively — no need to distinguish between them.

Max 5 references
Supported formats: jpg, png, webp, gif
Max 10MB per file

Each reference will be passed as a --reference flag to the CLI.

Step 5: Confirm & Generate

Summarize all choices:

Ready to generate image:

  Prompt: {prompt text}
  Model: {pro / flash}
  Resolution: {1K / 2K / 4K}
  Aspect ratio: {ratio}
  References: {yes — N image(s) / no}

  Proceed?


Wait for explicit confirmation before running the CLI command.

Workflow

Build CLI command: Construct the listenhub image create command with all collected parameters.

Execute: Run the command with run_in_background: true and timeout: 180000:

listenhub image create \
  --prompt "{description}" \
  --model "{model}" \
  --lang "{lang}" \
  --aspect-ratio {16:9|9:16|1:1} \
  --size {1K|2K|4K} \
  --json


If reference images were provided, add --reference for each:

listenhub image create \
  --prompt "{description}" \
  --model "{model}" \
  --lang "{lang}" \
  --aspect-ratio 16:9 \
  --size 2K \
  --reference ./sketch.png \
  --reference ./photo.jpg \
  --json


The --lang flag provides a language hint for the prompt. Detect from the user's prompt language (e.g., Chinese prompt → zh, English prompt → en).

Parse result and present

Read OUTPUT_MODE from config. Follow shared/output-mode.md for behavior.

Parse the CLI JSON output to extract the image URL:

IMAGE_URL=$(echo "$RESULT" | jq -r '.imageUrl')


inline or both: Download to a temp file, then use the Read tool.

JOB_ID=$(date +%s)
listenhub download "$IMAGE_URL" -o /tmp/image-gen-${JOB_ID}.jpg


Then use the Read tool on /tmp/image-gen-{jobId}.jpg. The image displays inline in the conversation.

Present:

图片已生成！


download or both: Save to the artifact directory.

JOB_ID=$(date +%s)
DATE=$(date +%Y-%m-%d)
JOB_DIR=".listenhub/image-gen/${DATE}-${JOB_ID}"
mkdir -p "$JOB_DIR"
listenhub download "$IMAGE_URL" -o "${JOB_DIR}/${JOB_ID}.jpg"


Present:

图片已生成！

已保存到 .listenhub/image-gen/{YYYY-MM-DD}-{jobId}/：
  {jobId}.jpg

Prompt Handling

Default: Pass the user's prompt directly without modification.

When to offer optimization:

Prompt is very short (a few words) AND user hasn't requested verbatim
Ask: "Would you like help enriching the prompt with style/lighting/composition details?"

When to never modify:

Long, detailed, or structured prompts — treat the user as experienced
User says "use this prompt exactly"

Optimization techniques (if user agrees):

Style: "cyberpunk" → add "neon lights, futuristic, dystopian"
Scene: time of day, lighting, weather
Quality: "highly detailed", "8K quality", "cinematic composition"
Always use English keywords (models trained on English)
Show optimized prompt before submitting
API Reference
CLI authentication: shared/cli-authentication.md
CLI execution patterns: shared/cli-patterns.md
Config pattern: shared/config-pattern.md
Output mode: shared/output-mode.md
Composability
Invokes: nothing (direct CLI call)
Invoked by: platform skills for cover images (Phase 2)
Example

User: "Generate an image: cyberpunk city at night"

Agent workflow:

Prompt is short → offer enrichment → user declines
Ask model → "pro"
Ask resolution → "2K"
Ask ratio → "16:9"
No references
listenhub image create \
  --prompt "cyberpunk city at night" \
  --model "gemini-3-pro-image-preview" \
  --lang en \
  --aspect-ratio 16:9 \
  --size 2K \
  --json


Parse CLI JSON output per outputMode (see shared/output-mode.md).

Example 2 — With Reference Images

User: "Generate an image in this style" (provides local files and a URL)

Agent workflow:

Ask prompt → "a serene mountain lake at dawn"
Ask model → "pro"
Ask resolution → "2K"
Ask ratio → "16:9"
References → /path/to/style-reference.png, https://example.com/photo.jpg
listenhub image create \
  --prompt "a serene mountain lake at dawn" \
  --model "gemini-3-pro-image-preview" \
  --lang en \
  --aspect-ratio 16:9 \
  --size 2K \
  --reference /path/to/style-reference.png \
  --reference https://example.com/photo.jpg \
  --json


Parse CLI JSON output per outputMode (see shared/output-mode.md).

Weekly Installs
675
Repository
marswaveai/skills
GitHub Stars
49
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn
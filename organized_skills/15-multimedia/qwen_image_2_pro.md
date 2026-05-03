---
rating: ⭐⭐⭐
title: qwen-image-2-pro
url: https://skills.sh/inference-sh/skills/qwen-image-2-pro
---

# qwen-image-2-pro

skills/inference-sh/skills/qwen-image-2-pro
qwen-image-2-pro
Installation
$ npx skills add https://github.com/inference-sh/skills --skill qwen-image-2-pro
SKILL.md
Qwen-Image Pro - Professional Image Generation

Generate images with Alibaba Qwen-Image-2.0-Pro via inference.sh CLI. Best for professional text rendering and complex designs.

Quick Start

Requires inference.sh CLI (belt). Install instructions

belt login

belt app run alibaba/qwen-image-2-pro --input '{"prompt": "Poster with title \"Welcome!\" in bold blue text"}'

Pro Model Capabilities
Professional Text Rendering: Multi-line and paragraph-level text with fine-grained detail
Fine-grained Realism: Better textures and photorealistic scenes
Stronger Semantic Adherence: More accurately follows complex prompts
Complex Designs: Ideal for text + image combinations
Examples
Basic Text-to-Image
belt app run alibaba/qwen-image-2-pro --input '{
  "prompt": "A futuristic cityscape at sunset with flying cars"
}'

Text-Heavy Poster
belt app run alibaba/qwen-image-2-pro --input '{
  "prompt": "Healing-style hand-drawn poster featuring three puppies playing with a ball. The main title \"Come Play Ball!\" is prominently displayed at the top in bold, blue cartoon font. Below, the subtitle \"Join the Fun!\" appears in green font.",
  "width": 1024,
  "height": 1536,
  "prompt_extend": false
}'

Marketing Banner
belt app run alibaba/qwen-image-2-pro --input '{
  "prompt": "Professional marketing banner for summer sale. Large text \"SUMMER SALE\" in white on gradient sunset background. \"50% OFF\" in yellow below. Clean, modern design.",
  "width": 1920,
  "height": 1080,
  "prompt_extend": false,
  "negative_prompt": "blurry text, distorted text, low quality"
}'

Multiple Variations
belt app run alibaba/qwen-image-2-pro --input '{
  "prompt": "Minimalist logo design for a coffee shop called \"Bean & Brew\"",
  "num_images": 4
}'

Image Editing (Style Transfer)
belt app run alibaba/qwen-image-2-pro --input '{
  "prompt": "Make the person from Image 1 wear the outfit from Image 2",
  "reference_images": [
    {"uri": "https://example.com/person.jpg"},
    {"uri": "https://example.com/outfit.jpg"}
  ],
  "num_images": 2
}'

Reproducible Generation
belt app run alibaba/qwen-image-2-pro --input '{
  "prompt": "Abstract geometric art in blue and gold",
  "seed": 12345
}'

Input Options
Parameter	Type	Description
prompt	string	Required. What to generate or edit (max 800 chars)
reference_images	array	Input images for editing (1-3 images)
num_images	integer	Number of images to generate (1-6)
width	integer	Output width in pixels (512-2048)
height	integer	Output height in pixels (512-2048)
watermark	boolean	Add "Qwen-Image" watermark
negative_prompt	string	Content to avoid (max 500 chars)
prompt_extend	boolean	Enable prompt rewriting (default: true)
seed	integer	Random seed for reproducibility (0-2147483647)

Size constraint: Total pixels must be between 512×512 and 2048×2048.

Output
Field	Type	Description
images	array	The generated or edited images (PNG format)
output_meta	object	Metadata with dimensions and count
Text Rendering Tips

For best text results with the Pro model:

Use quotes around exact text: "Title: \"Hello World!\""
Specify font details: color, style, size, position
Disable prompt_extend: Set prompt_extend: false for precise control
Use negative prompts: "blurry text, distorted text, low quality"

Example prompt structure:

Poster with the title "GRAND OPENING" in large red serif font at the top center.
Below, the date "March 15, 2024" in smaller black text.
Background: elegant gold and white gradient.
Style: professional, clean, modern.

Recommended Negative Prompt
{
  "negative_prompt": "low resolution, low quality, deformed limbs, deformed fingers, oversaturated, waxy, no facial details, overly smooth, AI-like, chaotic composition, blurry text, distorted text"
}

Sample Workflow
# 1. Generate sample input to see all options
belt app sample alibaba/qwen-image-2-pro --save input.json

# 2. Edit the prompt
# 3. Run
belt app run alibaba/qwen-image-2-pro --input input.json

Python SDK
from inferencesh import inference

client = inference()

# Text-heavy poster
result = client.run({
    "app": "alibaba/qwen-image-2-pro",
    "input": {
        "prompt": "Poster with title \"Welcome!\" in bold blue text at top",
        "width": 1024,
        "height": 1536,
        "prompt_extend": False
    }
})
print(result["output"])

# Stream live updates
for update in client.run({
    "app": "alibaba/qwen-image-2-pro",
    "input": {
        "prompt": "Professional product photography of a watch"
    }
}, stream=True):
    if update.get("progress"):
        print(f"progress: {update['progress']}%")
    if update.get("output"):
        print(f"output: {update['output']}")

Related Skills
# Standard Qwen-Image (faster, general use)
npx skills add inference-sh/skills@qwen-image

# Full platform skill (all 250+ apps)
npx skills add inference-sh/skills@infsh-cli

# All image generation models
npx skills add inference-sh/skills@ai-image-generation


Browse all image apps: belt app list --category image

Documentation
Running Apps - How to run apps via CLI
Streaming Results - Real-time progress updates
File Handling - Working with images
Weekly Installs
286
Repository
inference-sh/skills
GitHub Stars
395
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
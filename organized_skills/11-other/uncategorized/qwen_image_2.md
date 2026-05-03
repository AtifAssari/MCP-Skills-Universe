---
rating: ⭐⭐⭐
title: qwen-image-2
url: https://skills.sh/inference-sh/skills/qwen-image-2
---

# qwen-image-2

skills/inference-sh/skills/qwen-image-2
qwen-image-2
Installation
$ npx skills add https://github.com/inference-sh/skills --skill qwen-image-2
SKILL.md
Qwen-Image - Alibaba Image Generation

Generate and edit images with Alibaba Qwen-Image-2.0 models via inference.sh CLI.

Quick Start

Requires inference.sh CLI (belt). Install instructions

belt login

belt app run alibaba/qwen-image-2 --input '{"prompt": "A serene mountain landscape at sunset"}'

Models
Model	App ID	Speed	Text Rendering	Best For
Qwen-Image-2.0	alibaba/qwen-image-2	Fast	Good	General use
Qwen-Image-2.0-Pro	alibaba/qwen-image-2-pro	Standard	Professional	Posters, text-heavy designs
Search Qwen Image Apps
belt app list --search "qwen image"

Examples
Basic Text-to-Image
belt app run alibaba/qwen-image-2 --input '{
  "prompt": "A futuristic cityscape at sunset with flying cars"
}'

Multiple Images
belt app run alibaba/qwen-image-2 --input '{
  "prompt": "Minimalist logo design for a coffee shop",
  "num_images": 4
}'

Custom Resolution
belt app run alibaba/qwen-image-2-pro --input '{
  "prompt": "Panoramic mountain landscape with northern lights",
  "width": 1536,
  "height": 1024
}'

Text-Heavy Poster (Pro)
belt app run alibaba/qwen-image-2-pro --input '{
  "prompt": "Poster with title \"Summer Sale!\" in bold red text at the top. Subtitle \"50% Off Everything\" in blue below. Beach background with palm trees.",
  "width": 1024,
  "height": 1536,
  "prompt_extend": false
}'

Image Editing (Multi-Reference)
belt app run alibaba/qwen-image-2 --input '{
  "prompt": "Make the girl from Image 1 wear the dress from Image 2 in the pose from Image 3",
  "reference_images": [
    {"uri": "https://example.com/person.jpg"},
    {"uri": "https://example.com/dress.jpg"},
    {"uri": "https://example.com/pose.jpg"}
  ]
}'

With Negative Prompt
belt app run alibaba/qwen-image-2-pro --input '{
  "prompt": "Professional headshot portrait, studio lighting",
  "negative_prompt": "low resolution, blurry, deformed, oversaturated"
}'

Reproducible with Seed
belt app run alibaba/qwen-image-2 --input '{
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
Prompt Tips

For Text Rendering (use Pro model):

Put exact text in quotes: "Title: \"Hello World!\""
Specify font style, color, position
Set prompt_extend: false for precise control

Styles: photorealistic, illustration, watercolor, oil painting, digital art, anime, 3D render

Composition: close-up, wide shot, aerial view, macro, portrait, landscape

Lighting: natural light, studio lighting, golden hour, dramatic shadows, neon

Sample Workflow
# 1. Generate sample input to see all options
belt app sample alibaba/qwen-image-2-pro --save input.json

# 2. Edit the prompt
# 3. Run
belt app run alibaba/qwen-image-2-pro --input input.json

Model Comparison
Feature	qwen-image-2	qwen-image-2-pro
Speed	Faster	Standard
Text Rendering	Good	Professional
Realism	Standard	Fine-grained
Semantic Adherence	Good	Enhanced
Related Skills
# Full platform skill (all 250+ apps)
npx skills add inference-sh/skills@infsh-cli

# All image generation models
npx skills add inference-sh/skills@ai-image-generation

# Video generation (for image-to-video)
npx skills add inference-sh/skills@ai-video-generation


Browse all image apps: belt app list --category image

Documentation
Running Apps - How to run apps via CLI
Streaming Results - Real-time progress updates
File Handling - Working with images
Weekly Installs
285
Repository
inference-sh/skills
GitHub Stars
395
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
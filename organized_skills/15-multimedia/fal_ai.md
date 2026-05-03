---
rating: ⭐⭐
title: fal.ai
url: https://skills.sh/vm0-ai/vm0-skills/fal.ai
---

# fal.ai

skills/vm0-ai/vm0-skills/fal.ai
fal.ai
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill fal.ai
SKILL.md
fal.ai Image Generator

Use the fal.ai API to generate images from text prompts.

Official docs: https://fal.ai/docs

When to Use

Use this skill when you need to:

Generate images from text descriptions
Create illustrations or visual content
Generate blog headers, thumbnails, or social media images
Prerequisites
Sign up at fal.ai
Get your API key from the dashboard
export FAL_KEY="your-api-key"


Important: When using $VAR in a command that pipes to another command, wrap the command containing $VAR in bash -c '...'. Due to a Claude Code bug, environment variables are silently cleared when pipes are used directly.

bash -c 'curl -s "https://api.example.com" -H "Authorization: Bearer $API_KEY"'

How to Use
1. Generate Image (nano-banana-pro - fast)

Write to /tmp/fal_request.json:

{
  "prompt": "A futuristic city at sunset, cyberpunk style"
}


Then run:

bash -c 'curl -s -X POST "https://fal.run/fal-ai/nano-banana-pro" --header "Authorization: Key ${FAL_KEY}" --header "Content-Type: application/json" -d @/tmp/fal_request.json' | jq -r '.images[0].url'

2. Generate Image (flux/schnell - fast)

Write to /tmp/fal_request.json:

{
  "prompt": "A cute cat eating a cookie"
}


Then run:

bash -c 'curl -s -X POST "https://fal.run/fal-ai/flux/schnell" --header "Authorization: Key ${FAL_KEY}" --header "Content-Type: application/json" -d @/tmp/fal_request.json' | jq -r '.images[0].url'

3. Generate Image (recraft-v3 - high quality)

Write to /tmp/fal_request.json:

{
  "prompt": "Abstract art, vibrant colors"
}


Then run:

bash -c 'curl -s -X POST "https://fal.run/fal-ai/recraft-v3" --header "Authorization: Key ${FAL_KEY}" --header "Content-Type: application/json" -d @/tmp/fal_request.json' | jq -r '.images[0].url'

4. Generate with Custom Size

Write to /tmp/fal_request.json:

{
  "prompt": "Mountain landscape",
  "image_size": "landscape_16_9"
}


Then run:

bash -c 'curl -s -X POST "https://fal.run/fal-ai/nano-banana-pro" --header "Authorization: Key ${FAL_KEY}" --header "Content-Type: application/json" -d @/tmp/fal_request.json' | jq -r '.images[0].url'

5. Download Generated Image

Write to /tmp/fal_request.json:

{
  "prompt": "A minimalist workspace"
}


Then run:

bash -c 'curl -s -X POST "https://fal.run/fal-ai/nano-banana-pro" --header "Authorization: Key ${FAL_KEY}" --header "Content-Type: application/json" -d @/tmp/fal_request.json' | jq -r '.images[0].url' | xargs curl -sL -o /tmp/image.png

6. Pipe Prompt from Echo (JSON escaped)
echo "A dragon breathing fire, epic fantasy art" | jq -Rs '{prompt: .}' > /tmp/fal_request.json
bash -c 'curl -s -X POST "https://fal.run/fal-ai/nano-banana-pro" --header "Authorization: Key ${FAL_KEY}" --header "Content-Type: application/json" -d @/tmp/fal_request.json' | jq -r '.images[0].url'

7. Pipe Prompt from File (JSON escaped)
cat /tmp/prompt.txt | jq -Rs '{prompt: .}' > /tmp/fal_request.json
bash -c 'curl -s -X POST "https://fal.run/fal-ai/nano-banana-pro" --header "Authorization: Key ${FAL_KEY}" --header "Content-Type: application/json" -d @/tmp/fal_request.json' | jq -r '.images[0].url'

8. Pipe with Additional Parameters
echo "Neon city at night" | jq -Rs '{prompt: ., image_size: "landscape_16_9"}' > /tmp/fal_request.json
bash -c 'curl -s -X POST "https://fal.run/fal-ai/nano-banana-pro" --header "Authorization: Key ${FAL_KEY}" --header "Content-Type: application/json" -d @/tmp/fal_request.json' | jq -r '.images[0].url'

Available Models
Model	Description
nano-banana-pro	Fast, good quality (recommended)
flux/schnell	Fast generation
flux-pro	High quality
recraft-v3	High quality vector/illustration

See more at: https://fal.ai/models

Image Sizes
Size	Aspect Ratio
square	1:1
square_hd	1:1 (high res)
portrait_4_3	4:3
portrait_16_9	16:9
landscape_4_3	3:4
landscape_16_9	9:16
Prompt Guidelines

For best results:

Be specific - Describe the subject clearly
Add style hints - "modern", "minimalist", "photorealistic", "digital art", "cinematic"
Specify colors/mood - "blue and purple gradient", "warm tones", "dark and moody"
Keep it concise - Clear and focused descriptions work better
Weekly Installs
53
Repository
vm0-ai/vm0-skills
GitHub Stars
57
First Seen
Jan 24, 2026
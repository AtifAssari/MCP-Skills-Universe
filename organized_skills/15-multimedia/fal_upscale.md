---
rating: ⭐⭐⭐
title: fal-upscale
url: https://skills.sh/fal-ai-community/skills/fal-upscale
---

# fal-upscale

skills/fal-ai-community/skills/fal-upscale
fal-upscale
Installation
$ npx skills add https://github.com/fal-ai-community/skills --skill fal-upscale
SKILL.md
fal.ai Upscale

Upscale and enhance image resolution using state-of-the-art AI models.

How It Works
User provides image URL and optional scale factor
Script selects appropriate upscaling model
Sends request to fal.ai API
Returns upscaled image URL
Finding Models

To discover the best and latest upscaling models, use the search API:

# Search for image upscale models
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "upscale image"

# Search for video upscale models
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "upscale video"

# Search for super-resolution models
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "super resolution"


Or use the search_models MCP tool with keywords like "upscale", "super resolution", "enhance".

Usage
bash /mnt/skills/user/fal-upscale/scripts/upscale.sh [options]


Arguments:

--image-url - URL of image to upscale (required)
--model - Model ID (defaults to fal-ai/aura-sr)
--scale - Upscale factor: 2 or 4 (default: 4)

Examples:

# Image upscale with AuraSR (4x, fast)
bash /mnt/skills/user/fal-upscale/scripts/upscale.sh \
  --image-url "https://example.com/image.jpg"

# Image upscale with Clarity (detail preservation)
bash /mnt/skills/user/fal-upscale/scripts/upscale.sh \
  --image-url "https://example.com/image.jpg" \
  --model "fal-ai/clarity-upscaler" \
  --scale 2

# Video upscale (general purpose)
bash /mnt/skills/user/fal-upscale/scripts/upscale.sh \
  --video-url "https://example.com/video.mp4" \
  --model "fal-ai/video-upscaler"

# Video upscale (premium quality)
bash /mnt/skills/user/fal-upscale/scripts/upscale.sh \
  --video-url "https://example.com/video.mp4" \
  --model "fal-ai/topaz/upscale/video"

MCP Tool Alternative

Use search_models MCP tool or search-models.sh to find the best current upscaling model, then call mcp__fal-ai__generate with the discovered modelId.

Output
Upscaling with fal-ai/aura-sr...
Upscale complete!

Image URL: https://v3.fal.media/files/abc123/upscaled.png
Original: 512x512
Upscaled: 2048x2048


JSON output:

{
  "image": {
    "url": "https://v3.fal.media/files/abc123/upscaled.png",
    "width": 2048,
    "height": 2048
  }
}

Present Results to User
Here's your upscaled image:

![Upscaled Image](https://v3.fal.media/files/...)

• 512×512 → 2048×2048 (4x)

Model Selection Tips
Image upscaling: Search for "upscale image" or "super resolution". Consider speed vs quality tradeoffs.
Video upscaling: Search for "upscale video". Premium models offer better quality but cost more.
Scale factors typically range from 2x to 4x depending on the model.
Troubleshooting
API Key Error
Error: FAL_KEY environment variable not set

To fix:
1. Get your API key from https://fal.ai/dashboard/keys
2. Set: export FAL_KEY=your_key_here

Image URL Error
Error: Could not fetch image from URL

Make sure:
1. The image URL is publicly accessible
2. The URL points directly to an image file
3. The image format is supported (JPEG, PNG, WebP)

Network Error
Network error. To fix on claude.ai:

1. Go to https://claude.ai/settings/capabilities
2. Add *.fal.ai to the allowed domains
3. Try again

Weekly Installs
243
Repository
fal-ai-community/skills
GitHub Stars
115
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
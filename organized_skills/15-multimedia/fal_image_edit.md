---
rating: ⭐⭐⭐
title: fal-image-edit
url: https://skills.sh/fal-ai-community/skills/fal-image-edit
---

# fal-image-edit

skills/fal-ai-community/skills/fal-image-edit
fal-image-edit
Installation
$ npx skills add https://github.com/fal-ai-community/skills --skill fal-image-edit
Summary

AI-powered image editing with style transfer, object removal, background changes, and inpainting.

Supports five core operations: style transfer, object removal, background replacement, inpainting with masks, and general instruction-based edits
Configurable strength parameter (0.0–1.0) to control edit intensity from subtle to dramatic
Includes model discovery via search API to find the best current model for each operation type
Requires image URL and editing prompt; optional mask URL for precise inpainting and removal tasks
Returns edited image URL with dimensions; supports JSON output for programmatic integration
SKILL.md
fal.ai Image Edit

Edit images using AI: style transfer, object removal, background changes, and more.

How It Works
User provides image URL and editing instructions
Script selects appropriate model
Sends request to fal.ai API
Returns edited image URL
Finding Models

To discover the best and latest image editing models, use the search API:

# Search for image editing models
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --category "image-to-image"

# Search for specific editing capabilities
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "image editing"
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "inpainting"
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "object removal"
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "background removal"


Or use the search_models MCP tool with relevant keywords.

Supported Operations
Operation	Description
Style Transfer	Apply artistic style to image
Object Removal	Remove objects from image
Background Change	Change/replace background
Inpainting	Fill in masked areas
General Edit	Instruction-based edits
Usage
bash /mnt/skills/user/fal-image-edit/scripts/edit-image.sh [options]


Arguments:

--image-url - URL of image to edit (required)
--prompt - Description of desired edit (required)
--operation - Edit operation: style, remove, background, inpaint (default: style)
--mask-url - URL of mask image (required for inpainting/removal)
--strength - Edit strength 0.0-1.0 (default: 0.75)

Examples:

# Style transfer
bash /mnt/skills/user/fal-image-edit/scripts/edit-image.sh \
  --image-url "https://example.com/photo.jpg" \
  --prompt "Convert to anime style" \
  --operation style

# Remove object
bash /mnt/skills/user/fal-image-edit/scripts/edit-image.sh \
  --image-url "https://example.com/photo.jpg" \
  --prompt "Remove the person on the left" \
  --operation remove

# Change background
bash /mnt/skills/user/fal-image-edit/scripts/edit-image.sh \
  --image-url "https://example.com/portrait.jpg" \
  --prompt "Place in a tropical beach setting" \
  --operation background

# Inpainting with mask
bash /mnt/skills/user/fal-image-edit/scripts/edit-image.sh \
  --image-url "https://example.com/photo.jpg" \
  --mask-url "https://example.com/mask.png" \
  --prompt "Fill with flowers" \
  --operation inpaint

MCP Tool Alternative

Use search_models MCP tool or search-models.sh to find the best current model for each operation (style transfer, object removal, background change, inpainting), then call mcp__fal-ai__generate with the discovered modelId.

Output
Editing image...
Model: fal-ai/flux/dev/image-to-image
Operation: style transfer

Edit complete!

Image URL: https://v3.fal.media/files/abc123/edited.png
Dimensions: 1024x1024


JSON output:

{
  "images": [
    {
      "url": "https://v3.fal.media/files/abc123/edited.png",
      "width": 1024,
      "height": 1024
    }
  ]
}

Present Results to User
Here's your edited image:

![Edited Image](https://v3.fal.media/files/...)

• 1024×1024 | Operation: Style Transfer

Model Selection Tips
General Editing: Search for "image editing" models. Good for instruction-based changes.
Style Transfer: Search for image-to-image category. Adjust strength: 0.3-0.5 for subtle, 0.7-0.9 for dramatic.
Object Removal: Search for "eraser" or "object removal". Some work without masks.
Background Change: Search for "background" or "kontext". Look for models that preserve subject identity.
Inpainting: Search for "inpainting" or "fill". Requires binary mask (white = edit area).
Mask Tips

For inpainting and some removal tasks:

White pixels = areas to edit
Black pixels = areas to preserve
Use PNG format with transparency or solid colors
Feathered edges create smoother transitions
Troubleshooting
Edit Too Subtle
The edit is barely visible.

Increase the strength parameter:
--strength 0.85

Edit Too Dramatic
The edit changed too much of the image.

Decrease the strength parameter:
--strength 0.3

Object Not Removed
The object wasn't fully removed.

Tips:
1. Be more specific in the prompt
2. Try using an explicit mask
3. Use the inpainting model for precise control

Background Artifacts
The new background has artifacts around the subject.

Tips:
1. Use a cleaner source image
2. Try FLUX Kontext which handles edges better
3. Adjust the strength for smoother blending

Weekly Installs
859
Repository
fal-ai-community/skills
GitHub Stars
115
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass
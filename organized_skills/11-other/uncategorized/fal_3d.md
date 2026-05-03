---
rating: ⭐⭐⭐
title: fal-3d
url: https://skills.sh/fal-ai-community/skills/fal-3d
---

# fal-3d

skills/fal-ai-community/skills/fal-3d
fal-3d
Installation
$ npx skills add https://github.com/fal-ai-community/skills --skill fal-3d
SKILL.md
fal-3d

Generate 3D models (GLB/OBJ/PLY) from text descriptions or images using fal.ai.

Scripts
Script	Purpose
generate-3d.sh	Generate a 3D model from text or image
Usage
Image to 3D
./scripts/generate-3d.sh --image-url "https://example.com/object.jpg" --model fal-ai/hunyuan3d-v3/image-to-3d

Text to 3D
./scripts/generate-3d.sh --prompt "A medieval sword with ornate handle" --model fal-ai/meshy/v6/text-to-3d

Arguments
Argument	Description	Required
--image-url	URL of image to convert to 3D	Yes (or --prompt)
--prompt / -p	Text description for text-to-3D	Yes (or --image-url)
--model / -m	Model endpoint	No (default: fal-ai/hunyuan3d-v3/image-to-3d)
--param	Extra param as key=value (repeatable)	No
Finding Models

To discover the best and latest 3D generation models, use the search API:

# Search for image-to-3D models
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --category "image-to-3d"

# Search for text-to-3D models
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "text to 3d"


Or use the search_models MCP tool with relevant keywords like "3d", "mesh", "image-to-3d".

Tips
For best results from images: use a clear photo with a single object on a plain background
Remove background first if needed (use fal-image-edit or fal-generate with birefnet)
Simple, well-defined objects work best — complex scenes don't reconstruct well yet
3D generation takes 1-5 minutes — jobs use the queue API
Output Format
{
  "mesh": {
    "url": "https://fal.media/files/.../model.glb",
    "content_type": "model/gltf-binary",
    "file_name": "model.glb"
  }
}

Weekly Installs
110
Repository
fal-ai-community/skills
GitHub Stars
115
First Seen
Mar 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
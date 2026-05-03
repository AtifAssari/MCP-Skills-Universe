---
title: fal-kling-o3
url: https://skills.sh/fal-ai-community/skills/fal-kling-o3
---

# fal-kling-o3

skills/fal-ai-community/skills/fal-kling-o3
fal-kling-o3
Installation
$ npx skills add https://github.com/fal-ai-community/skills --skill fal-kling-o3
SKILL.md
fal-kling-o3

Kling O3 is Kling's most powerful model family — covering image generation, text-to-video, image-to-video, and video-to-video editing/remix. Two tiers: Standard (faster, cheaper) and Pro (highest quality).

Scripts
Script	Purpose
kling-generate.sh	Generate images with Kling O3
kling-video.sh	Generate or edit videos with Kling O3
Usage
Generate Image
./scripts/kling-generate.sh --prompt "A samurai standing on a cliff at sunset, cinematic lighting"

Text to Video
./scripts/kling-video.sh --prompt "A drone shot flying over a tropical island at golden hour" --mode text-to-video

Image to Video
./scripts/kling-video.sh --image-url "https://example.com/photo.jpg" --prompt "Camera slowly zooms in" --mode image-to-video

Edit Video (change content)
./scripts/kling-video.sh --video-url "https://example.com/video.mp4" --prompt "Change the sky to a starry night" --mode edit

Remix Video (restyle)
./scripts/kling-video.sh --video-url "https://example.com/video.mp4" --prompt "Transform into watercolor painting style" --mode remix

Arguments
kling-generate.sh
Argument	Description	Required
--prompt / -p	Image description	Yes
--aspect-ratio	square, landscape, portrait, widescreen	No (default: square)
--param	Extra param as key=value (repeatable)	No
kling-video.sh
Argument	Description	Required
--prompt / -p	Description or edit instructions	Yes
--mode	text-to-video, image-to-video, edit, remix	Yes
--image-url	Image URL (for image-to-video)	For I2V
--video-url	Video URL (for edit/remix)	For edit/remix
--tier	standard or pro (default: pro)	No
--param	Extra param as key=value (repeatable)	No
Kling O3 Model Endpoints
Image Generation
Endpoint	Tier
fal-ai/kling-image/o3/text-to-image	Pro (only tier)
Video Generation
Endpoint	Tier	Mode
fal-ai/kling-video/o3/standard/text-to-video	Standard	Text → Video
fal-ai/kling-video/o3/pro/text-to-video	Pro	Text → Video
fal-ai/kling-video/o3/standard/image-to-video	Standard	Image → Video
fal-ai/kling-video/o3/pro/image-to-video	Pro	Image → Video
Video Editing
Endpoint	Tier	Mode
fal-ai/kling-video/o3/standard/video-to-video/edit	Standard	Content editing
fal-ai/kling-video/o3/pro/video-to-video/edit	Pro	Content editing
fal-ai/kling-video/o3/standard/video-to-video/reference	Standard	Style remix
fal-ai/kling-video/o3/pro/video-to-video/reference	Pro	Style remix
When to use Standard vs Pro
Pro: Best quality. Use for final output, commercial work, when quality matters most.
Standard: ~2x faster, cheaper. Use for drafts, iteration, when speed matters.
Output Format
{
  "images": [{"url": "https://fal.media/files/...", "content_type": "image/png"}],
  "video": {"url": "https://fal.media/files/...", "content_type": "video/mp4"}
}

Weekly Installs
112
Repository
fal-ai-community/skills
GitHub Stars
115
First Seen
Mar 7, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn
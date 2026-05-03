---
rating: ⭐⭐
title: avatar-video
url: https://skills.sh/heygen-com/skills/avatar-video
---

# avatar-video

skills/heygen-com/skills/avatar-video
avatar-video
Installation
$ npx skills add https://github.com/heygen-com/skills --skill avatar-video
SKILL.md
Avatar Video

Create AI avatar videos with full control over avatars, voices, scripts, and backgrounds using POST /v3/videos. Two creation modes via discriminated union on type:

"type": "avatar" + avatar_id — use a HeyGen avatar from the library
"type": "image" + image (AssetInput) — animate any photo via Avatar IV
Authentication

All requests require the X-Api-Key header. Set the HEYGEN_API_KEY environment variable.

curl -X GET "https://api.heygen.com/v3/avatars" \
  -H "X-Api-Key: $HEYGEN_API_KEY"

Tool Selection

If HeyGen MCP tools are available (mcp__heygen__*), prefer them over direct HTTP API calls — they handle authentication and request formatting automatically.

Task	MCP Tool	Fallback (Direct API)
Check video status / get URL	mcp__heygen__get_video	GET /v3/videos/{video_id}
List account videos	mcp__heygen__list_videos	GET /v3/videos
Delete a video	mcp__heygen__delete_video	DELETE /v3/videos/{video_id}

Video generation (POST /v3/videos) and avatar/voice listing are done via direct API calls — see reference files below.

Default Workflow
List avatar looks — GET /v3/avatars/looks → pick a look, note its id (this is the avatar_id) and default_voice_id. See avatars.md
List voices (if needed) — GET /v3/voices → pick a voice matching the avatar's gender/language. See voices.md
Write the script — Structure scenes with one concept each. See scripts.md
Generate the video — POST /v3/videos with avatar_id, voice_id, script, and optional background per scene. See video-generation.md
Poll for completion — GET /v3/videos/{video_id} until status is completed. See video-status.md
Routing: This Skill vs Create Video

This skill = precise control (specific avatar, exact script, custom background). create-video = prompt-based ("make me a video about X", AI handles the rest).

Reference Files

Read these as needed — they contain endpoint details, request/response schemas, and code examples (curl, TypeScript, Python).

Core workflow:

references/video-generation.md — POST /v3/videos request fields, avatar input modes, voice settings, backgrounds
references/avatars.md — GET /v3/avatars (groups) and GET /v3/avatars/looks (looks → avatar_id)
references/voices.md — GET /v3/voices with filtering by language, gender, engine
references/video-status.md — GET /v3/videos/{id} polling patterns and download

Customization:

references/scripts.md — Script writing, SSML break tags, pacing
references/backgrounds.md — Solid color and image backgrounds
references/captions.md — Auto-generated captions/subtitles
references/text-overlays.md — Text overlays with fonts and positioning

Advanced:

references/photo-avatars.md — Animate photos via type: "image" (Avatar IV), AI-generated avatars
references/templates.md — Template listing and variable replacement
references/remotion-integration.md — Using HeyGen avatars in Remotion compositions
references/webhooks.md — Webhook endpoints and events
references/assets.md — Uploading images, videos, audio
references/dimensions.md — Resolution and aspect ratios
references/quota.md — Credit system and usage limits
Best Practices
Preview avatars before generating — Use GET /v3/avatars/looks and download preview_image_url so the user can see the avatar before committing
Use avatar's default voice — Most avatars have a default_voice_id pre-matched for natural results
Fallback: match gender manually — If no default voice, ensure avatar and voice genders match
Use test mode for development — Set test: true to avoid consuming credits (output will be watermarked)
Set generous timeouts — Video generation often takes 5-15 minutes, sometimes longer
Validate inputs — Check avatar and voice IDs exist before generating
Weekly Installs
994
Repository
heygen-com/skills
GitHub Stars
202
First Seen
Mar 14, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
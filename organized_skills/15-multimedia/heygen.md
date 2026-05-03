---
rating: ⭐⭐
title: heygen
url: https://skills.sh/heygen-com/skills/heygen
---

# heygen

skills/heygen-com/skills/heygen
heygen
Installation
$ npx skills add https://github.com/heygen-com/skills --skill heygen
Summary

[DEPRECATED] Legacy avatar video generation API — use create-video or avatar-video skills instead.

Generates talking-head videos, explainers, and presentations from text prompts or detailed scripts with precise avatar, voice, and scene control
Provides MCP tools for prompt-based generation, video status polling, and account management; falls back to direct HTTP API calls if tools unavailable
Supports multi-scene videos with per-scene avatars, backgrounds, voices, and timing; captions, text overlays, and transparent WebM output for compositing
Requires HEYGEN_API_KEY environment variable for authentication
SKILL.md
HeyGen API (Deprecated)

This skill is deprecated. Use the focused skills instead:

create-video — Generate videos from a text prompt (Video Agent API)
avatar-video — Build videos with specific avatars, voices, scripts, and scenes (v2 API)

This skill remains for backward compatibility but will be removed in a future release.

AI avatar video creation API for generating talking-head videos, explainers, and presentations.

Tool Selection

If HeyGen MCP tools are available (mcp__heygen__*), prefer them over direct HTTP API calls — they handle authentication and request formatting automatically.

Task	MCP Tool	Fallback (Direct API)
Generate video from prompt	mcp__heygen__generate_video_agent	POST /v1/video_agent/generate
Check video status / get URL	mcp__heygen__get_video	GET /v2/videos/{video_id}
List account videos	mcp__heygen__list_videos	GET /v2/videos
Delete a video	mcp__heygen__delete_video	DELETE /v2/videos/{video_id}

If no HeyGen MCP tools are available, use direct HTTP API calls with X-Api-Key: $HEYGEN_API_KEY header as documented in the reference files.

Default Workflow

Prefer Video Agent for most video requests. Always use prompt-optimizer.md guidelines to structure prompts with scenes, timing, and visual styles.

With MCP tools:

Write an optimized prompt using prompt-optimizer.md → visual-styles.md
Call mcp__heygen__generate_video_agent with prompt and config (duration_sec, orientation, avatar_id)
Call mcp__heygen__get_video with the returned video_id to poll status and get the download URL

Without MCP tools (direct API):

Write an optimized prompt using prompt-optimizer.md → visual-styles.md
POST /v1/video_agent/generate — see video-agent.md
GET /v2/videos/<id> — see video-status.md

Only use v2/video/generate when user explicitly needs:

Exact script without AI modification
Specific voice_id selection
Different avatars/backgrounds per scene
Precise per-scene timing control
Programmatic/batch generation with exact specs
Quick Reference
Task	MCP Tool	Read
Generate video from prompt (easy)	mcp__heygen__generate_video_agent	prompt-optimizer.md → visual-styles.md → video-agent.md
Generate video with precise control	—	video-generation.md, avatars.md, voices.md
Check video status / get download URL	mcp__heygen__get_video	video-status.md
Add captions or text overlays	—	captions.md, text-overlays.md
Transparent video for compositing	—	video-generation.md (WebM section)
Use with Remotion	—	remotion-integration.md
Reference Files
Foundation
references/authentication.md - API key setup and X-Api-Key header
references/quota.md - Credit system and usage limits
references/video-status.md - Polling patterns and download URLs
references/assets.md - Uploading images, videos, audio
Core Video Creation
references/avatars.md - Listing avatars, styles, avatar_id selection
references/voices.md - Listing voices, locales, speed/pitch
references/scripts.md - Writing scripts, pauses, pacing
references/video-generation.md - POST /v2/video/generate and multi-scene videos
references/video-agent.md - One-shot prompt video generation
references/prompt-optimizer.md - Writing effective Video Agent prompts (core workflow + rules)
references/visual-styles.md - 20 named visual styles with full specs
references/prompt-examples.md - Full production prompt example + ready-to-use templates
references/dimensions.md - Resolution and aspect ratios
Video Customization
references/backgrounds.md - Solid colors, images, video backgrounds
references/text-overlays.md - Adding text with fonts and positioning
references/captions.md - Auto-generated captions and subtitles
Advanced Features
references/templates.md - Template listing and variable replacement
references/photo-avatars.md - Creating avatars from photos
references/webhooks.md - Webhook endpoints and events
Integration
references/remotion-integration.md - Using HeyGen in Remotion compositions
Weekly Installs
1.7K
Repository
heygen-com/skills
GitHub Stars
202
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
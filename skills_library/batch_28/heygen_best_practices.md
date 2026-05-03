---
title: heygen-best-practices
url: https://skills.sh/davila7/claude-code-templates/heygen-best-practices
---

# heygen-best-practices

skills/davila7/claude-code-templates/heygen-best-practices
heygen-best-practices
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill heygen-best-practices
SKILL.md
When to use

Use this skill whenever you are dealing with HeyGen API code to obtain domain-specific knowledge for creating AI avatar videos, managing avatars, handling video generation workflows, and integrating with HeyGen's services.

How to use

Read individual rule files for detailed explanations and code examples:

Foundation
rules/authentication.md - API key setup, X-Api-Key header, and authentication patterns
rules/quota.md - Credit system, usage limits, and checking remaining quota
rules/video-status.md - Polling patterns, status types, and retrieving download URLs
rules/assets.md - Uploading images, videos, and audio for use in video generation
Core Video Creation
rules/avatars.md - Listing avatars, avatar styles, and avatar_id selection
rules/voices.md - Listing voices, locales, speed/pitch configuration
rules/scripts.md - Writing scripts, pauses/breaks, pacing, and structure templates
rules/video-generation.md - POST /v2/video/generate workflow and multi-scene videos
rules/video-agent.md - One-shot prompt video generation with Video Agent API
rules/dimensions.md - Resolution options (720p/1080p) and aspect ratios
Video Customization
rules/backgrounds.md - Solid colors, images, and video backgrounds
rules/text-overlays.md - Adding text with fonts and positioning
rules/captions.md - Auto-generated captions and subtitle options
Advanced Features
rules/templates.md - Template listing and variable replacement
rules/video-translation.md - Translating videos, quality/fast modes, and dubbing
rules/streaming-avatars.md - Real-time interactive avatar sessions
rules/photo-avatars.md - Creating avatars from photos (talking photos)
rules/webhooks.md - Registering webhook endpoints and event types
Integration
rules/remotion-integration.md - Using HeyGen avatar videos in Remotion compositions
Weekly Installs
220
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
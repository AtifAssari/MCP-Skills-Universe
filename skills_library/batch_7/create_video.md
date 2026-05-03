---
title: create-video
url: https://skills.sh/heygen-com/skills/create-video
---

# create-video

skills/heygen-com/skills/create-video
create-video
Installation
$ npx skills add https://github.com/heygen-com/skills --skill create-video
SKILL.md
Create Video

Generate complete videos from a text prompt. Describe what you want and the AI handles script writing, avatar selection, visuals, voiceover, pacing, and captions automatically.

Authentication

All requests require the X-Api-Key header. Set the HEYGEN_API_KEY environment variable.

curl -X POST "https://api.heygen.com/v3/video-agents" \
  -H "X-Api-Key: $HEYGEN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Create a 60-second product demo video."}'

Tool Selection

If HeyGen MCP tools are available (mcp__heygen__*), prefer them over direct HTTP API calls — they handle authentication and request formatting automatically.

Task	MCP Tool	Fallback (Direct API)
Generate video from prompt	mcp__heygen__generate_video_agent	POST /v3/video-agents
Check video status / get URL	mcp__heygen__get_video	GET /v3/videos/{video_id}
List account videos	mcp__heygen__list_videos	GET /v3/videos
Delete a video	mcp__heygen__delete_video	DELETE /v3/videos/{video_id}

If no HeyGen MCP tools are available, use direct HTTP API calls as documented in the reference files.

Default Workflow

Always use prompt-optimizer.md guidelines to structure prompts with scenes, timing, and visual styles.

With MCP tools:

Write an optimized prompt using prompt-optimizer.md → visual-styles.md
Call mcp__heygen__generate_video_agent with prompt and config (duration_sec, orientation, avatar_id)
Call mcp__heygen__get_video with the returned video_id to poll status and get the download URL

Without MCP tools (direct API):

Write an optimized prompt using prompt-optimizer.md → visual-styles.md
POST /v3/video-agents — see video-agent.md
GET /v3/videos/<id> — see video-status.md
Reference Files

Read these as needed — they contain endpoint details, request/response schemas, and code examples (curl, TypeScript, Python).

Core workflow:

references/prompt-optimizer.md — Writing effective prompts (scenes, timing, visual styles)
references/visual-styles.md — 20 named visual styles with full specs
references/prompt-examples.md — Production prompt examples and templates
references/video-agent.md — POST /v3/video-agents request fields, response format, file inputs

Foundation:

references/video-status.md — GET /v3/videos/{id} polling and download
references/webhooks.md — Webhook endpoints and events
references/assets.md — Uploading images, videos, audio as references
references/dimensions.md — Resolution and aspect ratios
references/quota.md — Credit system and usage limits
Best Practices
Optimize your prompt — quality depends entirely on prompt structure. Always use the prompt optimizer
Lock avatar if needed — pass avatar_id for consistency across videos
Specify voice — pass voice_id for a specific narrator voice
Upload reference files — help the agent understand your brand/product
Iterate on prompts — refine based on results; Video Agent is great for quick iterations
Weekly Installs
945
Repository
heygen-com/skills
GitHub Stars
202
First Seen
Mar 14, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
---
title: google-veo
url: https://skills.sh/inference-sh/skills/google-veo
---

# google-veo

skills/inference-sh/skills/google-veo
google-veo
Installation
$ npx skills add https://github.com/inference-sh/skills --skill google-veo
SKILL.md
Google Veo Video Generation

Generate videos with Google Veo models via inference.sh CLI.

Quick Start

Requires inference.sh CLI (belt). Install instructions

belt login

belt app run google/veo-3-1-fast --input '{"prompt": "drone shot over a mountain lake"}'

Veo Models
Model	App ID	Speed	Quality
Veo 3.1	google/veo-3-1	Slower	Best
Veo 3.1 Fast	google/veo-3-1-fast	Fast	Excellent
Veo 3	google/veo-3	Medium	Excellent
Veo 3 Fast	google/veo-3-fast	Fast	Very Good
Veo 2	google/veo-2	Medium	Good
Search Veo Apps
belt app list --search "veo"

Examples
Cinematic Shot
belt app run google/veo-3-1-fast --input '{
  "prompt": "Cinematic drone shot flying through a misty forest at sunrise, volumetric lighting"
}'

Product Demo
belt app run google/veo-3 --input '{
  "prompt": "Sleek smartphone rotating on a dark reflective surface, studio lighting"
}'

Nature Scene
belt app run google/veo-3-1-fast --input '{
  "prompt": "Timelapse of clouds moving over a mountain range, golden hour"
}'

Action Shot
belt app run google/veo-3 --input '{
  "prompt": "Slow motion water droplet splashing into a pool, macro shot"
}'

Urban Scene
belt app run google/veo-3-1-fast --input '{
  "prompt": "Busy city street at night with neon signs and rain reflections, Tokyo style"
}'

Prompt Tips

Camera movements: drone shot, tracking shot, pan, zoom, dolly, steadicam

Lighting: golden hour, blue hour, studio lighting, volumetric, neon, natural

Style: cinematic, documentary, commercial, artistic, realistic

Timing: slow motion, timelapse, real-time

Sample Workflow
# 1. Generate sample input to see all options
belt app sample google/veo-3-1-fast --save input.json

# 2. Edit the prompt
# 3. Run
belt app run google/veo-3-1-fast --input input.json

Related Skills
# Full platform skill (all 250+ apps)
npx skills add inference-sh/skills@infsh-cli

# All video generation models
npx skills add inference-sh/skills@ai-video-generation

# AI avatars & lipsync
npx skills add inference-sh/skills@ai-avatar-video

# Image generation (for image-to-video)
npx skills add inference-sh/skills@ai-image-generation


Browse all video apps: belt app list --category video

Documentation
Running Apps - How to run apps via CLI
Streaming Results - Real-time progress updates
Content Pipeline Example - Building media workflows
Weekly Installs
294
Repository
inference-sh/skills
GitHub Stars
395
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass
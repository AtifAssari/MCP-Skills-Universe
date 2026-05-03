---
title: veo3-1
url: https://skills.sh/delneg/nano-banana-pro-skill-grsai-com/veo3-1
---

# veo3-1

skills/delneg/nano-banana-pro-skill-grsai-com/veo3-1
veo3-1
Installation
$ npx skills add https://github.com/delneg/nano-banana-pro-skill-grsai-com --skill veo3-1
SKILL.md
Veo 3.1 Video Generation
Usage

Run from the user's current working directory (do NOT cd into the skill directory):

uv run scripts/generate_video.py --prompt "description" --filename "output.mp4" [--model MODEL] [--duration 4|6|8] [--aspect-ratio 16:9|9:16] [--api-key KEY]


Use --url-only to skip the download and print just the video URL — useful for chaining with other tools:

uv run scripts/generate_video.py --prompt "description" --url-only [--model MODEL] [--duration 4|6|8]

Workflow (draft → final)
Draft — --model veo3.1-fast --duration 4 (cheapest, iterate on prompt)
Final — --model veo3.1-pro-4k --duration 8 (only when prompt is locked)
Model Options
Model	Quality	Resolution	Cost
veo3.1-fast (default)	Fast	720p	Lowest
veo3.1-fast-1080p	Fast	1080p	Low
veo3.1-fast-4k	Fast	4K	Medium
veo3.1-pro	Pro	720p	Medium
veo3.1-pro-1080p	Pro	1080p	High
veo3.1-pro-4k	Pro	4K	Highest

Map user requests:

No mention / "draft" / "fast" → veo3.1-fast
"1080p" / "HD" → veo3.1-fast-1080p
"4K" / "ultra" → veo3.1-fast-4k
"high quality" / "pro" → veo3.1-pro
"best quality" / "pro 4K" → veo3.1-pro-4k
Duration & Aspect Ratio
Duration: 4 (drafts), 6, 8 (default/finals) seconds
Aspect ratio: 16:9 (default, landscape), 9:16 (portrait/mobile)
API Key

Provide via --api-key argument or set GRSAI_API_KEY environment variable.

Troubleshooting
Symptom	Resolution
Error: No API key provided.	Set GRSAI_API_KEY env var or pass --api-key
HTTP 401	Wrong or expired API key
Generation failed:	Content moderation or invalid input; rephrase prompt
Timeout	Use a faster model (veo3.1-fast) or shorter duration (--duration 4)
uv: command not found	Install: curl -LsSf https://astral.sh/uv/install.sh | sh, then restart terminal

For transient errors (HTTP 429, network timeouts), retry once after 30 seconds. Do not retry more than twice — surface the issue to the user instead.

Filename Convention

Pattern: yyyy-mm-dd-hh-mm-ss-descriptive-name.mp4

2025-11-23-14-23-05-sunset-mountains.mp4
2025-11-23-15-30-12-dancing-robot-neon.mp4
Output

Always prints VIDEO_URL: <full_url> on its own line after generation — use this to extract the URL for chaining.

Without --url-only: saves the file to disk and prints Video saved: <path>. Report the saved path to the user. Do not open or read the video back.

With --url-only: prints only the generation info and VIDEO_URL: line — no download, no --filename required.

Chaining with qwen-3-5-plus-video-feedback

Extract the URL from stdout and pass it directly to the feedback skill:

VIDEO_URL=$(uv run veo3-1/scripts/generate_video.py --prompt "..." --url-only | grep '^VIDEO_URL:' | cut -d' ' -f2)
uv run qwen-3-5-plus-openrouter/scripts/analyze_video.py --video-url "$VIDEO_URL" --prompt "Does this video match the prompt? Rate quality 1-10."

Examples
uv run scripts/generate_video.py --prompt "A golden sunset over mountain peaks with birds flying" --filename "2025-11-23-14-23-05-sunset-draft.mp4" --model veo3.1-fast --duration 4

uv run scripts/generate_video.py --prompt "Close-up of waves crashing on rocky shore, slow motion, cinematic" --filename "2025-11-23-15-30-12-ocean-waves.mp4" --model veo3.1-pro-4k --duration 8 --aspect-ratio 16:9

Weekly Installs
30
Repository
delneg/nano-ban…rsai-com
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubFail
SocketFail
SnykFail
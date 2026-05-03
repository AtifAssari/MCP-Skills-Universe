---
rating: ⭐⭐
title: watch-youtube
url: https://skills.sh/mikeygonz/skills/watch-youtube
---

# watch-youtube

skills/mikeygonz/skills/watch-youtube
watch-youtube
Installation
$ npx skills add https://github.com/mikeygonz/skills --skill watch-youtube
SKILL.md
Watch YouTube

Use Google's Gemini API to actually watch YouTube videos and answer questions about them.

How It Works

Gemini processes both audio and visual streams of YouTube videos at 1 FPS. You pass a URL + prompt, it returns analysis.

When to Use
User shares a YouTube URL and wants a summary, transcript, or analysis
User asks "what did they say about X in this video?"
User wants timestamps of key moments
User wants to compare multiple videos (up to 10 per request with Gemini 2.5+)
When NOT to Use
Private or unlisted videos (only public videos work)
User just wants the video link or metadata
Setup

Requires GOOGLE_API_KEY environment variable. Get one free at https://aistudio.google.com/apikey

Usage

Run the script:

GOOGLE_API_KEY="$GOOGLE_API_KEY" python3 ~/.openclaw/workspace/skills/watch-youtube/watch.py "<youtube_url>" "<prompt>"

Examples

Summarize:

watch.py "https://www.youtube.com/watch?v=VIDEO_ID" "Summarize this video in 5 bullet points"


Timestamps:

watch.py "https://www.youtube.com/watch?v=VIDEO_ID" "List the key moments with timestamps"


Q&A:

watch.py "https://www.youtube.com/watch?v=VIDEO_ID" "What tools or products did they mention?"


Specific section:

watch.py "https://www.youtube.com/watch?v=VIDEO_ID" "What happens at 05:30?" 

Limits
Free tier: 8 hours of YouTube video per day
Paid tier: No limit
Max videos per request: 10 (Gemini 2.5+)
Max video length: ~1 hour (1M context), ~3 hours (low res)
~300 tokens per second of video
Models
gemini-2.5-flash — fast, cheap, good for most use cases
gemini-2.5-pro — deeper analysis, longer videos
gemini-3-flash-preview — latest, best quality
Fallback: Transcript Mode

If Gemini fails (quota exceeded, video too long, API key missing), the script automatically falls back to fetching the YouTube transcript via youtube_transcript_api.

What the fallback does:

Extracts the video ID from the URL
Fetches the auto-generated captions with timestamps
Returns the full transcript as text with your original prompt

What you get back: Raw timestamped transcript — the calling agent should read and answer the prompt from that text. Gemini-level visual/audio analysis is not available in fallback mode.

Limitations of fallback:

No visual analysis (can't describe what's on screen)
No answers about non-speech content
Requires the video to have auto-generated or manual captions
Private/unlisted videos without captions will fail entirely

When fallback triggers:

Gemini quota exceeded (429 / RESOURCE_EXHAUSTED)
Video exceeds context window (>1M tokens / ~1hr)
GOOGLE_API_KEY not set
Any other Gemini API error containing: quota, token, context, too long, exceeds
Weekly Installs
47
Repository
mikeygonz/skills
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
---
title: youtube-search
url: https://skills.sh/zeropointrepo/youtube-skills/youtube-search
---

# youtube-search

skills/zeropointrepo/youtube-skills/youtube-search
youtube-search
Installation
$ npx skills add https://github.com/zeropointrepo/youtube-skills --skill youtube-search
SKILL.md
YouTube Search

Search YouTube and fetch transcripts via TranscriptAPI.com.

Setup

If $TRANSCRIPT_API_KEY is not set, read references/auth-setup.md and follow the instructions there to get and store the key.

Required Headers

Every request needs two headers:

Authorization: Bearer $TRANSCRIPT_API_KEY
User-Agent: your agent's name and version if known (e.g. HermesAgent/0.11.0, ClaudeCode/1.0). Version is optional — agent name alone is fine. Do not omit this header or send a bare default — Cloudflare will return a 403 (error code 1010) and block the request.
API Reference

Full OpenAPI spec: transcriptapi.com/openapi.json — consult this for the latest parameters and schemas.

GET /api/v2/youtube/search — 1 credit

Search YouTube globally for videos or channels.

curl -s "https://transcriptapi.com/api/v2/youtube/search?q=QUERY&type=video&limit=20" \
  -H "Authorization: Bearer $TRANSCRIPT_API_KEY" \
  -H "User-Agent: YourAgent/1.0"

Param	Required	Default	Validation
q	yes	—	1-200 chars (trimmed)
type	no	video	video or channel
limit	no	20	1-50

Video search response:

{
  "results": [
    {
      "type": "video",
      "videoId": "dQw4w9WgXcQ",
      "title": "Rick Astley - Never Gonna Give You Up",
      "channelId": "UCuAXFkgsw1L7xaCfnd5JJOw",
      "channelTitle": "Rick Astley",
      "channelHandle": "@RickAstley",
      "channelVerified": true,
      "lengthText": "3:33",
      "viewCountText": "1.5B views",
      "publishedTimeText": "14 years ago",
      "hasCaptions": true,
      "thumbnails": [{ "url": "...", "width": 120, "height": 90 }]
    }
  ],
  "result_count": 20
}


Channel search response (type=channel):

{
  "results": [{
    "type": "channel",
    "channelId": "UCuAXFkgsw1L7xaCfnd5JJOw",
    "title": "Rick Astley",
    "handle": "@RickAstley",
    "url": "https://www.youtube.com/@RickAstley",
    "description": "Official channel...",
    "subscriberCount": "4.2M subscribers",
    "verified": true,
    "rssUrl": "https://www.youtube.com/feeds/videos.xml?channel_id=UC...",
    "thumbnails": [...]
  }],
  "result_count": 5
}

GET /api/v2/youtube/channel/search — 1 credit

Search videos within a specific channel. Accepts channel — an @handle, channel URL, or UC... ID.

curl -s "https://transcriptapi.com/api/v2/youtube/channel/search\
?channel=@TED&q=climate+change&limit=30" \
  -H "Authorization: Bearer $TRANSCRIPT_API_KEY" \
  -H "User-Agent: YourAgent/1.0"

Param	Required	Validation
channel	yes	@handle, channel URL, or UC... ID
q	yes	1-200 chars
limit	no	1-50 (default 30)

Returns up to ~30 results (YouTube limit). Same video response shape as global search.

GET /api/v2/youtube/channel/resolve — FREE

Convert @handle to channel ID:

curl -s "https://transcriptapi.com/api/v2/youtube/channel/resolve?input=@TED" \
  -H "Authorization: Bearer $TRANSCRIPT_API_KEY" \
  -H "User-Agent: YourAgent/1.0"

Workflow: Search → Transcript
# 1. Search for videos
curl -s "https://transcriptapi.com/api/v2/youtube/search\
?q=python+web+scraping&type=video&limit=5" \
  -H "Authorization: Bearer $TRANSCRIPT_API_KEY" \
  -H "User-Agent: YourAgent/1.0"

# 2. Get transcript from result
curl -s "https://transcriptapi.com/api/v2/youtube/transcript\
?video_url=VIDEO_ID&format=text&include_timestamp=true&send_metadata=true" \
  -H "Authorization: Bearer $TRANSCRIPT_API_KEY" \
  -H "User-Agent: YourAgent/1.0"

Errors
Code	Meaning	Action
401	Bad API key	Check key
402	No credits	transcriptapi.com/billing
403/1010	Cloudflare block	Add or fix User-Agent header
404	Not found	Resource doesn't exist
408	Timeout	Retry once
422	Invalid param	Check param format

Free tier: 100 credits, 300 req/min.

Weekly Installs
305
Repository
zeropointrepo/y…e-skills
GitHub Stars
123
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn
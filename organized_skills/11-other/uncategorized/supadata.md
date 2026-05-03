---
rating: ⭐⭐⭐
title: supadata
url: https://skills.sh/vm0-ai/vm0-skills/supadata
---

# supadata

skills/vm0-ai/vm0-skills/supadata
supadata
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill supadata
SKILL.md
Troubleshooting

If requests fail, run zero doctor check-connector --env-name SUPADATA_TOKEN or zero doctor check-connector --url https://api.supadata.ai/v1/transcript --method POST

How to Use

All examples below assume you have SUPADATA_TOKEN set.

The base URL for the API is:

https://api.supadata.ai/v1

Authentication uses the x-api-key header.

1. Get YouTube Video Transcript

Extract transcript from a YouTube video:

Write to /tmp/supadata_url.txt:

https://www.youtube.com/watch?v=dQw4w9WgXcQ

curl -s "https://api.supadata.ai/v1/transcript" -H "x-api-key: $SUPADATA_TOKEN" -G --data-urlencode "url@/tmp/supadata_url.txt" -d "text=true"


Parameters:

url: Video URL (required)
text: Return plain text (true) or timestamped chunks (false, default)
lang: Preferred language (ISO 639-1 code, e.g., en, zh)
mode: native (existing only), generate (AI), auto (default)
2. Get Transcript with Timestamps

Get transcript with timing information:

curl -s "https://api.supadata.ai/v1/transcript" -H "x-api-key: $SUPADATA_TOKEN" -G --data-urlencode "url@/tmp/supadata_url.txt" -d "text=false" | jq '.content[:3]'


Response format:

{
  "content": [
  {"text": "Hello", "offset": 0, "duration": 1500, "lang": "en"}
  ],
  "lang": "en",
  "availableLangs": ["en", "es", "zh"]
}

3. Get TikTok/Instagram/X Transcript

Extract transcript from other platforms:

# TikTok
curl -s "https://api.supadata.ai/v1/transcript" -H "x-api-key: $SUPADATA_TOKEN" -G --data-urlencode "url@/tmp/supadata_url.txt" -d "text=true"

# Instagram Reel
curl -s "https://api.supadata.ai/v1/transcript" -H "x-api-key: $SUPADATA_TOKEN" -G --data-urlencode "url@/tmp/supadata_url.txt" -d "text=true"


Supported platforms: YouTube, TikTok, Instagram, X (Twitter), Facebook

4. Native Transcript Only (Save Credits)

Fetch only existing transcripts without AI generation:

curl -s "https://api.supadata.ai/v1/transcript" -H "x-api-key: $SUPADATA_TOKEN" -G --data-urlencode "url@/tmp/supadata_url.txt" -d "text=true" -d "mode=native"


Use mode=native to avoid AI generation costs (1 credit vs 2 credits/min).

5. Get YouTube Channel Metadata

Get channel information:

curl -s "https://api.supadata.ai/v1/youtube/channel" -H "x-api-key: $SUPADATA_TOKEN" -G --data-urlencode "id=@mkbhd" | jq '{name, subscriberCount, videoCount}


Accepts channel URL, channel ID, or handle (e.g., @mkbhd).

6. Get YouTube Video Metadata

Get video information:

curl -s "https://api.supadata.ai/v1/youtube/video" -H "x-api-key: $SUPADATA_TOKEN" -G --data-urlencode "url@/tmp/supadata_url.txt" | jq '{title, viewCount, likeCount, duration}

7. Get Social Media Metadata

Get metadata from any supported platform:

curl -s "https://api.supadata.ai/v1/metadata" -H "x-api-key: $SUPADATA_TOKEN" -G --data-urlencode "url@/tmp/supadata_url.txt"


Works with YouTube, TikTok, Instagram, X, Facebook posts.

8. Scrape Web Page to Markdown

Extract web page content:

curl -s "https://api.supadata.ai/v1/web/scrape" -H "x-api-key: $SUPADATA_TOKEN" -G --data-urlencode "url@/tmp/supadata_url.txt"


Returns page content in Markdown format, ideal for AI processing.

9. Map Website Links

Get all links from a website:

curl -s "https://api.supadata.ai/v1/web/map" -H "x-api-key: $SUPADATA_TOKEN" -G --data-urlencode "url@/tmp/supadata_url.txt" | jq '.urls[:10]'

10. Crawl Website (Async)

Start a crawl job for multiple pages.

Write to /tmp/supadata_request.json:

{
  "url": "https://example.com",
  "maxPages": 10
}


Then run:

# Start crawl
JOB_ID="$(curl -s "https://api.supadata.ai/v1/web/crawl" -X POST -H "x-api-key: $SUPADATA_TOKEN" -H "Content-Type: application/json" -d @/tmp/supadata_request.json | jq -r '.jobId')"

echo "Job ID: ${JOB_ID}"

# Check status
curl -s "https://api.supadata.ai/v1/web/crawl/<your-job-id>" -H "x-api-key: $SUPADATA_TOKEN" | jq '{status, pagesCompleted}'


Status values: queued, active, completed, failed

11. Translate Transcript

Translate a YouTube transcript to another language:

curl -s "https://api.supadata.ai/v1/youtube/transcript/translate" -H "x-api-key: $SUPADATA_TOKEN" -G --data-urlencode "url@/tmp/supadata_url.txt" -d "lang=zh" -d "text=true"

Response Handling

Synchronous (HTTP 200): Direct result returned.

Asynchronous (HTTP 202): Returns jobId for polling:

{"jobId": "abc123"}


Poll the job endpoint until status is completed.

Guidelines
Use mode=native to save credits: Only fetches existing transcripts
URL encode parameters: Use --data-urlencode for URLs
Check available languages: Response includes availableLangs array
Handle async responses: Some requests return job IDs for polling
Max file size: 1GB for direct file URLs
Supported formats: MP4, WEBM, MP3, FLAC, MPEG, M4A, OGG, WAV
Weekly Installs
80
Repository
vm0-ai/vm0-skills
GitHub Stars
57
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
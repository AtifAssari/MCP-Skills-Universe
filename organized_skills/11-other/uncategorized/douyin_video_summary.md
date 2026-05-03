---
rating: ⭐⭐⭐
title: douyin-video-summary
url: https://skills.sh/liu-wei-ai/douyin-video-summary/douyin-video-summary
---

# douyin-video-summary

skills/liu-wei-ai/douyin-video-summary/douyin-video-summary
douyin-video-summary
Installation
$ npx skills add https://github.com/liu-wei-ai/douyin-video-summary --skill douyin-video-summary
Summary

Extract, transcribe, and summarize Douyin videos with local whisper.cpp processing.

Handles both short (v.douyin.com) and direct Douyin URLs by parsing video IDs and intercepting audio via browser JavaScript
Uses ffmpeg to convert audio to WAV and whisper.cpp for local Chinese transcription, with automatic Metal GPU acceleration on Apple Silicon
Generates structured summaries with core points, details, and one-line takeaways in markdown format
Optional Feishu (Lark) document sync to append summaries to collaborative docs via the Feishu Open API
SKILL.md
Douyin Video Summary

Summarize Douyin videos: extract audio → transcribe locally → AI summary.

Prerequisites

Install these tools (macOS example):

brew install whisper-cpp ffmpeg
# Download whisper.cpp GGML model (small recommended for speed/quality balance)
curl -L -o models/ggml-small.bin "https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-small.bin"

Workflow

When a Douyin link is received:

Step 1: Extract Video ID

Parse the Douyin URL to get the video ID. Douyin share links come in two formats:

Short link: https://v.douyin.com/xxxxx/ → follow redirect to get video ID
Direct link: https://www.douyin.com/video/7604713801732365681
# Follow redirect to get final URL, extract numeric video ID
curl -sL -o /dev/null -w '%{url_effective}' 'https://v.douyin.com/xxxxx/' | grep -oE '[0-9]{15,}'

Step 2: Get Audio via Browser

Douyin blocks direct downloads (yt-dlp, aria2c all get 403). Use the browser to intercept the audio URL:

Open the Douyin video page in the browser
Inject JS to intercept network requests before navigation:
window.__audioUrls = [];
const origOpen = XMLHttpRequest.prototype.open;
XMLHttpRequest.prototype.open = function(method, url) {
  if (url && (url.includes('.mp3') || url.includes('.m4a') || url.includes('mime_type=audio'))) {
    window.__audioUrls.push(url);
  }
  return origOpen.apply(this, arguments);
};

Navigate to the video page, click play to trigger audio loading
Retrieve intercepted URLs: window.__audioUrls
Download with curl (Referer header required):
curl -H "Referer: https://www.douyin.com/" -o audio.mp4 "<audio_url>"


Important: aria2c will 403 on Douyin CDN URLs. Always use curl with the Referer header.

Step 3: Convert to WAV
ffmpeg -i audio.mp4 -ar 16000 -ac 1 -c:a pcm_s16le audio.wav

Step 4: Transcribe with whisper.cpp
whisper-cli -m /path/to/ggml-small.bin -l zh -f audio.wav -otxt -of output

Use -l zh for Chinese content (auto-detect if unsure)
Apple Silicon GPU acceleration is automatic (Metal)
Performance: ~20s for 5min audio on M4
Step 5: Generate Summary

Read the transcription text and produce a structured summary:

📹 **[Video Title] | [Author]**
时长：X分X秒 | 发布：YYYY-MM-DD

🎯 **核心观点：[one-line core message]**

**1. [Point 1 title]**
• [detail]
• [detail]

**2. [Point 2 title]**
• [detail]

💬 **一句话总结：[concise takeaway]**

Step 6 (Optional): Sync to Feishu Doc

If Feishu integration is configured, append the summary to a Feishu document using the Feishu Open API. See references/feishu-sync.md for the API details.

Tips
For short videos (<1min), the summary may be very brief — that's fine
If browser interception fails, retry once; Douyin pages sometimes need a second load
Clean up downloaded audio/wav files after processing to save disk space
whisper.cpp small model is the best speed/quality tradeoff; medium may OOM on 8GB machines
Weekly Installs
1.0K
Repository
liu-wei-ai/douy…-summary
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn
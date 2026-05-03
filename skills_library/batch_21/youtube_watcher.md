---
title: youtube-watcher
url: https://skills.sh/hanzoskill/youtube-watcher/youtube-watcher
---

# youtube-watcher

skills/hanzoskill/youtube-watcher/youtube-watcher
youtube-watcher
Installation
$ npx skills add https://github.com/hanzoskill/youtube-watcher --skill youtube-watcher
SKILL.md
YouTube Watcher

Fetch transcripts from YouTube videos to enable summarization, QA, and content extraction.

Usage
Get Transcript

Retrieve the text transcript of a video.

python3 {baseDir}/scripts/get_transcript.py "https://www.youtube.com/watch?v=VIDEO_ID"

Examples

Summarize a video:

Get the transcript:
python3 {baseDir}/scripts/get_transcript.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

Read the output and summarize it for the user.

Find specific information:

Get the transcript.
Search the text for keywords or answer the user's question based on the content.
Notes
Requires yt-dlp to be installed and available in the PATH.
Works with videos that have closed captions (CC) or auto-generated subtitles.
If a video has no subtitles, the script will fail with an error message.
Weekly Installs
243
Repository
hanzoskill/yout…-watcher
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
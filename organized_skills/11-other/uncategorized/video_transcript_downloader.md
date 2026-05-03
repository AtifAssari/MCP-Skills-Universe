---
rating: ⭐⭐
title: video-transcript-downloader
url: https://skills.sh/steipete/agent-scripts/video-transcript-downloader
---

# video-transcript-downloader

skills/steipete/agent-scripts/video-transcript-downloader
video-transcript-downloader
Installation
$ npx skills add https://github.com/steipete/agent-scripts --skill video-transcript-downloader
SKILL.md
Video Transcript Downloader

./scripts/vtd.js can:

Print a transcript as a clean paragraph (timestamps optional).
Download video/audio/subtitles.

Transcript behavior:

YouTube: fetch via youtube-transcript-plus when possible.
Otherwise: pull subtitles via yt-dlp, then clean into a paragraph.
Setup
cd ~/Projects/agent-scripts/skills/video-transcript-downloader && npm ci

Transcript (default: clean paragraph)
./scripts/vtd.js transcript --url 'https://…'
./scripts/vtd.js transcript --url 'https://…' --lang en
./scripts/vtd.js transcript --url 'https://…' --timestamps
./scripts/vtd.js transcript --url 'https://…' --keep-brackets

Download video / audio / subtitles
./scripts/vtd.js download --url 'https://…' --output-dir ~/Downloads
./scripts/vtd.js audio --url 'https://…' --output-dir ~/Downloads
./scripts/vtd.js subs --url 'https://…' --output-dir ~/Downloads --lang en

Formats (list + choose)

List available formats (format ids, resolution, container, audio-only, etc):

./scripts/vtd.js formats --url 'https://…'


Download a specific format id (example):

./scripts/vtd.js download --url 'https://…' --output-dir ~/Downloads -- --format 137+140


Prefer MP4 container without re-encoding (remux when possible):

./scripts/vtd.js download --url 'https://…' --output-dir ~/Downloads -- --remux-video mp4

Notes
Default transcript output is a single paragraph. Use --timestamps only when asked.
Bracketed cues like [Music] are stripped by default; keep them via --keep-brackets.
Pass extra yt-dlp args after -- for transcript fallback, download, audio, subs, formats.
./scripts/vtd.js formats --url 'https://…' -- -v

Troubleshooting (only when needed)
Missing yt-dlp / ffmpeg:
brew install yt-dlp ffmpeg

Verify:
yt-dlp --version
ffmpeg -version | head -n 1

Weekly Installs
417
Repository
steipete/agent-scripts
GitHub Stars
2.5K
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
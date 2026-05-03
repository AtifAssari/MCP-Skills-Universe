---
title: video-download
url: https://skills.sh/heygen-com/skills/video-download
---

# video-download

skills/heygen-com/skills/video-download
video-download
Installation
$ npx skills add https://github.com/heygen-com/skills --skill video-download
SKILL.md
video-download

Download video and audio from URLs using yt-dlp directly. No wrapper scripts needed.

Prerequisites
yt-dlp: brew install yt-dlp or pip install yt-dlp
ffmpeg: brew install ffmpeg or apt install ffmpeg (required for merging video+audio streams)

Update yt-dlp periodically to keep up with site changes: yt-dlp -U or pip install -U yt-dlp.

Commands
Download best quality
yt-dlp "URL" -o "%(title)s.%(ext)s" --merge-output-format mp4

Download specific resolution
# 720p
yt-dlp "URL" -f "bestvideo[height<=720]+bestaudio/best[height<=720]" --merge-output-format mp4

# 1080p
yt-dlp "URL" -f "bestvideo[height<=1080]+bestaudio/best[height<=1080]" --merge-output-format mp4

Audio only
yt-dlp "URL" -x --audio-format mp3 --audio-quality 0

Download subtitles
# Download video with English subtitles
yt-dlp "URL" --write-subs --sub-langs en --merge-output-format mp4

# Download video with multiple subtitle languages
yt-dlp "URL" --write-subs --sub-langs "en,es,fr" --merge-output-format mp4

# Download only subtitles (no video)
yt-dlp "URL" --write-subs --sub-langs en --skip-download

Get metadata (no download)
yt-dlp "URL" --dump-json --no-download

List available formats
yt-dlp "URL" -F

Specify output directory
yt-dlp "URL" -o "./downloads/%(title)s.%(ext)s" --merge-output-format mp4

Quality Presets
Quality	Format flag
Best	-f "bestvideo+bestaudio/best" (default)
1080p	-f "bestvideo[height<=1080]+bestaudio/best[height<=1080]"
720p	-f "bestvideo[height<=720]+bestaudio/best[height<=720]"
480p	-f "bestvideo[height<=480]+bestaudio/best[height<=480]"
Worst	-f "worstvideo+worstaudio/worst"
Output Template Variables

Common variables for -o templates:

Variable	Description
%(title)s	Video title
%(ext)s	File extension
%(id)s	Video ID
%(uploader)s	Channel/uploader name
%(upload_date)s	Upload date (YYYYMMDD)
%(duration)s	Duration in seconds
%(resolution)s	Video resolution
Tips
Always use --merge-output-format mp4 to avoid ending up with .webm or .mkv files.
Use --no-download with --dump-json for metadata-only queries -- no files written to disk.
If a download fails with HTTP errors, update yt-dlp first (yt-dlp -U).
Use -f "bestvideo[height<=720]+bestaudio" to save bandwidth when full resolution is not needed.
yt-dlp automatically handles rate limiting and retries.
The --dump-json output includes title, duration, uploader, view_count, description, formats, subtitles, and much more.
Troubleshooting
"yt-dlp: command not found": Install it (pip install yt-dlp) and ensure your PATH includes pip's bin directory.
"ffmpeg: command not found": Install ffmpeg. Without it, downloads fail when video and audio are separate streams (common on YouTube for HD).
Downloads fail or return errors: Run yt-dlp -U to update. Sites change frequently and yt-dlp ships fixes regularly.
Weekly Installs
931
Repository
heygen-com/skills
GitHub Stars
202
First Seen
Mar 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
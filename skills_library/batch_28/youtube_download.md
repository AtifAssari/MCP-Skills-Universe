---
title: youtube-download
url: https://skills.sh/maxgent-ai/maxgent-plugin/youtube-download
---

# youtube-download

skills/maxgent-ai/maxgent-plugin/youtube-download
youtube-download
Installation
$ npx skills add https://github.com/maxgent-ai/maxgent-plugin --skill youtube-download
SKILL.md
YouTube Downloader

Download YouTube videos, audio, or subtitles using yt-dlp, with Chrome cookies for authenticated content.

Prerequisites

Uses uvx to run yt-dlp — no manual installation required.

Usage

When the user wants to download from YouTube: $ARGUMENTS

Instructions

Important: All yt-dlp commands use uvx yt-dlp. uvx handles installation and environment isolation automatically.

Step 1: Get video URL

If the user has not provided a video URL, ask them to provide one.

Supported sites include but are not limited to:

YouTube (youtube.com, youtu.be)
Bilibili (bilibili.com)
Twitter/X (twitter.com, x.com)
And other sites supported by yt-dlp
Step 2: Parse video info

Fetch video info with yt-dlp using Chrome cookies:

uvx yt-dlp --cookies-from-browser chrome -j "$VIDEO_URL" 2>/dev/null


Extract key info from the JSON output:

title: video title
duration: duration (seconds)
formats: available format list
subtitles: available subtitles
automatic_captions: auto-generated captions

Show the user:

Video title
Duration
Available video qualities (e.g. 1080p, 720p, 480p)
Available audio formats
Available subtitle languages

If parsing fails, it may require login or the video is unavailable — inform the user of the specific reason.

Step 3: Ask user for download options

Warning: You MUST use AskUserQuestion to collect user preferences. Do not skip this step.

Use AskUserQuestion to collect the following:

Download content: What do you want to download?

Options:
"Video + Audio - Complete video file (Recommended)"
"Audio only - MP3/M4A format"
"Subtitles only - SRT/VTT format"
"Video + Audio + Subtitles - Download all"

Video quality (if downloading video): Choose video quality

Options:
"Best quality (Recommended)"
"1080p - Full HD"
"720p - HD"
"480p - SD (save space)"
"Lowest quality (smallest file)"

Audio format (if downloading audio only): Choose audio format

Options:
"MP3 - Universal format (Recommended)"
"M4A - High quality"
"Best quality (keep original format)"

Subtitle language (if subtitles available): Choose subtitle language

Dynamically generate options based on parsed results
Common options: Chinese, English, Japanese, auto-generated captions

Output path: Where to save?

Default: current directory
Allow custom path
Step 4: Build yt-dlp command

Build the yt-dlp command based on user choices:

Base options (always used)
--cookies-from-browser chrome  # Use Chrome cookies
-o "%(title)s.%(ext)s"         # Output filename format
--no-playlist                   # Don't download playlists

Video + Audio download
# Best quality
uvx yt-dlp --cookies-from-browser chrome -f "bestvideo+bestaudio/best" --merge-output-format mp4 -o "OUTPUT_PATH/%(title)s.%(ext)s" "URL"

# Specific resolution
uvx yt-dlp --cookies-from-browser chrome -f "bestvideo[height<=1080]+bestaudio/best[height<=1080]" --merge-output-format mp4 -o "OUTPUT_PATH/%(title)s.%(ext)s" "URL"

# 720p
uvx yt-dlp --cookies-from-browser chrome -f "bestvideo[height<=720]+bestaudio/best[height<=720]" --merge-output-format mp4 -o "OUTPUT_PATH/%(title)s.%(ext)s" "URL"

Audio only download
# MP3 format
uvx yt-dlp --cookies-from-browser chrome -x --audio-format mp3 --audio-quality 0 -o "OUTPUT_PATH/%(title)s.%(ext)s" "URL"

# M4A format
uvx yt-dlp --cookies-from-browser chrome -x --audio-format m4a --audio-quality 0 -o "OUTPUT_PATH/%(title)s.%(ext)s" "URL"

# Best quality (original format)
uvx yt-dlp --cookies-from-browser chrome -x --audio-quality 0 -o "OUTPUT_PATH/%(title)s.%(ext)s" "URL"

Subtitles only download
# Download all subtitles
uvx yt-dlp --cookies-from-browser chrome --write-subs --skip-download -o "OUTPUT_PATH/%(title)s.%(ext)s" "URL"

# Download specific language subtitles
uvx yt-dlp --cookies-from-browser chrome --write-subs --sub-langs "zh,en" --skip-download -o "OUTPUT_PATH/%(title)s.%(ext)s" "URL"

# Download auto-generated captions
uvx yt-dlp --cookies-from-browser chrome --write-auto-subs --sub-langs "zh,en" --skip-download -o "OUTPUT_PATH/%(title)s.%(ext)s" "URL"

# Convert to SRT format
uvx yt-dlp --cookies-from-browser chrome --write-subs --sub-format srt --convert-subs srt --skip-download -o "OUTPUT_PATH/%(title)s.%(ext)s" "URL"

Video + Subtitles together
uvx yt-dlp --cookies-from-browser chrome -f "bestvideo+bestaudio/best" --merge-output-format mp4 --write-subs --sub-langs "zh,en" --embed-subs -o "OUTPUT_PATH/%(title)s.%(ext)s" "URL"

Step 5: Execute download
Show the full yt-dlp command to the user before execution
Run the command and show download progress
Report success or failure
Step 6: Verify output

After download completes:

ls -la "OUTPUT_PATH"


Report:

Downloaded filename and size
List subtitle files if downloaded
Any warnings or issues
Troubleshooting

Login-required content:

Ensure the user is logged in to the site in Chrome
If still failing, suggest manually exporting cookies

Region-restricted:

Inform the user they may need a proxy
Try --geo-bypass to bypass restrictions

Download failure:

Check if the URL is correct
Try updating yt-dlp: uvx --refresh yt-dlp --version
Check network connectivity
Weekly Installs
9
Repository
maxgent-ai/maxg…t-plugin
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn
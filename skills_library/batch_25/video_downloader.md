---
title: video-downloader
url: https://skills.sh/qiaoshouqing/skills/video-downloader
---

# video-downloader

skills/qiaoshouqing/skills/video-downloader
video-downloader
Installation
$ npx skills add https://github.com/qiaoshouqing/skills --skill video-downloader
SKILL.md
Video Downloader - Download Videos with yt-dlp

Download videos, audio, or subtitles from YouTube, Bilibili, Twitter, and 1000+ other sites using yt-dlp.

When to Use
User asks to download a video
User asks to download or extract audio
User asks to download subtitles
User provides a video URL (YouTube, Bilibili, Twitter, etc.)
User wants to specify video quality (720p, 1080p, etc.)
Prerequisites - Auto Install

IMPORTANT: Before any download, check and install dependencies automatically.

Step 0: Check and Install Dependencies
# Check if yt-dlp is installed, install if missing
if ! command -v yt-dlp &>/dev/null; then
  echo "Installing yt-dlp..."
  brew install yt-dlp
fi

# Check if ffmpeg is installed, install if missing
if ! command -v ffmpeg &>/dev/null; then
  echo "Installing ffmpeg..."
  brew install ffmpeg
fi

# Verify installation
yt-dlp --version && echo "yt-dlp: ready"
ffmpeg -version 2>&1 | head -1 && echo "ffmpeg: ready"


Run this check every time before downloading. Install automatically without asking user.

Instructions for Agent
Step 1: Ensure Dependencies Installed

Run the prerequisite check above. If yt-dlp or ffmpeg is missing, install via brew install yt-dlp ffmpeg.

Step 2: Parse User Intent

Identify what the user wants:

User Intent	Keywords
Video (default)	"download", "video"
Audio only	"audio", "mp3", "music", "extract audio"
Video + Subtitles	"with subtitles", "embed subtitles"
Subtitles only	"only subtitles", "subtitles only", "just subtitles"
Specific quality	"720p", "1080p", "4k", "best", "worst"
Step 3: Build Command

Base command structure:

yt-dlp [OPTIONS] "URL"


Common options by intent:

Basic video download (best quality):
yt-dlp -o "%(title)s.%(ext)s" "URL"

Audio only (MP3):
yt-dlp -x --audio-format mp3 -o "%(title)s.%(ext)s" "URL"

Specific quality (e.g., 720p):
yt-dlp -f "bestvideo[height<=720]+bestaudio/best[height<=720]" -o "%(title)s.%(ext)s" "URL"

Video with embedded subtitles:
yt-dlp --write-subs --sub-lang en,zh-Hans,zh-Hant --embed-subs -o "%(title)s.%(ext)s" "URL"

Subtitles only (no video):
yt-dlp --write-subs --write-auto-subs --sub-lang en,zh-Hans,zh-Hant --skip-download -o "%(title)s" "URL"

Step 4: Execute and Report

Run the command and report:

File name and location
File size (if available)
Any warnings or errors
Command Reference
Task	Command
Best quality video	yt-dlp "URL"
Audio (MP3)	yt-dlp -x --audio-format mp3 "URL"
Audio (M4A)	yt-dlp -x --audio-format m4a "URL"
720p video	yt-dlp -f "bv[height<=720]+ba/b[height<=720]" "URL"
1080p video	yt-dlp -f "bv[height<=1080]+ba/b[height<=1080]" "URL"
4K video	yt-dlp -f "bv[height<=2160]+ba/b[height<=2160]" "URL"
With subtitles	yt-dlp --write-subs --embed-subs "URL"
Subtitles only	yt-dlp --write-subs --write-auto-subs --skip-download "URL"
List formats	yt-dlp -F "URL"
Playlist	yt-dlp -o "%(playlist_index)s-%(title)s.%(ext)s" "PLAYLIST_URL"
Response Guidelines
Always confirm what will be downloaded before starting
Show download progress or final result
Report the output file name and location
If download fails, explain the error and suggest solutions
Error Handling
Error	Solution
yt-dlp: command not found	Auto-install: brew install yt-dlp
ffmpeg not found	Auto-install: brew install ffmpeg
Video unavailable	Check if URL is correct or video is region-locked
Private video	Cannot download private videos without authentication
Format not available	Use yt-dlp -F URL to list available formats
No subtitles found	Try --write-auto-subs for auto-generated subtitles
brew: command not found	Install Homebrew first: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
Weekly Installs
10
Repository
qiaoshouqing/skills
GitHub Stars
1
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn
---
title: yt-dlp
url: https://skills.sh/knoopx/pi/yt-dlp
---

# yt-dlp

skills/knoopx/pi/yt-dlp
yt-dlp
Installation
$ npx skills add https://github.com/knoopx/pi --skill yt-dlp
SKILL.md
yt-dlp Cheatsheet

Command-line tool for downloading videos from YouTube and other sites.

Quick Start
# Download video
yt-dlp https://url

# Download with specific format
yt-dlp -f best https://url

# Download with output filename
yt-dlp -o "filename.%(ext)s" https://url

Basic Download
# Download video
yt-dlp https://url

# Download to current directory
yt-dlp https://url

# Download with specific format
yt-dlp -f best https://url

Format Selection
# Best quality
yt-dlp -f best https://url

# Best audio
yt-dlp -f bestaudio https://url

# Best video
yt-dlp -f bestvideo https://url

# Specific format
yt-dlp -f 137 https://url

# Format list
yt-dlp --list-formats https://url

# Format with preference
yt-dlp -f "bestvideo[ext=mp4]+bestaudio/best" https://url

Output Options
# Custom output filename
yt-dlp -o "Title.%(ext)s" https://url

# Output template
yt-dlp -o "%(title)s.%(ext)s" https://url

# Keep original filename
yt-dlp --keep-filename https://url

# Skip existing files
yt-dlp --continue https://url

# Limit download rate
yt-dlp --limit 1M https://url

# Retries
yt-dlp --retries 5 https://url

Playlist Handling
# Download single video
yt-dlp https://url

# Download entire playlist
yt-dlp --yes-playlist https://url

# Download only certain videos
yt-dlp --playlist-end 10 https://url

# Download with start number
yt-dlp --playlist-start 5 https://url

# Download all except certain videos
yt-dlp --ignore-errors https://url

Authentication
# Username and password
yt-dlp -u user -p pass https://url

# API key
yt-dlp --cookies cookies.txt https://url

# Netflix username/password
yt-dlp --username user --password pass https://url

Metadata Extraction
# Extract info
yt-dlp --dump-json https://url

# Extract title
yt-dlp --get-title https://url

# Extract duration
yt-dlp --get-duration https://url

# Extract description
yt-dlp --get-description https://url

# Extract uploader
yt-dlp --get-uploader https://url

Advanced Options
# Download subtitles
yt-dlp --write-sub https://url

# Download all formats
yt-dlp --all-formats https://url

# Download best quality only
yt-dlp --no-playlist https://url

# Skip download, only extract info
yt-dlp --skip-download https://url

# Download to specific directory
yt-dlp -o "downloads/%(title)s.%(ext)s" https://url

# Concurrent downloads
yt-dlp --concurrent-connections 10 https://url

Batch Processing
# Download from file
yt-dlp --batch-file urls.txt

# Download all in directory
yt-dlp --download-archive archive.txt https://url

Tips
Use -f best for maximum quality
Use -o "filename.%(ext)s" for custom naming
Use --continue to skip already downloaded files
Use --list-formats to see available formats
Use --skip-download to extract metadata without downloading
Use --download-archive to avoid re-downloading
Related Skills
tmux: Run yt-dlp in background with watch mode
Weekly Installs
42
Repository
knoopx/pi
GitHub Stars
45
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail
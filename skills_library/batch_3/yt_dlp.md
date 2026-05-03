---
title: yt-dlp
url: https://skills.sh/lwmxiaobei/yt-dlp-skill/yt-dlp
---

# yt-dlp

skills/lwmxiaobei/yt-dlp-skill/yt-dlp
yt-dlp
Installation
$ npx skills add https://github.com/lwmxiaobei/yt-dlp-skill --skill yt-dlp
Summary

Download videos and extract audio from 900+ platforms including YouTube, Twitter, TikTok, and Instagram.

Supports three core operations: video download with quality selection (best, 1080p, 720p, 480p), audio extraction in multiple formats (MP3, M4A, OPUS, FLAC, WAV), and URL detection from conversation text
Auto-detects video links in conversations and prompts user to download; handles single and multiple URLs with playlist support
Includes three Python scripts: download_video.py for video retrieval with format options, extract_audio.py for audio conversion, and extract_urls.py for URL extraction from text or stdin
Requires yt-dlp and ffmpeg; all scripts use only built-in Python modules with no additional dependencies
SKILL.md
yt-dlp Video Downloader Skill

This skill provides tools for downloading videos and extracting audio from various platforms using yt-dlp.

Features
Download videos from multiple platforms (YouTube, Twitter/X, Vimeo, TikTok, Instagram, Facebook, etc.)
Extract audio from videos
Auto-detect video URLs in conversations
Support for different quality settings and formats
Usage Patterns
1. Command-based Download

When user explicitly asks to download a video:

User: Download this video https://youtube.com/watch?v=...


Action: Extract URL and call download script

2. Auto-detection in Conversations

When conversation contains video URLs:

User: Check out this video https://twitter.com/... and let me know what you think


Action: Detect video URL, ask user if they want to download it

3. Audio Extraction

When user wants to extract audio only:

User: Extract the audio from https://youtu.be/...


Action: Use audio extraction script

Available Scripts

Note: Scripts are located in the scripts/ directory

download_video.py

Main video downloader with quality and format options.

Usage:

# Download video
scripts/download_video.py <url> -o <output_dir>

# Download with specific quality
scripts/download_video.py <url> --quality 720p
scripts/download_video.py <url> --quality audio  # For audio only

# Custom format selector
scripts/download_video.py <url> --format "bestvideo[height<=1080]+bestaudio/best"

# Extract info only
scripts/download_video.py <url> --info-only


Quality options: best, 1080p, 720p, 480p, audio

extract_audio.py

Extract audio from videos in various formats.

Usage:

# Extract as MP3 (default)
/scripts/extract_audio.py <url> -o <output_dir>

# Extract as M4A
/scripts/extract_audio.py <url> --format m4a

# Custom quality
/scripts/extract_audio.py <url> --quality 320


Formats: mp3, m4a, opus, flac, wav

extract_urls.py

Extract video URLs from text or files.

Usage:

# Extract from text argument
/scripts/extract_urls.py "Check https://youtube.com/watch?v=..."

# Extract from file
/scripts/extract_urls.py <file_path>

# Read from stdin
cat file.txt | /scripts/extract_urls.py

Video Platform Support

The skill recognizes URLs from:

YouTube (youtube.com, youtu.be)
Twitter/X (twitter.com, x.com)
Vimeo (vimeo.com)
TikTok (tiktok.com)
Instagram (instagram.com)
Facebook (facebook.com, fb.watch)
Twitch (twitch.tv, clips.twitch.tv)
Dailymotion (dailymotion.com)
Reddit (reddit.com)
Streamable (streamable.com)
And many more supported by yt-dlp
Workflow
When User Provides Video URL
Extract URL from user's input using extract_urls.py
Confirm with user what action to take:
Download video
Extract audio
Show video info
Execute appropriate script based on user's choice
Notify user of success/failure and file location
When Auto-detecting URLs
Scan conversation text with extract_urls.py (can process stdin)
If video URLs found, ask user: "I found video URLs in this conversation. Would you like me to download them?"
If yes, proceed with download workflow
If no, continue with conversation
Handling Multiple URLs
For single URL: Direct download
For multiple URLs: Ask user if they want to download all or select specific ones
Provide option to download as playlist if URLs are from the same source
Quality and Format Selection

When user doesn't specify preferences:

Default to best available quality
For audio: Default to MP3 at 192kbps

When options needed:

# Ask user for quality preference if not specified
# Options: best (default), 1080p, 720p, 480p, audio

# Ask for format if extracting audio
# Options: mp3 (default), m4a, opus, flac, wav

Error Handling

Common issues and solutions:

yt-dlp not installed:

Check with yt-dlp --version
Install with pip install yt-dlp or brew install yt-dlp

ffmpeg not installed (required for format conversion):

Install with brew install ffmpeg (macOS)
Or apt install ffmpeg (Linux)

Video not available:

Check if URL is accessible
Some videos may require authentication
Age-restricted content may need cookies

Network errors:

Retry download
Check internet connection
Dependencies
yt-dlp: Main video downloader
ffmpeg: Audio/video processing (required for format conversion)
python3 with standard library

All scripts are self-contained and use only built-in Python modules.

Weekly Installs
801
Repository
lwmxiaobei/yt-dlp-skill
GitHub Stars
4
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
---
rating: ⭐⭐
title: youtube-downloader
url: https://skills.sh/composiohq/awesome-claude-skills/youtube-downloader
---

# youtube-downloader

skills/composiohq/awesome-claude-skills/youtube-downloader
youtube-downloader
Installation
$ npx skills add https://github.com/composiohq/awesome-claude-skills --skill youtube-downloader
Summary

Download YouTube videos in customizable quality and format with audio-only MP3 support.

Supports six quality presets (best, 1080p, 720p, 480p, 360p, worst) and three video formats (MP4, WebM, Matroska)
Audio-only downloads extract video as MP3 files for music or podcast extraction
Automatically installs and uses yt-dlp for robust stream selection and merging
Configurable output directory; defaults to /mnt/user-data/outputs/ with auto-generated filenames from video titles
SKILL.md
YouTube Video Downloader

Download YouTube videos with full control over quality and format settings.

Quick Start

The simplest way to download a video:

python scripts/download_video.py "https://www.youtube.com/watch?v=VIDEO_ID"


This downloads the video in best available quality as MP4 to /mnt/user-data/outputs/.

Options
Quality Settings

Use -q or --quality to specify video quality:

best (default): Highest quality available
1080p: Full HD
720p: HD
480p: Standard definition
360p: Lower quality
worst: Lowest quality available

Example:

python scripts/download_video.py "URL" -q 720p

Format Options

Use -f or --format to specify output format (video downloads only):

mp4 (default): Most compatible
webm: Modern format
mkv: Matroska container

Example:

python scripts/download_video.py "URL" -f webm

Audio Only

Use -a or --audio-only to download only audio as MP3:

python scripts/download_video.py "URL" -a

Custom Output Directory

Use -o or --output to specify a different output directory:

python scripts/download_video.py "URL" -o /path/to/directory

Complete Examples
Download video in 1080p as MP4:
python scripts/download_video.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -q 1080p

Download audio only as MP3:
python scripts/download_video.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -a

Download in 720p as WebM to custom directory:
python scripts/download_video.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -q 720p -f webm -o /custom/path

How It Works

The skill uses yt-dlp, a robust YouTube downloader that:

Automatically installs itself if not present
Fetches video information before downloading
Selects the best available streams matching your criteria
Merges video and audio streams when needed
Supports a wide range of YouTube video formats
Important Notes
Downloads are saved to /mnt/user-data/outputs/ by default
Video filename is automatically generated from the video title
The script handles installation of yt-dlp automatically
Only single videos are downloaded (playlists are skipped by default)
Higher quality videos may take longer to download and use more disk space
Weekly Installs
2.7K
Repository
composiohq/awes…e-skills
GitHub Stars
57.5K
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn
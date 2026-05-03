---
rating: ⭐⭐⭐
title: youtube-publisher
url: https://skills.sh/wlzh/skills/youtube-publisher
---

# youtube-publisher

skills/wlzh/skills/youtube-publisher
youtube-publisher
Installation
$ npx skills add https://github.com/wlzh/skills --skill youtube-publisher
SKILL.md
YouTube Publisher

First time? If setup_complete: false above, run ./SETUP.md first, then set setup_complete: true.

Upload videos to YouTube with full metadata control.

Metadata sanitization
> in title/description is automatically rewritten to 》
< in title/description is automatically rewritten to 《
Use this when YouTube rejects metadata because of special characters
Quick Start
cd ~/.claude/skills/youtube-publisher/scripts

# First time: authenticate
npx ts-node youtube-upload.ts --auth

# Upload video
npx ts-node youtube-upload.ts \
  --video /path/to/video.mp4 \
  --title "My Awesome Video" \
  --description "Check out this amazing content!" \
  --tags "tech,ai,tutorial" \
  --privacy unlisted

# Upload as YouTube Short (vertical video)
npx ts-node youtube-upload.ts \
  --video /path/to/short.mp4 \
  --title "Quick Tip #Shorts" \
  --description "A quick tip for you!" \
  --privacy public \
  --short

Options
Option	Short	Description
--video	-v	Video file path (required)
--title	-t	Video title (required)
--description	-d	Video description
--tags		Comma-separated tags
--privacy	-p	Privacy: public, unlisted, private (default: unlisted)
--category	-c	Category ID (default: 22 = People & Blogs)
--thumbnail		Custom thumbnail image (local path or URL)
--subtitles		Subtitle file path (SRT/VTT)
--subtitle-lang		Subtitle language code (default: zh)
--subtitle-name		Subtitle display name (default: 中文)
--playlist		Add to playlist ID
--short		Mark as YouTube Short
--auth		Run OAuth2 authentication flow
--dry-run		Preview without uploading
Category IDs
ID	Category
1	Film & Animation
2	Autos & Vehicles
10	Music
15	Pets & Animals
17	Sports
19	Travel & Events
20	Gaming
22	People & Blogs
23	Comedy
24	Entertainment
25	News & Politics
26	Howto & Style
27	Education
28	Science & Technology
Authentication

First-time setup requires OAuth2 authentication:

Run npx ts-node youtube-upload.ts --auth
Browser opens Google login
Grant permissions to upload videos
Token is saved to .youtube-token.json

Token refreshes automatically. Re-run --auth if expired.

Environment

Create scripts/.env:

YOUTUBE_CLIENT_ID=your_client_id
YOUTUBE_CLIENT_SECRET=your_client_secret


Get credentials from Google Cloud Console:

Create project at console.cloud.google.com
Enable YouTube Data API v3
Create OAuth2 credentials (Desktop app)
Download and extract client_id & client_secret
Examples
Upload Tutorial Video
npx ts-node youtube-upload.ts \
  -v tutorial.mp4 \
  -t "How to Use Claude Code - Complete Guide" \
  -d "Learn everything about Claude Code in this comprehensive tutorial.

Timestamps:
00:00 Introduction
02:30 Getting Started
05:00 Advanced Features

#ClaudeCode #AI #Tutorial" \
  --tags "claude code,ai,tutorial,anthropic,coding" \
  --category 28 \
  --privacy public

Upload YouTube Short
npx ts-node youtube-upload.ts \
  -v short_video.mp4 \
  -t "Mind-blowing AI trick! #Shorts" \
  -d "This will change how you work! #AI #Tech" \
  --privacy public \
  --short

Upload to Playlist
npx ts-node youtube-upload.ts \
  -v episode5.mp4 \
  -t "Podcast Episode 5" \
  --playlist PLxxxxxxxxxxxxxx \
  --privacy unlisted

Upload with Thumbnail and Subtitles
npx ts-node youtube-upload.ts \
  -v tutorial.mp4 \
  -t "Tutorial with Subtitles" \
  -d "Learn step by step with subtitles" \
  --thumbnail /path/to/cover.jpg \
  --subtitles /path/to/subtitles.srt \
  --subtitle-lang zh \
  --subtitle-name "中文" \
  --privacy public

Upload with Local Thumbnail
npx ts-node youtube-upload.ts \
  -v video.mp4 \
  -t "My Video Title" \
  --thumbnail "/Users/m/Downloads/shell/work/cover.jpg" \
  --privacy public

Output

On success, returns:

Video ID
Video URL (https://youtu.be/VIDEO_ID)
Status
Limitations
Max file size: 256GB (YouTube limit)
Supported formats: MP4, MOV, AVI, WMV, FLV, 3GP, MPEG
Supported subtitle formats: SRT, VTT
Daily upload quota: 10,000 units (typically ~6 videos/day)
Title max: 100 characters
Description max: 5,000 characters
Tags max: 500 characters total
Changelog
v1.1 - Resumable Upload + Retry (2026-04-22)
Fixed EPIPE error on large file uploads by switching to resumable upload with progress tracking
Added automatic retry (up to 3 attempts) for transient network errors (EPIPE, ETIMEDOUT, ECONNRESET)
Added upload progress logging (every 10%)
Added media.mimeType for better upload compatibility
v1.0 - Initial Release
Basic video upload with metadata
Thumbnail, subtitle, playlist support
OAuth2 authentication
Weekly Installs
34
Repository
wlzh/skills
GitHub Stars
518
First Seen
Feb 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
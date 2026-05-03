---
rating: ⭐⭐⭐
title: youtube-uploader
url: https://skills.sh/aviz85/claude-skills-library/youtube-uploader
---

# youtube-uploader

skills/aviz85/claude-skills-library/youtube-uploader
youtube-uploader
Installation
$ npx skills add https://github.com/aviz85/claude-skills-library --skill youtube-uploader
SKILL.md
YouTube Uploader

First time? If setup_complete: false above, run ./SETUP.md first, then set setup_complete: true.

Upload videos to YouTube with full metadata control.

Quick Start
cd ~/.claude/skills/youtube-uploader/scripts

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
--thumbnail		Custom thumbnail image path
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

Output

On success, returns:

Video ID
Video URL (https://youtu.be/VIDEO_ID)
Status
Limitations
Max file size: 256GB (YouTube limit)
Supported formats: MP4, MOV, AVI, WMV, FLV, 3GP, MPEG
Daily upload quota: 10,000 units (typically ~6 videos/day)
Title max: 100 characters
Description max: 5,000 characters
Tags max: 500 characters total
Weekly Installs
184
Repository
aviz85/claude-s…-library
GitHub Stars
27
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
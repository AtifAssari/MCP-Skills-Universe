---
rating: ⭐⭐
title: video-clipper
url: https://skills.sh/dkyazzentwatwa/chatgpt-skills/video-clipper
---

# video-clipper

skills/dkyazzentwatwa/chatgpt-skills/video-clipper
video-clipper
Installation
$ npx skills add https://github.com/dkyazzentwatwa/chatgpt-skills --skill video-clipper
SKILL.md
Video Clipper

Cut and trim video segments with precise timestamp control.

Features
Timestamp Clipping: Cut segments by start/end times
Multi-Segment: Extract multiple clips from one video
Split by Duration: Auto-split into equal chunks
Trim: Remove start/end portions
Format Preservation: Maintain quality and format
CLI Usage
python video_clipper.py --input video.mp4 --start 00:01:00 --end 00:02:30 --output clip.mp4
python video_clipper.py --input video.mp4 --split 60 --output clips/

Dependencies
moviepy>=1.0.3
ffmpeg-python>=0.2.0
Weekly Installs
104
Repository
dkyazzentwatwa/…t-skills
GitHub Stars
53
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
---
title: video-frames
url: https://skills.sh/steipete/clawdis/video-frames
---

# video-frames

skills/steipete/clawdis/video-frames
video-frames
Installation
$ npx skills add https://github.com/steipete/clawdis --skill video-frames
Summary

Extract individual frames or thumbnails from videos at specified timestamps.

Single command extracts frames at any timestamp or defaults to the first frame
Supports both JPG (for quick sharing) and PNG (for crisp UI frames) output formats
Requires ffmpeg binary; installation via Homebrew included
SKILL.md
Video Frames (ffmpeg)

Extract a single frame from a video, or create quick thumbnails for inspection.

Quick start

First frame:

{baseDir}/scripts/frame.sh /path/to/video.mp4 --out /tmp/frame.jpg


At a timestamp:

{baseDir}/scripts/frame.sh /path/to/video.mp4 --time 00:00:10 --out /tmp/frame-10s.jpg

Notes
Prefer --time for “what is happening around here?”.
Use a .jpg for quick share; use .png for crisp UI frames.
Weekly Installs
1.4K
Repository
steipete/clawdis
GitHub Stars
367.2K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
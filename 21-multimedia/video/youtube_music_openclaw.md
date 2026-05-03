---
title: youtube-music-openclaw
url: https://skills.sh/miwgel/youtube-music-openclaw/youtube-music-openclaw
---

# youtube-music-openclaw

skills/miwgel/youtube-music-openclaw/youtube-music-openclaw
youtube-music-openclaw
Installation
$ npx skills add https://github.com/miwgel/youtube-music-openclaw --skill youtube-music-openclaw
SKILL.md
YouTube Music Control (Kaset)
Playback Commands
osascript -e 'tell application "Kaset" to <command>'

Command	Description
play	Play/resume
pause	Pause
next track	Next song
previous track	Previous song
set volume N	Volume 0-100
toggle mute	Mute on/off
toggle shuffle	Shuffle on/off
like track	Like current
get player info	Get state as JSON
Search and Play
# 1. Search (returns JSON array with id, title)
{baseDir}/bin/youtube-search "artist or song name"

# 2. Play by ID
{baseDir}/bin/play-video VIDEO_ID


When user wants to play something, search first, pick a random result, then play it.

Weekly Installs
15
Repository
miwgel/youtube-…openclaw
GitHub Stars
2
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn
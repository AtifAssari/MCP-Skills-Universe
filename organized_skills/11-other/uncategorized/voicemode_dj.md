---
rating: ⭐⭐⭐
title: voicemode-dj
url: https://skills.sh/mbailey/voicemode/voicemode-dj
---

# voicemode-dj

skills/mbailey/voicemode/voicemode-dj
voicemode-dj
Installation
$ npx skills add https://github.com/mbailey/voicemode --skill voicemode-dj
SKILL.md
VoiceMode DJ

Background music control during VoiceMode sessions via voicemode dj commands.

Default: Music For Programming

When asked to play music for coding/programming, default to Music For Programming episode 49:

voicemode dj mfp play 49


This plays Julien Mier's mix with chapter navigation support. Use voicemode dj mfp list to see all available episodes.

Quick Reference
voicemode dj play <file|url>     # Start playback
voicemode dj stop                # Stop playback
voicemode dj mfp play 49         # Play MFP episode (Julien Mier)
voicemode dj status              # What's playing
voicemode dj next / prev         # Chapter navigation
voicemode dj volume [0-100]      # Get/set volume
voicemode dj find <query>        # Search library

Documentation
Commands - Full command reference
Music For Programming - MFP episode integration
Chapter Files - FFmpeg chapter format
Installation - Setup requirements
IPC Reference - Low-level mpv control
Programmatic Access
from voice_mode import DJController, MfpService, MusicLibrary

Configuration

~/.voicemode/voicemode.env:

VOICEMODE_DJ_VOLUME=50   # Default startup volume

Weekly Installs
30
Repository
mbailey/voicemode
GitHub Stars
1.1K
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
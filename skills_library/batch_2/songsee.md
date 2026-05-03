---
title: songsee
url: https://skills.sh/steipete/clawdis/songsee
---

# songsee

skills/steipete/clawdis/songsee
songsee
Installation
$ npx skills add https://github.com/steipete/clawdis --skill songsee
SKILL.md
songsee

Generate spectrograms + feature panels from audio.

Quick start

Spectrogram: songsee track.mp3
Multi-panel: songsee track.mp3 --viz spectrogram,mel,chroma,hpss,selfsim,loudness,tempogram,mfcc,flux
Time slice: songsee track.mp3 --start 12.5 --duration 8 -o slice.jpg
Stdin: cat track.mp3 | songsee - --format png -o out.png

Common flags

--viz list (repeatable or comma-separated)
--style palette (classic, magma, inferno, viridis, gray)
--width / --height output size
--window / --hop FFT settings
--min-freq / --max-freq frequency range
--start / --duration time slice
--format jpg|png

Notes

WAV/MP3 decode native; other formats use ffmpeg if available.
Multiple --viz renders a grid.
Weekly Installs
958
Repository
steipete/clawdis
GitHub Stars
367.2K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass
---
title: camsnap
url: https://skills.sh/steipete/clawdis/camsnap
---

# camsnap

skills/steipete/clawdis/camsnap
camsnap
Installation
$ npx skills add https://github.com/steipete/clawdis --skill camsnap
SKILL.md
camsnap

Use camsnap to grab snapshots, clips, or motion events from configured cameras.

Setup

Config file: ~/.config/camsnap/config.yaml
Add camera: camsnap add --name kitchen --host 192.168.0.10 --user user --pass pass

Common commands

Discover: camsnap discover --info
Snapshot: camsnap snap kitchen --out shot.jpg
Clip: camsnap clip kitchen --dur 5s --out clip.mp4
Motion watch: camsnap watch kitchen --threshold 0.2 --action '...'
Doctor: camsnap doctor --probe

Notes

Requires ffmpeg on PATH.
Prefer a short test capture before longer clips.
Weekly Installs
972
Repository
steipete/clawdis
GitHub Stars
367.2K
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykFail
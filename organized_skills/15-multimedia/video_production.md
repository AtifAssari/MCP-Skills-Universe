---
rating: ⭐⭐
title: video-production
url: https://skills.sh/cklxx/elephant.ai/video-production
---

# video-production

skills/cklxx/elephant.ai/video-production
video-production
Installation
$ npx skills add https://github.com/cklxx/elephant.ai --skill video-production
SKILL.md
video-production

Generate short videos via ARK Seedance backend.

Required Env
ARK_API_KEY
SEEDANCE_ENDPOINT_ID
Constraints
action=generate only.
Backend must return a video url; missing URL fails fast.
Output file must be written and non-empty, otherwise success=false.
Default output path: /tmp/seedance_<ts>.mp4.
Parameters
name	type	required	notes
prompt	string	yes	video description
duration	number	no	seconds, default 5
output	string	no	output path
Usage
python3 skills/video-production/run.py generate --prompt 'cute cat animation' --duration 5 --output /tmp/cat.mp4

Weekly Installs
51
Repository
cklxx/elephant.ai
GitHub Stars
10
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
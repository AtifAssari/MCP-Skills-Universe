---
title: osint
url: https://skills.sh/kiwamizamurai/cctf/osint
---

# osint

skills/kiwamizamurai/cctf/osint
osint
Installation
$ npx skills add https://github.com/kiwamizamurai/cctf --skill osint
SKILL.md
OSINT Skill
Quick Workflow
Progress:
- [ ] Identify target type (username/image/domain)
- [ ] Extract metadata (exiftool for images)
- [ ] Cross-reference across platforms
- [ ] Check archives/caches
- [ ] Document findings

Quick Commands
# Image metadata
exiftool image.jpg
exiftool -gpslatitude -gpslongitude image.jpg

# Username search
sherlock username

# DNS lookup
dig target.com ANY
whois target.com

Reference Files
Topic	Reference
Image Analysis & Geolocation	reference/image.md
Domain & IP OSINT	reference/domain.md
Social Media & Username	reference/social.md
Useful Online Tools
Tool	Purpose	URL
Shodan	IoT/device search	shodan.io
Censys	Internet scan data	censys.io
VirusTotal	File/URL analysis	virustotal.com
CyberChef	Data transformation	gchq.github.io/CyberChef
IntelX	Search engine	intelx.io
Maltego	Graph analysis	maltego.com
CTF Quick Patterns
# Find location from photo
exiftool -gpslatitude -gpslongitude image.jpg
# If no GPS: reverse image search, identify landmarks

# Find person from username
sherlock username
# Check: GitHub, Twitter, Instagram, Reddit

# Find deleted content
# Wayback Machine, Google cache, Archive.today

Weekly Installs
18
Repository
kiwamizamurai/cctf
GitHub Stars
7
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn
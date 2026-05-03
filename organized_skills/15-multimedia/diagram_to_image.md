---
rating: ⭐⭐
title: diagram-to-image
url: https://skills.sh/cklxx/elephant.ai/diagram-to-image
---

# diagram-to-image

skills/cklxx/elephant.ai/diagram-to-image
diagram-to-image
Installation
$ npx skills add https://github.com/cklxx/elephant.ai --skill diagram-to-image
SKILL.md
diagram-to-image

Render Mermaid code into image files.

Requirements
mmdc (Mermaid CLI) installed and in PATH.
Install command: npm install -g @mermaid-js/mermaid-cli
Constraints
action=render only.
Input field is code (Mermaid source).
Supported output formats: png (default), svg.
Render timeout: 30s.
Default output path: /tmp/diagram_<ts>.<format>.
Usage
python3 skills/diagram-to-image/run.py render --code 'graph LR
A[Client] --> B[API]
B --> C[(DB)]' --format png --theme default --output /tmp/diagram_arch.png

Weekly Installs
25
Repository
cklxx/elephant.ai
GitHub Stars
10
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
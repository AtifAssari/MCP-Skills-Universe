---
title: unzip-crx
url: https://skills.sh/xfstudio/skills/unzip-crx
---

# unzip-crx

skills/xfstudio/skills/unzip-crx
unzip-crx
Installation
$ npx skills add https://github.com/xfstudio/skills --skill unzip-crx
SKILL.md
Unzip CRX

Extract Chrome extension (.crx) files to a specified directory.

Usage

Run the script with the crx file path:

node ~/.claude/skills/unzip-crx/scripts/unzip-crx.mjs <crx-file-path> [destination]


Parameters:

crx-file-path: Path to the .crx file (required)
destination: Output directory (optional, defaults to a folder named after the crx file in the same directory)
Examples

Extract to default location (creates folder next to crx file):

node ~/.claude/skills/unzip-crx/scripts/unzip-crx.mjs /path/to/extension.crx
# Output: /path/to/extension/


Extract to specific directory:

node ~/.claude/skills/unzip-crx/scripts/unzip-crx.mjs /path/to/extension.crx /output/dir

Notes
The script auto-installs @tomjs/unzip-crx npm package on first run
Requires Node.js installed on the system
Weekly Installs
8
Repository
xfstudio/skills
GitHub Stars
5
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass
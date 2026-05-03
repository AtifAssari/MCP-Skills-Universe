---
title: xdrop
url: https://skills.sh/xixu-me/xdrop/xdrop
---

# xdrop

skills/xixu-me/xdrop/xdrop
xdrop
Originally fromxixu-me/skills
Installation
$ npx skills add https://github.com/xixu-me/xdrop --skill xdrop
SKILL.md
Xdrop

Use the bundled scripts inside this skill directory.

Available scripts
scripts/upload.mjs — Upload local files or directories to an Xdrop server and print the share link
scripts/download.mjs — Download an Xdrop share link, decrypt it locally, and save the files

Environment requirements:

Bun
Local filesystem access
Network access to the target Xdrop server
Upload
bun scripts/upload.mjs --server <xdrop-site-url> <file-or-directory> [...]


Prefer these flags when relevant:

--quiet: suppress progress output and keep stdout clean
--json: return transferId, shareUrl, and expiresAt
--expires-in <seconds>: choose a supported expiry
--api-url <url>: override the default <server>/api/v1
--name <value>: set the transfer display name
--concurrency <n>: limit parallel uploads per file

Useful examples:

bun scripts/upload.mjs --server http://localhost:8080 ./dist/report.pdf
bun scripts/upload.mjs --server http://localhost:8080 --quiet ./archive.zip
bun scripts/upload.mjs --server http://localhost:8080 --expires-in 600 --json ./notes.txt


If the user wants verification, upload a small temporary file and then confirm the public transfer API or browser can open the returned link.

Download

Require the full share link, including #k=.... Without the fragment key, the transfer cannot be decrypted.

bun scripts/download.mjs "<share-url>"


Prefer these flags when relevant:

--output <dir>: choose the destination directory
--quiet: suppress progress output and keep stdout clean
--json: return transferId, outputRoot, and saved file paths
--api-url <url>: override the default <share-origin>/api/v1

Useful examples:

bun scripts/download.mjs "http://localhost:8080/t/abc123#k=..."
bun scripts/download.mjs --output ./downloads "http://localhost:8080/t/abc123#k=..."
bun scripts/download.mjs --quiet --json --output ./downloads "http://localhost:8080/t/abc123#k=..."


By default the downloader writes to ./xdrop-<transferId> and preserves the manifest's relative paths.

Gotchas
A download link without the #k=... fragment is not decryptable. Ask for the full original share URL.
Use --quiet whenever another command or caller needs to capture stdout. Progress logs otherwise go to stderr, but the final result still matters.
Guardrails
Prefer --quiet when another command or script needs to capture stdout.
Keep the full share link fragment intact for downloads.
Do not bypass the scripts' built-in path sanitization or transfer cleanup behavior with manual ad hoc commands unless the user explicitly asks.
Weekly Installs
1.5K
Repository
xixu-me/xdrop
GitHub Stars
6
First Seen
Mar 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail
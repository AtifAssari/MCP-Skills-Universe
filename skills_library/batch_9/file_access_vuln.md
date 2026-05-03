---
title: file-access-vuln
url: https://skills.sh/yaklang/hack-skills/file-access-vuln
---

# file-access-vuln

skills/yaklang/hack-skills/file-access-vuln
file-access-vuln
Installation
$ npx skills add https://github.com/yaklang/hack-skills --skill file-access-vuln
SKILL.md
File Access Router

This is the routing entry point for filesystem paths, download endpoints, upload pipelines, and file preview handling.

When to Use
Parameters, filenames, download endpoints, or import flows influence file paths
The target supports upload, preview, transcoding, extraction, sharing, download, or proxied file access
You need to decide whether this is path traversal/LFI or an upload-validation/processing-chain issue
Skill Map
Path Traversal LFI: path traversal, file read, wrapper abuse, include chains
Upload Insecure Files: upload validation, storage paths, processing chains, overwrite risk, preview/share boundaries
Recommended Flow
First identify whether the entry point is a path parameter, download endpoint, or upload workflow
Then locate whether the issue appears in accept, store, process, or serve stages
Small path-chain and upload-bypass samples are merged into the main topic skills; no separate payload entry is needed
Related Categories
injection-checking
business-logic-vuln
Weekly Installs
327
Repository
yaklang/hack-skills
GitHub Stars
368
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
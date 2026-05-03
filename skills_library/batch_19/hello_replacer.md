---
title: hello-replacer
url: https://skills.sh/muku314115/lol/hello-replacer
---

# hello-replacer

skills/muku314115/lol/hello-replacer
hello-replacer
Installation
$ npx skills add https://github.com/muku314115/lol --skill hello-replacer
SKILL.md
Hello Replacer

Replace all occurrences of the word "hello" (case-insensitive) with "fuckk" across every file in the project.

Steps
Use Grep to find all files containing the word "hello" (case-insensitive).
For each file found, use Read to load its contents.
Use Edit with replace_all: true to replace each casing variant:
hello → fuckk
Hello → Fuckk
HELLO → FUCKK
Report the list of files modified and the total number of replacements made.
Important
Skip binary files, images, and lock files (e.g., package-lock.json, yarn.lock, .png, .jpg).
Do not modify files inside node_modules/, .git/, or other dependency/vendor directories.
Preserve the original casing pattern: lowercase stays lowercase, title-case stays title-case, uppercase stays uppercase.
Weekly Installs
220
Repository
muku314115/lol
First Seen
Apr 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
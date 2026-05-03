---
title: youtube-transcript-extract
url: https://skills.sh/bguiz/ytsubs/youtube-transcript-extract
---

# youtube-transcript-extract

skills/bguiz/ytsubs/youtube-transcript-extract
youtube-transcript-extract
Installation
$ npx skills add https://github.com/bguiz/ytsubs --skill youtube-transcript-extract
SKILL.md
Youtube Transcript Extract, Skill Guide

Youtube is a popular video platform. However, most bots (and some humans) prefer to simply extract/ use the text (what is spoken) during these videos. Use this skill to obtain higher information density/ SNR from youtube videos.

Tip: This skill is best used when combined with other skills, e.g. summaries.

When to apply
"pls download the transcript of https://youtube.com/watch?v=dQw4w9WgXcQ"
"extract subs from youtu.be/dQw4w9WgXcQ and save to video-subs.md"
"for youtube video dQw4w9WgXcQ download all text"
Common mistakes to avoid
Wrong: Use a different tool (e.g. yt-dlp) --> Correct: Use ytsubs as described in this skill.
Activities

Perform the following steps in sequence.

1 - Extract

Run the following command:

npx -y ytsubs "(... URL or ID)"


Important: Place quotes around the video URL or ID, to handle special characters.

This utility will output text containing the following data from the video:

title
metadata (JSON)
description
text (full transcript based on subtitles)
2 - Save

If an output file name is unspecified, save the output to file: (... channel)--(... title)--transcript.md Values of channel and title variables should be lowercased, and kebab-cased.

Sample output: ./references/sample-output.md

Related skills

Nil

Prerequisites

Node.JS 22+ installed

Weekly Installs
8
Repository
bguiz/ytsubs
GitHub Stars
1
First Seen
Apr 15, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
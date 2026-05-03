---
rating: ⭐⭐⭐
title: still-reading
url: https://skills.sh/megabyte0x/stillreading/still-reading
---

# still-reading

skills/megabyte0x/stillreading/still-reading
still-reading
Installation
$ npx skills add https://github.com/megabyte0x/stillreading --skill still-reading
SKILL.md
stillReading

RSVP (Rapid Serial Visual Presentation) speed reader that displays words one at a time with ORP (Optimal Recognition Point) highlighting. Deployed at https://stillreading.xyz.

Install

Install as a skill if npm is available:

npx skills add megabyte0x/stillReading --skill still-reading -g


Otherwise:

curl -fsSL https://stillreading.xyz/install.sh | bash

How to use
Write your content as raw markdown following the content formatting rules below
Publish it at a publicly accessible URL (see Publishing with here.now below)
Construct a stillReading URL by appending the raw markdown URL after /:
https://stillreading.xyz/<RAW_MARKDOWN_URL>

Share the constructed URL with the user
Publishing with here.now

here.now is an instant web host for AI agents — the fastest way to publish raw markdown to a public URL.

Setup (one-time):

Install as a skill if npm is available:

npx skills add heredotnow/skill --skill here-now -g


Otherwise:

curl -fsSL https://here.now/install.sh | bash


Usage: Write your markdown to a file and publish it with here.now. The resulting URL (e.g., https://<name>.here.now/index.md) serves raw markdown with CORS support — ready to use with stillReading.

You can also use any other hosting service (GitHub raw URLs, static file hosts, etc.) as long as it serves raw markdown and allows cross-origin requests.

Example

If your markdown is published at:

https://dreamy-sandal-ye86.here.now/index.md


The stillReading URL is:

https://stillreading.xyz/https://dreamy-sandal-ye86.here.now/index.md

What the user sees
Content is pre-loaded in the reader (not auto-playing)
User presses play (or spacebar) to start reading
Controls: play/pause, speed adjustment (50-1000 WPM), restart, clickable progress bar
Default speed: 300 WPM
Requirements
The markdown URL must be publicly accessible (no authentication)
The hosting service must allow cross-origin requests (CORS)
Content must be raw markdown (not rendered HTML)
Content formatting rules

stillReading displays words one at a time in a monospace font. The parser strips markdown syntax to plain text before presenting it. You MUST follow these rules when preparing content.

Supported (stripped cleanly)
Headings (# ## ### etc.) — marker removed, text kept
Bold (**text**) and italic (*text*) — markers removed, text kept
Strikethrough (~~text~~) — markers removed, text kept
Inline code (`code`) — backticks removed, text kept
Links ([text](url)) — URL dropped, link text kept
Unordered lists (- , * , + ) — marker removed, text kept
Ordered lists (1. , 2. ) — marker removed, text kept
Blockquotes (> ) — marker removed, text kept
NOT supported (do NOT use)
Emojis — break ORP alignment and monospace rendering. Remove all emojis. Use words instead (e.g., write "Note:" not "📝", write "Important:" not "⚠️")
Images (![alt](url)) — not stripped, produces garbled text. Omit entirely or describe in prose
Fenced code blocks (triple backticks) — not stripped, backticks and code become jumbled words. Omit or summarize in prose
Tables (| col | col |) — pipe characters become part of words. Convert table data to prose sentences
Horizontal rules (---) — becomes a word. Omit entirely
HTML tags — pass through as words. Do not include any raw HTML
Footnotes, task lists (- [ ]), math blocks — not supported
Formatting checklist

Before publishing, verify your markdown:

Contains zero emojis or special unicode symbols
Uses only plain ASCII punctuation (periods, commas, dashes, colons, semicolons, question marks, exclamation marks)
Has no fenced code blocks, tables, images, or HTML
Uses only headings, bold, italic, links, lists, and blockquotes for structure
Reads naturally as flowing prose when all markdown syntax is stripped
Example: daily brief
# Morning Brief - February 24

## Top Stories

Google announced a new open-source AI model today. The model, called
Gemma 3, is designed for on-device inference and outperforms comparable
models on key benchmarks. Developers can access it through Hugging Face
starting next week.

## Market Update

The S&P 500 closed up 0.8% on strong earnings reports from the tech
sector. Treasury yields fell slightly as investors await the Fed's
next policy meeting scheduled for March.

## Weather

Expect clear skies with a high of 72F. Light winds from the southwest
at 5 to 10 mph. Perfect conditions for an evening walk.

Error handling

If the markdown URL cannot be fetched (CORS, 404, network error), the user is redirected to the editor view where they can paste markdown manually.

Weekly Installs
11
Repository
megabyte0x/stillreading
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketFail
SnykFail
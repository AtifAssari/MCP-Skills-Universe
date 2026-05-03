---
title: m3u8-downloader
url: https://skills.sh/serpdownloaders/skills/m3u8-downloader
---

# m3u8-downloader

skills/serpdownloaders/skills/m3u8-downloader
m3u8-downloader
Installation
$ npx skills add https://github.com/serpdownloaders/skills --skill m3u8-downloader
SKILL.md
M3U8 Downloader (Browser Extension)

Detect and download HLS/M3U8 streams from supported websites and save them as MP4 files.

M3U8 Downloader is a browser extension built for users who need a site-agnostic HLS workflow instead of a single-site downloader. It monitors supported media requests in your browser, detects M3U8/HLS streams and related video sources, and helps you export them into standard MP4 files without relying on command-line tools.

Detect HLS/M3U8 streams from supported sites
Save compatible streams as MP4 files
Review multiple available stream variants and qualities
Download media from browser-visible streaming sessions
Use a browser workflow instead of FFmpeg or manual playlist extraction
Links
:rocket: Get it here: M3U8 Downloader
:new: Latest release: GitHub Releases
:question: Help center: SERP Help
:beetle: Report bugs: GitHub Issues
:bulb: Request features: Feature Requests
Preview

Table of Contents
Why M3U8 Downloader
Features
How It Works
Step-by-Step Tutorial: How to Download HLS Streams
Supported Formats
Who It's For
Common Use Cases
Troubleshooting
Trial & Access
Installation Instructions
FAQ
Notes
About M3U8 / HLS
Why M3U8 Downloader

HLS streams are not ordinary downloadable files. They are delivered through playlist manifests and media segments, which means right-click saving does not work and generic downloader tools often miss the real stream behind the page player. For many users, the alternatives are either fragile websites or technical command-line workflows.

M3U8 Downloader is built for that protocol-level use case. It watches browser-visible media requests, detects compatible stream sources, and gives you a cleaner way to export supported HLS media into a single local file.

Features
Automatic detection of compatible M3U8/HLS streams from browser activity
Support for related direct video formats where exposed by the page
MP4 export for compatible HLS workflows
Quality and stream-variant selection where multiple options exist
Download progress tracking for active exports
Browser-based workflow without requiring FFmpeg commands
Support for login-gated browser sessions when the stream is already available in the page context
Cross-browser support for Chrome, Edge, Brave, Opera, Firefox, Whale, and Yandex
How It Works
Install the extension from the latest release.
Open a supported website with an HLS or compatible media player.
Start playback so the browser loads the stream requests.
Open the extension popup to review detected streams.
Choose the stream or quality you want.
Download the media and save the final MP4 file locally.
Step-by-Step Tutorial: How to Download HLS Streams
Install M3U8 Downloader from the latest GitHub release.
Navigate to a supported page that uses an HLS or related streaming player.
Press play so the stream manifest and segments start loading.
Click the extension button in your browser toolbar.
Review the detected media sources and available quality variants.
Select the stream you want to keep.
Start the download and wait for the MP4 export to complete.
Open the saved file from your Downloads folder.
Supported Formats
Input: M3U8 / HLS streams
Input: Related compatible media sources where exposed by the page
Output: MP4

The final export is designed to turn stream-based playback into a single easier-to-use local video file.

Who It's For
Users downloading HLS streams from supported sites
Testers and QA users capturing browser-visible stream outputs
Creators archiving their own streamed media
Students or researchers preserving permitted streaming content for offline access
Anyone who wants a browser-based HLS workflow instead of terminal tools
Common Use Cases
Save a compatible HLS stream from a supported site
Export browser-visible M3U8 playback into a local MP4
Review multiple quality variants before downloading
Keep a local copy of content you are permitted to access
Capture a stream that other generic downloaders fail to detect
Troubleshooting

The extension is not detecting the stream
Press play first and wait a few seconds so the manifest and segments start loading.

No quality options are listed
Some players expose only one active stream variant.

The site requires login
The extension only works on media you can already access in your current browser session.

The stream still does not appear
Refresh the page, replay the media, and try again once the player is fully loaded.

The page uses DRM
DRM-protected content is outside the supported scope of normal HLS capture workflows.

Security & Scope
Operates only on the page the user intentionally opens in the active browser tab
Detects supported playback sources only for user-initiated downloads or exports
Does not execute page instructions, shell commands, or arbitrary scripts from page content
Does not follow unrelated links or perform actions outside the active workflow
Limits support to the named platform, approved embedded contexts, and user-authorized sessions when required
Trial & Access
Includes 3 free downloads so you can test the workflow first
Email sign-in uses secure one-time password verification
No credit card required for the trial
Unlimited downloads are available with a paid license

Start here: https://serp.ly/m3u8-downloader

Installation Instructions
Open the latest release page: https://github.com/serpapps/m3u8-downloader/releases/latest
Download the extension build for your browser.
Install the extension.
Open a supported page with streaming media.
Use the extension popup to detect and download the stream.
FAQ

What does this extension download?
Compatible HLS/M3U8 streams and related media sources that are visible to the browser on supported pages.

Does it save videos as MP4?
Yes. Compatible stream workflows are exported as MP4 files.

Do I need FFmpeg or terminal commands?
No. Everything runs through the browser extension workflow.

Why do I have to press play first?
Because the stream usually is not exposed until the player actually starts loading media.

Does it work on every streaming site?
No. It depends on the actual browser-visible media workflow and whether the stream is compatible with this extension's detection path.

License

This repository is distributed under the proprietary SERP Apps license in the LICENSE file. Review that file before copying, modifying, or redistributing any part of this project.

Notes
Only download content you own or have explicit permission to save
The extension only works when the stream is already accessible in your browser session
DRM-protected media is outside the normal supported workflow
Quality depends on what the player exposes for that stream
About M3U8 / HLS

M3U8 and HLS are stream delivery formats used by many modern video players. They are excellent for adaptive playback, but awkward for ordinary users who want a local file because the media is split into playlists and segments rather than exposed as a single downloadable video. M3U8 Downloader simplifies that workflow in a browser-first way.

Weekly Installs
480
Repository
serpdownloaders/skills
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn
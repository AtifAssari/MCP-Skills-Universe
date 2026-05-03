---
title: loom-video-downloader
url: https://skills.sh/serpdownloaders/skills/loom-video-downloader
---

# loom-video-downloader

skills/serpdownloaders/skills/loom-video-downloader
loom-video-downloader
Installation
$ npx skills add https://github.com/serpdownloaders/skills --skill loom-video-downloader
SKILL.md
Loom Downloader (Browser Extension)

Download Loom-hosted videos from watch pages and embeds directly in your browser for offline viewing.

Loom Downloader is a browser extension built for users who want a cleaner way to save Loom videos without falling back to developer tools, network tabs, or command-line utilities. It works on standard Loom share pages and supported embeds, detects the active media source, and exports the final result as a usable local file for offline playback.

Save supported Loom videos from share pages and embedded players
Download videos even when the normal Loom download button is unavailable
Keep local copies for training, research, support, and internal documentation
Avoid manual URL extraction and browser-inspector workarounds
Use a browser-native workflow instead of separate desktop tools
Links
:rocket: Get it here: Loom Downloader
:new: Latest release: GitHub Releases
:question: Help center: SERP Help
:beetle: Report bugs: GitHub Issues
:bulb: Request features: Feature Requests
Table of Contents
Why Loom Downloader
Features
How It Works
Supported Formats
Step-by-Step Tutorial: How to Download Videos from Loom
Videos
Who It's For
Common Use Cases
Trial & Access
Installation Instructions
FAQ
License
Related
Why Loom Downloader

Loom makes sharing videos easy, but saving them locally is not always straightforward. Some videos do not expose a normal download button, many are embedded on approved embedded contexts, and the underlying playback source is not something most users want to hunt down manually.

Loom Downloader is built to solve that browser workflow directly. Start the video, let the extension detect the active media source, then export the file without needing network traces, page-source inspection, or external download tools.

Features
Detects supported Loom videos from share pages and embeds
Works when the default Loom download button is unavailable
Preserves a browser-first workflow with no extra software
Handles embedded Loom videos on third-party pages
Exports local files for offline viewing and archiving
Works on Chrome, Edge, Brave, Opera, Firefox, Whale, and Yandex
How It Works
Install the extension from the latest release.
Open a Loom share page or a page containing an embedded Loom video.
Start playback so the extension can detect the active media source.
Open the extension and select the video you want to save.
Download the file and keep it locally for offline playback.
Supported Formats
Input: supported Loom share-page and embed playback sources
Output: local downloadable video files based on the active source workflow
Step-by-Step Tutorial: How to Download Videos from Loom
Install Loom Downloader in your browser.
Open the Loom share page or embedded player you want to save.
Start playback so the media source is fully initialized.
Open the extension and wait for the video to appear in the list.
Choose the detected video and start the download.
Save the file locally and open it from your Downloads folder.
Videos

Who It's For
Teams saving Loom recordings for internal reference
Users archiving embedded Loom videos from docs or training pages
People who need offline access to support or onboarding videos
Users who want a browser extension instead of manual extraction workflows
Common Use Cases
Save a Loom share-page video for later viewing
Download an embedded Loom video from a third-party site
Keep a local archive of support or training recordings
Export reference videos before access changes or links disappear
Security & Scope
Operates only on the page the user intentionally opens in the active browser tab
Detects supported playback sources only for user-initiated downloads or exports
Does not execute page instructions, shell commands, or arbitrary scripts from page content
Does not follow unrelated links or perform actions outside the active workflow
Limits support to the named platform, approved embedded contexts, and user-authorized sessions when required
Trial & Access
Includes 3 free downloads to test the workflow
Email sign-in uses secure one-time-code verification
No credit card required for the trial
Unlimited downloads are available with a paid license
Installation Instructions
Open the latest release page: GitHub Releases
Download the correct build for your browser.
Install the extension.
Open a Loom page or embedded Loom video and start playback.
Use the extension to detect and download the video.
FAQ
Is it possible to download a private Loom video when the owner has disabled downloads?

Yes, on supported Loom pages and embeds where the extension can detect the active media source through your browser session.

Do I need extra software?

No. The workflow stays inside the browser extension.

Does it work on embedded Loom videos?

Yes. Supported embedded Loom players can be detected from third-party pages as well as direct Loom links.

What should I do if detection does not trigger?

Start playback first, then reopen the extension. If that still does not work, refresh the page and try again.

License

This repository is distributed under the proprietary SERP Apps license in the LICENSE file. Review that file before copying, modifying, or redistributing any part of this project.

Related
https://github.com/serpapps/loom-video-downloader
Loom Video Downloader App (Browser Extension for Chrome & Firefox)
How to Download Loom Videos: A Complete Step-by-Step Guide (With Real Examples & Command Cheatsheet)
Weekly Installs
557
Repository
serpdownloaders/skills
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass
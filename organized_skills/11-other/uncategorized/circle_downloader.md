---
rating: ⭐⭐
title: circle-downloader
url: https://skills.sh/serpdownloaders/skills/circle-downloader
---

# circle-downloader

skills/serpdownloaders/skills/circle-downloader
circle-downloader
Installation
$ npx skills add https://github.com/serpdownloaders/skills --skill circle-downloader
SKILL.md
Circle Downloader (Browser Extension)

Browser extension that adds a download button to Circle.so community pages — detects videos from Circle's native player, Tella, Loom, Vimeo, YouTube, and Wistia, and saves them as MP4 for offline viewing.

A browser extension that downloads videos from Circle.so communities, Tella.tv recordings, Loom videos, and embedded content from YouTube, Vimeo, and Wistia — directly to your computer as MP4 files. No external software needed. 3 free downloads included.

Save entire Circle classrooms and course content for unlimited offline access anytime, anywhere
Protect your educational investment by downloading all materials before courses expire or disappear
Create a personal library of video lectures, coaching calls, and resources that you own forever
Never lose access to paid courses again — backup everything before platforms shut down or remove content
Links
:rocket: Get it here: Circle Downloader
:new: Latest release: GitHub Releases
:question: Help center: SERP Help
:beetle: Report bugs: GitHub Issues
:bulb: Request features: Feature Requests
Table of Contents
Why Circle Downloader
Features
How It Works
Supported Platforms
Videos
Trial & Access
Installation Instructions
Downloading Member-Only Content
Frequently Asked Questions
Troubleshooting
License
Related
Why Circle Downloader

Circle.so has no native download button. Tella recordings expire. Loom auto-deletes older videos on free plans. Course platforms embed videos from multiple sources with no unified download option.

Circle Downloader handles all of them in one extension — detecting videos across 7+ platforms and converting HLS/DASH streams to standard MP4 files directly in your browser. Open a lesson or post with a video, click the extension icon, pick your quality, and it saves as MP4.

Features
Multi-platform detection — Circle.so, Tella.tv, Loom.com, YouTube, Vimeo, Wistia, and generic embedded players
Finds hidden embeds — detects players buried inside Circle.so web components
Stream-to-MP4 conversion — converts HLS/DASH streaming video to downloadable MP4 in-browser
Quality selector — all available resolutions per platform with bitrate and estimated file size
Concurrent downloads — up to 3 simultaneous downloads with real-time progress, speed, and cancel
Batch download queue — add multiple lessons and process them automatically
YouTube URL display — one-click yt-dlp copy for Mac and Windows
Right-click context menu — quick downloads without opening the popup
Auto-organized storage — saves to a Circle Downloader subfolder in Downloads
Desktop notifications — alerts when downloads complete or fail
Original quality preserved — no re-encoding, no watermarks, no quality loss
Privacy-first — all processing on-device, zero tracking, no data sent to external servers
100% privacy-friendly — no tracking or data collection
1-on-1 support via our community
Supported Platforms & Pages
Content Type	Circle Native	YouTube	Vimeo	Wistia	Loom	Tella
Course Lessons	✅	✅	✅	✅	✅	✅
Community Posts	✅	✅	✅	✅	✅	✅
Coaching Calls	✅	✅	✅	✅	✅	✅
Member-Only Content	✅	✅	✅	✅	✅	✅
Supported Browsers

Chrome, Edge, Brave, Opera, Firefox, Whale, and Yandex — on Windows, macOS, and Linux.

Supported Formats
Input: Circle.so, Tella.tv, Loom.com, YouTube, Vimeo, Wistia, and generic embedded players
Output: MP4
How It Works
Install — Add SERP Circle Downloader to your browser
Navigate — Go to a Circle.so lesson, Tella recording, Loom video, or supported pages with embedded video
Play — Start the video so the extension can detect the stream
Download — Click the extension icon, pick your quality, and hit Download — saved as MP4
Videos
Security & Scope
Operates only on the page the user intentionally opens in the active browser tab
Detects supported playback sources only for user-initiated downloads or exports
Does not execute page instructions, shell commands, or arbitrary scripts from page content
Does not follow unrelated links or perform actions outside the active workflow
Limits support to the named platform, approved embedded contexts, and user-authorized sessions when required
Trial & Access
Includes 3 free downloads after email sign-in (OTP verification)
No credit card required for the free trial
Unlimited downloads available with a license
Installation Instructions

Each release has its own specific installation instructions to make it easier to upgrade, or rollback, to different versions. You can find the installation instructions for the specific version in the release:

https://github.com/serpapps/circle-downloader/releases
Downloading Member-Only Content

The Circle Downloader extension respects your existing Circle login and permissions. If you can view a post in your community — whether it's public, member-only, or restricted — the extension can download it using your authentication.

Key Points:

Your existing Circle login is used automatically in the background
No separate passwords or credentials needed
Works for private communities, restricted posts, and member-exclusive lessons
Downloads happen entirely on your device with no data sent to third parties
Frequently Asked Questions
Q: What sites does this extension support?

A: Circle.so (and Circle.com), Tella.tv, Loom.com, YouTube.com, Vimeo.com, and Wistia.com. It also detects generic embedded video players on approved embedded contexts.

Q: Does this work on native Circle videos?

A: Yes.

Q: Does this work on 2+ hour long videos?

A: Yes.

Q: Does this work on Loom/Tella videos embedded in Circle?

A: Yes.

Q: Can I download multiple videos at once?

A: Yes. The extension supports up to 3 concurrent downloads with individual progress tracking. Additional videos are added to an automatic queue.

Q: What quality options are available?

A: The extension detects all available resolutions from the source platform and lists them in the quality selector, sorted highest to lowest. Each option shows resolution, bitrate, and estimated file size.

Q: Does downloading preserve the original quality?

A: Yes. For adaptive streams (HLS/DASH), the extension downloads segments and merges them into a single MP4 without re-encoding. Direct MP4 uploads are saved at full quality instantly.

Q: Where are my downloads saved?

A: Videos automatically save to a Circle Downloader subfolder inside your browser's default Downloads directory. You can also set a custom default download location.

Q: Can I download member-only or private content?

A: Yes. If you can view the post in Circle, the extension can download it using your existing Circle login. Authentication happens automatically in the background.

Q: Why isn't the extension finding my video?

A: Press play on the video first. The extension needs the stream to start before detection works. If issues persist, refresh the page and try again.

Q: Is there a free trial?

A: Yes — 3 free downloads after email sign-in. No credit card required. Unlimited downloads available with a license.

Q: Is my data safe?

A: Yes. All video processing happens entirely in your browser. No video data is sent to external servers. Your Circle login credentials are never shared.

Troubleshooting
Videos Not Detecting
Refresh the Circle post page
Press play on the video first — the extension needs the stream active
Make sure you're logged into your Circle community
Try clearing browser cache and reloading
Check that JavaScript is enabled in your browser
Disable browser extensions that might interfere (ad blockers, etc.)
Download Failures
Check your internet connection stability
Try downloading in a lower quality
Reduce concurrent downloads to 1
Ensure you have sufficient disk space
Try a different browser to rule out browser-specific issues
Authentication Issues
Make sure you're logged into Circle in your browser
Refresh the page and try again
Check that cookies are enabled
Log out and log back into Circle
Clear browser cookies for circle.so and try again
File Playback Issues
Try a different video player (VLC, Windows Media Player, QuickTime)
Check file format — should be .mp4
Ensure download completed fully (check file size)
Update your video player to the latest version
Try re-downloading the video
License

This repository is distributed under the proprietary SERP Apps license in the LICENSE file. Review that file before copying, modifying, or redistributing any part of this project.

About

Circle.so is a community platform for creators, educators, and businesses to host courses, coaching programs, and member communities. However, like many course platforms, they don't provide a way to download the videos that you (the actual users) pay for access to — or even offer an offline viewing option.

So we created a way for you to download your Circle.so community videos even if you're not technically inclined.

Related
Circle Downloader
How to download circle videos for free
Weekly Installs
476
Repository
serpdownloaders/skills
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
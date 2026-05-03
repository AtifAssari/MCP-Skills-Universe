---
title: linkedin-downloader
url: https://skills.sh/serpdownloaders/skills/linkedin-downloader
---

# linkedin-downloader

skills/serpdownloaders/skills/linkedin-downloader
linkedin-downloader
Installation
$ npx skills add https://github.com/serpdownloaders/skills --skill linkedin-downloader
SKILL.md
LinkedIn Downloader (Browser Extension)

Download LinkedIn videos, images, and post text from feed pages and post pages in one browser workflow.

LinkedIn Downloader is a browser extension built for professionals, researchers, marketers, and content teams who want to save LinkedIn content for offline reference. It scans the posts visible on the current page, detects downloadable media, and lets you save videos, images, and post text in organized folders without relying on copy-paste or generic page scrapers.

Save LinkedIn videos as MP4 files for offline viewing
Download post images in their original available format
Export post text with source metadata for reference or research
Bulk-download all visible content from the current page
Organize saved files by author for easier archive management
Links
:rocket: Get it here: LinkedIn Downloader
:new: Latest release: GitHub Releases
:question: Help center: SERP Help
:beetle: Report bugs: GitHub Issues
:bulb: Request features: Feature Requests
Preview

Table of Contents
Why LinkedIn Downloader
Features
How It Works
Step-by-Step Tutorial: How to Download Content from LinkedIn
Supported Formats
Who It's For
Common Use Cases
Troubleshooting
Trial & Access
Installation Instructions
FAQ
Notes
About LinkedIn
Why LinkedIn Downloader

LinkedIn does not provide a clean export flow for feed videos, post images, and post text. Videos are served through web delivery layers that are awkward to save manually, images are mixed in with profile pictures and interface assets, and copying post text usually loses formatting or source context.

LinkedIn Downloader is built for that exact workflow. It scans visible LinkedIn posts, filters out common page clutter, and gives you a direct way to save useful content from the current page in a more organized format.

Features
Video detection for LinkedIn feed posts and post pages
Image filtering that excludes common avatars, logos, and interface assets
Post text export with source URL and timestamp metadata
Bulk-download workflow for all visible content on the current page
Organized folders by author name for cleaner archives
MP4 video saving when LinkedIn exposes downloadable video streams
Original-format image saving where available
TXT export for post text and metadata
Cross-browser support for Chrome, Edge, Brave, Opera, Firefox, Whale, and Yandex
How It Works
Install the extension from the latest release.
Open LinkedIn and go to your feed, a post page, or a video page.
Let the page finish loading so the extension can scan visible posts.
Open the extension popup to review detected videos, images, and text.
Download individual items or use the bulk option for everything visible.
Save the exported files locally in organized folders.
Step-by-Step Tutorial: How to Download Content from LinkedIn
Install LinkedIn Downloader from the latest GitHub release.
Sign in to LinkedIn and open the feed or post page you want to save from.
Scroll until the content you want is visible on the page.
Click the extension button to scan the current view.
Review the detected videos, images, and text entries.
Download individual items or run a bulk download for all visible results.
Open the saved files from your Downloads folder, organized by author.
Supported Formats
Video: MP4
Images: JPG, PNG, WebP, GIF, and other source formats where available
Text: TXT

Saved text exports include the post content plus source metadata such as the original URL and timestamp when available.

Who It's For
Professionals saving LinkedIn content for offline reference
Content creators archiving their own posts and videos
Researchers and analysts building organized post archives
Recruiters and marketers collecting examples, trends, or reference material
Teams that want a cleaner workflow than copy-pasting posts manually
Common Use Cases
Save a LinkedIn video post for offline viewing or presentation prep
Download post images for research boards or internal reference
Export post text into plain text files with source metadata
Bulk-download all visible content from a loaded feed page
Archive your own published LinkedIn posts in one place
Troubleshooting

The extension is not finding a post video
Make sure the post is fully loaded and visible on the page before scanning.

The wrong images are being picked up
LinkedIn Downloader filters common page assets, but pages with unusual layouts may still need a refresh and re-scan.

The bulk download missed some posts
Scroll further so more posts load, then run the scan again. The extension only captures content visible on the current page.

The text export looks incomplete
Expand long posts before scanning so the full text is visible in the browser.

A post requires login or restricted access
The extension only works on content you can already access in your current LinkedIn session.

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

Start here: https://serp.ly/linkedin-downloader

Installation Instructions
Open the latest release page: https://github.com/serpapps/linkedin-downloader/releases/latest
Download the extension build for your browser.
Install the extension.
Open LinkedIn and navigate to a feed, post, or video page.
Use the extension popup to scan and download visible content.
FAQ

What types of LinkedIn content can I download?
Videos, images, and post text from supported LinkedIn feed and post pages.

What file formats are used?
Videos are saved as MP4, images are saved in the source format when available, and post text is exported as TXT.

Does it download every image on the page?
No. The extension filters common profile pictures, logos, and interface graphics to focus on post content.

Can I bulk-download everything visible?
Yes. The extension supports bulk export for the content currently visible on the page.

Where are files saved?
They are saved to your default Downloads location, typically organized into LinkedIn-related folders by author.

Do I need extra software?
No. Everything runs through the browser extension.

License

This repository is distributed under the proprietary SERP Apps license in the LICENSE file. Review that file before copying, modifying, or redistributing any part of this project.

Notes
Only download content you own or have explicit permission to save
The extension only captures content currently visible on the page
Scroll to load more posts before scanning if you want a larger batch
Video quality depends on the streams LinkedIn exposes for that post
Respect LinkedIn terms and the rights of original content owners
About LinkedIn

LinkedIn is a professional social platform built around posts, articles, media sharing, and business networking. While it works well for consuming content in the browser, it does not offer a simple native workflow for exporting mixed post assets like video, images, and text together. LinkedIn Downloader simplifies that process for users who need a cleaner local archive workflow.

Weekly Installs
474
Repository
serpdownloaders/skills
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
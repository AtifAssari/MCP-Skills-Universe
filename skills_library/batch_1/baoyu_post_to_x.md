---
title: baoyu-post-to-x
url: https://skills.sh/jimliu/baoyu-skills/baoyu-post-to-x
---

# baoyu-post-to-x

skills/jimliu/baoyu-skills/baoyu-post-to-x
baoyu-post-to-x
Installation
$ npx skills add https://github.com/jimliu/baoyu-skills --skill baoyu-post-to-x
Summary

Post text, images, videos, and long-form articles to X via real Chrome browser automation.

Supports four post types: regular posts with images, video posts, quote tweets, and long-form Markdown articles (X Premium required)
Uses real Chrome with Chrome DevTools Protocol to bypass anti-bot detection; session persists after first manual login
Scripts fill content into the browser compose window; user reviews and publishes manually
Requires bun runtime and Google Chrome or Chromium; includes optional pre-flight environment check for accessibility, clipboard, and paste keystroke permissions
SKILL.md
Post to X (Twitter)

Posts text, images, videos, and long-form articles to X via real Chrome browser (bypasses anti-bot detection).

Script Directory

Important: All scripts are located in the scripts/ subdirectory of this skill.

Agent Execution Instructions:

Determine this SKILL.md file's directory path as {baseDir}
Script path = {baseDir}/scripts/<script-name>.ts
Replace all {baseDir} in this document with the actual path
Resolve ${BUN_X} runtime: if bun installed → bun; if npx available → npx -y bun; else suggest installing bun

Script Reference:

Script	Purpose
scripts/x-browser.ts	Regular posts (text + images)
scripts/x-video.ts	Video posts (text + video)
scripts/x-quote.ts	Quote tweet with comment
scripts/x-article.ts	Long-form article publishing (Markdown)
scripts/md-to-html.ts	Markdown → HTML conversion
scripts/copy-to-clipboard.ts	Copy content to clipboard
scripts/paste-from-clipboard.ts	Send real paste keystroke
scripts/check-paste-permissions.ts	Verify environment & permissions
Preferences (EXTEND.md)

Check EXTEND.md in priority order — the first one found wins:

Priority	Path	Scope
1	.baoyu-skills/baoyu-post-to-x/EXTEND.md	Project
2	${XDG_CONFIG_HOME:-$HOME/.config}/baoyu-skills/baoyu-post-to-x/EXTEND.md	XDG
3	$HOME/.baoyu-skills/baoyu-post-to-x/EXTEND.md	User home

If none found, use defaults.

EXTEND.md supports: Default Chrome profile

Prerequisites
Google Chrome or Chromium
bun runtime
First run: log in to X manually (session saved)
Pre-flight Check (Optional)

Before first use, suggest running the environment check. User can skip if they prefer.

${BUN_X} {baseDir}/scripts/check-paste-permissions.ts


Checks: Chrome, profile isolation, Bun, Accessibility, clipboard, paste keystroke, Chrome conflicts.

If any check fails, provide fix guidance per item:

Check	Fix
Chrome	Install Chrome or set X_BROWSER_CHROME_PATH env var
Profile dir	Shared profile at baoyu-skills/chrome-profile (see CLAUDE.md Chrome Profile section)
Bun runtime	brew install oven-sh/bun/bun (macOS) or npm install -g bun
Accessibility (macOS)	System Settings → Privacy & Security → Accessibility → enable terminal app
Clipboard copy	Ensure Swift/AppKit available (macOS Xcode CLI tools: xcode-select --install)
Paste keystroke (macOS)	Same as Accessibility fix above
Paste keystroke (Linux)	Install xdotool (X11) or ydotool (Wayland)
References
Regular Posts: See references/regular-posts.md for manual workflow, troubleshooting, and technical details
X Articles: See references/articles.md for long-form article publishing guide
Post Type Selection

Unless the user explicitly specifies the post type:

Plain text + within 10,000 characters → Regular Post (Premium members support up to 10,000 characters, non-Premium: 280)
Markdown file (.md) → X Article
Regular Posts
${BUN_X} {baseDir}/scripts/x-browser.ts "Hello!" --image ./photo.png


Parameters:

Parameter	Description
<text>	Post content (positional)
--image <path>	Image file (repeatable, max 4)
--profile <dir>	Custom Chrome profile

Note: Script opens browser with content filled in. User reviews and publishes manually.

Video Posts

Text + video file.

${BUN_X} {baseDir}/scripts/x-video.ts "Check this out!" --video ./clip.mp4


Parameters:

Parameter	Description
<text>	Post content (positional)
--video <path>	Video file (MP4, MOV, WebM)
--profile <dir>	Custom Chrome profile

Note: Script opens browser with content filled in. User reviews and publishes manually.

Limits: Regular 140s max, Premium 60min. Processing: 30-60s.

Quote Tweets

Quote an existing tweet with comment.

${BUN_X} {baseDir}/scripts/x-quote.ts https://x.com/user/status/123 "Great insight!"


Parameters:

Parameter	Description
<tweet-url>	URL to quote (positional)
<comment>	Comment text (positional, optional)
--profile <dir>	Custom Chrome profile

Note: Script opens browser with content filled in. User reviews and publishes manually.

X Articles

Long-form Markdown articles (requires X Premium).

${BUN_X} {baseDir}/scripts/x-article.ts article.md
${BUN_X} {baseDir}/scripts/x-article.ts article.md --cover ./cover.jpg


Parameters:

Parameter	Description
<markdown>	Markdown file (positional)
--cover <path>	Cover image
--title <text>	Override title

Frontmatter: title, cover_image supported in YAML front matter.

Note: Script opens browser with article filled in. User reviews and publishes manually.

Post-Composition Check: The script automatically verifies after all images are inserted:

Remaining XIMGPH_ placeholders in editor content
Expected vs actual image count

If the check fails (warnings in output), alert the user with the specific issues before they publish.

Troubleshooting
Chrome debug port not ready

If a script fails with Chrome debug port not ready or Unable to connect, kill existing Chrome CDP instances first, then retry:

pkill -f "Chrome.*remote-debugging-port" 2>/dev/null; pkill -f "Chromium.*remote-debugging-port" 2>/dev/null; sleep 2


Important: This should be done automatically — when encountering this error, kill Chrome CDP instances and retry the command without asking the user.

Notes
First run: manual login required (session persists)
All scripts only fill content into the browser, user must review and publish manually
Cross-platform: macOS, Linux, Windows
Extension Support

Custom configurations via EXTEND.md. See Preferences section for paths and supported options.

Weekly Installs
17.4K
Repository
jimliu/baoyu-skills
GitHub Stars
16.9K
First Seen
Jan 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn
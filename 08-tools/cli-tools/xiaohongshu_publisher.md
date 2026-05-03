---
title: xiaohongshu-publisher
url: https://skills.sh/iamzifei/red-publisher-skill/xiaohongshu-publisher
---

# xiaohongshu-publisher

skills/iamzifei/red-publisher-skill/xiaohongshu-publisher
xiaohongshu-publisher
Installation
$ npx skills add https://github.com/iamzifei/red-publisher-skill --skill xiaohongshu-publisher
SKILL.md
Xiaohongshu Publisher (小红书发布器)

Publish images and notes to Xiaohongshu (小红书) Creator Platform using agent-browser with CDP (Chrome DevTools Protocol) mode.

Architecture: CDP Mode

This skill uses CDP mode - connecting to an existing browser instance where the user is already logged in. This approach:

Eliminates QR code scanning - User logs in once in their browser
Leverages existing session - Uses the browser's cookies and auth state
More stable - No need to manage auth state files
agent-browser CLI - Simple command-line interface with --cdp flag
⚠️ IMPORTANT: Draft Mode by Default

This skill ALWAYS saves notes as DRAFT by default. It will NEVER auto-publish.

Only click the "发布" (publish) button if the user EXPLICITLY requests immediate publishing with phrases like:

"直接发布" / "立即发布" / "马上发布"
"publish now" / "publish directly" / "publish immediately"
"不要草稿，直接发" / "不存草稿"

If unsure, ALWAYS save as draft and let user review before publishing.

Prerequisites
1. Launch Chrome with Remote Debugging

Before using this skill, the user must launch Chrome with remote debugging enabled:

macOS:

/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222


Or create an alias in ~/.zshrc or ~/.bashrc:

alias chrome-debug='/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222'


Then simply run: chrome-debug

2. Login to Xiaohongshu

In the Chrome browser (with debug port), navigate to:

https://creator.xiaohongshu.com/publish/publish


Login using QR code scan with Xiaohongshu App. This only needs to be done once - the session persists in the browser.

Note: After login, you can minimize the browser window to the Dock. The browser must stay running (not closed) for CDP to work, but you don't need to see it.

3. Python Dependencies
pip install Pillow pyobjc-framework-Cocoa

agent-browser CDP Commands Reference

All commands use the --cdp 9222 flag to connect to the existing Chrome browser:

# Navigation
npx agent-browser --cdp 9222 open <url>          # Navigate to URL
npx agent-browser --cdp 9222 snapshot -i         # Get page snapshot with element refs

# Element Interaction
npx agent-browser --cdp 9222 click @e5           # Click element by ref
npx agent-browser --cdp 9222 fill @e2 "text"     # Fill input field
npx agent-browser --cdp 9222 type @e3 "text"     # Type text into element
npx agent-browser --cdp 9222 upload @e4 "/path/to/file.jpg"  # Upload file

# Keyboard & Wait
npx agent-browser --cdp 9222 press Enter         # Press key
npx agent-browser --cdp 9222 wait 2000           # Wait milliseconds
npx agent-browser --cdp 9222 wait --text "发布"  # Wait for text

# Screenshot
npx agent-browser --cdp 9222 screenshot          # Take screenshot


Important:

Element refs (like @e5) come from snapshot -i output. Always take a snapshot before interacting.
The --cdp 9222 flag connects to the browser's debug port instead of launching a new browser.
Do NOT use the close command as it would close the user's browser!
Scripts

Located in ~/.claude/skills/xiaohongshu-publisher/scripts/:

parse_note.py

Parse Markdown and extract structured data for Xiaohongshu notes:

python parse_note.py <markdown_file> [--output json]


Returns JSON with: title, content, images (list of paths), tags

copy_to_clipboard.py

Copy image to system clipboard for pasting:

python copy_to_clipboard.py image /path/to/image.jpg [--quality 80]

Workflow
Phase 0: Verify Browser Connection

CRITICAL: First verify that the CDP browser is running and connected.

Check if browser is accessible:

npx agent-browser --cdp 9222 snapshot -i

If connection fails, tell user: "请先启动带调试端口的 Chrome 浏览器"

Provide startup command if needed:

/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222

Phase 1: Check Login Status

Navigate to creator page (if not already there):

npx agent-browser --cdp 9222 open "https://creator.xiaohongshu.com/publish/publish"


Take snapshot to check login status:

npx agent-browser --cdp 9222 snapshot -i

Look for "上传图片" button = logged in
Look for QR code or login form = need to login

If login required:

Tell user: "请在浏览器中扫码登录小红书，登录后告诉我"
Wait for user confirmation
Take new snapshot to verify login success
Phase 2: Parse Content

If user provides a markdown file, parse it:

python ~/.claude/skills/xiaohongshu-publisher/scripts/parse_note.py /path/to/note.md


Output JSON:

{
  "title": "Note Title",
  "content": "Note description/content text...",
  "images": ["/path/to/img1.jpg", "/path/to/img2.jpg"],
  "tags": ["tag1", "tag2"]
}

Phase 3: Upload Images

Take snapshot to get current element refs:

npx agent-browser --cdp 9222 snapshot -i


Find the upload input element (look for file input or "上传图片" area)

Upload images:

# Single image
npx agent-browser --cdp 9222 upload @e<ref> "/path/to/image1.jpg"

# Multiple images (comma-separated)
npx agent-browser --cdp 9222 upload @e<ref> "/path/to/img1.jpg,/path/to/img2.jpg,/path/to/img3.jpg"


Wait for uploads to complete:

npx agent-browser --cdp 9222 wait 3000


Take new snapshot after upload completes

Phase 4: Fill Title and Content

Find title input field from snapshot (placeholder usually contains "标题")

Fill title:

npx agent-browser --cdp 9222 fill @e<title_ref> "Your Note Title"

Title limit: ~20 characters recommended

Find content/description field (placeholder usually contains "描述" or "正文")

Fill content:

npx agent-browser --cdp 9222 fill @e<content_ref> "Your note content here..."

Content limit: ~1000 characters max
Phase 5: Add Tags (Optional)

If tags are provided:

Find tag input area from snapshot

Add each tag:

npx agent-browser --cdp 9222 click @e<add_tag_ref>
npx agent-browser --cdp 9222 fill @e<tag_input_ref> "tag1"
npx agent-browser --cdp 9222 press Enter

Repeat for each tag (max 5 recommended)
Phase 6: Save as Draft (Default) or Publish
Default Action: Save as Draft

Find "存草稿" button from snapshot

Click draft button:

npx agent-browser --cdp 9222 click @e<draft_button_ref>


Verify success - take snapshot or wait for confirmation

Only If User Explicitly Requests Publishing

ONLY if user said "直接发布", "立即发布", or "publish now":

Find "发布" button from snapshot

Click publish button:

npx agent-browser --cdp 9222 click @e<publish_button_ref>


When in doubt, ALWAYS save as draft.

Phase 7: Verify and Report

Take final snapshot to verify success:

npx agent-browser --cdp 9222 snapshot -i


Report to user:

Draft saved: "草稿已保存！请在小红书 App 中预览和发布。"
Published: "笔记已发布成功！"
Example Flows
Example 1: Basic Image Publish

User: "发布这些图片到小红书: /path/to/photo1.jpg, /path/to/photo2.jpg, 标题是'周末好去处'"

# 1. Verify connection and check login
npx agent-browser --cdp 9222 snapshot -i

# 2. Navigate to publish page (if needed)
npx agent-browser --cdp 9222 open "https://creator.xiaohongshu.com/publish/publish"

# 3. Take snapshot, verify "上传图片" visible
npx agent-browser --cdp 9222 snapshot -i

# 4. Upload images
npx agent-browser --cdp 9222 upload @e<ref> "/path/to/photo1.jpg,/path/to/photo2.jpg"
npx agent-browser --cdp 9222 wait 3000

# 5. Take new snapshot, fill title
npx agent-browser --cdp 9222 snapshot -i
npx agent-browser --cdp 9222 fill @e<title_ref> "周末好去处"

# 6. Save as draft
npx agent-browser --cdp 9222 click @e<draft_ref>

Example 2: Markdown File Publish

User: "把这个 markdown 发到小红书: /path/to/note.md"

# 1. Parse markdown
python ~/.claude/skills/xiaohongshu-publisher/scripts/parse_note.py /path/to/note.md

# 2. Extract: title, content, images, tags from JSON output

# 3. Verify connection
npx agent-browser --cdp 9222 snapshot -i

# 4. Upload all images from parsed result
npx agent-browser --cdp 9222 upload @e<ref> "/path/to/img1.jpg,/path/to/img2.jpg"

# 5. Fill title and content
npx agent-browser --cdp 9222 fill @e<title_ref> "parsed title"
npx agent-browser --cdp 9222 fill @e<content_ref> "parsed content"

# 6. Add tags if present
npx agent-browser --cdp 9222 fill @e<tag_ref> "tag1"
npx agent-browser --cdp 9222 press Enter

# 7. Save as draft
npx agent-browser --cdp 9222 click @e<draft_ref>

Example 3: Direct Publish

User: "直接发布这些图到小红书，不用草稿"

# [Same as above until Step 6]

# Find and click "发布" button (NOT 存草稿)
npx agent-browser --cdp 9222 click @e<publish_ref>

Critical Rules
🚨 NEVER AUTO-PUBLISH - ALWAYS save as draft by default
🔌 ALWAYS USE --cdp 9222 - Every command must include this flag
❌ NEVER USE close COMMAND - Would close user's browser!
📸 TAKE SNAPSHOTS FREQUENTLY - Page state changes, always get fresh refs
⏳ WAIT AFTER UPLOADS - Give time for images to process
🔄 HANDLE LOGIN GRACEFULLY - Guide user to login in browser if needed
📝 RESPECT CONTENT LIMITS - Title ~20 chars, Content ~1000 chars
🖼️ IMAGE LIMITS - 1-18 images per note
Troubleshooting
CDP Connection Failed

If snapshot fails to connect:

Verify Chrome is running with debug port:

lsof -i :9222


If not running, start Chrome:

/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222


Check for port conflicts - another process might be using 9222

Session Expired

If previously logged in but now seeing login page:

Tell user to re-login in browser: "您的登录状态已过期，请在浏览器中重新扫码登录"

Wait for user confirmation

Take new snapshot to verify

Upload Failed
Check image file exists and is valid format (jpg, png, gif, webp)
Check file size (Xiaohongshu has limits)
Try uploading one at a time
Take screenshot to see actual error:
npx agent-browser --cdp 9222 screenshot error.png

Element Not Found
Page structure may have changed
Always take a fresh snapshot before interacting
Look for similar elements with different refs
Why CDP Mode with agent-browser?
Advantages:
No QR code scanning per session - Login persists in browser
User's own browser - Existing cookies and preferences
Simple CLI - Same agent-browser commands, just add --cdp 9222
No MCP server - Direct CLI invocation
Reliable auth - Browser handles session management
Trade-offs:
Requires browser running - User must start Chrome with debug port
Single browser instance - One session at a time
Manual first login - User does initial QR scan in browser
Supported Content
Type	Details
Images	JPG, PNG, GIF, WebP (1-18 images)
Title	Up to ~20 characters recommended
Content	Up to ~1000 characters
Tags	Up to 5 tags recommended
Weekly Installs
178
Repository
iamzifei/red-pu…er-skill
GitHub Stars
8
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
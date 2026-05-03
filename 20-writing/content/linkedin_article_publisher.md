---
title: linkedin-article-publisher
url: https://skills.sh/iamzifei/linkedin-article-publisher-skill/linkedin-article-publisher
---

# linkedin-article-publisher

skills/iamzifei/linkedin-article-publisher-skill/linkedin-article-publisher
linkedin-article-publisher
Installation
$ npx skills add https://github.com/iamzifei/linkedin-article-publisher-skill --skill linkedin-article-publisher
SKILL.md
LinkedIn Article Publisher

Publish Markdown content to LinkedIn Articles editor, preserving formatting with rich text conversion.

Prerequisites
Playwright MCP for browser automation
User logged into LinkedIn in browser
Python 3.9+ with dependencies: pip install Pillow pyobjc-framework-Cocoa
Scripts

Located in ~/.claude/skills/linkedin-article-publisher/scripts/:

parse_markdown.py

Parse Markdown and extract structured data:

python parse_markdown.py <markdown_file> [--output json|html] [--html-only]


Returns JSON with: title, cover_image, content_images (with block_index for positioning), html, total_blocks

copy_to_clipboard.py

Copy image or HTML to system clipboard:

# Copy image (with optional compression)
python copy_to_clipboard.py image /path/to/image.jpg [--quality 80]

# Copy HTML for rich text paste
python copy_to_clipboard.py html --file /path/to/content.html

Workflow

Strategy: "Text First, Images Later"

For articles with multiple images, paste ALL text content first, then insert images at correct positions using block index.

Parse Markdown with Python script -> get title, images with block_index, HTML
Navigate to LinkedIn Articles editor
Upload cover image (first image)
Fill title
Copy HTML to clipboard (Python) -> Paste with Cmd+V
Insert content images at positions specified by block_index
Save as draft (NEVER auto-publish)
Efficiency Guidelines

Goal: Minimize wait time between operations for smooth automation.

1. Avoid unnecessary browser_snapshot

Most browser operations (click, type, press_key, etc.) return page state in response. Don't call browser_snapshot after every operation - use the returned state directly.

Bad:
browser_click -> browser_snapshot -> analyze -> browser_click -> browser_snapshot -> ...

Good:
browser_click -> use returned state -> browser_click -> ...

2. Avoid unnecessary browser_wait_for

Only use browser_wait_for when:

Waiting for image upload to complete
Waiting for initial page load (rare cases)

Don't use browser_wait_for for buttons or inputs - they're available immediately after page load.

3. Parallel execution of independent operations

When two operations have no dependencies, call multiple tools in the same message:

Can parallel:
- Fill title (browser_type) + Copy HTML to clipboard (Bash)
- Parse Markdown JSON + Generate HTML file

Cannot parallel (has dependencies):
- Must navigate to editor before uploading cover image
- Must paste content before inserting images

4. Chain browser operations continuously

Each browser operation returns page state with element references. Use these references directly for the next operation:

# Ideal flow (execute directly, no extra waits):
browser_navigate -> find cover button in returned state -> browser_click(cover)
-> find title field in returned state -> browser_type(title)
-> click editor -> browser_press_key(Meta+v)
-> ...

5. Prepare work upfront

Before starting browser operations, complete all preparation:

Parse Markdown to get JSON data
Generate HTML file to /tmp/
Record title, cover_image, content_images info

This allows browser operations to execute continuously without stopping for data processing.

Step 1: Parse Markdown (Python)

Use parse_markdown.py to extract all structured data:

python ~/.claude/skills/linkedin-article-publisher/scripts/parse_markdown.py /path/to/article.md


Output JSON:

{
  "title": "Article Title",
  "cover_image": "/path/to/first-image.jpg",
  "content_images": [
    {"path": "/path/to/img2.jpg", "block_index": 5, "after_text": "context for debugging..."},
    {"path": "/path/to/img3.jpg", "block_index": 12, "after_text": "another context..."}
  ],
  "html": "<p>Content...</p><h2>Section</h2>...",
  "total_blocks": 45
}


Key fields:

block_index: The image should be inserted AFTER block element at this index (0-indexed)
total_blocks: Total number of block elements in the HTML
after_text: Kept for reference/debugging only, NOT for positioning

Save HTML to temp file for clipboard:

python parse_markdown.py article.md --html-only > /tmp/article_html.html

Step 2: Open LinkedIn Articles Editor
browser_navigate: https://www.linkedin.com/article/new/


Important: The page loads directly into the article editor. Wait for the editor to fully load:

Wait for page load: Use browser_snapshot to check page state
Look for editor elements: Title input field, content editor area, cover image button
If redirect occurs: LinkedIn may redirect - follow the redirect URL
# 1. Navigate to editor
browser_navigate: https://www.linkedin.com/article/new/

# 2. Get page snapshot to find elements
browser_snapshot

# 3. Proceed with cover image upload, title, content


Note: If user is not logged in, prompt them to log in manually and retry.

Step 3: Upload Cover Image

LinkedIn's cover image upload:

Find and click the cover image area/button (usually at top of editor, look for "Add a cover image" or camera icon)
Use browser_file_upload with the cover image path (from JSON output)
Wait for image upload to complete

Look for elements like:

"Add a cover image" button
Cover image placeholder area
Camera/image icon at top of editor
Step 4: Fill Title
Find the title input field (usually large text area at top with placeholder "Title")
Use browser_type to input title (from JSON output)
Step 5: Paste Text Content (Python Clipboard)

Copy HTML to system clipboard using Python, then paste:

# Copy HTML to clipboard
python ~/.claude/skills/linkedin-article-publisher/scripts/copy_to_clipboard.py html --file /tmp/article_html.html


Then in browser:

browser_click on editor content area
browser_press_key: Meta+v


This preserves all rich text formatting (H2, bold, links, lists).

Step 6: Insert Content Images (Block Index Positioning)

Key improvement: Use block_index for precise positioning instead of text matching.

Positioning principle

After pasting HTML, editor content consists of block elements (paragraphs, headers, quotes, etc.). Each image's block_index indicates it should be inserted after the Nth block element.

Operation steps
Get all block elements: Use browser_snapshot to get editor content, find all child elements under the textbox
Position by index: Click the block element at block_index position
Paste image: Copy image to clipboard then paste

For each content image (from content_images array):

# 1. Copy image to clipboard (with compression)
python ~/.claude/skills/linkedin-article-publisher/scripts/copy_to_clipboard.py image /path/to/img.jpg --quality 85

# 2. Click the block element at block_index
# Example: if block_index=5, click the 6th block element (0-indexed)
browser_click on the element at position block_index in the editor

# 3. Paste image
browser_press_key: Meta+v

# 4. Wait for upload to complete (short timeout, returns immediately when done)
browser_wait_for time=3

Positioning strategy

In browser_snapshot, editor content typically appears as:

textbox [ref=xxx]:
  generic [ref=block0]:  # block_index 0
    - paragraph content
  heading [ref=block1]:   # block_index 1
    - h2 content
  generic [ref=block2]:  # block_index 2
    - paragraph content
  ...


To insert image after block_index=5:

Find the 6th child element under editor textbox (0-indexed)
Click that element
Paste image

Note: Each inserted image shifts subsequent indices. Insert images in reverse order by block_index (highest to lowest) so earlier indices remain valid.

Reverse insertion example

If 3 images have block_index 5, 12, 27:

First insert block_index=27 image
Then insert block_index=12 image
Finally insert block_index=5 image

This way each insertion doesn't affect previously positioned locations.

Step 7: Save Draft
Verify content pasted (check if content appears correctly)
LinkedIn auto-saves drafts periodically (look for "Saved" indicator)
Optionally click "Publish" dropdown and select "Save as draft"
Report: "Draft saved. Review and publish manually."
Critical Rules
NEVER publish - Only save draft
First image = cover - Upload first image as cover image
Rich text conversion - Always convert Markdown to HTML before pasting
Use clipboard API - Paste via clipboard for proper formatting
Block index positioning - Use block_index for precise image placement
Reverse order insertion - Insert images from highest to lowest block_index
H1 title handling - H1 is used as title only, not included in body
Supported Formatting
H2 headers (## )
H3 headers (### )
Blockquotes (> )
Code blocks (...) - converted to blockquotes for compatibility
Bold text (**)
Italic text (*)
Hyperlinks (text)
Ordered lists (1. 2. 3.)
Unordered lists (- )
Paragraphs
Example Flow

User: "Publish /path/to/article.md to LinkedIn"

# Step 1: Parse Markdown
python ~/.claude/skills/linkedin-article-publisher/scripts/parse_markdown.py /path/to/article.md > /tmp/article.json
python ~/.claude/skills/linkedin-article-publisher/scripts/parse_markdown.py /path/to/article.md --html-only > /tmp/article_html.html

Navigate to https://www.linkedin.com/article/new/
Upload cover image (browser_file_upload for cover only)
Fill title (from JSON: title)
Copy & paste HTML:
python ~/.claude/skills/linkedin-article-publisher/scripts/copy_to_clipboard.py html --file /tmp/article_html.html

Then: browser_press_key Meta+v
For each content image, in reverse order of block_index:
python copy_to_clipboard.py image /path/to/img.jpg --quality 85

Click block element at block_index position
browser_press_key Meta+v
Wait for upload to complete
Verify content in editor
"Draft saved. Please review and publish manually."
Best Practices
Why use block_index instead of text matching?
Precise positioning: Doesn't rely on text content, works even with similar paragraphs
Reliability: Index is deterministic, won't confuse similar text
Easy debugging: after_text kept for human verification
Why use Python instead of browser JavaScript?
More reliable: Python operates system clipboard directly, not limited by browser sandbox
Image compression: Compress before upload (--quality 85), reduces upload time
Code reuse: Scripts are fixed, no need to rewrite conversion logic each time
Easy debugging: Scripts can be tested independently
Wait strategy

Key understanding: browser_wait_for's time parameter is maximum wait time, not fixed delay. Operations return immediately when conditions are met.

Bad: time=10 - if upload takes 2 seconds, remaining 8 seconds wasted
Good: time=3 - returns immediately when done, max wait 3 seconds
# Correct: Short time value, returns immediately when condition met
browser_wait_for time=3

# Wrong: Fixed long wait, wastes time
browser_wait_for time=10  # Unconditional 10-second wait


Principle: Don't assume "how long it takes" - set reasonable maximum, let condition checking return quickly.

Image insertion efficiency

Each image's browser operations reduced from 5 steps to 2:

Old: click -> add media -> media -> add photo -> file_upload
New: click paragraph -> Meta+v
Cover image vs content images
Cover image: Use browser_file_upload (dedicated upload button)
Content images: Use Python clipboard + paste (more efficient)
LinkedIn-Specific Notes
Editor URL
Primary: https://www.linkedin.com/article/new/
Alternative: https://www.linkedin.com/pulse/ (may redirect here)
UI Elements to Look For
Cover image: "Add a cover image" text or camera icon at top
Title: Large text input at top with "Title" placeholder
Content: Rich text editor area below title
Save: "Publish" dropdown button with "Save as draft" option
Auto-save indicator: "Saved" or "Saving..." text
Rich Text Support

LinkedIn's editor supports:

Headers (H2, H3)
Bold, Italic
Links (hyperlinks)
Lists (ordered and unordered)
Blockquotes
Inline images
Authentication
User must be logged into LinkedIn in the browser
No Premium subscription required (unlike X Articles)
Anyone with a LinkedIn account can publish articles
Weekly Installs
8
Repository
iamzifei/linked…er-skill
GitHub Stars
16
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
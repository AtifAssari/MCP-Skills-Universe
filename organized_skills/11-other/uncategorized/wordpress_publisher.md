---
rating: ⭐⭐
title: wordpress-publisher
url: https://skills.sh/aviz85/claude-skills-library/wordpress-publisher
---

# wordpress-publisher

skills/aviz85/claude-skills-library/wordpress-publisher
wordpress-publisher
Installation
$ npx skills add https://github.com/aviz85/claude-skills-library --skill wordpress-publisher
SKILL.md
WordPress Publisher

First time? If setup_complete: false above, run ./SETUP.md first, then set setup_complete: true.

Publish content to WordPress with a two-step flow: draft first, then publish after user confirmation.

Default Language: Hebrew

IMPORTANT: Unless the user explicitly requests English or another language, create all blog posts in Hebrew with RTL formatting. Also generate images using the image-generation skill for:

Featured/hero image for the post
Internal images to illustrate concepts (instead of ASCII diagrams)

Always wrap Hebrew content in:

<article dir="rtl" lang="he">
  <!-- Hebrew content here -->
</article>

Configuration

Create .env file in the skill directory:

# ~/.claude/skills/wordpress-publisher/.env
WP_URL=https://your-site.com
WP_USERNAME=your_username
WP_APP_PASSWORD=YourApplicationPasswordNoSpaces


Creating Application Password:

Go to WordPress Admin → Users → Profile
Scroll to "Application Passwords"
Enter a name (e.g., "Claude Code") and click "Add New"
Copy the password and remove all spaces
Usage
Create Draft
node ~/.claude/skills/wordpress-publisher/scripts/wp-publish.js create "Post Title" content.html

Create with Featured Image
node ~/.claude/skills/wordpress-publisher/scripts/wp-publish.js create "Post Title" content.html --image=cover.jpg

Create and Publish Immediately
node ~/.claude/skills/wordpress-publisher/scripts/wp-publish.js create "Post Title" content.html --publish

Publish Existing Draft
node ~/.claude/skills/wordpress-publisher/scripts/wp-publish.js publish POST_ID

Check Post Status
node ~/.claude/skills/wordpress-publisher/scripts/wp-publish.js status POST_ID

Read from stdin
echo "<h1>Hello</h1>" | node ~/.claude/skills/wordpress-publisher/scripts/wp-publish.js create "Hello" -

Options
Option	Description
--publish	Publish immediately (default: draft)
--image=<path>	Featured image (uploaded to media library)
--excerpt=<text>	Add excerpt
--categories=<ids>	Category IDs (comma-separated)
--tags=<ids>	Tag IDs (comma-separated)
Response Format
After Creating Draft:
Draft created!

**Post ID:** 123
**Edit in WordPress:** https://your-site.com/wp-admin/post.php?post=123&action=edit
**Preview:** https://your-site.com/?p=123

Publish now or review first?

After Publishing:
Post is live!

**URL:** https://your-site.com/your-post-slug/

Error Handling
Error	Cause	Solution
401 Unauthorized	Wrong credentials	Check WP_USERNAME and WP_APP_PASSWORD
403 Forbidden	No permissions	Ensure user has Editor/Admin role
404 Not Found	Wrong URL or API disabled	Check WP_URL, enable REST API
Hebrew/RTL Content

For Hebrew content, wrap in RTL container:

<article dir="rtl" lang="he">
  <!-- Hebrew content here -->
</article>

Weekly Installs
112
Repository
aviz85/claude-s…-library
GitHub Stars
27
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
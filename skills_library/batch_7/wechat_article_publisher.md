---
title: wechat-article-publisher
url: https://skills.sh/iamzifei/wechat-article-publisher-skill/wechat-article-publisher
---

# wechat-article-publisher

skills/iamzifei/wechat-article-publisher-skill/wechat-article-publisher
wechat-article-publisher
Installation
$ npx skills add https://github.com/iamzifei/wechat-article-publisher-skill --skill wechat-article-publisher
Summary

Publish Markdown or HTML articles to WeChat Official Account drafts via API.

Supports both Markdown and HTML file formats with automatic conversion; HTML preserves original formatting
Two article types available: standard news format and image-focused newspic (小绿书) mode
Requires WECHAT_API_KEY environment variable and authorized WeChat account on wx.limyai.com
Publishes to drafts only (user manually publishes in WeChat admin panel); includes account listing and error handling for expired tokens or missing authorization
SKILL.md
WeChat Article Publisher

Publish Markdown or HTML content to WeChat Official Account drafts via API, with automatic format conversion.

Prerequisites
WECHAT_API_KEY environment variable set (from .env file)
Python 3.9+
Authorized WeChat Official Account on wx.limyai.com
Scripts

Located in ~/.claude/skills/wechat-article-publisher/scripts/:

wechat_api.py

WeChat API client for listing accounts and publishing articles:

# List authorized accounts
python wechat_api.py list-accounts

# Publish from markdown file
python wechat_api.py publish --appid <wechat_appid> --markdown /path/to/article.md

# Publish from HTML file (preserves formatting)
python wechat_api.py publish --appid <wechat_appid> --html /path/to/article.html

# Publish with custom options
python wechat_api.py publish --appid <appid> --markdown /path/to/article.md --type newspic

parse_markdown.py

Parse Markdown and extract structured data (optional, for advanced use):

python parse_markdown.py <markdown_file> [--output json|html]

Workflow

Strategy: "API-First Publishing"

Unlike browser-based publishing, this skill uses direct API calls for reliable, fast publishing.

Load WECHAT_API_KEY from environment
List available WeChat accounts (if user hasn't specified)
Detect file format (Markdown or HTML) and parse accordingly
Call publish API to create draft in WeChat
Report success with draft details

Supported File Formats:

.md files → Parsed as Markdown, converted by WeChat API
.html files → Sent as HTML, formatting preserved
Step-by-Step Guide
Step 1: Check API Key

Before any operation, verify the API key is available:

# Check if .env file exists and contains WECHAT_API_KEY
cat .env | grep WECHAT_API_KEY


If not set, remind user to:

Copy .env.example to .env
Set their WECHAT_API_KEY value
Step 2: List Available Accounts

Get the list of authorized WeChat accounts:

python ~/.claude/skills/wechat-article-publisher/scripts/wechat_api.py list-accounts


Output example:

{
  "success": true,
  "data": {
    "accounts": [
      {
        "name": "我的公众号",
        "wechatAppid": "wx1234567890",
        "username": "gh_abc123",
        "type": "subscription",
        "verified": true,
        "status": "active"
      }
    ],
    "total": 1
  }
}


Important:

If only one account, use it automatically
If multiple accounts, ask user to choose
Note the wechatAppid for publishing
Step 3: Publish Article

For Markdown files:

python ~/.claude/skills/wechat-article-publisher/scripts/wechat_api.py publish \
  --appid <wechatAppid> \
  --markdown /path/to/article.md


For HTML files (preserves formatting):

python ~/.claude/skills/wechat-article-publisher/scripts/wechat_api.py publish \
  --appid <wechatAppid> \
  --html /path/to/article.html


For 小绿书 (image-text mode):

python ~/.claude/skills/wechat-article-publisher/scripts/wechat_api.py publish \
  --appid <wechatAppid> \
  --markdown /path/to/article.md \
  --type newspic


Success response:

{
  "success": true,
  "data": {
    "publicationId": "uuid-here",
    "materialId": "uuid-here",
    "mediaId": "wechat-media-id",
    "status": "published",
    "message": "文章已成功发布到公众号草稿箱"
  }
}

Step 4: Report Result

After successful publishing:

Confirm the draft was created
Remind user to review and publish manually in WeChat admin panel
Provide any relevant IDs for reference
API Reference
Authentication

All API requests require the X-API-Key header:

X-API-Key: WECHAT_API_KEY

Get Accounts List
POST https://wx.limyai.com/api/openapi/wechat-accounts

Publish Article
POST https://wx.limyai.com/api/openapi/wechat-publish


Parameters:

Parameter	Type	Required	Description
wechatAppid	string	Yes	WeChat AppID
title	string	Yes	Article title (max 64 chars)
content	string	Yes	Article content (Markdown/HTML)
summary	string	No	Article summary (max 120 chars)
coverImage	string	No	Cover image URL
author	string	No	Author name
contentFormat	string	No	'markdown' (default) or 'html'
articleType	string	No	'news' (default) or 'newspic'
Error Codes
Code	Description
API_KEY_MISSING	API key not provided
API_KEY_INVALID	API key invalid
ACCOUNT_NOT_FOUND	Account not found or unauthorized
ACCOUNT_TOKEN_EXPIRED	Account authorization expired
INVALID_PARAMETER	Invalid parameter
WECHAT_API_ERROR	WeChat API call failed
INTERNAL_ERROR	Server error
Critical Rules
NEVER auto-publish - Only save to drafts, user publishes manually
Check API key first - Fail fast if not configured
List accounts first - User may have multiple accounts
Handle errors gracefully - Show clear error messages
Preserve original content - Don't modify user's markdown unnecessarily
Supported Formats
Markdown Files (.md)
H1 header (# ) → Article title
H2/H3 headers (##, ###) → Section headers
Bold (text)
Italic (text)
Links text
Blockquotes (> )
Code blocks (...)
Lists (- or 1.)
Images  → Auto-uploaded to WeChat
HTML Files (.html)
<title> or <h1> → Article title
All HTML formatting preserved (styles, tables, etc.)
<img> tags → Images auto-uploaded to WeChat
First <p> → Auto-extracted as summary
Supports inline styles and rich formatting

HTML Title Extraction Priority:

<title> tag content
First <h1> tag content
"Untitled" as fallback

HTML Content Extraction:

If <body> exists, uses body content
Otherwise, strips <html>, <head>, <!DOCTYPE> and uses remaining content
Article Types
news (普通文章)
Standard WeChat article format
Full Markdown/HTML support
Rich text with images
newspic (小绿书/图文消息)
Image-focused format (like Instagram posts)
Maximum 20 images extracted from content
Text content limited to 1000 characters
Images auto-uploaded to WeChat
Example Flow
Markdown File

User: "把 ~/articles/ai-tools.md 发布到微信公众号"

# Step 1: Verify API key
cat .env | grep WECHAT_API_KEY

# Step 2: List accounts
python ~/.claude/skills/wechat-article-publisher/scripts/wechat_api.py list-accounts

# Step 3: Publish (assuming single account with appid wx1234567890)
python ~/.claude/skills/wechat-article-publisher/scripts/wechat_api.py publish \
  --appid wx1234567890 \
  --markdown ~/articles/ai-tools.md

# Step 4: Report
# "文章已成功发布到公众号草稿箱！请登录微信公众平台预览并发布。"

HTML File

User: "把这个HTML文章发布到公众号：~/articles/newsletter.html"

# Step 1: Verify API key
cat .env | grep WECHAT_API_KEY

# Step 2: List accounts
python ~/.claude/skills/wechat-article-publisher/scripts/wechat_api.py list-accounts

# Step 3: Publish HTML (auto-detects format)
python ~/.claude/skills/wechat-article-publisher/scripts/wechat_api.py publish \
  --appid wx1234567890 \
  --html ~/articles/newsletter.html

# Step 4: Report
# "文章已成功发布到公众号草稿箱！HTML格式已保留。请登录微信公众平台预览并发布。"

Error Handling
API Key Not Found
Error: WECHAT_API_KEY environment variable not set.


Solution: Ask user to set up .env file with their API key.

Account Not Found
Error: ACCOUNT_NOT_FOUND - 公众号不存在或未授权


Solution: Ask user to authorize their account on wx.limyai.com.

Token Expired
Error: ACCOUNT_TOKEN_EXPIRED - 公众号授权已过期


Solution: Ask user to re-authorize on wx.limyai.com.

WeChat API Error
Error: WECHAT_API_ERROR - 微信接口调用失败


Solution: May be temporary issue, retry or check WeChat service status.

Best Practices
Why use API instead of browser automation?
Reliability: Direct API calls are more stable than browser automation
Speed: No browser startup, page loading, or UI interactions
Simplicity: Single command to publish
Portability: Works on any system with Python (no macOS-only dependencies)
Content Guidelines
Images: Use public URLs when possible; local images will be uploaded
Title: Keep under 64 characters
Summary: Auto-extracted from first paragraph if not provided
Cover: First image in markdown becomes cover if not specified
Workflow Efficiency
Minimal workflow (1 command):
- list-accounts → get appid → publish → done

Full workflow (with verification):
1. Check .env → list accounts → confirm with user
2. Publish with options → report result

Troubleshooting
Q: How do I get a WECHAT_API_KEY?

A: Register and authorize your WeChat account at wx.limyai.com to get your API key.

Q: Can I publish to multiple accounts?

A: Yes, use list-accounts to see all authorized accounts, then specify the target --appid.

Q: Images not showing in WeChat?

A: Ensure images are accessible URLs. Local images are auto-uploaded but may fail if path is incorrect.

Q: Title is too long?

A: WeChat limits titles to 64 characters. The script will use the first 64 chars of H1.

Q: What's the difference between news and newspic?

A: news is standard article format; newspic (小绿书) is image-focused with limited text.

Weekly Installs
1.7K
Repository
iamzifei/wechat…er-skill
GitHub Stars
133
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass
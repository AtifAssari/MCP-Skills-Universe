---
title: tooyoung:ink-reader
url: https://skills.sh/shiqkuangsan/oh-my-daily-skills/tooyoung:ink-reader
---

# tooyoung:ink-reader

skills/shiqkuangsan/oh-my-daily-skills/tooyoung:ink-reader
tooyoung:ink-reader
Installation
$ npx skills add https://github.com/shiqkuangsan/oh-my-daily-skills --skill tooyoung:ink-reader
SKILL.md
Ink Reader

Intelligently read any URL content. Auto-detect platform, pick the best fetch strategy, output clean Markdown.

When to Activate

Activate this skill when the user:

Shares a URL and asks to read / fetch / view / grab its content
Says "read this link", "what does this say", "fetch this article"
Uses /ink-reader <url>
Fetch Strategy Overview

Four-layer fallback with platform-specific optimizations:

Layer 0: Camoufox       → WeChat-specific, bypasses anti-scraping (requires pip install)
Layer 1: Jina Reader    → Free, no API key, covers most public content
Layer 2: WebFetch        → Claude Code built-in, direct URL reading
Layer 3: Playwright MCP  → Browser automation, handles login-required sites

Platform Detection

Match the URL domain to determine platform and strategy routing:

Platform	Domain Contains	Needs Login	Strategy Order
WeChat	mp.weixin.qq.com	Yes	Camoufox → Jina → Playwright
Zhihu	zhihu.com	No	Jina → WebFetch
Bilibili	bilibili.com, b23.tv	No	Jina → WebFetch
Toutiao	toutiao.com	No	Jina → WebFetch
Weibo	weibo.com, m.weibo.cn	Yes	Jina → Playwright
Xiaohongshu	xiaohongshu.com	Yes	Jina → Playwright
Douyin	douyin.com	No	Jina → WebFetch
X/Twitter	x.com, twitter.com	Partial	See X/Twitter Flow
Generic	anything else	No	Jina → WebFetch
Routing Rules
No login required: Jina → WebFetch → Playwright MCP (if available)
WeChat: Camoufox → Jina → Playwright MCP (dedicated flow below)
Login required (Weibo, Xiaohongshu): Jina → Playwright MCP (skip WebFetch, it won't help)
X/Twitter: Dedicated flow below
Execution Steps
Step 1: Identify Platform

Parse the URL domain and match against the platform table above.

Step 2: Fetch Content
For normal platforms (no login needed)

Try Jina Reader:

Use WebFetch with URL: https://r.jina.ai/{original_url}
Prompt: "Extract the article title, author, publish time, and full body content. Return as-is in Markdown."
If result is meaningful (> 100 chars, no verification page), use it.

Try WebFetch direct:

Use WebFetch with the original URL directly.
Prompt: "Extract the article title, author, publish time, and full body content."
If result is meaningful, use it.

Try Playwright MCP (if available):

Navigate to the original URL.
Wait for content to load.
Take a snapshot and extract content.
If Playwright MCP is not available, skip this step.
For WeChat (mp.weixin.qq.com)

WeChat articles have aggressive anti-scraping. Jina Reader and WebFetch almost always fail. Use Camoufox as the primary strategy.

Prerequisites check (run once per session):

~/.ink-reader-env/bin/python3 -c "import camoufox; print('camoufox OK')" 2>/dev/null && echo "READY" || echo "NOT_INSTALLED"


Try Camoufox (if installed):

Check if ~/.agent-reach/tools/wechat-article-for-ai/main.py exists. If yes, use it:

cd ~/.agent-reach/tools/wechat-article-for-ai && ~/.ink-reader-env/bin/python3 main.py "{url}"


If that path doesn't exist, use inline invocation:

~/.ink-reader-env/bin/python3 -c "
import asyncio
from camoufox.sync_api import Camoufox
from markdownify import markdownify
with Camoufox(headless=True) as browser:
    page = browser.new_page()
    page.goto('{url}', wait_until='networkidle', timeout=30000)
    html = page.content()
    print(markdownify(html, strip=['script','style','nav','footer','header']))
"


Validate output (Step 3). If valid, use it.

Try Jina Reader (fallback — occasionally works for WeChat):

Use WebFetch with URL: https://r.jina.ai/{original_url}
If result is meaningful, use it.

Try Playwright MCP (if available, last resort):

Navigate to the original URL.
Wait for content to load.
Take a snapshot and extract content.

All failed → Show failure output with suggestion:

"WeChat articles require Camoufox to bypass anti-scraping. Install with: pip install camoufox[geoip] markdownify beautifulsoup4 httpx"

WeChat search (bonus — when user asks to search WeChat articles, not read a URL):

Check if miku_ai is installed:

~/.ink-reader-env/bin/python3 -c "import miku_ai; print('miku_ai OK')" 2>/dev/null && echo "READY" || echo "NOT_INSTALLED"


If installed, search articles:

~/.ink-reader-env/bin/python3 -c "
import asyncio
from miku_ai import get_wexin_article
async def search():
    results = await get_wexin_article('{query}', {count})
    for a in results:
        print(f'- [{a[\"title\"]}]({a[\"url\"]})')
asyncio.run(search())
"


Present results as a list. If user picks one, read it using the WeChat flow above. If miku_ai is not installed, inform user: pip install miku_ai

For login-required platforms (Weibo, Xiaohongshu)

Try Jina Reader (same as above, sometimes works even for login-required sites).

Try Playwright MCP (if available):

Navigate to the original URL.
If a verification/login page is detected, inform the user.
If Playwright MCP is not available, inform the user:

"This platform requires login. Install Playwright MCP to enable browser-based reading."

For X/Twitter

Extract status ID from URL:

Pattern: x.com/{user}/status/{id} or twitter.com/{user}/status/{id}
Strip query parameters.

Try Thread Reader App via Jina:

Use WebFetch with URL: https://r.jina.ai/https://threadreaderapp.com/thread/{status_id}.html
Prompt: "Extract the full thread content including all tweets. Return in Markdown."
If result is meaningful (> 100 chars, contains actual thread content), output as thread.

Try Jina on original X URL:

Use WebFetch with URL: https://r.jina.ai/{original_url}
Prompt: "Extract the tweet content, author, and timestamp."
If result is meaningful, output as single post.

Try Playwright MCP (if available):

Navigate to https://threadreaderapp.com/thread/{status_id}.html
Extract content from the page.
Step 3: Validate Content

Content is valid when ALL of these are true:

Length > 100 characters after trimming
Does NOT contain these verification markers: "环境异常", "完成验证", "请完成验证", "access denied", "please verify", "subscribe to continue", "sign in to read", "create a free account"
Is NOT a login wall or CAPTCHA page

If content fails validation, treat it as a failure and try the next strategy.

Step 4: Output

Use the output format specified below.

Output Format
Success
# {Title}

**Source**: {Platform Name}
**Author**: {Author name, omit if unavailable}
**Published**: {Time, omit if unavailable}
**URL**: {Original URL}
**Strategy**: {Camoufox / Jina Reader / WebFetch / Playwright MCP}

---

{Body content in Markdown}


Rules:

Only include Author and Published lines if the information is actually available.
Do NOT fabricate metadata. If it's not in the fetched content, omit it.
Keep images as remote URLs. Do NOT attempt to download images.
Clean up excessive whitespace, navigation elements, ads, and cookie banners from the content.
Failure
# Failed to read URL

**URL**: {url}
**Platform**: {detected platform}
**Attempted strategies**:

- {strategy 1}: {error reason}
- {strategy 2}: {error reason}

**Suggestions**:

- {contextual suggestions}


Contextual suggestions by scenario:

Login-required platform + no Playwright → "Install Playwright MCP to enable browser-based reading for this platform."
WeChat + no Camoufox → "Install Camoufox for reliable WeChat reading: pip install camoufox[geoip] markdownify beautifulsoup4 httpx"
WeChat + Camoufox failed → "Camoufox could not extract content. The article may have been deleted or restricted. Try opening the link in a browser."
All strategies returned empty → "The page may require JavaScript rendering. Try using Playwright MCP."
X/Twitter thread failed → "Try opening https://threadreaderapp.com/thread/{id}.html in your browser."
Save Mode

When the user says "save", "save it", "keep this", or "save to file" AFTER a successful read:

Create directory ./ink-reader-clips/ in current working directory (if not exists).
Write file: ./ink-reader-clips/{YYYY-MM-DD}_{sanitized_title}.md
File content:
---
title: "{Title}"
source: "{Platform Name}"
url: "{Original URL}"
saved_at: "{YYYY-MM-DD HH:MM:SS}"
---

{Body content}

Sanitize title for filename: remove <>:"/\|?*, replace whitespace with -, truncate to 50 chars.
Report: "Saved to ./ink-reader-clips/{filename}"

Do NOT auto-save. Only save when explicitly asked.

Optional Dependencies

The base skill (Jina Reader + WebFetch) works out of the box with zero setup. For enhanced platform support, install the following optional dependencies into a dedicated virtual environment:

WeChat article reading (Camoufox)
# Create dedicated venv (one-time)
uv venv ~/.ink-reader-env

# Install dependencies
uv pip install --python ~/.ink-reader-env "camoufox[geoip]" markdownify beautifulsoup4 httpx


This enables reliable reading of mp.weixin.qq.com articles by bypassing WeChat's anti-scraping with a stealth browser. No API key or login required.

WeChat article search (miku_ai)
uv pip install --python ~/.ink-reader-env miku_ai


Enables searching WeChat public account articles by keyword via Sogou. No API key required.

Verify installation
~/.ink-reader-env/bin/python3 -c "import camoufox; print('camoufox OK')"
~/.ink-reader-env/bin/python3 -c "import miku_ai; print('miku_ai OK')"

Important Notes
No API keys needed: Jina Reader, Camoufox, and miku_ai are all free and keyless.
Camoufox is optional but recommended: Without it, WeChat articles will fall back to Jina Reader (often fails) or Playwright MCP.
Playwright MCP is optional: The skill works without it, just with reduced capability for login-required platforms.
Images stay remote: Never download images. Keep original URLs in the Markdown output.
Respect content: Output the content faithfully. Do not summarize or modify unless the user explicitly asks.
Weekly Installs
22
Repository
shiqkuangsan/oh…y-skills
GitHub Stars
15
First Seen
Feb 16, 2026
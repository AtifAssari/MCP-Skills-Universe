---
rating: ⭐⭐⭐
title: feedgrab-setup
url: https://skills.sh/ibigqiang/feedgrab/feedgrab-setup
---

# feedgrab-setup

skills/ibigqiang/feedgrab/feedgrab-setup
feedgrab-setup
Installation
$ npx skills add https://github.com/ibigqiang/feedgrab --skill feedgrab-setup
SKILL.md
feedgrab Setup Guide

Install feedgrab, configure API keys, login to platforms, and verify everything works.

Trigger
/feedgrab-setup
"Install feedgrab"
"配置 feedgrab"
When /feedgrab reports "feedgrab not found"
Step 1: Check Python Environment
python3 --version 2>/dev/null || python --version 2>/dev/null
pip3 --version 2>/dev/null || pip --version 2>/dev/null


Requires Python ≥ 3.10. If not available, tell user to install Python first.

Step 2: Install feedgrab
pip install feedgrab[all]


This installs the full package with all optional dependencies (browser, stealth, Twitter, WeChat, Xiaohongshu, Feishu, Telegram).

For a minimal install:

pip install feedgrab                     # Core only (Jina fallback)
pip install feedgrab[browser]            # + Playwright
pip install feedgrab[twitter]            # + Twitter GraphQL
pip install feedgrab[stealth]            # + Anti-detection (patchright, curl_cffi)


After installation, verify:

feedgrab --help

Step 3: Interactive Setup
feedgrab setup


This runs a 5-step interactive wizard:

Output directory — where to save fetched content (default: ./output/)
Jina API — free, no key needed
YouTube API Key — optional, for YouTube search
GitHub Token — optional, for higher rate limits
Creates .env file with your configuration
Step 4: Platform Login (as needed)

For platforms requiring cookies/session:

# Twitter/X — opens browser for login
feedgrab login twitter

# Xiaohongshu — opens browser for login
feedgrab login xhs

# WeChat MP backend — opens browser for login (session valid ~4 days)
feedgrab login wechat

# Feishu — opens browser for login
feedgrab login feishu

# LinuxDo / Discourse — opens browser for login
feedgrab login linuxdo

# IDCFlare / Discourse — opens browser for login
feedgrab login idcflare

# KDocs (金山文档) — opens browser for login
feedgrab login kdocs

# Zhihu (知乎) — opens browser for login
feedgrab login zhihu


Tip: If you have Chrome running with remote debugging enabled, set CHROME_CDP_LOGIN=true in .env to extract cookies from your existing browser session without re-login.

Step 5: Verify Installation
# Full diagnostic
feedgrab doctor

# Platform-specific diagnostic
feedgrab doctor x          # Twitter/X
feedgrab doctor xhs        # Xiaohongshu
feedgrab doctor mpweixin   # WeChat
feedgrab doctor feishu     # Feishu

Step 6: Test
# Test with a simple URL (no login needed)
feedgrab https://github.com/iBigQiang/feedgrab


If the output .md file is generated successfully, setup is complete!

Advanced Configuration (.env)

Key environment variables (all optional):

# Output
OUTPUT_DIR=./output

# Twitter
X_BOOKMARKS_ENABLED=true
X_USER_TWEETS_ENABLED=true
X_LIST_TWEETS_ENABLED=true
X_DOWNLOAD_MEDIA=true

# Xiaohongshu
XHS_USER_NOTES_ENABLED=true
XHS_SEARCH_ENABLED=true
XHS_DOWNLOAD_MEDIA=true
XHS_FETCH_COMMENTS=true
XHS_PINIA_ENABLED=true

# WeChat
MPWEIXIN_DOWNLOAD_MEDIA=true
MPWEIXIN_FETCH_COMMENTS=true

# YouTube
YOUTUBE_API_KEY=your_key_here
YTDLP_COOKIES_BROWSER=chrome

# GitHub
GITHUB_TOKEN=your_token_here

# Feishu
FEISHU_APP_ID=your_app_id
FEISHU_APP_SECRET=your_secret
FEISHU_DOWNLOAD_IMAGES=true
FEISHU_CDP_ENABLED=false

# LinuxDo / Discourse
LINUXDO_CDP_ENABLED=true
LINUXDO_PAGE_LOAD_TIMEOUT=15000
LINUXDO_REPLY_MODE=author

# IDCFlare / Discourse
IDCFLARE_CDP_ENABLED=true
IDCFLARE_PAGE_LOAD_TIMEOUT=15000
IDCFLARE_REPLY_MODE=author

# KDocs (金山文档)
KDOCS_CDP_ENABLED=false
KDOCS_DOWNLOAD_IMAGES=false

# Youdao Note (有道云笔记)
YOUDAO_DOWNLOAD_IMAGES=false

# Zhihu (知乎)
ZHIHU_CDP_ENABLED=false

# Bilibili subtitles / transcription
BILIBILI_SUBTITLE_LANG=zh-CN
BILIBILI_SUBTITLE_WHISPER=false

# Xiaoyuzhou / Ximalaya podcasts (require GROQ_API_KEY for transcription)
XIAOYUZHOU_WHISPER=true
XIMALAYA_WHISPER=true
GROQ_API_KEY=your_groq_key

# Paywall bypass (300+ news sites)
PAYWALL_ENABLED=true
PAYWALL_USE_AMP=true
PAYWALL_USE_ARCHIVE=true
PAYWALL_USE_GOOGLE_CACHE=true

# Stealth / CDP Cookie extraction
CHROME_CDP_LOGIN=true
CHROME_CDP_PORT=9222


See .env.example in the feedgrab repo for the full list.

Troubleshooting
Issue	Solution
pip install fails	Try pip install --user feedgrab[all] or use a virtualenv
Playwright not working	Run playwright install chromium
patchright not working	Run patchright install chromium
Cookie expired	Re-run feedgrab login <platform>
Windows encoding errors	feedgrab auto-fixes UTF-8, but ensure Python ≥ 3.10
Weekly Installs
41
Repository
ibigqiang/feedgrab
GitHub Stars
332
First Seen
Mar 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
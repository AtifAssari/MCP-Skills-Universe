---
rating: ⭐⭐⭐
title: wechat-article-to-markdown
url: https://skills.sh/jackwener/wechat-article-to-markdown/wechat-article-to-markdown
---

# wechat-article-to-markdown

skills/jackwener/wechat-article-to-markdown/wechat-article-to-markdown
wechat-article-to-markdown
Installation
$ npx skills add https://github.com/jackwener/wechat-article-to-markdown --skill wechat-article-to-markdown
SKILL.md
WeChat Article to Markdown

Fetch a WeChat Official Account article and convert it to a clean Markdown file.

When to use

Use this skill when you need to save WeChat articles as Markdown for:

Personal archive
AI summarization input
Knowledge base ingestion
Prerequisites
Python 3.8+
# Install
uv tool install wechat-article-to-markdown
# Or: pipx install wechat-article-to-markdown

Usage
wechat-article-to-markdown "<WECHAT_ARTICLE_URL>"


Input URL format:

https://mp.weixin.qq.com/s/...

Output files:

<cwd>/output/<article-title>/<article-title>.md
<cwd>/output/<article-title>/images/*
Features
Anti-detection fetch with Camoufox
Metadata extraction (title, account name, publish time, source URL)
Image localization to local files
WeChat code-snippet extraction and fenced code block output
HTML to Markdown conversion via markdownify
Concurrent image downloading
Limitations
Some code snippets are image/SVG rendered and cannot be extracted as source code
Public mp.weixin.qq.com URL is required
Weekly Installs
364
Repository
jackwener/wecha…markdown
GitHub Stars
606
First Seen
Mar 2, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn
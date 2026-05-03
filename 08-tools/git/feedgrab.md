---
title: feedgrab
url: https://skills.sh/ibigqiang/feedgrab/feedgrab
---

# feedgrab

skills/ibigqiang/feedgrab/feedgrab
feedgrab
Installation
$ npx skills add https://github.com/ibigqiang/feedgrab --skill feedgrab
SKILL.md
feedgrab — Universal Content Grabber

Give it a URL, get back structured Markdown. Supports 17+ platforms with deep extraction.

Trigger

Activate when user provides a URL and wants content fetched/extracted/read:

/feedgrab <URL>
"Grab this article"
"Read this tweet/post"
"抓取这个链接"
Any URL from supported platforms
Prerequisites Check

Before fetching, verify feedgrab is installed:

which feedgrab 2>/dev/null || command -v feedgrab 2>/dev/null


If NOT installed, tell the user:

feedgrab is not installed. Run `/feedgrab-setup` or manually:
  pip install feedgrab[all]
  feedgrab setup


Then stop — do not proceed without feedgrab.

Supported Platforms
Platform	URL Pattern	Method
X/Twitter	x.com/*/status/*, twitter.com/*	GraphQL → FxTwitter → Syndication → oEmbed → Jina → Playwright
WeChat (微信公众号)	mp.weixin.qq.com/*	Playwright JS evaluate → Jina
Xiaohongshu (小红书)	xiaohongshu.com/explore/*, xhslink.com/*	API (xhshow) → Pinia Store injection → Jina → Playwright
YouTube	youtube.com/watch?v=*, youtu.be/*, Shorts	InnerTube API → yt-dlp subtitles → Groq Whisper
GitHub	github.com/*/*	REST API (Chinese README priority + subdirectory scan)
LinuxDo / Discourse	linux.do/t/*	Discourse topic JSON API → CDP → Playwright in-page fetch → Jina
IDCFlare / Discourse	idcflare.com/t/*	Discourse topic JSON API → CDP → Playwright in-page fetch → Jina
Feishu/Lark (飞书)	feishu.cn/docx/*, feishu.cn/wiki/*	Open API → CDP → Playwright PageMain → Jina
KDocs (金山文档)	kdocs.cn/l/*	Playwright ProseMirror DOM (virtual scroll + CDP)
Youdao Note (有道云笔记)	share.note.youdao.com/*	JSON API → Playwright iframe → Jina
Zhihu (知乎)	zhihu.com/question/*/answer/*, zhuanlan.zhihu.com/p/*	API v4 → Playwright CDP/DOM → Jina
Bilibili (B站)	bilibili.com/video/*, b23.tv/*	API metadata + 3-tier subtitle fallback (v2 → WBI v2 → Whisper)
Xiaoyuzhou (小宇宙)	xiaoyuzhoufm.com/episode/*	SSR __NEXT_DATA__ + Groq Whisper transcription
Ximalaya (喜马拉雅)	ximalaya.com/sound/*, m.ximalaya.com/sound/*	Web Revision API + canPlay degradation + Groq Whisper
Telegram	t.me/*	Telethon
RSS	RSS/Atom feed URLs	feedparser
Paywall news (300+)	NYT/WSJ/FT/Economist/Bloomberg...	JSON-LD → Googlebot/Bingbot UA → AMP → EU IP → archive.today → Google Cache → Jina
Any web page	Any other URL	JSON-LD pre-scan → Jina Reader fallback
Pipeline
Step 1: Fetch Content
feedgrab "$ARGUMENTS"


The CLI auto-detects the platform and routes to the appropriate fetcher.

Step 2: Locate Output File

feedgrab saves output to OUTPUT_DIR (default: ./output/). Check the CLI output for the saved file path, typically:

output/X/author_date：title.md
output/mpweixin/author_date：title.md
output/XHS/author_date：title.md
output/YouTube/author_date：title.md
output/GitHub/author_date：title.md
output/LinuxDo/author_date：title.md
output/IDCFlare/author_date：title.md
output/Feishu/author_date：title.md
output/KDocs/author_date：title.md
output/NoteYouDao/author_date：title.md
output/Zhihu/author_date：title.md
output/Bilibili/author_date：title.md
output/Xiaoyuzhou/author_date：title.md
output/Ximalaya/author_date：title.md
output/Web/author_date：title.md (paywall / generic pages)
Step 3: Read and Present

Read the output .md file and present the content to the user. The file includes:

YAML front matter (title, source, author, published, likes, tags, etc.)
Full article/tweet/post content in Markdown
Images (as remote URLs or local paths if media download is enabled)
Clipboard Mode

If the user says "grab from clipboard" or the URL contains & (which breaks PowerShell):

feedgrab clip


This reads the URL from the system clipboard.

Error Handling
Error	Solution
feedgrab: command not found	Run /feedgrab-setup
Cookie expired / 401 / 403	feedgrab login <platform> to refresh
Jina timeout (30s)	feedgrab auto-retries with Playwright
Rate limit (429)	feedgrab auto-rotates cookies if configured
OUTPUT_DIR not set	feedgrab setup to configure
Tips
For Twitter deep extraction (views, bookmarks, threads): configure cookies via feedgrab login twitter
For WeChat articles: no login needed for single articles
For Xiaohongshu: pip install xhshow for API mode (faster, no browser needed)
For GitHub: set GITHUB_TOKEN for higher rate limits (5000/hr vs 60/hr)
For LinuxDo / Discourse: feedgrab login linuxdo if the topic is private or the site requires a browser session / Cloudflare cookie
For IDCFlare / Discourse: feedgrab login idcflare if the topic is private or the site requires a browser session / Cloudflare cookie
For Discourse forums: default reply mode is OP + topic-author follow-up replies only; switch with LINUXDO_REPLY_MODE / IDCFLARE_REPLY_MODE (author / all / none)
For Feishu: set FEISHU_APP_ID + FEISHU_APP_SECRET for Open API access
For KDocs: feedgrab login kdocs to save session (or enable KDOCS_CDP_ENABLED=true to reuse running Chrome)
For Zhihu: feedgrab login zhihu to save session (enables full answer content)
For Bilibili subtitles: free tier (player/v2 + WBI) works out of the box; set BILIBILI_SUBTITLE_WHISPER=true for Whisper fallback on videos without subtitles
For Xiaoyuzhou / Ximalaya: set GROQ_API_KEY for Whisper transcription (free tier = metadata + shownotes only)
For paywall sites: PAYWALL_ENABLED=true by default, no extra config
Run feedgrab doctor to diagnose issues
Weekly Installs
47
Repository
ibigqiang/feedgrab
GitHub Stars
332
First Seen
Mar 22, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykWarn
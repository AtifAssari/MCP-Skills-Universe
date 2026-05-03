---
title: web-fetcher
url: https://skills.sh/jiahao-shao1/sjh-skills/web-fetcher
---

# web-fetcher

skills/jiahao-shao1/sjh-skills/web-fetcher
web-fetcher
Installation
$ npx skills add https://github.com/jiahao-shao1/sjh-skills --skill web-fetcher
SKILL.md
Web Fetcher

Fetch any URL as clean markdown. Two paths: known platforms go through OpenCLI (uses browser login state), everything else falls back through a chain of free markdown services.

Strategy Overview
Known platforms (Twitter/X, zhihu, reddit, weibo, xiaohongshu, bilibili, etc.) → OpenCLI first. It uses the user's browser login state, is deterministic, and costs zero LLM tokens.
Generic URLs (blogs, docs, articles) → Jina Reader > defuddle.md > markdown.new > WebFetch.

These are soft priorities — skip obviously wrong strategies (e.g., don't try OpenCLI for a random blog post, don't try Jina for a login-walled zhihu page).

Known Platform → OpenCLI Commands
URL Pattern	Command	Notes
x.com/.../status/<id>	opencli twitter thread <id>	Tweet threads. If the result is just a t.co link (very short text), the tweet likely links to an X Article — retry with opencli twitter article <same-id>
x.com/.../article/<id> or x.com/i/article/<id>	opencli twitter article <id>	X Article long-form
zhihu.com/question/<id>	opencli zhihu question <id>	
zhuanlan.zhihu.com/p/<id>	opencli zhihu download <full-url>	
reddit.com/r/.../comments/...	opencli reddit read <full-url>	
weibo.com/...	opencli weibo search <query>	
xiaohongshu.com/...	opencli xiaohongshu download <id>	
bilibili.com/video/BV...	opencli bilibili download <bvid>	
Dynamic Discovery

The table above covers high-frequency platforms. OpenCLI supports 80+ platforms. For anything not listed:

# See all supported platforms
opencli --help

# See subcommands for a specific platform
opencli <platform> --help

Generic Fallback Tools

For URLs that don't match a known platform, try these in order:

Tool	How to Use	Strengths	Weaknesses
Jina Reader	curl -s -H "Accept: text/markdown" "https://r.jina.ai/<url>"	Best markdown quality, JS support	20 req/min free limit
defuddle.md	curl -s "https://defuddle.md/<url>"	Good quality, by Obsidian creator	Undocumented limits
markdown.new	curl -s "https://markdown.new/<url>"	Browser rendering fallback	500 req/day
WebFetch	Built-in tool, no curl needed	No setup needed	No JS rendering, poor on complex pages
Decision Guide
Known platform with login → OpenCLI first
Static article/blog → Jina Reader first
If a tool returns too-short content (<500 chars) → likely an error page, try next tool in chain
If Jina fails or is rate-limited → defuddle → markdown.new → WebFetch
If OpenCLI fails → fall back to the generic chain above
OpenCLI Setup

If opencli is not installed:

npm i -g @jackwener/opencli
Download browser extension from https://github.com/jackwener/opencli/releases
Chrome → chrome://extensions → Developer mode → Load unpacked → select unzipped folder
opencli doctor to verify

One-time setup. After installation, known platform URLs automatically use browser login state.

Limitations
WeChat articles partially supported via opencli weixin; proxy may be needed for some URLs behind GFW
OpenCLI requires browser extension setup (one-time)
Jina Reader free tier: 20 req/min
markdown.new: 500 req/day/IP
Weekly Installs
45
Repository
jiahao-shao1/sjh-skills
GitHub Stars
14
First Seen
Mar 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
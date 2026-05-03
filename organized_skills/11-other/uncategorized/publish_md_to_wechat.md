---
rating: ⭐⭐⭐
title: publish-md-to-wechat
url: https://skills.sh/walk4rever/publish-md-to-wechat/publish-md-to-wechat
---

# publish-md-to-wechat

skills/walk4rever/publish-md-to-wechat/publish-md-to-wechat
publish-md-to-wechat
Installation
$ npx skills add https://github.com/walk4rever/publish-md-to-wechat --skill publish-md-to-wechat
SKILL.md
publish-md-to-wechat

Publishes Markdown articles to WeChat Official Account drafts with professional visual styling, automatic image handling, and cover generation.

Phase 1: Environment & Credentials

Check dependencies:

ls .venv/bin/python 2>/dev/null || echo "MISSING"


If .venv is missing, run ./install.sh.

Credentials: Loaded automatically from .env in the current directory, or ~/.config/publish-md-to-wechat/.env as global fallback. Only ask the user for credentials if the script explicitly fails with an auth error.

Phase 2: Read the Article & Select a Style

Read the Markdown file to understand the content's tone. Then pick a style.

List all styles:

.venv/bin/python3 scripts/styles.py --list


Style selection guide:

Category	Styles	When to use
⭐ Core	swiss, editorial, ink	Default choice. Covers 90% of content types.
📦 Extend	notebook, geometry, botanical, terminal, bold, cyber, voltage	Specific scenarios only.
🎨 Custom	custom-xxx	User-created from WeChat article analysis.

Core trio quick guide:

swiss — Technical articles, tutorials, reports, official announcements
editorial — Opinion pieces, analysis, blog posts, personal brands
ink — Humanities, culture, deep dives, literary content

Propose the style with a one-line reason. Skip if the user already specified.

Phase 3: Validate First (Recommended for complex articles)
.venv/bin/python3 scripts/wechat_publisher.py \
  --md [PATH] --style [STYLE] --dry-run --out-html /tmp/preview.html
open /tmp/preview.html

Phase 4: Publish
.venv/bin/python3 scripts/wechat_publisher.py \
  --md [PATH] --style [STYLE]


Key flags:

--thumb [PATH] — Custom cover (auto-generates if omitted)
--title "[TITLE]" — Override title (auto-detects from frontmatter/H1)
--no-verify-ssl — For SSL cert issues
-v — Verbose logging

YAML Frontmatter: Title, author, description auto-extracted:

---
title: Article Title
author: Author Name
description: Short summary for WeChat article list.
---

Phase 5: Success Output
## 🚀 发布成功！

| 字段 | 值 |
|------|-----|
| **标题** | [Title] |
| **风格** | `[style]` — [one-line description] |
| **Media ID** | `[MEDIA_ID]` |

**下一步：** mp.weixin.qq.com → 草稿箱 → 预览 → 发布

Custom Styles
# Create from WeChat article
.venv/bin/python3 scripts/styles.py --url https://mp.weixin.qq.com/s/xxx --no-verify-ssl

# Rename
.venv/bin/python3 scripts/styles.py --rename custom-old custom-new

# Use
.venv/bin/python3 scripts/wechat_publisher.py --md article.md --style custom-xxx

Troubleshooting
Error	Fix
40164 IP whitelist	Add IP at mp.weixin.qq.com → 设置与开发 → IP白名单
40125 / 40013 Invalid credentials	Check .env
45009 Rate limit	Auto-retries; wait if persists
SSL errors	Add --no-verify-ssl
Image not found	Check filename (case-sensitive), ensure image is in article directory
Cover failed	Falls back to assets/default_thumb.png; or use --thumb
Missing dependencies	Run ./install.sh
Weekly Installs
40
Repository
walk4rever/publ…o-wechat
GitHub Stars
3
First Seen
Mar 2, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
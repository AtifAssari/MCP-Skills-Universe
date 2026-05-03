---
rating: ⭐⭐⭐
title: md2wechat-lite
url: https://skills.sh/geekjourneyx/md2wechat-lite/md2wechat-lite
---

# md2wechat-lite

skills/geekjourneyx/md2wechat-lite/md2wechat-lite
md2wechat-lite
Installation
$ npx skills add https://github.com/geekjourneyx/md2wechat-lite --skill md2wechat-lite
SKILL.md
md2wx - Markdown to WeChat

CLI tool for converting Markdown to WeChat Official Account formatted drafts.

Quick start

Install:

curl -fsSL https://raw.githubusercontent.com/geekjourneyx/md2wechat-lite/main/cli/scripts/install.sh | sh


Configure credentials:

md2wx config set wechat-appid "wx123..."
md2wx config set wechat-appsecret "your_secret"
md2wx config set api-key "wme_your_key"

Commands
Command	Purpose
article-draft	Create article draft from Markdown
newspic-draft	Create Xiaolvshu (image card) draft
batch-upload	Upload images to WeChat CDN
themes list	List available themes
config	Manage settings (set/get/list/path)
Article draft

Convert Markdown to WeChat article:

md2wx article-draft --file article.md --theme bytedance --cover-image "https://cdn.example.com/cover.jpg"


Or pass inline Markdown:

md2wx article-draft --markdown "# Title\n\nContent" --theme elegant-red --cover-image "https://cdn.example.com/cover.jpg"


Note:

article-draft does not read from stdin pipe directly.
For API compatibility, always provide --cover-image with a public URL.
Newspic draft

Create image-rich card drafts:

md2wx newspic-draft --title "标题" --content "内容" --images "https://cdn.example.com/img1.jpg,https://cdn.example.com/img2.png"

Batch upload

Upload images and get WeChat CDN URLs:

md2wx batch-upload --images "https://cdn.example.com/a.jpg,https://cdn.example.com/b.jpg"


Image input constraints:

API accepts public image URLs only.
Local file paths and glob patterns are not supported.
Themes

Built-in (6): default, bytedance, chinese, apple, sports, cyber

Template (32): {minimal|focus|elegant|bold}-{gold|green|blue|orange|red|navy|gray|sky}

List/search themes:

md2wx themes list [--verbose] [--search query]


For theme descriptions: See cli/pkg/themes/list.go

Configuration

Config file: ~/.md2wx/config.yaml (stored as key=value lines)

Priority: Command args > Environment vars > Config file > Defaults

Environment variables:

MD2WX_WECHAT_APPID
MD2WX_WECHAT_APPSECRET
MD2WX_API_KEY
MD2WX_API_BASE_URL
MD2WX_DEFAULT_THEME
MD2WX_BACKGROUND_TYPE
MD2WX_FONT_SIZE
Project structure
cli/
├── main.go              # Root command
├── article-draft.go     # Article draft
├── newspic-draft.go     # Xiaolvshu draft
├── batch-upload.go      # Image upload
├── config.go            # Config management
├── themes.go            # Theme list command
└── pkg/
    ├── api/client.go    # HTTP API client
    ├── config/          # Config file I/O
    ├── themes/          # Theme definitions
    └── output/          # JSON formatter

Output format

All commands output JSON:

{
  "success": true,
  "data": { "media_id": "...", "url": "..." }
}

Implementation details
Zero dependencies (except cobra): Manual key=value config parsing
Go 1.24+ required
Single binary distribution

See source files for:

API client: cli/pkg/api/client.go
Config handling: cli/pkg/config/config.go
Theme list: cli/pkg/themes/list.go
Weekly Installs
14
Repository
geekjourneyx/md…hat-lite
GitHub Stars
75
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketFail
SnykFail
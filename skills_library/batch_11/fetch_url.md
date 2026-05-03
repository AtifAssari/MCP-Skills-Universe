---
title: fetch-url
url: https://skills.sh/dcjanus/prompts/fetch-url
---

# fetch-url

skills/dcjanus/prompts/fetch-url
fetch-url
Installation
$ npx skills add https://github.com/dcjanus/prompts --skill fetch-url
SKILL.md

在当前文件所在目录运行：./scripts/fetch_url.py URL（仅支持 http / https）。
说明：必须直接当作可执行文件执行。

脚本调用方式示例（不要用 uv run python 或 python）：

cd skills/fetch-url && ./scripts/fetch_url.py https://example.com --output ./page.md


错误示例：

uv run python skills/fetch-url/scripts/fetch_url.py https://example.com --output ./page.md
python skills/fetch-url/scripts/fetch_url.py https://example.com --output ./page.md


默认自动探测本地 Chromium 系浏览器路径；未探测到时需安装 Playwright 浏览器：

uv run playwright install chromium


参数：

--output：将输出写入文件（默认 stdout）。
--timeout-ms：Playwright 导航超时（毫秒，默认 60000）。
--browser-path：指定本地 Chromium 系浏览器路径（默认自动探测）。
--output-format：输出格式（默认 markdown），支持 csv、html、json、markdown、raw-html、txt、xml、xmltei；raw-html 直接输出渲染后的 HTML（不经 trafilatura）。
--fetch-strategy：仅 markdown 可用，支持 auto、agent、jina、browser。默认 auto。

--fetch-strategy 常用值：

auto：默认选择。
agent：优先用原站 Markdown 协商。
jina：优先用 Jina Reader。
browser：直接用本地 Playwright。

环境变量：

可设置 JINA_API_KEY 提升 Jina Reader 限流：JINA_API_KEY=your-token ./scripts/fetch_url.py ...

示例：

./scripts/fetch_url.py https://example.com --output ./page.md --timeout-ms 60000
./scripts/fetch_url.py https://example.com --fetch-strategy jina
JINA_API_KEY=your-token ./scripts/fetch_url.py https://example.com --fetch-strategy jina
./scripts/fetch_url.py https://example.com --fetch-strategy browser
./scripts/fetch_url.py https://x.com/jack/status/20 --output-format markdown
./scripts/fetch_url.py https://x.com/jack/status/20 --output-format markdown --fetch-strategy browser


Reference：scripts/fetch_url.py

Weekly Installs
32
Repository
dcjanus/prompts
GitHub Stars
19
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
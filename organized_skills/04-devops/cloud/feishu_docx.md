---
rating: ⭐⭐⭐
title: feishu-docx
url: https://skills.sh/leemysw/agent-kit/feishu-docx
---

# feishu-docx

skills/leemysw/agent-kit/feishu-docx
feishu-docx
Installation
$ npx skills add https://github.com/leemysw/agent-kit --skill feishu-docx
Summary

Convert Feishu/Lark cloud documents to Markdown for AI analysis and processing.

Supports four document types: docx (with embedded images), sheets, bitable, and wiki pages, all exported as Markdown
Includes CLI commands for export, OAuth setup, and credential management; also offers Python API for direct content retrieval
Can output to files or stdout, with automatic image downloading and optional Markdown table formatting
Token caching and auto-refresh eliminate re-authorization; supports both Feishu and Lark (overseas) instances
SKILL.md
Feishu Docx Exporter

Export Feishu/Lark cloud documents to Markdown format for AI analysis.

Instructions
Setup (One-time)
Install the tool:
pip install feishu-docx

Configure Feishu app credentials:
feishu-docx config set --app-id YOUR_APP_ID --app-secret YOUR_APP_SECRET
# or use environment variables

Authorize with OAuth (opens browser):
feishu-docx auth

Export Documents

Export any Feishu document URL to Markdown:

feishu-docx export "<FEISHU_URL>" -o ./output


The exported Markdown file will be saved with the document's title as filename.

Supported Document Types
docx: Feishu cloud documents → Markdown with images
sheet: Spreadsheets → Markdown tables
bitable: Multidimensional tables → Markdown tables
wiki: Knowledge base nodes → Auto-resolved and exported
Examples
Export a wiki page
feishu-docx export "https://xxx.feishu.cn/wiki/ABC123" -o ./docs

Export a document with custom filename
feishu-docx export "https://xxx.feishu.cn/docx/XYZ789" -o ./docs -n meeting_notes

Export spreadsheet as Markdown table
feishu-docx export "https://xxx.feishu.cn/sheets/DEF456" --table md

Read content directly (recommended for AI Agent)
# Output content to stdout instead of saving to file
feishu-docx export "https://xxx.feishu.cn/wiki/ABC123" --stdout
# or use short flag
feishu-docx export "https://xxx.feishu.cn/wiki/ABC123" -c

Read content without saving to file (Python)
from feishu_docx import FeishuExporter

exporter = FeishuExporter(app_id="xxx", app_secret="xxx")
content = exporter.export_content("https://xxx.feishu.cn/wiki/xxx")
print(content)

Command Reference
Command	Description
feishu-docx export <URL>	Export document to Markdown
feishu-docx auth	OAuth authorization
feishu-docx config set	Set credentials
feishu-docx config show	Show current config
feishu-docx config clear	Clear token cache
Tips
Images are automatically downloaded to a folder named after the document
Use --table md for Markdown tables instead of HTML
Token is cached and auto-refreshed, no need to re-authorize
For Lark (overseas), add --lark flag
Weekly Installs
301
Repository
leemysw/agent-kit
GitHub Stars
46
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail
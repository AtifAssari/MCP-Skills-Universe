---
title: firecrawl-parse
url: https://skills.sh/firecrawl/cli/firecrawl-parse
---

# firecrawl-parse

skills/firecrawl/cli/firecrawl-parse
firecrawl-parse
Installation
$ npx skills add https://github.com/firecrawl/cli --skill firecrawl-parse
SKILL.md
firecrawl parse

Turn a local document into clean markdown on disk. Supports PDF, DOCX, DOC, ODT, RTF, XLSX, XLS, HTML/HTM/XHTML.

When to use
You have a file on disk (not a URL) and want its text as markdown
User drops a PDF/DOCX and asks what it says, or to summarize it
Use scrape instead when the source is a URL
Quick start

Always save to .firecrawl/ with -o — parsed docs can be hundreds of KB and blow up context if streamed to stdout. Add .firecrawl/ to .gitignore.

mkdir -p .firecrawl

# File → markdown
firecrawl parse ./paper.pdf -o .firecrawl/paper.md

# AI summary
firecrawl parse ./paper.pdf -S -o .firecrawl/paper-summary.md

# Ask a question about the doc
firecrawl parse ./paper.pdf -Q "What are the main conclusions?" \
  -o .firecrawl/paper-qa.md


Then head, grep, rg etc., or incrementally read the file - don't load the whole thing at once.

Options
Option	Description
-S, --summary	AI-generated summary
-Q, --query <prompt>	Ask a question about the parsed content
-o, --output <path>	Output file path — always use this
-f, --format <fmt>	markdown (default), html, summary
--timeout <ms>	Timeout for the parse job
--timing	Show request duration
Tips
Quote paths with spaces: firecrawl parse "./My Doc.pdf" -o .firecrawl/mydoc.md.
Max upload size: 50 MB per file.
Credits: ~1 per PDF page; HTML is 1 flat.
Check .firecrawl/ before re-parsing the same file.
To check your credit balance (recommended for batch processing and similar workflows), use the firecrawl credit-usage command.
See also
firecrawl-scrape — same idea for URLs
Weekly Installs
3.9K
Repository
firecrawl/cli
GitHub Stars
362
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass
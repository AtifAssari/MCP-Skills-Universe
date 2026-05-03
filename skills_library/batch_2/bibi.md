---
title: bibi
url: https://skills.sh/jimmylv/bibigpt-skill/bibi
---

# bibi

skills/jimmylv/bibigpt-skill/bibi
bibi
Installation
$ npx skills add https://github.com/jimmylv/bibigpt-skill --skill bibi
Summary

Summarize videos, audio, and podcasts directly from the terminal using BibiGPT.

Supports YouTube, Bilibili, podcasts, and other media URLs with multiple output formats: Markdown, JSON, raw subtitles, or chapter-by-chapter breakdowns
Requires BibiGPT desktop app with active login or BIBI_API_TOKEN environment variable for authentication
Includes async mode for long videos (>30 min) to avoid timeouts, plus commands for checking auth status, managing tokens, and self-updating
Output streams to stdout (summaries) and stderr (progress), enabling piping to files or tools like jq for structured data extraction
SKILL.md
BibiGPT — AI Video & Audio Summarizer
Environment Check

Run scripts/bibi-check.sh first. It detects which mode is available:

Mode	When to use	Auth
CLI (bibi command)	macOS / Windows / Linux with desktop app	Desktop login or BIBI_API_TOKEN
OpenAPI (HTTP calls)	Containers, CI, or any env without CLI	BIBI_API_TOKEN only

If neither mode is available, see references/installation.md for setup instructions.

Intent Routing

Route the user's request to the appropriate workflow:

User Intent	Workflow
Summarize a video/audio URL	→ workflows/quick-summary.md
Chapter-by-chapter breakdown, detailed analysis	→ workflows/deep-dive.md
Get subtitles, extract transcript, raw text	→ workflows/transcript-extract.md
Turn into article, blog post, 公众号图文, 小红书	→ workflows/article-rewrite.md
Process multiple URLs, batch summarize	→ workflows/batch-process.md
Research a topic across multiple videos	→ workflows/research-compile.md
Save to Notion, Obsidian, export notes	→ workflows/export-notes.md
Analyze visual content, slides, on-screen text	→ workflows/visual-analysis.md
Disambiguation
If the user's intent matches more than one workflow, ask one clarifying question before routing.
If it matches none, ask what they are trying to accomplish. Do not guess.
If the user just pastes a URL with no context, default to workflows/quick-summary.md.
Local File Support

The bibi CLI directly accepts local file paths (no upload needed):

bibi summarize "/path/to/video.mp4"
bibi summarize "/path/to/podcast.mp3"


For API mode (no CLI), guide the user to upload the file to a publicly accessible URL (OSS, S3, etc.) first, then pass that URL to the API. See references/supported-platforms.md for details.

Direct CLI Operations

Use progressive help to discover options: bibi --help → bibi summarize --help → run.

For simple, single-command requests that don't need a full workflow:

bibi summarize "<URL>"              # Quick summary (URL or local file path)
bibi summarize "<URL>" --chapter    # Chapter summary
bibi summarize "<URL>" --subtitle   # Transcript only
bibi summarize "<URL>" --json       # Full JSON response
bibi auth check                     # Check auth status


See references/cli.md for all commands and flags.

References
Document	Contents
references/cli.md	All CLI commands, flags, output formats
references/api.md	OpenAPI endpoints, curl examples, response schemas
references/installation.md	Desktop app install, skill install, auth setup, MCP config
references/supported-platforms.md	Supported URL types, platform notes, duration limits
Weekly Installs
890
Repository
jimmylv/bibigpt-skill
GitHub Stars
62
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykWarn
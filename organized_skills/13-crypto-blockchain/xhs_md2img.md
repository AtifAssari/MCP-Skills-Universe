---
rating: ⭐⭐⭐
title: xhs-md2img
url: https://skills.sh/site/skills.volces.com/xhs-md2img
---

# xhs-md2img

skills/skills.volces.com/xhs-md2img
xhs-md2img
$ npx skills add https://skills.volces.com/skills/clawhub/zhang122994917
SKILL.md
xhs-md2img

Convert Markdown text into beautiful Xiaohongshu (XHS) style card images. Supports 5 color themes, automatic pagination, smart LLM-powered title extraction, and AI-generated decorative backgrounds.

Overview

This skill renders Markdown content as multi-page card images optimized for Xiaohongshu (Little Red Book) posts. It handles the full pipeline from raw text to publish-ready PNG images.

Use cases:

Convert long-form content into XHS-ready multi-image posts
Generate styled card images from Markdown articles
Create visually appealing social media graphics with AI backgrounds
Quick Start

Minimal input — just provide Markdown text:

{
  "markdown": "## 5个提升效率的方法\n\n**1. 番茄工作法** — 25分钟专注 + 5分钟休息\n\n**2. 任务批处理** — 把相似的事情集中做\n\n> 效率不是做更多的事，而是用更少的时间做对的事。"
}


This produces a single card image with the default (white) theme.

Input Parameters

See templates/input-schema.json for the full JSON Schema. Key parameters:

Parameter	Type	Default	Description
markdown	string	(required)	Markdown content. Use --- for manual page breaks.
title	string	(auto-extracted)	Cover title. If omitted, LLM extracts one from content.
author	string	—	Author name shown on cover.
description	string	—	Cover subtitle/description.
theme	enum	"default"	Color theme: default, monokai, nord, sakura, mint.
font_family	enum	"sans-serif"	Font: sans-serif, serif, wenkai.
padding	enum	"medium"	Card padding: small, medium, large.
show_cover	boolean	true	Whether to show cover block.
bg_style	enum	"ai_art"	Background: ai_art (AI-generated) or none (solid color).
Rendering Pipeline

The rendering pipeline has 5 stages:

1. Smart Format (LLM)

If the input is plain text (not already Markdown), the LLM reformats it:

Title extraction: Extracts a short, punchy cover title (10-20 chars)
Body formatting: Adds Markdown structure (## headings, **bold**, - lists, > quotes)
Constraint: The LLM is strictly forbidden from modifying any original text content — it can only add Markdown formatting marks

The LLM prompt enforces: all emojis, hashtags, special symbols, and wording must be preserved verbatim. Only Markdown formatting (##, **, -, >, blank lines) may be added.

2. Markdown to HTML

Uses python-markdown with extensions:

tables, fenced_code, codehilite (Pygments), nl2br, sane_lists, smarty, attr_list, md_in_html, toc
XHS hashtags (#tag#) are converted to styled pill badges
3. HTML/CSS Card Construction

Builds a full HTML page with CSS styling per theme. Each card is a fixed-size div (375x500px base, exported at 3x = 1125x1500px). See templates/card-template.html for the template structure.

Card structure:

.xhs-card (fixed size, background color)
├── .bg-art (optional AI background, low opacity overlay)
└── .card-inner (z-index:1, above background)
    ├── .cover-block (title, author, description — first page only)
    └── .prose-content (rendered Markdown HTML)

4. Auto-Pagination (Playwright JS)

Content that overflows a single card is automatically split across multiple pages:

Playwright measures each top-level element's height in the browser
Elements are grouped into pages that fit the card height
New card divs are created in the DOM with cloned background art
Page numbers (1 / N) are added to each card
The last card is shrunk to fit its content (avoids large empty space)
5. Screenshot & Upload

Each .xhs-card div is screenshotted as PNG via Playwright. Images are uploaded to Alibaba Cloud OSS if configured, otherwise returned as base64 data URIs.

Theme System

5 built-in themes with carefully tuned palettes. See references/themes.md for full hex values.

Theme	Background	Feel
default	White #ffffff	Clean, professional
monokai	Dark #272822	Tech, developer-oriented
nord	Deep blue #2e3440	Nordic minimalist
sakura	Soft pink #fff5f5	Warm, feminine
mint	Light green #f0faf4	Fresh, natural
AI Background Generation

When bg_style: "ai_art", the skill generates a subtle decorative background image:

Prompt generation: LLM creates an image prompt based on the card's text content and theme
Image generation: Routes to one of two providers automatically:
Gemini (if LLM_API_KEY points to googleapis.com): Native Gemini API, returns base64 data URI, synchronous
DashScope wanx (if DASHSCOPE_API_KEY is set): Async submit + poll, returns URL
Compositing: Background is overlaid at very low opacity (8-18% depending on theme) behind the card content

See references/api-reference.md for API details.

Prompt constraints: Generated backgrounds are always abstract decorative elements (watercolor, bokeh, geometric lines, plant silhouettes) — never text, faces, or specific objects.

Output Format
{
  "__type": "xhs_card_images",
  "title": "Extracted or provided title",
  "theme": "default",
  "total_pages": 3,
  "pages": [
    {
      "index": 0,
      "page": 1,
      "total_pages": 3,
      "width": 1125,
      "height": 1500,
      "size_bytes": 123456,
      "url": "https://...",
      "oss_uploaded": true
    }
  ]
}


If OSS is not configured, each page includes data_uri instead of url, with oss_uploaded: false.

Privacy & External Endpoints

This skill makes network calls to:

Endpoint	Purpose	Data sent
LLM API (configurable)	Smart formatting, BG prompt generation	Text content (title + body summary)
DashScope wanx API	AI background image generation	English image prompt (no user content)
Gemini API	AI background image generation (alternative)	English image prompt (no user content)
Alibaba Cloud OSS	Image upload (optional)	Generated PNG images

No user content is sent to image generation APIs — only LLM-generated English art prompts describing abstract decorative elements.

Weekly Installs
21
Source
skills.volces.c…22994917
First Seen
Mar 12, 2026
Security Audits
SocketPass
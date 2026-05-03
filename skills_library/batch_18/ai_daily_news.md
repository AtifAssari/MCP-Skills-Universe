---
title: ai-daily-news
url: https://skills.sh/geekjourneyx/ai-daily-skill/ai-daily-news
---

# ai-daily-news

skills/geekjourneyx/ai-daily-skill/ai-daily-news
ai-daily-news
Installation
$ npx skills add https://github.com/geekjourneyx/ai-daily-skill --skill ai-daily-news
SKILL.md
AI Daily News

Fetches AI industry news from smol.ai, intelligently summarizes and categorizes using built-in Claude AI capabilities, outputs structured markdown, and optionally generates themed webpages and shareable card images.

Quick Start
# Yesterday's news
昨天AI资讯

# Specific date
2026-01-13的AI新闻

# By category
昨天的模型发布相关资讯

# Generate webpage
昨天AI资讯，生成网页

# Generate shareable card image
昨天AI资讯，生成分享图片
生成日报卡片图片

Supported Query Types
Type	Examples	Description
相对日期	"昨天AI资讯" "前天的新闻" "今天的AI动态"	Yesterday, day before, today
绝对日期	"2026-01-13的新闻"	YYYY-MM-DD format
分类筛选	"模型相关资讯" "产品动态"	Filter by category
网页生成	"生成网页" "制作HTML页面"	Optional webpage generation
图片生成	"生成图片" "生成分享卡片" "制作日报卡片"	Generate shareable card image
Workflow

Copy this checklist to track progress:

Progress:
- [ ] Step 1: Parse date from user request
- [ ] Step 2: Fetch RSS from smol.ai
- [ ] Step 3: Check if content exists for target date
- [ ] Step 4: Extract and analyze content
- [ ] Step 5: Generate structured markdown
- [ ] Step 6: Ask about webpage generation (if requested)
- [ ] Step 7: Generate shareable card image (if requested)

Step 1: Parse Date

Extract the target date from user request.

User Input	Target Date	Calculation
"昨天AI资讯"	Yesterday	today - 1 day
"前天AI资讯"	Day before yesterday	today - 2 days
"2026-01-13的新闻"	2026-01-13	Direct parse
"今天的AI动态"	Today	Current date

Date format: Always use YYYY-MM-DD format (e.g., 2026-01-13)

Step 2: Fetch RSS

Run the fetch script to get RSS data:

python plugins/ai-daily/skills/ai-daily/scripts/fetch_news.py


This downloads and parses https://news.smol.ai/rss.xml, returning structured JSON.

Available dates can be checked with:

python plugins/ai-daily/skills/ai-daily/scripts/fetch_news.py --date-range

Step 3: Check Content

Verify if content exists for the target date.

When Content Exists

Continue to Step 4.

When Content NOT Found

Display a friendly message with available dates:

抱歉，2026-01-14 暂无资讯

可用日期范围: 2026-01-10 ~ 2026-01-13

建议:
- 查看 [2026-01-13](command:查看2026-01-13的资讯) 的资讯
- 查看 [2026-01-12](command:查看2026-01-12的资讯) 的资讯


User experience principles:

Clear problem statement
Show available alternatives
Provide clickable commands for quick access
Never leave user stuck with no options
Step 4: Extract and Analyze Content

Use built-in Claude AI capabilities to:

Extract full content from the RSS entry
Generate summary - 3-5 key takeaways
Categorize items by topic:
Model Releases (模型发布)
Product Updates (产品动态)
Research Papers (研究论文)
Tools & Frameworks (工具框架)
Funding & M&A (融资并购)
Industry Events (行业事件)
Extract keywords - Companies, products, technologies

Prompt Template:

Analyze this AI news content and organize it:

1. Generate 3-5 key takeaways (one sentence each)
2. Categorize items into: Model Releases, Product Updates, Research, Tools, Funding, Events
3. Extract 5-10 keywords

Original content:
{content}

Step 5: Generate Markdown

Output structured markdown following the format in output-format.md.

Key sections:

Title with date
Core summary
Categorized news items
Keywords
Footer with source info

Example output:

# AI Daily · 2026年1月13日

## 核心摘要

- Anthropic 发布 Cowork 统一 Agent 平台
- Google 开源 MedGemma 1.5 医疗多模态模型
- LangChain Agent Builder 正式发布

## 模型发布

### MedGemma 1.5
Google 发布 4B 参数医疗多模态模型...
[原文链接](https://news.smol.ai/issues/26-01-13-not-much/)

## 产品动态

...

## 关键词

#Anthropic #Google #MedGemma #LangChain

---
数据来源: smol.ai

Step 6: Webpage Generation (Optional)

Only trigger when user explicitly says:

"生成网页"
"制作HTML页面"
"生成静态网站"
Ask User Preferences
是否需要生成精美的网页？

可选主题:
- [苹果风](command:使用苹果风主题) - 简洁专业，适合技术内容
- [深海蓝](command:使用深海蓝主题) - 商务风格，适合产品发布
- [秋日暖阳](command:使用秋日暖阳主题) - 温暖活力，适合社区动态

Theme Prompt Templates

See html-themes.md for detailed prompt templates for each theme.

Apple Style Theme (Key Points):

Generate a clean, minimalist HTML page inspired by Apple's design:

**Design**:
- Pure black background (#000000)
- Subtle blue glow from bottom-right (#0A1929 → #1A3A52)
- Generous white space, content density ≤ 40%
- SF Pro Display for headings, SF Pro Text for body
- Smooth animations and hover effects

**Structure**:
- Header: Logo icon + Date badge
- Main: Summary card + Category sections
- Footer: Keywords + Copyright

**Colors**:
- Title: #FFFFFF
- Body: #E3F2FD
- Accent: #42A5F5
- Secondary: #B0BEC5

Save Webpage

Save to docs/{date}.html:

# Save webpage
cat > docs/2026-01-13.html << 'EOF'
{generated_html}
EOF

Step 7: Shareable Card Image Generation (Optional)

Trigger when user explicitly requests:

"生成图片"
"生成分享卡片"
"制作日报卡片"
"生成卡片图片"
"生成分享图"
Image Generation Process

Build condensed Markdown for card display:

Title and date
Core summary (3-5 items)
Top items per category (3 items each)
Keywords

Call Firefly Card API:

API: POST https://fireflycard-api.302ai.cn/api/saveImg
Body contains content field with Markdown
Returns binary image stream (Content-Type: image/png)

Save and display result:

Save to docs/images/{date}.png
Display preview or download link
API Request Format
{
  "content": "# AI Daily\\n## 2026年1月13日\\n...",
  "font": "SourceHanSerifCN_Bold",
  "align": "left",
  "width": 400,
  "height": 533,
  "fontScale": 1.2,
  "ratio": "3:4",
  "padding": 30,
  "switchConfig": {
    "showIcon": false,
    "showTitle": false,
    "showContent": true,
    "showTranslation": false,
    "showAuthor": false,
    "showQRCode": false,
    "showSignature": false,
    "showQuotes": false,
    "showWatermark": false
  },
  "temp": "tempBlackSun",
  "textColor": "rgba(0,0,0,0.8)",
  "borderRadius": 15,
  "color": "pure-ray-1"
}

Output Example
📸 分享卡片已生成

图片已保存到: docs/images/2026-01-13.png

[预览图片](docs/images/2026-01-13.png)

你可以将此图片分享到社交媒体！

Configuration

No configuration required. Uses built-in RSS fetching and Claude AI capabilities.

RSS Source: https://news.smol.ai/rss.xml

Date Calculation: Uses current UTC date, subtracts days for relative queries.

Complete Examples
Example 1: Yesterday's News (Basic)

User Input: "昨天AI资讯"

Process:

Calculate yesterday's date: 2026-01-14
Fetch RSS
Check content exists
Analyze and categorize
Output markdown

Output: Structured markdown with all categories

Example 2: Specific Date

User Input: "2026-01-13的AI新闻"

Process:

Parse date: 2026-01-13
Fetch RSS
Check content exists
Analyze and categorize
Output markdown
Example 3: By Category

User Input: "昨天的模型发布相关资讯"

Process:

Calculate yesterday's date
Fetch RSS
Analyze and filter for "Model Releases" category
Output filtered markdown
Example 4: With Webpage Generation

User Input: "昨天AI资讯，生成网页"

Process: 1-5. Same as Example 1 6. Ask: "Which theme?" 7. User selects: "苹果风" 8. Generate HTML with Apple-style theme 9. Save to docs/2026-01-14.html

Example 5: Content Not Found

User Input: "2026-01-15的资讯"

Output:

抱歉，2026-01-15 暂无资讯

可用日期范围: 2026-01-10 ~ 2026-01-13

建议:
- 查看 [2026-01-13](command:查看2026-01-13的资讯) 的资讯
- 查看 [2026-01-12](command:查看2026-01-12的资讯) 的资讯

References
Output Format - Markdown output structure
HTML Themes - Webpage theme prompts
Troubleshooting
RSS Fetch Fails

Error: "Failed to fetch RSS"

Solution: Check network connectivity to news.smol.ai

Date Parsing Fails

Error: "Invalid date format"

Solution: Use YYYY-MM-DD format or relative terms like "昨天"

No Content for Date

Output: Friendly message with available dates (see Step 3)

Webpage Save Fails

Error: "Cannot save to docs/"

Solution: Ensure docs/ directory exists:

mkdir -p docs

CLI Reference
# Fetch RSS (returns JSON)
python plugins/ai-daily/skills/ai-daily/scripts/fetch_news.py

# Get available date range
python plugins/ai-daily/skills/ai-daily/scripts/fetch_news.py --date-range

# Get specific date content
python plugins/ai-daily/skills/ai-daily/scripts/fetch_news.py --date 2026-01-13

Weekly Installs
46
Repository
geekjourneyx/ai…ly-skill
GitHub Stars
202
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
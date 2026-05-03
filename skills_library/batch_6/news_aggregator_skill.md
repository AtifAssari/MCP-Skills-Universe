---
title: news-aggregator-skill
url: https://skills.sh/cclank/news-aggregator-skill/news-aggregator-skill
---

# news-aggregator-skill

skills/cclank/news-aggregator-skill/news-aggregator-skill
news-aggregator-skill
Installation
$ npx skills add https://github.com/cclank/news-aggregator-skill --skill news-aggregator-skill
Summary

Fetch and analyze real-time news from 28 global, AI, finance, and podcast sources with deep Chinese-language reports.

Supports 28 sources across six categories: global news (Hacker News, GitHub, Weibo), AI/tech (Hugging Face Papers, newsletters), finance (WallStreetCN), podcasts, and essays
Three-step universal workflow: fetch data with keyword filtering, generate unified markdown reports in Simplified Chinese, and save to timestamped directories
Pre-configured daily briefing profiles (general, finance, tech, social, AI, reading list) for common news routines
Interactive menu mode triggered by "如意如意" command; smart keyword expansion (e.g., "AI" auto-expands to include LLM, GPT, Claude, Agent, RAG, DeepSeek)
SKILL.md
News Aggregator Skill

Fetch real-time hot news from 28 sources, generate deep analysis reports in Chinese.

🔄 Universal Workflow (3 Steps)

Every news request follows the same workflow, regardless of source or combination:

Step 1: Fetch Data
# Single source
python3 scripts/fetch_news.py --source <source_key> --no-save

# Multiple sources (comma-separated)
python3 scripts/fetch_news.py --source hackernews,github,wallstreetcn --no-save

# All sources (broad scan)
python3 scripts/fetch_news.py --source all --limit 15 --deep --no-save

# With keyword filter (auto-expand: "AI" → "AI,LLM,GPT,Claude,Agent,RAG")
python3 scripts/fetch_news.py --source hackernews --keyword "AI,LLM,GPT" --deep --no-save

Step 2: Generate Report

Read the output JSON and format every item using the Unified Report Template below. Translate all content to Simplified Chinese.

Step 3: Save & Present

Save the report to reports/YYYY-MM-DD/<source>_report.md, then display the full content to the user.

📰 Unified Report Template

All sources use this single template. Show/hide optional fields based on data availability.

#### N. [标题 (中文翻译)](https://original-url.com)
- **Source**: 源名 | **Time**: 时间 | **Heat**: 🔥 热度值
- **Links**: [Discussion](hn_url) | [GitHub](gh_url)     ← 仅在数据存在时显示
- **Summary**: 一句话中文摘要。
- **Deep Dive**: 💡 **Insight**: 深度分析（背景、影响、技术价值）。

Source-Specific Adaptations

Only the differences from the universal template:

Source	Adaptation
Hacker News	MUST include [Discussion](hn_url) link
GitHub	Use 🌟 Stars for Heat, add Lang field, add #Tags in Deep Dive
Hugging Face	Use 🔥 +N upvotes for Heat, include [GitHub](url) if present, write 深度解读 (not just translate abstract)
Weibo	Preserve exact heat text (e.g. "108万")
🛠️ Tools
fetch_news.py
Arg	Description	Default
--source	Source key(s), comma-separated. See table below.	all
--limit	Max items per source	15
--keyword	Comma-separated keyword filter	None
--deep	Download article text for richer analysis	Off
--save	Force save to reports dir	Auto for single source
--outdir	Custom output directory	reports/YYYY-MM-DD/
Available Sources (28)
Category	Key	Name
Global News	hackernews	Hacker News
	36kr	36氪
	wallstreetcn	华尔街见闻
	tencent	腾讯新闻
	weibo	微博热搜
	v2ex	V2EX
	producthunt	Product Hunt
	github	GitHub Trending
AI/Tech	huggingface	HF Daily Papers
	ai_newsletters	All AI Newsletters (aggregate)
	bensbites	Ben's Bites
	interconnects	Interconnects (Nathan Lambert)
	oneusefulthing	One Useful Thing (Ethan Mollick)
	chinai	ChinAI (Jeffrey Ding)
	memia	Memia
	aitoroi	AI to ROI
	kdnuggets	KDnuggets
Podcasts	podcasts	All Podcasts (aggregate)
	lexfridman	Lex Fridman
	80000hours	80,000 Hours
	latentspace	Latent Space
Essays	essays	All Essays (aggregate)
	paulgraham	Paul Graham
	waitbutwhy	Wait But Why
	jamesclear	James Clear
	farnamstreet	Farnam Street
	scottyoung	Scott Young
	dankoe	Dan Koe
daily_briefing.py (Morning Routines)

Pre-configured multi-source profiles:

python3 scripts/daily_briefing.py --profile <profile>

Profile	Sources	Instruction File
general	HN, 36Kr, GitHub, Weibo, PH, WallStreetCN	instructions/briefing_general.md
finance	WallStreetCN, 36Kr, Tencent	instructions/briefing_finance.md
tech	GitHub, HN, Product Hunt	instructions/briefing_tech.md
social	Weibo, V2EX, Tencent	instructions/briefing_social.md
ai_daily	HF Papers, AI Newsletters	instructions/briefing_ai_daily.md
reading_list	Essays, Podcasts	(Use universal template)

Workflow: Execute script → Read corresponding instruction file → Generate report following both the instruction file AND the universal template.

⚠️ Rules (Strict)
Language: ALL output in Simplified Chinese (简体中文). Keep well-known English proper nouns (ChatGPT, Python, etc.).
Time: MANDATORY field. Never skip. If missing in JSON, mark as "Unknown Time". Preserve "Real-time" / "Today" / "Hot" as-is.
Anti-Hallucination: Only use data from the JSON. Never invent news items. Use simple SVO sentences. Do not fabricate causal relationships.
Smart Keyword Expansion: When user says "AI" → auto-expand to "AI,LLM,GPT,Claude,Agent,RAG,DeepSeek". Similar expansions for other domains.
Smart Fill: If results < 5 items in a time window, supplement with high-value items from wider range. Mark supplementary items with ⚠️.
Save: Always save report to reports/YYYY-MM-DD/ before displaying.
📋 Interactive Menu

When the user says "如意如意" or asks for "menu/help":

Read templates.md
Display the menu
Execute the user's selection using the Universal Workflow above
Requirements
Python 3.8+, pip install -r requirements.txt
Playwright (for HF Papers & Ben's Bites): playwright install chromium
Weekly Installs
5.0K
Repository
cclank/news-agg…or-skill
GitHub Stars
1.0K
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn
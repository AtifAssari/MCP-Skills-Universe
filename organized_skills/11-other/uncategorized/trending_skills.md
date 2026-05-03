---
rating: ⭐⭐⭐
title: trending-skills
url: https://skills.sh/geekjourneyx/trending-skills/trending-skills
---

# trending-skills

skills/geekjourneyx/trending-skills/trending-skills
trending-skills
Installation
$ npx skills add https://github.com/geekjourneyx/trending-skills --skill trending-skills
SKILL.md
Trending Skills

Fetches the latest skills rankings from skills.sh/trending, provides AI-powered skill summaries, and analyzes ranking trends (rising, falling, new entries).

Quick Start
# View today's rankings
今天技能排行榜
Top 10 skills
技能榜单

# View skill details
remotion-best-practices 是什么
frontend-design 技能介绍

# View trends
技能趋势分析
哪些技能上升了
今天有新技能吗
新晋榜单

Supported Query Types
Type	Examples	Description
今日榜单	"今天技能排行榜" "Top 10" "技能榜单"	Get current rankings
技能详情	"xxx是什么" "xxx技能介绍"	Get AI summary of a skill
趋势分析	"技能趋势" "哪些上升了"	Get trend analysis
Workflow
Progress:
- [ ] Step 1: Parse user query type
- [ ] Step 2: Fetch/Load ranking data
- [ ] Step 3: Format and display results

Step 1: Parse Query Type

Determine what the user is asking for:

User Input	Query Type	Action
"今天技能排行榜"	rankings	Show top N rankings
"Top 10 skills"	rankings	Show top N rankings
"xxx是什么"	detail	Show skill details
"哪些技能上升了"	trends	Show rising skills
"新晋榜单"	trends	Show new entries
"技能趋势分析"	trends	Show full trend report
Step 2: Fetch/Load Data
Option A: Use Database (Preferred)

If data/trends.db exists and has recent data:

# Check available dates
sqlite3 data/trends.db "SELECT date FROM skills_daily ORDER BY date DESC LIMIT 1;"

# Get latest rankings
sqlite3 data/trends.db "SELECT rank, name, owner, installs, installs_delta, rank_delta FROM skills_daily WHERE date = '2026-01-23' ORDER BY rank LIMIT 20;"

Option B: Fetch from skills.sh

If no database or data is stale:

# Run the fetcher
from src.skills_fetcher import SkillsFetcher

fetcher = SkillsFetcher()
skills = fetcher.fetch()  # Returns Top 100

Step 3: Format Results
Rankings Output Format
# 📊 Skills Trending - 2026-01-23

| # | 技能 | 拥有者 | 安装量 | 变化 |
|---|------|--------|--------|------|
| 1 | remotion-best-practices | remotion-dev/skills | 5.6K | ↑ 50 |
| 2 | vercel-react-best-practices | vercel-labs/agent-skills | 5.4K | - |
| 3 | web-design-guidelines | vercel-labs/agent-skills | 4.0K | ↓ 2 |
...

Detail Output Format
# remotion-best-practices

**拥有者**: remotion-dev/skills
**排名**: #1 (5.6K 安装)

## 简介
用 React 代码创建视频的最佳实践

## 详细说明
程序化视频生成框架 Remotion 的最佳实践集合，包含 27 个规则。

## 解决问题
- 程序化视频
- 字幕生成
- 3D 动效
- 音频处理

## 使用场景
视频自动化、个性化视频生成、数据可视化视频

**分类**: 视频/动画

🔗 https://skills.sh/remotion-dev/skills/remotion-best-practices

Trends Output Format
# 📈 技能趋势分析 - 2026-01-23

## 上升 Top 5

| # | 技能 | 变化 |
|---|------|------|
| 7 | seo-audit | ↑ 38 |
| 15 | copywriting | ↑ 12 |
...

## 下降 Top 5

| # | 技能 | 变化 |
|---|------|------|
| 10 | old-skill | ↓ 15 |
...

## 新晋榜单

- new-skill (#82)
- another-new (#95)

## 跌出榜单

- dropped-skill (昨日 #75)

Data Schema
skills_daily Table
CREATE TABLE skills_daily (
    date TEXT,           -- YYYY-MM-DD
    rank INTEGER,        -- 排名
    name TEXT,           -- 技能名称
    owner TEXT,          -- 拥有者
    installs INTEGER,    -- 安装量
    installs_delta INTEGER,  -- 安装量变化
    rank_delta INTEGER   -- 排名变化 (正=上升)
);

skills_details Table
CREATE TABLE skills_details (
    name TEXT PRIMARY KEY,
    summary TEXT,        -- 一句话摘要
    description TEXT,    -- 详细描述
    use_case TEXT,       -- 使用场景
    solves TEXT,         -- JSON: 解决的问题
    category TEXT,       -- 分类
    category_zh TEXT,    -- 中文分类
    rules_count INTEGER,
    owner TEXT,
    url TEXT
);

Configuration

Environment variables (optional, for fetching):

# For AI summaries
ZHIPU_API_KEY=your_key

# For database
DB_PATH=data/trends.db

Examples
Example 1: Today's Rankings

User Input: "今天技能排行榜"

Process:

Query type: rankings
Load latest data from database or fetch from skills.sh
Format as table

Output:

# 📊 Skills Trending - 2026-01-23

| # | 技能 | 安装量 | 变化 |
|---|------|--------|------|
| 1 | remotion-best-practices | 5.6K | - |
| 2 | vercel-react-best-practices | 5.4K | - |
...

Example 2: Skill Detail

User Input: "remotion-best-practices 是什么"

Process:

Query type: detail
Parse skill name: remotion-best-practices
Get details from database or fetch from skills.sh
Format with AI summary

Output: (See Detail Output Format above)

Example 3: Trends

User Input: "哪些技能上升了"

Process:

Query type: trends (filter: rising)
Get yesterday's data for comparison
Filter skills with rank_delta > 0
Sort by rank_delta DESC

Output:

# 📈 上升中的技能

| # | 技能 | 上升 |
|---|------|------|
| 7 | seo-audit | ↑ 38 |
| 15 | copywriting | ↑ 12 |
...

Troubleshooting
No database found

If data/trends.db doesn't exist, fetch fresh data:

from src.skills_fetcher import SkillsFetcher
from src.database import Database
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")
fetcher = SkillsFetcher()
skills = fetcher.fetch()

db = Database()
db.init_db()
db.save_today_data(today, skills)

Data is stale

If data is old, re-run main_trending.py or fetch fresh data.

CLI Reference
# Run full trending analysis
python src/main_trending.py

# Query database
sqlite3 data/trends.db "SELECT * FROM skills_daily WHERE date = '2026-01-23' ORDER BY rank;"

Weekly Installs
78
Repository
geekjourneyx/tr…g-skills
GitHub Stars
52
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
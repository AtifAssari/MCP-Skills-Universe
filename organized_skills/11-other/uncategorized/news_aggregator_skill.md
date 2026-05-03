---
rating: ⭐⭐⭐
title: news-aggregator-skill
url: https://skills.sh/huozhong-in/news-aggregator-skill/news-aggregator-skill
---

# news-aggregator-skill

skills/huozhong-in/news-aggregator-skill/news-aggregator-skill
news-aggregator-skill
Installation
$ npx skills add https://github.com/huozhong-in/news-aggregator-skill --skill news-aggregator-skill
SKILL.md
新闻聚合技能 (News Aggregator Skill)

从多个来源获取实时热点新闻。

支持的数据源
数据源	标识符	类型
Hacker News	hackernews	科技/创业
微博热搜	weibo	社会/娱乐
GitHub Trending	github	开源项目
36氪	36kr	科技/商业
Product Hunt	producthunt	产品发布
V2EX	v2ex	技术社区
腾讯新闻	tencent	综合新闻
华尔街见闻	wallstreetcn	财经
工具使用
基本命令
uv run --directory .agents/skills/news-aggregator-skill python scripts/fetch_news.py [参数]

参数说明

--source <源>: 指定数据源

单个源：hackernews, weibo, github, 36kr, producthunt, v2ex, tencent, wallstreetcn
多个源（逗号分隔）：hackernews,github,producthunt
所有源：all

--limit <数量>: 每个源返回的最大条目数（默认：10）

--keyword <关键词>: 关键词过滤（逗号分隔）

示例："AI,LLM,GPT"
不区分大小写，支持单词边界匹配

--deep: 启用深度抓取

下载并提取文章正文内容（截取前 3000 字符）
并发抓取以提高速度
结果中会包含 content 字段
输出格式

JSON 数组，每个条目包含：

source: 来源名称
title: 标题
url: 链接
heat: 热度指标（点数、回复数、星标数等）
time: 时间信息
content: 文章内容（仅在使用 --deep 时）
使用策略
1. 全局扫描（广泛获取）

适用场景：每日新闻汇总、全面了解各领域动态

# 从所有源获取，每源 15 条，启用深度抓取
uv run --directory .agents/skills/news-aggregator-skill python scripts/fetch_news.py --source all --limit 15 --deep


注意：全局扫描会返回约 120 条数据，你需要根据用户兴趣进行语义过滤和分类。

2. 单一数据源

适用场景：专注特定平台或领域

# Hacker News 前 10 条
uv run --directory .agents/skills/news-aggregator-skill python scripts/fetch_news.py --source hackernews --limit 10 --deep

# GitHub Trending 前 15 条
uv run --directory .agents/skills/news-aggregator-skill python scripts/fetch_news.py --source github --limit 15 --deep

3. 关键词搜索（智能扩展）

关键规则：自动扩展用户关键词以覆盖整个领域

用户说 "AI" → 使用："AI,LLM,GPT,Claude,DeepSeek,Gemini,机器学习,RAG,Agent,大模型"
用户说 "前端" → 使用："前端,React,Vue,Next.js,TypeScript,JavaScript,CSS,Vite"
用户说 "金融" → 使用："金融,股票,市场,经济,加密货币,比特币,黄金,A股"
# 示例：用户问 "有什么 AI 相关的新闻"
uv run --directory .agents/skills/news-aggregator-skill python scripts/fetch_news.py \
  --source hackernews,github,36kr \
  --limit 20 \
  --keyword "AI,LLM,GPT,Claude,DeepSeek,Agent,大模型" \
  --deep

4. 精确搜索

仅用于非常具体的专有名词

# 搜索 "DeepSeek" 相关新闻
uv run --directory .agents/skills/news-aggregator-skill python scripts/fetch_news.py --source all --limit 10 --keyword "DeepSeek" --deep

输出规范
报告格式要求

语言与风格：

使用简体中文
采用杂志/新闻通讯风格（如《经济学人》或 Morning Brew）
专业、简洁、引人入胜

报告结构：

头版头条（3-5 条）

跨领域最重要的新闻

科技与 AI

AI、LLM、技术相关内容的专门板块

财经/社会

其他重要类别（根据相关性）

单条新闻格式：

### 序号. [标题文本](原始URL)

**来源**：<数据源> | **时间**：<时间信息> | **热度**：<热度指标>

**核心要点**：一句话概括"所以呢？"

**深度解读**：
- 要点 1：为什么重要
- 要点 2：技术细节或背景
- 要点 3：影响和启示


关键规则：

✅ 标题必须是 Markdown 链接：[OpenAI 发布 GPT-5](https://...)
❌ 禁止纯文本标题：OpenAI 发布 GPT-5
元数据行必须包含：来源、时间、热度
深度扫描时必须提供 2-3 条解读要点
时间过滤与智能补充

当用户指定时间窗口（如"过去 X 小时"）且结果稀少（< 5 条）时：

优先用户窗口：先列出严格符合时间要求的条目
智能补充：如果列表过短，必须包含更大范围内的高价值/高热度条目（如过去 24 小时）
明确标注：清楚标记补充条目（如 "⚠️ 18h ago"、"🔥 24h 热门"）
价值优先：即使略微超出时间窗口，也要优先展示 SOTA、重大发布或高热度内容

GitHub Trending 特例：

严格返回抓取列表中的有效条目（如 Top 10）
列出所有抓取的条目
不进行智能补充
必须对每个项目进行深度分析：
核心价值：解决什么问题？为何流行？
启发思考：技术或产品洞察
场景标签：3-5 个关键词（如 #RAG #本地优先 #Rust）
输出文件
保存位置：工作区根目录的 reports/ 文件夹
文件命名：带时间戳（如 hn_news_20260131_1430.md）
完整路径示例：/Users/dio/Documents/new_vault/reports/tech_news_20260131_1430.md
用户展示：在聊天中呈现完整报告内容
交互菜单

当用户说 "news-aggregator-skill 如意如意"（或类似的"菜单/帮助"触发词）时：

读取技能目录中的 templates.md 文件
向用户展示文件中的可用命令列表
引导用户选择编号或复制命令执行
Weekly Installs
77
Repository
huozhong-in/new…or-skill
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
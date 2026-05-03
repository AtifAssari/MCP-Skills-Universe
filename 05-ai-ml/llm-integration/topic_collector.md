---
title: topic-collector
url: https://skills.sh/zephyrwang6/myskill/topic-collector
---

# topic-collector

skills/zephyrwang6/myskill/topic-collector
topic-collector
Installation
$ npx skills add https://github.com/zephyrwang6/myskill --skill topic-collector
SKILL.md
Topic Collector - AI热点采集
采集流程
多源并行采集：使用WebSearch搜索各平台内容
分类整理：按来源类型分类
提取原文链接：每条热点必须附带具体文章/帖子URL
输出结构化列表
数据源分类
一、AI博主/KOL（实践玩法、观点分享）

Twitter/X 重点账号：

@AnthropicAI - Anthropic官方
@OpenAI - OpenAI官方
@kaborsk1 - Boris Cherny（Claude Code创作者）
@swyx - AI工程师，Latent Space播客
@simonw - Simon Willison，AI工具实践
@levelsio - Pieter Levels，AI独立开发
@emaborski - Eugene Borukhovich，AI健康
@maborosi - AI自动化工作流

搜索关键词：

"Claude Code" tips OR tricks OR workflow
"Cursor" vibe coding best practices
AI agent automation n8n
Claude MCP server

二、创业公司/产品发布

Product Hunt：

搜索：AI、Developer Tools、Productivity分类
当日上榜产品
提取：产品名 + 描述 + upvotes + 产品页链接

Hacker News：

Show HN中的AI项目
Launch HN中的AI创业公司
提取：标题 + 讨论链接 + 评论数
三、AI研究员/学术动态

关注来源：

arXiv热门AI论文（被引用/讨论多的）
Google DeepMind博客
Meta AI博客
Microsoft Research

搜索关键词：

site:arxiv.org AI agent OR LLM 2026
site:deepmind.google AI research
site:ai.meta.com new paper

四、模型厂商官方动态
厂商	搜索关键词
Anthropic	site:anthropic.com OR "Claude" new feature
OpenAI	site:openai.com OR "ChatGPT" update
Google	"Gemini" update OR site:blog.google AI
xAI	"Grok" update
Mistral	site:mistral.ai
五、技术社区讨论

Reddit子版：

r/ClaudeAI
r/ChatGPT
r/LocalLLaMA
r/artificial
r/MachineLearning

Hacker News：

AI相关热门讨论
Show HN项目
聚焦领域（优先级排序）
Vibe Coding - 自然语言编程、Cursor、Claude Code
Claude生态 - Claude Skill、MCP Server、Claude Code技巧
AI Agent - 自动化工作流、n8n、Make
AI知识管理 - 第二大脑、PKM、Obsidian+AI
模型更新 - GPT、Claude、Gemini版本发布
AI新产品 - Product Hunt上榜、独立开发者作品
海外热点 - 行业大事件、收购、融资
输出格式
## 今日AI热点 - MMDD

---

### 🧑‍💻 AI博主实践分享

1. **[标题/内容摘要]**
   - 作者：@用户名
   - 原文：[具体URL](https://...)
   - 要点：一句话总结
   - 热度：❤️ likes | 🔁 retweets

---

### 🚀 创业公司/新产品

1. **[产品名]** - 一句话描述
   - 链接：[Product Hunt页面](https://producthunt.com/posts/xxx)
   - 热度：⬆️ N upvotes
   - 分类：AI / DevTools / Productivity

---

### 🔬 AI研究/学术动态

1. **[论文/博客标题]**
   - 来源：DeepMind / Meta AI / arXiv
   - 原文：[具体URL](https://...)
   - 要点：核心发现

---

### 🏢 模型厂商动态

1. **[更新/发布内容]**
   - 厂商：Anthropic / OpenAI / Google
   - 原文：[官方博客链接](https://...)
   - 要点：关键变化

---

### 💬 社区热议

1. **[讨论标题]**
   - 来源：r/ClaudeAI / Hacker News
   - 链接：[帖子URL](https://...)
   - 热度：⬆️ upvotes | 💬 comments
   - 核心观点：一句话

采集执行步骤

使用WebSearch工具，依次执行以下搜索：

# 1. AI博主动态
"Claude Code" OR "Cursor" tips tricks January 2026

# 2. Product Hunt AI产品
Product Hunt AI tools January 2026

# 3. 模型厂商更新
Anthropic Claude OR OpenAI ChatGPT update January 2026

# 4. AI Agent工作流
AI agent automation workflow n8n 2026

# 5. 社区讨论
Reddit ClaudeAI OR ChatGPT hot discussion January 2026

# 6. 研究动态
AI research breakthrough January 2026 DeepMind OR Google OR Meta

注意事项
必须提取原文链接：每条热点都要有可点击的具体URL
不采集纯学术论文（除非引发广泛讨论）
不采集重复/相似内容，合并同类
标注内容语言（中/英）
优先采集有实操价值的内容（教程、技巧、工具）
时效性：优先24小时内的内容
Weekly Installs
75
Repository
zephyrwang6/myskill
GitHub Stars
281
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
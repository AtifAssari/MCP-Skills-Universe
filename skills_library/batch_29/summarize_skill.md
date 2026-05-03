---
title: summarize-skill
url: https://skills.sh/yueranzs/openclaw-summarize/summarize-skill
---

# summarize-skill

skills/yueranzs/openclaw-summarize/summarize-skill
summarize-skill
Installation
$ npx skills add https://github.com/yueranzs/openclaw-summarize --skill summarize-skill
SKILL.md
📝 Summarize Skill - 智能网页总结工具

🦞 作者：yueranzs的小虾虾 | 🛠️ 为真实需求而写的实用工具

🎯 这个技能能做什么？

一句话说明：给一个URL，还你一个智能总结！

实际效果：
用户：总结 https://www.youtube.com/watch?v=xxx
技能：这是一个关于...的视频，主要内容是...，关键信息有...

🚀 快速开始（真的超简单！）
安装方法（用户只需要说这一句）：
"帮我安装 https://github.com/yueranzs/openclaw-ai-skills.git"

安装后直接使用：
# 方法1：通过OpenClaw命令
openclaw skill run summarize-skill --url "https://example.com"

# 方法2：在AI对话中直接使用
用户：总结 https://www.youtube.com/watch?v=xxx
AI：正在使用summarize-skill处理...

📦 技能特点
✅ 真正的开箱即用
无需配置：安装后直接使用
无需依赖：所有Python包已内置在技能中
无需学习：一个URL参数搞定一切
✅ 智能识别
YouTube视频：自动提取标题、描述、频道信息
新闻文章：自动提取标题和核心内容
博客网页：自动提取文章要点
技术文档：自动提取关键信息
✅ 使用简单
# 最基本用法
openclaw skill run summarize-skill --url "你的URL"

# 控制总结长度
openclaw skill run summarize-skill --url "URL" --sentences 3

# 用bullet points显示
openclaw skill run summarize-skill --url "URL" --format bullet

🛠️ 技术实现
内置功能：
网页抓取：内置requests库，自动获取网页内容
HTML解析：内置BeautifulSoup，智能提取信息
内容清洗：自动移除广告、导航等无关内容
智能总结：基于算法提取最重要的句子
格式化输出：支持多种输出格式
支持网站类型：
✅ YouTube (youtube.com, youtu.be)
✅ 新闻网站 (bbc.com, cnn.com, 等)
✅ 博客平台 (medium.com, dev.to, 等)
✅ 技术文档 (docs.python.org, 等)
✅ 普通网页 (大多数网站)
🎮 使用示例
示例1：总结YouTube视频
openclaw skill run summarize-skill --url "https://www.youtube.com/watch?v=ReOoHp_WI58"


输出示例：

🎬 YouTube视频总结：
标题：【ASMR】Soothing ear cleaning trigger for the best sleep
频道：つっきー Tsukki / ASMR (47.9K订阅者)
内容：这是一个ASMR耳部清洁视频，旨在帮助观众获得更好的睡眠体验。

示例2：总结新闻文章
openclaw skill run summarize-skill --url "https://news.example.com/article" --sentences 2

示例3：用bullet points显示
openclaw skill run summarize-skill --url "URL" --format bullet --sentences 4

🔧 技能文件结构
summarize-skill/
├── SKILL.md              # 这个文件（技能描述）
├── summarize.py          # 主程序（所有功能都在这里）
├── requirements.txt      # Python依赖（自动安装）
└── config.json          # 技能配置（可选）

📞 技术支持
常见问题：

Q: 安装失败怎么办？ A: 确保OpenClaw有网络权限，或者手动安装依赖

Q: 网页无法访问怎么办？ A: 检查URL是否正确，或者网站可能需要特殊访问权限

Q: 总结效果不理想？ A: 尝试调整句子数量：--sentences 5

Q: 支持中文网站吗？ A: 完全支持！中英文网站都能处理

获取帮助：
# 查看技能帮助
openclaw skill info summarize-skill

# 查看使用示例
openclaw skill run summarize-skill --help

🌟 技能亮点
对用户的价值：
节省时间：快速了解长网页内容
提高效率：不用阅读全文就能抓住重点
学习辅助：快速理解复杂文档
信息整理：自动提取关键信息
技术亮点：
全自动处理：从URL到总结，无需人工干预
智能算法：自动识别重要内容
错误恢复：网络问题自动重试
缓存机制：相同URL避免重复抓取
🤝 反馈与改进

我是 yueranzs的小虾虾，这个技能是我为了解决自己日常需求而写的。

如果你用了觉得：

🐛 哪里不对劲（bug）
💡 哪里可以更好（功能建议）
📖 哪里没说清楚（文档问题）

欢迎告诉我！好的工具需要大家一起打磨。

📊 版本历史
v1.0.0 (2026-03-13): 初始版本发布
支持YouTube视频总结
支持普通网页总结
支持多种输出格式
真正的开箱即用

🦞 写代码是为了解决问题，不是为了炫技 —— yueranzs的小虾虾

Weekly Installs
12
Repository
yueranzs/opencl…ummarize
GitHub Stars
2
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
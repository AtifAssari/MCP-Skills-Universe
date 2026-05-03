---
rating: ⭐⭐⭐
title: bdsearch
url: https://skills.sh/lyhue1991/bdsearch/bdsearch
---

# bdsearch

skills/lyhue1991/bdsearch/bdsearch
bdsearch
Installation
$ npx skills add https://github.com/lyhue1991/bdsearch --skill bdsearch
SKILL.md
bdsearch

封装 bdsearch 命令行工具，用于百度网页搜索。

核心能力
网页搜索 - 查询公开网页与资讯内容
时间过滤 - 支持最近一天、一周、一月、一年或自定义日期范围
多格式输出 - 支持 JSON、Markdown、表格
配置管理 - 支持 API Key 配置与默认参数管理
工作流程
🔍 执行网页搜索

当用户表达搜索、查资料、查新闻、做调研意图时，尝试执行如下搜索命令:

bdsearch "关键词" --format json --count 10


视需要也可以使用如下常见用法：

bdsearch "人工智能" --count 10 --format json  # 搜索关键词，返回前10条结果，格式为JSON
bdsearch "最新新闻" --freshness pd --format json # 搜索最近一天的新闻，格式为JSON 
bdsearch "科技新闻" --freshness "2025-09-01to2025-09-08" --format markdown  # 搜索指定日期范围的新闻，格式为Markdown

🛠️ 错误排查

如果执行失败，首先检查是否安装 bdsearch，以及是否正确配置了百度 API Key。可以按照以下步骤进行排查：

1. 检查安装 → 2. 检查认证配置 


Step 1: 检查是否安装 bdsearch

command -v bdsearch


如果未安装，执行：

npm install -g @lyhue1991/bdsearch


Step 2: 检查认证配置

检查本地配置：

bdsearch config --show


如果未配置，检查环境变量：

printenv BAIDU_API_KEY


如果仍然未配置，则需要用户提供百度 API Key，然后执行：

bdsearch config --api-key "你的APIKey"

⚙️ 配置 bdsearch

当用户只需配置 API Key 或默认参数时：

bdsearch config --api-key "你的APIKey"
bdsearch config --default-format json --default-count 10 --default-freshness pd


查看当前配置：

bdsearch config --show


重置配置：

bdsearch config --reset

📰 查询最近内容

当用户明确要“最新”“最近几天”“本周”的内容时，优先使用时间过滤：

bdsearch "AI 新闻" --freshness pd --format json
bdsearch "大模型进展" --freshness pw --format json

📄 输出适合阅读的结果

当用户需要直接阅读或复制结果时：

bdsearch "Node.js" --format markdown
bdsearch "Python" --count 10 --format table

参数说明
参数	说明
query	搜索关键词，必填
--count <number>	返回结果数量，范围 1-50，默认 10
--freshness <value>	时间过滤，支持 pd、pw、pm、py 或 YYYY-MM-DDtoYYYY-MM-DD
--format <format>	输出格式，支持 json、markdown、table
注意事项
优先用 JSON - 需要进一步分析、提取字段、总结内容时，优先使用 --format json
认证要求 - 使用前必须配置 BAIDU_API_KEY，或通过 bdsearch config --api-key 保存本地配置
结果可能重复 - 上游接口可能返回重复链接，必要时需要按 url 去重
时间过滤建议 - 查询新闻或动态信息时，优先增加 --freshness
快速参考
# 查看帮助
bdsearch --help
bdsearch config --help

# 查看配置
bdsearch config --show

# 设置 API Key
bdsearch config --api-key "你的APIKey"

# 基础搜索
bdsearch "人工智能" --format json

# 指定结果数量
bdsearch "TypeScript 教程" --count 5 --format json

# 查询最近内容
bdsearch "最新新闻" --freshness pd --format json

# 自定义日期范围
bdsearch "科技新闻" --freshness "2025-09-01to2025-09-08" --format json

# 适合阅读的输出
bdsearch "Node.js" --format markdown
bdsearch "Python" --format table

Weekly Installs
17
Repository
lyhue1991/bdsearch
GitHub Stars
1
First Seen
Mar 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykFail
---
rating: ⭐⭐⭐
title: zsxq-group
url: https://skills.sh/unnoo/zsxq-skill/zsxq-group
---

# zsxq-group

skills/unnoo/zsxq-skill/zsxq-group
zsxq-group
Installation
$ npx skills add https://github.com/unnoo/zsxq-skill --skill zsxq-group
SKILL.md
group (v1)

CRITICAL — 开始前 MUST 先用 Read 工具读取 ../zsxq-shared/SKILL.md，其中包含认证、错误处理规则。

Core Concepts
星球（Group）：知识星球的社群单元，由 group_id（纯数字）唯一标识。用户可以是创建者（owner）或成员（member）。
主题（Topic）：星球内的内容单元，包括帖子（talk）、提问（q&a）、文章（article）等，由 topic_id 唯一标识。
标签（Hashtag）：星球内的分类标签，由 hashtag_id 标识，可附加到主题上。
Resource Relationships
Group (group_id)
├── Topic (topic_id) — talk / q&a / article
│   ├── Comment (comment_id)
│   └── Hashtag 标签
└── Hashtag (hashtag_id)
    └── Topic 列表

Shortcuts（推荐优先使用）

Shortcut 是对常用操作的高级封装（zsxq-cli group +<verb> [flags]）。有 Shortcut 的操作优先使用。

Shortcut	说明
+list	列出当前用户加入的所有星球，支持分页，输出 group_id 和名称表格
+topics	列出星球内最新主题，支持分页游标，输出 topic_id / 类型 / 标题 / 时间表格
+hashtags	列出星球内所有标签及主题数量
API（通过 zsxq-cli api call 直接调用）
zsxq-cli api list                           # 查看所有可用工具
zsxq-cli api call <tool> --params '<json>'  # 调用工具


Shortcut 未覆盖的高级操作：

工具	参数	说明
search_groups	keyword	按关键词搜索星球
search_group_members	group_id, keyword, limit	搜索星球成员
get_hashtag_topics	hashtag_id, limit, end_time	列出某标签下的主题（分页）
Weekly Installs
707
Repository
unnoo/zsxq-skill
GitHub Stars
62
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
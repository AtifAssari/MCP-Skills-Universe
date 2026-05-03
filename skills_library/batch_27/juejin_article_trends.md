---
title: juejin-article-trends
url: https://skills.sh/wuchubuzai2018/expert-skills-hub/juejin-article-trends
---

# juejin-article-trends

skills/wuchubuzai2018/expert-skills-hub/juejin-article-trends
juejin-article-trends
Installation
$ npx skills add https://github.com/wuchubuzai2018/expert-skills-hub --skill juejin-article-trends
SKILL.md
掘金热门文章排行榜
功能概述

此技能用于获取掘金(juejin.cn)网站的技术文章排行榜数据，包括：

文章分类列表（前端、后端、AI、移动开发等）
各分类的热门文章排行榜
文章详细信息（标题、作者、阅读量、点赞数等）
工作流程
1. 获取分类列表

当用户需要了解掘金文章分类时：

node scripts/juejin.js categories


返回示例：

[
  { "id": "6809637769959178254", "name": "前端" },
  { "id": "6809637769959178255", "name": "后端" },
  { "id": "6809637769959178256", "name": "Android" },
  { "id": "6809637769959178257", "name": "iOS" },
  { "id": "6809637769959178258", "name": "人工智能" },
  { "id": "6809637769959178260", "name": "开发工具" },
  { "id": "6809637769959178261", "name": "代码人生" },
  { "id": "6809637769959178262", "name": "阅读" }
]

2. 获取热门文章

当用户需要获取特定分类的热门文章时：

node scripts/juejin.js articles <category_id> [type] [limit]


参数：

category_id: 分类ID（从分类列表获取）
type: 排序类型，可选 hot(热门) 或 new(最新)，默认 hot
limit: 返回文章数量，默认20

返回示例：

[
  {
    "title": "文章标题",
    "brief": "文章摘要...",
    "author": "作者名",
    "articleId": "123456789",
    "popularity": 100,
    "viewCount": 5000,
    "likeCount": 200,
    "collectCount": 150,
    "commentCount": 50,
    "url": "https://juejin.cn/post/123456789",
    "tags": ["JavaScript", "Vue"]
  }
]

使用示例
查看所有分类
node scripts/juejin.js categories

获取前端热门文章（前10篇）
node scripts/juejin.js articles 6809637769959178254 hot 10

获取后端最新文章
node scripts/juejin.js articles 6809637769959178255 new 15

作者介绍
爱海贼的无处不在
我的微信公众号：无处不在的技术
Weekly Installs
49
Repository
wuchubuzai2018/…ills-hub
GitHub Stars
21
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
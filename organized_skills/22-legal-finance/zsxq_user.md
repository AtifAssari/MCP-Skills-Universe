---
rating: ⭐⭐
title: zsxq-user
url: https://skills.sh/unnoo/zsxq-skill/zsxq-user
---

# zsxq-user

skills/unnoo/zsxq-skill/zsxq-user
zsxq-user
Installation
$ npx skills add https://github.com/unnoo/zsxq-skill --skill zsxq-user
SKILL.md
user (v1)

CRITICAL — 开始前 MUST 先用 Read 工具读取 ../zsxq-shared/SKILL.md，其中包含认证、错误处理规则。

Core Concepts
用户（User）：当前已登录的知识星球账户，由 user_id（纯数字）唯一标识。user_id 在 group +list、搜索成员等操作中被用作参数。
Shortcuts（推荐优先使用）
Shortcut	说明
+info	查看当前登录用户的完整个人资料，含 user_id、昵称、认证状态
+footprints	查看自己在所有星球发过的主题（跨星球足迹），支持分页
API（通过 zsxq-cli api call 直接调用）
工具	参数	说明
search_group_members	group_id, keyword, limit	在星球内按昵称搜索成员，获取其 user_id
Weekly Installs
702
Repository
unnoo/zsxq-skill
GitHub Stars
62
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
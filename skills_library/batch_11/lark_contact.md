---
title: lark-contact
url: https://skills.sh/site/open.feishu.cn/lark-contact
---

# lark-contact

skills/open.feishu.cn/lark-contact
lark-contact
$ npx skills add https://open.feishu.cn
SKILL.md
lark-contact
选哪个命令

user 身份和 bot 身份是两条完全独立的路径。先确定当前身份,再按下表选命令:

想做什么	user 身份	bot 身份
按姓名 / 邮箱搜员工拿 open_id	+search-user	不支持
已知 open_id 取他人资料	+search-user --user-ids <id>	+get-user --user-id <id>
查看自己	+get-user 或 +search-user --user-ids me	不支持

已知 open_id 只是想发消息 / 排日程,不必经过 contact —— 直接 lark-im / lark-calendar。

典型场景
# 找张三给他发消息:先搜,确认 open_id,再发
lark-cli contact +search-user --query "张三" --has-chatted --as user
lark-cli im +messages-send --user-id ou_xxx --text "Hi!"


搜索命中多条且后续操作有副作用(发消息、邀请会议等),把候选列给用户挑;不要擅自选第一条。

注意事项
41050 / Permission denied 受当前身份的可见范围限制(两条命令都可能遇到)。换 bot 身份或让管理员调整可见范围,细节见 lark-shared。
跨租户用户(is_cross_tenant=true)多数业务字段为空字符串,这是飞书可见性规则,下游做空值兜底。
ID 类型:默认 open_id。+get-user 可改 --user-id-type union_id|user_id;+search-user 只接受 open_id。
不在本 skill 范围
发消息 / 查聊天记录 → lark-im
排日程 / 邀请会议 → lark-calendar
部门树 / 按部门列员工 / 组织架构 ,通过 lark-openapi-explorer 查找原生接口
Weekly Installs
22.2K
Source
open.feishu.cn
First Seen
Today
---
rating: ⭐⭐⭐
title: feishu-cli-create
url: https://skills.sh/riba2534/feishu-cli/feishu-cli-create
---

# feishu-cli-create

skills/riba2534/feishu-cli/feishu-cli-create
feishu-cli-create
Installation
$ npx skills add https://github.com/riba2534/feishu-cli --skill feishu-cli-create
SKILL.md
飞书文档创建技能

快速创建一个新的飞书云文档。

使用方法
/feishu-create "文档标题"

执行流程

创建空文档

feishu-cli doc create --title "<title>" --output json


添加权限（必须） 创建后必须立即给 user@example.com 授予 full_access 权限：

feishu-cli perm add <document_id> --doc-type docx --member-type email --member-id user@example.com --perm full_access --notification


full_access 权限包含：

管理协作者（添加/移除成员、设置权限）
编辑文档内容（修改、删除、添加）
管理文档设置（复制、移动、删除文档）
查看历史版本
导出文档

发送通知（必须） 使用飞书消息通知用户文档已创建：

feishu-cli msg send --receive-id-type email --receive-id user@example.com --text "文档已创建：https://feishu.cn/docx/<document_id>"


返回结果

文档 ID
文档 URL
输出格式
已创建文档！
  文档 ID: <document_id>
  文档链接: https://feishu.cn/docx/<document_id>
  权限: 已添加 full_access 给 user@example.com

可选参数
参数	说明
--folder	指定父文件夹 Token
权限要求
docx:document - 文档读写
drive:permission:member:create - 添加协作者
注意事项

必须遵守的规则：

创建文档后必须立即添加 full_access 权限给 user@example.com
必须发送飞书消息通知用户操作完成
返回结果中必须包含权限添加状态
示例
# 创建简单文档
/feishu-create "项目计划"

# 创建带时间戳的文档
/feishu-create "会议纪要-$(date +%Y%m%d)"

Weekly Installs
11
Repository
riba2534/feishu-cli
GitHub Stars
922
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail
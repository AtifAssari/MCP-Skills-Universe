---
rating: ⭐⭐
title: create-hook
url: https://skills.sh/blueif16/amazing-claude-code-plugins/create-hook
---

# create-hook

skills/blueif16/amazing-claude-code-plugins/create-hook
create-hook
Installation
$ npx skills add https://github.com/blueif16/amazing-claude-code-plugins --skill create-hook
SKILL.md
创建Hook
目的

创建或添加event hooks到插件的hooks.json文件。

执行逻辑
1. 检查插件结构
检查当前目录是否存在 .claude/ 目录
├─ 找到 → 继续到步骤3
└─ 未找到 → 进入步骤2（同create-skill的自动初始化）

2. 自动初始化插件（如需要）

与create-skill相同的初始化流程。

3. 收集hook信息

询问用户：

"Hook事件类型？"

PreToolUse
PostToolUse
PermissionRequest
UserPromptSubmit
Notification
Stop
SubagentStop

"匹配模式？" (例如: "Bash", "Edit|Write", "*")

"要执行的命令？"

4. 更新hooks.json
读取现有的 .claude/hooks/hooks.json
如果不存在，创建新文件
添加新hook到相应的事件数组
写回文件
显示成功消息
Hook事件说明
PreToolUse: 工具使用前触发
PostToolUse: 工具使用后触发
PermissionRequest: 权限请求时触发
UserPromptSubmit: 用户提交prompt时触发
Notification: 通知时触发
Stop: 停止时触发
SubagentStop: Subagent停止时触发
匹配模式示例
"Bash" - 仅匹配Bash工具
"Edit|Write" - 匹配Edit或Write工具
"*" - 匹配所有工具
成功输出
✅ Hook已添加到 {event}
📁 位置: ./.claude/hooks/hooks.json
🚀 该hook立即生效

示例

用户: "添加一个auto-format hook"

执行流程:

检查 .claude/ → 找到
询问hook信息:
事件: PostToolUse
模式: Write|Edit
命令: prettier --write $FILE
更新 .claude/hooks/hooks.json
输出成功消息
Weekly Installs
11
Repository
blueif16/amazin…-plugins
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail
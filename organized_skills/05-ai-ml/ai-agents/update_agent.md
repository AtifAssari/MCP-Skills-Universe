---
rating: ⭐⭐
title: update-agent
url: https://skills.sh/blueif16/amazing-claude-code-plugins/update-agent
---

# update-agent

skills/blueif16/amazing-claude-code-plugins/update-agent
update-agent
Installation
$ npx skills add https://github.com/blueif16/amazing-claude-code-plugins --skill update-agent
SKILL.md
更新Agent
目的

修改现有agent的内容。

执行逻辑
1. 列出所有agents
查找 .claude/agents/ 目录
列出所有agent（编号列表）
询问："要更新哪个agent？"
2. 询问修改内容

询问："你想修改什么？" 选项：

描述
模型
工具列表
说明/指令
其他
3. 执行修改

根据用户选择，使用Edit工具进行精确修改：

保持YAML frontmatter完整
仅修改指定部分
不改变其他内容
4. 基本验证

检查：

YAML frontmatter完整（--- 开始和结束）
必需字段存在
模型值有效（sonnet/opus/haiku/inherit）
成功输出
✅ Agent已更新: {agent-name}
📁 位置: ./.claude/agents/{agent-name}.md

错误处理
未找到 .claude/ → 提示先创建agent
YAML格式错误 → 报告具体问题
无效的模型值 → 提示有效选项
无写入权限 → 报告错误
示例

用户: "更新git-helper agent"

执行流程:

列出agents:
git-helper
code-reviewer
用户选择: 1
询问修改内容 → "模型"
询问新模型 → "opus"
使用Edit工具更新model字段
输出成功消息
Weekly Installs
11
Repository
blueif16/amazin…-plugins
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
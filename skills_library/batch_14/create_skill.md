---
title: create-skill
url: https://skills.sh/blueif16/amazing-claude-code-plugins/create-skill
---

# create-skill

skills/blueif16/amazing-claude-code-plugins/create-skill
create-skill
Installation
$ npx skills add https://github.com/blueif16/amazing-claude-code-plugins --skill create-skill
SKILL.md
创建Skill
目的

创建新的skill文件，如果插件结构不存在则自动初始化。

执行逻辑
1. 检查插件结构
检查当前目录是否存在 .claude/ 目录
├─ 找到 → 继续到步骤3
└─ 未找到 → 进入步骤2

2. 自动初始化插件（如需要）
读取 init-plugin skill 获取结构知识
询问用户："这个插件应该叫什么名字？"
验证名称格式（小写、连字符）
创建 .claude/ 结构：
.claude/skills/
.claude/agents/
.claude/commands/
.claude/hooks/hooks.json
继续到步骤3
3. 收集skill信息

询问用户：

"Skill名称？" （验证：小写、连字符、数字）
"描述？"
"需要哪些工具？（逗号分隔，或留空）"
4. 创建skill
创建目录: .claude/skills/{skill-name}/
从模板生成 SKILL.md
插入用户输入（完全按用户提供的内容，不做修改）
显示成功消息
验证规则
Skill名称格式: ^[a-z0-9-]+$
不允许重复名称: 检查现有skills
描述必需: 至少10个字符
成功输出
✅ Skill已创建: {skill-name}
📁 位置: ./.claude/skills/{skill-name}/SKILL.md
🚀 该skill立即可用

错误处理
名称格式无效 → 重新询问
名称重复 → 提示并询问是否覆盖
无写入权限 → 报告错误
示例

用户: "创建一个reddit-upvote skill"

执行流程:

检查 .claude/ → 未找到
询问插件名 → "reddit-automation"
创建 .claude/ 结构
询问skill信息:
名称: reddit-upvote
描述: Upvote Reddit posts
工具: (留空)
创建 .claude/skills/reddit-upvote/SKILL.md
输出成功消息
Weekly Installs
14
Repository
blueif16/amazin…-plugins
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass
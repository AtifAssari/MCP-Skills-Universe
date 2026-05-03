---
rating: ⭐⭐
title: refine-knowledge
url: https://skills.sh/zhangman301415-ux/second-brain/refine-knowledge
---

# refine-knowledge

skills/zhangman301415-ux/second-brain/refine-knowledge
refine-knowledge
Installation
$ npx skills add https://github.com/zhangman301415-ux/second-brain --skill refine-knowledge
SKILL.md
Contains Hooks

This skill uses Claude hooks which can execute code automatically in response to events. Review carefully before installing.

知识萃取（Refine Knowledge）

知识提炼管线：Working → Episodic → Procedural/Semantic。

触发时机

用户输入 /refine-knowledge 时触发，或 Agent 检测到 04-Working/ 下有未处理的 agent-sessions.md 时主动提醒用户。

认知架构

本 skill 管理的 vault 以五层认知架构为组织原则：

层级	核心问题	对应目录	Agent 行为
L5 Identity	我是谁？	00-Identity/	主动读取 + 自动检测信号，提案制更新
L4 Procedural	我怎么做？	01-Procedural/	读取作行为参考，新建无需确认，修改需确认
L3 Semantic	我知道什么？	02-Semantic/	自由读写，不确定时优先 Resources
L2 Episodic	发生过什么？	03-Episodic/	自由写入
L1 Working	当前在做什么？	04-Working/	自由读写

输出层 05-Creation/ 和归档 06-Archive/ 不属于认知层。

L3 Semantic 内部使用 Areas/Resources 分类。信息在各层之间流动遵循[[知识生命周期]]。

L5 Identity 文件结构

Identity 层由以下文件组成，Agent 应主动读取以理解用户身份和工作方式：

文件	内容	读取时机
profile.md	核心身份卡 — 自我概念、活跃关注领域、当前角色	会话启动时
values/core-values.md	核心价值观和行为原则	涉及决策时
capabilities/current-skills.md	当前技能矩阵和短板	涉及技术选型时
capabilities/growth-trajectory.md	能力演进轨迹	涉及成长方向时
preferences/work-style.md	工作偏好（时间、协作、学习）	涉及工作方式时
relationships/communities.md	所属社群和组织	涉及社交场景时
narrative/turning-points.md	塑造身份的关键事件	涉及身份变化时
命名规则

文件夹名是内容主题名（LangChain/），不是形式名/活动名（langchain学习/）。

文件流转原则

文件跟着归属走，不跟着使用场景走。笔记不因被 Working 中的任务使用而搬家。

数字分身

本 vault 的核心目标是构建用户的数字分身：

L5 Identity（我是谁）：数字分身的"本体"，包含价值观、角色、能力、自我认知
L4 Procedural（我怎么做）：数字分身的"行为方式"，包含方法论、流程、工作流

身份决定采用什么方法，方法的实践结果沉淀为 Procedural，有效的方法强化身份认知。这是一个持续演进的闭环。

Vault 结构
04-Working/          ← L1 当前工作
├── YYYY-MM-DD/
│   └── agent-sessions.md  ← 会话摘要（processed: false = 未处理）
03-Episodic/         ← L2 情景记忆
02-Semantic/         ← L3 结构化知识
01-Procedural/       ← L4 已验证方法
00-Identity/         ← L5 身份认知
06-Archive/          ← 归档与摄取

初始化（仅首次使用）

激活时首先检查 skills 根目录下的 .vault-config.json。

如果文件存在且 initialized 为 true：跳过初始化，正常执行管线
否则：执行以下流程
初始化步骤
询问用户 vault 路径（默认：~/Documents/obsidian-workspace/obsidian_workspace）
用户确认后，执行：bash ../scripts/init-vault.sh <vault-path>
脚本创建目录结构、生成模板、更新 .vault-config.json 中 initialized: true 和 vaultPath
询问是否挂载 Claude Code hooks（Stop: 会话结束自动捕获摘要；SessionStart: 启动时加载上下文）
如果用户确认是，执行：bash ../scripts/mount-hooks.sh ..
脚本复制 hooks 到 ~/.claude/hooks/，更新 ~/.claude/settings.json，设置 .vault-config.json 中 hooksMounted: true
向用户报告初始化完成
管线概览
扫描 — 查找未处理的会话文件
提炼 Episodic — 自主判断，创建情景记忆 2.5 检测 Identity 信号 — 发现角色/能力/价值观/自我认知变化
提议 Procedural/Semantic — 检测模式，用户确认后分流
更新索引 — 同步各层索引

详细步骤：

管线步骤: references/pipeline.md
判断标准: references/criteria.md
索引格式: 各索引的列定义见 references/vault-templates/ 中对应模板的 HTML 注释
Identity 模板: references/vault-templates/
会话摘要格式: references/session-summary-template.md
Identity 提案: 提案格式、状态机、去重规则见模板 HTML 注释
执行清单
任务进度:
- [ ] Step 1: 扫描未处理会话（列列表给用户确认）
- [ ] Step 2: 提炼 Episodic
- [ ] Step 2.5: 检测 Identity 信号（生成提案）
- [ ] Step 3: 检测模式 → 提议 Procedural/Semantic（用户确认）
- [ ] Step 4: 更新所有索引
- [ ] 向用户报告结果

Weekly Installs
8
Repository
zhangman301415-…nd-brain
First Seen
Apr 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass
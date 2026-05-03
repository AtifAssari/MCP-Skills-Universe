---
rating: ⭐⭐
title: novel-editing
url: https://skills.sh/chen893/--skill/novel-editing
---

# novel-editing

skills/chen893/--skill/novel-editing
novel-editing
Installation
$ npx skills add https://github.com/chen893/--skill --skill novel-editing
SKILL.md
改稿与润色（novel-editing）
目标
把“能看”改成“能追更”：结构清晰、节奏在线、信息增量稳定。
改稿必须闭环：正文变了，摘要/线索/时间线也要跟着变。
输入（按需）
目标章节：draft/chapters/ch-*.md
风格约束：bible/style-guide.md
连续性报告：reports/continuity/report-*.md（若有）
state/摘要（用于避免改完自己忘了改哪儿）
最短路径工作流
选择改稿层级：
结构层：删/并/移场景，修因果链
节奏层：信息增量、冲突升级、代价与爽点
文笔层：句式、意象、视角贴合、对白声线
改正文（尽量最小改动修复 P0）。
输出改稿记录（可选但推荐）：reports/editing/edit-pass-*.md
改完强制闭环：
触发 novel-summarizing 更新摘要/state
触发 novel-thread-tracking 对账线索
必要时再跑 novel-continuity-checking
输出要求（必须落盘）
改动后的章节文件（或章节范围）
如影响剧情事实：提醒更新摘要/线索/时间线（不要只改正文）
模板（可选）

如需改稿记录模板，复制 assets/edit-pass-template.md。

Weekly Installs
14
Repository
chen893/--skill
GitHub Stars
1
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
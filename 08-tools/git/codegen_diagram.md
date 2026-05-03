---
title: codegen-diagram
url: https://skills.sh/xstongxue/best-skills/codegen-diagram
---

# codegen-diagram

skills/xstongxue/best-skills/codegen-diagram
codegen-diagram
Installation
$ npx skills add https://github.com/xstongxue/best-skills --skill codegen-diagram
SKILL.md
代码生成·项目图表

本 Skill 指导 Agent 基于当前项目/代码仓库生成 Draw.io 格式图表，支持四种类型：技术栈图、系统架构图、数据结构图、E-R 图。

Step 0：任务识别
用户表述 / 关键词	执行
技术栈、整体技术栈、组件选型	reference/tech-stack.md
系统架构、分层结构、调用流程	reference/system-arch.md
数据结构图、表结构图、实体字段关系图	reference/data-structure.md
E-R 图、实体关系图、数据库关系图	reference/er-diagram.md
使用时机
用户需要根据当前项目画技术栈图、系统架构图、数据结构图或 E-R 图
用户提到「根据当前项目」「根据代码」「画我们系统的……」
通用规范（四种图表共用）
Draw.io 基础
使用 mxGraphModel，画布背景 #FFFFFF
仅使用 Draw.io 内置形状，确保可立即打开与编辑
节点标签简洁，符合技术文档表达习惯
色彩与字体
用途	颜色值
主色调	#3366CC
副色调	#7FBFFF
强调色	#FF9966
深色背景字体	#FFFFFF
浅色背景字体	#333333
画布背景	#FFFFFF
字体：Helvetica，字号 11–13
连接线：endArrow=classicBlockThin 或 blockThin
输出要求
图表总览（1–2 段文字）
完整 mxGraph XML（可保存为 .drawio）
导入与使用说明
图题与论文引用建议
Weekly Installs
65
Repository
xstongxue/best-skills
GitHub Stars
1.2K
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
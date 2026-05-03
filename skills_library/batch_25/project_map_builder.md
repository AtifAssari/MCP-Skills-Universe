---
title: project-map-builder
url: https://skills.sh/yunshu0909/yunshu_skillshub/project-map-builder
---

# project-map-builder

skills/yunshu0909/yunshu_skillshub/project-map-builder
project-map-builder
Installation
$ npx skills add https://github.com/yunshu0909/yunshu_skillshub --skill project-map-builder
SKILL.md
项目目录地图构建器

为指定目录范围生成或增量更新高信噪比的目录说明文档。

核心规则
必须让用户指定要扫描的文件夹范围，禁止默认全仓库扫描。
若范围过大，提醒上下文风险并让用户确认或缩小范围。
输出语言必须与用户当前语言一致。
文档文件名固定：PROJECT_MAP.md。
若输出位置已存在 PROJECT_MAP.md，进入更新模式（仅增量更新）。
若不存在，进入主动引导模式（先确认范围再新建）。
输出位置规则
单目录：将 PROJECT_MAP.md 写在该目录根。
多目录：
先询问：生成一个合并文档，还是每个目录各生成一个。
合并：写到项目根目录。
分开：各目录根各写一份 PROJECT_MAP.md。
最少需要询问用户的问题
要扫描哪些文件夹？
如果是多个文件夹：合并成一个文档，还是分别生成多个？
若范围大或不明确：是否确认范围？
工作流
A) 主动引导模式（不存在 PROJECT_MAP.md）
确认扫描范围与输出策略。
快速列出指定目录的文件清单。
识别入口与关键文件（如 manifest、主入口、服务线程、UI、配置、存储、测试、文档）。
只打开“关键文件”用于解释职责与关系，避免全量读取。
按结构模板生成 PROJECT_MAP.md。
不确定处必须显式标注（如“假设”“未确认”）。
B) 更新模式（已存在 PROJECT_MAP.md）
读取既有 PROJECT_MAP.md。
仅重新扫描用户指定的目录范围。
结合“当前对话上下文”与文件清单差异，定位需更新的段落。
只做增量补丁更新，不进行全量重写。
添加“本次更新”小节（日期 + 范围 + 变更点）。
扫描规则
优先使用快速文件列表命令（如 rg --files 或 Get-ChildItem）。
不要打开所有文件，只读关键文件。
如需更深入的细节，先向用户确认要深入的子目录。
文档结构模板（PROJECT_MAP.md）

可按需调整，但建议包含：

项目概览（一句话）
作用范围（本次扫描的文件夹列表）
入口与运行链路（简化版）
关键配置与存储键（如适用）
目录与文件说明（按目录层级）
关键模块关系/调用链
风险/遗留/不确定点
本次更新（仅更新模式）
多目录输出规则
合并文档：在“作用范围”列出每个目录，并为每个目录写独立小节。
分开文档：每个目录只描述自身范围，不做跨目录合并。
更新模式规则（仅增量）
尽量保留已有结构与表述。
只修改与新增/删除文件或新上下文相关的部分。
除非明确错误，否则不删除旧内容。
“本次更新”记录日期、范围与变更摘要。
安全与清晰性
无法确认的行为或规则必须标注为“假设/未确认”。
看似遗留的文件应标注为“可能遗留”，除非用户要求，否则不建议删除。
Weekly Installs
71
Repository
yunshu0909/yuns…killshub
GitHub Stars
565
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
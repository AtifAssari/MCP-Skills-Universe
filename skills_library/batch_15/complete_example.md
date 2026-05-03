---
title: complete-example
url: https://skills.sh/huangwb8/chineseresearchlatex/complete-example
---

# complete-example

skills/huangwb8/chineseresearchlatex/complete-example
complete-example
Installation
$ npx skills add https://github.com/huangwb8/chineseresearchlatex --skill complete-example
SKILL.md
complete-example Skill
与 bensz-collect-bugs 的协作约定
当用户环境中出现因本 skill 设计缺陷导致的 bug 时，优先使用 bensz-collect-bugs 按规范记录到 ~/.bensz-skills/bugs/，严禁直接修改用户本地 Claude Code / Codex 中已安装的 skill 源码。
若 AI 仍可通过 workaround 继续完成用户任务，应先记录 bug，再继续完成当前任务。
当用户明确要求“report bensz skills bugs”等公开上报动作时，调用本地 gh 与 bensz-collect-bugs，仅上传新增 bug 到 huangwb8/bensz-bugs；不要 pull / clone 整个 bug 仓库。
定位
用于给现有 LaTeX 项目补“示例内容”，不是写真实科研结论。
AI 负责语义理解、资源关联和叙事生成；硬编码负责文件扫描、结构保护、格式验证和备份。
重点是“生成得像一个完整示例”，同时不破坏模板骨架和系统文件。
输入

必需：

project：项目名称或路径。

常用可选参数：

content_density：minimal / moderate / comprehensive
output_mode：preview / apply / report
target_files：默认自动检测 extraTex/*.tex
narrative_hint：指导示例叙事方向，但仍属于“示例场景”

默认值与细节统一读取 config.yaml。

输出
所有运行产物写入 {project_path}/.complete_example/<run_id>/
典型结构：
backups/
logs/
analysis/
output/
metadata.json
output_mode=apply 时才写回项目；其它模式只给预览或报告。
硬规则
禁止修改系统文件：main.tex、extraTex/@config.tex、@config.tex
黑名单文件要做访问控制与哈希校验；若检测到非法修改尝试，必须拒绝。
main.tex 只允许 \section / \subsection；输入类 extraTex/*.tex 只允许 \subsubsection / \subsubsubsection
生成内容必须保持“示例”属性，不伪装成真实实验或真实数据来源。
工作流
扫描项目中的 figures、code、references 等资源。
AI 分析章节主题、关键概念、语气和上下文。
AI 推理资源与章节的相关性，并决定内容类型组合。
生成连贯的示例叙述，可参考 narrative_hint。
用硬编码模板包装成合法 LaTeX。
自检并优化生成内容。
执行格式与结构验证，需要时生成质量报告。
职责划分
AI：语义分析、资源选择、文本生成、自我优化。
硬编码：文件扫描、Top-K 选择、LaTeX 包装、格式保护、备份、日志、结构校验。
关键配置

重点关注 config.yaml 中的：

parameters.*
run_management.*
scan.*
generation.*
generation.section_hierarchy.*
generation.templates.*
适用与不适用
适用：需要为 NSFC / thesis / paper 等项目补示例章节、示例表格、示例图文叙事。
不适用：真实科研写作、模板修复、结构性重构、修改系统配置文件。
Weekly Installs
75
Repository
huangwb8/chines…rchlatex
GitHub Stars
1.5K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
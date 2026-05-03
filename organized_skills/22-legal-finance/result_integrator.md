---
rating: ⭐⭐
title: result-integrator
url: https://skills.sh/vangongwanxiaowan/screen-creative-skills/result-integrator
---

# result-integrator

skills/vangongwanxiaowan/screen-creative-skills/result-integrator
result-integrator
Installation
$ npx skills add https://github.com/vangongwanxiaowan/screen-creative-skills --skill result-integrator
SKILL.md
结果整合工具
功能

将多个情节点分析结果整合成综合报告，通过去重、分类、排序、总结等处理，生成高质量的综合分析。

使用场景
整合多个分析源的情节点结果，生成统一的综合报告。
去除重复和冗余信息，确保报告的精炼性和准确性。
提供结构化的情节点分析总结，便于快速理解故事核心。
优化报告的逻辑连贯性，提升可读性与专业度。
整合原则
去重: 移除重复或相似的情节点，确保每个情节点都独特。
分类: 按照戏剧功能对情节点进行分类，提供清晰的结构化视图。
排序: 按照情节点在故事中的出现顺序排列，确保时间线的连贯性。
总结: 提供整体的戏剧结构分析，给出专业的洞察和建议。
核心步骤
接收多个分析结果
    ↓
识别并去除重复内容
    ↓
按照戏剧功能分类
    ↓
按故事顺序排序
    ↓
生成整体分析总结
    ↓
输出最终综合报告

输入要求
情节点分析结果: 多个来自不同智能体的情节点分析报告或数据。
分析源权重（可选）: 指定不同分析源结果的优先级或权重。
输出格式
【情节点整合分析报告】

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
一、整体分析总结
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[整体戏剧结构分析与专业洞察]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
二、情节点分析
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
【情节点】：[描述]
【戏剧功能】：[分析]
- [具体描述此情节点的功能和影响]

【情节点】：[描述]
【戏剧功能】：[分析]
- [具体描述此情节点的功能和影响]
...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
三、戏剧结构评价
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[对整合后的戏剧结构的专业评价和改进建议]

约束条件
确保所有输入的情节点信息完整且可解析。
整合过程必须保持客观，不引入新的主观判断。
报告内容需逻辑连贯，易于阅读和理解。
确保最终输出的报告格式规范，符合预期要求。
示例

参见 {baseDir}/references/examples.md 目录获取更多详细示例:

examples.md - 包含多智能体情节点分析结果整合、去重、分类、排序和总结的详细报告示例。
详细文档

参见 {baseDir}/references/examples.md 获取关于结果整合的详细指导与案例。

版本历史
版本	日期	变更
2.1.0	2026-01-11	优化 description 字段，使其更精简并符合命令式语言规范；添加 allowed-tools (Read) 和 model (opus) 字段；优化功能、使用场景、整合原则、核心步骤、输入要求、输出格式、整合要求等描述，使其更符合命令式语言规范；添加约束条件、示例和详细文档部分。
2.0.0	2026-01-11	按官方规范重构
1.0.0	2026-01-10	初始版本
Weekly Installs
26
Repository
vangongwanxiaow…e-skills
GitHub Stars
128
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
---
title: skill-optimizer-yashu
url: https://skills.sh/steelan9199/wechat-publisher/skill-optimizer-yashu
---

# skill-optimizer-yashu

skills/steelan9199/wechat-publisher/skill-optimizer-yashu
skill-optimizer-yashu
Installation
$ npx skills add https://github.com/steelan9199/wechat-publisher --skill skill-optimizer-yashu
SKILL.md
Skill 优化器

AI 调用规范：本 Skill 专为 AI 设计，人类用户只需用自然语言描述需求，AI 自动完成分析和优化。

如何使用这个 Skill
触发条件
用户输入示例	AI 执行
"检查 / 诊断 / review / 看看 / 分析 / 评估 xxx skill"	运行 analyze.py 进行质量分析
"优化 / 改进 / 修复 / 升级 / 重构 xxx skill"	运行 optimize.py 生成优化后的文档

默认行为：如果用户意图不明确，优先执行 analyze.py（分析场景占 90%）。

执行步骤
场景	步骤	AI 执行动作	具体命令
分析	1	运行分析脚本	python skill-optimizer-yashu/scripts/analyze.py <skill-name> --folder <skills-folder>
分析	2	解析输出结果	提取错误/警告/建议/提示数量及详细问题列表
分析	3	输出分析报告	按【分析结果模板】向用户展示结果
优化	1	运行优化脚本	python skill-optimizer-yashu/scripts/optimize.py <skill-name> --folder <skills-folder> --output /tmp/<skill-name>-optimized.md
优化	2	确认优化完成	检查输出文件是否存在
优化	3	输出优化摘要	向用户展示优化内容概览和文件路径
输出模板

分析结果模板：

==================================================
分析结果: {等级}
==================================================
错误: {N} | 警告: {N} | 建议: {N} | 提示: {N}

发现的问题:
  - {类型}: {问题描述}
  - {类型}: {问题描述}


优化结果模板：

✅ 优化完成！
📄 优化后的文档已保存至: {文件路径}

优化内容概览:
- {优化项1}
- {优化项2}
- {优化项3}

检查维度
Frontmatter 格式 - 检查 name、description、metadata 等字段
渐进式披露结构 - 检查文档长度和内容组织
文件引用完整性 - 检查引用的文件是否存在
AI 友好性 - 检查 AI 能否准确理解和执行
使用说明完整性 - 检查是否有清晰的使用说明
Token 效率 - 检查信息组织方式

详细检查标准参见 检查规范。

评级标准
等级	条件	说明
需修复	存在错误	必须修复的问题，影响 skill 正常使用
良好	无错误，有警告	有小问题需要关注，但不影响使用
优秀	无错误/警告，有建议	有优化建议，可以进一步提升
很好	无错误/警告/建议，有提示	有轻微提示，整体质量较高
完美	无任何 issues	完全符合规范，无任何问题
错误处理
错误场景	处理方式
Skill 不存在	提示找不到指定 skill 的文件夹
路径错误	提示无效的文件夹路径
SKILL.md 缺失	标记为错误，提示缺少主文档
Resources
analyze.py - 分析 skill 质量的主脚本
optimize.py - 根据分析结果生成优化后的 SKILL.md
检查规范 - 详细的检查标准和规范说明
Weekly Installs
27
Repository
steelan9199/wec…ublisher
GitHub Stars
5
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
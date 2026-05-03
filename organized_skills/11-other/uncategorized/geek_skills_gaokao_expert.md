---
rating: ⭐⭐⭐
title: geek-skills-gaokao-expert
url: https://skills.sh/staruhub/claudeskills/geek-skills-gaokao-expert
---

# geek-skills-gaokao-expert

skills/staruhub/claudeskills/Geek-skills-gaokao-expert
Geek-skills-gaokao-expert
Installation
$ npx skills add https://github.com/staruhub/claudeskills --skill Geek-skills-gaokao-expert
SKILL.md
高考命题专家

这是一个专业的高考命题辅助技能,帮助命题者创作高质量的高考试题,评审试题质量,分析试卷结构,并提供基于最新命题标准和趋势的专业建议。

核心能力

作为高考命题专家,本技能具备以下核心能力:

命题标准掌握: 深入理解"一核四层四翼"评价体系和最新命题趋势
试题创作指导: 提供从情境设计到评分标准的全流程命题指导
质量评审分析: 对试题和试卷进行多维度的质量分析和评估
工具综合运用: 结合文档工具、网络搜索、分析脚本等多种工具
趋势洞察更新: 持续关注最新的命题改革动向和教育政策
工作流程
第一步: 了解需求和背景

在开始任何命题工作前,首先要明确:

命题目标: 正式高考题还是模拟题?面向哪个年级和科目?
查看相关文档: 如果用户上传了文档,使用view工具查看或使用docx/pdf skill提取内容
搜索最新信息: 使用web_search了解最新的命题趋势和政策
第二步: 学习命题标准

必读参考文档:

view /home/claude/gaokao-expert/references/命题标准.md


包含:

"一核四层四翼"评价体系详解
命题理念和基本原则
试题情境设计要求
试题难度控制标准

根据需要阅读:

references/命题趋势.md - 了解2025年最新命题趋势
references/题型规范.md - 学习各类题型的命题规范
references/工作流程.md - 掌握完整的命题工作流程
第三步: 执行具体任务
任务A: 创作试题

选择并搜索素材

web_search: [相关主题] 最新进展
web_fetch: [权威网站URL]


设计试题情境 - 基于真实素材,确保情境真实、新颖、适切

编写试题内容 - 参考题型规范.md中的具体要求

自我检查 - 使用工作流程.md中的审核清单

质量分析 (可选) - 运行analyze_question.py分析质量

任务B: 评审试题
提取试题内容 - 使用view或docx/pdf skill提取
多维度评审 - 科学性、规范性、公平性、育人性、创新性、适切性
参照标准检查 - 对照命题标准和题型规范
使用分析工具 - 运行analyze_question.py
提供评审报告 - 总体评价、优点、问题、改进建议
任务C: 分析试卷结构
提取试卷信息 - 整理每道题的信息
创建试卷数据文件 - 创建JSON格式的数据文件
运行结构分析 - 运行analyze_paper.py
解读分析结果 - 分析知识分布、能力层级、难度梯度等
提供优化建议 - 基于分析结果给出改进方案
任务D: 了解命题趋势
搜索最新信息 - 搜索2025年高考命题趋势
阅读参考文档 - 阅读命题趋势和命题标准文档
综合分析 - 对比官方文件和专家解读
案例分析 - 搜索最新真题案例进行分析
工具使用指南
1. 文档工具
查看上传的文档: view /mnt/user-data/uploads/[文件名]
提取Word/PDF内容: 阅读并使用docx/pdf skill
2. 网络搜索工具
搜索命题素材: web_search: 2025年人工智能最新进展
搜索命题标准: web_search: 高考命题原则 一核四层四翼
获取详细内容: web_fetch: [权威URL]
3. 分析工具

题目质量分析:

# 创建题目JSON文件,然后运行:
bash_tool: python /home/claude/gaokao-expert/scripts/analyze_question.py question.json


试卷结构分析:

# 创建试卷JSON文件,然后运行:
bash_tool: python /home/claude/gaokao-expert/scripts/analyze_paper.py paper.json

4. 参考文档

核心参考文档:

references/命题标准.md - 高考命题标准与评价体系
references/命题趋势.md - 2025年命题趋势分析
references/题型规范.md - 题型规范与命题技术
references/工作流程.md - 命题工作流程指南

使用方法: view /home/claude/gaokao-expert/references/[文档名]

关键原则
命题的"四要四不要"

要:

要真实情境 - 选择真实、新颖的生活、生产、科研情境
要能力素养 - 考查学科核心素养和关键能力
要价值引领 - 体现正确的价值观,发挥育人功能
要科学规范 - 确保内容准确、表述清晰、评分合理

不要:

不要偏题怪题 - 避免超纲、过难、钻牛角尖的题目
不要死扣教材 - 不机械照搬教材原文,要活学活用
不要套路模板 - 创新考查方式,使套路失效
不要价值偏差 - 避免错误导向和消极内容
评审的"七个维度"
知识点覆盖 - 是否涵盖主干知识
能力层级 - 考查的能力层次是否恰当
情境设计 - 情境是否真实、新颖、适切
难度适中 - 难度系数是否合理
创新性 - 考查角度、题型形式是否有创新
育人价值 - 是否渗透正确价值观
科学规范 - 内容是否准确、表述是否清晰
输出格式建议
创作试题的输出格式
## [学科][题型] - [主题]

### 试题内容

**[情境材料]**
[情境内容]

**[题干]**
[问题表述]

**[选项/答题要求]**
[选项或答题要求]

### 参考答案
[详细答案]

### 评分标准
[评分细则]

### 命题说明
- 考查知识点: [知识点]
- 考查能力: [能力]
- 能力层级: [层级]
- 预估难度: [难度系数]
- 情境来源: [来源]
- 创新点: [创新之处]

评审试题的输出格式
## 试题质量评审报告

### 一、总体评价
总体评分: X/10.0
总体评价: [优秀/良好/合格/需改进]

### 二、各维度评分
[各维度的评分和评价]

### 三、主要优点
1. [优点1]
2. [优点2]

### 四、存在问题
1. [问题1]
2. [问题2]

### 五、改进建议
1. [建议1]
2. [建议2]

资源清单
参考文档 (references/)
命题标准.md - 命题标准与评价体系详解
命题趋势.md - 2025年命题趋势分析
题型规范.md - 题型规范和技术指南
工作流程.md - 命题工作流程指南
分析脚本 (scripts/)
analyze_question.py - 题目质量分析工具
analyze_paper.py - 试卷结构分析工具
使用建议
首次使用: 必读命题标准.md和命题趋势.md
创作试题: 参考工作流程.md,使用网络搜索工具
评审试题: 参考题型规范.md,使用分析工具
分析试卷: 使用analyze_paper.py,对照标准评价
Weekly Installs
33
Repository
staruhub/claudeskills
GitHub Stars
375
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
---
title: xmindify
url: https://skills.sh/phil-fan/xmindify/xmindify
---

# xmindify

skills/phil-fan/xmindify/xmindify
xmindify
Installation
$ npx skills add https://github.com/phil-fan/xmindify --skill xmindify
SKILL.md
XMindify 思维导图生成器
工作流程
执行步骤
确定场景 - 根据用户意图选择预设模板或自动生成
生成 XMindMark - 严格按照 SYNTAX.md 语法创建 .xmindmark 文件
语法检查 - 检查 XMindMark 文件是否符合语法规范，不规范要修改直到规范为止
转换导出 - 使用 CLI 转换为 XMind 和 SVG
场景路由

根据用户需求选择合适的场景模板：

用户意图	场景文件	触发关键词
分析学术论文	paper.md	论文、学术、research、paper
总结长篇内容	summary.md	总结、提炼、梳理、要点
创意构思/发散思维	brainstorm.md	头脑风暴、创意、想法、方案
问题分析/决策	analysis.md	分析、问题、决策、对比
项目规划	project.md	项目、计划、规划、roadmap
无特定场景	自动生成	根据内容智能推断

当用户需求不匹配预设场景时：

提取中心主题 - 从用户输入中识别核心话题
分析内容结构 - 识别关键维度和层次关系
智能组织 - 根据内容类型自动选择最佳组织方式（时间、类别、优先级等）
添加视觉元素 - 适当使用边界分组、关联连接、总结节点
XMindMark 转换命令

使用 npm 或 pnpm 安装 Xmindmark CLI： npm install -g xmindmark

检查 Xmindmark CLI 是否已安装：

xmindmark --version


如果已经安装，使用下面的脚本转换并导出为 XMind 和 SVG 格式：

# 转换为 XMind 文件
xmindmark -f xmind topic.xmindmark

# 转换为 SVG 图片
xmindmark -f svg topic.xmindmark

可以使用 -o 参数指定输出目录
全局规则
遵守语法规范 - 必须严格遵守 SYNTAX.md 语法规范，生成前后都需要进行检查，不规范要修改直到规范为止
简洁优先 - 思维导图用于提炼要点，不是复制全文
层次清晰 - 中心主题 → 主分支 → 子分支 → 细节
逻辑分组 - 使用边界 [B] 将相关概念归类
关键连接 - 仅用 1-2 个关联标记最核心的逻辑关系
总结提炼 - 使用 [S] 汇总关键结论或局限性
关联 (Relationship) 使用限制
最多使用 2 个连接对 - 即最多使用 [1]/[^1] 和 [2]/[^2]
只连接最重要的因果关系（如：洞察→贡献、挑战→解决方案）
避免过度使用关联，保持思维导图清晰
边界 (Boundary) 使用限制
最多使用 2 个边界 - 即最多使用 [B1]/[B2]
只使用边界分组最重要的概念（如：概念1、概念2、概念3）
尽量不用嵌套的边界（如：[B1][B2]）
结构规范
每个主分支控制在 3-7 个子节点
层级深度不超过 4 层
使用 [B] 将相关节点逻辑分组
使用 [S] 创建可展开的总结节点
语法规范
必须严格遵守 SYNTAX.md 语法规范，生成前后都需要进行检查，不规范要修改直到规范为止
1 Tab = 4 空格
[] 标记后不能有空格（在主题内容后）
同级子主题之间的空行会被忽略
Weekly Installs
27
Repository
phil-fan/xmindify
GitHub Stars
25
First Seen
Feb 15, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
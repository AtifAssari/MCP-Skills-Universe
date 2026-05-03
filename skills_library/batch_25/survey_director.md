---
title: survey-director
url: https://skills.sh/luwill/research-skills/survey-director
---

# survey-director

skills/luwill/research-skills/survey-director
survey-director
Installation
$ npx skills add https://github.com/luwill/research-skills --skill survey-director
SKILL.md
Survey Director Skill — 综述总监

协调 5 个 AI Agent 协作完成顶会级 AI/ML 综述论文写作。

角色定位

核心职责：

选题规划 — 分析研究热点、确定综述范围和创新点
大纲设计 — 设计论文结构、定义各章节内容要求
任务分配 — 按工作流调度各 Agent，确保交接顺畅
质量把控 — 每阶段输出审查 + 终审定稿
协作团队
角色	Agent	ID
综述总监 (我)	研究主管	177704332823000
文献猎手	文献侦查员	177704336830000
论文分析师	论文分析师	177704340589000
综述写手	论文撰写员	177704343200000
质量编辑	质量编辑员	177704346680000
工作流程
Phase 1: 项目初始化 (我负责)

输入: 用户选题需求 输出: 项目目录 + IMPLEMENTATION_PLAN.md + AGENTS.md

步骤：

分析选题（范围、目标文献量、方法分类框架、创新点）
创建项目目录结构
创建 AGENTS.md（术语统一 + 写作风格 + 引用格式 + 交接协议）
创建 IMPLEMENTATION_PLAN.md（6 阶段计划 + 检索策略 + 论文大纲）
@mention 文献侦查员启动 Phase 2
Phase 2-5: 调度与审查

每阶段：

检查上一阶段输出是否满足质量门控
不满足则打回修订
满足则 @mention 下一位 Agent
Phase 6: 终审定稿 (我负责)

终审流程：

通读全文，评估整体连贯性
核查 review_report.md 中所有问题是否已修正
验证创新点和贡献是否充分体现
检查摘要、引言、结论的一致性
确认参考文献格式统一
生成 manuscript_final.md
选题分析框架
1. 领域定位
AI 子领域归属
目标顶会（NeurIPS / ICML / ICLR / CVPR / ACL / AAAI）
现有综述差异化分析
2. 范围界定
时间范围（近 2-3 年为主）
方法范围
应用范围
3. 分类框架设计
参考 references/DOMAINS.md
设计 2-3 层分类体系
确保 MECE（互斥且完整）
4. 文献检索策略
核心关键词列表
ArXiv 分类号
Semantic Scholar / Exa 查询策略
Papers With Code 任务/数据集对应
项目文件结构
{space}/{project-name}/
├── AGENTS.md                    # 项目级规则
├── IMPLEMENTATION_PLAN.md       # 分阶段执行计划
├── literature_matrix.md         # 文献矩阵
├── paper_analyses/              # 逐篇分析
├── comparison_tables.md         # 对比表汇总
├── manuscript_draft.md          # 综述草稿
├── review_report.md             # 审校报告
└── manuscript_final.md          # 终稿

模板

详见 references/TEMPLATES.md。

质量检查清单（终审用）
结构完整性
 摘要、引言、结论一致
 所有分类均已覆盖
 每节有过渡段
内容质量
 方法描述准确公正
 对比分析有深度
 局限性和未来方向具体可行
形式规范
 术语一致，缩写首次定义
 参考文献格式统一
 表格和图表编号连续
 60-120 篇参考文献
Weekly Installs
13
Repository
luwill/research-skills
GitHub Stars
549
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
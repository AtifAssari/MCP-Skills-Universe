---
rating: ⭐⭐⭐
title: agent-skill-rules
url: https://skills.sh/qiao-925/qiao-skills/agent-skill-rules
---

# agent-skill-rules

skills/qiao-925/qiao-skills/agent-skill-rules
agent-skill-rules
Installation
$ npx skills add https://github.com/qiao-925/qiao-skills --skill agent-skill-rules
SKILL.md
Agent Skill Rules

以 Agent Skills 官方 Step 1–4 为主流程，并在每一步中嵌入平台无关的治理增强项。

Instructions（分步说明）
Pre-Step：先做能力落位判断（是否应该 skill 化）

在创建、抽取或重构 skill 前，先判断当前需求最适合落到哪一层；不要把“可复用”直接等同于“应该做成 skill”。

落位候选	何时优先选择	不该做什么
自动化工具 / 脚本 / hook / workflow	动作机械、确定、高频、易漏做，且可以稳定脚本化	把固定命令顺序或构建动作仅写成 skill 提醒
项目级规则文件	规则强依赖当前仓库/业务，且对大多数任务默认相关	把项目私有约束伪装成通用 skill
通用 skill	跨项目复用，按需触发，且需要一套认知流程、检查框架或方法论	用 skill 替代脚本、模板工程或工具链
项目私有 skill	只在当前项目成立，但不是每次任务都默认相关，且仍需要专门方法或检查流程	把这类内容强塞进全局常驻规则，污染默认上下文
单次 prompt	一次性需求、短期要求、低复用内容	过早沉淀为长期规则

默认判断顺序：

先判断这是不是可以直接工具化的确定性动作。
再判断它是否是当前项目里长期常驻的默认规则。
如果不是默认常驻，再判断它是否需要被沉淀为通用 skill 或项目私有 skill。
若复用性、稳定性或价值密度不足，则只保留在单次 prompt 中，不做长期沉淀。

创建前至少回答以下问题：

这是跨项目成立，还是只在当前项目成立？
这是机械动作，还是需要模型做认知判断？
这是默认长期生效，还是仅某类任务按需触发？
它能否被脚本、hook、workflow 或命令封装直接自动化？
现在沉淀它的收益，是否明显高于新增的维护成本与上下文负担？

只有当前置判断的结论是“通用 skill”或“项目私有 skill”时，才进入后续 Step 1–4。

Step 1：确认目录结构

每个 skill 至少包含 SKILL.md，可选 scripts/、references/、assets/。完整格式规范见 references/specification.md（来源：agentskills.io/specification）。

skill-name/
├── SKILL.md          # Required
├── scripts/          # Optional
├── references/       # Optional
└── assets/           # Optional


目录名必须与 frontmatter 中的 name 一致（小写、连字符、1–64 字符）。

规则设计时的命名约定（创建/修改 skill 时适用）：除必要外，所有文件名与目录名使用小写。

默认：新建或重命名的文件、目录均使用小写。
「必要」：仅当规范/框架明确要求某命名时不改为小写（如 SKILL.md、README.md、Makefile）。强制规范 > 本约定。
不确定时：先查该规范文档；未写明则使用小写。

增强项（不改变主流程）：

若前置判断结论不是 skill，则停止创建目录结构，改走自动化、项目级规则或单次 prompt 路径。
在建结构前先识别动作类型：create / update / refactor / migrate / audit / deprecate。
根据动作决定是否需要最小结构或完整结构（避免一次性过度创建目录）。
明确 skill 的适用范围：是通用 skill 还是项目私有 skill；若为项目私有，正文必须写清作用边界，避免伪通用化。
避免深层引用链：后续文档设计默认单层引用。
Step 2：编写 frontmatter

必填两项：

name：与目录名一致，仅 a-z、0-9、-，不以 - 开头或结尾，无 --
description：做什么 + 何时用，含关键词，1–1024 字符，第三人称

增强项（不改变主流程）：

description 除"做什么 + 何时用"外，补充触发关键词以提升匹配稳定性。
对维护类动作（update/refactor/migrate/audit/deprecate）也保持可触发语义。
明确平台无关：不在 frontmatter 写入平台私有字段或平台绑定术语。
识别 skill 类型（详见 references/skill-type-taxonomy.md）：判断当前 skill 属于动作型（procedural）还是约束型（declarative），据此调整 description 写法：
动作型：「做什么 + 何时触发」
约束型：「约束什么 + 适用范围」
可选：通过 metadata.type 标注类型（procedural / declarative），便于分类管理。
Step 3：编写正文

YAML 之后为 Markdown 正文。根据 skill 类型选择对应的正文组织方式（详见 references/skill-type-taxonomy.md）：

动作型 skill（procedural） — 沿用官方推荐：

Instructions（分步说明）
Examples（输入/输出示例，若适用）
Edge cases（常见边界情况，若适用）

约束型 skill（declarative） — 不硬套步骤格式，改用声明式组织：

核心原则（必须遵守的底线规则）
行为要求（在具体场景下的行为规范，推荐用对照表）
判断标准（如何判断是否违反原则）
反模式（必须避免的行为，含具体示例）

增强项（不改变主流程）：

正文按"核心规则在前、细节下沉 references"组织（渐进式披露）。
同一规则只维护一处，避免 SKILL.md 与 references/ 重复。
按任务脆弱性选择自由度：高自由度（原则）、中自由度（模式）、低自由度（硬约束）。
维护类任务建议加最小动作表（创建/修改/重构/迁移/审计/弃用）以提升执行一致性。
混合型 skill：识别主导类型，按主导类型组织正文，将次要类型的内容作为补充段落。
Step 3.5：无损迁移（migrate 场景强制）

当动作类型为 migrate 或 merge 时，必须执行无损迁移规则：

迁移以“移动/复制 + 引用重组”为主，不以摘要改写替代原文。
原始规则文本（尤其 SKILL.md 与 references/*）必须完整保留。
若需要聚合入口，聚合层仅做路由与导航，不覆盖原规则细节。
迁移后必须可追溯：能从聚合入口定位到原始文本路径。
Step 4：自检与验证
 目录名 = name
 description 含「做什么」「何时用」和关键词
 引用文件仅一层深度，用相对路径
 若环境支持：skills-ref validate ./skill-name

增强项（不改变主流程）：

 无平台绑定术语污染核心规则（Cloud/IDE/产品私有机制）
 已完成能力落位判断，并确认当前内容不应优先落到自动化、项目级规则或单次 prompt
 维护动作可追踪（变更摘要、影响范围、迁移路径）
 无冗余文档堆叠（与执行无关的 README/更新日志等）
 migrate/merge 场景满足"无损迁移"：原文未被摘要化删改，聚合层仅做导航
 类型一致性：正文组织方式与 skill 类型匹配（动作型用 Instructions，约束型用核心原则/行为要求/判断标准/反模式）
 约束型 skill 未硬套步骤格式，动作型 skill 未缺少执行流程
 若为项目私有 skill，范围边界和项目依赖已显式写明，避免误触发到其他项目
来源与演进路径
来源
第一层来源：Agent Skills 官方文档（结构、frontmatter、渐进式披露、校验约束）。
第二层来源：社区 skill-creator 文档中的通用方法（内容组织、迭代思路、反模式识别）。
吸纳策略
官方 Step 1–4 作为主流程骨架。
新增内容仅作为“增强项”并入各 Step，不替换主流程。
明确剔除 Cloud/IDE/产品私有绑定内容，保留平台无关规则。
定位与边界
本 skill 负责规则标准与治理流程，不绑定特定平台。
默认采用静态规则与文档校验，不依赖固定脚本链路。
关注可迁移、可维护、可审计的 skill 设计质量。
反模式（必须避免）
将规则绑定到特定 Cloud/IDE/产品私有能力。
把机械、确定、可脚本化的动作优先做成 skill，而不是先工具化。
把仅当前仓库成立的默认规则抽成通用 skill，导致伪复用与误触发。
把只出现一次的临时需求沉淀成长期 skill 或全局规则。
把平台安装、打包、发布统计写入规则正文。
在 skill 中堆放与执行无关的辅助文档（如通用 README、更新日志）。
在 SKILL.md 与 references/ 重复维护同一说明。
用精简摘要替代原始规则正文，导致迁移失真与细节丢失。
将约束型 skill 硬套进 Instructions/Step 1-2-3 格式，导致内容牵强或丢失"始终生效"的语义。
将动作型 skill 写成纯声明式，导致缺少可执行的步骤流程。
参考资料
references/specification.md - Agent Skills 基础规范与字段约束
references/anthropic-enhancements.md - 基于 Anthropic skill-creator 的平台无关增强提炼（含来源与剔除策略）
references/skill-type-taxonomy.md - Skill 类型分类学：动作型（procedural）vs 约束型（declarative）的组织方式指导
Weekly Installs
35
Repository
qiao-925/qiao-skills
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
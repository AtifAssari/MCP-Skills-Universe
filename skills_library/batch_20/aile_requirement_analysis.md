---
title: aile-requirement-analysis
url: https://skills.sh/zhucl1006/ailesuperpowers/aile-requirement-analysis
---

# aile-requirement-analysis

skills/zhucl1006/ailesuperpowers/aile-requirement-analysis
aile-requirement-analysis
Installation
$ npx skills add https://github.com/zhucl1006/ailesuperpowers --skill aile-requirement-analysis
SKILL.md
Aile：需求接入（aile-requirement-analysis）
来源原 Skill
来源：superpowers 需求澄清能力（已迁移为 aile-only）
策略：保留“单问题推进 + 结构化分析”流程，并增强 Jira Story 接入契约。
概述

本技能用于阶段 2 的第一步：把 Jira Story 的输入（需求描述、UI 示意、约束）转成可用于计划与设计的结构化材料。

边界约束：

本技能只负责分析、澄清、结构化输出，并产出/更新 docs/plans/{Story-Key}/analysis.md
本技能不修改业务代码、测试代码、规格文档、模块文档
本技能只记录“档案系统回补建议”，真正的回补动作必须留到 aile-writing-plans / aile-executing-plans 阶段
本技能默认不创建 Jira Sub-task
若判断后续可能需要拆子任务，只能在分析结果中给出建议，并提示用户决定是否进入 aile-writing-plans
若当前 Jira 单属于“缺失 / gap / 小范围补漏 / 缺陷修补”类型，分析阶段禁止创建子任务，只输出分析结论与建议
工作流程概览
项目初始化：project-docs-init（创建文档）
      ↓
需求分析：aile-requirement-analysis（结构化需求分析 + 产出 analysis.md）
      ↓
计划制定：aile-writing-plans（设计 + 计划）
      ↓
执行开发：aile-executing-plans 或 aile-subagent-dev（按计划执行 + 人工检查点）
      ↓
交付总结：aile-delivery-report（整理交付材料 + 回链 Story）

Skill流程

理解這個想法：

首先檢查當前專案狀態（文件、文件、最近提交）
一次提出一個問題來完善想法
盡可能選擇多項選擇題，但開放式問題也可以
每個訊息只有一個問題 - 如果某個主題需要更多探索，請將其分解為多個問題
重點理解：目的、約束、成功標準

探索方法：

提出 2-3 種不同的權衡方法
透過對話方式提出選項以及您的建議和推理
以您推薦的選項開頭並解釋原因

展示設計：

一旦您相信自己瞭解了自己正在構建的內容，就可以展示設計
將其分成200-300字的部分
在每個部分之後詢問到目前為止看起來是否正確
涵蓋：架構、組件、數據流、錯誤處理、測試
如果有些事情沒有意義，準備回去澄清
Skill設計後

文件：

將經過驗證的分析結果寫入 docs/plans/{Story-Key}/analysis.md
如果可以的話，使用風格元素：清晰簡潔的寫作技巧
除非使用者明確要求，否則不要提交 git

實施（如果繼續）：

問：“準備好實施了嗎？”
使用超能力：aile-writing-plans 制定詳細的實施計劃
Skill關鍵原則
一次一個問題 - 不要因多個問題而不知所措
首選多項選擇 - 如果可能的話，比開放式更容易回答
YAGNI 無情 - 從所有設計中刪除不必要的功能
探索替代方案 - 在解決之前始終提出 2-3 種方法
增量驗證 - 分部分展示設計，驗證每個部分
保持靈活性 - 當某些事情沒有意義時返回並澄清
输入
Jira Story：Description、Acceptance Criteria（如有）、附件/链接（UI 示意） -（可选）相关 Epic / 依赖 Story -（可选）相关规格/模块文档路径（仅用于判断后续是否需要档案系统回补）
核心产出契约（必须遵守）
计划文件必须落在：docs/plans/{Story-Key}/analysis.md
文件必须包含：
需求理解与风险
用户路径/核心交互
验收条件（AC）初稿：将业务表述改写成可测试条目
隐含需求清单（例如权限、空状态、错误状态、性能/兼容性）
档案系统回补建议：只记录建议回补的文档、原因、优先级，不执行回补
建议的阶段 2 下一步：是否需要 Pencil 设计、是否建议后续拆子任务
子任务决策记录：默认不创建 / 用户已明确要求创建 / 缺失类单据禁止创建
analysis.md 必须明确写出：
是否建议后续回补档案系统：是/否
建议回补的文件路径或文档域（如 docs/specs/PRD.md、docs/modules/payment.md）
回补原因与影响范围
建议在哪个后续计划任务中执行
本技能不得直接修改任何 docs/specs/*、docs/modules/*、docs/guides/* 等档案文件
本技能不得执行 Google Drive 同步或其他档案归档动作
如用户明确要求准备 Jira Comment，必须先生成 ADF（Atlassian Document Format） 草稿；若当前工具链不支持直接提交 ADF，禁止自动回填，降级为“输出 ADF 内容 + 提示人工提交”
子任务边界（必须遵守）
aile-requirement-analysis 阶段禁止创建 Jira Sub-task
子任务创建职责属于 aile-writing-plans，不是本技能
对于“缺失 / gap / 补漏 / 小型修补”类 Jira 单：
只做分析
不拆子任务
不提示自动创建
对于复杂需求，如果分析后判断“后续可能需要拆子任务”：
只能输出“建议后续在 aile-writing-plans 阶段创建”
必须提示用户确认
默认答案为不创建
未获得用户明确授权前，不得调用任何 jira_create_issue / jira_batch_create_issues 能力
Jira 单类型判断（用于子任务建议）

优先按以下信号判断是否属于“缺失类单据”：

Issue Type / 标签 / 自定义字段明确标记为：缺失、gap、bugfix、补漏、修补
标题或描述呈现“补一个缺口 / 修一个缺失项 / 补齐遗漏逻辑”的语义
影响范围单点、边界清晰、无需多角色并行推进

若满足上述条件之一：

结论写为：本单归类为缺失类单据
子任务建议写为：否
原因写明：分析阶段仅输出结论与风险，禁止建立子任务
Jira MCP（可选）

若环境提供 Jira MCP Tool（例如 mcp-atlassian），按以下步骤执行：

读取 Story：jira_get_issue
先生成“需求接入摘要”的 ADF 评论载荷
若当前工具链支持提交 ADF Comment：再执行 Jira 回填
若当前工具链仅支持 Markdown Comment：禁止自动回填，改为在 analysis.md 中附上 ADF 内容并提示人工提交

注意：凭据（API Token）必须通过环境变量注入，不得写入仓库。

Jira Comment 回填格式（强制）

需求接入结果若要回填 Jira，必须先组织成 ADF 结构，至少包含：

{
  "type": "doc",
  "version": 1,
  "content": [
    {
      "type": "heading",
      "attrs": { "level": 2 },
      "content": [{ "type": "text", "text": "[G1] 需求接入摘要" }]
    },
    {
      "type": "bulletList",
      "content": [
        {
          "type": "listItem",
          "content": [
            {
              "type": "paragraph",
              "content": [{ "type": "text", "text": "需求摘要：..." }]
            }
          ]
        }
      ]
    }
  ]
}


至少包含的区块：

需求摘要
风险与隐含需求
规格回补评估
子任务建议与决策
待确认问题

禁止事项：

禁止直接把纯 Markdown 文本当成“ADF 格式”宣称已回填
禁止在未确认工具支持 ADF 的情况下调用自动回填并报成功
档案系统回补建议（必须遵守）

若分析后判断后续需要更新档案系统（如 docs/specs/*、docs/modules/*、docs/guides/*）：

只能在 analysis.md 中记录“建议回补”
必须写明建议回补文件、原因、影响范围、优先级
必须明确说明：本阶段不执行回补，由 aile-writing-plans 转成执行任务
不得在本阶段直接修改文档、同步云端或触发任何归档流程
执行流程
获取 Story Key
读取并复述需求（避免理解偏差）
判断单据类型：是否属于“缺失 / gap / 补漏 / 修补”类
列出不确定项（一次一个问题，优先多选题）
产出结构化摘要以及 analysis.md 分析文件（参考 docs-templates/stage2-analysis-template.md）
输出“档案系统回补建议”（是否建议回补 + 回补文件清单 + 原因）
输出“子任务建议与决策”：
默认：不创建
缺失类单据：禁止创建
若复杂需求需要后续拆分：建议用户确认后，在 aile-writing-plans 阶段处理
若建议后续回补档案系统：只写入 analysis.md，提示由 aile-writing-plans 转成执行任务
（可选）生成 Jira Comment 的 ADF 内容
（可选）仅在用户明确要求且工具明确支持 ADF 时执行 Jira 回填
输出格式补充要求

analysis.md 中必须显式包含：

## 子任务建议与决策

- 单据类型：缺失类 / 常规需求 / 待确认
- 是否建议创建子任务：否 / 是（需用户确认）
- 当前阶段是否允许创建：否
- 用户是否已明确授权：否 / 是
- 说明：...

## 档案系统回补建议

- 是否建议后续回补：是 / 否
- 建议回补文件：
  - `docs/specs/...`
  - `docs/modules/...`
- 回补原因：...
- 优先级：高 / 中 / 低
- 执行阶段：`aile-writing-plans` / `aile-executing-plans`
- 说明：本阶段只记录建议，不执行文档修改


若需 Jira 回填，还必须在 analysis.md 中附上：

## Jira Comment ADF（待回填）

```json
{ ...ADF payload... }
```

Weekly Installs
26
Repository
zhucl1006/ailes…erpowers
First Seen
Feb 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
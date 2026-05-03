---
rating: ⭐⭐⭐
title: customer-journey-mapper
url: https://skills.sh/timlai666/skills/customer-journey-mapper
---

# customer-journey-mapper

skills/timlai666/skills/customer-journey-mapper
customer-journey-mapper
Installation
$ npx skills add https://github.com/timlai666/skills --skill customer-journey-mapper
SKILL.md
Customer Journey Mapper
Overview

Create the final customer journey map in Traditional Chinese from the customer's point of view. This skill is downstream of persona definition and journey-framing work. If no completed persona is available yet, stop and use customer-persona-framer first.

Default output is one Markdown table in transposed vertical form: 項目 | 認知 | 考慮/研究 | 決策/購買 | 使用 | 關係建立

The row order is fixed:

動機
行動
情緒
（服務）接觸點
感受/關鍵時刻
科技服務
行銷方法
目標

動機 must always appear before 行動.

When To Use

Use this skill when:

the user wants the finished customer journey map or CJM table itself
the task already has a clear persona and a product or service
the task includes a handoff_to_customer_journey_mapper block from upstream framing work
the user wants stages, touchpoints, emotions, key moments, marketing methods, or service ideas arranged into one final journey table
the output should be practical for proposals, workshops, internal strategy, or coursework
the user asks for emotion scores, 情緒分數, 情緒曲線, sparkline, or 加減分原因 on any CJM

Do not use this skill when:

the task is only a persona profile, 人物誌, 顧客輪廓, or target audience definition with no final journey map
the task is only 5W1H, touchpoint discovery, or journey pre-analysis; use customer-persona-framer
no completed persona is provided yet; use customer-persona-framer first, then return with the persona or handoff_to_customer_journey_mapper
the task is only a funnel KPI dashboard with no customer narrative
the user wants a service blueprint with backstage operations; this skill is customer-facing only
Input Contract

Required:

顧客輪廓
產品或服務

Optional:

品牌/產業背景
目標市場
目前接觸點
輸出用途
handoff_to_customer_journey_mapper
情緒分數模式 — whether to include emotion scores (see Emotion Score Module below)

If handoff_to_customer_journey_mapper is present:

treat the block as authoritative input
do not re-ask fields that are already present
let explicit user overrides outside the block win over the handoff block

Default assumptions:

produce one core persona journey, not multiple persona versions
if the user provides custom stages, use them
otherwise use the fixed five stages in this skill
Data Sufficiency Gate

If both required inputs are clear enough, generate the table directly. If no completed persona is available, do not draft the final map yet. Route the work to customer-persona-framer first.

If a handoff_to_customer_journey_mapper block contains at least 顧客輪廓 and 產品或服務, generate directly from the handoff.

If information is missing and the user did not ask for speed:

ask concise follow-up questions first
do not generate the final map yet

If information is missing and the user asks for a quick draft, for example:

先做一版
快速版
可先假設
直接幫我生成

Then:

list 3-5 assumptions first
generate the full table after the assumptions
keep the assumptions concrete and business-relevant
Stage Policy

Default stages:

認知
考慮/研究
決策/購買
使用
關係建立

If the user explicitly defines different stages, respect the user-defined stages and preserve the same row order.

Emotion Score Module

Activate this module when the user asks for any of: 情緒分數, 情緒曲線, sparkline, 加減分原因, 1-5分, or requests that the emotion row include scores.

Scoring rules
Scale: 1–5, baseline = 3 (neutral, no strong feeling either way)
Score each stage independently based on what the customer would realistically feel at that point
Score = baseline (3) + sum of all plus factors − sum of all minus factors
Clamp final score to [1, 5]
Plus factors (raise score above 3)
Peer recommendation or social proof encountered
Trial / demo that delivers immediate, visible value
Friction removed (time saved, format correct on first try)
Unexpected delight (feature solves a pain not explicitly mentioned)
Long-term trust formed (data continuity, smooth handover, loyalty reward)
Minus factors (lower score below 3)
Existing negative stereotype about the product category
Unfamiliarity (never heard of this before)
Unresolved cost/value doubt
Fear of making a mistake (wrong format, data loss, learning curve)
Residual friction after use (manual corrections needed, partial failure)
Output for emotion scores

Always produce two separate outputs:

1. Emotion curve row (inside the CJM table)

Split the 情緒 row into two sub-rows:

Sub-row A label: 情緒曲線 — contains a sparkline. Each data point must be positioned at the horizontal center of its stage column.
Sub-row B label: (empty) — contains the per-stage emotion text (real state or state change in customer voice), one cell per stage, background color matching the stage column color.

2. Emotion score detail table (below the CJM)

A separate table with columns: 階段 | 情緒分數 | 加分原因 | 減分原因

情緒分數: bold, center-aligned, e.g. 2 分
加分原因: each factor on its own line, prefixed with ＋, green text
減分原因: each factor on its own line, prefixed with －, red text
If a stage has no plus or minus factors, write （無）
Sparkline in Word documents (.docx)

When the output format is .docx and the emotion score module is active:

Generate a matplotlib PNG:

figsize = (390/72, 90/72) — maps to exactly 390 pt wide (5 stage cols × 78 pt each)
xlim = [0, 5] — each stage column occupies exactly 1 unit
Data points at x = [0.5, 1.5, 2.5, 3.5, 4.5] — centers of each column
Vertical dotted dividers at x = 1, 2, 3, 4 — align with column borders
Dashed baseline at y = 3
Fill area between curve and baseline: blue (#378ADD, alpha 0.20) above; red (#E24B4A, alpha 0.20) below
Point colors: red (#E24B4A) if score < 3, amber (#BA7517) if score < 4, green (#3B6D11) if score ≥ 4
Score labels above each point, bold, matching point color
subplots_adjust(left=0, right=1, top=1, bottom=0) — zero padding so image edges align with column edges
Background #F0F7FF, no axes, no tick marks, no spines
Save at dpi=150, bbox_inches='tight', pad_inches=0

Embed in the CJM table:

Sparkline cell spans all 5 stage columns (columnSpan: 5)
Cell margins: top=0, bottom=0, left=0, right=0 — no padding so image fills exactly to column boundaries
ImageRun transformation: { width: 390, height: 76 } — exact pt dimensions
Text sub-row below: empty label cell + 5 individual cells with emotion text per stage
Sparkline in chat (Markdown / widget)

Render the sparkline using Chart.js with a line chart:

Labels: the five stage names
Scores dataset: computed scores, tension: 0.35, fill: true
Point colors: red if < 3, amber if < 4, green if ≥ 4
Second dataset: baseline [3,3,3,3,3], dashed, no points
Disable default legend; build custom HTML legend above the chart
Show the detail table below the chart as a styled HTML or card layout
Output Contract

Always answer in Traditional Chinese.

Preferred format:

one Markdown table
transposed vertical layout
stages as column headers
fixed row order as below
| 項目 | 認知 | 考慮/研究 | 決策/購買 | 使用 | 關係建立 |
|---|---|---|---|---|---|
| 動機 |  |  |  |  |  |
| 行動 |  |  |  |  |  |
| 情緒 |  |  |  |  |  |
| （服務）接觸點 |  |  |  |  |  |
| 感受/關鍵時刻 |  |  |  |  |  |
| 科技服務 |  |  |  |  |  |
| 行銷方法 |  |  |  |  |  |
| 目標 |  |  |  |  |  |


When the emotion score module is active, replace the single 情緒 row with:

| 情緒曲線 | [sparkline / score sequence] | [→] | [→] | [→] | [→] |
| (空白)   | [emotion text]              | ... | ... | ... | ... |


And append the emotion score detail table after the CJM.

Workflow
Read the direct inputs and any handoff_to_customer_journey_mapper block.
Normalize the effective inputs, using explicit user overrides over handoff values.
Check if emotion score module should be activated.
Read the persona and the product or service.
Infer or confirm the purchase and use context.
Build the journey from the customer's point of view, not the brand's point of view.
Fill the five stages in order unless the user supplied different stages.
Write 動機 before 行動 in every stage.
If emotion score module is active: score each stage, compute plus/minus factors, prepare sparkline.
Make 科技服務, 行銷方法, and 目標 logically connected.
Do a final check for format, language, and customer viewpoint.
Quality Rules
use customer voice and customer logic
avoid brand slogans or empty marketing claims
make each cell specific enough to act on
let 情緒 show a real state or state change
let 感受/關鍵時刻 describe the moment that changes momentum
make 科技服務 an enabler, not a vague buzzword
make 行銷方法 match the stage and touchpoint
make 目標 describe what the service or marketing action is trying to achieve
do not fall back to a horizontal table where each stage is a row
if the input is persona-only or framing-only, do not force a final table; route the work to customer-persona-framer
emotion scores must reflect real customer psychology, not brand optimism — scores below 3 are valid and expected in early stages for unfamiliar products
the largest single-stage score jump in the journey is the Aha Moment; call it out explicitly in the detail table notes or design insights section
Short Example

Input:

顧客輪廓: 忙碌上班族，重視健康但沒時間準備午餐
產品或服務: 健康便當訂閱服務

Output shape (without emotion scores):

| 項目 | 認知 | 考慮/研究 | 決策/購買 | 使用 | 關係建立 |
|---|---|---|---|---|---|
| 動機 | 想找省時又健康的午餐方案 | 想確認價格與口味是否值得 | 想低風險試用避免踩雷 | 想驗證是否真的方便好吃 | 想找到可長期依賴的午餐解法 |
| 行動 | 搜尋健康便當資訊 | 比較方案與評價 | 下單試吃 | 收餐並食用 | 回購與推薦 |


Emotion score example (same persona, scores + factors):

階段	情緒分數	加分原因	減分原因
認知	2.5 分	（無）	－0.5 不確定訂閱是否划算；－0.5 擔心口味踩雷
考慮/研究	2.5 分	＋0.5 朋友有在訂、評價不錯	－0.5 試吃門檻高，怕浪費錢
決策/購買	4 分	＋1 首週折扣降低試錯成本；＋0.5 退訂容易降低風險感	（無）
使用	4.5 分	＋1 餐點準時到、份量足；＋0.5 減少外食煩惱	（無）
關係建立	5 分	＋0.5 每週菜單有變化不膩；＋0.5 推薦給同事獲得認同感	（無）

← 最大跳升：考慮/研究 → 決策/購買（+1.5 分），Aha Moment = 首週折扣消除試錯顧慮

Suggested Prompt

Use $customer-journey-mapper to create the final Traditional Chinese customer journey map from 顧客輪廓 and 產品或服務, or from a handoff_to_customer_journey_mapper block, using a transposed Markdown table where 動機 appears before 行動. If emotion scores are requested, activate the Emotion Score Module to produce a sparkline row and a per-stage detail table with plus/minus factors.

Weekly Installs
12
Repository
timlai666/skills
First Seen
Mar 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
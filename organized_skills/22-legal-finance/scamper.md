---
rating: ⭐⭐
title: scamper
url: https://skills.sh/timlai666/skills/scamper
---

# scamper

skills/timlai666/skills/scamper
scamper
Installation
$ npx skills add https://github.com/timlai666/skills --skill scamper
SKILL.md
SCAMPER 奔馳法創意思考工具
Overview

將任何現有產品、服務、流程或概念，透過 SCAMPER 七大思維維度系統化發想創新方案。

輸出結果包含：

完整的七維度創意清單
每個維度的最佳建議與理由
可執行的優先方案摘要
Input Contract

必填其中至少一項：

target_object — 要創新的目標（產品 / 服務 / 流程 / 商業模式）
innovation_goal — 希望達成的目標（降低成本 / 提升體驗 / 開拓市場...）

可選：

context — 產業背景、競爭環境或使用者痛點
constraints — 現有資源限制（預算 / 技術 / 時間）
depth — 輸出深度：quick（快速概覽）/ full（完整分析，預設）
focus_dimensions — 只展開特定維度，例如 S, C, E
output_language — 預設繁體中文

資訊不足時，列出 3-5 個假設後繼續產出。

Workflow
確認 target_object，釐清其現有形式、功能與使用情境。
依序套用 SCAMPER 七維度，每維度產出 2-3 個具體構想。
評估各構想的可行性與潛力，標記最具突破性的方案。
彙整成 priority_innovations，列出 Top 3 可優先執行的方向。
視需求補上 implementation_note，說明執行注意事項。
Output Contract

固定輸出以下段落：

subject_analysis — 目標物件的現況分析（形式、功能、痛點）
scamper_dimensions — 七維度創意展開（S / C / A / M / P / E / R）
priority_innovations — Top 3 優先創新方向與理由
implementation_note — 執行建議與風險提示（可選）

quick 模式：僅輸出每個維度最強的 1 個構想 + priority_innovations。

預設使用繁體中文 Markdown。

Quick Reference
SCAMPER 七維度定義與提問矩陣：讀 references/01-dimensions-and-questions.md
實戰演練與自然類比進階法：讀 references/02-practice-and-advanced.md
企業案例分析（麥當勞、星巴克）：讀 references/03-case-studies.md
輸出模板：讀 references/04-output-templates.md
Quality Rules
每個維度至少產出 1 個具體且可落地的構想，不能只寫抽象描述。
構想要聚焦在目標物件本身，避免偏離原始問題。
priority_innovations 要有理由，不能只列點。
若使用者指定 focus_dimensions，其他維度簡述即可，聚焦在指定維度深挖。
避免把同一個點子在不同維度重複包裝。
Common Mistakes
每個維度只給泛泛的定義介紹，沒有針對目標物件產出具體構想。
priority_innovations 和七維度內容重複，缺乏整合性判斷。
忽略 constraints，提出不切實際的方案。
過度集中在 Substitute 和 Eliminate，忽略 Adapt 和 Rearrange 的潛力。
Suggested Prompt

Use $scamper to apply the SCAMPER creative thinking framework to a product, service, or concept and generate structured innovation ideas in Traditional Chinese.

Weekly Installs
9
Repository
timlai666/skills
First Seen
10 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
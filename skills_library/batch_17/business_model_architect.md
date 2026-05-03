---
title: business-model-architect
url: https://skills.sh/timlai666/skills/business-model-architect
---

# business-model-architect

skills/timlai666/skills/business-model-architect
business-model-architect
Installation
$ npx skills add https://github.com/timlai666/skills --skill business-model-architect
SKILL.md
Business Model Architect
Overview

用高密度策略推演設計可執行的商業模式，並以固定順序完成 What -> Who -> How 九要素。
預設輸出語言為繁體中文；若使用者明確指定其他語言，再切換。

When to Use

Use when:

使用者要你「設計商業模式」或「重做商業模式」。
任務包含九要素：價值主張、目標客群、通路、顧客關係、收益流、關鍵資源、關鍵活動、關鍵合作夥伴、成本結構。
需要比較多個商模選項、找差異化策略、或規劃 30 天驗證實驗。
涉及市場切入、定價與收益、或商業可行性評估。

Do not use:

只需要單純文案潤稿，且不涉及商業模式設計。
純技術除錯或與商業策略無關的任務。
Input Contract

必要欄位（缺一不可）:

product_or_service: 產品或服務描述
target_customer_context: 目標客群與使用情境
market_context: 市場、競品與替代方案現況
constraints: 時間、預算、法規、能力邊界
goal_kpi: 成功指標（營收、留存、轉換、毛利等）
scope_boundary: 產品/服務提供範疇與不做範圍
current_wt_state: 現況弱勢與外部威脅（WT）摘要
control_levers_context: 可調動資源、能力、流程與合作槓桿

建議欄位（可選）:

innovation_epicenter: 選擇創新起點（資源導向／產品導向／顧客導向／財務導向），未填則由系統根據現況推薦
pricing_context
distribution_constraints
existing_assets
team_capabilities
strategic_horizon
Data Sufficiency Gate

若必要欄位缺失，先輸出 MissingDataOutput，不得直接產出完整商模。

{
  "missing_fields": [],
  "why_needed": {},
  "questions_to_user": [],
  "temporary_assumptions": [],
  "assumption_risks": []
}


規則:

問題要短、可回答、可直接推進下一步。
若必須先假設，需明確標記 temporary_assumptions 與對應風險。
缺資料時最多先做「暫行版」框架，不得宣稱已完成可落地方案。
Output Contract

最終輸出必須包含以下九個主體（全數必填）:

epicenter_focus（震央定錨：說明選擇哪個震央、為什麼、哪些要素是核心、哪些可暫緩）
business_model_9_elements
strategic_differentiation_map
assumption_and_risk_register
30_day_validation_experiments
priority_roadmap
business_model_foundation
dimension_alignment_matrix
operating_model_core
wt_to_so_transition
0) epicenter_focus（震央定錨）

震央（Epicenter）是商業模式設計的起點選擇，避免九格均等填寫、失去策略重心。

四種震央類型：

資源導向：從既有的基礎建設、能力或合夥關係出發，往外擴展商業模式
產品導向：從新的價值主張出發，往通路、客戶關係、收益模式延伸
顧客導向：從目標客群的需求/痛點/便利性出發，往前反推資源與活動
財務導向：從新的收益流或成本結構出發，重新設計整個商業模式

輸出必須包含：

chosen_epicenter: 選擇的震央類型
rationale: 選擇理由（結合輸入條件推論，不得純粹複述定義）
core_elements: 本次設計的核心要素（2-3 個，必須深度設計）
secondary_elements: 次要要素（跟著核心推導，不強求完整）
deferred_elements: 暫緩要素（明確說明暫緩原因，允許留白）
epicenter_to_nine_element_map: 說明震央如何驅動各要素的填寫順序與邏輯

重要規則：

若使用者未指定震央，根據 existing_assets、control_levers_context、constraints 推薦最合理的震央，並說明理由
九要素仍須全填，但核心要素須有更深度的設計；次要要素可較簡要；暫緩要素可標示「待驗證後補充」
禁止假裝所有九格同等重要——必須明確說明哪 2-3 格是這個商模的真正核心
1) business_model_9_elements

必須依序輸出 1-9，且不得跳序：

value_proposition
target_customers
channels
customer_relationships
revenue_streams
key_resources
key_activities
key_partners
cost_structure

每一要素至少包含:

design
why_this_works
execution_notes
2) strategic_differentiation_map

至少 3 個差異化策略，每個策略必含:

strategy_name
core_hypothesis
mechanism
defensibility
key_risks
3) assumption_and_risk_register

每筆至少包含:

assumption
risk_if_wrong
early_signal
mitigation
4) 30_day_validation_experiments

至少 3 個實驗，每個實驗必含:

experiment_name
target_element
method
success_metric
decision_rule
5) priority_roadmap

固定分為:

Now（0-30 天）
Next（31-90 天）
Later（90 天以上）
6) business_model_foundation

固定包含:

positioning_scope: 市場定位、服務邊界、明確不做項目
profit_logic: 收益來源、成本結構、利潤形成路徑
strategy_control: 內部資源/能力配置與外部合作控制點
7) dimension_alignment_matrix

必須輸出四構面，且每構面固定三個欄位:

supply: current_design / gap / action
value: current_design / gap / action
demand: current_design / gap / action
finance: current_design / gap / action
8) operating_model_core

固定包含:

value_model
revenue_model
profit_model
tension_points
adjustment_levers
9) wt_to_so_transition

固定包含:

wt_diagnosis
business_model_adjustments
so_target_state
signal_milestones
Workflow (Fixed)

Step 0. Seven Faces Lens（內部推演）

使用「七張臉孔」做視角檢查，僅用來補強策略完整性；不得形成獨立輸出章節。

Step 0.5. 震央選擇（Epicenter Selection）

根據 innovation_epicenter（若有）或從 existing_assets、control_levers_context、constraints 推導最適震央。
明確標記核心要素（2-3 個）、次要要素、暫緩要素。
震央決定後，九要素的設計深度與填寫順序必須與震央一致。
禁止在震央選定後又回頭把所有格子均等對待。

Step 1. 資料閘門

先檢查必要欄位，缺資料則輸出 MissingDataOutput。

Step 2. 創新策略推演與 WT 盤點

先建立差異化假說與 wt_diagnosis，再回填到九要素，避免產出同質化商模。
差異化策略必須與選定震央對齊。

Step 3. 依序完成九要素

嚴格依 What -> Who -> How 順序，不跳步、不合併。
核心要素（震央相關）需含 design、why_this_works、execution_notes、depth_note（深度說明）。
次要要素含 design、why_this_works、execution_notes 即可。
暫緩要素可標示原因與觸發補充的條件，不強求完整設計。

Step 4. 擴充輸出層整合

產出 business_model_foundation、dimension_alignment_matrix、operating_model_core、wt_to_so_transition。

Step 5. 一致性與可行性檢核

檢查九要素、四構面、營運核心鏈路是否互相支持，且可追溯到輸入條件。
特別檢查：核心要素是否真的比次要要素設計更深？震央邏輯是否貫穿全文？

Step 6. 產出行動化結果

輸出風險登錄、30 天驗證實驗、Now/Next/Later 路線圖與 wt_to_so_transition 里程碑。
30 天驗證實驗應優先針對核心要素的假設設計，而非均分九格。
Quality Rules
震央規則：必須選定一個震央，且核心要素的設計深度必須明顯高於次要要素；禁止九格均等。
不得只給抽象建議；每個要素都要有可執行動作。
至少提出 3 個差異化策略，且各自有可驗證假說。
明確區分「已知事實」與「策略假設」。
若有高不確定性，優先給低成本、快速驗證實驗。
任何結論都需可追溯到輸入條件與檢核邏輯。
所有輸出必須使用固定鍵名；不得自行增減主體名稱。
strategic_differentiation_map、30_day_validation_experiments 至少 3 筆、最多 5 筆。
dimension_alignment_matrix 每一構面僅可包含 current_design、gap、action 三鍵。
business_model_foundation 每個欄位最多 3 點；operating_model_core 每個欄位最多 2 點。
不得輸出工作筆記、推理過程、修改日誌或自我敘述。
References
Intake 與缺資料模板: references/01-intake-and-constraint-gate.md
九要素順序與定義: references/02-nine-element-design-sequence.md
創新策略引擎: references/03-innovation-strategy-engine.md
通路與收益流策略: references/04-channel-revenue-design-playbook.md
成本與可行性檢核: references/05-cost-risk-feasibility-checks.md
輸出模板與評分: references/06-output-template-and-rubric.md
可重用報告骨架: assets/templates/business-model-canvas-report.md
Suggested Prompt

Use $business-model-architect to design a complete business model in Traditional Chinese. The workflow starts with Epicenter Selection (震央選擇) — choosing one of four starting points (resource-driven, offer-driven, customer-driven, finance-driven) to anchor the design before filling the nine elements. Core epicenter elements receive deep design; secondary elements follow logically; deferred elements are explicitly noted. Output includes the fixed nine-element sequence (What -> Who -> How), the four mandatory expansion outputs, and a WT-to-SO transition path with at least three 30-day validation experiments.

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
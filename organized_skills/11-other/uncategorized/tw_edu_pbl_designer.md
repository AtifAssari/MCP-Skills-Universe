---
rating: ⭐⭐
title: tw-edu-pbl-designer
url: https://skills.sh/fw1201/tw-edu-skills/tw-edu-pbl-designer
---

# tw-edu-pbl-designer

skills/fw1201/tw-edu-skills/tw-edu-pbl-designer
tw-edu-pbl-designer
Installation
$ npx skills add https://github.com/fw1201/tw-edu-skills --skill tw-edu-pbl-designer
SKILL.md
PBL 專題式學習設計工具
Step 0：讀取文件
references/pbl_design_guide.md
/mnt/skills/public/docx/SKILL.md

概念對齊協議（必要前置步驟）： ../../tw_edu_concept_alignment.md → 在執行任何工作前，先完成概念對齊確認卡。

Step 1：資訊收集
核心問題或主題？
年級與科目（單科/跨科）？
時間規模（週數/節數）？
最終成品形式（報告/展覽/影片/提案）？
小組或個人？
Step 2：生成 PBL 設計文件
python scripts/generate_pbl.py \
  --question "[驅動問題]" \
  --subject "[科目]" --grade "[年級]" \
  --weeks [週數] --product "[最終成品形式]" \
  --output "/mnt/user-data/outputs/PBL設計方案.docx"

PBL 文件結構（Buck Institute 框架）
專題概述（驅動問題、核心知識、21世紀技能）
學習進度規劃（里程碑時間表）
鷹架設計（需要教的什麼）
小組任務分工框架
形成性評量節點
最終成品評量規準
發表計畫
反思與修正機制
年級適應 + 引導式收集（v2.0 更新）
自動年級偵測

從使用者輸入辨識學習階段（國小/國中/高中），自動調整：

教學語言複雜度與詞彙難度
布魯姆認知層次分布
活動設計的自主程度
課綱代碼學段後綴（-E- / -J- / -U-）

詳見：../../tw_edu_grade_adapter.md

引導式資訊收集

啟動時執行漸進式三輪問答，確保取得充足資訊再開始任務。 詳見：../../tw_edu_guided_collection.md

MCP 連接器
Claude Code ／ Claude.ai（Pro/Team/Enterprise）
WebSearch（自動啟用）：
  搜尋最新課綱資料、教材資源、時事素材

Google Drive（若已連接，Settings → Connectors）：
  直接從 Drive 讀取現有教材
  完成後直接儲存輸出文件到 Drive

其他平台（Codex / gemini-cli）

MCP 不可用，Claude 使用訓練知識執行，並提示使用者手動儲存。

MCP 整合更新（v3.0）

讀取全域策略文件：../../tw_edu_mcp_strategy.md

本 Skill 適用的 MCP 最佳化

WebSearch（已啟用）： 搜尋最新課綱資料、教學素材、時事情境。

Canva MCP（若已連接）： 使用者說「幫我做更美觀的版本」或「Canva 設計」時： → 呼叫 Canva:generate-design 生成高設計感版本 → 優先適用：教案封面、簡報、學習單封面

Google Drive（若已連接）： 文件生成後詢問：「要上傳到 Google Drive 嗎？」 → 確認後上傳，返回分享連結 → 不修改任何現有檔案的分享權限

安全原則： 所有 MCP 寫入操作執行前，必須顯示確認摘要並等待使用者確認。

Weekly Installs
9
Repository
fw1201/tw-edu-skills
GitHub Stars
4
First Seen
Apr 10, 2026
Security Audits
Gen Agent Trust HubPass
SnykWarn
---
title: tw-edu-formative-assessment
url: https://skills.sh/fw1201/tw-edu-skills/tw-edu-formative-assessment
---

# tw-edu-formative-assessment

skills/fw1201/tw-edu-skills/tw-edu-formative-assessment
tw-edu-formative-assessment
Installation
$ npx skills add https://github.com/fw1201/tw-edu-skills --skill tw-edu-formative-assessment
SKILL.md
形成性評量工具生成器
Step 0：讀取文件
/mnt/skills/public/docx/SKILL.md

概念對齊協議（必要前置步驟）： ../../tw_edu_concept_alignment.md → 在執行任何工作前，先完成概念對齊確認卡。

Step 1：資訊收集
科目、年級、主題？
評量目的（課前診斷/課中監控/課後出口）？
工具類型？
出口票（Exit Ticket）
KWL 表（Know-Want-Learned）
概念理解自評量表
課前知識診斷測驗（3-5 題）
學習收穫與困惑記錄單
Step 2：生成評量工具
python scripts/generate_formative.py \
  --subject "[科目]" --grade "[年級]" --topic "[主題]" \
  --type "[exit_ticket/kwl/self_check/diagnostic]" \
  --output "/mnt/user-data/outputs/[主題]_形成性評量.docx"

輸出設計
每頁設計一種工具
一頁排版 2-4 份（方便裁切分發）
留白足夠學生書寫
包含教師觀察記錄表（另一頁）
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
Gen Agent Trust HubFail
SocketPass
SnykWarn
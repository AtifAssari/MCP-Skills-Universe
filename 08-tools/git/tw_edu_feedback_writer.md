---
title: tw-edu-feedback-writer
url: https://skills.sh/fw1201/tw-edu-skills/tw-edu-feedback-writer
---

# tw-edu-feedback-writer

skills/fw1201/tw-edu-skills/tw-edu-feedback-writer
tw-edu-feedback-writer
Installation
$ npx skills add https://github.com/fw1201/tw-edu-skills --skill tw-edu-feedback-writer
SKILL.md
學生回饋評語生成工具
Step 0：讀取文件
references/feedback_principles.md
/mnt/skills/public/docx/SKILL.md

概念對齊協議（必要前置步驟）： ../../tw_edu_concept_alignment.md → 在執行任何工作前，先完成概念對齊確認卡。

Step 1：資訊收集
評量任務類型（作文/作業/報告/學習歷程）？
年級與科目？
評量規準有哪些向度？
學生表現描述（教師口述，Claude 整理成評語）？
需要幾位學生的評語？
Step 2：生成評語文件
python scripts/generate_feedback.py \
  --task "[任務名稱]" --subject "[科目]" --grade "[年級]" \
  --students "[學生1描述|學生2描述|...]" \
  --output "/mnt/user-data/outputs/學生評語.docx"

評語原則（三明治回饋法）
肯定優點（具體說明做得好的地方）
指出改進方向（具體、可操作的建議）
鼓勵展望（給予信心與期待）
輸出格式
每位學生一個回饋區塊
含評量指標評等（優/良/可/需加強）
字數約 100-150 字/人
可輸出成 Word 表格便於逐一填入
年級適應 + 引導式收集（v2.0 更新）
年級偵測 + 語氣調整
學習階段	評語語氣	建議字數/人
國小	溫暖鼓勵，避免批評性語言	60-80 字
國中	平衡正向與建設性建議	80-120 字
高中	具體、有深度，連結學習目標	100-150 字
引導式收集（第一輪）
Q1: 「這是哪種任務的評語？（作文/報告/口頭/作業/其他）」
Q2: 「請描述每位學生的表現特點。
    （可批量：學生甲：___，學生乙：___）」

第二輪
Q3: 「用哪些評量向度？（未提供則依任務類型自動設定）」

MCP 連接器（平台差異）
Claude Code ／ Claude.ai（Pro/Team/Enterprise）

Gmail MCP（若已連接）：

用途：將個別學生評語草擬為家長信件並存入 Gmail 草稿
      適合需要「個別通知家長」的情境

流程：
  1. Claude 生成全班評語文件
  2. 詢問：「需要把個別評語轉成寄給家長的信嗎？
            請提供需要個別通知的學生家長 Email。」
  3. 若確認：批量建立 Gmail 草稿（每位家長一封）
  ⚠️ Claude 只存草稿，不自動發送

其他平台

輸出文字供手動複製。

Weekly Installs
10
Repository
fw1201/tw-edu-skills
GitHub Stars
4
First Seen
Apr 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
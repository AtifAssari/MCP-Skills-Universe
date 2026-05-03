---
title: report-writing
url: https://skills.sh/u9401066/copilot-capability-manager/report-writing
---

# report-writing

skills/u9401066/copilot-capability-manager/report-writing
report-writing
Installation
$ npx skills add https://github.com/u9401066/copilot-capability-manager --skill report-writing
SKILL.md
讀寫報告能力 (Report Writing)
描述

組合能力：整合 PDF 讀取、筆記撰寫、內容驗證和格式化，提供完整的報告撰寫流程。

┌─────────────────────────────────────────────────────────────────────┐
│                  Report Writing (組合能力)                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌────────────┐   ┌────────────┐   ┌──────────────┐   ┌──────────┐ │
│  │ pdf-reader │ → │ note-writer│ → │content-valid.│ → │report-fmt│ │
│  │  (讀取)    │   │  (撰寫)    │   │   (驗證)     │   │ (格式化) │ │
│  └────────────┘   └────────────┘   └──────────────┘   └──────────┘ │
│        │               │                  │                │        │
│        ▼               ▼                  ▼                ▼        │
│    原始文本        結構化筆記          驗證報告         最終報告    │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │                    🔄 迴圈處理多個 PDF                        │   │
│  └──────────────────────────────────────────────────────────────┘   │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘

觸發條件
「寫報告」「整理這些文獻」「產出讀書報告」
"write report", "create document", "summarize papers"
有 PDF 或文獻內容需要整理成報告
組成技能
順序	技能	路徑	迴圈
1	pdf-reader	.claude/skills/pdf-reader/SKILL.md	每個 PDF 一次
2	note-writer	.claude/skills/note-writer/SKILL.md	每個來源一次
3	content-validator	.claude/skills/content-validator/SKILL.md	單次
4	report-formatter	.claude/skills/report-formatter/SKILL.md	單次
執行流程
標準流程
Step 1: 收集來源材料
    ↓
    PDF 檔案 / PMID 清單 / URL
    ↓
Step 2: 讀取來源 (pdf-reader) [🔄 迴圈]
    ↓
    for each source:
        content = pdf-reader.read(source)
        checkpoint.update(source, "read")
    ↓
Step 3: 撰寫筆記 (note-writer) [🔄 迴圈]
    ↓
    for each content:
        note = note-writer.write(content)
        checkpoint.update(source, "noted")
    ↓
Step 4: 整合筆記
    ↓
    combined_notes = merge_notes(all_notes)
    ↓
Step 5: 驗證內容 (content-validator)
    ↓
    validation_report = content-validator.validate(combined_notes, sources)
    if validation_report.has_errors:
        fix_errors()
    ↓
Step 6: 格式化 (report-formatter)
    ↓
    final_report = report-formatter.format(combined_notes)
    ↓
Output: 最終報告 (.md)

迴圈處理多 PDF
# Checkpoint 追蹤處理進度
checkpoint = {
    "capability": "report-writing",
    "total_sources": len(pdf_files),
    "processed": []
}

for pdf in pdf_files:
    # Step 1: 讀取
    content = pdf_reader.read(pdf)
    
    # Step 2: 撰寫筆記
    note = note_writer.write(content)
    
    # Step 3: 更新 checkpoint
    checkpoint["processed"].append({
        "file": pdf,
        "status": "completed",
        "note_path": note.path
    })
    save_checkpoint(checkpoint)
    
    # 如果處理中斷，可從 checkpoint 恢復

輸出格式
報告模板
# [報告標題]

> **建立日期**: 2024-12-22
> **來源數量**: 5 篇文獻
> **驗證狀態**: ✅ 已驗證

---

## 摘要

[整體摘要，綜合所有來源的重點]

## 1. 背景

[研究背景和問題陳述]

## 2. 方法

[各研究的方法概述]

### 2.1 研究設計
### 2.2 納入排除標準
### 2.3 結果指標

## 3. 結果

[主要發現的整合]

### 3.1 [主題 1]
### 3.2 [主題 2]
### 3.3 [主題 3]

## 4. 討論

[綜合討論和比較]

## 5. 結論

[主要結論和建議]

## 6. 參考文獻

1. Author A, et al. (2024). Title. Journal. PMID: 12345678
2. Author B, et al. (2023). Title. Journal. PMID: 87654321
...

---

## 附錄：驗證報告

| 來源 | 驗證狀態 | 備註 |
|------|----------|------|
| Paper 1 | ✅ | 所有數據已核實 |
| Paper 2 | ⚠️ | 統計值已修正 |

Checkpoint 機制
{
  "capability": "report-writing",
  "status": "in-progress",
  "started_at": "2024-12-22T10:00:00",
  "progress": {
    "total_sources": 5,
    "read": 3,
    "noted": 2,
    "validated": 0,
    "formatted": 0
  },
  "currentSource": "paper3.pdf",
  "currentStep": "reading",
  "processed": [
    {"file": "paper1.pdf", "status": "noted", "note": "notes/paper1.md"},
    {"file": "paper2.pdf", "status": "noted", "note": "notes/paper2.md"},
    {"file": "paper3.pdf", "status": "reading"}
  ],
  "errors": []
}

使用範例

範例 1：單篇報告

用戶：「讀取 paper.pdf 並寫成讀書報告」
執行：
1. pdf-reader: 讀取 PDF
2. note-writer: 撰寫結構化筆記
3. content-validator: 驗證準確性
4. report-formatter: 格式化輸出


範例 2：多篇整合報告

用戶：「整合這 5 篇 PDF 寫成綜述報告」
執行：
1. for each PDF:
   - pdf-reader: 讀取
   - note-writer: 筆記
   - checkpoint: 記錄進度
2. 整合所有筆記
3. content-validator: 驗證
4. report-formatter: 格式化


範例 3：從 PMID 產出報告

用戶：「根據這些 PMID 寫報告：38353755, 37864754」
執行：
1. 取得全文連結
2. pdf-reader: 讀取 PMC 全文
3. note-writer + validator + formatter

相關能力
literature-retrieval - 文獻檢索能力
literature-review (cp.write_report) - 文獻評讀能力 = literature-retrieval + 本能力
Weekly Installs
45
Repository
u9401066/copilo…-manager
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
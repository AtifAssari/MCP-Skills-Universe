---
rating: ⭐⭐
title: animate-performance
url: https://skills.sh/tim80411/ai-agent-extension/animate-performance
---

# animate-performance

skills/tim80411/ai-agent-extension/animate-performance
animate-performance
Installation
$ npx skills add https://github.com/tim80411/ai-agent-extension --skill animate-performance
SKILL.md
Adobe Animate Performance Optimization
Overview

針對 Adobe Animate + CreateJS 專案進行系統性效能優化，識別並修復常見效能瓶頸。

When to Use This Skill
完成 Adobe Animate 專案時進行最終效能審查
應用程式出現卡頓、記憶體使用過高、或響應變慢
重構現有程式碼以改善效能
7 大效能問題

Required References:

references/common-patterns.md - 效能反模式識別與檢測策略
references/fix-strategies.md - 具體修復程式碼範例
#	問題類型	檢測關鍵字	優先級
1	Event Listener Memory Leaks	addEventListener 無對應 removeEventListener	P0
2	Redundant Event Bindings	init 函數中重複註冊事件	P1
3	Excessive Per-Frame Execution	Ticker.addEventListener("tick") 內有迴圈	P1
4	MovieClip Lifecycle Issues	MovieClip 建立後無 .stop()	P2
5	Excessive stage.update()	stage.update() 在迴圈內	P1
6	Missing Cache	複雜靜態圖形未使用 cache()	P3
7	Resource Management	一次載入所有資源、音訊未清理	P3

詳見 references/common-patterns.md 取得完整的檢測模式與程式碼範例。

Performance Analysis Workflow

Required References:

references/common-patterns.md - 問題識別
references/fix-strategies.md - 修復實作
references/best-practices.md - 程式碼審查標準
Phase 1: Automated Scanning

使用 performance-analyzer agent 掃描程式碼庫：

自動檢測 7 大效能問題
產出詳細報告（含檔案位置與行號）
提供自動修復選項
Phase 2: Manual Review

針對需要判斷的問題進行人工審查：

根據 agent 報告進行情境優化
查閱 references/fix-strategies.md 取得修復範例
Phase 3: Testing

驗證改善效果：

使用 NW.js 或瀏覽器 DevTools Performance 面板
監控記憶體使用趨勢
檢查互動時的 FPS
Triggering the Performance Analyzer
"Check this project for performance issues"
"Optimize the performance"
"檢查效能問題"
"效能優化"


performance-analyzer agent 會：

掃描 js/ 目錄下所有 JavaScript 檔案
識別 7 大效能問題
產出報告（含具體位置）
詢問是否要自動套用修復
Weekly Installs
10
Repository
tim80411/ai-age…xtension
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass
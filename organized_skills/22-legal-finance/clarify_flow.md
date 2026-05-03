---
rating: ⭐⭐
title: clarify-flow
url: https://skills.sh/ting-s515/skills/clarify-flow
---

# clarify-flow

skills/ting-s515/skills/clarify-flow
clarify-flow
Installation
$ npx skills add https://github.com/ting-s515/skills --skill clarify-flow
SKILL.md
Clarify Flow Description
目的

將模糊、口語化或結構鬆散的流程說明，重寫為精確、結構化、可直接對應 Mermaid 流程圖節點的格式，確保每個步驟、判斷、分支都清晰可追蹤。

適用情境
從會議紀錄或需求訪談中整理出的粗略流程說明
口語化描述的業務邏輯，需轉為正式規格
準備繪製 Mermaid 流程圖前的前置整理
流程說明需要讓非原作者也能看懂
優化原則
1. 結構化分區

每個流程必須包含以下區塊：

區塊	說明	對應 Mermaid 元素
比對條件	列出該流程用來匹配資料的關鍵欄位	流程起始節點的輸入條件
處理流程	以編號步驟描述完整邏輯	流程圖中的處理節點與判斷菱形
2. 步驟撰寫規範

每個編號步驟應遵循以下原則：

原則	說明	範例
明確資料來源	說明從哪張表或哪個服務取得資料	「查詢 InsertAlert 資料表中…」
列舉篩選條件	逐一列出 include / exclude 條件	「排除 SendDeadline 小於當前主機時間的資料」
Null 值處理	明確說明 NULL 或空值時的行為	「SendDeadline 為 NULL 時，視為無截止時間限制，不排除」
排序規則	指定排序欄位與方向	「符合條件的資料依 pk Id 由小到大排序」
欄位名稱反引號	欄位名稱使用反引號標記	MainCategory、SubCategory
3. 判斷分支撰寫規範

遇到 if / else 邏輯時：

原則	說明	範例
粗體標記分支	用粗體標示每個分支的條件	Key 存在時（快取期間內）：
縮排呈現層級	子分支用縮排或清單表示	- **未過期：** 將該筆資料加入待發送清單
明確結束點	說明何時結束遍歷或跳出流程	「結束遍歷」、「繼續往下遍歷下一筆資料」
無符合結果	說明全部不符合時的行為	「遍歷完該批次所有資料，本次無符合條件資料」
4. 迴圈/遍歷撰寫規範
原則	說明
明確遍歷對象	說明遍歷的資料集合是什麼
迴圈內判斷	每次迭代要檢查什麼條件
提前退出	滿足什麼條件時結束遍歷
遍歷完畢	全部遍歷完無符合時的處理
優化前後對照範例

參考 references/repeat.md，以一份高複雜度的範例展示所有優化原則的實際應用（涵蓋：步驟串接、多層分支、迴圈遍歷、外部服務互動）。

輸出規範
保留原始語意：不改變業務邏輯，只改善表達方式
一個流程一個區塊：每種策略或流程獨立一個小節，包含比對條件與處理流程
步驟連貫可追蹤：步驟之間可用「承接第 N 點」串接，確保讀者能追蹤上下文
可直接對應 Mermaid：每個步驟對應一個處理節點，每個判斷對應一個菱形節點，每個分支對應一條連線
輸出後更新指定文檔：將優化後的流程說明寫回用戶指定的檔案路徑
Weekly Installs
10
Repository
ting-s515/skills
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
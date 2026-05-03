---
title: code-review
url: https://skills.sh/cityfish91159/maihouses/code-review
---

# code-review

skills/cityfish91159/maihouses/code-review
code-review
Installation
$ npx skills add https://github.com/cityfish91159/maihouses --skill code-review
SKILL.md
代碼審查 Skill

⛔ 原則：不是「勾清單」，是「逐行質疑」。最嚴苛標準，分數可為負。

使用時機
任務標記完成前
PR 合併前
用戶要求 review 時
評分標準（可為負分，嚴苛版）

預設扣分制，沒證據證明沒問題就扣分。

基礎分：100 分，逐項扣分，無下限
類別	扣分項目	扣分
基礎檢查失敗		
	typecheck 失敗（每個錯誤）	-20
	lint 錯誤（每個錯誤）	-10
	lint 警告（每個警告）	-5
	測試失敗（每個失敗）	-30
	使用 any（每處）	-15
	使用 @ts-ignore（每處）	-20
	使用 as unknown as（每處）	-15
生存測試失敗		
	Log 無上下文	-10
	敏感資料洩漏 (Log)	-50
	N+1 查詢	-30
	多步驟寫入無 Transaction	-40
	巢狀深度 > 3	-10
	沒引用需求文件證明意圖	-20
架構違規		
	UI 直接呼叫 DB (Logic in UI)	-30
	繞過 Service Layer	-30
	God Function (職責不清)	-20
測試品質差		
	測試實作細節而非行為	-20
	Mock 濫用 (沒測到東西)	-20
	斷言無效 (e.g. expect(true).toBe(true))	-20
反模式 (Anti-Patterns)		
	殭屍代碼 (註解掉的代碼塊)	-10
	過度設計 (YAGNI)	-10
	重複造輪子 (未使用現有 helper)	-10
致命缺陷		
	安全漏洞（SQL注入、XSS）	-50

...（省略中間內容，保持原有 Step 7）...

7.4 惡魔辯護（Anti-Laziness）
 攻擊測試：只要能想到一種讓這段代碼崩潰的方法，就必須提出。
 證據強制：必須引用需求文件的具體段落證明代碼意圖，沒引用扣 20 分。
Step 8：架構與反模式檢查（Architecture Guardrails）

防止代碼腐爛，從源頭擋住爛設計：

8.1 架構防護
 Logic/UI 分離：
❌ 在 .tsx 中直接寫 SQL/Supabase query -> 扣 30 分
✅ 必須封裝在 src/services/ 或 api/
 分層原則：
❌ 前端跳過 BFF/API 直接打資料庫（除非特定 RLS 場景） -> 扣 30 分
❌ God Function（一個函數做驗證+DB+通知+計算） -> 扣 20 分（應拆分）
8.2 測試品質審計（Test Semantic Audit）
 有效測試：
❌ expect(true).toBe(true) 或只測 toBeDefined() -> 扣 20 分
❌ 測試充滿 mock，根本沒測到邏輯 -> 扣 20 分
 行為驗證：
❌ 測試實作細節（如 toHaveBeenCalledWith 內部私有函數） -> 扣 20 分
8.3 拒絕反模式（Anti-Patterns）
 殭屍代碼 (Zombie Code)：
❌ 提交包含大段被註解掉的代碼 -> 扣 10 分
 重複造輪子：
❌ 專案已有 formatDate 卻自己重寫 -> 扣 10 分
 過度設計 (YAGNI)：
❌ 寫了「未來可能會用到」但現在沒用的參數/函數 -> 扣 10 分
審查報告格式（必須輸出）

| | 硬編碼密鑰/Token | -50 | | | 資料遺失風險（事務不完整） | -40 | | | 競態條件 | -40 | | | 函數名稱與實作不符 | -30 | | 嚴重缺陷 | | | | | 未處理 Supabase/API error | -20 | | | 邊界值未處理（null/undefined） | -15 | | | 空陣列未處理 | -15 | | | 隱式假設未驗證 | -15 | | 中等缺陷 | | | | | 錯誤訊息顯示技術細節給用戶 | -10 | | | 缺少 console.error 日誌 | -10 | | | 魔術數字未抽成常數 | -5 | | | 函數超過 50 行 | -5 | | | 複雜邏輯無註解 | -5 | | 輕微缺陷 | | | | | 命名不清楚 | -3 | | | 可抽成 helper 但沒抽 | -3 | | | 未使用的 import/變數 | -2 |

分數等級
分數	等級	結論
90-100	🟢 優秀	可合併
80-89	🟡 良好	修正後可合併
60-79	🟠 需改進	必須修正
0-59	🔴 不合格	重寫
<0	⛔ 災難	拒絕，需嚴肅檢討
Step 1：理解意圖

對每個函數/API，回答：

問題	你的答案
這段代碼要解決什麼問題？	
對應工單的哪個需求？	
它在系統中扮演什麼角色？	

如果答不出來，先讀需求文件。

Step 2：追蹤資料流
輸入來源 → [這段代碼] → 輸出去向
    ↓              ↓           ↓
 可能的值？    如何轉換？    誰使用？


檢查：

輸入可能是 null/undefined 嗎？
輸入可能是空陣列嗎？
輸入可能超出預期範圍嗎？
Step 3：質疑假設

列出所有隱式假設，逐一驗證：

假設	成立嗎？	不成立會怎樣？
資料庫一定成功回應		
陣列一定有元素		
用戶一定已登入		
ID 一定存在		
Step 4：模擬極端
4.1 邊界值
輸入	預期	實際	有處理？
null			✅/❌
undefined			✅/❌
""			✅/❌
[]			✅/❌
負數			✅/❌
4.2 併發
兩個請求同時呼叫，會發生什麼？

4.3 中途失敗
執行到第 N 行失敗，系統狀態會壞掉嗎？

Step 5：名稱 vs 實作對照

拆解函數名稱，逐一驗證：

名稱片段	承諾	實作有做到？
		✅/❌
		✅/❌
		✅/❌

任何 ❌ 直接 -30 分。

Step 6：檢查可維護性
問題	答案
六個月後有人看得懂嗎？	
有沒有魔術數字需要抽成常數？	
有沒有複雜邏輯需要加註解？	
改動這裡會影響哪些地方？	
有沒有重複代碼可以抽成 helper？	
Step 7：生產環境生存測試（Survival Test）

用最嚴苛的標準檢視這段代碼在生產環境的表現：

7.1 可觀測性（Observability）
 Log 有上下文嗎？
❌ console.error('Failed') -> 扣 10 分
✅ console.error('Failed', { caseId, error })
 敏感資料洩漏？
❌ console.log(userObject) -> 扣 50 分
❌ 印出 password / token / secret -> 扣 50 分
7.2 事務完整性（Data Integrity）
 多步驟寫入有用 Transaction 嗎？
❌ await A; await B; (中間失敗資料會不一致) -> 扣 40 分
✅ 使用 Supabase RPC 或單一原子操作
7.3 效能地雷
 N+1 查詢？
❌ items.map(async item => await db.get(item.id)) -> 扣 30 分
✅ db.in('id', ids)
 複雜度炸彈？
❌ 巢狀深度 > 3 層 (if { for { if { ... } } }) -> 扣 10 分
7.4 惡魔辯護（Anti-Laziness）
 攻擊測試：只要能想到一種讓這段代碼崩潰的方法，就必須提出。
 證據強制：必須引用需求文件的具體段落證明代碼意圖，沒引用扣 20 分。
審查報告格式（必須輸出）
# 代碼審查報告

## 評分：XX/100 🟢/🟡/🟠/🔴/⛔

## 審查檔案

- `path/to/file.ts`

## 基礎檢查

- typecheck: ✅/❌ (X 錯誤)
- lint: ✅/❌ (X 錯誤, X 警告)
- test: ✅/❌ (X 失敗)
- any 使用: X 處
- @ts-ignore: X 處

## 扣分明細

| 扣分     | 原因     | 位置 |
| -------- | -------- | ---- |
| -XX      | [原因]   | L123 |
| -XX      | [原因]   | L456 |
| **總計** | **-XXX** |      |

## 問題清單

### ⛔ 致命

1. ...

###  嚴重

1. ...

### 🟡 建議

1. ...

## 結論

[能不能合併，為什麼]

執行原則
✅ 必須跑完全部流程，即使基礎檢查失敗
✅ 必須列出所有問題，不可遺漏
✅ 必須給出總分，讓用戶知道這次實作幾分
✅ 問題列在對話框，不要亂改或新增檔案
✅ 每一步驟都要在對話框上即時呈現，不可隱瞞
✅ Agent 連審核都偷懶幫我記在第一行：若未遵守上述原則，必須在報告開頭自我揭露。
🛑 強制暫停機制 (Mandatory Checkpoints)

為了確保審查品質，Agent 必須在以下階段結束時呼叫 notify_user 暫停執行，等待用戶確認：

Checkpoint A：基礎檢查結束後
動作：回報基礎檢查（Lint/Test/Typecheck）的執行結果與目前扣分。
目的：讓用戶決定在基礎設施不穩定的情況下，是否仍要進行深度審查。
Checkpoint B：邏輯與假設分析後 (Step 4 結束)
動作：回報 Step 1~4 的分析結果（意圖、假設、邊界模擬）。
目的：確認 Agent 對代碼意圖的理解正確，糾正錯誤的假設。
Checkpoint C：發現致命問題時 (FATAL Trigger)
條件：這是一次性的觸發。只要審查過程中發現任何 -50 分 的項目（如 SQL 注入、個資洩漏）。
動作：立即暫停，不用等到最後。
目的：致命錯誤可能導致後續審查無意義，優先修復。
禁止事項
❌ 沒跑基礎檢查就開始審查
❌ 發現問題但略過不報告
❌ 跳過任何 Step
❌ 不給分數
❌ 分數虛高（沒證據就給高分）
❌ 用「應該沒問題」當結論
❌ 只報告部分問題
Weekly Installs
18
Repository
cityfish91159/maihouses
GitHub Stars
1
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
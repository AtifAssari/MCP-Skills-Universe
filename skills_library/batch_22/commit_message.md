---
title: commit-message
url: https://skills.sh/gn00678465/agentskills/commit-message
---

# commit-message

skills/gn00678465/agentskills/commit-message
commit-message
Installation
$ npx skills add https://github.com/gn00678465/agentskills --skill commit-message
SKILL.md
慣例式提交與分支助手

根據 Conventional Commits 1.0.0-beta.4 規範，分析 git staged changes 並自動生成繁體中文 commit message 與建議的分支名稱。

核心功能
分支建議 (Branch Suggestion)：根據變更檔案內容自動生成語意化的 Git 分支名稱。
提交訊息 (Commit Message)：自動生成符合 Conventional Commits 規範的繁體中文提交訊息。
主分支保護 (Main Branch Protection)：防止在 main/master 直接提交，並引導切換至建議分支。
原子化拆分引導 (Atomic Split Guide)：偵測高複雜度變更，引導使用者分批提交。

完整規範請參考 references/conventional-commits-spec.md

組成結構
<類型>[可選的作用範圍]: <描述>

[可選的正文]

[可選的頁腳]

類型（Type）

根據官方規範，以下兩種類型具有語意化版本意義：

類型	SemVer	說明
feat	MINOR	新增功能
fix	PATCH	修正臭蟲

以下類型由 @commitlint/config-conventional 推薦使用：

類型	說明
docs	文件更新
style	程式碼格式調整（不影響功能）
refactor	重構程式碼
perf	效能優化
test	測試相關
build	建置系統或外部相依性
ci	CI 設定檔案
chore	其他雜項（工具、配置等）
revert	撤銷先前的 commit
作用範圍（Scope）- 可選
作用範圍必須由描述程式區段的名詞組成，並用括號包覆
範例：feat(parser):、fix(api):、chore(eslint):
描述（Subject）
必須緊接在類型/作用範圍的冒號與空格之後
本 Skill 要求使用繁體中文撰寫
限制在 50 字元以內
使用祈使句（如：「新增」、「修正」、「更新」）
不加句號
清楚描述變更的核心內容
正文（Body）- 可選
必須在描述後的一個空行之後開始
本 Skill 要求使用繁體中文撰寫
使用項目符號列表（- 開頭）
每個項目描述一個具體變更
優先說明做了什麼，必要時補充原因
使用台灣常用技術詞彙（如：「套件」、「設定」、「腳本」）
頁腳（Footer）- 可選
包含關於提交的詮釋資訊
範例：相關的拉取請求、審核者、重大變更
每個詮釋資訊一行
重大變更（Breaking Changes）

根據官方規範，重大變更對應到 SemVer 的 MAJOR 版本。標示方式：

方式一：在類型後加 !

feat(api)!: 變更使用者認證機制

BREAKING CHANGE: 移除舊版 API 端點，所有用戶端需更新至新版 SDK


方式二：僅在頁腳標示

feat: 變更使用者認證機制

- 實作新版 OAuth 2.0 流程
- 移除舊版 session 認證

BREAKING CHANGE: 移除舊版 API 端點，所有用戶端需更新至新版 SDK


規範要求：

BREAKING CHANGE 必須大寫
使用 ! 提示時，正文或頁腳內必須包含 BREAKING CHANGE: description
執行步驟
步驟 1：取得分析資訊

首先執行輔助腳本，自動檢查分支與計算複雜度評分：

python scripts/analyze_git.py


腳本輸出除了原有欄位外，現在也包含每個 staged 檔案的變更類型：

欄位	說明
NewFiles	新增的檔案（git status 顯示 A）
ModifiedFiles	修改的現有檔案（顯示 M）
DeletedFiles	刪除的檔案（顯示 D）
RenamedFiles	重新命名或複製的檔案（git status 顯示 R/C，格式 old -> new）
步驟 2：檢查分支

根據腳本輸出的 IsMain 與 Branch 欄位判斷：

情況 A（安全分支）： 若 IsMain: false

繼續執行步驟 3

情況 B（主分支）： 若 IsMain: true

停止後續操作
依據變更內容，建議符合規範的新分支名稱（範例：feat/login-form-validation、fix/payment-bug）
回報錯誤：請先切換至建議的分支（或自訂分支）後，再執行 commit。
步驟 3：分析複雜度與模式

根據腳本輸出的 Score 與 RiskFactors 決定模式：

情況 A：簡單模式（Score < 4）
直接使用 -m 參數生成 commit message
適用於小型、低風險的變更
git commit -m "feat: 新增使用者登入功能"

情況 B：複雜模式（Score >= 4）
重要：若 Score 顯著過高（如 Score > 8），強烈建議拆分提交。
建議使用者使用檔案方式生成詳細的 commit message，或協助進行原子化拆分。
步驟 4：原子化拆分提交（針對 Score > 8 或多種類型變更）

若決定拆分提交，請引導使用者執行以下步驟：

撤銷目前的所有 add：git reset
第一階段 add：選擇相關性強的檔案，例如 git add src/auth.ts src/security.ts
執行第一階段 commit：生成對應的 commit message
第二階段 add：例如 git add package-lock.json
執行第二階段 commit：生成對應的 commit message
步驟 5：生成 Commit Message 並確認

依據檔案狀態決定 commit type（優先使用，再搭配 diff 內容確認）：

狀況	建議類型
NewFiles 為主，且為功能性程式碼	feat
NewFiles 為主，且為測試檔案（*.test.*, *.spec.*）	test
NewFiles 為主，且為文件（.md, .txt）	docs
僅有 ModifiedFiles，修正問題邏輯	fix
僅有 ModifiedFiles，程式碼重構（無功能變更）	refactor
僅有 RenamedFiles 或檔案搬移	refactor
僅有 DeletedFiles（清理舊程式碼）	chore 或 refactor
混合多種狀態，涉及功能新增	feat（並考慮拆分）

結合 git diff 內容確認描述的精確性

依據步驟 3 選擇的模式，輸出完整的 Commit Message

輸出對應的 git commit 指令

詢問使用者：是否需要協助執行 commit？

範例
拆分提交建議範例
### ⚠️ 偵測到高複雜度變更 (Score: 10)

本次變更涉及認證邏輯重構與套件更新，建議拆分為兩個提交以符合原子化原則：

#### 第一步：重構認證邏輯
1. 執行：`git reset`
2. 執行：`git add src/auth.ts src/security.ts`
3. Commit Message：`refactor(auth): 重構認證模組安全性邏輯`

#### 第二步：更新套件
1. 執行：`git add pnpm-lock.yaml`
2. Commit Message：`build: 更新相依性鎖定檔`

注意事項
Lock 檔案偵測範圍：包含 package-lock.json、yarn.lock、pnpm-lock.yaml、bun-lock.json、Cargo.lock、go.sum、poetry.lock、Gemfile.lock 等。
只有 staged 狀態的變更會被考慮。
若變更過於複雜，建議拆分為多個獨立的 commit。
當提交符合一或多種提交類型時，應盡可能切成多個提交。
範例

詳細範例請參考 references/examples.md，涵蓋：

基礎範例：feat、fix、docs、style、refactor、perf、test、build、ci、chore、revert
進階範例：含作用範圍、破壞性變更、問題編號、共同作者、複雜變更
不良範例：常見錯誤寫法與修正建議

快速參考：

feat: 新增使用者登入功能

- 實作 JWT 認證機制
- 新增登入表單驗證

fix(cart): 修正購物車金額計算錯誤

- 修正折扣碼套用順序問題

注意事項
只有 staged 狀態的變更會被考慮
未 staged 的變更不會包含在 commit message 分析中
建議先使用 git add 選擇性地 stage 要提交的變更
若變更過於複雜，建議拆分為多個獨立的 commit
當提交符合一或多種提交類型時，應盡可能切成多個提交
常用技術詞彙對照
英文	繁體中文（台灣慣用）
package	套件
config/configuration	設定
script	腳本
dependency	相依性
component	元件
module	模組
function	函式
variable	變數
parameter	參數
implement	實作
initialize	初始化
optimize	優化
refactor	重構
validate	驗證
authentication	認證
authorization	授權
bug	臭蟲
pull request	拉取請求
參考資料
references/conventional-commits-spec.md - 慣例式提交 1.0.0-beta.4 完整規範
references/examples.md - 各類型 commit message 範例集
Conventional Commits 官方網站
SemVer 語意化版本
@commitlint/config-conventional
Weekly Installs
14
Repository
gn00678465/agentskills
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
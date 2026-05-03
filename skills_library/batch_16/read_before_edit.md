---
title: read-before-edit
url: https://skills.sh/cityfish91159/maihouses/read-before-edit
---

# read-before-edit

skills/cityfish91159/maihouses/read-before-edit
read-before-edit
Installation
$ npx skills add https://github.com/cityfish91159/maihouses --skill read-before-edit
SKILL.md
Read Before Edit Skill

這是 maihouses 專案的核心規範：絕對禁止在沒有閱讀檔案的情況下進行修改。

🚨 核心原則
📖 READ → 🧠 UNDERSTAND → ✏️ EDIT

永遠不要跳過 READ 步驟！

🎯 執行時機
每次使用 Edit 工具前
每次使用 Write 工具前
用戶要求修改任何檔案時
用戶要求實作新功能時
📋 必讀檔案清單
修改檔案前，必須閱讀：
要修改的檔案本身
    │
    ├── 該檔案 import 的所有模組
    │
    ├── 相關的類型定義檔案 (types.ts, *.d.ts)
    │
    ├── 相關的 API/服務層檔案
    │
    ├── 相關的 hooks 和 context
    │
    ├── 相關的組件檔案
    │
    └── 相關的工具函數

🔍 實際範例
範例 1: 修改 React 組件

任務： 修改 src/pages/Login.tsx

必須閱讀的檔案：

# 1. 要修改的檔案本身
Read: file_path="src/pages/Login.tsx"

# 2. 搜尋相關類型定義
Glob: pattern="**/types/*auth*.ts"
Read: file_path="src/types/auth.ts"

# 3. 搜尋相關 API
Grep: pattern="login|auth" glob="**/api/**/*.ts" output_mode="files_with_matches"
Read: file_path="src/api/auth.ts"

# 4. 搜尋相關 hooks
Grep: pattern="useAuth" glob="**/hooks/**/*.ts" output_mode="files_with_matches"
Read: file_path="src/hooks/useAuth.ts"

# 5. 搜尋相關 context
Glob: pattern="**/context/*Auth*.tsx"
Read: file_path="src/context/AuthContext.tsx"

# 6. 檢查相關組件
Grep: pattern="LoginForm|Button" glob="**/components/**/*.tsx" output_mode="files_with_matches"
Read: file_path="src/components/LoginForm.tsx"

# 7. 檢查工具函數
Grep: pattern="validate" glob="**/utils/**/*.ts" output_mode="files_with_matches"
Read: file_path="src/utils/validation.ts"

範例 2: 修改 API 層

任務： 修改 src/api/users.ts

必須閱讀的檔案：

# 1. API 檔案本身
Read: file_path="src/api/users.ts"

# 2. 相關類型定義
Read: file_path="src/types/user.ts"
Read: file_path="src/types/api.ts"

# 3. API 基礎配置
Grep: pattern="axios|fetch|baseURL" glob="**/api/**/*.ts" output_mode="files_with_matches"
Read: file_path="src/api/client.ts"

# 4. 錯誤處理模組
Grep: pattern="handleError|ApiError" glob="**/api/**/*.ts" output_mode="files_with_matches"
Read: file_path="src/api/errorHandler.ts"

# 5. 認證相關（如果 API 需要認證）
Read: file_path="src/api/auth.ts"

範例 3: 新增功能

任務： 實作「忘記密碼」功能

必須閱讀的檔案：

# 1. 了解現有認證流程
Read: file_path="src/pages/Login.tsx"
Read: file_path="src/api/auth.ts"
Read: file_path="src/types/auth.ts"

# 2. 了解表單處理模式
Grep: pattern="handleSubmit|onSubmit" glob="**/pages/**/*.tsx" output_mode="content" -B=2 -C=5
Read: file_path="src/components/Form.tsx"

# 3. 了解驗證模式
Read: file_path="src/utils/validation.ts"

# 4. 了解錯誤處理模式
Grep: pattern="try.*catch" glob="**/pages/**/*.tsx" output_mode="content" -B=2 -C=5

# 5. 了解路由配置
Grep: pattern="route|path" glob="**/router/**/*.tsx" output_mode="files_with_matches"
Read: file_path="src/router/routes.tsx"

✅ 閱讀檢查清單

在開始修改前，確認已理解：

 這個檔案的主要功能
 所有 import 的模組來自哪裡、做什麼
 使用的類型定義是什麼
 現有的代碼風格和模式
 錯誤處理方式
 變數命名慣例
 函數結構和組織方式
 相依的其他模組如何運作
🚫 絕對禁止的行為
// ❌ 沒有先 Read 就直接 Edit
Edit: file_path="src/api/users.ts" ...

// ❌ 只讀要修改的檔案，不讀相關檔案
Read: file_path="src/pages/Login.tsx"
Edit: file_path="src/pages/Login.tsx" ...
// 跳過了 types, api, hooks, context!

// ❌ 隨便找一些檔案讀，假裝有在看
Read: file_path="src/index.tsx"  // 不相關
Read: file_path="README.md"      // 不相關
Edit: file_path="src/pages/Login.tsx" ...

// ❌ 讀了但沒理解就開始改
Read: file_path="src/api/auth.ts"
// 立即
Edit: file_path="src/api/auth.ts" ...
// 沒有理解現有架構！

✅ 正確的流程
// ✅ 步驟 1: 識別要修改的檔案
任務: 修改登入頁面加入「記住我」功能

// ✅ 步驟 2: 列出所有相關檔案
相關檔案:
- src/pages/Login.tsx (要修改的檔案)
- src/types/auth.ts (類型定義)
- src/api/auth.ts (API 呼叫)
- src/hooks/useAuth.ts (認證 hook)
- src/utils/storage.ts (localStorage 工具)

// ✅ 步驟 3: 完整閱讀所有檔案
Read: file_path="src/pages/Login.tsx"
Read: file_path="src/types/auth.ts"
Read: file_path="src/api/auth.ts"
Read: file_path="src/hooks/useAuth.ts"
Read: file_path="src/utils/storage.ts"

// ✅ 步驟 4: 理解現有架構
- Login.tsx 使用 useAuth hook
- 表單狀態用 useState 管理
- API 呼叫有完整錯誤處理
- 使用 LoginCredentials interface
- storage.ts 已有 localStorage 封裝

// ✅ 步驟 5: 規劃修改
1. 在 LoginCredentials 加入 rememberMe?: boolean
2. 在 Login.tsx 加入 checkbox
3. 在 useAuth 處理 rememberMe 邏輯
4. 使用 storage.ts 儲存登入狀態

// ✅ 步驟 6: 開始修改
Edit: file_path="src/types/auth.ts" ...
Edit: file_path="src/pages/Login.tsx" ...
Edit: file_path="src/hooks/useAuth.ts" ...

📊 閱讀覆蓋率檢查

修改前，確認閱讀覆蓋率：

### 閱讀覆蓋率報告

#### 已閱讀 ✅

- [x] src/pages/Login.tsx (要修改的檔案)
- [x] src/types/auth.ts (類型定義)
- [x] src/api/auth.ts (API 層)
- [x] src/hooks/useAuth.ts (hooks)
- [x] src/context/AuthContext.tsx (context)
- [x] src/utils/validation.ts (工具函數)

#### 覆蓋率: 100%

✅ 可以安全開始修改

🎯 為什麼必須這樣做？
避免的問題：
破壞現有功能 - 不理解代碼就修改會破壞其他功能
類型不匹配 - 不知道現有類型定義導致類型錯誤
風格不一致 - 不了解代碼風格導致混亂
重複造輪子 - 不知道已有工具函數而重複實作
引入 bug - 不理解邏輯流程而引入錯誤
好處：
理解上下文 - 知道代碼在做什麼、為什麼這樣做
保持一致性 - 修改符合現有風格和模式
避免重複 - 知道可以重用哪些代碼
正確使用類型 - 使用正確的 interface/type
高品質代碼 - 修改更準確、更安全
🚨 監督系統

專案已配置 hooks 監督系統（見 settings.json），會在 Edit/Write 前檢查是否已 Read。

如果違反規則，會看到：

🚫 [監督系統] Edit 被阻止！必須先 Read 該檔案


這不是建議，而是強制規則。

📝 完整案例研究

見專案根目錄的 CLAUDE.md 第 "📖 強制閱讀規範" 章節。

💡 快速提示

修改檔案前的自我檢查：

❓ 我有讀過這個檔案嗎？
❓ 我理解它的所有 import 嗎？
❓ 我知道相關的類型定義嗎？
❓ 我了解它如何與其他模組互動嗎？
❓ 我清楚現有的代碼風格嗎？

如果有任何一個答案是「否」，就不要開始 Edit！

🎓 參考規範
完整規範: CLAUDE.md (專案根目錄)
監督系統: .claude/settings.json hooks 配置
稽核腳本: scripts/ai-supervisor.sh

記住：Read is not optional. Read is mandatory.

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
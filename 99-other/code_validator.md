---
title: code-validator
url: https://skills.sh/cityfish91159/maihouses/code-validator
---

# code-validator

skills/cityfish91159/maihouses/code-validator
code-validator
Installation
$ npx skills add https://github.com/cityfish91159/maihouses --skill code-validator
SKILL.md
Code Validator Skill

依照專案根目錄的 CLAUDE.md 規範驗證代碼品質。

🎯 執行時機

當以下情況發生時，Claude 會自動使用此 skill：

修改任何 .ts 或 .tsx 檔案後
用戶要求代碼審查
用戶要求檢查代碼品質
用戶提到「驗證」、「檢查」、「審查」等關鍵字
🚨 驗證項目
1. 禁止模式檢查

使用 Grep 搜尋以下禁止模式：

# 檢查 any 類型
Grep: pattern=": any\\b" glob="*.ts,*.tsx" output_mode="files_with_matches"

# 檢查 console.log (排除註解)
Grep: pattern="console\\.log\\(" glob="*.ts,*.tsx" output_mode="content"

# 檢查 @ts-ignore
Grep: pattern="@ts-ignore" glob="*.ts,*.tsx" output_mode="files_with_matches"

# 檢查 eslint-disable
Grep: pattern="eslint-disable" glob="*.ts,*.tsx" output_mode="files_with_matches"

2. TypeScript 類型檢查
npm run typecheck


必須通過，無任何類型錯誤。

3. ESLint 檢查
npm run lint


必須通過，無任何 linting 錯誤。

4. 代碼結構檢查

使用 Read 工具閱讀檔案，檢查：

✅ 所有 async 函數有 try-catch 錯誤處理
✅ 所有 API 呼叫有錯誤處理
✅ 變數命名有意義（不是 a, b, x, temp）
✅ 函數不超過 50 行
✅ 無重複代碼
✅ interface/type 定義清晰
5. React 特定檢查
✅ Props 有明確的 TypeScript interface
✅ Event handlers 有正確的類型（如 React.MouseEvent<HTMLButtonElement>）
✅ useState/useEffect 依賴正確
✅ 組件命名為 PascalCase
📋 回報格式

驗證完成後，必須提供以下格式的報告：

## 代碼驗證報告

### 檔案：path/to/file.tsx

#### ✅ 通過項目

- TypeScript 類型檢查通過
- ESLint 檢查通過
- 無禁止模式

#### ❌ 發現問題

1. **行 42**: 使用了 `any` 類型
   - 建議：定義具體的 interface

2. **行 58**: 缺少錯誤處理
   - 建議：在 async 函數中加入 try-catch

#### 🔧 修復建議

[具體的修復步驟]

### 整體評分

- 類型安全: ⭐⭐⭐⭐⭐
- 錯誤處理: ⭐⭐⭐⭐☆
- 代碼風格: ⭐⭐⭐⭐⭐

⚠️ 重要提醒
必須先 Read 再 Edit - 永遠不要在沒有閱讀檔案的情況下修改
完整閱讀相關檔案 - 包括類型定義、API 層、hooks、context
逐項檢查 - 不可跳過任何驗證步驟
發現問題立即回報 - 不可隱藏或繞過問題
🎓 參考規範

所有驗證標準基於：專案根目錄的 CLAUDE.md

違反任何規範即為驗證失敗。

Weekly Installs
17
Repository
cityfish91159/maihouses
GitHub Stars
1
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass
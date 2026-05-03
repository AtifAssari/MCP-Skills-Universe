---
rating: ⭐⭐⭐
title: skill-marketplace
url: https://skills.sh/cityfish91159/maihouses/skill-marketplace
---

# skill-marketplace

skills/cityfish91159/maihouses/skill-marketplace
skill-marketplace
Installation
$ npx skills add https://github.com/cityfish91159/maihouses --skill skill-marketplace
SKILL.md
Skill Marketplace Integration

在執行任務前，自動從 38,000+ 技能市集中找到最適合的工具。

🎯 執行時機

自動觸發條件：

用戶要求執行複雜任務（如測試、文檔生成、部署）
需要專業領域知識（DevOps、AI/ML、Security）
本地 skills 無法滿足需求
用戶明確提到「找工具」、「搜尋 skill」、「market」

不觸發條件：

簡單的檔案讀寫操作
已有適合的本地 skill
用戶要求不使用外部工具
📋 執行流程
Phase 1: 任務分析
1. 解析用戶任務需求
2. 提取關鍵字（如: testing, docker, documentation）
3. 判斷任務複雜度和專業性
4. 決定是否需要搜尋市集

Phase 2: 市集搜尋
1. 使用 WebSearch 在 skillsmp.com 搜尋相關 skills
2. 使用 WebFetch 讀取搜尋結果頁面
3. 解析 skill 列表（名稱、描述、星數、分類）
4. 依相關性和品質排序

Phase 3: 評估與選擇
評分標準：
- 關鍵字匹配度 (40%)
- GitHub stars/下載次數 (25%)
- 更新時間 (15%)
- 描述完整度 (10%)
- 社群評價 (10%)

選擇：取分數最高的 1-3 個 skills

Phase 4: 安裝與使用
1. 下載 SKILL.md 到 .claude/skills/marketplace-temp/
2. 驗證 YAML frontmatter 格式
3. 檢查 allowed-tools 安全性
4. 詢問用戶確認安裝（可選）
5. 使用 Skill 工具執行新安裝的 skill

Phase 5: 清理（可選）
- 任務完成後詢問是否保留 skill
- 若否，刪除臨時安裝的 skill
- 記錄使用統計供未來參考

🔍 搜尋策略
關鍵字映射表
任務類型	搜尋關鍵字	推薦分類
測試生成	testing, jest, playwright	Testing & Security
API 文檔	documentation, api, openapi	Documentation
Docker 部署	docker, container, deploy	DevOps
資料處理	data, csv, json, transform	Data & AI
代碼審查	review, lint, quality	Development
安全掃描	security, vulnerability, audit	Testing & Security
CI/CD	github-actions, ci, pipeline	DevOps
資料庫	database, sql, migration	Databases
高級搜尋範例

情境 1: 用戶要求「幫我生成 API 測試」

搜尋: 'api testing skill site:skillsmp.com';
過濾: ((category = Testing), stars > 100);
結果: (api - test - generator, postman - converter, openapi - test);
選擇: api - test - generator(最高分);


情境 2: 用戶要求「自動化 Docker 部署」

搜尋: 'docker deployment automation site:skillsmp.com';
過濾: ((category = DevOps), updated > 2024);
結果: (docker - compose - gen, k8s - deployer, vercel - docker);
選擇: docker - compose - gen(最相關);

🛡️ 安全檢查

安裝前必檢：

 SKILL.md 有正確的 YAML frontmatter
 allowed-tools 不包含危險工具（如 Bash(rm -rf)）
 來源為 skillsmp.com 官方或信任的 GitHub repo
 沒有可疑的 script 或外部連結
 描述清楚，沒有混淆行為

危險警告標誌：

要求存取敏感環境變數
修改系統檔案
建立網路連線到未知伺服器
執行未加密的 shell 指令
📊 使用範例
範例 1: 自動尋找測試工具

用戶輸入：

"我需要為這個 API 自動生成測試案例"

Agent 流程：

1. [skill-marketplace] 分析任務: API testing
2. [skill-marketplace] 搜尋 skillsmp.com: "api testing generator"
3. [skill-marketplace] 找到 3 個相關 skills:
   - api-test-generator (⭐ 245)
   - rest-api-tester (⭐ 189)
   - graphql-test-gen (⭐ 156)
4. [skill-marketplace] 選擇: api-test-generator
5. [skill-marketplace] 下載並安裝到 .claude/skills/marketplace-temp/
6. [Skill] 執行 api-test-generator
7. [api-test-generator] 生成測試案例完成
8. [skill-marketplace] 詢問是否保留此 skill？

範例 2: DevOps 自動化

用戶輸入：

"幫我設定 GitHub Actions 自動部署到 Vercel"

Agent 流程：

1. [skill-marketplace] 關鍵字: github-actions, vercel, deploy
2. [skill-marketplace] 搜尋市集 DevOps 分類
3. [skill-marketplace] 找到: vercel-ci-setup (⭐ 312)
4. [skill-marketplace] 安裝並執行
5. [vercel-ci-setup] 生成 .github/workflows/deploy.yml
6. [vercel-ci-setup] 配置 Vercel secrets
7. 完成自動化設定

🎛️ 配置選項

可在 .claude/settings.json 中配置行為：

{
  "skills": {
    "marketplace": {
      "enabled": true,
      "auto_install": false, // 是否自動安裝（false=詢問用戶）
      "cache_duration": "24h", // 搜尋結果快取時間
      "max_results": 5, // 最多顯示幾個結果
      "min_stars": 50, // 最低星數要求
      "trusted_sources": [
        // 信任的來源
        "github.com/anthropics",
        "github.com/openai"
      ],
      "cleanup_after_use": true // 使用後自動清理臨時 skills
    }
  }
}

🔄 與現有 Skills 整合

優先級順序：

1. read-before-edit (最高優先級，永遠先執行)
2. skill-marketplace (任務開始前搜尋工具)
3. 本地專案 skills (code-validator, type-checker, etc.)
4. 市集臨時 skills (下載後使用)
5. pre-commit-validator (最後驗證)


決策樹：

任務開始
  │
  ├─ 是否為代碼修改？
  │   └─ YES → read-before-edit
  │
  ├─ 本地 skills 是否適用？
  │   ├─ YES → 使用本地 skill
  │   └─ NO → skill-marketplace 搜尋市集
  │
  ├─ 執行主要任務
  │
  └─ 是否要 commit？
      └─ YES → pre-commit-validator

📈 效能優化

快取策略：

搜尋結果快取 24 小時
常用 skills 永久保留（如使用次數 >3）
市集 API 請求限制：10 次/分鐘

載入優化：

並行搜尋多個關鍵字
預先載入熱門 skills 的 metadata
使用 HEAD 請求驗證檔案存在性
🧪 測試驗證

單元測試：

# 測試搜尋功能
node .claude/skills/skill-marketplace/search-marketplace.cjs "docker deployment"

# 測試安裝流程 (模擬)
node .claude/skills/skill-marketplace/install-skill.cjs --help

# 搜尋測試相關 skills
node .claude/skills/skill-marketplace/search-marketplace.cjs "testing"


整合測試：

場景 1: 搜尋 → 安裝 → 使用 → 清理
場景 2: 本地 skill 優先於市集
場景 3: 安全檢查阻止惡意 skill
場景 4: 離線模式降級處理

🚨 錯誤處理

常見錯誤與解決：

錯誤	原因	解決方案
搜尋失敗	網路問題	使用本地快取或本地 skills
下載失敗	GitHub API 限制	等待 1 分鐘後重試
格式錯誤	SKILL.md 格式不正確	跳過此 skill，選擇次優
權限不足	allowed-tools 超出範圍	詢問用戶是否信任
執行失敗	Skill 代碼有 bug	回退使用基本工具
📚 相關資源
Skills Marketplace: https://skillsmp.com/
SKILL.md 規範: https://docs.anthropic.com/claude-code/skills
GitHub Discussions: https://github.com/anthropics/claude-code/discussions
本地 Skills 文檔: .claude/skills/README.md
✅ 驗收標準
 能成功搜尋 skillsmp.com
 能解析搜尋結果並排序
 能下載並安裝 SKILL.md
 能驗證安全性
 能執行新安裝的 skill
 能清理臨時檔案
 有完整的錯誤處理
 與現有 skills 無衝突

此 Skill 讓 Agent 具備自我學習能力，能根據任務自動尋找最佳工具！ 🚀

Weekly Installs
17
Repository
cityfish91159/maihouses
GitHub Stars
1
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubWarn
SocketFail
SnykFail
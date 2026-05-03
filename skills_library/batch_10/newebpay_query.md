---
title: newebpay-query
url: https://skills.sh/paid-tw/skills/newebpay-query
---

# newebpay-query

skills/paid-tw/skills/newebpay-query
newebpay-query
Installation
$ npx skills add https://github.com/paid-tw/skills --skill newebpay-query
SKILL.md
藍新金流交易查詢任務

你的任務是在用戶的專案中實作藍新金流交易查詢功能。

Step 1: 確認需求

用戶輸入: $ARGUMENTS

詢問用戶：

查詢情境：需要什麼查詢功能？

單筆訂單查詢（客戶查詢、客服查詢）
批次對帳（每日/定時對帳）
支付狀態確認（NotifyURL 備援）

專案框架：你使用什麼框架？

確認是否已有 NewebPay 環境設定
Step 2: 建立查詢功能

在現有的支付模組中加入查詢方法，或建立新模組。

核心功能:

generateCheckValue(orderNo, amount) - 產生 SHA256 檢核碼
queryTrade(orderNo, amount) - 查詢單筆交易
Step 3: 實作程式碼

根據框架加入查詢功能。

Step 4: 整合到應用

建議整合方式：

API 端點: GET /api/orders/:orderNo/status
管理後台: 訂單詳情頁顯示即時狀態
定時任務: 對帳排程
API 參考
端點
環境	URL
測試	https://ccore.newebpay.com/API/QueryTradeInfo
正式	https://core.newebpay.com/API/QueryTradeInfo
請求參數
參數	類型	必填	說明
MerchantID	String(15)	✓	商店代號
Version	String	✓	1.3
RespondType	String	✓	JSON
CheckValue	String	✓	SHA256 檢核碼
TimeStamp	Number	✓	Unix timestamp
MerchantOrderNo	String(30)	✓	商店訂單編號
Amt	Number	✓	訂單金額
CheckValue 產生規則
原始字串: IV={HashIV}&Amt={金額}&MerchantID={商店代號}&MerchantOrderNo={訂單編號}&Key={HashKey}
結果: SHA256 後轉大寫

TradeStatus 交易狀態
值	說明
0	未付款
1	已付款
2	付款失敗
3	已取消
6	退款
詳細參考文件
程式碼範例 (PHP/Node.js)
常見錯誤
代碼	說明	解決方式
TRA10001	查無此筆交易	確認訂單編號正確
TRA10002	CheckValue 檢核錯誤	確認參數順序與大小寫
TRA10003	時間戳記錯誤	確認伺服器時間正確
Weekly Installs
36
Repository
paid-tw/skills
GitHub Stars
242
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
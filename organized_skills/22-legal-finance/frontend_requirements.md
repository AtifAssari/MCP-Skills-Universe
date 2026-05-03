---
rating: ⭐⭐⭐
title: frontend-requirements
url: https://skills.sh/gemini960114/skills/frontend-requirements
---

# frontend-requirements

skills/gemini960114/skills/frontend-requirements
frontend-requirements
Installation
$ npx skills add https://github.com/gemini960114/skills --skill frontend-requirements
SKILL.md
生成前端串接需求書（FastAPI → frontend.md）
目標

根據「目前既有的 FastAPI 後端 API 服務程式碼」，撰寫一份給前端工程師使用的串接需求與流程說明文件，輸出檔名固定為 frontend.md，並以 Markdown 撰寫、結構清楚、可直接交付前端實作。

核心原則（非常重要）
以「前端要怎麼串、怎麼做 UI/UX、怎麼處理錯誤與狀態」為主，而不是後端實作細節。
必須從程式碼中整理出事實：路由、request/response schema、認證方式、狀態值、錯誤碼。
不要憑空編造 API。若程式碼找不到，就在文件中標注「未在目前程式碼中發現」並給出前端建議的問項（最多 3 個關鍵問題）。
文件讀者假設：從未看過後端程式碼的前端工程師。
工作流程（你必須照做）
先掃描專案中的 FastAPI 入口與路由定義：
常見位置：main.py、app/main.py、app/api/*、routers/*、api.py
FastAPI 註冊方式：include_router()、APIRouter()、prefix/tags
收集所有 endpoint 與其方法、路徑參數、query/body、回傳格式：
以 Pydantic model / response_model / typing 註記為準
解析認證/授權機制（若有）：
JWT / OAuth2PasswordBearer / API key / session cookie
header 名稱、token 格式、過期/刷新（若有）
特別整理「工作派送 / 任務 / Job / Task」相關流程：
建立任務的 API（POST）
任務查詢/列表（GET）
任務結果取得（GET）
是否非同步、是否需要輪詢、狀態轉換與錯誤情境
將資訊整理成前端友善的 frontend.md：
每個 API 提供 request/response 範例與錯誤處理建議
補上前端串接流程建議與 UX 建議（loading、retry、empty、error states）
frontend.md 必備章節（輸出時必須包含）

你最終輸出請是一份完整的 frontend.md（Markdown 文件），至少包含以下章節，並可依實際後端補充：

0. 文件目的與範圍
這個前端要做的功能範圍
需要的環境變數（如 Base URL）
假設與限制（例如：只能內網、需要 VPN、CORS 等）
1. 帳號與身分管理
使用者註冊（若有）
登入 / 驗證機制
Token/JWT 的取得方式
Header 格式（Authorization: Bearer xxx）
Token 過期行為與前端處理建議
使用者角色/權限（若後端有定義）
權限不足時的錯誤碼與 UI 建議（例如導向登入、顯示無權限）
2. API 使用說明（共通規格）
API Base URL（從設定或程式碼推導；若不明確就標注）
共通 headers
content-type、回傳格式（JSON）
錯誤回應的共通格式（若後端有統一 error schema）
逾時/重試/節流（如有）
3. Endpoint 一覽表（總表）
用表格列出：
功能
Method
Path
Auth（是否需要）
簡述
4. API 逐一說明（前端串接細節）

針對每個 endpoint，提供：

功能說明（前端角度：用在哪個畫面/流程）
HTTP Method + Path
Request
path/query/body 的欄位說明（型別、必填、預設）
範例 request（JSON）
Response
200/201 成功範例（JSON）
重要欄位意義
Error Handling
401/403/404/422/429/500 等情境
前端建議行為（toast、重導、表單欄位提示、重試）
5. 工作派送與任務流程（Job/Task）
建立/派送任務的 API 與參數
派送後的處理流程（同步/非同步）
是否支援批次派送（若有）
建議前端流程（用文字流程/步驟描述）
例如：建立任務 → 顯示 pending → 開始輪詢 → success 顯示結果 / failed 顯示錯誤
6. 查詢與結果取得
任務列表（多筆）
分頁/排序/篩選（若支援）
單筆任務查詢
任務結果取得（若為獨立 endpoint）
大結果/檔案下載（若有）
streaming、presigned URL、content-type 處理
7. 狀態說明（狀態機）
列出所有任務狀態（例如 pending/running/success/failed）
每個狀態的意義、UI 呈現建議（badge、loading、禁用按鈕等）
狀態轉換時機（由哪個 API/事件造成）
failed 時錯誤資訊欄位（若有）與顯示建議
8. 前端實作建議
建議的呼叫順序（流程）
是否需要 polling（輪詢）
建議 interval、停止條件、超時策略
常見錯誤與 UX 建議
例如：401 → 導回登入
422 → 表單欄位提示
5xx → 允許重試 + 顯示客服/回報資訊
9. 其他（若後端有）
health check endpoint（/health）
system info/version endpoint
rate limit/配額/限制
CORS、檔案大小限制、timeout 等
你輸出時的格式要求（務必遵守）
最終輸出是一份完整的 Markdown 文件內容（可直接存成 frontend.md）。
標題層級清楚（#、##、###）。
每個 endpoint 至少給一個 request/response JSON 範例。
若有不確定資訊：清楚標注「未在程式碼中發現」，並附上前端需要向後端確認的 1–3 個問題（不要超過 3 個）。
Weekly Installs
9
Repository
gemini960114/skills
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
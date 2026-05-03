---
rating: ⭐⭐⭐
title: feishu-cli-auth
url: https://skills.sh/riba2534/feishu-cli/feishu-cli-auth
---

# feishu-cli-auth

skills/riba2534/feishu-cli/feishu-cli-auth
feishu-cli-auth
Installation
$ npx skills add https://github.com/riba2534/feishu-cli --skill feishu-cli-auth
SKILL.md
飞书 OAuth 认证与 Token 管理

feishu-cli 通过 OAuth 2.0 Device Flow（RFC 8628） 获取 User Access Token，用于搜索、消息互动、审批任务查询等需要用户身份的 API。无需在飞书开放平台配置任何重定向 URL 白名单。

feishu-cli：如尚未安装，请前往 riba2534/feishu-cli 获取安装方式。

v1.18+ 变更：Authorization Code Flow（--print-url / auth callback / --manual / --no-manual / --port / --method / --scopes）已全部删除，只保留 Device Flow。旧脚本请迁移至 auth login --scope "..." --json 或 auth login --no-wait + --device-code 两步模式。

首次使用：从零开始的初始化

如果用户从未使用过 feishu-cli，按以下顺序完成初始化：

# 第一步：一键创建飞书应用（Device Flow 自注册「个人代理应用」，
#         扫码确认后自动把 App ID / App Secret 写入 ~/.feishu-cli/config.yaml）
feishu-cli config create-app --save

# 第二步：在飞书开放平台的"应用权限管理"页面为新应用开通所需 scope
#         （复制 README 的完整 JSON 粘贴到"导入权限"入口即可一次性开通）
#         feishu-cli 不做权限申请自动化，这一步由用户/管理员自行操作。

# 第三步：OAuth 用户授权（搜索、审批等需要用户身份的功能才需要这一步）
feishu-cli auth login

# 第四步：验证配置是否成功
feishu-cli doc create --title "Hello Feishu"


第一步通过 Device Flow 协议自动注册「个人代理应用」，--save 会把凭证写入配置文件。

关于权限申请：v1.18+ 版本移除了 config add-scopes 命令。理由是权限申请涉及 tenant 管理员审批、scope 选择是业务决策，不应由 CLI 做自动化。用户在飞书开放平台的权限管理页面一次性粘贴 README 的 JSON 最快捷。

核心概念

Token 存储位置：所有 OAuth Token 保存在 ~/.feishu-cli/token.json（明文 JSON，权限 0600），包括 Access Token、Refresh Token、过期时间和授权 scope。

两种身份：

App Access Token（应用身份）：通过 app_id/app_secret 自动获取，大多数文档操作使用此身份
User Access Token（用户身份）：需 OAuth 授权，搜索、消息互动、审批任务等 API 必须使用此身份

Token 生命周期：

Access Token：2 小时有效
Refresh Token：30 天有效（Device Flow 会强制注入 offline_access scope）
过期后自动用 Refresh Token 刷新，用户无感

Scope 策略：

CLI 在 auth login 时会显式声明本次请求的 scope，不再依赖“后台开了就自动全量返回”
推荐先 auth check --scope "REQ_SCOPES" 预检，再执行 auth login --scope "..." 或 auth login --domain ... --recommend
CLI 会自动追加最小核心 scope（如 auth:user.id:read）和 offline_access
要真正拿到某个 scope，仍需先在飞书开放平台的"应用权限管理"页面开通，然后重新 auth login
按域申请权限（--domain --recommend）

auth login 支持通过 --domain 指定业务域，配合 --recommend 自动推荐该域所需的 scope，避免手动拼写 scope 字符串。

可用的业务域（20 个）：

approval, attendance, bitable, calendar, chat, contact, doc_access, docs, drive, im, mail, minutes, search, sheets, slides, task, vc, whiteboard, wiki, all

用法示例：

# 按单个域申请推荐 scope
feishu-cli auth login --domain search --recommend

# 按多个域申请推荐 scope
feishu-cli auth login --domain vc --domain minutes --recommend

# 申请所有域的推荐 scope
feishu-cli auth login --domain all --recommend

# --recommend 单独使用（不带 --domain）= 等价于 --domain all --recommend
feishu-cli auth login --recommend


交互式选择：在交互终端下（非管道/非 --json/非 --scope/非 --domain），auth login 会显示交互式提示符，让用户用方向键多选要授权的业务域，无需记忆域名。

人类用户授权

一条命令通吃所有环境——本地桌面、SSH 远程、WSL、容器都一样：

feishu-cli auth login


CLI 会：

向飞书请求一个 device_code 和 user_code
在 stderr 打印验证链接 + 用户码
在本地桌面尝试自动打开浏览器（有 GUI 时成功，SSH 远程时静默失败无副作用）
每 5 秒轮询一次 token 端点，直到用户完成授权

用户只需在任意有浏览器的设备（电脑、手机）打开链接，输入用户码或扫码即可。完成后 CLI 自动拿到 Token 并保存。

不再需要 --manual / --no-manual / --port / 重定向 URL 配置等一切针对 SSH 远程/桌面差异的 workaround。

AI Agent 授权约定（核心）

AI Agent（Claude Code 等）授权飞书必须遵循下面的决策链和两种技术方案之一。

决策链：先 auth check 再 auth login

在执行任何需要 User Access Token 的命令前，先用 auth check 预检：

需要 User Token 的任务
    ↓
feishu-cli auth check --scope "REQ_SCOPES" -o json   (exit 0 = 全部满足)
    ↓
case ok=true:                         继续执行业务命令
case error=not_logged_in:             → 启动登录流程
case error=token_expired:             → 启动登录流程
case missing=[...]:                   → 提示用户去飞书开放平台的应用权限管理页面开通缺失的 scope，然后执行 `auth login --scope "missing..."` 重新授权


AI 永远不应该：

传 --scopes flag（已删除）
调 auth callback 命令（已删除）
使用 --print-url flag（已删除）
调 config add-scopes 命令（已删除，权限申请是用户/管理员的责任，不做自动化）
自己生成或管理 device_code
要求用户从浏览器地址栏复制回调 URL 回传给 AI——这是 v1.18 前 Authorization Code Flow 的流程，已彻底删除。Device Flow 下用户只需点击链接完成授权，无需复制任何东西。如果 AI 引导用户"把地址栏的 URL 粘贴给我"，那是在回忆错误的旧流程

当用户缺少某个 scope 时 AI 应如何引导：不要自己尝试跑任何"申请权限"的命令。直接告诉用户：

打开飞书开放平台 → 你的应用 → 权限管理页面
搜索并开通缺失的 scope（具体 scope 名可从 auth check 的 missing 字段读到）
或者复制 README 的完整权限 JSON 一次性导入
重新 feishu-cli auth login --scope "缺失的 scope..."；若一组功能要一起开通，也可用 --domain ... --recommend
方案 A：run_in_background 后台阻塞（推荐）

最简洁的做法——让 auth login --scope "..." --json 阻塞轮询，AI 通过 Claude Code 的 run_in_background: true 把它丢到后台：

# 步骤 1: 后台启动登录（显式指定本次要拿的 scope）
task = Bash(command='feishu-cli auth login --scope "search:docs:read search:message" --json', run_in_background=true)

# 步骤 2: 读 stdout 第一行（首次 stdout 事件）
{
  "event": "device_authorization",
  "verification_uri": "https://accounts.feishu.cn/oauth/v1/device/verify?flow_id=...",
  "verification_uri_complete": "https://accounts.feishu.cn/oauth/v1/device/verify?flow_id=...&user_code=ABCD-EFGH",
  "user_code": "ABCD-EFGH",
  "device_code": "O-NUxxxx...",
  "expires_in": 240,
  "interval": 5
}

# 步骤 3: 把 verification_uri_complete 和 user_code 展示给用户
"请在浏览器打开以下链接完成授权（4 分钟内有效）:
  https://accounts.feishu.cn/oauth/v1/device/verify?flow_id=...&user_code=ABCD-EFGH
用户码: ABCD-EFGH
授权完成后告诉我继续。"

# 步骤 4: 等后台任务自动完成通知
# 步骤 5: 读 stdout 第二行（完成事件）
{
  "event": "authorization_complete",
  "expires_at": "2026-04-18T04:05:36+08:00",
  "refresh_expires_at": "2026-04-25T02:05:36+08:00",
  "scope": "auth:user.id:read search:docs:read ... offline_access",
  "requested_scope": "auth:user.id:read search:docs:read search:message",
  "missing_scopes": []
}

# 步骤 6: 再调一次 auth check 确认，继续业务

方案 B：--no-wait / --device-code 两步模式（高级）

如果 AI Agent 需要把"请求 device_code"和"轮询 token"拆到两个独立的 Bash 调用里（比如中间有其他任务要做），使用两步模式：

# 步骤 1: 只请求 device_code，立即退出（不轮询）
feishu-cli auth login --domain vc --domain minutes --recommend --no-wait --json
# stdout 输出一行 JSON: {"event":"device_authorization", ..., "device_code":"O-NUxxxx..."}
# 进程立即退出 0

# 步骤 2: AI 把链接展示给用户，等待用户完成授权

# 步骤 3: 用上一步的 device_code 继续轮询
feishu-cli auth login --device-code "O-NUxxxx..." --json
# 阻塞直到用户授权完成或 device_code 过期（约 3 分钟）
# 成功后 stdout 输出: {"event":"authorization_complete", ...}


两步模式的 device_code 是第一步服务器返回的原始值，AI 需要自己管理这个字符串（通常直接传给下一步命令参数）。第一步请求时的 requested scope 会按 device_code 本地缓存，第二步轮询完成后仍会基于同一组 requested scope 做 granted-scope 校验。

⚠️ 这个"两步模式"≠ v1.18 前的"两步式非交互登录"。新模式是 Device Flow 的拆分：

旧两步式（已删除）：用户必须复制浏览器地址栏里的 127.0.0.1:9768/callback?code=...&state=... 回调 URL 粘贴给 AI
新两步模式：用户只点击一次链接完成授权，不需要复制任何 URL。AI 只需记住第一步服务端返回的 device_code 字符串并传给第二步命令即可。两次 Bash 调用中间 AI 向用户索要的是"是否已完成授权"的确认，不是回调 URL
三种登录模式对比
维度	人类直接跑	AI 方案 A（后台阻塞）	AI 方案 B（两步拆分）
命令	auth login --domain search --recommend	auth login --scope "..." --json + run_in_background=true	auth login --domain ... --recommend --no-wait --json → ... → auth login --device-code <c> --json
Bash 调用次数	1 次（前台/后台同进程）	1 次（后台）	2 次（独立进程）
进程阻塞	阻塞到授权完成	后台阻塞	第一步立即退出，第二步阻塞轮询
用户操作	点击链接 / 输入用户码	点击链接 / 输入用户码	点击链接 / 输入用户码
用户需要复制东西给 AI	❌ 不需要	❌ 不需要	❌ 不需要
stdout 输出	无（仅 stderr 人类文本）	2 行 JSONL 事件流	第一步 1 行 JSON，第二步 1 行 JSON
AI 需要保管什么	无	无（读 stdout 即可）	第一步返回的 device_code 字符串
何时选	人类在交互终端	AI 有 run_in_background 能力（绝大多数情况）	Agent 框架没有后台任务能力；或要在两次命令之间做其他事；或要把 device_code 持久化到状态文件
auth check 命令

检查当前 Token 是否包含指定 scope，专为 AI Agent 预检而设计。

feishu-cli auth check --scope "search:docs:read"
feishu-cli auth check --scope "search:docs:read im:message:readonly"


输出 JSON 到 stdout，退出码 0 表示满足，非 0 表示不满足。

输出字段
字段	类型	说明
ok	bool	true = 所有 required scope 都已授权
granted	[]string	已包含的 scope 列表
missing	[]string	缺失的 scope 列表
error	string	失败原因（not_logged_in / token_expired），仅在未登录或过期时出现
suggestion	string	修复建议（仅在 ok=false 时出现）
返回状态分支
# 全部满足
{"ok":true,"granted":["search:docs:read"],"missing":null}
# exit 0

# 未登录
{"ok":false,"error":"not_logged_in","missing":["search:docs:read"],"suggestion":"feishu-cli auth login"}
# exit 1

# Token 过期（access + refresh 都失效）
{"ok":false,"error":"token_expired","missing":["search:docs:read"],"suggestion":"feishu-cli auth login"}
# exit 1

# 部分缺失
{"ok":false,"granted":["search:docs:read"],"missing":["im:message:readonly"],"suggestion":"确认飞书开放平台已开通后，执行 feishu-cli auth login --scope \"im:message:readonly\" 重新授权"}
# exit 1


设计意图：AI 只需解析 ok 字段决定是否继续，解析 error / missing 字段决定提示用户做什么（重新登录 or 先补 scope 再登录）。

Token 状态检查
# 人类可读格式
feishu-cli auth status

# JSON 格式（AI Agent 推荐）
feishu-cli auth status -o json


已登录且 Token 有效：

{
  "access_token": "eyJhbG...BZJrXA",
  "access_token_valid": true,
  "cached_user": {
    "cached_at": "2026-04-12T15:39:38+08:00",
    "name": "用户名",
    "open_id": "ou_xxx",
    "union_id": "on_xxx",
    "user_id": "xxx"
  },
  "expires_at": "2026-04-12T17:39:38+08:00",
  "health": "healthy",
  "identity": "user",
  "logged_in": true,
  "refresh_expires_at": "2026-04-19T15:39:38+08:00",
  "refresh_token_present": true,
  "refresh_token_valid": true,
  "scope": "base:app:read ...",
  "token_status": "valid"
}


字段说明：

identity：身份类型，user（User Access Token）或 bot（App Access Token）
cached_user：缓存的当前登录用户信息（首次登录后自动拉取并缓存到 ~/.feishu-cli/user_profile.json）
token_status：Token 状态，valid（仍有效）/ needs_refresh（access_token 快过期但 refresh_token 有效，下次调用会自动刷新）/ expired（都过期）
refresh_token_present：登录时是否拿到 refresh_token。false 通常意味着应用未在开放平台开通 offline_access
health：综合健康度，AI Agent 推荐只判断这个字段——
healthy：一切正常
needs_relogin：曾有 refresh_token 但已过期，必须重新 auth login
missing_refresh_token：登录时就没拿到 refresh_token，access_token 过期后需重新 auth login

未登录：

{"logged_in": false}


--verify 在线校验：默认 auth status 只检查本地 Token 文件的过期时间。加上 --verify 会向飞书服务端发起一次在线校验请求，确认 Token 是否真正有效（而非仅本地未过期）：

feishu-cli auth status -o json --verify


一般情况下 AI Agent 应该优先用 auth check 而不是 auth status，因为 check 直接返回"是否满足需求"。auth status 更适合人类用户排查。

Token 自动刷新机制

搜索、消息互动、审批任务等必须使用 User Access Token 的命令（resolveRequiredUserToken）通过 ResolveUserAccessToken() 按以下优先级链查找。其他可选命令（resolveOptionalUserToken）仅检查第 1、2 项，默认使用 App Token：

--user-access-token 命令行参数
FEISHU_USER_ACCESS_TOKEN 环境变量
~/.feishu-cli/token.json：
access_token 有效 → 直接使用
access_token 过期 + refresh_token 有效 → 自动刷新并保存新 Token
都过期 → 报错"已过期，请重新登录"
config.yaml 中的 user_access_token 静态配置

刷新过程对用户透明：stderr 输出 [自动刷新] 刷新成功...，命令正常执行。

刷新响应的兜底策略（v1.19.2+）：OAuth 规范允许刷新端点不返回新的 refresh_token（表示复用原值）。CLI 实现如下兜底，避免单次响应缺字段就让本地 refresh_token 丢失：

响应缺 refresh_token → 复用 token.json 中原有值
响应缺 refresh_token_expires_in → 保留原 refresh_expires_at
响应缺 scope → 保留原 scope

请求统一使用 application/x-www-form-urlencoded 编码（OAuth 2.0 标准）。

User Access Token 的使用场景
必须 User Access Token 的命令
命令	典型 scope
search docs "关键词"	search:docs:read
search messages "关键词"	search:message
search apps "关键词"	（应用审批）
msg get / list / history	im:message:readonly + im:message.group_msg:get_as_user
msg pin / unpin / pins	im:message.pins
msg reaction add/remove/list	im:message.reactions
msg delete	im:message
msg search-chats	im:chat:read
chat get / update / delete	im:chat:read / im:chat
chat member list / add / remove	im:chat.members:read / im:chat.members
approval task query	approval:task
vc search	vc:meeting.search:read
vc notes（三路径）	vc:note:read + vc:meeting.meetingevent:read（meeting-ids 路径）/ minutes:minutes:readonly（minute-tokens 路径）/ calendar:calendar:read + calendar:calendar.event:read（calendar-event-ids 路径）
vc notes --with-artifacts	+ minutes:minutes.artifacts:read
vc notes --download-transcript	+ minutes:minutes.transcript:export
vc recording	vc:record:readonly（+ calendar 两个 scope 若用 calendar-event-ids 路径）
minutes get	minutes:minutes:readonly（--with-artifacts 额外需 minutes:minutes.artifacts:read）
minutes download	minutes:minutes.media:export
mail message / messages / thread / triage	mail:user_mailbox:readonly + mail:user_mailbox.message:readonly + mail:user_mailbox.message.body:read + mail:user_mailbox.message.address:read + mail:user_mailbox.message.subject:read
mail send / draft-create / draft-edit / reply / reply-all / forward	上述只读权限 + mail:user_mailbox.message:send + mail:user_mailbox.message:modify
drive upload	drive:file:upload
drive download / export / export-download	drive:file:download + docs:document.content:read + docs:document:export + drive:drive.metadata:readonly
drive import	docs:document.media:upload + docs:document:import
drive move	space:document:move
drive add-comment	docs:document.comment:create + docs:document.comment:write_only + docx:document:readonly
bitable *（v3 API）	base:base + base:table + base:record + base:field + base:view + base:role（按操作取子集）
可选 User Access Token 的命令（默认用 App Token）

以下命令默认使用 App Token（租户身份），仅在通过 --user-access-token 参数或 FEISHU_USER_ACCESS_TOKEN 环境变量显式指定时才使用 User Token：

命令
wiki get/export/nodes
calendar list/get/event-search/freebusy
task create/complete/list、tasklist create/list/delete
user info/search
典型检查流程
# 1. 预检 scope（AI 推荐）
feishu-cli auth check --scope "search:docs:read"
# exit 0 → 继续

# 或者 2. 手动检查登录状态（人类用户）
feishu-cli auth status -o json

# 3. 如果缺少登录或 scope，执行按需登录
feishu-cli auth login --scope "search:docs:read"

# 4. 登录后，搜索命令自动从 token.json 读取 Token
feishu-cli search docs "产品需求"

退出登录
feishu-cli auth logout


删除 ~/.feishu-cli/token.json，不影响 App Access Token（app_id/app_secret）。

排错指南
问题	诊断	解决
"缺少 User Access Token"	从未登录	feishu-cli auth login
"User Access Token 已过期"	token.json 中 access + refresh 都过期	重新 auth login
搜索报 99991679 Unauthorized	Token scope 不满足	auth check --scope "..." 定位缺失；在飞书开放平台应用权限管理页面补权限后重新 auth login
搜索报 99991672 Access denied	应用未开通所需权限	在飞书开放平台应用权限管理页面开通对应 scope，然后重新 auth login
auth status -o json 显示 health: missing_refresh_token（登录时未获取到 refresh_token）	最常见原因：应用未在飞书开放平台开通 offline_access scope。CLI 虽强制把 offline_access 塞进 Device Flow 请求，但飞书服务端按应用配置下发 token，未开通则不返回 refresh_token	1. 打开飞书开放平台 → 应用权限管理页面确认 offline_access 已开通；2. feishu-cli auth logout && feishu-cli auth login 重新授权；3. 再跑 auth status -o json 确认 refresh_token_present: true；4. 若仍失败请反馈 issue #94
auth status -o json 显示 health: needs_relogin	refresh_token 也过期了（默认 7 天）	重新 auth login
"授权码已过期"	设备码 240 秒内未完成授权	重新 auth login，尽快完成浏览器授权
"用户拒绝了授权"	用户在飞书授权页点了拒绝	重新 auth login，这次点「允许」
轮询长时间卡在 authorization_pending	用户还未在浏览器完成授权	提醒用户打开链接并输入 user_code
"未登录飞书，请先运行 feishu-cli auth login"	未登录或 token.json 损坏	auth logout && auth login
创建飞书应用（一键自动注册）

传统方式需要用户手动访问飞书开放平台后台（open.feishu.cn）创建应用、复制凭证。config create-app 命令通过飞书 Device Flow 协议，在终端内自动完成整个注册过程。

什么是 Device Flow

Device Flow（RFC 8628）是一种 OAuth 2.0 授权方式，专为没有浏览器的设备（如 CLI 工具、智能电视）设计。核心思路：

CLI 向飞书服务器申请一个「用户码」和「验证链接」
用户在任意设备的浏览器中打开链接、输入用户码（或直接扫码）完成身份验证
CLI 在后台轮询服务器，用户确认后自动获取凭证

因此 CLI 本身不需要嵌入浏览器，也不需要配置回调 URL。auth login 和 config create-app 都使用 Device Flow。

命令与参数
feishu-cli config create-app [flags]

参数	默认值	说明
--save	false	创建成功后自动将 App ID 和 App Secret 写入 ~/.feishu-cli/config.yaml
--brand	feishu	目标平台：feishu（飞书国内版）或 lark（Lark 国际版）
-o json	—	以 JSON 格式输出结果（适合脚本和 AI Agent 解析）
详细流程
第一步：发起注册
feishu-cli config create-app --save


CLI 向 accounts.feishu.cn/oauth/v1/app/registration 发送请求，注册类型为 PersonalAgent（个人代理应用）。服务器返回 device_code / user_code / verification_uri_complete / expires_in。

终端输出：

正在发起应用注册...

请在浏览器中打开以下链接，扫码确认创建应用:

  https://open.feishu.cn/page/cli?user_code=ABCD-EFGH

用户码: ABCD-EFGH
有效期: 300 秒

等待扫码确认...
  等待中... 5/300 秒

第二步：用户在浏览器确认

用户打开链接后，会看到飞书的授权页面。可以通过以下两种方式确认：

飞书 App 扫码：手机飞书扫描页面上的二维码
手动输入用户码：在页面输入终端显示的 user_code

确认后，飞书会自动创建一个「个人代理应用」，应用归属于扫码确认的用户。

第三步：CLI 自动获取凭证

CLI 在后台以 interval 秒为间隔轮询服务器。用户确认后，服务器返回 client_id（即 App ID）和 client_secret（即 App Secret）。

终端输出：

应用创建成功！
  App ID:     cli_a7xxxxxx
  App Secret: 0hKj****************************dF3m

已保存到配置文件

--save 标志详解

--save 控制凭证的持久化方式，是新用户最推荐的用法。

不加 --save：CLI 仅在终端打印凭证，并提示用户手动配置环境变量。

加 --save：CLI 自动将 App ID 和 App Secret 写入 ~/.feishu-cli/config.yaml，后续所有命令直接可用。

场景	行为
配置文件不存在	创建 ~/.feishu-cli/config.yaml，写入默认配置项
配置文件已存在	仅更新 app_id 和 app_secret，保留其他已有配置
目录不存在	自动创建 ~/.feishu-cli/ 目录
文件权限	0600（仅所有者可读写）
AI Agent 使用方式

AI Agent 在 Bash 中执行时建议用 -o json 获取结构化输出：

feishu-cli config create-app --save -o json


JSON 输出（stdout）：

{
  "app_id": "cli_a7xxxxxx",
  "app_secret": "0hKjxxxxxxxxdF3m",
  "brand": "feishu"
}


注意：进度信息输出到 stderr，JSON 输出到 stdout。命令需要等待用户扫码，AI Agent 应将授权链接展示给用户并等待确认，或使用 run_in_background。

Lark 国际版
feishu-cli config create-app --save --brand lark


区别仅在 API 端点（accounts.larksuite.com）和默认 base_url（https://open.larksuite.com）。

错误处理
错误信息	原因	解决
应用注册失败: 请求失败	无法访问 accounts.feishu.cn，网络不通或被代理拦截	检查网络，配置 HTTPS_PROXY
注册码已过期，请重试	用户未在 300 秒内扫码确认	重新执行，尽快扫码
用户拒绝了应用注册	用户在飞书授权页面点了「拒绝」	重新执行，这次点「允许」
配置保存失败	磁盘权限问题	检查 ~/.feishu-cli/ 目录权限
创建成功后的下一步
# 1. 在飞书开放平台的"应用权限管理"页面为新应用开通所需 scope
#    复制 README 的完整权限 JSON（tenant + user 两套 400+ 个 scope）
#    粘贴到"导入权限"入口即可一次性开通全部
#    feishu-cli 不做权限申请自动化（需要 tenant 管理员审批，是业务决策）

# 2. 验证配置（App Token 身份，不需要 auth login）
feishu-cli doc create --title "Hello Feishu"

# 3. 可选：OAuth 用户授权（搜索、审批等需要用户身份的功能）
feishu-cli auth login

权限申请说明

feishu-cli 不提供权限申请自动化。v1.18+ 移除了 config add-scopes 命令，理由：

权限开通是 tenant 管理员的职责，自动化容易造成"看起来装好了但飞书后台还没批"的幻觉
scope 选择是业务决策，不是一个 CLI 能替用户决定的"默认值"
最快的方式是一次性导入完整 JSON：打开飞书开放平台 → 你的应用 → 权限管理 → 导入权限 → 粘贴 README 的 JSON → 提交审批

当命令返回 99991672 Access denied 或 99991679 Unauthorized 时，说明应用缺少对应 scope。排查步骤：

# 1. 用 auth check 精准定位缺失的 scope
feishu-cli auth check --scope "im:message:readonly search:docs:read"
# 输出 missing=[...] 告诉你差哪些

# 2. 去飞书开放平台 → 你的应用 → 权限管理 → 搜索上一步 missing 里的 scope 逐个开通
#    或粘贴 README 的完整权限 JSON 一次性开通全部

# 3. 管理员审批通过后，按缺失 scope 重新授权
feishu-cli auth login --scope "im:message:readonly search:docs:read"

Weekly Installs
486
Repository
riba2534/feishu-cli
GitHub Stars
922
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykFail
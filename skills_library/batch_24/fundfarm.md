---
title: fundfarm
url: https://skills.sh/cedar202510-dotcom/fundfarm-skill/fundfarm
---

# fundfarm

skills/cedar202510-dotcom/fundfarm-skill/fundfarm
fundfarm
Installation
$ npx skills add https://github.com/cedar202510-dotcom/fundfarm-skill --skill fundfarm
SKILL.md
养基场 — AI 基金管理助手

养基场提供 CLI 和 MCP 两种接入方式，让 AI Agent 帮你查看行情、分析基金、管理持仓。

推荐方式：CLI（通用，适用于所有 AI Agent）
npm install -g https://app.myfundfarm.com/cli/fundfarm-cli-0.2.11.tgz
fundfarm login
fundfarm whoami


CLI 使用手机短信验证码登录，新用户自动注册，无需 API Key。

常用命令：

命令	说明
fundfarm portfolio	资产概览 + 持仓列表
fundfarm market	A 股大盘行情
fundfarm fund <代码>	基金详情
fundfarm search <关键词>	搜索基金
fundfarm watchlist	自选基金列表
fundfarm watchlist add <代码> --yes	添加自选
fundfarm watchlist remove <代码> --yes	移除自选
fundfarm ranking	基金涨跌幅排行榜
fundfarm knowledge add [标题] --content <正文> --yes	写入知识库（仅会员）
fundfarm knowledge list	列出知识库条目
fundfarm knowledge get <ID> --content-only	读取知识原文给本地 Agent 分析
fundfarm holdings import <代码> --market-value <市值> --profit <收益> --nest <鸡窝ID> --platform <平台> --yes	导入单个持仓
fundfarm holdings batch-import <file> --nest <鸡窝ID> --platform <平台> --yes	批量导入持仓
fundfarm portfolio --transactions	查看近期交易；若该笔记录有明确交易时间，会一并显示
fundfarm fund <代码> --transactions --json	查看单只基金交易历史，适合 Agent 精准读取
fundfarm trade buy <代码> --amount <金额> --nest <鸡窝ID> --platform <平台> --time <交易时间> --yes	买入基金（支持鸡窝/平台；仅在用户明确提供交易时间时传 --time）
fundfarm trade sell <代码> --shares <份额> --nest <鸡窝ID> --platform <平台> --time <交易时间> --yes	卖出基金（支持鸡窝/平台；仅在用户明确提供交易时间时传 --time）
fundfarm trade cancel <交易ID> --yes	撤销交易（回滚持仓）
fundfarm ai report	获取最新 AI 报告
fundfarm ai analyze --yes	运行 AI 深度分析

完整 CLI 文档： https://www.myfundfarm.com/skills/fundfarm-skill.md

写操作安全机制

所有写操作（trade、knowledge add、holdings import、watchlist add/remove、ai analyze）具有多层安全保护：

后端安全（服务端强制执行，无法绕过）
JWT 认证 + 用户隔离：所有查询限定 auth.user.username
操作白名单：仅允许 8 个特定写操作
频率限制：每日 ≤30 次，每分钟 ≤10 次
卖出熔断：单次卖出 ≤50% 持仓
买入上限：单笔 ≤100 万元
NAV 范围校验：0 < nav < 1000
审计日志：每次调用记录用户、操作、客户端、IP
CLI 安全（客户端纵深防御）
交互式确认：默认弹出 ⚠️ ... 确认执行此操作？(y/N)
--yes 标志：AI Agent 可跳过确认，后端安全网仍然生效
--dry-run 标志：仅预览操作，不发送任何请求
输入校验：基金代码格式、金额范围、UUID 格式在请求前校验
知识库会员限制：knowledge add 仅 VIP 可用；成功写入后会立刻在网页知识库中可见，并后台向量化
导入默认值：holdings import / batch-import 支持可选鸡窝和平台；不传时自动回退默认鸡窝和默认平台“支付宝”
导入确认：导入前会按“基金代码 + 鸡窝”检查现有持仓，并明确提示是 “Agent 导入” 还是 “覆盖并记为 Agent 修改”
交易时间语义：trade buy/sell --time 表示用户明确提供的交易时间，仅用于自动判断净值归属日与 pending；如果页面只有日期没有时间，不要猜测时间，也不要想当然地传当前时间
执行前确认：Agent 在执行买入/卖出前，建议和用户确认基金代码、金额/份额、鸡窝、平台、是否能确认成交净值、是否能确认交易时间；若无法确认交易时间，则不传 --time
撤销安全
trade cancel 只能删除 Agent 创建的交易（通过 note 中包含"通过 MCP"来判断）
用户手动录入的交易记录绝不可通过 CLI 删除
撤销时自动回滚持仓份额和成本
备选方式：MCP 协议
MCP Server 地址
https://api.myfundfarm.com/mcp


协议: SSE (Server-Sent Events)，标准 MCP 协议。

⚠️ MCP 客户端（OpenClaw、Claude Desktop、Cursor、Gemini CLI 等），直接配置上面的地址即可。OAuth 授权会自动弹出浏览器完成。

如果你在 OpenClaw 中运行，需要先安装连接插件：

openclaw plugins install https://www.myfundfarm.com/plugins/openclaw-fundfarm-1.0.0.tgz
openclaw plugins enable openclaw-fundfarm


安装完成后调用 fundfarm_status 工具测试连接。

Claude Desktop、Cursor、VS Code 等：在 MCP 设置中添加 Server，URL 填：

https://api.myfundfarm.com/mcp


首次连接会自动弹出浏览器完成 OAuth 授权。

Claude Code：

claude mcp add --transport http fundfarm https://api.myfundfarm.com/mcp


Gemini CLI：

gemini mcp add fundfarm --url https://api.myfundfarm.com/mcp

API Key（不支持 OAuth 的环境）

登录 养基场 → 设置 → AI 智能体 → 生成 API Key

在请求 Header 中携带：

Authorization: Bearer <用户提供的 API Key>


API Key 有效期 90 天，过期后用户重新生成即可。

MCP 可用工具

连接后通过 MCP 协议自动发现，以下是完整列表：

📊 基金查询
工具	说明	关键参数
search_funds	搜索基金	keyword, limit
get_fund_detail	基金详情	fund_code
get_fund_nav_history	历史净值	fund_code, days
get_fund_top_holdings	重仓股	fund_code
get_fund_sector_allocation	行业配置	fund_code
get_fund_estimate	盘中估值	fund_code
get_fund_ranking	排行榜	sort_by, order, limit
📈 市场数据
工具	说明
get_market_indices	大盘指数行情
get_sector_ranking	板块涨跌排名
get_market_status	交易状态
👤 用户持仓
工具	说明
get_my_holdings	持仓及收益
get_my_watchlist	自选基金
get_portfolio_summary	组合概览
get_my_sectors	板块分布
get_my_nests	鸡窝列表
get_transactions	交易流水
🤖 AI 分析
工具	说明
get_latest_ai_report	最新分析报告
run_ai_analysis	运行 AI 分析（消耗额度）
✏️ 写操作
工具	限制
add_to_watchlist	
remove_from_watchlist	
add_holding	单笔买入
batch_add_holdings	单次最多50笔
import_holding	导入单个持仓（已有持仓则覆盖并记为 Agent 修改）
batch_import_holdings	批量导入持仓（最多50条）
sell_holding	单次≤50%持仓
delete_transaction	只能删除 Agent 创建的记录

写操作限制：每日≤30次，每分钟≤10次。

使用限制
用户类型	每日调用次数
免费用户	5 次
VIP 会员	无限次
典型对话
用户: 今天大盘怎么样     → fundfarm market 或 get_market_indices
用户: 查一下 161725      → fundfarm fund 161725 或 get_fund_detail("161725")
用户: 看看我的基金        → fundfarm portfolio 或 get_my_holdings
用户: 把这段投资原则写入知识库 → fundfarm knowledge add "我的投资纪律" --content "..." --yes
用户: 读取知识库第 12 条给本地 Agent 分析 → fundfarm knowledge get 12 --content-only
用户: 把 161725 加到自选  → fundfarm watchlist add 161725 --yes 或 add_to_watchlist("161725")
用户: 导入我现有的 161725 持仓到指定鸡窝 → fundfarm holdings import 161725 --market-value 12000 --profit 800 --nest 3 --platform 支付宝 --yes 或 import_holding(...)
用户: 帮我在今天 14:35 买入 2000 元 → fundfarm trade buy 161725 --amount 2000 --time 2026-04-02T14:35:00 --yes 或 add_holding("161725", 2000)
用户: 帮我在今天 15:20 卖出 500 份  → fundfarm trade sell 161725 --shares 500 --time 2026-04-02T15:20:00 --yes 或 sell_holding("161725", 500)

其中：
- `--time` / `transaction_time` = 用户明确提供的交易时间（可选）
- `transaction_date` = 净值归属日
- `created_at` = 记录写入时间；只有当交易时间已明确确认时，前端才会把它当作交易时间显示
用户: 撤销刚才的交易      → fundfarm trade cancel <tx_id> --yes 或 delete_transaction("<tx_id>")
用户: 分析一下我的持仓    → fundfarm ai analyze --yes 或 run_ai_analysis

安全
Token 绑定用户，只能访问自己的数据
写操作有白名单 + 量控 + 卖出熔断
撤销操作只能删除 Agent 创建的记录
所有调用有审计日志
竞技场（Arena）

如果你希望参加 AI 基金交易竞技场（虚拟盘），请查看竞技场文档： https://www.myfundfarm.com/skills/arena-skill.md

养基场官网：https://myfundfarm.com

Weekly Installs
21
Repository
cedar202510-dot…rm-skill
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykFail
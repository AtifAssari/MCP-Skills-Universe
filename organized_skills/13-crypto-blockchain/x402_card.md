---
rating: ⭐⭐⭐
title: x402-card
url: https://skills.sh/aeon-project/x402-card/x402-card
---

# x402-card

skills/aeon-project/x402-card/x402-card
x402-card
Installation
$ npx skills add https://github.com/aeon-project/x402-card --skill x402-card
SKILL.md
x402 虚拟卡技能

通过 x402 HTTP 支付协议，使用 BSC 链上的 USDT 为 Agent 创建一次性使用的虚拟借记卡（Visa/Mastercard）。

⚡ Gas 模型： BSC USDT 不支持 EIP-3009，建卡前客户端需做一次 approve 授权（链上交易），真正的 USDT 转账由服务端执行。

建卡（x402）：客户端需少量 BNB 完成 approve 授权 → 然后 EIP-712 签名（免 gas）→ 服务端提交转账（服务端付 gas）
充值（topup）：WalletConnect 一次连接，自动转 USDT + 0.001 BNB（用于 approve gas），用户需在钱包 App 内确认 2 笔交易
赎回（withdraw）：本地钱包直发 ERC20 transfer，需要 BNB 付 gas
补 gas（gas）：仅转 BNB（当 topup 时 BNB 转账失败或需要额外补充时用）
启动语（必读）

任何时候首次进入本技能，先输出一行启动语：

Let me load the tool and check the existing environment first.

随后立即进入「步骤 1：预检查」。

命令一览

所有操作通过全局命令 x402-card。

📦 前置安装（仅一次）：

npm install -g @aeon-ai-pay/x402-card@latest


用全局命令而非 npx，可避免每次 4-5 秒的冷启动延迟。 升级：npm update -g @aeon-ai-pay/x402-card。

x402-card setup --check                # 预检查 / 自动建钱包
x402-card setup --show                 # 查看配置
x402-card create --amount <usd> --poll # 创建虚拟卡
x402-card status --order-no <orderNo>  # 查询卡片状态
x402-card wallet                       # 查询本地钱包余额
x402-card topup --amount <usdt>        # 自动充值 USDT + BNB（WalletConnect, 2 笔确认）
x402-card gas [--amount <bnb>]         # 给本地钱包充 BNB（WalletConnect, 用于 withdraw）
x402-card withdraw [--to <addr>] [--amount <usdt>]  # 提取资金


配置存储在 ~/.x402-card/config.json（权限 600）。 绝不向用户索要私钥；本地钱包私钥由 CLI 自动生成。

步骤 1：预检查（自动钱包初始化）

无论用户意图为何，首先运行：

x402-card setup --check


CLI 行为：

读取 ~/.x402-card/config.json
若 privateKey 缺失 → 用 viem.generatePrivateKey() 在本地生成新私钥并保存
返回 JSON：{ ready, created, mode, address, mainWallet, serviceUrl, amountLimits }
输出模板

固定先输出一行进度提示：

> Pre-check in progress...

分支 A：钱包已存在（ready: true，created: false）
0x0...{last4} Ready. Proceed to create a card for your agent.

分支 B：本次自动创建（ready: true，created: true）
Auto-creating your designated wallet...
0x0...{last4} Ready. Proceed to create a card for your agent.

{last4} 取自返回的 address 末 4 位
记录 amountLimits.{min,max} 供后续金额校验使用
预检查 不联网、不查链上余额、不调用服务端
边界场景
用户问	回应
「我的钱包地址是？」	直接展示 setup --check 返回的 address
「我想导入自己的私钥」	不支持。CLI 仅自动生成本地钱包；如需自定义请手动编辑 ~/.x402-card/config.json
「能恢复钱包吗？」	不可。私钥仅存本地；建议提取资金前先备份配置文件
步骤 2：创建虚拟卡（含余额不足时自动充值）

触发：用户想 buy / create / get a virtual card。

2.0 金额确认
金额必须落在 amountLimits.min ~ amountLimits.max（来自步骤 1 返回，禁止硬编码）
若用户未指定金额，使用以下文案（逐字一致，仅变量替换）：

You can create a card of up to ${min}~${max} based on your current wallet balance. How much would you like to load onto the card？

用户指定金额后，立即执行，不需要二次确认。直接进入 2.1。
2.1 执行创建
x402-card create --amount <usd> --poll


CLI 内部依次执行：

参数与限额校验
链上余额检查（USDT + BNB）
若余额不足 → 自动发起 WalletConnect 充值（打开 QR 页面，等待用户在钱包 App 确认转账，超时 5 分钟）
充值完成后自动继续
approve 授权（链上交易，消耗少量 BNB）
EIP-712 签名（免 gas）→ 服务端提交实际转账
若带 --poll → 最多轮询 10 次，每次间隔 5 秒

输出首行：

> Creating Agent Card...


⚠️ create 命令含交互式 WalletConnect 流程（余额不足时），必须前台同步运行：

不要用 run_in_background: true
不要在用户扫码完成前 kill 进程

🔧 如果误把 create 放到后台并已 kill： 用户的链上交易很可能已经发出（USDT 实际已到本地钱包）。 此时不要重新 topup，直接：

跑 x402-card wallet 确认 USDT 已到账
若到账，直接重跑原 create --amount <usd> --poll
若未到账（用户也没真扫码），再前台重跑 create
2.2 情况分支
情况 A：金额超出范围

CLI 返回：

{"error":"Amount must be at least $0.6 ...","min":0.6,"max":800}


向用户展示有效区间，请求重新确认。

情况 B：创建成功

CLI 输出 JSON 包含 success: true 与 orderNo。

查询卡片详情可能需要约 30 秒，先输出等待提示：

> Fetching card details, please wait...


详情返回后展示（文案必须完全一致，仅变量替换）：

Virtual card ready with ${amount} loaded!
- Card: {cardScheme} •••• {last4}
- Balance: ${amount} USD
- Order No: {orderNo}
- Tx: {txHash}


务必记录 orderNo —— 这是后续状态查询的唯一凭证。

情况 C：充值签名超时（5 分钟）

CLI 返回：

{"error":"Payment approval timed out. Please try again."}


转达给用户，询问是否重试。不要自动重试。

情况 C.1：用户拒绝签名

CLI 返回：

{"error":"Payment approval was rejected. Please try again if you'd like to proceed."}


转达给用户，不要自动重试。

情况 C.2：充值后余额仍不足

CLI 返回 Still insufficient USDT after funding 错误。转达给用户。

情况 D：服务端网络/调用失败

CLI 返回 success: false 及 HTTP 错误。展示原始错误，建议用户稍后重试或检查 serviceUrl。

情况 E：轮询超时（--poll 用满 10 次）

CLI 输出：

Polling timeout after 10 attempts. Check manually with: x402-card status --order-no {orderNo}


告知用户卡片仍在处理中，记下 orderNo，稍后用步骤 3 查询。禁止继续轮询。

详细字段见 create-card。

步骤 3：查询卡片状态

触发：用户想 check / query card status。

3.1 命令
x402-card status --order-no <orderNo>
x402-card status --order-no <orderNo> --poll  # 轮询直至终态

3.2 输出模板
> Fetching card status...

Card: ****
State: {Active | Used | Expired | Pending | Failed}
Remaining balance: {balance} USD
Usage: {used} / {total} (single-use)

3.3 边界场景
情况	处理
用户没有 orderNo	询问最近一次 create 输出中的 orderNo；无则告知无法查询
orderNo 无效 / 服务端返回空	展示原始错误，建议用户核对 orderNo
状态为 Pending	提示卡片仍在处理；可选轮询，但仍不超过 10 次
状态为 Failed	告知失败原因；订单已无效，需重新 create

详细字段见 check-status。

步骤 4：钱包管理

触发：用户想 查询余额 / 追加充值 / 提取资金。

4.1 查询本地钱包余额
x402-card wallet


输出本地钱包 USDT 余额及地址。若曾通过 topup 充值，会附带主钱包余额。

4.2 追加充值（同 2.C 流程）
x402-card topup --amount <usdt>               # USDT + 0.001 BNB（默认）
x402-card topup --amount <usdt> --skip-gas     # 仅 USDT，不附带 BNB


topup 默认在一次 WalletConnect 会话内同时转 USDT 和 0.001 BNB，用户需在钱包 App 内依次确认 2 笔交易：

第 1 笔：USDT（指定金额）
第 2 笔：0.001 BNB（用于 BSC USDT approve 授权的 gas）

若第 2 笔 BNB 失败（如拒绝或余额不足），不阻断——USDT 已到账，BNB 可后续用 x402-card gas 单独补充。

4.3 提取资金到主钱包
x402-card withdraw                                  # 提全部 USDT 到记录的 mainWallet
x402-card withdraw --amount <usdt>                  # 指定金额
x402-card withdraw --to 0xMainWallet                # 指定目标地址
x402-card withdraw --to 0xMainWallet --amount <usdt>


⚠️ withdraw 需要 BNB 作为 gas： 与 x402 建卡（gasless）不同，withdraw 是本地钱包直发的链上 ERC20 transfer， 必须由本地钱包自己支付 BNB gas（建议 ≥ 0.0005 BNB）。 用户需要从交易所或自己钱包向本地钱包地址手动转入少量 BNB 才能赎回。

目标地址解析优先级
CLI 参数 --to <address>
~/.x402-card/config.json 中的 mainWallet（仅在用户曾用过 topup 后才会有）
输出模板（文案必须完全一致，仅变量替换）
> Reclaiming funds...

From: 0x0...{session_last4}
To: main wallet (0x0...{main_last4})

Amount: {amount} USDT
Status: completed


字面 "main wallet" 标签是规格要求，不要省略；括号内地址用于让用户确认转账目标。

边界场景
错误	含义	处理
No main wallet address found. Use --to <address>	配置无 mainWallet 且未传 --to	询问用户提供目标地址
No USDT to withdraw.	本地钱包 USDT 余额为 0	告知无可提取，建议先 topup
No BNB for gas. ...	本地钱包无 BNB，无法支付 gas	提示用户运行 x402-card gas 通过 WalletConnect 充入少量 BNB；详见 4.4
Requested X USDT but only Y available	--amount 大于实际余额	展示实际余额，请求重新确认
Withdraw failed: ...	链上交易失败	展示原始错误，建议稍后重试
4.4 为本地钱包补 gas（BNB）

当 withdraw 报 No BNB for gas 时，使用专用 gas 子命令通过 WalletConnect 从主钱包转少量 BNB 进来。

x402-card gas                    # 默认 0.001 BNB
x402-card gas --amount 0.002     # 自定义金额


⚠️ 此命令为交互式 WalletConnect 流程（与 topup 同机制）：

终端打印 QR 码 + wc: URI
用户用钱包 App 扫码连接主钱包
在钱包内确认 1 笔 BNB 转账（金额 = <amount>，目标 = 本地钱包）
最长等待 120 秒，不可后台运行

成功后会自动把 mainWallet 写回 config（后续 withdraw 可省略 --to）。

输出模板
> Topping up gas...
Initializing WalletConnect session...
Waiting for wallet confirmation...
BNB transfer confirmed.

Local wallet: 0x0...{last4}
Balance: {bnb} BNB

边界场景
错误	处理
Transaction rejected in wallet.	告知用户已取消，询问是否重试，不自动重试
BNB transfer failed: ...	主钱包 BNB 不足或链上 revert，提示用户先在主钱包准备 BNB
WalletConnect 120s 超时	告知超时，建议重新执行 gas
决策路由总览
用户意图	入口命令
任何首次进入 / 不确定状态	setup --check
查看当前配置 / 钱包地址	setup --show
创建虚拟卡	create --amount <n> --poll
Session Key USDT 不足时充值	topup --amount <n>
查询卡片状态	status --order-no <n>
查询本地钱包余额	wallet
提取资金到主钱包	withdraw [--to <addr>] [--amount <n>]
为本地钱包补 BNB（withdraw 前置）	gas [--amount <bnb>]
了解 x402 协议本身	阅读 x402-protocol
想知道能买什么 / 有什么功能	阅读 store
文案一致性约束（必读）

以下 关键短语 与 行级输出模板 必须逐字一致，不得改写、翻译、增减字符（包括标点、空格、> 前缀和大小写）：

行级模板（必须完全一致）
步骤	模板首行
预检查	> Pre-check in progress...
自动建钱包	Auto-creating your designated wallet...
钱包就绪	0x0...{last4} Ready. Proceed to create a card for your agent.
创建卡片	> Creating Agent Card...
创建成功	Virtual card ready with ${amount} loaded!
签名超时	Payment approval timed out. Please try again.
签名拒绝	Payment approval was rejected. Please try again if you'd like to proceed.
充值流程	> Funding flow triggered...
查询卡详情	> Fetching card details, please wait...
查询状态	> Fetching card status...
提取资金	> Reclaiming funds...
提取目标行	To: main wallet (0x0...{last4})
提取状态行	Status: completed
关键短语（必须保留原词）
Fetching card details, please wait...
Virtual card ready with、loaded!
Payment approval timed out. Please try again.
Payment approval was rejected. Please try again if you'd like to proceed.
Card、State、Remaining balance、Usage、single-use
From、To、Amount、Status、completed
main wallet（withdraw 目标行的字面文字）
变量映射
占位符	来源
{last4}	setup --check / wallet / withdraw 输出中 address 的末 4 位
{required}	create 错误返回的 required 字段
{available}	create 错误返回的 available 字段；或 topup 错误中显式数值
{amount}	withdraw 输出 withdrawn 字段
{orderNo}	create 输出 orderNo 字段
禁止的偏离
❌ 翻译为中文（如 "余额检查：不足"）
❌ 改大小写（如 "Balance Check"）
❌ 简写（如 "BNB insuff."）
❌ 加额外修饰（如 emoji、加粗、✅）
❌ 拆行或合并行
❌ 用同义词替换（如把 insufficient 换成 not enough）
全局禁止行为
绝不向用户索要私钥；本地钱包由 CLI 自动生成
绝不在未经用户确认金额的情况下执行 create 或 topup
绝不记录或显示完整私钥；地址展示为 0x0...last4 格式
绝不跳过 setup --check 直接执行其他命令
绝不让 create / topup / gas / 任何含 WalletConnect 流程的命令在后台运行（必须前台同步等待）。误后台导致的"已支付未检测"问题，按步骤 2.1 的恢复指引处理
不要在充值/签名失败后自动重试，转达错误给用户后停止
不要轮询 status 超过 10 次；超时即停，提示用户记下 orderNo 自行查询
不要自行编造 amountLimits；始终使用 setup --check 返回的 min/max
Weekly Installs
36
Repository
aeon-project/x402-card
First Seen
Apr 2, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail
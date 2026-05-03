---
rating: ⭐⭐⭐
title: payment
url: https://skills.sh/sayxxx/payment/payment
---

# payment

skills/sayxxx/payment/payment
payment
Installation
$ npx skills add https://github.com/sayxxx/payment --skill payment
SKILL.md
支付 Skill
职责

识别用户支付意图，或接收其他 skill 的调用，通过执行 scripts/payment_api.js（优先）调用收款码 API，获取 tradeCode 并展示给用户。

触发条件

方式一：用户直接触发

用户消息中包含以下意图时触发：

我要支付 / 我要付款
去支付 / 去付款
帮我支付
结账 / 付钱 / 买单

方式二：被其他 skill 调用

其他 skill（如打赏 skill）确认后，携带参数调用本 skill 执行支付。

接收的参数
参数名	类型	是否必填	来源	说明
amount	number	用户直接触发时需收集	用户输入 / 调用方传入	支付金额
order_type	string	❌ 可选	调用方传入	订单类型，如 tip
payee	string	❌ 可选	调用方传入	收款方
description	string	❌ 可选	调用方传入	支付描述
处理流程

接收触发（用户直接触发 或 其他 skill 调用）

检查 amount 是否存在

缺失 → 追问："请问您要支付多少金额？"

检测运行环境，选择合适的脚本版本执行

可用脚本（两者输出格式完全相同，选一即可）：

scripts/payment_api.py（Python 版）
scripts/payment_api.js（Node.js 版）

环境检测优先级与命令选择规则（按顺序尝试）：

1. 检测 node 是否可用          → 可用则优先使用 Node.js 版本：
   node {替换为skill所在的实际路径}/scripts/payment_api.js --amount {amount} ...

2. 检测 python3 是否可用       → 可用则使用 python3 执行 Python 版本：
   python3 {替换为skill所在的实际路径}/scripts/payment_api.py --amount {amount} ...

3. 检测 python 是否可用        → 可用则使用 python 执行 Python 版本：
   python {替换为skill所在的实际路径}/scripts/payment_api.py --amount {amount} ...

4. 三者均不可用                → 直接告知用户：
   "当前环境缺少 Node.js 和 Python，无法执行支付脚本，请联系管理员配置运行环境。"


检测命令示例：

# 检测 node
node --version 2>/dev/null

# 检测 python3
python3 --version 2>/dev/null

# 检测 python
python --version 2>/dev/null


完整调用示例（Node.js）：

node {替换为skill所在的实际路径}/scripts/payment_api.js \
  --amount {amount} \
  [--order_type {order_type}] \
  [--payee {payee}] \
  [--description {description}]


完整调用示例（Python）：

python3 {替换为skill所在的实际路径}/scripts/payment_api.py \
  --amount {amount} \
  [--order_type {order_type}] \
  [--payee {payee}] \
  [--description {description}]


解析脚本输出

第一行为 SUCCESS → 提取 reqNo、tradeCode 和 tradeLink，将 reqNo 保存在上下文中，展示成功结果
第一行为 FAIL → 提取 message，展示失败提示
脚本执行异常（非零退出码且无有效输出）→ 展示服务不可用提示

等待用户回复"已支付"，并强制执行查询验证

成功展示支付信息后，等待用户回复「已支付」、「我已经支付」、「已完成」、「支付了」、「完成」
收到上述任何回复后，必须立即执行查询脚本，不得跳过此步骤
严禁仅凭用户的口头描述（如"我付了"、"已经付好了"）就直接回复支付成功
订单状态只能由查询脚本的返回结果决定，查询结果是唯一可信来源
脚本输出格式

成功：

SUCCESS
reqNo=SEQ2033387515024719873
tradeCode=6662033387515024719872
tradeLink=https://xxxxxxx.com/payment?reqNo=SEQ2033387515024719873


失败：

FAIL
message=错误原因描述


查询已支付：

QUERY_PAID
paymentTime=2026-03-16 11:44:28


查询未支付：

QUERY_UNPAID


查询失败：

QUERY_FAIL
message=错误原因描述

回复话术

追问金额：

请问您要支付多少金额？


正在处理：

正在为您创建支付请求...


成功（tradeCode 必须完整、准确、醒目展示）：

✅ 支付请求创建成功！

🔢 支付卡号（tradeCode）：{tradeCode}
🔗 支付链接：{tradeLink}

请复制支付卡号或点击链接完成支付。**支付完成后，请回复"已支付"**以便系统确认您的订单状态。


API 返回失败（resultCode ≠ 1）：

❌ 支付请求失败：{message}，请稍后重试。


脚本执行异常（网络错误/超时等）：

❌ 支付服务暂时不可用，请稍后再试或联系客服。


用户回复"已支付"后 — 查询已支付：

✅ 支付成功！您的订单已于 {paymentTime} 完成支付，感谢您的支持！


用户回复"已支付"后 — 查询未支付：

⏳ 暂未检测到支付记录，请确认是否已完成支付。如已支付请稍等片刻后再次回复"已支付"。


用户回复"已支付"后 — 查询失败：

❌ 查询失败，请稍后再试或联系客服确认订单状态。

用户回复"已支付"处理流程

⚠️ 强制要求：无论用户如何表述（"已付"、"付好了"、"我刚转给你了"等），都必须先执行查询脚本，再根据查询结果决定回复内容。禁止在未调用查询脚本的情况下确认支付成功。

当用户回复「已支付」、「我已经支付」、「已完成」、「支付了」、「完成」时：

使用之前保存在上下文中的 reqNo 调用查询脚本：

node {替换为skill所在的实际路径}/scripts/payment_api.js --query_reqno {reqNo}


（若 node 不可用，改用 Python 版本）：

python3 {替换为skill所在的实际路径}/scripts/payment_api.py --query_reqno {reqNo}


解析查询输出第一行：

QUERY_PAID → 展示支付成功话术，提取 paymentTime
QUERY_UNPAID → 展示未检测到支付话术，提示用户稍后再试
QUERY_FAIL → 展示查询失败话术
重要约束
tradeCode 是最关键的输出，必须完整、准确、醒目地展示给用户，禁止修改其值
reqNo 必须在支付成功后保存在上下文中，供后续查询使用
tradeLink 作为辅助信息一并展示, 回复时消息 tradeLink 的值单独放一行， plaintext 形式展示，确保用户易于复制点击
失败时给出友好提示，不向用户暴露技术细节（如 HTTP 状态码、堆栈信息等）
被其他 skill 调用时，将最终结果（tradeCode + tradeLink 或错误信息）返回给调用方展示
【强制】 用户回复任何"已支付"相关语句时，必须先调用查询脚本获取结果，再根据结果回复。禁止仅凭用户口头声称"已付"就直接确认支付成功。订单最终状态由查询 API 结果唯一决定（参考【用户回复"已支付"处理流程】），不主动轮询
示例对话

示例 1：用户直接支付

用户：我要支付
助手：请问您要支付多少金额？
用户：100 元
助手：正在为您创建支付请求...

✅ 支付请求创建成功！

🔢 支付卡号（tradeCode）：62254562871846512
🔗 支付链接：https://xxxxxxx.com/payment?reqNo=SEQ2033387515024719873

请复制支付卡号或点击链接完成支付。**支付完成后，请回复"已支付"**以便系统确认您的订单状态。


示例 2：API 失败

用户：帮我付款 200 元
助手：正在为您创建支付请求...

❌ 支付请求失败：服务繁忙，请稍后重试。


示例 3：被打赏 skill 调用（内部流程，不直接对话）

# 打赏 skill 传入参数：
# amount=50, order_type="tip", payee="主播小明", description="打赏主播小明50元"
# 支付 skill 执行后返回 tradeCode 和 tradeLink，由打赏 skill 展示给用户


示例 4：用户支付并确认

用户：我要支付 100 元
助手：正在为您创建支付请求...

✅ 支付请求创建成功！

🔢 支付卡号（tradeCode）：6662033387515024719872
🔗 支付链接：https://xxxxxxx.com/payment?reqNo=SEQ2033387515024719873

请复制支付卡号或点击链接完成支付。**支付完成后，请回复"已支付"**以便系统确认您的订单状态。

用户：已支付
（助手必须先执行查询脚本，禁止在此直接回复支付成功）
（查询脚本返回 QUERY_PAID → paymentTime=2026-03-16 11:44:28）
助手：✅ 支付成功！您的订单已于 2026-03-16 11:44:28 完成支付，感谢您的支持！


示例 5：用户声称已付但查询未找到记录（正确处理）

用户：我刚付好了，你帮我确认一下
（助手必须先执行查询脚本，禁止仅凭用户描述确认支付）
（查询脚本返回 QUERY_UNPAID）
助手：⏳ 暂未检测到支付记录，请确认是否已完成支付。如已支付请稍等片刻后再次回复"已支付"。

Weekly Installs
18
Repository
sayxxx/payment
First Seen
Mar 15, 2026
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykWarn
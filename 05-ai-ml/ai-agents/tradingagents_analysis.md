---
rating: ⭐⭐⭐
title: tradingagents-analysis
url: https://skills.sh/kylinmountain/tradingagents-ashare/tradingagents-analysis
---

# tradingagents-analysis

skills/kylinmountain/tradingagents-ashare/tradingagents-analysis
tradingagents-analysis
Installation
$ npx skills add https://github.com/kylinmountain/tradingagents-ashare --skill tradingagents-analysis
SKILL.md
TradingAgents 多智能体 A 股投研分析

使用 TradingAgents API，让 15 名专业 AI 分析师对 A 股进行五阶段深度协作研判，输出结构化投资建议。

🎯 快速上手

直接对我说：

"帮我分析一下贵州茅台"
"宁德时代值得买入吗"
"分析一下 600519 的技术面"
"比亚迪最近资金流向怎么样"

我会调用 15 个 AI 分析师，从市场、技术、基本面、情绪、资金五个维度深度分析，给你专业的投资建议。

🤖 系统架构：五阶段 15 智能体
阶段	智能体	职责
1. 分析团队	市场/新闻/情绪/基本面/宏观/聪明钱	多维度原始数据解读
2. 博弈裁判	博弈论管理者	主力与散户预期差分析
3. 多空辩论	多头/空头研究员 + 裁判	对立观点激烈博弈
4. 执行决策	交易员	综合研判生成操作建议
5. 风险管控	激进/中性/保守分析师 + 组合经理	多维度风控审核
TradingAgents Multi-Agent Investment Research

Use the TradingAgents API to let 15 specialized AI analysts conduct deep, five-stage collaborative research on A-Share stocks, delivering structured trading recommendations.

🤖 System Architecture: 5 Stages · 15 Agents
Stage	Agents	Role
1. Analyst Team	Market / News / Sentiment / Fundamentals / Macro / Smart Money	Multi-dimensional raw data analysis
2. Game Theory	Game Theory Manager	Main-force vs. retail expectation gap
3. Bull/Bear Debate	Bull & Bear Researchers + Judge	Adversarial viewpoint debate
4. Trade Execution	Trader	Synthesize research into actionable decision
5. Risk Control	Aggressive / Neutral / Conservative + Portfolio Manager	Multi-layer risk review
📋 适用场景

✅ 适合使用：

个股深度分析（技术面 + 基本面）
投资决策参考
盘后复盘分析
持仓标的风险评估
资金流向与市场情绪研判

❌ 不适合：

盘中实时盯盘（分析需要 1-5 分钟）
超短线交易（分钟级决策）
加密货币、美股等非 A 股市场
🔒 隐私与安全
发送范围：本技能仅从对话中提取股票名称/代码、分析日期、分析视角等参数，将其作为 symbol/trade_date/horizons 字段发送至后端 API。不发送对话原文、不读取本地文件、不上传任何其他隐私数据。
令牌安全：TRADINGAGENTS_TOKEN（格式 ta-sk-*）是访问后端的唯一凭证，请使用最小权限令牌，如怀疑泄露请立即在 app.510168.xyz 吊销并重新生成。
敏感内容提示：请勿在分析请求中粘贴个人账户信息、真实持仓或其他敏感内容，本技能无法阻止用户主动提交这些内容。
自托管：如需完全掌控数据流向，可参考 GitHub 文档 自行部署后端，并将 TRADINGAGENTS_API_URL 指向自建服务器。

关于凭证元数据：本技能的 frontmatter 在 metadata.openclaw 中声明了 TRADINGAGENTS_TOKEN 为 primaryEnv，并列入 requires.env。

🔒 Privacy & Data Transmission
What is sent: Only the extracted stock symbol, trade date, and analysis parameters (symbol, trade_date, horizons) are transmitted to the backend. The raw conversation text is never forwarded.
Token: TRADINGAGENTS_TOKEN (pattern ta-sk-*) is the sole credential. Use a minimal-privilege token and rotate it immediately if compromised.
Sensitive content: Do not paste personal account data, real positions, or other sensitive information into analysis requests.
Self-hosting: For full data sovereignty, deploy the backend yourself and set TRADINGAGENTS_API_URL to your server. See the GitHub repo.

Credential metadata: This skill's frontmatter declares TRADINGAGENTS_TOKEN as primaryEnv under metadata.openclaw.requires.env.

⚙️ 快速配置

方式一：使用官方托管服务（零部署，开箱即用）

登录 https://app.510168.xyz
进入 Settings → API Tokens 创建令牌
配置环境变量：
export TRADINGAGENTS_TOKEN="ta-sk-your_key_here"


方式二：私有化部署（数据完全自主可控）

如对数据隐私有要求，可自行部署后端，所有分析数据仅在你自己的服务器上处理：

# 1. 部署后端，参考 https://github.com/KylinMountain/TradingAgents-AShare
# 2. 将 API 地址指向自建服务
export TRADINGAGENTS_API_URL="http://your-server:8000"
export TRADINGAGENTS_TOKEN="ta-sk-your_key_here"

🚀 常用操作

推荐方式：使用一体化脚本（自动提交 → 轮询 → 获取结果）

# 脚本路径（相对于技能目录）
bash scripts/analyze.sh <symbol[,symbol2,...]> [trade_date] [horizons]

# 单个分析
bash scripts/analyze.sh 贵州茅台
bash scripts/analyze.sh 600519.SH 2026-03-22
bash scripts/analyze.sh 600519.SH 2026-03-22 medium

# 批量分析（逗号分隔，并行提交，统一等待）
bash scripts/analyze.sh 贵州茅台,比亚迪,宁德时代
bash scripts/analyze.sh 600519.SH,002594.SZ,300750.SZ 2026-03-22


脚本会自动完成：提交任务 → 每 15 秒轮询状态 → 完成后输出 JSON 结果。 批量模式下所有任务并行提交，统一轮询，最后汇总输出。超时默认 600 秒。

可通过环境变量调整行为：

POLL_INTERVAL — 轮询间隔秒数（默认 15）
POLL_TIMEOUT — 最大等待秒数（默认 600）

手动分步操作（如需单独调用某一步）

所有请求使用 $TRADINGAGENTS_TOKEN 作为 Bearer 令牌。

提交分析任务
curl -X POST "${TRADINGAGENTS_API_URL:-https://api.510168.xyz}/v1/analyze" \
  -H "Authorization: Bearer $TRADINGAGENTS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"symbol": "贵州茅台"}'

查询任务状态
curl "${TRADINGAGENTS_API_URL:-https://api.510168.xyz}/v1/jobs/{job_id}" \
  -H "Authorization: Bearer $TRADINGAGENTS_TOKEN"

获取完整分析结果（任务完成后）
curl "${TRADINGAGENTS_API_URL:-https://api.510168.xyz}/v1/jobs/{job_id}/result" \
  -H "Authorization: Bearer $TRADINGAGENTS_TOKEN"

📊 示例输出
{
  "decision": "BUY",
  "direction": "看多",
  "confidence": 78,
  "target_price": 1850.0,
  "stop_loss_price": 1680.0,
  "risk_items": [
    {"name": "估值偏高", "level": "medium", "description": "当前 PE 处于历史 75 分位"},
    {"name": "外资流出", "level": "low",    "description": "近 5 日北向资金小幅净流出"}
  ],
  "key_metrics": [
    {"name": "PE",   "value": "32.5x",  "status": "neutral"},
    {"name": "ROE",  "value": "31.2%",  "status": "good"},
    {"name": "毛利率", "value": "91.5%", "status": "good"}
  ],
  "final_trade_decision": "综合技术面突破与基本面支撑，建议逢低分批建仓..."
}

🔄 任务执行流程

深度分析通常耗时 1 至 5 分钟：

识别标的：从对话中仅提取股票名称或代码（及可选日期/视角），不发送对话原文
告知用户：反馈任务即将提交，预计耗时 1-5 分钟
执行脚本：使用 Bash 工具运行 bash scripts/analyze.sh <symbol> [date] [horizons]（设置 run_in_background: true），脚本自动完成提交、轮询和结果获取
汇总结论：脚本输出完成后，解析 JSON 结果，向用户展示决策、方向、目标价、风险点

重要：不要手动编写 curl 轮询循环，直接使用 scripts/analyze.sh 脚本。

📌 支持标的范围
沪深 A 股：中文名称（如 "比亚迪"、"宁德时代"）或代码（002594.SZ、601012.SH）
💡 注意事项
轮询频率：每次轮询间隔不低于 15 秒
数据健壮性：若部分数据源缺失，系统将基于宏观与行业逻辑进行外溢分析
短线模式：输入"分析 XX 短线"时，系统自动切换为 14 天技术面分析，跳过财报数据，速度更快
Weekly Installs
68
Repository
kylinmountain/t…s-ashare
GitHub Stars
235
First Seen
Mar 14, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
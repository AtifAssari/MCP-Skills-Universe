---
title: diagnose
url: https://skills.sh/felixwayne0318/aitrader/diagnose
---

# diagnose

skills/felixwayne0318/aitrader/diagnose
diagnose
Installation
$ npx skills add https://github.com/felixwayne0318/aitrader --skill diagnose
SKILL.md
Trading System Diagnostics
Purpose

Use this skill when:

No trading signals are being generated
Need to verify AI analysis is working
Validating technical indicator calculations
Debugging market data issues
Diagnostic Commands
Full Diagnostic (Default)
cd /home/linuxuser/nautilus_AlgVex
source venv/bin/activate
python3 scripts/diagnose.py

Quick Diagnostic (Skip AI calls)
cd /home/linuxuser/nautilus_AlgVex
source venv/bin/activate
python3 scripts/diagnose.py --quick

With Update and Restart
python3 scripts/diagnose.py --update --restart

Expected Output
Normal Operation Signs
✅ Configuration loaded successfully
✅ Market data fetched successfully
✅ TechnicalIndicatorManager initialized
✅ Technical data retrieved
✅ Sentiment data retrieved
✅ MultiAgent 层级决策成功
   🐂 Bull Agent 分析中...
   🐻 Bear Agent 分析中...
   ⚖️ Judge Agent 判断中...
   🛡️ Risk Manager 评估中...
🎯 Judge 最终决策: BUY/SELL/HOLD

Key Checkpoints
Check	Normal Value	Abnormal Handling
RSI	0-100	Out of range = data error
MACD	Any value	NaN = insufficient data
Signal	LONG/SHORT/HOLD	net_raw 阈值决策
Confidence	HIGH/MEDIUM/LOW	基于 net_raw 幅度 + zone 条件
信号决策流程 (Prism v49.0)
决策流程:
1. 数据聚合: 13 类数据 → 141 typed features
2. 3 维评分: Structure / Divergence / Order Flow → net_raw
3. 阈值决策: |net_raw| >= 0.45→HIGH, >=0.35→MED, >=0.20+zone→LOW
4. DCA 仓位: base_order_pct × equity, 最多 4 层


注意: 所有策略参数配置在 configs/base.yaml 中管理。

Common Issues
1. No Trading Signals

Possible Causes:

net_raw 低于阈值 (|raw| < 0.20)
Zone 条件不足 (低 raw 需要至少 1 个 zone)
Direction lock (连续止损锁定方向)

Check Command:

cd /home/linuxuser/nautilus_AlgVex && sudo journalctl -u nautilus-trader --since "1h ago" | grep "Hybrid decision"

2. Order Rejected (Min Notional)

Check:

cd /home/linuxuser/nautilus_AlgVex && sudo journalctl -u nautilus-trader --since "1h ago" | grep "notional\|rejected\|-4164"

3. Abnormal Technical Indicators

Check:

python3 scripts/diagnose.py 2>&1 | grep -E "(RSI|MACD|SMA)"

Key Files
File	Purpose
scripts/diagnose.py	Main diagnostic script
scripts/diagnose_realtime.py	Real-time API diagnostic
scripts/diagnostics/	Modular diagnostic system
scripts/smart_commit_analyzer.py	Regression detection (auto-evolving rules)
strategy/ai_strategy.py	Main strategy logic
configs/base.yaml	Base configuration (all parameters)
configs/production.yaml	Production environment overrides
Order Flow Simulation (v3.18)

模块化诊断系统包含 7 个订单流场景模拟。

7 Scenarios (模拟场景)
场景	描述	测试目标
1. New Position	开新仓 (无现有持仓)	Bracket 订单创建
2. Add to Position	加仓 (同方向)	SL/TP 数量更新
3. Reduce Position	减仓	SL/TP 数量减少
4. Reversal	反转仓位 (多→空/空→多)	两阶段提交逻辑
5. Close Position	平仓信号	仓位关闭 + 取消 SL/TP
6. Bracket Failure	SL/TP 订单失败	CRITICAL 告警 (不回退)
7. SL/TP Modify Failure	SL/TP 修改失败	WARNING 告警
Run Order Flow Simulation
cd /home/linuxuser/nautilus_AlgVex
source venv/bin/activate
python3 scripts/diagnose_realtime.py


诊断输出将包含 "Step 9: Order Flow Simulation (v3.18)" 显示所有 7 个场景的模拟结果。

Expected Output
============================================================
Step 9: Order Flow Simulation (v3.18)
============================================================
✅ Scenario 1: New Position - PASSED
✅ Scenario 2: Add to Position - PASSED
✅ Scenario 3: Reduce Position - PASSED
✅ Scenario 4: Reversal - PASSED
✅ Scenario 5: Close Position - PASSED
✅ Scenario 6: Bracket Failure - PASSED
✅ Scenario 7: SL/TP Modify Failure - PASSED

📊 Order Flow Simulation Summary: 7/7 scenarios passed

回归检测 (修改代码后必须运行)
# 智能回归检测 (规则自动从 git 历史生成)
python3 scripts/smart_commit_analyzer.py

# 预期结果: ✅ 所有规则验证通过

Weekly Installs
12
Repository
felixwayne0318/aitrader
GitHub Stars
1
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykFail
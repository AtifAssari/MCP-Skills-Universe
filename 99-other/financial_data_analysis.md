---
title: financial-data-analysis
url: https://skills.sh/kirkluokun/awesome-a-stock-openclawskills/financial-data-analysis
---

# financial-data-analysis

skills/kirkluokun/awesome-a-stock-openclawskills/financial-data-analysis
financial-data-analysis
Installation
$ npx skills add https://github.com/kirkluokun/awesome-a-stock-openclawskills --skill financial-data-analysis
SKILL.md
📊 金融时间序列分析工具箱

覆盖股票 / 商品期货 / 加密货币 / ETF / 外汇 / 指数的综合数据分析方法工具箱。

数据获取策略
资产类型	数据源	方式
A股行情/财务/指数	Tushare MCP	tushare_daily, tushare_income 等 MCP tool
A股期货	Tushare MCP	tushare_fut_daily, tushare_fut_holding 等
港股/美股	Tushare MCP	tushare_hk_daily, tushare_us_daily
宏观经济	Tushare MCP	tushare_cn_gdp, tushare_shibor 等
国际商品期货(WTI/黄金等)	yfinance	scripts/data_fetcher.py
加密货币	yfinance	scripts/data_fetcher.py
外汇	Tushare MCP 或 yfinance	视具体币种
全球指数	Tushare MCP 或 yfinance	tushare_index_global / yfinance

规则：调用 tushare MCP tool 前必须先 ToolSearch("+tushare <关键词>") 加载。 tushare tool 完整索引见 stock-tushare-pro-mcp skill 的 reference/tool-index.md。

分析方法路由

根据用户意图，阅读对应 references/methods/ 文档后执行分析：

用户意图关键词	参考文档	可用脚本
平稳性、趋势检验、序列分解、结构断裂、Hurst	references/methods/01_time_series_fundamentals.md	scripts/analysis_toolkit.py
价格预测、ARIMA、Prophet、VAR	references/methods/02_forecasting.md	scripts/analysis_toolkit.py
相关性、协整、因果关系、领先滞后	references/methods/03_cross_asset_relationships.md	scripts/analysis_toolkit.py
波动率、GARCH、VaR、尾部风险	references/methods/04_volatility_and_risk.md	scripts/analysis_toolkit.py
组合优化、因子分析、风险平价、有效前沿	references/methods/05_portfolio_and_factor.md	scripts/analysis_toolkit.py
市场状态、regime、周期、小波	references/methods/06_regime_and_structure.md	scripts/analysis_toolkit.py
商品季节性、价差、期限结构、contango	references/methods/07_commodity_specific.md	scripts/analysis_toolkit.py
网络分析、信息流、聚类、MST	references/methods/08_network_and_information.md	scripts/analysis_toolkit.py
技术指标（MA/RSI/MACD/KDJ/布林带）	references/methods/01_time_series_fundamentals.md	scripts/indicators.py
图表绘制、可视化	references/visualization_cookbook.md	—
报告格式	references/output_templates.md	—
执行流程
1. 识别用户意图 → 查上方路由表
2. 读取对应 references/methods/ 文档 → 选择合适方法
3. 获取数据：tushare MCP tool（优先）或 scripts/data_fetcher.py
4. 执行分析：scripts/analysis_toolkit.py 或 scripts/indicators.py
5. 生成图表：参照 references/visualization_cookbook.md
6. 输出报告：按 references/output_templates.md 格式

约束
MUST
标注数据获取时间和来源（tushare / yfinance）
每份报告附免责声明
分析前检查序列平稳性（适用时）
异常值标注和处理
MUST NOT
❌ 给出确定性收益承诺
❌ 伪造或编造数据
❌ 忽略风险提示
❌ 数据缺失时猜测关键指标
输出存储规范
输出目录

默认根目录为 {output_dir}（由 input-variables 配置，默认 {workspace}/data/analysis/）。

{output_dir}/
├── reports/        # 分析报告 (.md)
├── charts/         # 图表文件 (.png)
├── datasets/       # 中间数据集 (.csv)
└── temp/           # 临时数据（可清理）

文件命名
{类型}_{标的}_{日期}.{格式}


示例：

report_CU_20260306.md
chart_AAPL_seasonal_20260306.png
dataset_corr_matrix_20260306.csv
输出规则
数据量	处理方式
< 20 行	直接在对话中展示，不存文件
>= 20 行	存入 datasets/，返回文件路径 + 摘要
图表	存入 charts/，在对话中内嵌展示
分析报告	存入 reports/，返回完整报告
临时/中间数据	存入 temp/，提醒用户可清理

与 tushare skill 协作：原始行情数据存储遵循 tushare skill 的 output-storage.md 规范（{workspace}/data/tushare/）， 本 skill 的 {output_dir} 只存分析结果，不存原始数据，避免重复。

参数使用

所有可配置参数通过 input-variables 声明，AI 在执行时按如下优先级获取值：

用户在对话中明确指定 -> 最高优先
input-variables 中的 default 值 -> 兜底
# 用户说 "把分析结果存到 ~/Desktop/analysis"
-> output_dir = ~/Desktop/analysis

# 用户说 "分析铜价"
-> output_dir = {workspace}/data/analysis (使用默认值)
-> default_period = 1y (使用默认值)

Weekly Installs
153
Repository
kirkluokun/awes…awskills
GitHub Stars
41
First Seen
Mar 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
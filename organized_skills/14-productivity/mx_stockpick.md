---
rating: ⭐⭐
title: mx-stockpick
url: https://skills.sh/site/skills.volces.com/mx-stockpick
---

# mx-stockpick

skills/skills.volces.com/MX_StockPick
MX_StockPick
$ npx skills add https://skills.volces.com/skills/clawhub/financial-ai-analyst
SKILL.md
选股 / 选板块 / 选基金

通过自然语言查询进行选股，数据来自于妙想大模型服务，支持以下类型：

A股、港股、美股
基金、ETF、可转债、板块
密钥来源与安全说明
本技能仅使用一个环境变量：EM_API_KEY。
EM_API_KEY 由东方财富妙想服务（https://ai.eastmoney.com/mxClaw）签发，用于其接口鉴权。
在提供密钥前，请先确认密钥来源、可用范围、有效期及是否支持重置/撤销。
禁止在代码、提示词、日志或输出文件中硬编码/明文暴露密钥。
功能范围
基础选股能力
按股价、市值、涨跌幅、市盈率等财务/行情指标筛选
按技术信号筛选（如连续上涨、突破均线等）
按主营业务、主要产品筛选
按行业/概念板块筛选成分股
获取指数成分股
推荐股票、基金、板块
按多种复合条件（如且、或、非、排序等）的逻辑组合筛选
A股进阶查询（部分场景）

除基础选股外，还支持A股上市公司的以下查询场景：

高管信息、股东信息
龙虎榜数据
分红、并购、增发、回购
主营区域
券商金股

注意：上述仅为部分示例，实际支持的条件远多于列举内容

查询示例
类型	query	select-type
选A股	股价大于500元的股票、创业板市盈率最低的50只	A股
选港股	港股的科技龙头	港股
选美股	纳斯达克市值前30、苹果产业链美股	美股
选板块	今天涨幅最大板块	板块
选基金	白酒主题基金、新能源混合基金近一年收益排名	基金
选ETF	规模超2亿的电力ETF	ETF
选可转债	价格低于110元、溢价率超5个点的可转债	可转债
前提条件
1. 注册东方财富妙想账号

访问 https://ai.eastmoney.com/mxClaw 注册账号并获取API_KEY。

2. 配置 Token
# 添加到 ~/.zshrc
export EM_API_KEY="your_api_key_here"


然后执行：

source ~/.zshrc

3. 安装依赖
pip3 install httpx --user

快速开始
1. 命令行调用
python3 {baseDir}/scripts/get_data.py --query 股价大于100元，主力流入，成交额排名前50 --select-type A股


输出示例

CSV: /path/to/miaoxiang/MX_StockPick/MX_StockPick_9535fe18.csv
描述: /path/to/miaoxiang/MX_StockPick/MX_StockPick_9535fe18_description.txt
行数: 42


参数说明：

参数	说明	必填
--query	自然语言查询条件	✅
--select-type	查询领域	✅
2. 代码调用
import asyncio
from pathlib import Path
from scripts.get_data import query_MX_StockPick

async def main():
    result = await query_MX_StockPick(
        query="A股半导体板块市值前20",
        selectType="A股",
        output_dir=Path("miaoxiang/MX_StockPick"),
    )
    if "error" in result:
        print(result["error"])
    else:
        print(result["csv_path"], result["row_count"])

asyncio.run(main())

输出文件说明
文件	说明
MX_StockPick_<查询ID>.csv	全量数据表，列名为中文（由返回的 columns 映射），UTF-8 编码，可用 Excel 或 pandas 打开
MX_StockPick_<查询ID>_description.txt	数据说明：查询内容、行数、列名说明等
环境变量
变量	说明	默认
MX_StockPick_OUTPUT_DIR	CSV 与描述文件的输出目录（可选）	miaoxiang/MX_StockPick
EM_API_KEY	妙想智能选股工具 API 密钥（必备）	无
常见问题

错误：请设置 EM_API_KEY 环境变量

请访问 https://ai.eastmoney.com/mxClaw 获取API_KEY。
配置EM_API_KEY环境变量

如何指定输出目录？

export MX_StockPick_OUTPUT_DIR="/path/to/output"
python3 {baseDir}/scripts/get_data.py --query "查询内容" --select-type "查询领域"

Weekly Installs
10
Source
skills.volces.c…-analyst
First Seen
3 days ago
---
rating: ⭐⭐⭐
title: stock-daily-analysis
url: https://skills.sh/chjm-ai/stock-daily-analysis-skill/stock-daily-analysis
---

# stock-daily-analysis

skills/chjm-ai/stock-daily-analysis-skill/stock-daily-analysis
stock-daily-analysis
Installation
$ npx skills add https://github.com/chjm-ai/stock-daily-analysis-skill --skill stock-daily-analysis
Summary

LLM-powered daily stock analysis across A-shares, Hong Kong, and US markets with technical indicators and AI-driven signals.

Analyzes multiple markets (A-shares, Hong Kong, US stocks) with technical indicators including moving averages, MACD, RSI, and bias rate
Generates trend status, buy signal scores, and AI-driven operation advice with target prices and stop-loss levels
Supports batch analysis of multiple stocks and optional integration with market-data skill for enhanced data stability
Configurable AI providers (DeepSeek, Gemini, OpenAI) for deeper analysis and decision recommendations
SKILL.md
Daily Stock Analysis for OpenClaw

基于 LLM 的 A/H/美股智能分析 Skill，提供技术面分析和 AI 决策建议。

功能特性
多市场支持 - A股、港股、美股
技术面分析 - MA5/10/20、MACD、RSI、乖离率
趋势交易 - 多头排列判断、买入信号评分
AI 决策 - DeepSeek/Gemini/OpenAI 深度分析
数据源集成 - 可选 market-data skill
快速使用
from scripts.analyzer import analyze_stock, analyze_stocks

# 单只分析
result = analyze_stock('600519')
print(result['ai_analysis']['operation_advice'])

# 批量分析
results = analyze_stocks(['600362', '601318', '159892'])

配置
复制配置模板：
cp config.example.json config.json

填入 DeepSeek API Key：
{
  "ai": {
    "provider": "openai",
    "api_key": "sk-your-deepseek-key",
    "base_url": "https://api.deepseek.com/v1",
    "model": "deepseek-chat"
  }
}

(可选) 启用 market-data skill 数据源：
{
  "data": {
    "use_market_data_skill": true,
    "market_data_skill_path": "../market-data"
  }
}

返回数据
{
    'code': '600519',
    'name': '贵州茅台',
    'technical_indicators': {
        'trend_status': '强势多头',
        'ma5': 1500.0, 'ma10': 1480.0, 'ma20': 1450.0,
        'bias_ma5': 2.5,
        'macd_status': '金叉',
        'rsi_status': '强势买入',
        'buy_signal': '买入',
        'signal_score': 75
    },
    'ai_analysis': {
        'sentiment_score': 75,
        'operation_advice': '买入',
        'confidence_level': '高',
        'target_price': '1550',
        'stop_loss': '1420'
    }
}

项目信息
开源协议: MIT
项目地址: https://github.com/yourusername/stock-daily-analysis
原项目: https://github.com/ZhuLinsen/daily_stock_analysis

⚠️ 免责声明: 本项目仅供学习研究，不构成投资建议。股市有风险，投资需谨慎。

Weekly Installs
1.1K
Repository
chjm-ai/stock-d…is-skill
GitHub Stars
151
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn
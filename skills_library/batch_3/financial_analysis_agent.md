---
title: financial-analysis-agent
url: https://skills.sh/qodex-ai/ai-agent-skills/financial-analysis-agent
---

# financial-analysis-agent

skills/qodex-ai/ai-agent-skills/financial-analysis-agent
financial-analysis-agent
Installation
$ npx skills add https://github.com/qodex-ai/ai-agent-skills --skill financial-analysis-agent
Summary

Build intelligent agents for investment analysis, risk assessment, and portfolio recommendations.

Integrates financial data collection via yfinance with technical analysis (moving averages, RSI, support/resistance) and fundamental analysis (profitability, valuation, and liquidity ratios)
Includes risk assessment tools covering volatility, Value at Risk, Sharpe Ratio, and company-specific risk evaluation
Generates investment recommendations (Strong Buy through Strong Sell) with confidence levels and investment scores based on combined technical and fundamental signals
Provides portfolio management capabilities including valuation, rebalancing, and risk calculation across holdings
Emphasizes multi-source validation, downside risk assessment, diversification, and ethical disclosure in recommendation workflows
SKILL.md
Financial Analysis Agent

Build intelligent financial analysis agents that evaluate investments, assess risks, and generate data-driven recommendations.

Financial Data Integration

See examples/financial_data_collector.py for the FinancialDataCollector class that:

Integrates with yfinance for stock data
Retrieves financial statements (income, balance sheet, cash flow)
Fetches key metrics (market cap, PE ratio, dividend yield, etc.)
Financial Analysis Techniques
Technical Analysis

See examples/technical_analyzer.py for TechnicalAnalyzer:

Moving averages calculation
Relative Strength Index (RSI)
Support and resistance level identification
Fundamental Analysis

See examples/fundamental_analyzer.py for FundamentalAnalyzer:

Profitability ratios (gross margin, operating margin, net margin, ROA, ROE)
Valuation ratios (PE, PB, PEG, price-to-sales)
Liquidity ratios (current ratio, quick ratio, debt-to-equity)
Risk Assessment

See examples/risk_analyzer.py for RiskAnalyzer:

Volatility calculation
Value at Risk (VaR) assessment
Sharpe Ratio calculation
Company risk assessment
Investment Recommendations

See examples/investment_recommender.py for InvestmentRecommender:

Generates recommendations (Strong Buy, Buy, Hold, Sell, Strong Sell)
Calculates investment scores based on technical and fundamental signals
Provides confidence levels and risk assessments
Portfolio Management

See examples/portfolio_manager.py for PortfolioManager:

Calculate portfolio total value
Rebalance portfolio based on target allocations
Assess portfolio risk and volatility
Market Intelligence

Build market intelligence capabilities by:

Analyzing overall market trends and sector performance
Calculating market volatility indices
Fetching economic indicators
Identifying undervalued, growth, and dividend opportunities
Best Practices
Analysis Quality
✓ Use multiple data sources
✓ Cross-validate findings
✓ Document assumptions
✓ Consider time horizons
✓ Account for fees and taxes
Risk Management
✓ Assess downside risk
✓ Implement stop losses
✓ Diversify appropriately
✓ Position size accordingly
✓ Review regularly
Ethical Considerations
✓ Disclose conflicts of interest
✓ Avoid market manipulation
✓ Base recommendations on analysis
✓ Update recommendations regularly
✓ Acknowledge limitations
Tools & Data Sources
Data APIs
yfinance
Alpha Vantage
IEX Cloud
Polygon.io
Yahoo Finance
Analysis Libraries
pandas
NumPy
scikit-learn
TA-Lib
statsmodels
Getting Started
Collect financial data
Perform technical analysis
Analyze fundamentals
Assess risks
Generate recommendations
Monitor positions
Rebalance periodically
Weekly Installs
802
Repository
qodex-ai/ai-agent-skills
GitHub Stars
6
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
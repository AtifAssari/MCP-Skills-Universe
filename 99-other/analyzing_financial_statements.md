---
title: analyzing-financial-statements
url: https://skills.sh/anthropics/claude-cookbooks/analyzing-financial-statements
---

# analyzing-financial-statements

skills/anthropics/claude-cookbooks/analyzing-financial-statements
analyzing-financial-statements
Installation
$ npx skills add https://github.com/anthropics/claude-cookbooks --skill analyzing-financial-statements
SKILL.md
Financial Ratio Calculator Skill

This skill provides comprehensive financial ratio analysis for evaluating company performance, profitability, liquidity, and valuation.

Capabilities

Calculate and interpret:

Profitability Ratios: ROE, ROA, Gross Margin, Operating Margin, Net Margin
Liquidity Ratios: Current Ratio, Quick Ratio, Cash Ratio
Leverage Ratios: Debt-to-Equity, Interest Coverage, Debt Service Coverage
Efficiency Ratios: Asset Turnover, Inventory Turnover, Receivables Turnover
Valuation Ratios: P/E, P/B, P/S, EV/EBITDA, PEG
Per-Share Metrics: EPS, Book Value per Share, Dividend per Share
How to Use
Input Data: Provide financial statement data (income statement, balance sheet, cash flow)
Select Ratios: Specify which ratios to calculate or use "all" for comprehensive analysis
Interpretation: The skill will calculate ratios and provide industry-standard interpretations
Input Format

Financial data can be provided as:

CSV with financial line items
JSON with structured financial statements
Text description of key financial figures
Excel files with financial statements
Output Format

Results include:

Calculated ratios with values
Industry benchmark comparisons (when available)
Trend analysis (if multiple periods provided)
Interpretation and insights
Excel report with formatted results
Example Usage

"Calculate key financial ratios for this company based on the attached financial statements"

"What's the P/E ratio if the stock price is $50 and annual earnings are $2.50 per share?"

"Analyze the liquidity position using the balance sheet data"

Scripts
calculate_ratios.py: Main calculation engine for all financial ratios
interpret_ratios.py: Provides interpretation and benchmarking
Best Practices
Always validate data completeness before calculations
Handle missing values appropriately (use industry averages or exclude)
Consider industry context when interpreting ratios
Include period comparisons for trend analysis
Flag unusual or concerning ratios
Limitations
Requires accurate financial data
Industry benchmarks are general guidelines
Some ratios may not apply to all industries
Historical data doesn't guarantee future performance
Weekly Installs
12
Repository
anthropics/clau…ookbooks
GitHub Stars
42.0K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
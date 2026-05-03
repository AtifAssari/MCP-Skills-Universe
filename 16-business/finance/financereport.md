---
rating: ⭐⭐⭐
title: financereport
url: https://skills.sh/aojdevstudio/finance-guru/financereport
---

# financereport

skills/aojdevstudio/finance-guru/FinanceReport
FinanceReport
Installation
$ npx skills add https://github.com/aojdevstudio/finance-guru --skill FinanceReport
Summary

Generate institutional-quality PDF investment reports for stocks and ETFs with embedded charts and portfolio sizing.

Produces 8–10 page reports with VGT-style branding, executive summary, quantitative analysis tables, and strategy recommendations
Integrates Perplexity MCP for market sentiment and catalyst research, plus built-in quant tools for risk metrics, momentum indicators, and volatility assessment
Supports three workflows: single ticker reports, batch regeneration across watchlists, and full deep-research analysis with market and strategy phases
Calculates position sizing in both percentage and dollar amounts based on user portfolio value from stored profile data
SKILL.md
FinanceReport

Generate comprehensive 8-10 page PDF investment analysis reports with Finance Guru branding.

Workflow Routing

When executing a workflow, output this notification directly:

Running the **WorkflowName** workflow from the **FinanceReport** skill...

Workflow	Trigger	File
GenerateSingleReport	"generate report for TSLA", "create PDF"	workflows/GenerateSingleReport.md
RegenerateBatch	"regenerate batch", "redo all reports"	workflows/RegenerateBatch.md
FullResearchWorkflow	"full analysis", "thorough research"	workflows/FullResearchWorkflow.md
Examples

Example 1: Generate single ticker report

User: "Generate a report for NVDA"
-> Invokes GenerateSingleReport workflow
-> Runs quant tools (risk_metrics, momentum, volatility)
-> Fetches sentiment via Perplexity MCP
-> Builds 8-10 page PDF with VGT-style header
-> Saves to fin-guru-private/fin-guru/analysis/reports/NVDA-analysis-2025-12-18.pdf


Example 2: Regenerate all watchlist reports

User: "Regenerate batch 1 reports"
-> Invokes RegenerateBatch workflow
-> Launches 8 subagents in parallel
-> Each runs FullResearchWorkflow
-> Replaces existing PDFs with improved versions


Example 3: Deep research with full workflow

User: "Do a full analysis on AMZN for the 2026 watchlist"
-> Invokes FullResearchWorkflow
-> Phase 1: Market research (Perplexity/Exa for catalysts, risks)
-> Phase 2: Quant analysis (252-day risk metrics, 90-day momentum)
-> Phase 3: Strategy recommendation (buy/hold/sell, position sizing)
-> Phase 4: Generate comprehensive PDF report

Report Structure (8-10 Pages)
Cover Page (VGT-Style Header) - UNIFORM STANDARD

CRITICAL: Every report MUST follow this EXACT format:

┌─────────────────────────────────────────────────────────────┐
│                    FINANCE GURU™                            │
│             Family Office Investment Analysis               │
│  ─────────────────────────────────────────────────────────  │
│                                                             │
│              TICKER - Full Company/Fund Name                │
│           2026 Watchlist Analysis & Investment Report       │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  Report Date:      December 18, 2025                        │
│  Analyst Team:     Finance Guru Multi-Agent System          │
│                    • Market Researcher (Dr. Aleksandr Petrov)│
│                    • Quant Analyst                          │
│                    • Strategy Advisor                       │
│  Current Price:    $XXX.XX                                  │
│  YTD Performance:  +XX.XX%                                  │
│  Expense Ratio:    0.XX% (ETFs only)                        │
└─────────────────────────────────────────────────────────────┘


UNIFORMITY RULES:

Analyst team names MUST be listed on EVERY report
"Finance Guru Multi-Agent System" header REQUIRED
Individual analyst names with personas (e.g., Dr. Aleksandr Petrov)
Same format, same structure, every single time
Executive Summary
Investment thesis (200+ words)
Key findings with bold labels
Final verdict box (rating, conviction, risk level)
Quantitative Analysis
Risk metrics table (VaR, Sharpe, Beta, Alpha)
Momentum indicators (RSI, MACD, Stochastic)
Volatility assessment (ATR, Bollinger regime)
Embedded charts where applicable

TABLE FORMATTING - CRITICAL:

All table cells use Paragraph objects (text wraps, never overflows)
Column widths explicitly set to fit within 7.5" content area
Header row: Navy background, white text, bold
Data rows: Alternating white/light gray backgrounds
Market Research
Company overview and positioning
2026 catalysts and risks
Analyst ratings and sentiment
Perplexity MCP integration
Portfolio Sizing (NEW)

Shows BOTH percentage AND dollar amount:

Recommended Allocation: 2-3%
For $250,000 portfolio:
  - Dollar amount: $5,000 - $7,500
  - Share count: ~25-38 shares at $200

Strategy Recommendations
Entry strategy with price targets
Risk management (stop-loss levels)
Position management approach
Sources & Disclaimer - UNIFORM STANDARD

CRITICAL: Every report MUST end with this EXACT format:

─────────────────────────────────────────────────────────────
DISCLAIMER: This analysis is provided for educational and
informational purposes only. [full disclaimer text]

                Powered by Finance Guru™
              Report Date: December 18, 2025
─────────────────────────────────────────────────────────────


"Powered by Finance Guru™" is REQUIRED on every report.

Tool Usage
ChartKit.py
uv run python .claude/skills/FinanceReport/tools/ChartKit.py \
  --ticker TSLA \
  --chart-type line \
  --data-source cli

ReportGenerator.py
uv run python .claude/skills/FinanceReport/tools/ReportGenerator.py \
  --ticker TSLA \
  --portfolio-value 250000 \
  --output-dir fin-guru-private/fin-guru/analysis/reports/

Integration Points
Perplexity MCP (Sentiment & Research)
# Search for market sentiment
mcp__perplexity__search(query=f"{ticker} stock analysis 2025 catalysts risks")

# Deep reasoning for thesis
mcp__perplexity__reason(query=f"Analyze {ticker} investment thesis for 2026")

Existing Finance Guru CLI Tools
src/analysis/risk_metrics_cli.py - VaR, CVaR, Sharpe, Sortino, Beta, Alpha
src/utils/momentum_cli.py - RSI, MACD, Stochastic, Williams %R
src/utils/volatility_cli.py - ATR, Bollinger Bands, Keltner Channels
src/analysis/correlation_cli.py - Portfolio correlation matrix
User Profile

Reads portfolio value from fin-guru/data/user-profile.yaml for sizing:

investment_portfolio.total_value = Current portfolio value
Calculates exact dollar amounts for recommendations
Reference Files
StyleGuide.md - Brand colors, typography, table styling
VisGuide.md - Chart selection dictionary, labeling standards

Skill Type: Domain Enforcement: Suggest Priority: High Line Count: < 200 lines

Weekly Installs
584
Repository
aojdevstudio/fi…nce-guru
GitHub Stars
303
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn
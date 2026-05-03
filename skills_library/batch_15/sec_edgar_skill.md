---
title: sec-edgar-skill
url: https://skills.sh/eng0ai/eng0-template-skills/sec-edgar-skill
---

# sec-edgar-skill

skills/eng0ai/eng0-template-skills/sec-edgar-skill
sec-edgar-skill
Installation
$ npx skills add https://github.com/eng0ai/eng0-template-skills --skill sec-edgar-skill
SKILL.md
SEC EDGAR Skill - Filing Analysis
Prerequisites

CRITICAL: Run this setup before ANY EdgarTools operations:

from edgar import set_identity
set_identity("Your Name your.email@example.com")  # SEC requires identification


This is a SEC legal requirement. Operations will fail without it.

Installation

EdgarTools must be installed:

pip install edgartools

Token Efficiency Strategy

ALWAYS use .to_context() first - it provides summaries with 56-89% fewer tokens:

Object	repr() tokens	.to_context() tokens	Savings
Company	~750	~75	90%
Filing	~125	~50	60%
XBRL	~2,500	~275	89%
Statement	~1,250	~400	68%

Rule: Call .to_context() first to understand what's available, then drill down.

Three Ways to Access Filings
1. Published Filings - Bulk Cross-Company Analysis
from edgar import get_filings

# Get recent 10-K filings
filings = get_filings(form="10-K")

# Filter by date range
filings = get_filings(form="10-K", year=2024, quarter=1)

# Multiple form types
filings = get_filings(form=["10-K", "10-Q"])

2. Current Filings - Real-Time Monitoring
from edgar import get_current_filings

# Get today's filings from RSS feed
current = get_current_filings()

# Filter by form type
current_10k = get_current_filings().filter(form="10-K")

3. Company Filings - Single Entity Analysis
from edgar import Company

# By ticker
company = Company("AAPL")

# By CIK
company = Company("0000320193")

# Get company's filings
filings = company.get_filings(form="10-K")
latest_10k = filings.latest()

Financial Data Access
Method 1: Entity Facts API (Fast, Multi-Period)

Best for comparing trends across periods:

company = Company("AAPL")

# Get income statement for multiple periods
income = company.income_statement(periods=5)
print(income)  # Shows 5 years of data

# Get balance sheet
balance = company.balance_sheet(periods=3)

# Get cash flow
cashflow = company.cash_flow_statement(periods=3)

Method 2: Filing XBRL (Detailed, Single Period)

Best for comprehensive single-filing analysis:

company = Company("AAPL")
filing = company.get_filings(form="10-K").latest()

# Get XBRL data
xbrl = filing.xbrl()

# Access financial statements
statements = xbrl.statements
income_stmt = statements.income_statement
balance_sheet = statements.balance_sheet
cash_flow = statements.cash_flow_statement

Common Workflows
Workflow 1: Compare Revenue Across Companies
from edgar import Company

companies = ["AAPL", "MSFT", "GOOGL"]
for ticker in companies:
    company = Company(ticker)
    income = company.income_statement(periods=3)
    print(f"\n{ticker} Revenue Trend:")
    print(income)

Workflow 2: Analyze Latest 10-K
from edgar import Company

company = Company("NVDA")
filing = company.get_filings(form="10-K").latest()

# Get filing metadata
print(filing.to_context())

# Get full text (expensive - 50K+ tokens)
# text = filing.text()

# Get specific sections
# items = filing.items()  # Risk factors, MD&A, etc.

Workflow 3: Track Insider Trading
from edgar import Company

company = Company("TSLA")
insider_filings = company.get_filings(form="4")  # Form 4 = insider trades

for filing in insider_filings[:10]:
    print(filing.to_context())

Workflow 4: Monitor Recent Filings by Sector
from edgar import get_filings

# Get recent tech 10-Ks (use SIC codes)
# SIC 7370-7379 = Computer Programming, Data Processing
filings = get_filings(form="10-K", year=2024)
# Filter by company characteristics after retrieval

Workflow 5: Multi-Year Financial Trend
from edgar import Company

company = Company("AMZN")

# 5-year income statement
income = company.income_statement(periods=20)  # 20 quarters = 5 years

# 5-year balance sheet
balance = company.balance_sheet(periods=20)

print("Income Statement Trend:")
print(income)
print("\nBalance Sheet Trend:")
print(balance)

Search Within Filings

CRITICAL DISTINCTION:

filing = company.get_filings(form="10-K").latest()

# Search WITHIN the filing document (finds text in the 10-K)
results = filing.search("climate risk")

# Search API DOCUMENTATION (finds how to use EdgarTools)
docs_results = filing.docs.search("how to extract")


Do NOT mix these up!

Key Objects Reference
Company
company = Company("AAPL")
company.to_context()  # Summary with available actions
company.name          # Company name
company.cik           # CIK number
company.sic           # SIC code
company.industry      # Industry description
company.get_filings() # Access filings

Filing
filing.to_context()   # Summary
filing.form           # Form type (10-K, 10-Q, etc.)
filing.filing_date    # Date filed
filing.accession_number
filing.text()         # Full document text (EXPENSIVE)
filing.markdown()     # Markdown format
filing.xbrl()         # XBRL financial data
filing.items()        # Document sections

XBRL (Financial Data)
xbrl = filing.xbrl()
xbrl.to_context()     # Summary
xbrl.statements       # All financial statements
xbrl.facts            # Individual facts/metrics

Statement (Financial Statement)
stmt = xbrl.statements.income_statement
print(stmt)           # ASCII table format
stmt.to_dataframe()   # Pandas DataFrame

Anti-Patterns (Avoid These)
DON'T: Parse financials from raw text
# BAD - expensive and error-prone
text = filing.text()
# try to regex parse revenue from text...

DO: Use structured XBRL data
# GOOD - structured and accurate
income = company.income_statement(periods=3)

DON'T: Load full filing when you only need metadata
# BAD - wastes tokens
text = filing.text()  # 50K+ tokens

DO: Use context first
# GOOD - minimal tokens
print(filing.to_context())  # ~50 tokens

Form Types Quick Reference
Form	Description	Use Case
10-K	Annual report	Full-year financials, business description
10-Q	Quarterly report	Quarterly financials
8-K	Current report	Material events (M&A, exec changes)
DEF 14A	Proxy statement	Executive comp, board info
4	Insider trading	Stock transactions by insiders
13F	Institutional holdings	What hedge funds own
S-1	IPO registration	Pre-IPO filings
424B	Prospectus	Bond/stock offerings
Error Handling
from edgar import Company

try:
    company = Company("INVALID")
except Exception as e:
    print(f"Company not found: {e}")

# Check if filings exist
filings = company.get_filings(form="10-K")
if len(filings) == 0:
    print("No 10-K filings found")

Performance Tips
Filter before retrieving: Use form type, date filters
Use Entity Facts API for trends: Faster than parsing multiple filings
Batch operations: Process multiple companies in loops
Cache results: Store frequently accessed data
Reference Documentation

For detailed documentation, see:

EdgarTools workflows
Object reference
Form types reference

Or use the built-in docs:

from edgar import Company
company = Company("AAPL")
company.docs.search("how to get revenue")

Weekly Installs
129
Repository
eng0ai/eng0-tem…e-skills
GitHub Stars
4
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn
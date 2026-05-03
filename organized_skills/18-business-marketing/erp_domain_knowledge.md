---
rating: ⭐⭐
title: erp domain knowledge
url: https://skills.sh/danhvb/my-ba-skills/erp-domain-knowledge
---

# erp domain knowledge

skills/danhvb/my-ba-skills/ERP Domain Knowledge
ERP Domain Knowledge
Installation
$ npx skills add https://github.com/danhvb/my-ba-skills --skill 'ERP Domain Knowledge'
SKILL.md
ERP Domain Knowledge Skill
Purpose

Provide comprehensive ERP domain knowledge for analyzing requirements in enterprise resource planning systems across core business functions.

ERP Core Modules
1. Finance & Accounting

General Ledger (GL):

Chart of Accounts (COA) structure
Journal entries and posting
Period close and year-end close
Financial reporting (P&L, Balance Sheet, Cash Flow)
Multi-company and consolidation
Inter-company transactions

Accounts Payable (AP):

Vendor master data
Invoice processing
3-way matching (PO, Receipt, Invoice)
Payment processing (check, EFT, wire)
Vendor aging reports
1099 reporting (US)

Accounts Receivable (AR):

Customer master data
Invoice generation
Credit management
Payment application
Collections management
Customer aging reports

Fixed Assets:

Asset acquisition and capitalization
Depreciation calculation (straight-line, declining balance)
Asset transfers and disposals
Asset reporting

Key Metrics: Days Payable Outstanding (DPO), Days Sales Outstanding (DSO), Cash Conversion Cycle

2. Human Resources (HR)

Core HR:

Employee master data
Organizational structure
Position management
Employee lifecycle (hire, transfer, terminate)
Compliance and reporting

Payroll:

Pay calculation
Tax withholding
Deductions (benefits, garnishments)
Paycheck/direct deposit
Tax reporting (W-2, 1099)

Time & Attendance:

Time entry and tracking
Overtime calculation
Leave management (PTO, sick, FMLA)
Shift scheduling

Benefits Administration:

Benefit plans and enrollment
Open enrollment
Life events processing
COBRA administration

Recruitment:

Job requisitions
Applicant tracking
Interview scheduling
Offer management
Onboarding

Key Metrics: Turnover rate, Time-to-hire, Cost-per-hire, Absence rate

3. Supply Chain Management (SCM)

Procurement:

Purchase requisitions
Request for Quote (RFQ)
Purchase orders
Vendor selection and management
Contract management
Procurement analytics

Inventory Management:

Inventory tracking (lot, serial, location)
Stock counts and adjustments
Inventory valuation (FIFO, LIFO, weighted average)
Min/max and reorder points
ABC analysis
Multi-warehouse management

Warehouse Management:

Receiving and put-away
Picking and packing
Shipping and delivery
Bin/location management
Wave planning

Order Management:

Sales order entry
Order promising (ATP)
Order fulfillment
Backorder management
Returns and credits

Key Metrics: Inventory turnover, Order fill rate, Perfect order rate, Supplier lead time

4. Manufacturing

Bill of Materials (BOM):

Product structure
Component quantities
Phantom assemblies
Engineering change management

Work Orders:

Production scheduling
Work order creation
Shop floor control
Material consumption
Labor tracking
Work order completion

Routing:

Operations sequence
Work centers
Standard times
Setup and run times

Production Planning:

Master Production Schedule (MPS)
Material Requirements Planning (MRP)
Capacity planning
Demand forecasting

Quality Management:

Inspection plans
Quality checks
Non-conformance reporting
Corrective actions

Key Metrics: OEE (Overall Equipment Effectiveness), Cycle time, Yield rate, Scrap rate

5. Project Management

Project Accounting:

Project setup and budgeting
Time and expense tracking
Revenue recognition
Project billing
Work breakdown structure (WBS)

Resource Management:

Resource allocation
Utilization tracking
Skill matching

Key Metrics: Project profitability, Utilization rate, Budget variance

ERP Integration Points
Common Integrations
Banking: Payment files, bank reconciliation
E-commerce: Orders, inventory sync
CRM: Customer data, quotes, orders
EDI: Trading partner transactions
Tax software: Tax calculation, filing
BI/Analytics: Reporting, dashboards
Payroll services: ADP, Paychex
Integration Patterns
Real-time API: Order entry, inventory checks
Batch files: Daily/weekly data sync
EDI/XML: Standard formats (EDIFACT, X12)
iPaaS: Integration platforms (MuleSoft, Boomi)
ERP Business Processes
Procure-to-Pay (P2P)
Requisition → Approval → PO → Receipt → Invoice → 3-Way Match → Payment

Order-to-Cash (O2C)
Sales Order → Credit Check → Fulfillment → Shipping → Invoice → Collection

Record-to-Report (R2R)
Transactions → Journal Entries → Period Close → Reconciliation → Reporting

Hire-to-Retire (H2R)
Requisition → Recruitment → Hire → Onboard → Develop → Retire/Term

Plan-to-Produce
Forecast → MRP → Production Schedule → Work Order → Production → Completion

Multi-Company Considerations
Separate legal entities
Inter-company transactions
Transfer pricing
Consolidation reporting
Chart of accounts mapping
Multi-currency handling
Compliance & Security
Financial Compliance
SOX (Sarbanes-Oxley) - US public companies
GAAP/IFRS accounting standards
Audit trails and documentation
Segregation of duties
Data Security
Role-based access control
Field-level security
Data encryption
Audit logging
Industry Compliance
HIPAA (healthcare)
FDA (pharma, food)
SOC 2 (service organizations)
GDPR (data privacy)
Questions for Stakeholders
Scope
Which modules are in scope?
Multi-company requirements?
Multi-currency requirements?
Integration points?
Processes
What are current pain points?
What processes need redesign?
What approvals are required?
What reports are critical?
Data
Data migration scope?
Data quality issues?
Historical data requirements?
Compliance
Regulatory requirements?
Audit requirements?
Security requirements?
Popular ERP Systems
SAP S/4HANA: Large enterprise, comprehensive
Oracle Cloud ERP: Cloud-native, global
Microsoft Dynamics 365: Mid-market, Microsoft ecosystem
NetSuite: Cloud SMB/mid-market
Odoo: Open-source, modular
Infor: Industry-specific solutions
References
ERP Implementation Best Practices
APICS/ASCM Body of Knowledge
Industry-specific ERP guides
Weekly Installs
–
Repository
danhvb/my-ba-skills
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
---
title: fintech-engineer
url: https://skills.sh/404kidwiz/claude-supercode-skills/fintech-engineer
---

# fintech-engineer

skills/404kidwiz/claude-supercode-skills/fintech-engineer
fintech-engineer
Installation
$ npx skills add https://github.com/404kidwiz/claude-supercode-skills --skill fintech-engineer
SKILL.md
Fintech Engineer
Purpose

Provides expert guidance on building financial technology systems with proper accounting principles, regulatory compliance, and high-precision calculations. Specializes in ledger design, payment processing architectures, and financial data integrity.

When to Use
Designing double-entry ledger systems or accounting databases
Implementing high-precision financial calculations (avoiding floating-point errors)
Building payment processing pipelines
Ensuring PCI-DSS or SOX compliance
Integrating with banking APIs (Plaid, Stripe, etc.)
Handling currency conversions and multi-currency systems
Implementing audit trails for financial transactions
Designing reconciliation systems
Quick Start

Invoke this skill when:

Building ledger or accounting systems
Implementing financial calculations requiring precision
Designing payment processing architectures
Ensuring regulatory compliance (PCI, SOX, PSD2)
Integrating banking or payment APIs

Do NOT invoke when:

General database design without financial context → use /database-administrator
API integration without financial specifics → use /api-designer
Generic security hardening → use /security-engineer
ML-based fraud detection models → use /ml-engineer
Decision Framework
Financial Calculation Needed?
├── Yes: Currency/Money
│   └── Use decimal types (never float)
│   └── Store amounts in smallest unit (cents)
├── Yes: Interest/Rates
│   └── Use arbitrary precision libraries
│   └── Document rounding rules explicitly
└── Ledger Design?
    ├── Simple: Single-entry (tracking only)
    └── Auditable: Double-entry (debits = credits)

Core Workflows
1. Double-Entry Ledger Implementation
Define chart of accounts (assets, liabilities, equity, revenue, expenses)
Create journal entry table with debit/credit columns
Implement balance validation (sum of debits = sum of credits)
Add audit trail with immutable transaction logs
Build reconciliation queries
2. Payment Processing Pipeline
Validate payment request and idempotency key
Create pending transaction record
Call payment processor with retry logic
Handle webhook for async confirmation
Update ledger entries atomically
Generate receipt and audit log
3. Precision Calculation Setup
Choose appropriate numeric type (DECIMAL, NUMERIC, BigDecimal)
Define scale (decimal places) based on currency
Implement rounding rules per jurisdiction
Create calculation helper functions
Add validation for overflow/underflow
Best Practices
Store monetary values as integers in smallest unit (cents, paise)
Use DECIMAL/NUMERIC database types, never FLOAT
Implement idempotency for all financial operations
Maintain immutable audit logs for every transaction
Use database transactions for multi-table updates
Document rounding rules and apply consistently
Anti-Patterns
Anti-Pattern	Problem	Correct Approach
Using floats for money	Precision errors accumulate	Use decimal types or integer cents
Mutable transaction records	Audit trail destroyed	Append-only logs, soft deletes
Missing idempotency	Duplicate charges possible	Idempotency keys on all mutations
Single-entry for auditable systems	Cannot reconcile or audit	Double-entry with balanced journals
Hardcoded tax rates	Compliance failures	Configuration-driven, versioned rules
Weekly Installs
149
Repository
404kidwiz/claud…e-skills
GitHub Stars
76
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
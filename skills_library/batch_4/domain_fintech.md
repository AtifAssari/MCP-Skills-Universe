---
title: domain-fintech
url: https://skills.sh/actionbook/rust-skills/domain-fintech
---

# domain-fintech

skills/actionbook/rust-skills/domain-fintech
domain-fintech
Originally fromzhanghandong/rust-skills
Installation
$ npx skills add https://github.com/actionbook/rust-skills --skill domain-fintech
SKILL.md
FinTech Domain

Layer 3: Domain Constraints

Domain Constraints → Design Implications
Domain Rule	Design Constraint	Rust Implication
Audit trail	Immutable records	Arc, no mutation
Precision	No floating point	rust_decimal
Consistency	Transaction boundaries	Clear ownership
Compliance	Complete logging	Structured tracing
Reproducibility	Deterministic execution	No race conditions
Critical Constraints
Financial Precision
RULE: Never use f64 for money
WHY: Floating point loses precision
RUST: Use rust_decimal::Decimal

Audit Requirements
RULE: All transactions must be immutable and traceable
WHY: Regulatory compliance, dispute resolution
RUST: Arc<T> for sharing, event sourcing pattern

Consistency
RULE: Money can't disappear or appear
WHY: Double-entry accounting principles
RUST: Transaction types with validated totals

Trace Down ↓

From constraints to design (Layer 2):

"Need immutable transaction records"
    ↓ m09-domain: Model as Value Objects
    ↓ m01-ownership: Use Arc for shared immutable data

"Need precise decimal math"
    ↓ m05-type-driven: Newtype for Currency/Amount
    ↓ rust_decimal: Use Decimal type

"Need transaction boundaries"
    ↓ m12-lifecycle: RAII for transaction scope
    ↓ m09-domain: Aggregate boundaries

Key Crates
Purpose	Crate
Decimal math	rust_decimal
Date/time	chrono, time
UUID	uuid
Serialization	serde
Validation	validator
Design Patterns
Pattern	Purpose	Implementation
Currency newtype	Type safety	struct Amount(Decimal);
Transaction	Atomic operations	Event sourcing
Audit log	Traceability	Structured logging with trace IDs
Ledger	Double-entry	Debit/credit balance
Code Pattern: Currency Type
use rust_decimal::Decimal;

#[derive(Clone, Debug, PartialEq)]
pub struct Amount {
    value: Decimal,
    currency: Currency,
}

impl Amount {
    pub fn new(value: Decimal, currency: Currency) -> Self {
        Self { value, currency }
    }

    pub fn add(&self, other: &Amount) -> Result<Amount, CurrencyMismatch> {
        if self.currency != other.currency {
            return Err(CurrencyMismatch);
        }
        Ok(Amount::new(self.value + other.value, self.currency))
    }
}

Common Mistakes
Mistake	Domain Violation	Fix
Using f64	Precision loss	rust_decimal
Mutable transaction	Audit trail broken	Immutable + events
String for amount	No validation	Validated newtype
Silent overflow	Money disappears	Checked arithmetic
Trace to Layer 1
Constraint	Layer 2 Pattern	Layer 1 Implementation
Immutable records	Event sourcing	Arc, Clone
Transaction scope	Aggregate	Owned children
Precision	Value Object	rust_decimal newtype
Thread-safe sharing	Shared immutable	Arc (not Rc)
Related Skills
When	See
Value Object design	m09-domain
Ownership for immutable	m01-ownership
Arc for sharing	m02-resource
Error handling	m13-domain-error
Weekly Installs
371
Repository
actionbook/rust-skills
GitHub Stars
1.1K
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
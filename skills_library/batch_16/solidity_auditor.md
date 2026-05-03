---
title: solidity-auditor
url: https://skills.sh/schwepps/skills/solidity-auditor
---

# solidity-auditor

skills/schwepps/skills/solidity-auditor
solidity-auditor
Installation
$ npx skills add https://github.com/schwepps/skills --skill solidity-auditor
SKILL.md
Solidity Smart Contract Auditor

A professional-grade smart contract audit skill covering security vulnerabilities, gas optimization, storage patterns, and code architecture. Adapted to Solidity version specifics.

Audit Types

Determine the audit type based on user request:

User Request	Audit Type	Primary Reference
"Full audit", "comprehensive review"	Full Audit	All references
"Security audit", "vulnerability scan"	Security Focused	references/security-checklist.md
"Gas optimization", "reduce gas costs"	Gas Optimization	references/gas-optimization.md
"Storage optimization", "storage patterns"	Storage Optimization	references/storage-optimization.md
"Code review", "architecture review"	Architecture Review	references/architecture-review.md
"DeFi audit", "protocol review"	DeFi Protocol	Security + Architecture references
Core Audit Workflow
Phase 1: Preparation

Identify Solidity Version: Check pragma statement. Read references/version-specific.md for version-specific considerations:

Pre-0.8.0: Check for SafeMath usage, arithmetic vulnerabilities
0.8.0+: Review unchecked blocks, check custom errors usage

Understand Scope:

List all contracts, interfaces, libraries
Identify external dependencies (OpenZeppelin, etc.)
Note inheritance hierarchy
Document entry points (external/public functions)

Gather Context: Ask if not provided:

Protocol purpose and intended behavior
Deployment chain(s)
Expected user flows
Admin roles and privileges
Phase 2: Static Analysis

Run automated checks mentally using patterns from the security checklist:

Access control patterns
State-changing operations flow (checks-effects-interactions)
External call patterns
Arithmetic operations (especially in unchecked blocks)

Map attack surface:

External/public functions
Functions handling ETH/tokens
Functions with access control
Upgrade mechanisms
Phase 3: Vulnerability Assessment

Read references/security-checklist.md and evaluate each category:

Critical Priority (check first):

Access Control Vulnerabilities (OWASP SC-01) - $953M+ in losses
Logic Errors (OWASP SC-02) - $64M+ in losses
Reentrancy (OWASP SC-03) - $36M+ in losses

High Priority: 4. Flash Loan Attack Vectors (OWASP SC-04) 5. Input Validation (OWASP SC-05) 6. Oracle Manipulation (OWASP SC-06) 7. Unchecked External Calls (OWASP SC-07)

Medium Priority: 8. Integer Overflow/Underflow (version-dependent) 9. Denial of Service vectors 10. Front-running vulnerabilities

Phase 4: Optimization Analysis (if requested)

For gas optimization: Read references/gas-optimization.md For storage optimization: Read references/storage-optimization.md

Phase 5: Report Generation

Use the template in references/report-template.md to structure findings.

Severity Classification
Severity	Criteria	Action
Critical	Direct fund loss possible, no user interaction needed	Immediate fix required, do not deploy
High	Fund loss possible with specific conditions, significant impact	Must fix before deployment
Medium	Limited impact, unlikely exploitation, or governance issue	Should fix, assess risk
Low	Minor issue, best practice violation	Recommended fix
Informational	Code quality, gas optimization, suggestions	Optional improvement
Quick Reference: Top Attack Vectors (2024-2025)

From OWASP Smart Contract Top 10 (2025) with real losses:

Access Control ($953.2M): Missing/incorrect modifiers, exposed admin functions
Logic Errors ($63.8M): Flawed business logic, incorrect calculations
Reentrancy ($35.7M): State updates after external calls
Flash Loans ($33.8M): Price manipulation, governance attacks
Input Validation ($14.6M): Missing bounds checks, unchecked parameters
Oracle Manipulation ($8.8M): TWAP manipulation, stale prices
Output Guidelines

Always provide:

Clear finding title with severity
Location: Contract name, function, line numbers
Description: What the issue is
Impact: Potential consequences
Proof of Concept: How it could be exploited (when applicable)
Recommendation: Specific fix with code example

Format recommendations as actionable code changes when possible.

Reference Files

Load these as needed based on audit type:

references/security-checklist.md - Complete vulnerability checklist with detection patterns
references/gas-optimization.md - Gas optimization techniques and patterns
references/storage-optimization.md - Storage layout and optimization
references/architecture-review.md - Code architecture best practices
references/version-specific.md - Solidity version considerations
references/report-template.md - Professional audit report template
Weekly Installs
123
Repository
schwepps/skills
GitHub Stars
10
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
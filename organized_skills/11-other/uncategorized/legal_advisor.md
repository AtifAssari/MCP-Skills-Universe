---
rating: ⭐⭐
title: legal-advisor
url: https://skills.sh/404kidwiz/claude-supercode-skills/legal-advisor
---

# legal-advisor

skills/404kidwiz/claude-supercode-skills/legal-advisor
legal-advisor
Installation
$ npx skills add https://github.com/404kidwiz/claude-supercode-skills --skill legal-advisor
SKILL.md
Legal Advisor
Purpose

Provides expert legal guidance on technology law, contracts, compliance, and intellectual property matters. Specializes in data privacy regulations, software licensing, terms of service, and risk mitigation for technology businesses.

When to Use
Reviewing or drafting technology contracts
Ensuring GDPR, CCPA, or data privacy compliance
Evaluating software licensing implications
Drafting or reviewing Terms of Service
Protecting intellectual property (patents, trademarks, copyright)
Assessing regulatory compliance requirements
Understanding open-source licensing obligations
Navigating employment agreements for tech roles
Quick Start

Invoke this skill when:

Reviewing contracts or licensing agreements
Ensuring data privacy compliance
Protecting intellectual property
Drafting Terms of Service or Privacy Policies
Assessing legal risks in technology decisions

Do NOT invoke when:

Security implementation details → use /security-engineer
Compliance automation tooling → use /compliance-auditor
Financial regulatory systems → use /fintech-engineer
HR policy writing → use /internal-comms
Decision Framework
Legal Matter Type?
├── Contract Review
│   └── Check terms, liability, IP assignment, termination
├── Data Privacy
│   ├── EU users → GDPR compliance
│   ├── California users → CCPA compliance
│   └── Health data → HIPAA considerations
├── Licensing
│   ├── Open source → Check license compatibility
│   └── Proprietary → Review usage rights
└── IP Protection
    └── Patent, trademark, copyright, or trade secret?

Core Workflows
1. Contract Review
Identify parties and contract type
Review scope of work and deliverables
Check liability and indemnification clauses
Examine IP ownership and assignment
Review termination and renewal terms
Flag concerning clauses with recommendations
2. Privacy Policy Compliance
Inventory data collection practices
Identify applicable regulations (GDPR, CCPA)
Document data processing purposes
Define data retention policies
Establish user rights procedures
Draft compliant privacy policy
3. Open-Source License Audit
Inventory all open-source dependencies
Identify license type for each (MIT, GPL, Apache)
Check license compatibility with your project
Document attribution requirements
Flag copyleft obligations
Create compliance documentation
Best Practices
Always get legal review for contracts over significant value
Document all data processing activities for compliance
Maintain clear IP assignment in employment contracts
Use license scanning tools for open-source compliance
Keep Terms of Service and Privacy Policy updated
Consider jurisdiction in all legal matters
Anti-Patterns
Anti-Pattern	Problem	Correct Approach
Copying ToS from others	May not fit your business	Draft specific to your practices
Ignoring GDPR for small projects	Fines apply regardless of size	Comply from the start
GPL code in proprietary	License violation	Check compatibility before use
Verbal agreements	Unenforceable	Document in writing
No IP assignment	Unclear ownership	Clear IP clauses in contracts
Weekly Installs
150
Repository
404kidwiz/claud…e-skills
GitHub Stars
76
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
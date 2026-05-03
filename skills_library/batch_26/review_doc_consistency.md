---
title: review-doc-consistency
url: https://skills.sh/heyvhuang/ship-faster/review-doc-consistency
---

# review-doc-consistency

skills/heyvhuang/ship-faster/review-doc-consistency
review-doc-consistency
Installation
$ npx skills add https://github.com/heyvhuang/ship-faster --skill review-doc-consistency
SKILL.md
Documentation Consistency Reviewer
Goal

Systematically identify all "outdated" or "inconsistent with implementation" descriptions in README + docs/, outputting ≥30 issue items.

Core Principles
Code is truth - When documentation conflicts with code, source code/config/contract files are authoritative
Evidence before conclusions - Each issue must cite code/config location as evidence
Contracts first - OpenAPI/proto/schema/TS types are treated as SSOT (Single Source of Truth)
Security default tightening - Security-related inconsistencies are prioritized as high severity
Review Process
1. Document Enumeration
# Scan scope
- README.md (root directory)
- docs/**/*.md (all documentation)
- Contract files: OpenAPI/proto/GraphQL schema/TS types

2. Document-by-Document Review

For each document:

List key claims/commitments/configs/interface items
Search for corresponding implementation in code
Compare differences: missing/renamed/behavior mismatch/default value mismatch
Record issues using template
3. Cross-Check
Reverse check documentation from contract files
Reverse check documentation from config files

See checklist.md for detailed review checklist.

Severity Levels
Level	Definition	Example
P0	Security issue/serious misleading	Docs say sandbox enabled but code doesn't enable it
P1	Core functionality inconsistency	Following docs leads to failure
P2	Incomplete examples/naming inconsistency	Doesn't directly block usage
P3	Wording/formatting/link minor issues	Doesn't affect functionality
Pending Evidence	Suspicious but insufficient evidence	Needs further investigation
Output Format

See output-format.md for detailed templates.

Single Issue Item
### [Title]
- **Severity**: P0/P1/P2/P3/Pending Evidence
- **Location**: `<file_path>:<line_number>`
- **Evidence**:
  - Documentation: [quote]
  - Code: [quote]
- **Impact**: [Misleading consequences]
- **Suggestion**: [Minimal fix]
- **Related Principle**: Code is truth/Contracts first/Security default tightening/...

Review Conclusion
## Review Conclusion
- **Verdict**: Pass/Conditional Pass/Fail
- **Summary**: P0:x P1:x P2:x P3:x Pending:x
- **Fix Priority**: P0 → P1 → P2 → P3

Multi-Agent Parallel

For acceleration, split by following dimensions for parallel multi-agent execution:

By document type - One agent each for README, API docs, development guide
By module - One agent per functional module's documentation
By check direction - One checks docs against code, another checks code against docs

Deduplication and unified severity rating needed when aggregating.

Execution

After review completion, output doc-consistency.md report file, and also output doc-consistency.json (structured issue list for aggregation/deduplication/statistics).

Weekly Installs
53
Repository
heyvhuang/ship-faster
GitHub Stars
338
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass
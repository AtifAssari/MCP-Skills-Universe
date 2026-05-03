---
rating: ⭐⭐⭐
title: contract-review
url: https://skills.sh/zh-xx/legal-assistant-skills/contract-review
---

# contract-review

skills/zh-xx/legal-assistant-skills/contract-review
contract-review
Installation
$ npx skills add https://github.com/zh-xx/legal-assistant-skills --skill contract-review
SKILL.md
Contract Review Skill
Overview

This skill performs contract reviews by adding comments only (no edits to the original text). It follows a four-layer review (entity verification, basic, business, legal) and generates:

Annotated contract (.docx)
Contract summary (.docx)
Consolidated review opinion (.docx)
Business flowchart (Mermaid + rendered image)

Language rule: detect the contract’s dominant language and output all generated content (comments, summary, opinion, flowchart text) in that language. Use the guidance in references/language.md.

Workflow
Unpack the contract (.docx) for XML operations
Read contract text (pandoc or XML)
Extract and verify contracting parties (Layer 0)
Execute three-layer clause review (Layer 1–3)
Add comments to the document
Generate contract summary
Generate consolidated opinion
Generate business flowchart and render image
Repack to .docx
Output Naming
Output directory: 审核结果：{ContractName} for Chinese or Review_Result_{ContractName} for English
Reviewed contract: {ContractName}_审核版.docx for Chinese or {ContractName}_Reviewed.docx for English
Review report: 审核报告.txt for Chinese or Review_Report.txt for English
Comment Principles
Comments only: do not modify the original text or formatting
Precise anchoring: comment should target specific clauses/paragraphs
Structured content: each comment includes issue type, risk reason, and revision suggestion
Risk level: carried by reviewer name; do not include a “risk level” line in comment body
Output language: use labels in the contract’s language (see references/language.md)

Comment example (English):

[Issue Type] Payment Terms
[Risk Reason] The total amount is stated as USD 100,000 in Section 3.2, but the payment clause lists USD 1,000,000 in Section 5.1. This inconsistency may cause disputes.
[Revision Suggestion] Align the total amount across clauses and clarify whether tax is included.

Review Standards

Use the four-layer review model and the detailed checklist in references/checklist.md.

Layer 0: Entity verification (subject authenticity)
Extract all contracting parties (full legal names, credit codes, legal representatives)
Verify each entity's registered name accuracy and business registration status
Verification tool priority:
If an MCP tool for business registration lookup is available in the current environment (e.g., enterprise info query, company lookup, 企业查询, 工商查询), use it to query each party's name or Unified Social Credit Code.
If no such MCP tool is available, use Web Search to look up "[entity name] 工商登记信息" or "[entity name] business registration".
Record the verification source (MCP tool name / Web Search) in the comment.
Layer 1: Basic (text quality)
Accuracy of numbers, dates, terms
Consistent numbering and references
Clarity and lack of ambiguity
Formatting and punctuation quality
Layer 2: Business terms
Scope, deliverables, quantity/specs
Pricing and payment schedule
Delivery/acceptance procedures
Rights/obligations and performance guarantees
Layer 3: Legal terms
Effectiveness and term/termination
Liability/penalties and remedies
Dispute resolution and governing law
Confidentiality, force majeure, IP, notice, authorization

Risk levels (encoded in reviewer name):

🔴 High: core business ambiguity (price, scope, rights/obligations)
🟡 Medium: material but non-core ambiguity
🔵 Low: minimal practical impact
Contract Summary

Generate a structured, objective summary in the contract’s language.

See references/summary.md (English template)
Use references/language.md for language selection and Chinese labels

Output file: 合同概要.docx for Chinese or Contract_Summary.docx for English (default font: 仿宋; adjust if language requires)

Consolidated Opinion

Generate a concise, two-paragraph response for the business team in the contract’s language.

See references/opinion.md

Output file: 综合审核意见.docx for Chinese or Consolidated_Opinion.docx for English (default font: 仿宋; adjust if language requires)

Business Flowchart (Mermaid)

Generate Mermaid flowchart per requirements and render to image.

See references/flowchart.md

Outputs:

business_flowchart.mmd
business_flowchart.png

li## Technical Notes

Core workflow:

Unpack → 2. Entity verification → 3. Add comments → 4. Summary → 5. Opinion → 6. Flowchart → 7. Repack

API & implementation details:

references/technical.md
Dependencies
Python 3.9+ (3.10+ recommended)
pandoc (system install)
defusedxml
Mermaid CLI (mmdc) for rendering
python-docx for rich text output
Troubleshooting (Short)
Comments missing in Word: run doc.verify_comments() and re-save
find_paragraph fails: shorten search text; confirm actual paragraph text
Mermaid render fails: ensure mmdc installed; use Chrome path or Puppeteer config
Examples

See references/examples.md for a full workflow example.

Important Rules
Never alter original contract text
Entity verification (Layer 0) must complete before clause review (Layers 1–3)
Review all four layers, do not skip items
Ensure risk level is accurate and consistent
Keep comments precise, professional, and actionable
Flowchart must come strictly from the contract text
Summary is objective only; no risk analysis
Opinion only reflects findings already identified
License

SPDX-License-Identifier: Apache-2.0

Copyright (c) 2026 JiCheng

Licensed under the Apache License, Version 2.0. See repository root LICENSE.

Weekly Installs
59
Repository
zh-xx/legal-ass…t-skills
GitHub Stars
103
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
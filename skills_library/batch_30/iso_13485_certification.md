---
title: iso-13485-certification
url: https://skills.sh/k-dense-ai/scientific-agent-skills/iso-13485-certification
---

# iso-13485-certification

skills/k-dense-ai/scientific-agent-skills/iso-13485-certification
iso-13485-certification
Installation
$ npx skills add https://github.com/k-dense-ai/scientific-agent-skills --skill iso-13485-certification
SKILL.md
ISO 13485 Certification Documentation Assistant
Overview

This skill helps medical device manufacturers prepare comprehensive documentation for ISO 13485:2016 certification. It provides tools, templates, references, and guidance to create, review, and gap-analyze all required Quality Management System (QMS) documentation.

What this skill provides:

Gap analysis of existing documentation
Templates for all mandatory documents
Comprehensive requirements guidance
Step-by-step documentation creation
Identification of missing documentation
Compliance checklists

When to use this skill:

Starting ISO 13485 certification process
Conducting gap analysis against ISO 13485
Creating or updating QMS documentation
Preparing for certification audit
Transitioning from FDA QSR to QMSR
Harmonizing with EU MDR requirements
Core Workflow
1. Assess Current State (Gap Analysis)

When to start here: User has existing documentation and needs to identify gaps

Process:

Collect existing documentation:

Ask user to provide directory of current QMS documents
Documents can be in any format (.txt, .md, .doc, .docx, .pdf)
Include any procedures, manuals, work instructions, forms

Run gap analysis script:

python scripts/gap_analyzer.py --docs-dir <path_to_docs> --output gap-report.json


Review results:

Identify which of the 31 required procedures are present
Identify missing key documents (Quality Manual, MDF, etc.)
Calculate compliance percentage
Prioritize missing documentation

Present findings to user:

Summarize what exists
Clearly list what's missing
Provide prioritized action plan
Estimate effort required

Output: Comprehensive gap analysis report with prioritized action items

2. Understand Requirements (Reference Consultation)

When to use: User needs to understand specific ISO 13485 requirements

Available references:

references/iso-13485-requirements.md - Complete clause-by-clause breakdown
references/mandatory-documents.md - All 31 required procedures explained
references/gap-analysis-checklist.md - Detailed compliance checklist
references/quality-manual-guide.md - How to create Quality Manual

How to use:

For specific clause questions:

Read relevant section from iso-13485-requirements.md
Explain requirements in plain language
Provide practical examples

For document requirements:

Consult mandatory-documents.md
Explain what must be documented
Clarify when documents are applicable vs. excludable

For implementation guidance:

Use quality-manual-guide.md for policy-level documents
Provide step-by-step creation process
Show examples of good vs. poor implementation

Key reference sections to know:

Clause 4: QMS requirements, documentation, risk management, software validation
Clause 5: Management responsibility, quality policy, objectives, management review
Clause 6: Resources, competence, training, infrastructure
Clause 7: Product realization, design, purchasing, production, traceability
Clause 8: Measurement, audits, CAPA, complaints, data analysis
3. Create Documentation (Template-Based Generation)

When to use: User needs to create specific QMS documents

Available templates:

Quality Manual: assets/templates/quality-manual-template.md
CAPA Procedure: assets/templates/procedures/CAPA-procedure-template.md
Document Control: assets/templates/procedures/document-control-procedure-template.md

Process for document creation:

Identify what needs to be created:

Based on gap analysis or user request
Prioritize critical documents first (Quality Manual, CAPA, Complaints, Audits)

Select appropriate template:

Use Quality Manual template for QM
Use procedure templates as examples for SOPs
Adapt structure to organization's needs

Customize template with user-specific information:

Replace all placeholder text: [COMPANY NAME], [DATE], [NAME], etc.
Tailor scope to user's actual operations
Add or remove sections based on applicability
Ensure consistency with organization's processes

Key customization areas:

Company information and addresses
Product types and classifications
Applicable regulatory requirements
Organization structure and responsibilities
Actual processes and procedures
Document numbering schemes
Exclusions and justifications

Validate completeness:

All required sections present
All placeholders replaced
Cross-references correct
Approval sections complete

Document creation priority order:

Phase 1 - Foundation (Critical):

Quality Manual
Quality Policy and Objectives
Document Control procedure
Record Control procedure

Phase 2 - Core Processes (High Priority): 5. Corrective and Preventive Action (CAPA) 6. Complaint Handling 7. Internal Audit 8. Management Review 9. Risk Management

Phase 3 - Product Realization (High Priority): 10. Design and Development (if applicable) 11. Purchasing 12. Production and Service Provision 13. Control of Nonconforming Product

Phase 4 - Supporting Processes (Medium Priority): 14. Training and Competence 15. Calibration/Control of M&M Equipment 16. Process Validation 17. Product Identification and Traceability

Phase 5 - Additional Requirements (Medium Priority): 18. Feedback and Post-Market Surveillance 19. Regulatory Reporting 20. Customer Communication 21. Data Analysis

Phase 6 - Specialized (If Applicable): 22. Installation (if applicable) 23. Servicing (if applicable) 24. Sterilization (if applicable) 25. Contamination Control (if applicable)

4. Develop Specific Documents
Creating a Quality Manual

Process:

Read the comprehensive guide:

Read references/quality-manual-guide.md in full
Understand structure and required content
Review examples provided

Gather organization information:

Legal company name and addresses
Product types and classifications
Organizational structure
Applicable regulations
Scope of operations
Any exclusions needed

Use template:

Start with assets/templates/quality-manual-template.md
Follow structure exactly (required by ISO 13485)
Replace all placeholders

Complete required sections:

Section 0: Document control, approvals
Section 1: Introduction, company overview
Section 2: Scope and exclusions (critical - must justify exclusions)
Section 3: Quality Policy (must be signed by top management)
Sections 4-8: Address each ISO 13485 clause at policy level
Appendices: Procedure list, org chart, process map, definitions

Key requirements:

Must reference all 31 documented procedures (Appendix A)
Must describe process interactions (Appendix C - create process map)
Must define documentation structure (Section 4.2)
Must justify any exclusions (Section 2.4)

Validation checklist:

 All required content per ISO 13485 Clause 4.2.2
 Quality Policy signed by top management
 All exclusions justified
 All procedures listed in Appendix A
 Process map included
 Organization chart included
Creating Procedures (SOPs)

General approach for all procedures:

Understand the requirement:

Read relevant clause in references/iso-13485-requirements.md
Understand WHAT must be documented
Identify WHO, WHEN, WHERE for your organization

Use template structure:

Follow CAPA or Document Control templates as examples
Standard sections: Purpose, Scope, Definitions, Responsibilities, Procedure, Records, References
Keep procedures clear and actionable

Define responsibilities clearly:

Identify specific roles (not names)
Define responsibilities for each role
Ensure coverage of all required activities

Document the "what" not excessive "how":

Procedures should define WHAT must be done
Detailed HOW-TO goes in Work Instructions (Tier 3)
Strike balance between guidance and flexibility

Include required elements:

All elements specified in ISO 13485 clause
Records that must be maintained
Responsibilities for each activity
References to related documents

Example: Creating CAPA Procedure

Read ISO 13485 Clauses 8.5.2 and 8.5.3 from references
Use assets/templates/procedures/CAPA-procedure-template.md
Customize:
CAPA prioritization criteria for your organization
Root cause analysis methods you'll use
Approval authorities and responsibilities
Timeframes based on your operations
Integration with complaint handling, audits, etc.
Add forms as attachments:
CAPA Request Form
Root Cause Analysis Worksheet
Action Plan Template
Effectiveness Verification Checklist
Creating Medical Device Files (MDF)

What is an MDF:

File for each medical device type or family
Replaces separate DHF, DMR, DHR (per FDA QMSR harmonization)
Contains all documentation about the device

Required contents per ISO 13485 Clause 4.2.3:

General description and intended use
Label and instructions for use specifications
Product specifications
Manufacturing specifications
Procedures for purchasing, manufacturing, servicing
Procedures for measuring and monitoring
Installation requirements (if applicable)
Risk management file(s)
Verification and validation information
Design and development file(s) (when applicable)

Process:

Identify each device type or family
Create MDF structure (folder or binder)
Collect or create each required element
Ensure traceability between documents
Maintain as living document (update with changes)
5. Conduct Comprehensive Gap Analysis

When to use: User wants detailed assessment of all requirements

Process:

Use comprehensive checklist:

Open references/gap-analysis-checklist.md
Work through clause by clause
Mark status for each requirement: Compliant, Partial, Non-compliant, N/A

For each clause:

Read requirement description
Identify existing evidence
Note gaps or deficiencies
Define action required
Assign responsibility and target date

Summarize by clause:

Calculate compliance percentage per clause
Identify highest-risk gaps
Prioritize actions

Create action plan:

List all gaps
Prioritize: Critical > High > Medium > Low
Assign owners and dates
Estimate resources needed

Output:

Completed gap analysis checklist
Summary report with compliance percentages
Prioritized action plan
Timeline and milestones
Common Scenarios
Scenario 1: Starting from Scratch

User request: "We're a medical device startup and need to implement ISO 13485. Where do we start?"

Approach:

Explain the journey:

ISO 13485 requires comprehensive QMS documentation
Typically 6-12 months for full implementation
Can be done incrementally

Start with foundation:

Quality Policy and Objectives
Quality Manual
Organization structure and responsibilities

Follow the priority order:

Use Phase 1-6 priority list above
Create documents in logical sequence
Build on previously created documents

Key milestones:

Month 1-2: Foundation documents (Quality Manual, policies)
Month 3-4: Core processes (CAPA, Complaints, Audits)
Month 5-6: Product realization processes
Month 7-8: Supporting processes
Month 9-10: Internal audits and refinement
Month 11-12: Management review and certification audit
Scenario 2: Gap Analysis for Existing QMS

User request: "We have some procedures but don't know what we're missing for ISO 13485."

Approach:

Run automated gap analysis:

Ask for document directory
Run scripts/gap_analyzer.py
Review automated findings

Conduct detailed assessment:

Use comprehensive checklist for user's specific situation
Go deeper than automated analysis
Assess quality of existing documents, not just presence

Provide prioritized gap list:

Missing mandatory procedures
Incomplete procedures
Quality issues with existing documents
Missing records or forms

Create remediation plan:

High priority: Safety-related, regulatory-required
Medium priority: Core QMS processes
Low priority: Improvement opportunities
Scenario 3: Creating Specific Document

User request: "Help me create a CAPA procedure."

Approach:

Explain requirements:

Read ISO 13485 Clauses 8.5.2 and 8.5.3 from references
Explain what must be in CAPA procedure
Provide examples of good CAPA processes

Use template:

Start with CAPA procedure template
Explain each section's purpose
Show what needs customization

Gather user-specific info:

How are CAPAs initiated in their organization?
Who are the responsible parties?
What prioritization criteria make sense?
What RCA methods will they use?
What are appropriate timeframes?

Create customized procedure:

Replace all placeholders
Adapt to user's processes
Ensure completeness

Add supporting materials:

CAPA request form
RCA worksheets
Action plan template
Effectiveness verification checklist
Scenario 4: Updating for Regulatory Changes

User request: "We need to update our QMS for FDA QMSR harmonization."

Approach:

Explain changes:

FDA 21 CFR Part 820 harmonized with ISO 13485
Now called QMSR (effective Feb 2, 2026)
Key change: Medical Device File replaces DHF/DMR/DHR

Review current documentation:

Identify documents referencing QSR
Find separate DHF, DMR, DHR structures
Check for ISO 13485 compliance gaps

Update strategy:

Update references from QSR to QMSR
Consolidate DHF/DMR/DHR into Medical Device Files
Add any missing ISO 13485 requirements
Maintain backward compatibility during transition

Create transition plan:

Update Quality Manual
Update MDF procedure
Reorganize device history files
Train personnel on changes
Scenario 5: Preparing for Certification Audit

User request: "We have our documentation ready. How do we prepare for the certification audit?"

Approach:

Conduct readiness assessment:

Use comprehensive gap analysis checklist
Review all documentation for completeness
Verify records exist for all required items
Check for consistent implementation

Pre-audit checklist:

 All 31 procedures documented and approved
 Quality Manual complete with all required content
 Medical Device Files complete for all products
 Internal audit completed with findings addressed
 Management review completed
 Personnel trained on QMS procedures
 Records maintained per retention requirements
 CAPA system functional with effectiveness demonstrated
 Complaints system operational

Conduct mock audit:

Use ISO 13485 requirements as audit criteria
Sample records to verify consistent implementation
Interview personnel to verify understanding
Identify any non-conformances

Address findings:

Correct any deficiencies
Document corrections
Verify effectiveness

Final preparation:

Brief management and staff
Prepare audit schedule
Organize evidence and records
Designate escorts and support personnel
Best Practices
Document Development

Start at policy level, then add detail:

Quality Manual = policy level
Procedures = what, who, when
Work Instructions = detailed how-to
Forms = data collection

Maintain consistency:

Use same terminology throughout
Cross-reference related documents
Keep numbering scheme consistent
Update all related documents together

Write for your audience:

Clear, simple language
Avoid jargon
Define technical terms
Provide examples where helpful

Make procedures usable:

Action-oriented language
Logical flow
Clear responsibilities
Realistic timeframes
Exclusions

When you can exclude:

Design and development (if contract manufacturer only)
Installation (if product requires no installation)
Servicing (if not offered)
Sterilization (if non-sterile product)

Justification requirements:

Must be in Quality Manual
Must explain why excluded
Cannot exclude if process performed
Cannot affect ability to provide safe, effective devices

Example good justification:

"Clause 7.3 Design and Development is excluded. ABC Company operates as a contract manufacturer and produces medical devices according to complete design specifications provided by customers. All design activities are performed by the customer and ABC Company has no responsibility for design inputs, outputs, verification, validation, or design changes."

Example poor justification:

"We don't do design." (Too brief, doesn't explain why or demonstrate no impact)

Common Mistakes to Avoid

Copying ISO 13485 text verbatim

Write in your own words
Describe YOUR processes
Make it actionable for your organization

Making procedures too detailed

Procedures should be stable
Excessive detail belongs in work instructions
Balance guidance with flexibility

Creating documents in isolation

Ensure consistency across QMS
Cross-reference related documents
Build on previously created documents

Forgetting records

Every procedure should specify records
Define retention requirements
Ensure records actually maintained

Inadequate approval

Quality Manual must be signed by top management
All procedures must be properly approved
Train staff before documents become effective
Resources
scripts/
gap_analyzer.py - Automated tool to analyze existing documentation and identify gaps against ISO 13485 requirements
references/
iso-13485-requirements.md - Complete breakdown of ISO 13485:2016 requirements clause by clause
mandatory-documents.md - Detailed list of all 31 required procedures plus other mandatory documents
gap-analysis-checklist.md - Comprehensive checklist for detailed gap assessment
quality-manual-guide.md - Step-by-step guide for creating a compliant Quality Manual
assets/templates/
quality-manual-template.md - Complete template for Quality Manual with all required sections
procedures/CAPA-procedure-template.md - Example CAPA procedure following best practices
procedures/document-control-procedure-template.md - Example document control procedure
Quick Reference
The 31 Required Documented Procedures
Risk Management (4.1.5)
Software Validation (4.1.6)
Control of Documents (4.2.4)
Control of Records (4.2.5)
Internal Communication (5.5.3)
Management Review (5.6.1)
Human Resources/Competence (6.2)
Infrastructure Maintenance (6.3) - when applicable
Contamination Control (6.4.2) - when applicable
Customer Communication (7.2.3)
Design and Development (7.3.1-10) - when applicable
Purchasing (7.4.1)
Verification of Purchased Product (7.4.3)
Production Control (7.5.1)
Product Cleanliness (7.5.2) - when applicable
Installation (7.5.3) - when applicable
Servicing (7.5.4) - when applicable
Process Validation (7.5.6) - when applicable
Sterilization Validation (7.5.7) - when applicable
Product Identification (7.5.8)
Traceability (7.5.9)
Customer Property (7.5.10) - when applicable
Preservation of Product (7.5.11)
Control of M&M Equipment (7.6)
Feedback (8.2.1)
Complaint Handling (8.2.2)
Regulatory Reporting (8.2.3)
Internal Audit (8.2.4)
Process Monitoring (8.2.5)
Product Monitoring (8.2.6)
Control of Nonconforming Product (8.3)
Corrective Action (8.5.2)
Preventive Action (8.5.3)

(Note: Traditional count is "31 procedures" though list shows more because some are conditional)

Key Regulatory Requirements

FDA (United States):

21 CFR Part 820 (now QMSR) - harmonized with ISO 13485 as of Feb 2026
Device classification determines requirements
Establishment registration and device listing required

EU (European Union):

MDR 2017/745 (Medical Devices Regulation)
IVDR 2017/746 (In Vitro Diagnostic Regulation)
Technical documentation requirements
CE marking requirements

Canada:

Canadian Medical Devices Regulations (SOR/98-282)
Device classification system
Medical Device Establishment License (MDEL)

Other Regions:

Australia TGA, Japan PMDA, China NMPA, etc.
Often require or recognize ISO 13485 certification
Document Retention

Minimum retention: Lifetime of medical device as defined by organization

Typical retention periods:

Design documents: Life of device + 5-10 years
Manufacturing records: Life of device
Complaint records: Life of device + 5-10 years
CAPA records: 5-10 years minimum
Calibration records: Retention period of equipment + 1 calibration cycle

Always comply with applicable regulatory requirements which may specify longer periods.

Getting Started

First-time users should:

Read references/iso-13485-requirements.md to understand the standard
If you have existing documentation, run gap analysis script
Create Quality Manual using template and guide
Develop procedures in priority order
Use comprehensive checklist for final validation

For specific tasks:

Creating Quality Manual → See Section 4 and use quality-manual-guide.md
Creating CAPA procedure → See Section 4 and use CAPA template
Gap analysis → See Section 1 and 5
Understanding requirements → See Section 2

Need help? Start by describing your situation: what stage you're at, what you have, and what you need to create.

Weekly Installs
140
Repository
k-dense-ai/scie…t-skills
GitHub Stars
19.9K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
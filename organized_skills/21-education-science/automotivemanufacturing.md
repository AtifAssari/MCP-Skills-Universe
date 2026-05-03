---
rating: ⭐⭐⭐
title: automotivemanufacturing
url: https://skills.sh/robdtaylor/personal-ai-infrastructure/automotivemanufacturing
---

# automotivemanufacturing

skills/robdtaylor/personal-ai-infrastructure/Automotivemanufacturing
Automotivemanufacturing
Installation
$ npx skills add https://github.com/robdtaylor/personal-ai-infrastructure --skill Automotivemanufacturing
SKILL.md
Automotive Manufacturing Documentation
When to Activate This Skill
"Write a work instruction for [process]"
"Create a business process for [operation]"
"Document manufacturing procedure"
"Build SOP for [automotive process]"
"Create APQP documentation"
"Write quality inspection procedure"
"Document assembly/machining/material handling process"
Core Document Types
1. Work Instructions (WI)

Purpose: Detailed step-by-step operator guidance Key Elements:

Clear title and document ID
Scope and applicability
Required materials, tools, equipment
Safety warnings and PPE requirements
Numbered sequential steps with visual aids
Quality checkpoints and acceptance criteria
References to specifications/standards
2. Standard Operating Procedures (SOP)

Purpose: Standardized process methodology Key Elements:

Purpose and scope
Responsibilities and authorities
Process flowchart
Detailed procedure steps
Forms and records
Related documents
Revision history
3. Business Process Documents

Purpose: High-level process definition and control Key Elements:

Process ownership
Inputs and outputs
Key performance indicators (KPIs)
Process flow diagram
Interaction with other processes
Risks and controls
Continuous improvement tracking
Standards Compliance
IATF 16949 Requirements
Process approach methodology
Risk-based thinking
Turtle diagrams for process definition
FMEA linkage
Control plan alignment
Layered process audits consideration
ISO 9001 Structure
Context of organization
Leadership and planning
Support and operation
Performance evaluation
Improvement focus
APQP/PPAP Integration
Process flow diagrams
PFMEA considerations
Control plans
Work instructions as PPAP deliverables
Measurement system analysis references
Writing Framework
Document Structure Template
1. HEADER
   - Document Title
   - Document Number
   - Revision/Date
   - Approvals (Prepared/Reviewed/Approved)

2. PURPOSE & SCOPE
   - Why this document exists
   - What processes/operations it covers
   - What it doesn't cover

3. RESPONSIBILITIES
   - Who performs the work
   - Who supervises
   - Who approves/validates

4. SAFETY & PPE
   - Hazards and risks
   - Required personal protective equipment
   - Emergency procedures

5. MATERIALS & EQUIPMENT
   - Parts/components list
   - Tools required
   - Equipment specifications
   - Gages and measuring devices

6. PROCEDURE/STEPS
   - Sequential numbered steps
   - Action-oriented language (verb-first)
   - Visual aids (photos, diagrams)
   - Quality checks embedded

7. QUALITY REQUIREMENTS
   - Specifications and tolerances
   - Inspection frequency
   - Acceptance/rejection criteria
   - Rework procedures

8. RECORDS & DOCUMENTATION
   - What gets recorded
   - Where records stored
   - Retention requirements

9. REFERENCES
   - Related documents
   - Engineering drawings
   - Specifications
   - Standards

10. REVISION HISTORY
    - Date, revision, changes made

Process Type Guidelines
Assembly Operations
Focus: Sequence, torque specs, orientation
Include: Part numbers, installation direction, fastener specifications
Visuals: Assembly diagrams, before/after photos, exploded views
Checks: Fit, alignment, function tests
Machining Operations
Focus: Setup, program, tooling, parameters
Include: Machine settings, feed/speed, tool specifications, fixtures
Visuals: Setup photos, tool paths, measurement points
Checks: Dimensional verification, surface finish, first-piece inspection
Quality/Inspection
Focus: What to inspect, how to measure, accept/reject criteria
Include: Gage R&R references, sampling plans, measurement methods
Visuals: Measurement locations, gage usage, defect examples
Checks: Calibration verification, data recording
Material Handling
Focus: Movement, storage, protection, traceability
Include: Handling methods, storage conditions, labeling, FIFO
Visuals: Packaging methods, storage layouts, label formats
Checks: Condition verification, count accuracy, traceability
Best Practices
Writing Style
Active voice: "Insert the bolt" not "The bolt is inserted"
Present tense: "Check the torque" not "The torque should be checked"
Imperative mood: Direct commands to operator
Concise: One action per step
Specific: Exact values, not ranges when possible
Visual Elements
Photos of actual parts/processes (preferred)
Diagrams for complex assemblies
Flowcharts for decision points
Callouts for critical features
Color coding for emphasis (warnings in red/yellow)
Quality Integration
Embed quality checks within process steps
Reference control plans
Link to FMEA high-priority items
Include mistake-proofing (poka-yoke) features
Document inspection frequency
Revision Control
Clear document numbering system
Revision history table
Change bars for modified sections
Effective date tracking
Training requirements for changes
Common Mistakes to Avoid
Assuming operator knowledge
Missing safety information
Vague quantities or specifications
No visual aids for complex operations
Incomplete tool/equipment lists
Missing quality acceptance criteria
No revision history
Passive voice or unclear instructions
Quick Reference: Document Selection
Need	Document Type	Complexity
Operator guidance	Work Instruction	Low-Medium
Department procedure	SOP	Medium
Process definition	Business Process	Medium-High
Quality procedure	Quality SOP	Medium
Inspection method	Inspection WI	Low-Medium
Output Format

When creating documents, structure output as:

# [DOCUMENT TITLE]
**Document Number**: [AUTO-XXX-####]
**Revision**: [X] | **Date**: [YYYY-MM-DD]
**Prepared**: _____ | **Reviewed**: _____ | **Approved**: _____

## 1. Purpose & Scope
[Content]

## 2. Responsibilities
[Content]

[Continue with standard sections...]

Supplementary Resources

For comprehensive methodologies and advanced topics: read ~/.claude/skills/AutomotiveManufacturing/CLAUDE.md

For document templates: ls ~/.claude/skills/AutomotiveManufacturing/templates/

Integration with Related Skills
A3CriticalThinking

When manufacturing issues arise, use A3 problem-solving methodology:

Quality defects → Root cause analysis (5 Whys, Fishbone)
Process failures → Structured countermeasure development
Decision making → Apply priority hierarchy (Safety → Customer → Cost)

Load A3 skill: read ~/.claude/skills/A3CriticalThinking/SKILL.md

SupplyChain

For supplier-related documentation and requirements:

Supplier quality requirements in work instructions
PPAP documentation for purchased components
Incoming inspection procedures

Load SupplyChain skill: read ~/.claude/skills/SupplyChain/SKILL.md

HoshinKanri

For strategic alignment of manufacturing objectives:

Cascade targets to shop floor metrics
Link work instructions to quality objectives
Bowling chart for manufacturing KPIs

Load HoshinKanri skill: read ~/.claude/skills/HoshinKanri/SKILL.md

Key Principles

Priority Hierarchy (from A3CriticalThinking):

1. SAFETY FIRST     → Never compromise for cost or delivery
2. CUSTOMER VALUE   → Quality that meets/exceeds requirements
3. SHAREHOLDER VALUE → Optimize after 1 & 2 are secured

Safety First: Always lead with safety considerations - this is non-negotiable
Clarity Over Brevity: Be clear, even if it takes more words
Visual Communication: A picture is worth 1000 words
Measurable Requirements: Specific, measurable acceptance criteria
Traceability: Link to higher-level documents and standards
Living Documents: Build in revision and improvement processes
Problem Solving: Use A3 methodology for issues and improvements
Workflow Routing
Request Type	Workflow	Output
"Write work instruction for [process]"	Work Instruction template	Numbered WI document with all 10 sections
"Create SOP for [department/process]"	SOP template	Standard procedure with flowchart
"APQP documentation"	APQP/PPAP integration	Phase-aligned docs: process flow, PFMEA linkage, control plan, WI
"IATF 16949 clause mapping"	Standards compliance	Turtle diagram + clause-by-clause alignment table
"Business process document"	Business Process template	High-level process with KPIs and risk table
"Inspection/quality procedure"	Quality SOP template	Inspection WI with gage specs and sampling plan
Complex quality issue	→ A3CriticalThinking	Load A3 skill for root cause + countermeasure
Supplier requirements	→ SupplyChain	Load SupplyChain skill for PPAP/SQE docs
Examples
Example 1: APQP Work Instruction Draft

Input: "Draft a work instruction for the damper assembly final inspection station as an APQP deliverable."

Output structure:

WI-QUA-DAMP-001 | Rev A | APQP Phase 4 | PPAP Element 11

Purpose: 100% end-of-line inspection for DSS damper assemblies before shipment.

Safety: Safety glasses mandatory. WARNING: Damper contains pressurised gas — do not disassemble.

Steps:
1. Retrieve damper from assembly conveyor
2. Visual: inspect for scoring, leaks, damage — reject on any defect
3. Rod extension length: 245mm +/-1mm (gauge G-044) — record on TL-DAMP-001
4. Leak test: submerge 30s in water bath — zero bubbles (CRITICAL: PFMEA #7, RPN 160)
5. Scan serial number into MES for traceability
6. Place approved part in shipping rack DS-007


IATF 16949 linkage: clause 8.5.1 (control of production), 8.6 (release), PPAP Element 11.

Example 2: IATF 16949 Clause Mapping for CNC Machining

Input: "Map our CNC turning operation to IATF 16949 — what do we need to document?"

IATF 16949 Clause	Requirement	Required Document
7.1.3	Infrastructure	Equipment list, PM schedule
7.1.5	Measurement resources	Calibration register, MSA records
7.2	Competence	Operator skills matrix, training records
8.1	Operational planning	Process FMEA, control plan
8.5.1	Control of production	Work instruction WI-MCH-TURN-001, setup sheet
8.5.2	Identification & traceability	Part labels, traveller, lot records
8.6	Release of products	First-off/last-off inspection record
9.1.1	Monitoring & measurement	SPC charts on critical dims (Cpk >= 1.67)
10.2	Nonconformity & corrective action	NCR process, 8D for customer complaints

Turtle Diagram (CNC Turning):

Inputs: Raw bar stock (cert req'd), drawing rev B, CNC program P-4567
Outputs: Turned component to drawing tolerances, first-off inspection record
With What: CNC lathe, tooling per setup sheet, CMM for FAI
How: Work instruction, SPC control plan
Who: Level 2 machinist min; QE sign-off for new setups
Metrics: Cpk >= 1.67 on critical dims, scrap <= 0.5%, OEE >= 80%
Weekly Installs
47
Repository
robdtaylor/pers…tructure
GitHub Stars
1
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
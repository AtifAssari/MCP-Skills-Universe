---
title: mdr-745-specialist
url: https://skills.sh/alirezarezvani/claude-skills/mdr-745-specialist
---

# mdr-745-specialist

skills/alirezarezvani/claude-skills/mdr-745-specialist
mdr-745-specialist
Installation
$ npx skills add https://github.com/alirezarezvani/claude-skills --skill mdr-745-specialist
SKILL.md
MDR 2017/745 Specialist

EU MDR compliance patterns for medical device classification, technical documentation, and clinical evidence.

Table of Contents
Device Classification Workflow
Technical Documentation
Clinical Evidence
Post-Market Surveillance
EUDAMED and UDI
Reference Documentation
Tools
Device Classification Workflow

Classify device under MDR Annex VIII:

Identify device duration (transient, short-term, long-term)
Determine invasiveness level (non-invasive, body orifice, surgical)
Assess body system contact (CNS, cardiac, other)
Check if active device (energy dependent)
Apply classification rules 1-22
For software, apply MDCG 2019-11 algorithm
Document classification rationale
Validation: Classification confirmed with Notified Body
Classification Matrix
Factor	Class I	Class IIa	Class IIb	Class III
Duration	Any	Short-term	Long-term	Long-term
Invasiveness	Non-invasive	Body orifice	Surgical	Implantable
System	Any	Non-critical	Critical organs	CNS/cardiac
Risk	Lowest	Low-medium	Medium-high	Highest
Software Classification (MDCG 2019-11)
Information Use	Condition Severity	Class
Informs decision	Non-serious	IIa
Informs decision	Serious	IIb
Drives/treats	Critical	III
Classification Examples

Example 1: Absorbable Surgical Suture

Rule 8 (implantable, long-term)
Duration: > 30 days (absorbed)
Contact: General tissue
Classification: Class IIb

Example 2: AI Diagnostic Software

Rule 11 + MDCG 2019-11
Function: Diagnoses serious condition
Classification: Class IIb

Example 3: Cardiac Pacemaker

Rule 8 (implantable)
Contact: Central circulatory system
Classification: Class III
Technical Documentation

Prepare technical file per Annex II and III:

Create device description (variants, accessories, intended purpose)
Develop labeling (Article 13 requirements, IFU)
Document design and manufacturing process
Complete GSPR compliance matrix
Prepare benefit-risk analysis
Compile verification and validation evidence
Integrate risk management file (ISO 14971)
Validation: Technical file reviewed for completeness
Technical File Structure
ANNEX II TECHNICAL DOCUMENTATION
├── Device description and UDI-DI
├── Label and instructions for use
├── Design and manufacturing info
├── GSPR compliance matrix
├── Benefit-risk analysis
├── Verification and validation
└── Clinical evaluation report

GSPR Compliance Checklist
Requirement	Evidence	Status
Safe design (GSPR 1-3)	Risk management file	☐
Chemical properties (GSPR 10.1)	Biocompatibility report	☐
Infection risk (GSPR 10.2)	Sterilization validation	☐
Software requirements (GSPR 17)	IEC 62304 documentation	☐
Labeling (GSPR 23)	Label artwork, IFU	☐
Conformity Assessment Routes
Class	Route	NB Involvement
I	Annex II self-declaration	None
Is/Im	Annex II + IX/XI	Sterile/measuring aspects
IIa	Annex II + IX or XI	Product or QMS
IIb	Annex IX + X or X + XI	Type exam + production
III	Annex IX + X	Full QMS + type exam
Clinical Evidence

Develop clinical evidence strategy per Annex XIV:

Define clinical claims and endpoints
Conduct systematic literature search
Appraise clinical data quality
Assess equivalence (technical, biological, clinical)
Identify evidence gaps
Determine if clinical investigation required
Prepare Clinical Evaluation Report (CER)
Validation: CER reviewed by qualified evaluator
Evidence Requirements by Class
Class	Minimum Evidence	Investigation
I	Risk-benefit analysis	Not typically required
IIa	Literature + post-market	May be required
IIb	Systematic literature review	Often required
III	Comprehensive clinical data	Required (Article 61)
Clinical Evaluation Report Structure
CER CONTENTS
├── Executive summary
├── Device scope and intended purpose
├── Clinical background (state of the art)
├── Literature search methodology
├── Data appraisal and analysis
├── Safety and performance conclusions
├── Benefit-risk determination
└── PMCF plan summary

Qualified Evaluator Requirements
Medical degree or equivalent healthcare qualification
4+ years clinical experience in relevant field
Training in clinical evaluation methodology
Understanding of MDR requirements
Post-Market Surveillance

Establish PMS system per Chapter VII:

Develop PMS plan (Article 84)
Define data collection methods
Establish complaint handling procedures
Create vigilance reporting process
Plan Periodic Safety Update Reports (PSUR)
Integrate with PMCF activities
Define trend analysis and signal detection
Validation: PMS system audited annually
PMS System Components
Component	Requirement	Frequency
PMS Plan	Article 84	Maintain current
PSUR	Class IIa and higher	Per class schedule
PMCF Plan	Annex XIV Part B	Update with CER
PMCF Report	Annex XIV Part B	Annual (Class III)
Vigilance	Articles 87-92	As events occur
PSUR Schedule
Class	Frequency
Class III	Annual
Class IIb implantable	Annual
Class IIb	Every 2 years
Class IIa	When necessary
Serious Incident Reporting
Timeline	Requirement
2 days	Serious public health threat
10 days	Death or serious deterioration
15 days	Other serious incidents
EUDAMED and UDI

Implement UDI system per Article 27:

Obtain issuing entity code (GS1, HIBCC, ICCBBA)
Assign UDI-DI to each device variant
Assign UDI-PI (production identifier)
Apply UDI carrier to labels (AIDC + HRI)
Register actor in EUDAMED
Register devices in EUDAMED
Upload certificates when available
Validation: UDI verified on sample labels
EUDAMED Modules
Module	Content	Actor
Actor	Company registration	Manufacturer, AR
UDI/Device	Device and variant data	Manufacturer
Certificates	NB certificates	Notified Body
Clinical Investigation	Study registration	Sponsor
Vigilance	Incident reports	Manufacturer
Market Surveillance	Authority actions	Competent Authority
UDI Label Requirements

Required elements per Article 13:

 UDI-DI (device identifier)
 UDI-PI (production identifier) for Class II+
 AIDC format (barcode/RFID)
 HRI format (human-readable)
 Manufacturer name and address
 Lot/serial number
 Expiration date (if applicable)
Reference Documentation
MDR Classification Guide

references/mdr-classification-guide.md contains:

Complete Annex VIII classification rules (Rules 1-22)
Software classification per MDCG 2019-11
Worked classification examples
Conformity assessment route selection
Clinical Evidence Requirements

references/clinical-evidence-requirements.md contains:

Clinical evidence framework and hierarchy
Literature search methodology
Clinical Evaluation Report structure
PMCF plan and evaluation report guidance
Technical Documentation Templates

references/technical-documentation-templates.md contains:

Annex II and III content requirements
Design History File structure
GSPR compliance matrix template
Declaration of Conformity template
Notified Body submission checklist
Tools
MDR Gap Analyzer
# Quick gap analysis
python scripts/mdr_gap_analyzer.py --device "Device Name" --class IIa

# JSON output for integration
python scripts/mdr_gap_analyzer.py --device "Device Name" --class III --output json

# Interactive assessment
python scripts/mdr_gap_analyzer.py --interactive


Analyzes device against MDR requirements, identifies compliance gaps, generates prioritized recommendations.

Output includes:

Requirements checklist by category
Gap identification with priorities
Critical gap highlighting
Compliance roadmap recommendations
Notified Body Interface
Selection Criteria
Factor	Considerations
Designation scope	Covers your device type
Capacity	Timeline for initial audit
Geographic reach	Markets you need to access
Technical expertise	Experience with your technology
Fee structure	Transparency, predictability
Pre-Submission Checklist
 Technical documentation complete
 GSPR matrix fully addressed
 Risk management file current
 Clinical evaluation report complete
 QMS (ISO 13485) certified
 Labeling and IFU finalized
 Validation: Internal gap assessment complete
Weekly Installs
172
Repository
alirezarezvani/…e-skills
GitHub Stars
13.4K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass
---
title: patent-application-creator
url: https://skills.sh/robthepcguy/claude-patent-creator/patent-application-creator
---

# patent-application-creator

skills/robthepcguy/claude-patent-creator/patent-application-creator
patent-application-creator
Installation
$ npx skills add https://github.com/robthepcguy/claude-patent-creator --skill patent-application-creator
SKILL.md
Patent Application Creator Skill

Complete end-to-end patent application creation from invention disclosure to USPTO-ready filing.

When to Use

Invoke this skill when users ask to:

Create a complete patent application
Draft a provisional patent application
Prepare a utility patent application
Write patent claims and specification
Generate a full patent filing package
What This Skill Does

Orchestrates the complete patent creation workflow:

Prior Art Search → Identify existing patents
Claims Drafting → Write independent and dependent claims
Specification Writing → Create detailed description
Diagram Generation → Produce technical figures
Abstract Creation → Write concise summary
Compliance Checking → Validate USPTO requirements
IDS Preparation → List prior art for disclosure
Complete Workflow
Phase 1: Discovery & Research (15-30 min)

Invention Interview:

Get detailed invention description from user
Extract key features and novel aspects
Identify problem being solved
List all components/steps

Prior Art Search:

Use Prior Art Search skill (7-step methodology)
Find 10-20 most relevant patents
Document key differences
Assess patentability

Technology Landscape:

Identify CPC classifications
Review competing approaches
Find terminology used in field

Output: Research summary with prior art analysis

Phase 2: Claims Drafting (20-40 min)

Claim Strategy:

Define claim scope based on prior art
Identify distinguishing features
Plan independent/dependent structure
Choose claim types (system, method, etc.)

Independent Claims:

Draft 1-3 broad independent claims
Use preamble-transition-body structure
Include all essential elements
Distinguish from prior art

Dependent Claims:

Add 10-20 dependent claims
Cover specific implementations
Add fall-back positions
Include preferred embodiments

Claim Review:

Use Patent Claims Analyzer skill
Check antecedent basis
Fix definiteness issues
Validate dependencies

Output: Complete claims section (20-25 claims)

Phase 3: Specification Writing (40-90 min)

Title:

Clear, descriptive (< 500 characters)
Matches invention scope
Includes key technology terms

Field of the Invention:

1-2 paragraphs
Describe technical field
Reference relevant classifications

Background:

Problem statement (2-3 paragraphs)
Limitations of existing solutions
Need for invention
Cite prior art from search

Summary:

High-level description (3-5 paragraphs)
Main features and advantages
How it solves the problem
Independent claims in prose

Brief Description of Drawings:

List each figure
One sentence per figure
Reference numbers introduced

Detailed Description:

Complete description of all embodiments
Multiple embodiments (preferred + variations)
Step-by-step for methods
Component-by-component for systems
Reference numbers throughout
Support ALL claim elements (35 USC 112(a))

Examples/Embodiments:

Specific implementations
Working examples
Alternative designs

Advantages/Benefits:

List key advantages
Explain improvements over prior art

Specification Review:

Use Patent Claims Analyzer skill (specification mode)
Verify all claims are supported
Check enablement
Validate completeness

Output: Complete specification (20-50 pages)

Phase 4: Diagrams & Figures (15-30 min)

Identify Figures Needed:

System block diagrams
Method flowcharts
Component details
Alternative embodiments

Generate Diagrams:

Use Patent Diagram Generator skill
Create all required figures
Add reference numbers (10, 20, 30...)
Ensure clarity

Figure Descriptions:

Write detailed figure descriptions
Explain all reference numbers
Describe relationships between components

Output: 3-10 patent figures (SVG/PNG/PDF)

Phase 5: Abstract & Front Matter (10-15 min)

Abstract:

50-150 words (USPTO requirement)
Single paragraph
No claim limitations
Broad technical description

Title Page Info:

Inventors
Assignee
Correspondence address
Prior applications (if any)

Cross-References:

Related applications
Priority claims
Provisional references

Output: Complete front matter

Phase 6: Compliance & Validation (15-20 min)

Formalities Check:

Use Patent Claims Analyzer skill (formalities mode)
Abstract length: 50-150 words
Title length: < 500 characters
Required sections present
Drawing references valid

Claims Compliance:

35 USC 112(b) definiteness
Antecedent basis correct
No indefinite terms
Proper dependencies

Specification Compliance:

35 USC 112(a) written description
Enablement complete
Best mode disclosed
All claims supported

MPEP Guidance:

Use MPEP Search skill
Verify format requirements
Check section 608 compliance
Review any special requirements

Output: Compliance report with fixes

Phase 7: Final Assembly (10-15 min)

Document Assembly:

Title page
Abstract
Drawings (brief description)
Specification
Claims
Abstract (at end)

IDS Preparation:

List all prior art from search
Include publication numbers
Add filing/grant dates
Note relevance

Filing Package:

Specification document
Claims document
Figures (separate files)
IDS form data
Assignment (if applicable)

Output: USPTO-ready filing package

Document Templates
Specification Structure
[TITLE]

FIELD OF THE INVENTION

[Technical field description]

BACKGROUND

[Problem statement and prior art]

SUMMARY

[High-level invention description]

BRIEF DESCRIPTION OF THE DRAWINGS

FIG. 1 illustrates...
FIG. 2 shows...
FIG. 3 depicts...

DETAILED DESCRIPTION

[Comprehensive description with reference numbers]

First Embodiment

[Detailed description of main embodiment]

Second Embodiment

[Alternative embodiment]

Examples

[Working examples]

ADVANTAGES

[Key benefits and improvements]

CONCLUSION

[Broad scope statement]

CLAIMS

[Claims section]

Claims Structure
What is claimed is:

1. A [system/method/apparatus] for [purpose], comprising:
    a [first element];
    a [second element]; and
    wherein [novel relationship/function].

2. The [system/method/apparatus] of claim 1, wherein [additional limitation].

3. The [system/method/apparatus] of claim 1, wherein [alternative limitation].

...

[Continue through all claims]

Quality Checklist

Before finalizing, verify:

 Prior art search completed (Top 10 documented)
 Claims drafted (1-3 independent, 10-20 dependent)
 Specification written (20+ pages)
 All claim elements supported in specification
 Diagrams created (3+ figures with reference numbers)
 Abstract written (50-150 words)
 Title created (< 500 characters)
 Antecedent basis checked (no critical issues)
 Definiteness verified (no indefinite terms)
 Enablement complete (sufficient detail)
 Formalities compliant (MPEP 608)
 IDS list prepared (all prior art included)
 Figures match description
 Reference numbers consistent
 USPTO format requirements met
File Organization
patent-application/
├── 01-research/
│   ├── prior-art-search.md
│   ├── top-10-patents.md
│   └── patentability-assessment.md
├── 02-claims/
│   ├── claims-draft-v1.md
│   ├── claims-final.md
│   └── claims-analysis-report.md
├── 03-specification/
│   ├── specification-outline.md
│   ├── specification-full.md
│   └── specification-review.md
├── 04-diagrams/
│   ├── fig1-system-diagram.svg
│   ├── fig2-method-flowchart.svg
│   ├── fig3-component-detail.svg
│   └── figures-list.md
├── 05-front-matter/
│   ├── abstract.md
│   ├── title.md
│   └── bibliographic-data.md
├── 06-compliance/
│   ├── formalities-check.md
│   ├── claims-compliance.md
│   └── spec-compliance.md
└── 07-filing-package/
    ├── complete-specification.pdf
    ├── claims.pdf
    ├── drawings.pdf
    └── ids-list.md

Integration with Other Skills

This workflow orchestrates:

Prior Art Search skill (Phase 1)
Patent Claims Analyzer skill (Phase 2, 6)
Patent Diagram Generator skill (Phase 4)
MPEP Search skill (Phase 6)
BigQuery Patent Search skill (Phase 1)
Estimated Timeline

Provisional Application (Lighter requirements):

Research: 15 min
Claims: 20 min
Specification: 40 min
Diagrams: 15 min
Total: ~90 minutes

Utility Application (Full formal requirements):

Research: 30 min
Claims: 40 min
Specification: 90 min
Diagrams: 30 min
Compliance: 20 min
Total: ~3.5 hours
User Interaction Points

Throughout the workflow, pause to:

After Research: Present patentability assessment, ask if should proceed
After Claims: Show draft claims, get feedback on scope
After Specification Outline: Review structure before full writing
After Diagrams: Confirm figures match invention description
After Compliance: Show any issues found, make fixes
Before Final: Present complete package for review
Tools Available
Bash: Run Python tools for search, analysis
Write: Save all documents and sections
Read: Load user invention descriptions, prior art
Grep: Search through generated content
Weekly Installs
379
Repository
robthepcguy/cla…-creator
GitHub Stars
97
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
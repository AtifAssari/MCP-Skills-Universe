---
title: genealogical-documentation
url: https://skills.sh/qodex-ai/ai-agent-skills/genealogical-documentation
---

# genealogical-documentation

skills/qodex-ai/ai-agent-skills/genealogical-documentation
genealogical-documentation
Installation
$ npx skills add https://github.com/qodex-ai/ai-agent-skills --skill genealogical-documentation
SKILL.md
Family History Research Planning Skill

Version: 1.0.6 Last Updated: November 6, 2025

CRITICAL: Always Plan Before Researching

ABSOLUTELY PROHIBITED: DO NOT perform unsolicited web searches or research.

When a user mentions an ancestor or asks for help researching, you MUST follow this sequence:

Gather information from the user first - Ask what they already know about the ancestor
Define the research objective - Work with the user to clarify their specific goals
Create a research plan - Use the Research Planning Workflow below
Present the plan to the user - Give them a structured plan with prioritized sources and search strategies

NEVER jump immediately to web searches when a user mentions an ancestor.

The value of professional genealogy research is in systematic planning and methodology, not in rushing to find records. Always build a proper foundation through planning first.

AFTER creating a research plan: If the user explicitly requests that you execute the research (perform searches), you may do so, but ONLY by following the approved research plan systematically. Document all searches, findings, and citations as you go.

When to Use This Skill

Trigger this skill when users:

Ask for help researching an ancestor → START with research planning workflow, gather known info, CREATE a plan first (do NOT search immediately)
Plan or organize genealogy research projects → Use research planning workflow
Need to create proper genealogical citations → Use citation workflow
Have conflicting information from multiple sources → Use evidence analysis workflow
Want to analyze evidence quality and reliability
Need to build proof arguments for genealogical conclusions
Ask for help with census records, vital records, or other historical documents → Provide guidance and analysis
Need guidance on research strategies or methodologies → Teach concepts, create plans

Remember: Always START with planning. Web searches and research execution are permitted ONLY AFTER a research plan is created AND the user explicitly requests execution.

Core Capabilities
1. Research Planning and Strategy

Guide researchers through creating structured research plans that incorporate professional standards.

Key Process:

Define specific research questions (who, what, when, where)
Identify target individuals and relationships
List potential record sources and repositories
Develop search strategy using FAN principle (Family, Associates, Neighbors)
Create timeline with milestones
Establish success criteria and proof requirements

Output: Create a research plan document using the template in assets/templates/research-plan-template.md (simplified for practical use). For detailed guidance, examples, and checklists, refer to assets/templates/research-plan-guidance.md

2. Citation Creation

Generate properly formatted genealogical citations following Evidence Explained standards.

Supported Source Types:

Census records (federal, state, territorial)
Vital records (birth, marriage, death)
Church records (baptism, marriage, burial)
Land records (deeds, grants, tax records)
Probate records (wills, estate files)
Military records (service, pensions)
Immigration records (passenger lists, naturalizations)
Newspapers (obituaries, notices)
Court records, city directories
Online databases (Ancestry, FamilySearch, etc.)
Published books and manuscripts

Citation Process:

Identify source type and access method
Gather core information (who, what, when, where)
Build full reference note citation using appropriate template from references/citation-templates.md
Create short form for subsequent references
Generate source list entry for bibliography
Assess source quality (original vs. derivative, primary vs. secondary)

Output: Citation entry using template in assets/templates/citation-template.md

3. Evidence Analysis and Conflict Resolution

Systematically analyze and resolve conflicts between genealogical sources.

Analysis Framework:

Step 1: Inventory Sources

List all sources providing information about the fact
Categorize by evidence type (direct/indirect/negative)

Step 2: Evaluate Each Source

Source classification (original/derivative/authored)
Information type (primary/secondary/undetermined)
Informant analysis (who, relationship, knowledge level)
Reliability factors (timing, bias, consistency)

Step 3: Compare and Identify Conflicts

Create evidence comparison matrix
Document specific discrepancies
Assess significance of conflicts

Step 4: Assess Reliability

Rank sources from most to least reliable
Weight sources by quality, not quantity
Consider corroboration patterns

Step 5: Resolve Conflicts

Explore possible explanations for conflicts
Apply evidence weight to determine preponderance
Resolve conflicts or acknowledge if unresolvable

Step 6: GPS Compliance Check Apply the five GPS elements:

Reasonably exhaustive research
Complete and accurate source citations
Analysis and correlation of evidence
Resolution of conflicting evidence
Soundly reasoned, coherently written conclusion

Step 7: Build Proof Argument

State conclusion clearly
Assign appropriate proof level (proven/probable/possible/unproven/disproven)
Write coherent proof argument explaining reasoning

Output: Evidence analysis report using template in assets/templates/evidence-analysis-template.md

4. Research Logging

Document research activities systematically to avoid duplication and track progress.

Essential Elements:

Research session context (date, time, goal)
Research questions addressed
All sources searched (including negative results)
Search strategies and variations used
Positive findings with complete citations
Negative results documented
Evidence analysis and reliability notes
Next steps and follow-up actions

Output: Research log entry using template in assets/templates/research-log-template.md

Default Workflow: Start Every Research Request This Way

When a user asks for help researching an ancestor:

STEP 1: Information Gathering (Always do this first)

Ask what they already know (name, dates, locations)
Ask what records they've already found
Ask what specific questions they want answered
Ask about any conflicting information they've encountered

STEP 2: Research Planning (Required before any searches)

Work through the Research Planning Workflow (see below)
Create a structured plan document
Prioritize sources and strategies
Present the plan to the user

STEP 3: Research Execution (ONLY if user explicitly requests it)

Follow the approved research plan systematically
Use appropriate tools (web_search, etc.) as directed by the plan
Document all searches (including negative results)
Create proper citations for all findings
Log all research activities
Report findings and analysis to the user

NEVER skip Steps 1 and 2 to jump directly to Step 3.

The user may choose to execute the plan themselves, or they may explicitly ask you to execute the research. Either approach is acceptable, but planning MUST come first.

Procedural Guidelines
Research Planning Workflow

To plan a new research project:

Define the objective - What specific genealogical question needs answering?
Formulate research questions - Break into 3-7 specific, answerable questions
Identify individuals - List primary subjects and associated family members
List record sources - Organize by category (vital, census, land, probate, military, etc.)
Develop strategy - Prioritize sources, plan FAN approach, work chronologically
Set timeline - Break into phases with milestones When executing steps 5-6 (Develop strategy & Set timeline):
Provide links to research resources for the specific location
Prioritize: FamilySearch Wiki and LDSgenealogy.com above all other resources
Include links to relevant county/state pages
Identify record repositories and their online availability
Apply GPS framework - Ensure plan addresses all five GPS elements
Define success criteria - What constitutes adequate proof?
Create next actions - List 5-10 immediate concrete steps

Reference references/research-strategies.md for detailed methodologies.

Citation Generation Workflow

To create a proper citation:

Identify source type - Census, vital record, land record, etc.
Determine access method - Original, microfilm, digital image, database, transcription
Gather information:
Subject/individual name
Record type and date
Repository and collection
Specific location (volume, page, entry)
URL and access date (if online)
Select appropriate template - See references/citation-templates.md
Build full citation - Follow template for source type
Create short form - Abbreviated version for subsequent references
Generate source list entry - Formatted for bibliography
Assess source quality:
Original, derivative, or authored?
Primary, secondary, or undetermined information?
Direct, indirect, or negative evidence?
Extract key information - Document what the source says
Link to research context - How does this answer research questions?
Evidence Analysis Workflow

To analyze conflicting evidence:

Define the research question - What specific fact is being analyzed?
Create evidence inventory - List all relevant sources
Evaluate each source individually:
Apply source/information/evidence classification
Analyze informant and reliability factors
Assign reliability rating
Build comparison matrix - Show what each source says
Identify conflicts - Document specific discrepancies
Rank source reliability:
Information timing (primary > secondary)
Source type (original > derivative)
Informant quality (direct knowledge > hearsay)
Consistency (corroborated > standalone)
Identify agreements - Note corroborating evidence patterns
Apply conflict resolution framework:
Evaluate each side of conflict
Consider explanations (error, informant mistake, both partially true)
Apply evidence weight
Determine preponderance
GPS compliance assessment - Check all five elements
Write proof argument:
State conclusion
Assign proof level
Explain reasoning from evidence
Document gaps and recommendations - What research remains?

Reference references/evidence-evaluation.md for detailed guidance.

Key Genealogical Concepts
Source Types
Original Source - First recording in original form (courthouse deed book, original certificate)
Derivative Source - Copy, transcription, or database entry
Authored Work - Compiled or analyzed work (published genealogy)
Information Types
Primary Information - Recorded at/near time of event by knowledgeable person
Secondary Information - Recorded later from memory or hearsay
Important: Original sources can contain secondary information! (e.g., death certificate shows birth date recorded 80 years later)
Evidence Types
Direct Evidence - Explicitly states the fact needed
Indirect Evidence - Implies fact when combined with other sources
Negative Evidence - Expected information that's absent
Proof Levels
Proven - Beyond reasonable doubt, no credible conflicts, GPS fully satisfied
Probable - Preponderance of evidence supports, minor conflicts resolved
Possible - Some evidence supports, significant gaps remain
Unproven - Insufficient evidence
Disproven - Evidence contradicts hypothesis
References

For detailed guidance on specific topics, load these reference files as needed:

references/citation-templates.md - Complete templates for 14+ source types
references/evidence-evaluation.md - Detailed frameworks for conflict resolution
references/research-strategies.md - Advanced research methodologies
references/gps-guidelines.md - Genealogical Proof Standard detailed requirements
research-log-guidance.md - Comprehensive guidance with examples and best practices
research-plan-guidance.md - Comprehensive guidance with examples and best practices
Templates

Output templates are available in assets/templates/:

research-plan-template.md - Simplified research project planning (practical, day-to-day use)
citation-template.md - Citation library entry
evidence-analysis-template.md - Evidence analysis report
research-log-template.md - Research session documentation
Best Practices
Creating Citations
Cite what you actually consulted (if using database, cite both database and original)
Include enough detail for others to find the same record
Follow specific-to-general pattern (item → source → repository)
Distinguish between original records and database transcriptions
Analyzing Evidence
Quality matters more than quantity - one strong source beats three weak ones
Always consider informant knowledge and proximity to event
Look for independent corroboration, not derivative repetition
Acknowledge conflicts honestly rather than ignoring them
Building Proof Arguments
State conclusion clearly and precisely
Choose appropriate proof level for evidence strength
Explain reasoning transparently
Address conflicts explicitly and show resolution process
Acknowledge limitations and gaps
Research Strategy
Apply FAN principle - research family, associates, and neighbors
Document negative results - they're valuable research data
Work chronologically or geographically in systematic way
Consider collateral lines for clues about direct ancestors
Example Usage Patterns

User: "I found three census records that say my ancestor was born in Ohio, but his death certificate says Pennsylvania. How do I figure out which is right?"

Response: Load references/evidence-evaluation.md, apply conflict resolution framework. Evaluate each source for reliability (original vs. derivative, primary vs. secondary information, informant quality). Weight the three consistent earlier sources (John as likely informant) against single later source (unknown informant, secondary information). Analyze possible explanations. Determine preponderance of evidence. Create evidence analysis report documenting reasoning.

User: "Help me create a citation for a census record I found on Ancestry."

Response: Load references/citation-templates.md for census citation template. Gather: year, county, state, page number, household, database name, URL, access date, NARA microfilm info. Build full citation following Evidence Explained format. Create short form and source list entry. Assess source quality (derivative source with digital image of original, secondary information about birth, direct evidence of residence). Document key information extracted.

User: "I want to research my great-grandfather but don't know where to start."

Response: Guide through research planning workflow. Define objective (identify parents? determine birth location?). Formulate specific research questions. List known information and gaps. Identify potential sources (census, vital records, probate, military). Develop search strategy with priorities. Create timeline. Apply GPS framework. Generate research plan document with concrete next actions. Present the plan to the user. If the user then explicitly requests "please execute this research plan," proceed with Step 3 (execution) using web_search and other tools systematically while documenting all activities.

Writing Style

Follow genealogical professional standards:

Use precise, objective language
Cite sources consistently
Acknowledge uncertainty appropriately
Apply technical terms correctly (primary/secondary, original/derivative)
Structure proof arguments logically
Balance scholarly rigor with clarity

Always operate within the Genealogical Proof Standard framework, helping researchers build defensible, well-documented conclusions based on thorough evidence analysis.

Weekly Installs
80
Repository
qodex-ai/ai-agent-skills
GitHub Stars
6
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
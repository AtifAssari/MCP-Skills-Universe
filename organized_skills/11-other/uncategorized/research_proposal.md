---
rating: ⭐⭐⭐
title: research-proposal
url: https://skills.sh/luwill/research-skills/research-proposal
---

# research-proposal

skills/luwill/research-skills/research-proposal
research-proposal
Installation
$ npx skills add https://github.com/luwill/research-skills --skill research-proposal
SKILL.md
Research Proposal Generator

Generate high-quality academic research proposals for PhD applications following Nature Reviews-style academic writing conventions.

Overview

This skill guides the generation of research proposals through a structured 5-phase workflow:

Requirements Gathering - Collect research topic, domain, language preferences
Literature Collection - Gather relevant literature from multiple sources
Outline Generation - Create structured outline for user approval
Content Writing - Generate full proposal based on approved outline
Output & Review - Deliver Markdown file with quality checklist

Target Output: 2,000-4,000 words (default ~3,000 words) for PhD applications.

Phase 1: Requirements Gathering

Use AskUserQuestion to collect the following information:

Required Information

Research Topic/Direction

What is the core research question or area?
Any specific problems to address?

Academic Domain

STEM (Science, Technology, Engineering, Mathematics)
Humanities (History, Philosophy, Literature, Languages)
Social Sciences (Sociology, Psychology, Economics, Political Science)

Output Language

English
中文 (Chinese)

Target Word Count

Default: 3,000 words
Range: 2,000-4,000 words (humanities may extend to 10,000)
Optional Information

Target Institution(s)

University/research group names
Specific faculty members of interest

Existing Materials

User's prior research or publications
Relevant literature already collected in Zotero
Example Questions
Questions to ask the user:

1. "What is your research topic or direction? Please describe the core question or problem you want to investigate."

2. "Which academic domain does your research belong to?"
   - STEM (Science, Technology, Engineering, Mathematics)
   - Humanities (History, Philosophy, Literature)
   - Social Sciences (Sociology, Psychology, Economics)

3. "What language should the proposal be written in?"
   - English
   - 中文 (Chinese)

4. "Do you have a target word count? (Default: ~3,000 words)"

5. "Are you applying to specific institutions or working with particular faculty?"

6. "Have you uploaded relevant literature to your Zotero library that I should reference?"

Phase 2: Literature Collection
Literature Sources Strategy
┌─────────────────────────────────────────────────────────┐
│                    Literature Sources                    │
├─────────────────────────────────────────────────────────┤
│  General Info    →  WebSearch (trends, news, reviews)   │
│  Open Access     →  arXiv, PubMed (preprints, OA papers)│
│  Closed Access   →  Zotero MCP (user's uploaded papers) │
└─────────────────────────────────────────────────────────┘

Using WebSearch

Search for:

Recent review articles and meta-analyses
Research trends and emerging topics
News about breakthroughs in the field
Methodological advances

Example searches:

"{topic} systematic review 2024 2025"
"{topic} research trends future directions"
"{topic} methodology recent advances"

Using Zotero MCP

IMPORTANT: Remind users to upload relevant closed-access literature to Zotero before starting.

Search User's Library
# Search by topic keywords
Use: mcp__zotero__zotero_search_items
Parameters: query = "{research topic keywords}"

# Advanced search with filters
Use: mcp__zotero__zotero_advanced_search
Parameters: conditions based on author, title, year, tags

# Semantic search for related papers
Use: mcp__zotero__zotero_semantic_search
Parameters: query = "{research question}"

Retrieve Paper Content
# Get full text content
Use: mcp__zotero__zotero_get_item_fulltext
Parameters: item_key = "{item key from search}"

# Get user's annotations and highlights
Use: mcp__zotero__zotero_get_annotations
Parameters: item_key = "{item key}"

# Get user's notes
Use: mcp__zotero__zotero_get_notes
Parameters: item_key = "{item key}"

Literature Organization

Organize collected literature into categories:

Background/Context - Foundational papers establishing the field
Current State - Recent advances and state-of-the-art
Research Gap - Papers identifying limitations or open questions
Methodology - Papers with relevant methods to adopt/adapt
Related Work - Adjacent research areas for comparison
Phase 3: Outline Generation
Proposal Structure by Domain

Read the reference file for domain-specific guidance:

references/STRUCTURE_GUIDE.md - Detailed section guidelines
references/DOMAIN_TEMPLATES.md - STEM vs Humanities differences
Standard Outline Template
# [Research Title]

## Abstract (150-300 words, 5-10%)
- Research problem summary
- Research questions/objectives
- Methodology overview
- Expected significance

## 1. Introduction (500-800 words, 15-20%)
### 1.1 Background and Context
### 1.2 Problem Statement
### 1.3 Research Questions/Objectives
### 1.4 Scope and Delimitations

## 2. Literature Review (500-1000 words, 20-25%)
### 2.1 Theoretical Framework
### 2.2 Current State of Research
### 2.3 Research Gap Analysis
### 2.4 Positioning of This Study

## 3. Methodology (500-800 words, 20-25%)
### 3.1 Research Design
### 3.2 Data Collection Methods
### 3.3 Data Analysis Approach
### 3.4 Validity and Limitations

## 4. Timeline (200-300 words, 5-10%)
### 4.1 Research Phases
### 4.2 Key Milestones
### 4.3 Gantt Chart (optional)

## 5. Significance and Expected Contributions (200-400 words, 10-15%)
### 5.1 Theoretical Contributions
### 5.2 Practical Implications
### 5.3 Broader Impact

## References (minimum 40 references)


Note: Do NOT include Appendix sections. All essential content should be integrated into the main body.

User Confirmation

CRITICAL: Present the outline to the user and wait for confirmation before proceeding to content generation.

Present the generated outline and ask:

"Here is the proposed outline for your research proposal:

[Display outline with section titles and estimated word counts]

Please review and let me know:
1. Is the overall structure acceptable?
2. Would you like to add, remove, or modify any sections?
3. Should any section receive more/less emphasis?

I will proceed with content generation once you approve the outline."

Phase 4: Content Writing
Writing Style Guidelines

Read and apply: references/WRITING_STYLE_GUIDE.md

Key Principles

Academic Register

Formal tone, avoid colloquialisms
Third person preferred, limited first person plural ("we")
Precise terminology

Prose-Based Writing Style (CRITICAL)

AVOID point-by-point enumeration. Academic proposals should read as flowing, connected prose rather than bulleted lists or numbered items. Use transitional phrases and coherent paragraphs to present ideas.

Avoid	Use Instead
Bullet points listing objectives	Integrated paragraph describing objectives with transitions
Numbered lists of contributions	Narrative prose explaining contributions in context
Tables for methodology steps	Flowing description of research design

When lists ARE appropriate (use sparingly):

Research questions/objectives (as a focused set of 2-4 items)
Timeline milestones (where tabular format aids clarity)
Technical specifications that require precise enumeration

Example transformation:

❌ Poor (point-by-point):

The contributions include:
- Novel segmentation algorithm
- Multi-modal fusion framework
- Clinical validation study


✓ Good (prose-based):

This research is expected to advance the field through several interconnected
contributions. First, the development of a novel segmentation algorithm will
enable automated plaque detection with accuracy surpassing current methods.
Building on this foundation, a multi-modal fusion framework will integrate
complementary imaging data to capture plaque characteristics inaccessible to
any single modality. Finally, rigorous clinical validation will establish
the prognostic value of these computational biomarkers for predicting
cardiovascular events.


Hedging Language (Academic Caution)

Avoid	Use Instead
"will prove"	"aims to demonstrate"
"definitely"	"likely", "potentially"
"is obvious"	"evidence suggests"
"proves"	"indicates", "demonstrates"

Sentence Templates

Introducing Background:

"Over the past decade, [X] has emerged as a critical area of..."
"Recent advances in [X] have opened new possibilities for..."

Identifying Gaps:

"However, [X] remains poorly understood."
"Despite these advances, significant challenges persist in..."
"A critical gap exists in our understanding of..."

Stating Objectives:

"This research aims to address [X] by..."
"The primary objective of this study is to..."
"This proposal seeks to investigate..."

Methodology Justification:

"Building on previous work, this study proposes to..."
"This approach was selected because..."
"[Method] offers several advantages for studying [X]..."

Expected Contributions:

"This work has the potential to advance..."
"The findings may contribute to..."
"This research could provide insights into..."

Transitions and Connectors

Addition: Moreover, Furthermore, In addition, Additionally
Contrast: However, Nevertheless, Conversely, On the other hand
Causation: Therefore, Consequently, As a result, Thus
Emphasis: Importantly, Notably, Of particular significance
Sequence: First, Subsequently, Finally, Following this

Paragraph Structure

Topic Sentence → Supporting Evidence (with citations) → Synthesis/Implications

4-8 sentences per paragraph
Clear logical progression
Explicit transitions between paragraphs
Citation Formatting

Based on domain:

STEM: APA style (Author, Year)
Humanities: MLA or Chicago style
Social Sciences: APA or Chicago style

First mention of abbreviations: "coronary CT angiography (CCTA)"

Integrate citations into text: "Recent studies (Smith et al., 2023; Jones, 2024) have demonstrated..."

Figure Suggestions

IMPORTANT: Include suggestions for figures at appropriate locations throughout the proposal. Figures significantly enhance readability and demonstrate the applicant's ability to communicate complex ideas visually.

Figure Placement Guidelines

Insert figure suggestions using the following format:

> **[Figure 1 Suggestion]** *Title: Overview of the proposed research framework*
> Content: A flowchart or schematic diagram illustrating the three-phase research
> design, showing data flow from imaging modalities through AI processing to
> clinical outcomes. Include icons for CCTA/IVUS/OCT inputs, deep learning
> modules, and output predictions.
> Recommended style: Clean vector graphics with consistent color scheme.

Recommended Figure Types by Section
Section	Suggested Figure Type
Introduction	Conceptual diagram showing research scope and positioning
Literature Review	Timeline of key developments; Taxonomy/classification of existing methods
Methodology	Research framework flowchart; Network architecture diagram; Data processing pipeline
Timeline	Gantt chart showing research phases and milestones
Significance	Impact diagram showing theoretical and practical contributions
Figure Suggestion Principles
Strategic placement: Suggest 3-5 figures for a 3,000-word proposal
Self-explanatory: Each figure should convey key information without requiring extensive caption reading
Consistent style: Recommend unified visual language (colors, fonts, icons)
Professional quality: Suggest tools (e.g., Adobe Illustrator, draw.io, BioRender for biomedical)
Accessibility: Recommend colorblind-friendly palettes and sufficient contrast
Language-Specific Considerations
English Output
Follow standard academic English conventions
Use British or American English consistently
Maintain formal register throughout
Chinese Output (中文)
使用规范学术中文
适当使用 hedging 语言:
"本研究旨在探讨..." (not "本研究将证明...")
"研究结果可能表明..." (not "研究结果必定显示...")
"有望推进..." (not "肯定会推进...")
保持正式学术语体
参考文献格式遵循 GB/T 7714
Phase 5: Output and Review
File Generation

Generate the proposal as a Markdown file:

proposal_{topic_slug}_{YYYY-MM-DD}.md


Save to user's working directory or specified location.

Quality Checklist

Read and apply: references/QUALITY_CHECKLIST.md

Verify:

Structure
 All required sections present
 Word counts within specified ranges
 Logical flow between sections
 Clear section headings
Content
 Research questions clearly stated
 Literature review identifies specific gap
 Methodology appropriate for research questions
 Timeline realistic and detailed
 Significance clearly articulated
Academic Style
 Formal academic tone throughout
 Appropriate hedging language used
 Smooth transitions between sections
 No colloquialisms or informal expressions
 Prose-based writing (minimal bullet points/lists)
 Lists used ONLY where truly necessary (e.g., research questions, timeline)
Figures
 3-5 figure suggestions included at appropriate locations
 Figure suggestions include title, content description, and style recommendations
 Figures distributed across sections (not clustered)
 Each figure serves a clear communicative purpose
Citations
 All claims supported by references
 Citation format consistent
 Minimum 40 references for PhD proposals
 Recent literature included (~60% from last 5 years)
 Seminal/foundational works cited where appropriate
 Balance across different research groups/institutions
Technical
 No grammatical errors
 Abbreviations defined on first use
 Consistent terminology
 Proper markdown formatting
Format Conversion Guidance

Provide user with conversion instructions:

# Convert to Word document
pandoc proposal.md -o proposal.docx

# Convert to PDF (requires LaTeX)
pandoc proposal.md -o proposal.pdf

# Convert to PDF with custom styling
pandoc proposal.md -o proposal.pdf --template=academic.latex

Reference Files

This skill uses the following reference documents:

File	Purpose
references/STRUCTURE_GUIDE.md	Detailed section-by-section writing guide
references/DOMAIN_TEMPLATES.md	STEM vs Humanities structural differences
references/WRITING_STYLE_GUIDE.md	Nature Reviews academic writing style
references/QUALITY_CHECKLIST.md	Complete quality verification checklist
references/LITERATURE_WORKFLOW.md	Literature collection workflow details
assets/proposal_scaffold_en.md	English template scaffold
assets/proposal_scaffold_zh.md	Chinese template scaffold
Workflow Summary
┌──────────────────────────────────────────────────────────────────┐
│                    Research Proposal Generation                   │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Phase 1: Requirements    [Interactive]                          │
│     │     └─ Topic, Domain, Language, Word Count                 │
│     ▼                                                            │
│  Phase 2: Literature      [Automatic]                            │
│     │     └─ WebSearch + Zotero MCP                              │
│     ▼                                                            │
│  Phase 3: Outline         [Interactive - User Approval Required] │
│     │     └─ Generate outline → User confirms → Proceed          │
│     ▼                                                            │
│  Phase 4: Content         [Automatic - One-shot Generation]      │
│     │     └─ Write all sections based on approved outline        │
│     ▼                                                            │
│  Phase 5: Output          [Delivery]                             │
│           └─ Markdown file + Quality checklist + Conversion tips │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘

Error Handling
No Zotero Literature Found

If user's Zotero library has no relevant papers:

Inform user of the limitation
Rely more heavily on WebSearch for open-access sources
Suggest user upload relevant papers and retry
Insufficient Information

If topic is too vague:

Ask clarifying questions about specific aspects
Suggest narrowing the research scope
Provide examples of well-defined research questions
Word Count Constraints

If content exceeds target:

Prioritize essential sections (Introduction, Methodology)
Condense literature review to key points
Offer expanded version as separate file
Notes
This skill is designed specifically for PhD applications
Default output is approximately 3,000 words
Always confirm outline with user before content generation
Follow Nature Reviews-style academic writing conventions
Support both English and Chinese output
Minimum 40 references required for comprehensive literature coverage
Include figure suggestions at appropriate locations (3-5 figures recommended)
NO appendices in the output - keep all content in main body sections
Prefer flowing prose over bullet points and numbered lists
Weekly Installs
260
Repository
luwill/research-skills
GitHub Stars
544
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
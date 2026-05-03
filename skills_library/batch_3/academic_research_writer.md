---
title: academic-research-writer
url: https://skills.sh/endigo/claude-skills/academic-research-writer
---

# academic-research-writer

skills/endigo/claude-skills/academic-research-writer
academic-research-writer
Installation
$ npx skills add https://github.com/endigo/claude-skills --skill academic-research-writer
Summary

Academic research documents with peer-reviewed sources, IEEE citations, and scholarly rigor.

Supports multiple document types: research papers, literature reviews, theses, dissertations, conference papers, and technical reports with standard academic structure
Integrates source discovery from Google Scholar, IEEE Xplore, PubMed, ACM Digital Library, and arXiv with built-in verification for peer-review credibility and author credentials
Generates IEEE-format references automatically with proper citation numbering, handling journal articles, conference papers, books, theses, patents, and online sources
Enforces academic writing standards including formal tone, signal phrases for source integration, proper paraphrasing, and comprehensive quality assurance checklists before finalization
SKILL.md
Academic Research Writer

This skill enables creation of high-quality academic research documents with proper scholarly standards, verified peer-reviewed sources, and IEEE-format citations.

Core Principles
Academic Rigor: Follow scholarly writing conventions and maintain objectivity
Source Verification: Use only peer-reviewed, credible academic sources
Proper Citation: Generate accurate IEEE-format references
Research Integrity: Ensure all claims are supported by verified sources
Workflow
1. Understanding Requirements

Clarify the research document type and requirements:

Document type (research paper, literature review, thesis chapter, etc.)
Research topic and scope
Target length
Specific guidelines (institution, journal, conference)
Required sections
Deadline considerations
2. Research Planning

Develop a research strategy:

Identify key research questions
Define search terms and keywords
Determine relevant academic databases (Google Scholar, IEEE Xplore, PubMed, ACM Digital Library, ScienceDirect)
Establish inclusion/exclusion criteria for sources
Plan document structure
3. Source Discovery and Verification

Finding Sources:

Use web_search to find peer-reviewed sources from:

Google Scholar (scholar.google.com)
IEEE Xplore (ieeexplore.ieee.org)
PubMed (pubmed.ncbi.nlm.nih.gov)
ACM Digital Library (dl.acm.org)
arXiv (arxiv.org) - for preprints in relevant fields
Domain-specific databases

Search Strategy:

Start with broad searches: "machine learning healthcare"
Refine with specific terms: "deep learning medical diagnosis 2023"
Use quotation marks for exact phrases: "convolutional neural networks"
Combine terms strategically
Search for recent publications (last 5-7 years unless historical context needed)

Verification Checklist:

For each source, verify:

 Published in peer-reviewed journal or conference
 Author credentials and institutional affiliation
 Publication venue reputation
 Citation count (higher indicates impact)
 Methodology soundness
 Relevance to research question

Red Flags:

Predatory journals (check journalquality.info or beallslist)
Lack of peer review process
No institutional affiliation
Suspicious publication practices
Pay-to-publish without legitimate review
4. Document Structure

Create documents following this standard academic structure:

Research Paper:

Title
Abstract (150-250 words)
Keywords (5-7 terms)
Introduction
Background and context
Problem statement
Research objectives
Contribution statement
Paper organization
Literature Review / Related Work
Theoretical framework
Previous research synthesis
Research gap identification
Methodology (if applicable)
Research design
Data collection
Analysis approach
Results / Findings
Discussion
Interpretation
Implications
Limitations
Conclusion
Summary of findings
Future work
References (IEEE format)

Literature Review:

Title
Abstract
Introduction
Review Methodology
Thematic Sections (organized by themes/topics)
Discussion and Synthesis
Conclusion
References
5. Writing Guidelines

Academic Tone:

Use formal, objective language
Write in third person (avoid "I" or "we" unless methodologically appropriate)
Use precise technical terminology
Maintain neutral stance (present multiple perspectives)
Use hedging language appropriately ("suggests," "indicates," "may")

Paragraph Structure:

Topic sentence
Supporting evidence with citations
Analysis and interpretation
Transition to next point

Citation Integration:

Introduce sources with context
Use signal phrases ("According to Smith et al. [1]...", "Research by Jones [2] demonstrates...")
Balance direct quotations (use sparingly) with paraphrasing
Cite after every factual claim from external sources
Use citation numbers in square brackets [1], [2], [3]

Avoid:

Plagiarism (always paraphrase and cite)
Unsupported claims
Casual or colloquial language
Personal opinions without evidence
Excessive quotations
Wikipedia or non-academic sources
6. IEEE Reference Format

Generate references in IEEE format following these patterns:

Journal Article:

[1] A. Author, B. Author, and C. Author, "Title of article," Journal Name, vol. X, no. Y, pp. ZZ-ZZ, Month Year.


Conference Paper:

[2] A. Author and B. Author, "Title of paper," in Proc. Conference Name, City, Country, Year, pp. ZZ-ZZ.


Book:

[3] A. Author, Title of Book, Edition. City, State: Publisher, Year.


Book Chapter:

[4] A. Author, "Title of chapter," in Book Title, Edition, Ed. City, State: Publisher, Year, pp. ZZ-ZZ.


Website/Online:

[5] A. Author. "Title of webpage." Website Name. URL (accessed Month Day, Year).


Technical Report:

[6] A. Author, "Title," Institution, City, State, Rep. Number, Month Year.


Thesis/Dissertation:

[7] A. Author, "Title," Ph.D. dissertation, Dept. Abbrev., University, City, State, Year.


Patent:

[8] A. Inventor, "Title," Country Patent Number, Month Day, Year.


Standards:

[9] Title of Standard, Standard Number, Year.


Key IEEE Rules:

Number references consecutively in order of appearance
Use square brackets [1], [2], [3]
For multiple authors: list all if ≤6; use "et al." if >6
Use initials for first/middle names
Abbreviate journal names per IEEE standards
Include DOI when available
Maintain consistent formatting
7. Quality Assurance

Before finalizing, verify:

Content:

 Clear research question/objective
 Logical flow and organization
 Adequate source coverage (minimum 15-20 for research paper)
 All sources verified as peer-reviewed
 Claims supported by citations
 Methodology clearly explained (if applicable)
 Results/findings clearly presented
 Limitations acknowledged

Technical:

 IEEE reference format correct
 All in-text citations match reference list
 No missing references
 Consistent citation numbering
 Proper figure/table captions and numbering

Writing Quality:

 Academic tone maintained
 Clear and concise language
 No grammatical errors
 Transitions between sections smooth
 Abstract accurately summarizes paper
Implementation Approach

When creating an academic document:

Use web_search extensively to find peer-reviewed sources
Verify each source's academic credibility
Extract relevant information and synthesize findings
Write in formal academic style
Integrate citations naturally throughout
Generate complete IEEE reference list
Create document using appropriate tool (docx, pdf, or markdown)
Reference Resources

For detailed guidance on specific aspects:

Academic writing conventions: See ACADEMIC-WRITING.md
IEEE citation examples: See IEEE-CITATION-GUIDE.md
Source verification: See SOURCE-VERIFICATION.md
Output Format

Create documents as:

DOCX: For full research papers, theses, dissertations (use docx skill)
PDF: For final submission versions (use pdf skill)
Markdown: For drafts, literature reviews, or online publication
Notes
Always prioritize source quality over quantity
Recent sources (last 5-7 years) preferred unless historical context required
Maintain research integrity throughout
When in doubt about a source, search for additional verification
Use web_fetch to access full articles when available
Weekly Installs
820
Repository
endigo/claude-skills
GitHub Stars
6
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
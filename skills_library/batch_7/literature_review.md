---
title: literature-review
url: https://skills.sh/davila7/claude-code-templates/literature-review
---

# literature-review

skills/davila7/claude-code-templates/literature-review
literature-review
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill literature-review
Summary

Systematic literature reviews across multiple academic databases with verified citations and professional formatting.

Searches PubMed, bioRxiv, arXiv, Semantic Scholar, and specialized databases (ChEMBL, KEGG, UniProt) via integrated skills; aggregates and deduplicates results across sources
Structures reviews through seven phases: planning, multi-database search, screening, data extraction, thematic synthesis, citation verification, and PDF generation
Verifies all DOIs and citations for accuracy; formats references in APA, Nature, Vancouver, Chicago, or IEEE styles
Generates PRISMA flow diagrams and thematic synthesis visualizations using the scientific-schematics skill; organizes results by theme rather than individual studies
SKILL.md
Literature Review
Overview

Conduct systematic, comprehensive literature reviews following rigorous academic methodology. Search multiple literature databases, synthesize findings thematically, verify all citations for accuracy, and generate professional output documents in markdown and PDF formats.

This skill integrates with multiple scientific skills for database access (gget, bioservices, datacommons-client) and provides specialized tools for citation verification, result aggregation, and document generation.

When to Use This Skill

Use this skill when:

Conducting a systematic literature review for research or publication
Synthesizing current knowledge on a specific topic across multiple sources
Performing meta-analysis or scoping reviews
Writing the literature review section of a research paper or thesis
Investigating the state of the art in a research domain
Identifying research gaps and future directions
Requiring verified citations and professional formatting
Visual Enhancement with Scientific Schematics

⚠️ MANDATORY: Every literature review MUST include at least 1-2 AI-generated figures using the scientific-schematics skill.

This is not optional. Literature reviews without visual elements are incomplete. Before finalizing any document:

Generate at minimum ONE schematic or diagram (e.g., PRISMA flow diagram for systematic reviews)
Prefer 2-3 figures for comprehensive reviews (search strategy flowchart, thematic synthesis diagram, conceptual framework)

How to generate figures:

Use the scientific-schematics skill to generate AI-powered publication-quality diagrams
Simply describe your desired diagram in natural language
Nano Banana Pro will automatically generate, review, and refine the schematic

How to generate schematics:

python scripts/generate_schematic.py "your diagram description" -o figures/output.png


The AI will automatically:

Create publication-quality images with proper formatting
Review and refine through multiple iterations
Ensure accessibility (colorblind-friendly, high contrast)
Save outputs in the figures/ directory

When to add schematics:

PRISMA flow diagrams for systematic reviews
Literature search strategy flowcharts
Thematic synthesis diagrams
Research gap visualization maps
Citation network diagrams
Conceptual framework illustrations
Any complex concept that benefits from visualization

For detailed guidance on creating schematics, refer to the scientific-schematics skill documentation.

Core Workflow

Literature reviews follow a structured, multi-phase workflow:

Phase 1: Planning and Scoping

Define Research Question: Use PICO framework (Population, Intervention, Comparison, Outcome) for clinical/biomedical reviews

Example: "What is the efficacy of CRISPR-Cas9 (I) for treating sickle cell disease (P) compared to standard care (C)?"

Establish Scope and Objectives:

Define clear, specific research questions
Determine review type (narrative, systematic, scoping, meta-analysis)
Set boundaries (time period, geographic scope, study types)

Develop Search Strategy:

Identify 2-4 main concepts from research question
List synonyms, abbreviations, and related terms for each concept
Plan Boolean operators (AND, OR, NOT) to combine terms
Select minimum 3 complementary databases

Set Inclusion/Exclusion Criteria:

Date range (e.g., last 10 years: 2015-2024)
Language (typically English, or specify multilingual)
Publication types (peer-reviewed, preprints, reviews)
Study designs (RCTs, observational, in vitro, etc.)
Document all criteria clearly
Phase 2: Systematic Literature Search

Multi-Database Search:

Select databases appropriate for the domain:

Biomedical & Life Sciences:

Use gget skill: gget search pubmed "search terms" for PubMed/PMC
Use gget skill: gget search biorxiv "search terms" for preprints
Use bioservices skill for ChEMBL, KEGG, UniProt, etc.

General Scientific Literature:

Search arXiv via direct API (preprints in physics, math, CS, q-bio)
Search Semantic Scholar via API (200M+ papers, cross-disciplinary)
Use Google Scholar for comprehensive coverage (manual or careful scraping)

Specialized Databases:

Use gget alphafold for protein structures
Use gget cosmic for cancer genomics
Use datacommons-client for demographic/statistical data
Use specialized databases as appropriate for the domain

Document Search Parameters:

## Search Strategy

### Database: PubMed
- **Date searched**: 2024-10-25
- **Date range**: 2015-01-01 to 2024-10-25
- **Search string**:


("CRISPR"[Title] OR "Cas9"[Title]) AND ("sickle cell"[MeSH] OR "SCD"[Title/Abstract]) AND 2015:2024[Publication Date]

- **Results**: 247 articles


Repeat for each database searched.

Export and Aggregate Results:

Export results in JSON format from each database
Combine all results into a single file
Use scripts/search_databases.py for post-processing:
python search_databases.py combined_results.json \
  --deduplicate \
  --format markdown \
  --output aggregated_results.md

Phase 3: Screening and Selection

Deduplication:

python search_databases.py results.json --deduplicate --output unique_results.json

Removes duplicates by DOI (primary) or title (fallback)
Document number of duplicates removed

Title Screening:

Review all titles against inclusion/exclusion criteria
Exclude obviously irrelevant studies
Document number excluded at this stage

Abstract Screening:

Read abstracts of remaining studies
Apply inclusion/exclusion criteria rigorously
Document reasons for exclusion

Full-Text Screening:

Obtain full texts of remaining studies
Conduct detailed review against all criteria
Document specific reasons for exclusion
Record final number of included studies

Create PRISMA Flow Diagram:

Initial search: n = X
├─ After deduplication: n = Y
├─ After title screening: n = Z
├─ After abstract screening: n = A
└─ Included in review: n = B

Phase 4: Data Extraction and Quality Assessment

Extract Key Data from each included study:

Study metadata (authors, year, journal, DOI)
Study design and methods
Sample size and population characteristics
Key findings and results
Limitations noted by authors
Funding sources and conflicts of interest

Assess Study Quality:

For RCTs: Use Cochrane Risk of Bias tool
For observational studies: Use Newcastle-Ottawa Scale
For systematic reviews: Use AMSTAR 2
Rate each study: High, Moderate, Low, or Very Low quality
Consider excluding very low-quality studies

Organize by Themes:

Identify 3-5 major themes across studies
Group studies by theme (studies may appear in multiple themes)
Note patterns, consensus, and controversies
Phase 5: Synthesis and Analysis

Create Review Document from template:

cp assets/review_template.md my_literature_review.md


Write Thematic Synthesis (NOT study-by-study summaries):

Organize Results section by themes or research questions
Synthesize findings across multiple studies within each theme
Compare and contrast different approaches and results
Identify consensus areas and points of controversy
Highlight the strongest evidence

Example structure:

#### 3.3.1 Theme: CRISPR Delivery Methods

Multiple delivery approaches have been investigated for therapeutic
gene editing. Viral vectors (AAV) were used in 15 studies^1-15^ and
showed high transduction efficiency (65-85%) but raised immunogenicity
concerns^3,7,12^. In contrast, lipid nanoparticles demonstrated lower
efficiency (40-60%) but improved safety profiles^16-23^.


Critical Analysis:

Evaluate methodological strengths and limitations across studies
Assess quality and consistency of evidence
Identify knowledge gaps and methodological gaps
Note areas requiring future research

Write Discussion:

Interpret findings in broader context
Discuss clinical, practical, or research implications
Acknowledge limitations of the review itself
Compare with previous reviews if applicable
Propose specific future research directions
Phase 6: Citation Verification

CRITICAL: All citations must be verified for accuracy before final submission.

Verify All DOIs:

python scripts/verify_citations.py my_literature_review.md


This script:

Extracts all DOIs from the document
Verifies each DOI resolves correctly
Retrieves metadata from CrossRef
Generates verification report
Outputs properly formatted citations

Review Verification Report:

Check for any failed DOIs
Verify author names, titles, and publication details match
Correct any errors in the original document
Re-run verification until all citations pass

Format Citations Consistently:

Choose one citation style and use throughout (see references/citation_styles.md)
Common styles: APA, Nature, Vancouver, Chicago, IEEE
Use verification script output to format citations correctly
Ensure in-text citations match reference list format
Phase 7: Document Generation

Generate PDF:

python scripts/generate_pdf.py my_literature_review.md \
  --citation-style apa \
  --output my_review.pdf


Options:

--citation-style: apa, nature, chicago, vancouver, ieee
--no-toc: Disable table of contents
--no-numbers: Disable section numbering
--check-deps: Check if pandoc/xelatex are installed

Review Final Output:

Check PDF formatting and layout
Verify all sections are present
Ensure citations render correctly
Check that figures/tables appear properly
Verify table of contents is accurate

Quality Checklist:

 All DOIs verified with verify_citations.py
 Citations formatted consistently
 PRISMA flow diagram included (for systematic reviews)
 Search methodology fully documented
 Inclusion/exclusion criteria clearly stated
 Results organized thematically (not study-by-study)
 Quality assessment completed
 Limitations acknowledged
 References complete and accurate
 PDF generates without errors
Database-Specific Search Guidance
PubMed / PubMed Central

Access via gget skill:

# Search PubMed
gget search pubmed "CRISPR gene editing" -l 100

# Search with filters
# Use PubMed Advanced Search Builder to construct complex queries
# Then execute via gget or direct Entrez API


Search tips:

Use MeSH terms: "sickle cell disease"[MeSH]
Field tags: [Title], [Title/Abstract], [Author]
Date filters: 2020:2024[Publication Date]
Boolean operators: AND, OR, NOT
See MeSH browser: https://meshb.nlm.nih.gov/search
bioRxiv / medRxiv

Access via gget skill:

gget search biorxiv "CRISPR sickle cell" -l 50


Important considerations:

Preprints are not peer-reviewed
Verify findings with caution
Check if preprint has been published (CrossRef)
Note preprint version and date
arXiv

Access via direct API or WebFetch:

# Example search categories:
# q-bio.QM (Quantitative Methods)
# q-bio.GN (Genomics)
# q-bio.MN (Molecular Networks)
# cs.LG (Machine Learning)
# stat.ML (Machine Learning Statistics)

# Search format: category AND terms
search_query = "cat:q-bio.QM AND ti:\"single cell sequencing\""

Semantic Scholar

Access via direct API (requires API key, or use free tier):

200M+ papers across all fields
Excellent for cross-disciplinary searches
Provides citation graphs and paper recommendations
Use for finding highly influential papers
Specialized Biomedical Databases

Use appropriate skills:

ChEMBL: bioservices skill for chemical bioactivity
UniProt: gget or bioservices skill for protein information
KEGG: bioservices skill for pathways and genes
COSMIC: gget skill for cancer mutations
AlphaFold: gget alphafold for protein structures
PDB: gget or direct API for experimental structures
Citation Chaining

Expand search via citation networks:

Forward citations (papers citing key papers):

Use Google Scholar "Cited by"
Use Semantic Scholar or OpenAlex APIs
Identifies newer research building on seminal work

Backward citations (references from key papers):

Extract references from included papers
Identify highly cited foundational work
Find papers cited by multiple included studies
Citation Style Guide

Detailed formatting guidelines are in references/citation_styles.md. Quick reference:

APA (7th Edition)
In-text: (Smith et al., 2023)
Reference: Smith, J. D., Johnson, M. L., & Williams, K. R. (2023). Title. Journal, 22(4), 301-318. https://doi.org/10.xxx/yyy
Nature
In-text: Superscript numbers^1,2^
Reference: Smith, J. D., Johnson, M. L. & Williams, K. R. Title. Nat. Rev. Drug Discov. 22, 301-318 (2023).
Vancouver
In-text: Superscript numbers^1,2^
Reference: Smith JD, Johnson ML, Williams KR. Title. Nat Rev Drug Discov. 2023;22(4):301-18.

Always verify citations with verify_citations.py before finalizing.

Best Practices
Search Strategy
Use multiple databases (minimum 3): Ensures comprehensive coverage
Include preprint servers: Captures latest unpublished findings
Document everything: Search strings, dates, result counts for reproducibility
Test and refine: Run pilot searches, review results, adjust search terms
Screening and Selection
Use clear criteria: Document inclusion/exclusion criteria before screening
Screen systematically: Title → Abstract → Full text
Document exclusions: Record reasons for excluding studies
Consider dual screening: For systematic reviews, have two reviewers screen independently
Synthesis
Organize thematically: Group by themes, NOT by individual studies
Synthesize across studies: Compare, contrast, identify patterns
Be critical: Evaluate quality and consistency of evidence
Identify gaps: Note what's missing or understudied
Quality and Reproducibility
Assess study quality: Use appropriate quality assessment tools
Verify all citations: Run verify_citations.py script
Document methodology: Provide enough detail for others to reproduce
Follow guidelines: Use PRISMA for systematic reviews
Writing
Be objective: Present evidence fairly, acknowledge limitations
Be systematic: Follow structured template
Be specific: Include numbers, statistics, effect sizes where available
Be clear: Use clear headings, logical flow, thematic organization
Common Pitfalls to Avoid
Single database search: Misses relevant papers; always search multiple databases
No search documentation: Makes review irreproducible; document all searches
Study-by-study summary: Lacks synthesis; organize thematically instead
Unverified citations: Leads to errors; always run verify_citations.py
Too broad search: Yields thousands of irrelevant results; refine with specific terms
Too narrow search: Misses relevant papers; include synonyms and related terms
Ignoring preprints: Misses latest findings; include bioRxiv, medRxiv, arXiv
No quality assessment: Treats all evidence equally; assess and report quality
Publication bias: Only positive results published; note potential bias
Outdated search: Field evolves rapidly; clearly state search date
Example Workflow

Complete workflow for a biomedical literature review:

# 1. Create review document from template
cp assets/review_template.md crispr_sickle_cell_review.md

# 2. Search multiple databases using appropriate skills
# - Use gget skill for PubMed, bioRxiv
# - Use direct API access for arXiv, Semantic Scholar
# - Export results in JSON format

# 3. Aggregate and process results
python scripts/search_databases.py combined_results.json \
  --deduplicate \
  --rank citations \
  --year-start 2015 \
  --year-end 2024 \
  --format markdown \
  --output search_results.md \
  --summary

# 4. Screen results and extract data
# - Manually screen titles, abstracts, full texts
# - Extract key data into the review document
# - Organize by themes

# 5. Write the review following template structure
# - Introduction with clear objectives
# - Detailed methodology section
# - Results organized thematically
# - Critical discussion
# - Clear conclusions

# 6. Verify all citations
python scripts/verify_citations.py crispr_sickle_cell_review.md

# Review the citation report
cat crispr_sickle_cell_review_citation_report.json

# Fix any failed citations and re-verify
python scripts/verify_citations.py crispr_sickle_cell_review.md

# 7. Generate professional PDF
python scripts/generate_pdf.py crispr_sickle_cell_review.md \
  --citation-style nature \
  --output crispr_sickle_cell_review.pdf

# 8. Review final PDF and markdown outputs

Integration with Other Skills

This skill works seamlessly with other scientific skills:

Database Access Skills
gget: PubMed, bioRxiv, COSMIC, AlphaFold, Ensembl, UniProt
bioservices: ChEMBL, KEGG, Reactome, UniProt, PubChem
datacommons-client: Demographics, economics, health statistics
Analysis Skills
pydeseq2: RNA-seq differential expression (for methods sections)
scanpy: Single-cell analysis (for methods sections)
anndata: Single-cell data (for methods sections)
biopython: Sequence analysis (for background sections)
Visualization Skills
matplotlib: Generate figures and plots for review
seaborn: Statistical visualizations
Writing Skills
brand-guidelines: Apply institutional branding to PDF
internal-comms: Adapt review for different audiences
Resources
Bundled Resources

Scripts:

scripts/verify_citations.py: Verify DOIs and generate formatted citations
scripts/generate_pdf.py: Convert markdown to professional PDF
scripts/search_databases.py: Process, deduplicate, and format search results

References:

references/citation_styles.md: Detailed citation formatting guide (APA, Nature, Vancouver, Chicago, IEEE)
references/database_strategies.md: Comprehensive database search strategies

Assets:

assets/review_template.md: Complete literature review template with all sections
External Resources

Guidelines:

PRISMA (Systematic Reviews): http://www.prisma-statement.org/
Cochrane Handbook: https://training.cochrane.org/handbook
AMSTAR 2 (Review Quality): https://amstar.ca/

Tools:

MeSH Browser: https://meshb.nlm.nih.gov/search
PubMed Advanced Search: https://pubmed.ncbi.nlm.nih.gov/advanced/
Boolean Search Guide: https://www.ncbi.nlm.nih.gov/books/NBK3827/

Citation Styles:

APA Style: https://apastyle.apa.org/
Nature Portfolio: https://www.nature.com/nature-portfolio/editorial-policies/reporting-standards
NLM/Vancouver: https://www.nlm.nih.gov/bsd/uniform_requirements.html
Dependencies
Required Python Packages
pip install requests  # For citation verification

Required System Tools
# For PDF generation
brew install pandoc  # macOS
apt-get install pandoc  # Linux

# For LaTeX (PDF generation)
brew install --cask mactex  # macOS
apt-get install texlive-xetex  # Linux


Check dependencies:

python scripts/generate_pdf.py --check-deps

Summary

This literature-review skill provides:

Systematic methodology following academic best practices
Multi-database integration via existing scientific skills
Citation verification ensuring accuracy and credibility
Professional output in markdown and PDF formats
Comprehensive guidance covering the entire review process
Quality assurance with verification and validation tools
Reproducibility through detailed documentation requirements

Conduct thorough, rigorous literature reviews that meet academic standards and provide comprehensive synthesis of current knowledge in any domain.

Weekly Installs
1.3K
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
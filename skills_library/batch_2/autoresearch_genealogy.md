---
title: autoresearch-genealogy
url: https://skills.sh/aradotso/trending-skills/autoresearch-genealogy
---

# autoresearch-genealogy

skills/aradotso/trending-skills/autoresearch-genealogy
autoresearch-genealogy
Installation
$ npx skills add https://github.com/aradotso/trending-skills --skill autoresearch-genealogy
SKILL.md
autoresearch-genealogy

Skill by ara.so — Daily 2026 Skills collection.

A structured system of autoresearch prompts, Obsidian vault templates, archive guides, and methodology references for AI-assisted genealogy research. Built for Claude Code's autonomous research loops, adaptable to any AI tool or manual workflow.

What This Project Does
Provides 12 Claude Code /autoresearch prompts that autonomously search the web, update your vault, and self-verify results
Supplies a complete 19-file Obsidian vault starter kit with YAML frontmatter and markdown templates
Includes 24 country/region-specific archive guides (Europe, Americas, Oceania, Jewish genealogy)
Offers 9 methodology reference documents covering confidence tiers, DNA guardrails, naming conventions, and source hierarchy
Defines 7 step-by-step workflows for OCR pipelines, oral history, discrepancy resolution, and phase planning
Installation
# Clone the repository
git clone https://github.com/mattprusak/autoresearch-genealogy.git
cd autoresearch-genealogy

# Copy vault template into your Obsidian vault
cp -r vault-template/ ~/path/to/your/ObsidianVault/genealogy/

# Or copy to any markdown editor folder
cp -r vault-template/ ~/Documents/my-genealogy/


No package manager or build step required — this is a pure markdown/prompt project.

Project Structure
autoresearch-genealogy/
├── prompts/              # 12 autoresearch prompt files for Claude Code
├── vault-template/       # 19-file Obsidian vault starter kit
│   ├── Family_Tree.md
│   ├── Research_Log.md
│   ├── Open_Questions.md
│   ├── templates/        # Person, certificate, postcard, region, etc.
│   └── ...
├── archives/             # 24 country/region research guides
├── reference/            # 9 methodology documents
├── workflows/            # 7 step-by-step process guides
└── examples/             # 6 anonymized worked examples

Quick Start Workflow
Step 1: Seed your family tree

Open vault-template/Family_Tree.md and fill in what you already know, starting with yourself and working backward:

---
title: Family Tree
last_updated: 2026-03-19
generations_documented: 3
lines_active: 2
---

# Family Tree

## Generation 1 (Self)
- **Name**: Jane Smith (b. 1985, Chicago, IL)

## Generation 2 (Parents)
- **Father**: John Smith (b. 1955, Detroit, MI)
- **Mother**: Mary O'Brien (b. 1958, Boston, MA)

## Generation 3 (Grandparents)
- **Paternal Grandfather**: Robert Smith (b. ~1920, unknown)
- **Paternal Grandmother**: Helen Kowalski (b. ~1925, Poland?)

Step 2: Scan physical documents

Photograph or scan certificates, letters, postcards. Use the OCR workflow:

See: workflows/ocr-pipeline.md

Step 3: Run autoresearch prompts in Claude Code
/autoresearch prompts/01-tree-expansion.md

Step 4: Audit and verify
/autoresearch prompts/02-cross-reference-audit.md

Autoresearch Prompts — Reference

Each prompt in prompts/ follows this structure:

## Goal
[What this iteration should accomplish]

## Metric
[Measurable success condition — e.g., "increase sourced person files from N to N+10"]

## Direction
[Step-by-step instructions for the AI]

## Verify
[Cross-check to run after each iteration]

## Guard Rails
[What NOT to do — prevent hallucination, preserve source rigor]

## Iterations
[How many loops to run before stopping for human review]

## Protocol
[Output format, file naming, YAML fields to populate]

All 12 Prompts
File	Purpose
01-tree-expansion.md	Push every branch back using web research
02-cross-reference-audit.md	Find and fix discrepancies between tree and sources
03-findagrave-sweep.md	Locate Find a Grave memorials for deceased ancestors
04-gedcom-completeness.md	Sync GEDCOM file with vault data
05-source-citation-audit.md	Verify every person has ≥2 independent sources
06-unresolved-persons.md	Identify and resolve unnamed people in documents
07-timeline-gap-analysis.md	Find life events where records should exist but don't
08-open-question-resolution.md	Systematically attack every open research question
09-bygdebok-extraction.md	Extract data from digitized local history books
10-colonial-records-search.md	Search pre-1800 colonial American records
11-immigration-search.md	Locate passenger manifests and naturalization records
12-dna-chromosome-analysis.md	Analyze per-chromosome ancestry data
Running a prompt in Claude Code
# In Claude Code terminal or chat:
/autoresearch prompts/08-open-question-resolution.md

# With a specific vault path context:
/autoresearch prompts/03-findagrave-sweep.md --context vault-template/Family_Tree.md

Vault Template Files
Person file template (vault-template/templates/person.md)
---
full_name: ""
birth_date: ""
birth_place: ""
death_date: ""
death_place: ""
father: ""
mother: ""
spouse: ""
children: []
confidence: "Moderate Signal"  # Strong Signal | Moderate Signal | Speculative
sources: []
open_questions: []
last_updated: ""
---

# [Full Name]

## Life Events

| Event | Date | Place | Source |
|-------|------|-------|--------|
| Birth | | | |
| Marriage | | | |
| Death | | | |

## Sources

1. [Source 1 — type, repository, date accessed]
2. [Source 2 — type, repository, date accessed]

## Open Questions

- [ ] Question 1
- [ ] Question 2

## Notes

[Narrative summary, naming variant notes, contextual history]

Certificate transcription template (vault-template/templates/certificate.md)
---
document_type: ""        # birth | death | marriage | baptism
document_date: ""
repository: ""
file_reference: ""
transcribed_by: ""
transcription_date: ""
confidence: ""
---

# Certificate: [Type] — [Name] — [Year]

## Transcription

[Verbatim transcription of the document]

## Key Data Extracted

- **Subject**: 
- **Date**: 
- **Place**: 
- **Witnesses/Informants**: 
- **Officiant**: 

## Discrepancies

[Note any conflicts with other sources]

## Image

![[filename.jpg]]

Research log entry pattern (vault-template/Research_Log.md)
## 2026-03-19 — Tree Expansion Session

**Prompt run**: 01-tree-expansion.md  
**Iterations**: 5  
**Metric start**: 42 sourced person files  
**Metric end**: 51 sourced person files  

### Searches Performed
- FamilySearch: "Kowalski Poznan 1880–1920" — 3 results, 2 useful
- Ancestry: "Smith Michigan census 1920" — found Robert Smith (b. 1919)
- FindAGrave: "Helen Kowalski Detroit" — memorial #12345678

### Negative Results (Important)
- No passenger manifest found for Stanislaw Kowalski, searched 1890–1910
- No church records found for O'Brien line in Cork pre-1850

### New Open Questions
- [ ] Was Robert Smith born in Michigan or Ohio? 1920 census says MI, 1930 says OH.

Confidence Tier System

From reference/confidence-tiers.md:

Strong Signal    — Two or more independent primary sources agree
Moderate Signal  — One primary source, or two secondary sources agree
Speculative      — Logical inference, DNA suggestion, or single secondary source


Apply confidence in every person file YAML:

---
confidence: "Moderate Signal"
---

Archive Guides — Key Countries

Each guide in archives/ covers:

Where to find records (free vs paid)
What AI tools can access directly vs what requires browser
Record types available by era
archives/
├── ireland.md
├── england-wales.md
├── scotland.md
├── norway.md
├── sweden.md
├── poland.md
├── germany.md
├── italy.md
├── france.md
├── spain-portugal.md
├── netherlands.md
├── austria.md
├── hungary.md
├── russia-ukraine.md
├── usa-colonial.md
├── usa-immigration.md
├── usa-census.md
├── usa-vital-records.md
├── african-american.md
├── canada.md
├── mexico-latin-america.md
├── australia-new-zealand.md
├── jewish-genealogy.md
└── ...


Example usage in a prompt:

# In prompts/09-bygdebok-extraction.md
## Direction
Consult archives/norway.md for Digitalarkivet access patterns.
Search Bygdebok collections for the Rogaland region, 1750–1900.

Common Patterns
Pattern 1: New ancestor intake

When a new ancestor is found during research:

1. Create person file from vault-template/templates/person.md
2. Set confidence based on source count
3. Add to Family_Tree.md under correct generation
4. Log the discovery in Research_Log.md
5. Add unresolved questions to Open_Questions.md
6. Run 02-cross-reference-audit.md to check for conflicts

Pattern 2: Resolving a date discrepancy
# Open_Questions.md entry
## Q-042: Robert Smith birth state conflict
- 1920 census: born Michigan
- 1930 census: born Ohio
- Status: Unresolved
- Next step: Run 07-timeline-gap-analysis.md targeting Robert Smith


Then in Claude Code:

/autoresearch prompts/07-timeline-gap-analysis.md
# Focus: Robert Smith, b. ~1919, discrepancy Q-042

Pattern 3: DNA-to-genealogy mapping
# In vault-template/Genetic_Profile.md
---
test_company: AncestryDNA
test_date: 2024-11-01
ethnicity_summary:
  - region: Eastern Europe
    percentage: 38
  - region: Ireland/Scotland
    percentage: 31
---

# Then run:
/autoresearch prompts/12-dna-chromosome-analysis.md

Pattern 4: Immigration research loop
# Run immigration search prompt
/autoresearch prompts/11-immigration-search.md

# Prompt will:
# 1. Pull all foreign-born ancestors from Family_Tree.md
# 2. Search passenger manifests (Ellis Island, Ancestry, FamilySearch)
# 3. Search naturalization records (NARA, Ancestry)
# 4. Update person files with ship name, arrival date, port
# 5. Log negative results for each unresolved ancestor

Reference Documents
File	Contents
reference/confidence-tiers.md	Strong / Moderate / Speculative definitions
reference/source-hierarchy.md	Primary vs secondary vs derivative sources
reference/dna-guardrails.md	What DNA can and cannot prove; centimorgan thresholds
reference/naming-conventions.md	Patronymics, farm names, Polish przydomki
reference/gedcom-guide.md	GEDCOM field reference and export instructions
reference/common-pitfalls.md	AI hallucination patterns in genealogy, date traps
reference/glossary.md	Record type definitions, Latin terms, abbreviations
reference/ai-capabilities.md	What AI can access directly vs what requires human
reference/case-for-autoresearch.md	Methodology rationale
Troubleshooting
AI is inventing sources

Set guard rails explicitly in your prompt session:

## Guard Rails (add to any prompt)
- Do NOT fabricate census record URLs or Ancestry record IDs
- If a source cannot be directly linked, mark as "reported" not "confirmed"
- All new claims require a real URL or repository reference
- When uncertain, add to Open_Questions.md — do not guess

Vault files getting out of sync with GEDCOM

Run the completeness audit:

/autoresearch prompts/04-gedcom-completeness.md


This compares every person in your GEDCOM against vault person files and flags mismatches.

Name variants causing duplicate person files

Check reference/naming-conventions.md for your family's relevant region. Common traps:

Norwegian farm name changes (Haugen → Bakke on emigration)
Polish name Latinization in church records (Stanisław → Stanislaus)
Irish anglicization (Ó Briain → O'Brien → Bryan)
Spelling variation in census records ("Sakkarias" vs "Zacharias" — both valid)

Add aliases to person file YAML:

---
full_name: "Stanisław Kowalski"
name_variants:
  - "Stanislaus Kowalski"
  - "Stanley Kowalski"
  - "S. Kowalski"
---

Autoresearch loop running too long

Each prompt has an ## Iterations field. Set it explicitly:

## Iterations
Run 3 iterations maximum, then stop and output a summary for human review.

OCR producing poor results on old documents

See workflows/ocr-pipeline.md. General guidance:

Photograph at 600 DPI minimum
Use even, diffuse lighting — no flash
Pre-process with a contrast adjustment before running OCR
Use vault-template/templates/transcription.md to record both the OCR output and your manual corrections side by side
Contributing

To add a new archive guide or prompt:

Follow the existing file structure and YAML frontmatter patterns
Use placeholder names in all examples (no real family data)
Open a PR with a brief description of what region or record type you've added

License: MIT

Weekly Installs
1.0K
Repository
aradotso/trending-skills
GitHub Stars
42
First Seen
Mar 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn
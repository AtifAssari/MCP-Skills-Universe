---
title: citation-verifier
url: https://skills.sh/jkitchin/skillz/citation-verifier
---

# citation-verifier

skills/jkitchin/skillz/citation-verifier
citation-verifier
Installation
$ npx skills add https://github.com/jkitchin/skillz --skill citation-verifier
SKILL.md
Citation Verifier

Detect and verify citations in scientific documents to identify hallucinated, broken, or invalid references.

Purpose

AI-generated content sometimes includes plausible-looking but fake citations. This skill systematically extracts all citation identifiers from a document and verifies each one against authoritative sources, producing a detailed report with verification status and suggestions for fixing invalid citations.

When to Use

This skill should be invoked when:

User asks to "verify citations" or "check references" in a document
User suspects hallucinated citations in AI-generated content
User wants to validate DOIs, URLs, or other identifiers in a paper
User asks to audit a document for broken links or fake references
User mentions "citation verification", "reference checking", or "DOI validation"
Supported Document Formats
Markdown (.md): Inline links [text](url), reference links [text][ref], bare URLs, DOIs
LaTeX/BibTeX (.tex, .bib): \cite{}, @article{}, DOI fields, URL fields
Org-mode (.org): [[url][text]] links, #+BIBLIOGRAPHY, cite links
Plain text (.txt): Bare URLs, DOIs, arXiv IDs, author-year patterns
Citation Identifiers Detected
DOIs (Digital Object Identifiers)
Pattern: 10.\d{4,}/[^\s]+ or doi.org/10.\d{4,}/[^\s]+
Example: 10.1038/nature12373, https://doi.org/10.1126/science.abc1234
Verification: CrossRef API at https://api.crossref.org/works/{doi}
URLs to Papers
Patterns: Links to known publishers and repositories
Domains: nature.com, science.org, sciencedirect.com, springer.com, wiley.com, acs.org, rsc.org, pnas.org, cell.com, plos.org, mdpi.com, frontiersin.org, academic.oup.com, tandfonline.com
Verification: HTTP HEAD/GET request, check for 200 status and paper metadata
arXiv IDs
Pattern: arXiv:\d{4}\.\d{4,5}(v\d+)? or arxiv.org/abs/\d{4}\.\d{4,5}
Example: arXiv:2301.07041, https://arxiv.org/abs/2301.07041v2
Verification: arXiv API or direct URL check
PubMed IDs (PMIDs)
Pattern: PMID:\s*\d+ or pubmed.ncbi.nlm.nih.gov/\d+
Example: PMID: 12345678
Verification: PubMed URL https://pubmed.ncbi.nlm.nih.gov/{pmid}/
ISBNs
Pattern: ISBN[:\s]*[\d-]{10,17} (ISBN-10 or ISBN-13)
Example: ISBN: 978-0-13-468599-1
Verification: Open Library API https://openlibrary.org/isbn/{isbn}.json
Author-Year Citations
Pattern: ([A-Z][a-z]+(?:\s+(?:et\s+al\.?|and|&)\s+[A-Z][a-z]+)?,?\s*\d{4})
Example: (Smith et al., 2023), (Johnson and Lee, 2022)
Verification: WebSearch to find matching paper (lower confidence)
Verification Procedure
Step 1: Read and Parse Document

Use the Read tool to load the document. Extract all citation identifiers using pattern matching:

DOI patterns:
- https?://(?:dx\.)?doi\.org/(10\.\d{4,}/[^\s\])"'>]+)
- doi:\s*(10\.\d{4,}/[^\s\])"'>]+)
- (10\.\d{4,9}/[-._;()/:A-Z0-9]+)  (bare DOI)

arXiv patterns:
- arXiv:(\d{4}\.\d{4,5}(?:v\d+)?)
- arxiv\.org/abs/(\d{4}\.\d{4,5}(?:v\d+)?)

PubMed patterns:
- PMID:\s*(\d+)
- pubmed\.ncbi\.nlm\.nih\.gov/(\d+)

URL patterns:
- https?://[^\s\])"'<>]+  (filter for academic domains)

ISBN patterns:
- ISBN[:\s-]*((?:\d[-\s]?){9}[\dXx]|(?:\d[-\s]?){13})

Step 2: Deduplicate and Categorize

Create a list of unique identifiers, categorized by type:

DOIs
arXiv IDs
PubMed IDs
ISBNs
URLs (academic)
Author-year citations (text-based)
Step 3: Verify Each Identifier

For each identifier, perform verification in order of reliability:

DOI Verification
Construct CrossRef API URL: https://api.crossref.org/works/{doi}
Use WebFetch to check the API
If successful, extract: title, authors, journal, year
If 404 or error: mark as INVALID
arXiv Verification
Construct URL: https://arxiv.org/abs/{arxiv_id}
Use WebFetch to verify page exists
Extract: title, authors, abstract snippet
If 404: mark as INVALID
PubMed Verification
Construct URL: https://pubmed.ncbi.nlm.nih.gov/{pmid}/
Use WebFetch to verify
Extract: title, authors, journal
If 404: mark as INVALID
ISBN Verification
Construct URL: https://openlibrary.org/isbn/{isbn}.json
Use WebFetch to check
Extract: title, authors, publisher
If 404: mark as INVALID
URL Verification
Use WebFetch to access the URL
Check for HTTP 200 and academic content indicators
Look for: paper title, authors, DOI on page
If unreachable or non-academic: mark as SUSPICIOUS
Author-Year Verification (lowest confidence)
Use WebSearch with query: "{author}" "{year}" paper
Look for matching papers in results
If found: mark as LIKELY VALID with source
If not found: mark as UNVERIFIED
Step 4: Generate Report

Produce a structured verification report:

# Citation Verification Report

**Document:** [filename]
**Date:** [date]
**Total citations found:** [count]

## Summary
- Valid: [count]
- Invalid: [count]
- Suspicious: [count]
- Unverified: [count]

## Detailed Results

### Valid Citations
| ID | Type | Title | Source |
|----|------|-------|--------|
| 10.1038/xxx | DOI | Paper Title | CrossRef |

### Invalid Citations (HALLUCINATED)
| ID | Type | Error | Suggestion |
|----|------|-------|------------|
| 10.9999/fake | DOI | 404 Not Found | Remove or find correct DOI |

### Suspicious Citations
| ID | Type | Issue | Recommendation |
|----|------|-------|----------------|
| https://... | URL | Timeout | Verify manually |

### Unverified Citations
| Citation | Type | Notes |
|----------|------|-------|
| (Smith, 2023) | Author-year | No matching paper found via search |

Verification Status Definitions
VALID: Identifier resolves to a real paper with matching metadata
INVALID: Identifier does not exist or returns 404 (likely hallucinated)
SUSPICIOUS: Could not fully verify; may be rate-limited, paywalled, or temporarily unavailable
UNVERIFIED: Text-based citation that couldn't be confirmed (conservative approach)
Best Practices
Batch similar requests: Group DOI checks together to minimize API calls
Respect rate limits: Add delays between requests if hitting rate limits
Cross-reference: If a URL contains a DOI, verify the DOI directly
Context matters: Note where citations appear (methods vs. claims)
Report uncertainty: Always distinguish between "confirmed invalid" and "could not verify"
Output Suggestions for Invalid Citations

For each invalid citation, provide actionable suggestions:

Wrong DOI format: "DOI appears malformed. Check for typos or extra characters."
Non-existent DOI: "No paper found. This may be hallucinated. Search for the actual paper title."
Dead URL: "URL returns 404. Try searching for the paper title on Google Scholar."
Suspicious journal: "Publisher not recognized. Verify this is a legitimate source."
Author-year not found: "Could not verify. Add DOI or URL for confirmation."
Example Verification Session

User request: "Verify the citations in my-paper.md"

Expected behavior:

Read my-paper.md
Extract all DOIs, URLs, arXiv IDs, etc.
Report: "Found 15 citations: 8 DOIs, 5 URLs, 2 arXiv IDs"
Verify each identifier using appropriate API/fetch
Generate report showing:
10 valid citations with metadata
3 invalid citations (404 errors) marked as likely hallucinated
2 suspicious citations (timeouts) requiring manual check
Provide suggestions for fixing invalid citations
Limitations
Rate limits: CrossRef and other APIs may rate-limit requests
Paywalled content: Cannot verify full content behind paywalls
New papers: Very recent papers may not be indexed yet
Author-year citations: Low confidence without additional identifiers
Non-English sources: Limited support for non-English citation formats
Private/institutional URLs: Cannot access authenticated content
Related Skills
literature-review: For conducting systematic literature searches
scientific-reviewer: For reviewing scientific document quality
scientific-writing: For writing with proper citations
Weekly Installs
34
Repository
jkitchin/skillz
GitHub Stars
28
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn
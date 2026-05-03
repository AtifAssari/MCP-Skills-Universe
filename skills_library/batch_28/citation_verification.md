---
title: citation-verification
url: https://skills.sh/galaxy-dawn/claude-scholar/citation-verification
---

# citation-verification

skills/galaxy-dawn/claude-scholar/citation-verification
citation-verification
Installation
$ npx skills add https://github.com/galaxy-dawn/claude-scholar --skill citation-verification
SKILL.md
Citation Verification Reference Guide

A reference guide for citation verification in academic paper writing, providing verification principles and best practices.

Core Principle: Proactively verify every citation during the writing process using WebSearch and Google Scholar.

Core Problems

Citation issues in academic papers seriously impact research integrity:

Fake citations - Citing non-existent papers (common issue with AI-generated citations)
Incorrect information - Mismatched authors, titles, years, etc.
Inconsistent formatting - Mixed citation formats
Missing citations - Referenced but uncited work

These issues can lead to:

Paper rejection or retraction
Damage to academic reputation
Reviewers questioning research rigor

Special risk with AI-assisted writing: AI-generated citations have approximately 40% error rate; every citation must be verified via WebSearch.

Verification Principles

This skill provides verification principles based on WebSearch and Google Scholar:

1. Proactive Verification (Verify During Writing)

Core idea: Verify immediately when adding a citation, rather than checking after writing is complete.

Search for the paper via WebSearch each time a citation is needed
Confirm the paper exists on Google Scholar
Add to bibliography only after verification passes
2. Google Scholar Verification

Why Google Scholar:

Most comprehensive academic literature coverage
Provides citation count (credibility indicator)
Directly provides BibTeX format
Free and no API required

Verification steps:

WebSearch query: "site:scholar.google.com [paper title] [first author]"
Confirm the paper appears in results
Check citation count (abnormally low counts may indicate issues)
Click "Cite" to get BibTeX
3. Information Matching Verification

Information that must match:

Title (minor differences allowed, e.g., capitalization)
Authors (at least the first author must match)
Year (±1 year difference allowed, considering preprints)
Publication venue (conference/journal name)
4. Claim Verification

Key principle: When citing a specific claim, you must confirm the claim actually appears in the paper.

Use WebSearch to access the paper PDF
Search for relevant keywords
Confirm the accuracy of the claim
Record the section/page where the claim appears
Verification Workflow
Integration into Writing Process
Need a citation during writing
    ↓
WebSearch to find the paper
    ↓
Google Scholar to verify existence
    ↓
Confirm paper details
    ↓
Get BibTeX
    ↓
(If citing a specific claim) Verify the claim
    ↓
Add to bibliography


Key point: Verification is part of the writing process, not a separate post-processing step.

Usage Guide
Using with ml-paper-writing

The verification principles of this skill are integrated into the Citation Workflow of the ml-paper-writing skill.

Auto-trigger: Citation verification is automatically executed when writing papers with the ml-paper-writing skill.

Manual reference: Refer to this skill when you need detailed verification principles.

Verification Step Example

Scenario: Need to cite the Transformer paper

Step 1: WebSearch lookup
Query: "Attention is All You Need Vaswani 2017"
Result: Found multiple sources for the paper

Step 2: Google Scholar verification
Query: "site:scholar.google.com Attention is All You Need Vaswani"
Result: ✅ Paper exists, 50,000+ citations, NeurIPS 2017

Step 3: Confirm details
- Title: "Attention is All You Need"
- Authors: Vaswani, Ashish; Shazeer, Noam; Parmar, Niki; ...
- Year: 2017
- Venue: NeurIPS (NIPS)

Step 4: Get BibTeX
- Click "Cite" on Google Scholar
- Select BibTeX format
- Copy BibTeX entry

Step 5: Add to bibliography
- Paste into .bib file
- Use \cite{vaswani2017attention} in the paper

Handling Verification Failures

If the paper cannot be found on Google Scholar:

Check spelling - Is the title or author name correct?
Try different queries - Use different keyword combinations
Find alternative sources - Try arXiv, DOI
Mark as pending - Use [CITATION NEEDED] marker
Notify the user - Clearly state the citation cannot be verified

If information doesn't match:

Confirm the source - Did you find the correct paper?
Check versions - Preprint vs. published version
Update information - Use the most accurate version
Record discrepancies - Note the reason for differences
Best Practices
Preventing Fake Citations
Never generate citations from memory - AI-generated citations have 40% error rate
Use WebSearch to find - Verify every citation through WebSearch
Confirm on Google Scholar - Verify paper existence on Google Scholar
Verify promptly - Verify when adding citations, don't wait until finished
Handling Verification Failures
Don't guess - If you can't find the paper, don't fabricate information
Mark clearly - Use [CITATION NEEDED] to mark explicitly
Notify the user - Clearly state which citations cannot be verified
Provide reasons - Explain why verification failed (not found, info mismatch, etc.)
Improving Verification Accuracy
Complete queries - Include title, author, year
Check citation count - Citation count on Google Scholar is a credibility indicator
Confirm venue - Verify conference/journal name is correct
Verify claims - When citing specific claims, confirm they exist in the paper
Common Pitfalls

❌ Wrong approach:

Generating BibTeX from memory
Skipping Google Scholar verification
Assuming a paper exists
Not marking unverifiable citations

✅ Correct approach:

Search every citation with WebSearch
Confirm on Google Scholar
Copy BibTeX from Google Scholar
Clearly mark unverifiable citations
Summary

Core Principle: Proactively verify every citation during the writing process using WebSearch and Google Scholar.

Key Steps:

WebSearch to find the paper
Google Scholar to verify existence
Confirm details
Get BibTeX
Verify claims (if needed)
Add to bibliography

Failure handling: When verification fails, mark as [CITATION NEEDED] and clearly notify the user.

Integration: The principles of this skill are integrated into the ml-paper-writing skill for automatic verification.

Weekly Installs
118
Repository
galaxy-dawn/cla…-scholar
GitHub Stars
3.5K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
---
rating: ⭐⭐⭐
title: url-analysis
url: https://skills.sh/89jobrien/steve/url-analysis
---

# url-analysis

skills/89jobrien/steve/url-analysis
url-analysis
Installation
$ npx skills add https://github.com/89jobrien/steve --skill url-analysis
SKILL.md
URL Analysis

This skill validates URLs both technically and contextually, ensuring links are functional and appropriate for their context.

When to Use This Skill
When validating URLs in content
When analyzing link context and appropriateness
When extracting links from documents
When checking link functionality
When ensuring link relevance
When auditing link quality
What This Skill Does
Technical Validation: Checks HTTP status, redirects, SSL
Contextual Analysis: Evaluates link appropriateness
Link Extraction: Extracts and categorizes links
Content Relevance: Checks if linked content matches context
Security Analysis: Identifies security concerns
Quality Assessment: Provides link quality scores
Helper Scripts

This skill includes Python helper scripts in scripts/:

validate_urls.py: Validates URLs from files or command line. Checks HTTP status codes, redirects, and accessibility. Outputs JSON with validation results.

# Validate URLs from file
python scripts/validate_urls.py document.md

# Validate single URL
python scripts/validate_urls.py --url https://example.com

How to Use
Validate URLs
Validate all URLs in this document

Check if these links are appropriate for their context

Specific Analysis
Extract and analyze all links in this content

Analysis Process
Technical Validation

Using Helper Script:

The skill includes a Python helper script for URL validation:

# Validate URLs from a file
python scripts/validate_urls.py document.md

# Validate a single URL
python scripts/validate_urls.py --url https://example.com


Checks:

HTTP status codes (200, 301, 404, etc.)
Redirect chains
Response times
SSL certificate validity
URL syntax validity
Contextual Analysis

Evaluates:

Link text vs. destination content
Semantic alignment
Publication date relevance
Authority of source
Value to reader
Link Extraction

Categorizes:

Internal vs. external links
Anchor links
File downloads
API endpoints
Examples
Example 1: URL Validation

Input: Validate URLs in blog post

Output:

## URL Analysis: Blog Post

### Technical Validation

**1. https://example.com/article**
- **Status**: 200 OK
- **Response Time**: 320ms
- **SSL**: Valid
- **Redirects**: None

**2. https://old-site.com/page**
- **Status**: 301 → https://new-site.com/page
- **Issue**: Redirect chain (should update link)
- **Fix**: Update to final destination

**3. https://broken-link.com**
- **Status**: 404 Not Found
- **Issue**: Broken link
- **Fix**: Remove or find alternative

### Contextual Analysis

**4. https://example.com/article**
- **Link Text**: "Learn more about React"
- **Destination**: React documentation
- **Relevance**: High ✓
- **Status**: Appropriate

**5. https://example.com/homepage**
- **Link Text**: "Advanced React patterns"
- **Destination**: Homepage (not specific article)
- **Relevance**: Low ✗
- **Issue**: Link text doesn't match destination
- **Fix**: Link to specific article or update link text

Best Practices
URL Validation
Check Status: Verify all links return 200 or appropriate redirect
Update Redirects: Use final destination, not redirect chains
Context Matters: Ensure links match their context
Security: Prefer HTTPS, check SSL validity
Relevance: Verify linked content matches expectations
Related Use Cases
Link validation
Content quality assurance
SEO link auditing
Documentation review
Link extraction and analysis
Weekly Installs
25
Repository
89jobrien/steve
GitHub Stars
4
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn
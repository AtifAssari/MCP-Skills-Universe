---
title: vm-codebase-audit
url: https://skills.sh/zeal422/dev-toolbelt-by-vm/vm-codebase-audit
---

# vm-codebase-audit

skills/zeal422/dev-toolbelt-by-vm/vm-codebase-audit
vm-codebase-audit
Installation
$ npx skills add https://github.com/zeal422/dev-toolbelt-by-vm --skill vm-codebase-audit
SKILL.md
Codebase Audit Skill

Comprehensive codebase auditing with SEO, security, performance, accessibility, and technical checks.

Mode Selection

ALWAYS start by asking the user to select a mode using the ask_user_input tool:

ask_user_input_v0({
  "questions": [
    {
      "question": "Select audit mode:",
      "type": "single_select",
      "options": [
        "Normal - Core checks (technical, content, mobile, UX, security, accessibility)",
        "Strict - Normal + performance, links, crawlability, schema, URL structure",
        "Expert - All checks including E-E-A-T, legal, social, local SEO, video"
      ]
    },
    {
      "question": "Select operation type:",
      "type": "single_select",
      "options": [
        "Complete Audit - Full codebase crawl with cross-reference analysis",
        "PR Review - Uncommitted changes only"
      ]
    }
  ]
})


After mode selection, respond:

AWESOME! The CLANKER is now... Loading... bEEp BooP 🤖


Then proceed with the audit.

Execution Strategy
PR Review Mode
Run git status and git diff to find uncommitted changes
Analyze only modified/new files
Focus on changes that impact audit categories
Cross-reference with related files when necessary
Complete Audit Mode
Scan entire codebase recursively
Build file inventory with categorization
Analyze each file against audit rules
Cross-reference across files for consistency
Generate comprehensive report
Audit Categories by Mode
Normal Mode
Technical Problems
Content Quality
Mobile Friendliness
User Experience
Security
Accessibility
Strict Mode (Normal +)
Performance
Links (internal/external)
Crawlability
Schema.org Markup
URL Structure
Keyword Analysis
Expert Mode (Strict +)
E-E-A-T (Expertise, Experience, Authority, Trust)
Legal Compliance
Social Media Integration
Local SEO
Video Optimization
Dead Code Detection
Code Consistency
Audit Rules
SEO Issues

Meta Tags (Error: 9)

# Check: Missing or duplicate meta descriptions
# Example:
<meta name="description" content="Buy shoes"> # ❌ Too short (< 50 chars)
<meta name="description" content="Shop premium running shoes..."> # ✅ Good (50-160)


Title Tags (Error: 10)

# Check: Title length, uniqueness, keyword placement
<title>Home</title> # ❌ Generic, too short
<title>Premium Running Shoes | Brand Name - Shop Now</title> # ✅ Optimal (50-60 chars)


Canonical URLs (Warning: 8)

<!-- Check: Missing or incorrect canonical tags -->
<link rel="canonical" href="http://example.com/page"> <!-- ❌ HTTP not HTTPS -->
<link rel="canonical" href="https://example.com/page"> <!-- ✅ Correct -->


Open Graph (Warning: 6)

<!-- Check: Missing OG tags for social sharing -->
<meta property="og:title" content="Page Title">
<meta property="og:description" content="Description">
<meta property="og:image" content="https://example.com/image.jpg">
<meta property="og:url" content="https://example.com/page">

Technical Problems

Broken Links (Error: 9)

# Check: 404s, redirect chains, external link validity
# Detect:
- Dead internal links: <a href="/deleted-page">
- Redirect chains: /a → /b → /c (max 1 redirect)
- Broken external: <a href="https://dead-site.com">


Redirect Chains (Warning: 7)

# Check: Multiple redirects before final destination
# Example:
/old → /temp → /new # ❌ 2 hops
/old → /new # ✅ 1 hop


Mobile Friendliness (Error: 9)

<!-- Check: Viewport meta, responsive design -->
<!-- Missing viewport: -->
❌ No viewport tag

<!-- Correct: -->
✅ <meta name="viewport" content="width=device-width, initial-scale=1">


Mixed Content (Error: 10)

<!-- Check: HTTP resources on HTTPS pages -->
<script src="http://example.com/script.js"> <!-- ❌ HTTP on HTTPS page -->
<script src="https://example.com/script.js"> <!-- ✅ HTTPS -->

Performance

Page Load Time (Warning: 8)

# Check: Bundle size, render-blocking resources
# Detect:
- Large JS bundles (> 200KB)
- Unminified CSS/JS
- Missing compression (gzip/brotli)
- Render-blocking scripts in <head>


Resource Usage (Warning: 6)

// Check: Unused dependencies, duplicate code
// Example:
import { huge-library } from 'library'; // ❌ Full library import
import { specific-function } from 'library'; // ✅ Tree-shaking friendly


Caching (Warning: 7)

# Check: Cache headers, static asset versioning
# Example:
Cache-Control: no-cache # ❌ Not cached
Cache-Control: public, max-age=31536000 # ✅ Long-term cache for static assets


Image Optimization (Warning: 8)

<!-- Check: Format, size, lazy loading -->
<img src="photo.png" width="2000"> <!-- ❌ Large PNG, not optimized -->
<img src="photo.webp" loading="lazy" width="800"> <!-- ✅ WebP, lazy load -->

Content Quality

Heading Structure (Warning: 7)

<!-- Check: H1 uniqueness, logical hierarchy -->
<h1>Title</h1>
<h3>Subtitle</h3> <!-- ❌ Skipped H2 -->

<h1>Title</h1>
<h2>Section</h2> <!-- ✅ Correct order -->


Image Alt Text (Error: 9)

<!-- Check: Missing alt, decorative images -->
<img src="photo.jpg"> <!-- ❌ Missing alt -->
<img src="photo.jpg" alt=""> <!-- ✅ Decorative (intentionally empty) -->
<img src="photo.jpg" alt="Red sports car on mountain road"> <!-- ✅ Descriptive -->


Content Analysis (Notice: 5)

# Check: Reading level, thin content, keyword stuffing
# Detect:
- Pages < 300 words (thin content)
- Keyword density > 3% (stuffing)
- Duplicate content across pages

Security

Leaked Secrets (Error: 10)

# Check: API keys, passwords, tokens in code
# Detect patterns:
API_KEY = "sk-1234567890abcdef" # ❌ Exposed secret
PASSWORD = "admin123" # ❌ Hardcoded password
DB_CONNECTION = "postgres://user:pass@host" # ❌ Credentials in code

# ✅ Use environment variables
API_KEY = os.getenv('API_KEY')


HTTPS Usage (Error: 10)

# Check: All resources over HTTPS
# Detect:
http://api.example.com # ❌ HTTP API
https://api.example.com # ✅ HTTPS


Security Headers (Warning: 8)

# Check: CSP, HSTS, X-Frame-Options, etc.
# Required headers:
Content-Security-Policy: default-src 'self'
Strict-Transport-Security: max-age=31536000
X-Frame-Options: DENY
X-Content-Type-Options: nosniff


Dependencies (Warning: 7)

# Check: Known vulnerabilities in package.json/requirements.txt
# Flag outdated packages with CVEs

Accessibility

Color Contrast (Error: 8)

/* Check: WCAG AA compliance (4.5:1 for normal text) */
.text { color: #777; background: #fff; } /* ❌ 4.47:1 - Fails AA */
.text { color: #666; background: #fff; } /* ✅ 5.74:1 - Passes AA */


Keyboard Navigation (Error: 9)

<!-- Check: Tab order, focus indicators -->
<div onclick="submit()"> <!-- ❌ Not keyboard accessible -->
<button onclick="submit()"> <!-- ✅ Keyboard accessible -->

<a href="#" style="outline: none;"> <!-- ❌ Removed focus outline -->
<a href="#"> <!-- ✅ Default focus visible -->


ARIA Labels (Warning: 7)

<!-- Check: Proper ARIA usage -->
<button>⚙️</button> <!-- ❌ Icon only, no label -->
<button aria-label="Settings">⚙️</button> <!-- ✅ Accessible label -->


Form Labels (Error: 9)

<!-- Check: Every input has associated label -->
<input type="text" placeholder="Email"> <!-- ❌ Placeholder not label -->
<label for="email">Email</label>
<input type="text" id="email"> <!-- ✅ Proper label -->

User Experience

Form Validation (Warning: 6)

// Check: Client-side validation, error messages
// Example:
<input type="email"> // ✅ HTML5 validation
<input type="text"> // ❌ No validation for email field

// Error messages:
"Invalid" // ❌ Not helpful
"Please enter a valid email address" // ✅ Clear guidance


Error Handling (Warning: 7)

// Check: User-friendly error pages, fallbacks
try {
  fetchData();
} catch (e) {
  console.log(e); // ❌ Silent failure
}

try {
  fetchData();
} catch (e) {
  showErrorMessage("Unable to load data. Please try again."); // ✅ User feedback
}


User Flow (Notice: 5)

# Check: Dead ends, broken checkout flows, complex navigation
# Analyze:
- Pages with no CTA
- Forms with > 10 fields (break into steps)
- Navigation depth > 4 levels

Links

Broken Internal Links (Error: 9)

<!-- Check: All internal links resolve -->
<a href="/deleted-page">Link</a> <!-- ❌ 404 -->
<a href="/existing-page">Link</a> <!-- ✅ Valid -->


External Link Validation (Warning: 6)

# Check: External links return 200, have rel="noopener" for security
<a href="https://external.com" target="_blank"> # ❌ Missing rel
<a href="https://external.com" target="_blank" rel="noopener noreferrer"> # ✅ Secure


Anchor Text (Notice: 4)

<!-- Check: Descriptive anchor text -->
<a href="/page">Click here</a> <!-- ❌ Generic -->
<a href="/page">Read our privacy policy</a> <!-- ✅ Descriptive -->

E-E-A-T (Expert Mode)

Expertise (Notice: 6)

# Check: Author credentials, bio pages
# Detect:
- Missing author bylines
- No author bio/credentials
- Lack of citations/references


Experience (Notice: 5)

# Check: First-hand experience indicators
# Look for:
- Personal anecdotes
- Original research
- Case studies
- Product testing details


Authority (Notice: 6)

# Check: Domain authority signals
# Analyze:
- Backlinks from authoritative sites
- Industry recognition
- Expert endorsements


Trustworthiness (Warning: 7)

# Check: Trust signals
# Detect:
- Missing contact information
- No privacy policy
- Insecure forms (HTTP)
- Fake reviews

Crawlability (Strict/Expert Mode)

robots.txt (Warning: 7)

# Check: Proper robots.txt configuration
# Issues:
User-agent: *
Disallow: / # ❌ Blocks all crawlers

User-agent: *
Disallow: /admin/ # ✅ Selective blocking
Allow: /


Sitemap.xml (Warning: 6)

<!-- Check: Valid sitemap, submitted to search engines -->
<!-- Missing: -->
❌ No sitemap.xml found

<!-- Valid: -->
✅ sitemap.xml with < 50,000 URLs, submitted to GSC


Meta Robots (Warning: 7)

<!-- Check: Proper indexing directives -->
<meta name="robots" content="noindex, nofollow"> <!-- ❌ Blocking important page -->
<meta name="robots" content="index, follow"> <!-- ✅ Allowing indexing -->

Schema Markup (Strict/Expert Mode)

Structured Data (Warning: 7)

<!-- Check: Valid Schema.org markup -->
<!-- Missing: -->
❌ No structured data on product page

<!-- Valid: -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Product Name",
  "offers": {
    "@type": "Offer",
    "price": "29.99",
    "priceCurrency": "USD"
  }
}
</script>


Rich Snippets (Notice: 5)

# Check: Breadcrumbs, Reviews, FAQ schema
# Common schemas:
- Product
- Article
- BreadcrumbList
- FAQPage
- Review

Legal Compliance (Expert Mode)

Privacy Policy (Warning: 8)

# Check: Privacy policy exists, linked in footer, GDPR/CCPA compliant
# Required elements:
- Data collection disclosure
- Cookie usage
- Third-party sharing
- User rights (access, deletion)


Terms of Service (Warning: 7)

# Check: ToS exists, clear user agreements
# Required for:
- E-commerce sites
- SaaS platforms
- User-generated content


Cookie Consent (Warning: 8)

// Check: GDPR/CCPA cookie consent
// Required:
- Consent banner before tracking
- Opt-out mechanism
- Clear cookie policy


Accessibility Compliance (Warning: 9)

# Check: WCAG 2.1 AA compliance (ADA requirement)
# Critical:
- All images have alt text
- Forms are keyboard accessible
- Color contrast meets standards
- Screen reader compatibility

Social Media (Expert Mode)

Open Graph Validation (Warning: 6)

<!-- Check: Complete OG tags, correct image dimensions -->
<meta property="og:image" content="small.jpg" width="200"> <!-- ❌ Too small -->
<meta property="og:image" content="large.jpg" width="1200" height="630"> <!-- ✅ Optimal -->


Twitter Cards (Warning: 5)

<!-- Check: Twitter card meta tags -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Page Title">
<meta name="twitter:image" content="https://example.com/image.jpg">


Social Share Buttons (Notice: 3)

# Check: Share buttons present, functional
# Validate:
- Share URLs encode properly
- Open in new window
- Include proper tracking parameters

URL Structure (Strict/Expert Mode)

URL Length (Warning: 5)

# Check: URL < 75 characters for optimal display
example.com/very/long/url/path/that/goes/on/forever # ❌ > 75 chars
example.com/short-page # ✅ Concise


Hyphens vs Underscores (Notice: 4)

# Check: Hyphens preferred over underscores
example.com/my_page # ❌ Underscores
example.com/my-page # ✅ Hyphens (SEO-friendly)


Keywords in URL (Notice: 5)

# Check: Descriptive URLs with keywords
example.com/p=123 # ❌ No keywords
example.com/running-shoes-men # ✅ Descriptive

Local SEO (Expert Mode)

NAP Consistency (Warning: 8)

# Check: Name, Address, Phone consistent across pages
# Issues:
Footer: "123 Main St"
Contact: "123 Main Street" # ❌ Inconsistent

# All pages should match exactly


Geo Metadata (Warning: 6)

<!-- Check: Geographic targeting -->
<meta name="geo.region" content="US-CA">
<meta name="geo.placename" content="San Francisco">
<meta name="geo.position" content="37.774929;-122.419415">


Local Business Schema (Warning: 7)

{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Business Name",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Main St",
    "addressLocality": "San Francisco",
    "addressRegion": "CA",
    "postalCode": "94102"
  },
  "telephone": "+1-415-555-0100"
}

Video SEO (Expert Mode)

VideoObject Schema (Warning: 7)

{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "Video Title",
  "description": "Video description",
  "thumbnailUrl": "https://example.com/thumbnail.jpg",
  "uploadDate": "2024-01-15",
  "duration": "PT2M30S"
}


Video Accessibility (Error: 8)

<!-- Check: Captions, transcripts -->
<video>
  <source src="video.mp4">
  <track kind="captions" src="captions.vtt"> <!-- ✅ Captions -->
</video>

Dead Code Detection (Expert Mode)

Unused Imports (Notice: 4)

// Check: Imported but never used
import { unused } from 'library'; // ❌ Never referenced
import { used } from 'library'; 
const result = used(); // ✅ Used


Unreachable Code (Warning: 6)

// Check: Code after return/throw
function example() {
  return true;
  console.log("Never runs"); // ❌ Unreachable
}


Duplicate Code (Notice: 5)

# Check: Identical code blocks > 5 lines
# Suggest: Extract to shared function

Code Consistency (Expert Mode)

Naming Conventions (Notice: 4)

// Check: Consistent camelCase, PascalCase, snake_case
const user_name = ""; // ❌ Inconsistent with camelCase
const userName = ""; // ✅ Consistent


File Organization (Notice: 3)

# Check: Similar files grouped logically
/components/Button.jsx
/styles/button.css # ❌ Separated
/components/Button.jsx
/components/Button.css # ✅ Co-located

Report Output

Generate a comprehensive report with:

1. Health Score (0-100)
Overall Score: 73/100 🟡

Calculation:
- Critical errors: -5 points each
- Warnings: -2 points each
- Notices: -0.5 points each

2. Category Breakdown
📊 Category Scores:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SEO               ████████░░ 82/100
Technical         ██████░░░░ 65/100
Performance       ███████░░░ 71/100
Security          █████░░░░░ 54/100 ⚠️
Accessibility     ████████░░ 78/100
UX                ███████░░░ 73/100
Content           ████████░░ 81/100

3. Issue Summary
🔴 Critical (10): 3 issues
🟡 Warnings (7-9): 12 issues
🔵 Notices (1-6): 8 issues

Top Priority Fixes:
1. [Error-10] Leaked API keys in config.js
2. [Error-10] Missing HTTPS on checkout flow
3. [Error-9] 15 broken internal links

4. Detailed Findings
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔴 SECURITY: Leaked Secrets (Error, Rank: 10)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Issue: Hardcoded API key found in codebase
File: src/config.js:12
Code:
  const API_KEY = "sk-1234567890abcdef";

Fix:
  const API_KEY = process.env.API_KEY;

Impact: Critical security vulnerability
Priority: Fix immediately
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

5. Actionable Recommendations
Quick Wins (< 1 hour):
✓ Add missing alt text to 8 images
✓ Fix 3 broken internal links
✓ Add viewport meta tag to mobile.html

High Impact (1-4 hours):
✓ Implement HTTPS across all pages
✓ Add security headers to server config
✓ Optimize 12 large images to WebP

Strategic (> 4 hours):
✓ Implement comprehensive Schema.org markup
✓ Build XML sitemap and submit to GSC
✓ Conduct full accessibility audit and remediation

6. Files Analyzed
Total Files: 247
Analyzed: 189
Skipped: 58 (node_modules, .git, build artifacts)

File Types:
- HTML: 34 files
- CSS: 28 files
- JavaScript: 67 files
- Images: 45 files
- Other: 15 files

Output Format

Always use concise examples rather than verbose explanations. Show code snippets with ❌ (bad) and ✅ (good) examples.

Issue template:

[Severity-Rank] Category: Issue Title
File: path/to/file.ext:line
Problem: Brief description
Example: Code snippet
Fix: Corrected code
Impact: User/SEO/Security impact
Priority: When to fix

Severity Levels
Error (10): Critical issues that break functionality or pose security risks
Error (9): Major issues affecting SEO, accessibility, or user experience
Error (8): Serious issues with measurable impact
Warning (7-8): Important but not critical
Warning (6-7): Moderate impact
Warning (5-6): Minor improvements
Notice (4-5): Best practices
Notice (1-3): Optional enhancements
Tech Stack Detection

Auto-detect framework/CMS and apply specific rules:

React: Check hooks, component structure, prop-types
Next.js: Check SSR/SSG, routing, Image component
WordPress: Check theme functions, plugins, database queries
Vue: Check composition API, reactivity
Django/Flask: Check templates, ORM queries, middleware
Execution Notes
Prefer concise examples over verbose explanations
Show visual indicators: ❌ ✅ 🔴 🟡 🔵
Provide immediate actionable fixes
Rank issues by business impact
Include estimated fix time
Cross-reference related issues
Detect patterns (e.g., all images missing alt text)
Suggest batch fixes when applicable
Git Integration (PR Mode)
# Get uncommitted changes
git status --porcelain
git diff HEAD

# Analyze only:
- Modified files (M)
- Added files (A)
- Renamed files (R)

# Compare with main branch
git diff main...HEAD

File Exclusions

Always skip:

node_modules/
.git/
dist/, build/, .next/
vendor/
*.min.js, *.min.css
package-lock.json, yarn.lock
Binary files (images analyzed separately)
Final Report Structure
# Codebase Audit Report

**Mode**: [Normal/Strict/Expert]
**Type**: [Complete Audit/PR Review]
**Date**: YYYY-MM-DD
**Files Analyzed**: N

## Executive Summary
[Overall score, top issues, quick wins]

## Health Score: XX/100
[Visual score breakdown]

## Critical Issues (Fix Immediately)
[Top 5 errors ranked 9-10]

## Important Issues (Fix Soon)
[Warnings ranked 7-8]

## Recommendations (Improve Over Time)
[Notices and strategic improvements]

## Category Details
[Detailed breakdown by category]

## Appendix
[Full file list, methodology, tool versions]

Weekly Installs
9
Repository
zeal422/dev-too…lt-by-vm
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail
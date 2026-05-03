---
title: diagnose-seo
url: https://skills.sh/calm-north/seojuice-skills/diagnose-seo
---

# diagnose-seo

skills/calm-north/seojuice-skills/diagnose-seo
diagnose-seo
Installation
$ npx skills add https://github.com/calm-north/seojuice-skills --skill diagnose-seo
Summary

Structured technical SEO diagnostic framework organized by crawlability, indexability, renderability, and signals.

Diagnoses four interdependent layers in order: crawlability (robots.txt, sitemaps, site architecture, server response), indexability (meta robots, canonical tags, duplicate content), renderability (JavaScript rendering, content visibility), and signals (titles, descriptions, headings, structured data, hreflang)
Provides specific checklists for each diagnostic area, including common mistakes and validation steps
Outputs findings in a prioritized table format with severity levels, affected pages, and recommended fixes
Covers multilingual sites, paginated content, and JavaScript-heavy pages; excludes Core Web Vitals (see audit-speed skill instead)
SKILL.md
Diagnose SEO

Structured diagnostic framework for crawl issues, canonicalization errors, indexation problems, and rendering failures.

Diagnostic Approach

Technical SEO problems fall into four categories. Diagnose in this order — each layer depends on the previous one working correctly:

Crawlability — Can search engines find and access the pages?
Indexability — Are the pages allowed to be indexed?
Renderability — Can search engines see the full content?
Signals — Are the right signals (titles, structured data, links) in place?
Layer 1: Crawlability

Check these in order:

robots.txt
Fetch [domain]/robots.txt and review the rules
Look for overly broad Disallow rules blocking important paths
Verify Sitemap: directive points to the correct sitemap URL
Check for different rules per user-agent (Googlebot vs others)

Common mistakes:

Disallow: / blocking the entire site (often left from staging)
Blocking CSS/JS files that Googlebot needs for rendering
Blocking API or AJAX endpoints that load dynamic content
Staging robots.txt accidentally deployed to production
XML Sitemap
Fetch the sitemap URL(s) and check:
Does it return 200? Is it valid XML?
Does it list all important pages?
Does it exclude pages that shouldn't be indexed (404s, redirects, noindex pages)?
Are <lastmod> dates accurate and recent?
For large sites: is there a sitemap index?
Site Architecture
Pages should be reachable within 3 clicks from the homepage
Check for orphan pages (no internal links pointing to them)
Check for redirect chains (page A → B → C — should be A → C)
Check for redirect loops
Server Response
Do all important pages return HTTP 200?
Check for unexpected 301/302 redirects
Check for soft 404s (page returns 200 but shows "not found" content)
Verify HTTPS is enforced (HTTP should 301 to HTTPS)
Layer 2: Indexability
Meta Robots / X-Robots-Tag
Check for <meta name="robots" content="noindex"> on pages that should be indexed
Check HTTP headers for X-Robots-Tag: noindex
Common cause: CMS accidentally applying noindex to pagination, tag pages, or new pages
Canonical Tags
Every page should have a <link rel="canonical"> pointing to itself (self-referencing canonical)
Check for canonical tags pointing to wrong pages (common in paginated content, filtered URLs)
Check for conflicting signals: canonical says page A, but noindex is set, or the page redirects

Canonical diagnosis checklist:

 Does the canonical URL match the actual URL?
 Is the canonical URL accessible (returns 200)?
 Does the canonical URL have the same content?
 Is there only one canonical tag on the page?
Duplicate Content
Check for the same content accessible at multiple URLs:
With and without trailing slash (/page vs /page/)
With and without www (example.com vs www.example.com)
HTTP vs HTTPS
URL parameters creating duplicate pages (?sort=price, ?page=1)
Each duplicate set needs one canonical URL; all others should redirect or use canonical tags
Layer 3: Renderability
JavaScript Rendering
Does the page content appear in the raw HTML source? Or is it loaded via JavaScript?
If JS-rendered: does Googlebot see the full content? (Use URL Inspection tool in Search Console)
Check for content hidden behind click events, tabs, or accordions
Check for lazy-loaded content that only appears on scroll
Core Content Visibility
Is the main content in the initial HTML? Or loaded async after page load?
Are important elements (titles, headings, product details) in the DOM on first render?
Check for content that requires login or cookies to view
Layer 4: Signals
Title Tags
Every page has a unique <title>
Title includes the primary keyword
Under 60 characters (to avoid truncation in SERPs)
Descriptive and click-worthy
Meta Descriptions
Every important page has a meta description
150-160 characters
Includes target keyword and a value proposition
Unique per page
Heading Structure
One H1 per page containing the primary keyword
Logical heading hierarchy (H1 → H2 → H3, no skips)
Headings describe section content (not decorative)
Structured Data
Check for JSON-LD structured data appropriate to the page type
Validate with Google's Rich Results Test
Common types: Article, Product, FAQ, HowTo, BreadcrumbList, Organization
Hreflang (multilingual sites)
Check for correct hreflang tags linking language variants
Verify reciprocal tags (page A points to B, B points back to A)
Check for x-default tag
Output Format
Technical SEO Diagnosis: [domain]

Summary

Critical issues: [count]
Warnings: [count]
Passed checks: [count]

Findings by Layer

For each issue found:

Layer	Issue	Severity	Affected Pages	Fix
Crawlability	robots.txt blocks /blog/	Critical	All blog pages	Remove Disallow: /blog/ from robots.txt
Indexability	Missing canonical tags	Warning	15 pages	Add self-referencing canonicals
...	...	...	...	...

Priority Fix List

Ordered by impact:

[Critical fix] — affects [n] pages, blocks [crawling/indexing/ranking]
[Warning fix] — affects [n] pages, reduces [signal quality]
...

Pro Tip: Run the free SEO Audit for a quick technical check, the Broken Link Checker to find dead links, and the Robots.txt Generator to fix crawl directives. SEOJuice MCP users can run /seojuice:site-health for a full technical report and /seojuice:page-audit [domain] [url] to drill into specific pages.

Weekly Installs
1.7K
Repository
calm-north/seoj…e-skills
GitHub Stars
7
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
---
title: seo-optimizer
url: https://skills.sh/ailabs-393/ai-labs-claude-skills/seo-optimizer
---

# seo-optimizer

skills/ailabs-393/ai-labs-claude-skills/seo-optimizer
seo-optimizer
Installation
$ npx skills add https://github.com/ailabs-393/ai-labs-claude-skills --skill seo-optimizer
SKILL.md
SEO Optimizer
Overview

This skill provides comprehensive SEO optimization capabilities for HTML/CSS websites. It analyzes websites for SEO issues, implements best practices, and generates optimization reports covering all critical SEO aspects including meta tags, heading structure, image optimization, schema markup, mobile optimization, and technical SEO.

When to Use This Skill

Use this skill when the user requests:

"Analyze my website for SEO issues"
"Optimize this page for SEO"
"Generate an SEO audit report"
"Fix SEO problems on my website"
"Add proper meta tags to my pages"
"Implement schema markup"
"Generate a sitemap"
"Improve my site's search engine rankings"
Any task related to search engine optimization for HTML/CSS websites
Workflow
1. Initial SEO Analysis

Start with comprehensive analysis using the SEO analyzer script:

python scripts/seo_analyzer.py <directory_or_file>


This script analyzes HTML files and generates a detailed report covering:

Title tags (length, presence, uniqueness)
Meta descriptions (length, presence)
Heading structure (H1-H6 hierarchy)
Image alt attributes
Open Graph tags
Twitter Card tags
Schema.org markup
HTML lang attribute
Viewport and charset meta tags
Canonical URLs
Content length

Output Options:

Default: Human-readable text report with issues, warnings, and good practices
--json: Machine-readable JSON format for programmatic processing

Example Usage:

# Analyze single file
python scripts/seo_analyzer.py index.html

# Analyze entire directory
python scripts/seo_analyzer.py ./public

# Get JSON output
python scripts/seo_analyzer.py ./public --json

2. Review Analysis Results

The analyzer categorizes findings into three levels:

Critical Issues (🔴) - Fix immediately:

Missing title tags
Missing meta descriptions
Missing H1 headings
Images without alt attributes
Missing HTML lang attribute

Warnings (⚠️) - Fix soon for optimal SEO:

Suboptimal title/description lengths
Multiple H1 tags
Missing Open Graph or Twitter Card tags
Missing viewport meta tag
Missing schema markup
Heading hierarchy issues

Good Practices (✅) - Already optimized:

Properly formatted elements
Correct lengths
Present required tags
3. Prioritize and Fix Issues

Address issues in priority order:

Priority 1: Critical Issues

Missing or Poor Title Tags:

<!-- Add unique, descriptive title to <head> -->
<title>Primary Keyword - Secondary Keyword | Brand Name</title>

Keep 50-60 characters
Include target keywords at the beginning
Make unique for each page

Missing Meta Descriptions:

<!-- Add compelling description to <head> -->
<meta name="description" content="Clear, concise description that includes target keywords and encourages clicks. 150-160 characters.">


Missing H1 or Multiple H1s:

Ensure exactly ONE H1 per page
H1 should describe the main topic
Should match or relate to title tag

Images Without Alt Text:

<!-- Add descriptive alt text to all images -->
<img src="image.jpg" alt="Descriptive text explaining image content">


Missing HTML Lang Attribute:

<!-- Add to opening <html> tag -->
<html lang="en">

Priority 2: Important Optimizations

Viewport Meta Tag (critical for mobile SEO):

<meta name="viewport" content="width=device-width, initial-scale=1.0">


Charset Declaration:

<meta charset="UTF-8">


Open Graph Tags (for social media sharing):

<meta property="og:title" content="Your Page Title">
<meta property="og:description" content="Your page description">
<meta property="og:image" content="https://example.com/image.jpg">
<meta property="og:url" content="https://example.com/page-url">
<meta property="og:type" content="website">


Twitter Card Tags:

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Your Page Title">
<meta name="twitter:description" content="Your page description">
<meta name="twitter:image" content="https://example.com/image.jpg">


Canonical URL:

<link rel="canonical" href="https://example.com/preferred-url">

Priority 3: Advanced Optimization

Schema Markup - Refer to references/schema_markup_guide.md for detailed implementation. Common types:

Organization (homepage)
Article/BlogPosting (blog posts)
LocalBusiness (local businesses)
Breadcrumb (navigation)
FAQ (FAQ pages)
Product (e-commerce)

Example implementation:

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Article Title",
  "author": {
    "@type": "Person",
    "name": "Author Name"
  },
  "datePublished": "2024-01-15",
  "image": "https://example.com/image.jpg"
}
</script>

4. Generate or Update Sitemap

After fixing issues, generate an XML sitemap:

python scripts/generate_sitemap.py <directory> <base_url> [output_file]


Example:

# Generate sitemap for website
python scripts/generate_sitemap.py ./public https://example.com

# Specify output location
python scripts/generate_sitemap.py ./public https://example.com ./public/sitemap.xml


The script:

Automatically finds all HTML files
Generates proper URLs
Includes lastmod dates
Estimates priority and changefreq values
Creates properly formatted XML sitemap

After generation:

Upload sitemap.xml to website root
Add reference to robots.txt
Submit to Google Search Console and Bing Webmaster Tools
5. Update robots.txt

Use the template from assets/robots.txt and customize:

User-agent: *
Allow: /

# Block sensitive directories
Disallow: /admin/
Disallow: /private/

# Reference your sitemap
Sitemap: https://yourdomain.com/sitemap.xml


Place robots.txt in website root directory.

6. Verify and Test

After implementing fixes:

Local Testing:

Run the SEO analyzer again to verify fixes
Check that all critical issues are resolved
Ensure no new issues were introduced

Online Testing:

Deploy changes to production
Test with Google Rich Results Test: https://search.google.com/test/rich-results
Validate schema markup: https://validator.schema.org/
Check mobile-friendliness: https://search.google.com/test/mobile-friendly
Monitor in Google Search Console
7. Ongoing Optimization

Regular maintenance:

Update sitemap when adding new pages
Keep meta descriptions fresh and compelling
Ensure new images have alt text
Add schema markup to new content types
Monitor Search Console for issues
Update content regularly
Common Optimization Patterns
Pattern 1: New Website Setup

For a brand new HTML/CSS website:

Run initial analysis: python scripts/seo_analyzer.py ./public
Add essential meta tags to all pages (title, description, viewport)
Ensure proper heading structure (one H1 per page)
Add alt text to all images
Implement organization schema on homepage
Generate sitemap: python scripts/generate_sitemap.py ./public https://yourdomain.com
Create robots.txt from template
Deploy and submit sitemap to search engines
Pattern 2: Existing Website Audit

For an existing website needing optimization:

Run comprehensive analysis: python scripts/seo_analyzer.py ./public
Identify and prioritize issues (critical first)
Fix critical issues across all pages
Add missing Open Graph and Twitter Card tags
Implement schema markup for appropriate pages
Regenerate sitemap with updates
Verify fixes with analyzer
Deploy and monitor
Pattern 3: Single Page Optimization

For optimizing a specific page:

Analyze specific file: python scripts/seo_analyzer.py page.html
Fix identified issues
Optimize title and meta description for target keywords
Ensure proper heading hierarchy
Add appropriate schema markup for page type
Verify with analyzer
Update sitemap if new page
Pattern 4: Blog Post Optimization

For blog posts and articles:

Ensure unique title (50-60 chars) with target keyword
Write compelling meta description (150-160 chars)
Use single H1 for article title
Implement proper H2/H3 hierarchy for sections
Add alt text to all images
Implement Article or BlogPosting schema (see references/schema_markup_guide.md)
Add Open Graph and Twitter Card tags for social sharing
Include author information
Add breadcrumb schema for navigation
Reference Materials
Detailed Guides

references/seo_checklist.md: Comprehensive checklist covering all SEO aspects:

Title tags and meta descriptions guidelines
Heading structure best practices
Image optimization techniques
URL structure recommendations
Internal linking strategies
Page speed optimization
Mobile optimization requirements
Semantic HTML usage
Complete technical SEO checklist

Reference this for detailed specifications on any SEO element.

references/schema_markup_guide.md: Complete guide for implementing schema.org structured data:

JSON-LD implementation (recommended format)
10+ common schema types with examples
Organization, LocalBusiness, Article, BlogPosting, FAQ, Product, etc.
Required properties for each type
Best practices and common mistakes
Validation tools and resources

Reference this when implementing schema markup for any content type.

Scripts

scripts/seo_analyzer.py: Python script for automated SEO analysis. Analyzes HTML files for common issues and generates detailed reports. Can output text or JSON format. Deterministic and reliable for repeated analysis.

scripts/generate_sitemap.py: Python script for generating XML sitemaps. Automatically crawls directories, estimates priorities and change frequencies, and generates properly formatted sitemaps ready for submission to search engines.

Assets

assets/robots.txt: Template robots.txt file with common configurations and comments. Customize for specific needs and place in website root directory.

Key Principles

User-First: Optimize for users first, search engines second. Good user experience leads to better SEO.

Unique Content: Every page should have unique title, description, and H1. Duplicate content hurts SEO.

Mobile-First: Google uses mobile-first indexing. Always include viewport meta tag and ensure mobile responsiveness.

Accessibility = SEO: Accessible websites (alt text, semantic HTML, proper headings) rank better.

Quality Over Quantity: Substantial, valuable content ranks better than thin content. Aim for comprehensive pages.

Technical Foundation: Fix critical technical issues (missing tags, broken structure) before advanced optimization.

Structured Data: Schema markup helps search engines understand content and can lead to rich results.

Regular Updates: SEO is ongoing. Keep content fresh, monitor analytics, and adapt to algorithm changes.

Natural Language: Write for humans using natural language. Avoid keyword stuffing.

Validation: Always validate changes with testing tools before deploying to production.

Tips for Maximum Impact
Start with critical issues: Fix missing title tags and meta descriptions first - these have the biggest impact
Be consistent: Apply optimizations across all pages, not just homepage
Use semantic HTML: Use proper HTML5 semantic tags (<header>, <nav>, <main>, <article>, <aside>, <footer>)
Optimize images: Compress images, use descriptive filenames, always include alt text
Internal linking: Link to related pages with descriptive anchor text
Page speed matters: Fast-loading pages rank better
Test on mobile: Majority of searches are mobile - ensure excellent mobile experience
Monitor Search Console: Use Google Search Console to track performance and identify issues
Update regularly: Fresh content signals active, valuable websites
Quick Reference Commands
# Analyze single file
python scripts/seo_analyzer.py index.html

# Analyze entire website
python scripts/seo_analyzer.py ./public

# Generate sitemap
python scripts/generate_sitemap.py ./public https://example.com

# Get JSON analysis output
python scripts/seo_analyzer.py ./public --json

Weekly Installs
757
Repository
ailabs-393/ai-l…e-skills
GitHub Stars
357
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
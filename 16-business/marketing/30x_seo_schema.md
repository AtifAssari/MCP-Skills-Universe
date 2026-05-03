---
title: 30x-seo-schema
url: https://skills.sh/norahe0304-art/30x-seo/30x-seo-schema
---

# 30x-seo-schema

skills/norahe0304-art/30x-seo/30x-seo-schema
30x-seo-schema
Installation
$ npx skills add https://github.com/norahe0304-art/30x-seo --skill 30x-seo-schema
SKILL.md
Schema Markup Analysis & Generation
Detection
Scan page source for JSON-LD <script type="application/ld+json">
Check for Microdata (itemscope, itemprop)
Check for RDFa (typeof, property)
Always recommend JSON-LD as primary format (Google's stated preference)
Validation
Check required properties per schema type
Validate against Google's supported rich result types
Test for common errors:
Missing @context
Invalid @type
Wrong data types
Placeholder text
Relative URLs (should be absolute)
Invalid date formats
Flag deprecated types (see below)
Schema Type Status (as of Feb 2026)

Read references/schema-types.md for the full list. Key rules:

ACTIVE — recommend freely:

Organization, LocalBusiness, SoftwareApplication, WebApplication, Product (with Certification markup as of April 2025), ProductGroup, Offer, Service, Article, BlogPosting, NewsArticle, Review, AggregateRating, BreadcrumbList, WebSite, WebPage, Person, ProfilePage, ContactPage, VideoObject, ImageObject, Event, JobPosting, Course, DiscussionForumPosting

VIDEO & SPECIALIZED — recommend freely:

BroadcastEvent, Clip, SeekToAction, SoftwareSourceCode

See schema/templates.json for ready-to-use JSON-LD templates for these types.

JSON-LD and JavaScript rendering: Per Google's December 2025 JS SEO guidance, structured data injected via JavaScript may face delayed processing. For time-sensitive markup (especially Product, Offer), include JSON-LD in the initial server-rendered HTML.

RESTRICTED — only for specific sites:
FAQ: ONLY for government and healthcare authority sites (restricted Aug 2023)
DEPRECATED — never recommend:
HowTo: Rich results removed September 2023
SpecialAnnouncement: Deprecated July 31, 2025
CourseInfo, EstimatedSalary, LearningVideo: Retired June 2025
ClaimReview: Retired from rich results June 2025
VehicleListing: Retired from rich results June 2025
Practice Problem: Retired from rich results late 2025
Dataset: Retired from rich results late 2025
Book Actions: Deprecated then reversed — still functional as of Feb 2026 (historical note)
Generation

When generating schema for a page:

Identify page type from content analysis
Select appropriate schema type(s)
Generate valid JSON-LD with all required + recommended properties
Include only truthful, verifiable data — use placeholders clearly marked for user to fill
Validate output before presenting
Common Schema Templates
Organization
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "[Company Name]",
  "url": "[Website URL]",
  "logo": "[Logo URL]",
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "[Phone]",
    "contactType": "customer service"
  },
  "sameAs": [
    "[Facebook URL]",
    "[LinkedIn URL]",
    "[Twitter URL]"
  ]
}

LocalBusiness
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "[Business Name]",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[Street]",
    "addressLocality": "[City]",
    "addressRegion": "[State]",
    "postalCode": "[ZIP]",
    "addressCountry": "US"
  },
  "telephone": "[Phone]",
  "openingHours": "Mo-Fr 09:00-17:00",
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "[Lat]",
    "longitude": "[Long]"
  }
}

Article/BlogPosting
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "[Title]",
  "author": {
    "@type": "Person",
    "name": "[Author Name]"
  },
  "datePublished": "[YYYY-MM-DD]",
  "dateModified": "[YYYY-MM-DD]",
  "image": "[Image URL]",
  "publisher": {
    "@type": "Organization",
    "name": "[Publisher]",
    "logo": {
      "@type": "ImageObject",
      "url": "[Logo URL]"
    }
  }
}

Output
SCHEMA-REPORT.md — detection and validation results
generated-schema.json — ready-to-use JSON-LD snippets
Validation Results
Schema	Type	Status	Issues
...	...	✅/⚠️/❌	...
Recommendations
Missing schema opportunities
Validation fixes needed
Generated code for implementation

[PROTOCOL]: Update this header on changes, then check CLAUDE.md

Weekly Installs
33
Repository
norahe0304-art/30x-seo
GitHub Stars
27
First Seen
Mar 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
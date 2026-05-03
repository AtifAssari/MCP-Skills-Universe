---
title: optimise-seo
url: https://skills.sh/mblode/agent-skills/optimise-seo
---

# optimise-seo

skills/mblode/agent-skills/optimise-seo
optimise-seo
Installation
$ npx skills add https://github.com/mblode/agent-skills --skill optimise-seo
SKILL.md
Optimise SEO

No visual redesigns or layout changes. Allowed: metadata, structured data, semantic HTML, internal links, alt text, sitemap/robots, performance tuning.

Workflow

Copy and track this checklist:

SEO progress:
- [ ] Step 1: Inventory routes and index intent
- [ ] Step 2: Fix crawl/index foundations
- [ ] Step 3: Implement metadata + structured data
- [ ] Step 4: Improve semantics, links, and CWV
- [ ] Step 5: Validate with seo-checklist.md and document changes

Inventory routes and index intent
Fix crawl/index foundations
Implement metadata + structured data
Improve semantics, links, and CWV
Validate with seo-checklist.md and document changes
Must-have
Sitemap (app/sitemap.ts) and robots (app/robots.ts):
// app/sitemap.ts
import type { MetadataRoute } from "next";
export default function sitemap(): MetadataRoute.Sitemap {
  return [{ url: "https://example.com", lastModified: new Date() }];
}

Canonicals consistent on every page
Unique titles + descriptions via metadata or generateMetadata
OpenGraph + Twitter Card tags
JSON-LD: Organization, WebSite, BreadcrumbList (+ Article/Product/FAQ as needed):
<script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify({
  "@context": "https://schema.org", "@type": "Organization",
  name: "Example", url: "https://example.com"
}) }} />

One h1 and logical heading hierarchy
Alt text, internal links, CWV targets, mobile/desktop parity
Programmatic SEO (pages at scale)
Validate demand for a repeatable pattern before generating pages
Require unique value per page and defensible data
Clean subfolder URLs, hubs/spokes, and breadcrumbs
Index only strong pages; monitor indexation and cannibalization
SEO audit (triage order)
Crawl/index: robots, sitemap, noindex, canonicals, redirects, soft 404s
Technical: HTTPS, CWV, mobile parity
On-page/content: titles/H1, internal links, remove or noindex thin pages
Gotchas
Don't over-generate thin or doorway pages — indexation drops and quality signals suffer.
Don't omit canonicals or let them conflict across variants (trailing slash, www, uppercase) — search engines split ranking signal.
Don't block crawlers unintentionally via robots.txt, noindex, or auth walls on routes meant to be indexed.
Don't rely on JS-only rendering without SSR/SSG for indexable content.
Don't change URLs without 301 redirects — link equity and crawl budget are lost.
Don't add JSON-LD that doesn't match visible page content — Google treats this as spam and may demote the page.
Resources
nextjs-implementation.md — implementation patterns for steps 2-4
seo-checklist.md — pass/fail validation during step 5
Validation
Check HTTP response headers for correct status codes and redirects
Confirm robots.txt has correct crawl directives
Confirm sitemap.xml lists all indexed routes with valid URLs
Verify pages include canonical, OpenGraph, and Twitter Card tags in source HTML
Run a Lighthouse audit and confirm performance scores meet targets
Validate JSON-LD with Rich Results Test per URL
Report remaining blockers with exact URLs and owner/action
Weekly Installs
199
Repository
mblode/agent-skills
GitHub Stars
35
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
---
rating: ⭐⭐⭐
title: pseo-schema
url: https://skills.sh/lisbeth718/pseo-skills/pseo-schema
---

# pseo-schema

skills/lisbeth718/pseo-skills/pseo-schema
pseo-schema
Installation
$ npx skills add https://github.com/lisbeth718/pseo-skills --skill pseo-schema
SKILL.md
pSEO Schema Markup

Implement JSON-LD structured data that gives search engines explicit semantic understanding of every programmatic page.

Core Principles
JSON-LD format: Always use JSON-LD, not Microdata or RDFa
Context-appropriate types: Match schema type to the page's actual content
Data-driven generation: Schema is built from the same data that drives the page
Valid and complete: Every schema block must pass Google's Rich Results Test
No fabrication: Only include fields backed by real data
Baseline Schema (Every Page)

Every pSEO page should include these foundational types:

WebSite — once per site (on the homepage or via a shared layout), declares site-level search and name
WebPage — on every page, declares the page URL, name, description, and dateModified
BreadcrumbList — on every page with navigation hierarchy

These are in addition to the content-specific types below.

Schema Types by Page Context
Page Type	Primary Schema	Supporting Schema
Content/article page	Article	BreadcrumbList, FAQPage, WebPage
Product page	Product	BreadcrumbList, AggregateRating, WebPage
FAQ/Q&A page	FAQPage	BreadcrumbList, WebPage
How-to/tutorial page	HowTo	BreadcrumbList, FAQPage, WebPage
Category/hub page	CollectionPage	BreadcrumbList, ItemList, WebPage
Local/location page	LocalBusiness	BreadcrumbList, FAQPage, WebPage
Implementation Steps
1. Create Schema Generator Functions

Build a module of pure functions that produce schema objects from page data:

// lib/schema.ts

export function generateArticleSchema(data: PageData, url: string) {
  return {
    "@context": "https://schema.org",
    "@type": "Article",
    headline: data.h1,
    description: data.metaDescription,
    url,
    datePublished: data.publishedDate,
    dateModified: data.lastModified,
    author: { "@type": "Organization", name: "..." },
    publisher: { "@type": "Organization", name: "..." },
  };
}

// IMPORTANT: FAQPage schema is ONLY valid when the FAQ content is
// visible on the page itself. Google requires the questions and answers
// to be present in the rendered HTML, not just in the JSON-LD.
// Never add FAQPage schema to a page that does not render the FAQs.
export function generateFAQSchema(faqs: FAQ[]) {
  if (!faqs?.length) return null;
  return {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    mainEntity: faqs.map((faq) => ({
      "@type": "Question",
      name: faq.question,
      acceptedAnswer: {
        "@type": "Answer",
        text: faq.answer,
      },
    })),
  };
}

export function generateWebPageSchema(data: PageData, url: string) {
  return {
    "@context": "https://schema.org",
    "@type": "WebPage",
    name: data.title,
    description: data.metaDescription,
    url,
    dateModified: data.lastModified,
  };
}

export function generateBreadcrumbSchema(
  items: { name: string; url: string }[]
) {
  return {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    itemListElement: items.map((item, i) => ({
      "@type": "ListItem",
      position: i + 1,
      name: item.name,
      item: item.url,
    })),
  };
}

2. Create the Schema Renderer Component

Build a reusable component that injects JSON-LD into the page head:

export function JsonLd({ data }: { data: Record<string, unknown> | null }) {
  if (!data) return null;
  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(data) }}
    />
  );
}

3. Compose Schema per Page

Each page template composes its schema from multiple generators:

// In the page component
const schemas = [
  generateArticleSchema(data, canonicalUrl),
  generateBreadcrumbSchema(breadcrumbItems),
  data.faqs?.length ? generateFAQSchema(data.faqs) : null,
].filter(Boolean);

// Render each as a separate script tag
{schemas.map((schema, i) => <JsonLd key={i} data={schema} />)}

4. Schema Field Rules

Required fields per type:

Article: headline, url, datePublished, dateModified, author, publisher
FAQPage: mainEntity with at least 1 Question/Answer pair
BreadcrumbList: itemListElement with position, name, item
Product: name, description; offers or review if available
HowTo: name, step (with text for each step)

Field integrity rules:

headline must match the page's H1 or title
url must match the canonical URL
dateModified must be a valid ISO 8601 date
Never include empty strings or placeholder values
Never include fields with fabricated data (e.g., fake reviews)
5. Handle Multiple Schema Types

A single page can have multiple schema blocks. Render them as separate <script type="application/ld+json"> tags, not as an array in one tag (for maximum compatibility).

Validation

Schema must:

Pass Google's Rich Results Test (https://search.google.com/test/rich-results)
Pass Schema.org validation
Not include deprecated properties
Not include fields with empty or placeholder values
Use absolute URLs, not relative paths
6. E-E-A-T Schema Support

Google's 2025 updates weight Experience, Expertise, Authoritativeness, and Trustworthiness heavily. Schema markup can reinforce these signals:

Author/Organization schema on every page:

export function generateAuthorSchema(author: AuthorInfo) {
  return {
    "@context": "https://schema.org",
    "@type": author.type === "person" ? "Person" : "Organization",
    name: author.name,
    url: author.url,
    ...(author.credentials && { jobTitle: author.credentials }),
    ...(author.sameAs && { sameAs: author.sameAs }),
  };
}


Add author and publisher to Article schema (already included but emphasize this is now critical, not optional).

dateModified must be accurate — Google has increased weighting on freshness signals. Never set dateModified to today's date if the content hasn't actually changed. Use the real last-modified date from the data source.

For YMYL content, additionally include:

reviewedBy on medical/health content (Person with MedicalBusiness or Physician type)
citation or isBasedOn for content derived from authoritative sources
credentialCategory on author's Person schema if applicable
File Organization
lib/
  schema.ts            # all schema generator functions
  schema.test.ts       # validation tests
components/
  JsonLd.tsx           # reusable JSON-LD renderer

Relationship to Other Skills
Depends on: pseo-data (structured fields feed schema generation)
Works with: pseo-templates (schema components are rendered inside page templates)
Breadcrumb data from: pseo-linking (breadcrumb trail structure)
Weekly Installs
11
Repository
lisbeth718/pseo-skills
GitHub Stars
40
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
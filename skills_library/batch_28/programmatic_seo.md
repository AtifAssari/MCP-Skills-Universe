---
title: programmatic-seo
url: https://skills.sh/alexwelcing/copy/programmatic-seo
---

# programmatic-seo

skills/alexwelcing/copy/programmatic-seo
programmatic-seo
Installation
$ npx skills add https://github.com/alexwelcing/copy --skill programmatic-seo
SKILL.md
Programmatic SEO Skill

You are an expert in programmatic SEO. Your goal is to help create scalable SEO strategies through templated, data-driven page generation.

Programmatic SEO Fundamentals
What is Programmatic SEO?

Creating many pages at scale using templates and data, targeting long-tail keywords with similar search intent.

When to Use
Large data sets (cities, products, terms)
Repetitive keyword patterns
Long-tail keyword opportunities
Scalable content structure
Aggregator/marketplace models
Examples
Zapier: "[App] + [App] integrations"
Webflow: "[Type] website template"
Nomad List: "Cost of living in [City]"
G2: "[Product] reviews"
Strategy Development
Step 1: Identify Opportunities

Pattern research:

Find repetitive search queries
"[X] for [Y]"
"[X] in [City]"
"[X] vs [Y]"
"Best [X] for [Use case]"
"[X] [Year]"

Volume assessment:

Individual keyword volume (may be low)
Aggregate volume (many pages × low volume = high total)
Competition level at keyword level
Step 2: Data Source

Internal data:

Product catalog
User-generated content
Usage data
API data

External data:

Public datasets
APIs (cities, companies, etc.)
Scraped data (carefully)
Partnerships

Data requirements:

Unique per page
Valuable to users
Updatable/maintainable
Legally usable
Step 3: Template Design

Essential elements:

Unique H1 with target keyword
Dynamic meta title/description
Structured, templated content
Unique data per page
Internal linking
Schema markup

Quality standards:

Each page must provide real value
Not just keyword stuffing
Useful even without SEO benefit
Better than competing pages
Page Architecture
URL Structure

Pattern: /category/[variable]/

Examples:

/templates/[industry]-website/
/integrations/[app1]-[app2]/
/locations/[city]/
/compare/[product]-vs-[product]/

Best practices:

Short and descriptive
Include target keyword
Avoid parameter strings
Logical hierarchy
Template Components
# [Primary Keyword] - [Value Prop]

## What is [Topic]?
[Templated intro with variables]

## Key Data Points
[Dynamic data section]

## [Use case/benefit 1]
[Templated content]

## [Use case/benefit 2]
[Templated content]

## Related [Items]
[Internal links to related pages]

## FAQ
[Common questions with dynamic answers]

Schema Markup

Apply relevant schema:

Article/BlogPosting
Product
LocalBusiness
FAQ
HowTo
BreadcrumbList
Quality Control
Avoid Thin Content

Red flags:

Pages with just keyword variations
No unique value per page
Duplicate content across pages
No user benefit

Quality checks:

Would you bookmark this page?
Does it answer the search intent?
Is it better than competitors?
Would you share it?
Content Depth

Minimum standards:

300+ words of unique content
Real data/value per page
Useful internal links
Good user experience
Indexation Control

Index: High-value, unique pages Noindex: Low-value, duplicate, thin pages Canonical: Prevent duplication Pagination: Proper rel=next/prev or single pages

Implementation
Build Process
Data collection: Gather all variables
Template creation: Design page layout
Content generation: Create templated copy
Technical setup: URL structure, routing
Schema implementation: Structured data
Internal linking: Connect pages
Quality review: Check sample pages
Launch: Deploy and monitor
Technical Considerations

Static vs Dynamic:

Static: Better performance, easier caching
Dynamic: Real-time data, easier updates

Performance:

Fast page load essential
Efficient database queries
Proper caching
CDN for static assets

Scalability:

Plan for page growth
Efficient sitemap handling
Crawl budget management
Internal Linking
Link Structure

Category pages → Individual pages → Related pages

Strategies:

Related items at bottom
In-content contextual links
Category/hub pages
Breadcrumb navigation
"See also" sections
Hub Pages

Create category pages that link to programmatic pages:

/templates/ → All template pages
/integrations/ → All integration pages
/locations/ → All location pages
Monitoring & Iteration
Metrics to Track

Search performance:

Indexed pages
Ranking keywords
Organic traffic
CTR by template

Page quality:

Bounce rate
Time on page
Conversion rate
User feedback
Iteration Process
Monitor performance by template/segment
Identify top/bottom performers
Improve template based on data
Test new variations
Expand to new keywords/patterns
Common Pitfalls
To Avoid
Thin content: Each page needs real value
Keyword stuffing: Write for users first
Poor UX: Speed and usability matter
Ignoring intent: Match search intent
Over-scaling: Quality over quantity
Neglecting updates: Keep data fresh
Duplicate content: Ensure uniqueness
Output Format

When creating programmatic SEO strategy, provide:

Opportunity analysis with keyword patterns
Data source requirements
Page template design with components
URL structure recommendation
Schema markup specification
Internal linking strategy
Quality guidelines and checks
Implementation roadmap
Related Skills
seo-audit - For overall SEO health
schema-markup - For structured data
copywriting - For template copy
page-cro - For page optimization
Weekly Installs
15
Repository
alexwelcing/copy
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
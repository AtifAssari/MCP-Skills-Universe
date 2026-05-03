---
rating: ⭐⭐⭐
title: seo
url: https://skills.sh/addyosmani/web-quality-skills/seo
---

# seo

skills/addyosmani/web-quality-skills/seo
seo
Installation
$ npx skills add https://github.com/addyosmani/web-quality-skills --skill seo
Summary

Technical SEO optimization covering crawlability, on-page elements, structured data, and mobile best practices.

Addresses crawlability through robots.txt, meta robots tags, canonical URLs, and XML sitemaps with submission guidance
Covers on-page optimization including title tags, meta descriptions, heading hierarchy, image SEO, and internal linking strategies
Provides JSON-LD structured data templates for Organization, Article, Product, FAQ, and Breadcrumb schemas with validation tools
Includes mobile SEO requirements (responsive viewport, tap targets, font sizing) and international SEO via hreflang tags
Offers a tiered audit checklist (critical, high priority, medium priority, ongoing) and references to Google Search Console and Lighthouse
SKILL.md
SEO optimization

Search engine optimization based on Lighthouse SEO audits and Google Search guidelines. Focus on technical SEO, on-page optimization, and structured data.

SEO fundamentals

Search ranking factors (approximate influence):

Factor	Influence	This Skill
Content quality & relevance	~40%	Partial (structure)
Backlinks & authority	~25%	✗
Technical SEO	~15%	✓
Page experience (Core Web Vitals)	~10%	See Core Web Vitals
On-page SEO	~10%	✓
Technical SEO
Crawlability

robots.txt:

# /robots.txt
User-agent: *
Allow: /

# Block admin/private areas
Disallow: /admin/
Disallow: /api/
Disallow: /private/

# Don't block resources needed for rendering
# ❌ Disallow: /static/

Sitemap: https://example.com/sitemap.xml


Meta robots:

<!-- Default: indexable, followable -->
<meta name="robots" content="index, follow">

<!-- Noindex specific pages -->
<meta name="robots" content="noindex, nofollow">

<!-- Indexable but don't follow links -->
<meta name="robots" content="index, nofollow">

<!-- Control snippets -->
<meta name="robots" content="max-snippet:150, max-image-preview:large">


Canonical URLs:

<!-- Prevent duplicate content issues -->
<link rel="canonical" href="https://example.com/page">

<!-- Self-referencing canonical (recommended) -->
<link rel="canonical" href="https://example.com/current-page">

<!-- For paginated content -->
<link rel="canonical" href="https://example.com/products">
<!-- Or use rel="prev" / rel="next" for explicit pagination -->

XML sitemap
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://example.com/</loc>
    <lastmod>2024-01-15</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://example.com/products</loc>
    <lastmod>2024-01-14</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>


Sitemap best practices:

Maximum 50,000 URLs or 50MB per sitemap
Use sitemap index for larger sites
Include only canonical, indexable URLs
Update lastmod when content changes
Submit to Google Search Console
URL structure
✅ Good URLs:
https://example.com/products/blue-widget
https://example.com/blog/how-to-use-widgets

❌ Poor URLs:
https://example.com/p?id=12345
https://example.com/products/item/category/subcategory/blue-widget-2024-sale-discount


URL guidelines:

Use hyphens, not underscores
Lowercase only
Keep short (< 75 characters)
Include target keywords naturally
Avoid parameters when possible
Use HTTPS always
HTTPS & security
<!-- Ensure all resources use HTTPS -->
<img src="https://example.com/image.jpg">

<!-- Not: -->
<img src="http://example.com/image.jpg">


Security headers for SEO trust signals:

Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

On-page SEO
Title tags
<!-- ❌ Missing or generic -->
<title>Page</title>
<title>Home</title>

<!-- ✅ Descriptive with primary keyword -->
<title>Blue Widgets for Sale | Premium Quality | Example Store</title>


Title tag guidelines:

50-60 characters (Google truncates ~60)
Primary keyword near the beginning
Unique for every page
Brand name at end (unless homepage)
Action-oriented when appropriate
Meta descriptions
<!-- ❌ Missing or duplicate -->
<meta name="description" content="">

<!-- ✅ Compelling and unique -->
<meta name="description" content="Shop premium blue widgets with free shipping. 30-day returns. Rated 4.9/5 by 10,000+ customers. Order today and save 20%.">


Meta description guidelines:

150-160 characters
Include primary keyword naturally
Compelling call-to-action
Unique for every page
Matches page content
Heading structure
<!-- ❌ Poor structure -->
<h2>Welcome to Our Store</h2>
<h4>Products</h4>
<h1>Contact Us</h1>

<!-- ✅ Proper hierarchy -->
<h1>Blue Widgets - Premium Quality</h1>
  <h2>Product Features</h2>
    <h3>Durability</h3>
    <h3>Design</h3>
  <h2>Customer Reviews</h2>
  <h2>Pricing</h2>


Heading guidelines:

Single <h1> per page (the main topic)
Logical hierarchy (don't skip levels)
Include keywords naturally
Descriptive, not generic
Image SEO
<!-- ❌ Poor image SEO -->
<img src="IMG_12345.jpg">

<!-- ✅ Optimized image -->
<img src="blue-widget-product-photo.webp"
     alt="Blue widget with chrome finish, side view showing control panel"
     width="800"
     height="600"
     loading="lazy">


Image guidelines:

Descriptive filenames with keywords
Alt text describes the image content
Compressed and properly sized
WebP/AVIF with fallbacks
Lazy load below-fold images
Internal linking
<!-- ❌ Non-descriptive -->
<a href="/products">Click here</a>
<a href="/widgets">Read more</a>

<!-- ✅ Descriptive anchor text -->
<a href="/products/blue-widgets">Browse our blue widget collection</a>
<a href="/guides/widget-maintenance">Learn how to maintain your widgets</a>


Linking guidelines:

Descriptive anchor text with keywords
Link to relevant internal pages
Reasonable number of links per page
Fix broken links promptly
Use breadcrumbs for hierarchy
Structured data (JSON-LD)
Organization
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Example Company",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "sameAs": [
    "https://twitter.com/example",
    "https://linkedin.com/company/example"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+1-555-123-4567",
    "contactType": "customer service"
  }
}
</script>

Article
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How to Choose the Right Widget",
  "description": "Complete guide to selecting widgets for your needs.",
  "image": "https://example.com/article-image.jpg",
  "author": {
    "@type": "Person",
    "name": "Jane Smith",
    "url": "https://example.com/authors/jane-smith"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Example Blog",
    "logo": {
      "@type": "ImageObject",
      "url": "https://example.com/logo.png"
    }
  },
  "datePublished": "2024-01-15",
  "dateModified": "2024-01-20"
}
</script>

Product
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Blue Widget Pro",
  "image": "https://example.com/blue-widget.jpg",
  "description": "Premium blue widget with advanced features.",
  "brand": {
    "@type": "Brand",
    "name": "WidgetCo"
  },
  "offers": {
    "@type": "Offer",
    "price": "49.99",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "url": "https://example.com/products/blue-widget"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "1250"
  }
}
</script>

FAQ
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What colors are available?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Our widgets come in blue, red, and green."
      }
    },
    {
      "@type": "Question",
      "name": "What is the warranty?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "All widgets include a 2-year warranty."
      }
    }
  ]
}
</script>

Breadcrumbs
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://example.com"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Products",
      "item": "https://example.com/products"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Blue Widgets",
      "item": "https://example.com/products/blue-widgets"
    }
  ]
}
</script>

Validation

Test structured data at:

Google Rich Results Test
Schema.org Validator
Mobile SEO
Responsive design
<!-- ❌ Not mobile-friendly -->
<meta name="viewport" content="width=1024">

<!-- ✅ Responsive viewport -->
<meta name="viewport" content="width=device-width, initial-scale=1">

Tap targets
/* ❌ Too small for mobile */
.small-link {
  padding: 4px;
  font-size: 12px;
}

/* ✅ Adequate tap target */
.mobile-friendly-link {
  padding: 12px;
  font-size: 16px;
  min-height: 48px;
  min-width: 48px;
}

Font sizes
/* ❌ Too small on mobile */
body {
  font-size: 10px;
}

/* ✅ Readable without zooming */
body {
  font-size: 16px;
  line-height: 1.5;
}

International SEO
Hreflang tags
<!-- For multi-language sites -->
<link rel="alternate" hreflang="en" href="https://example.com/page">
<link rel="alternate" hreflang="es" href="https://example.com/es/page">
<link rel="alternate" hreflang="fr" href="https://example.com/fr/page">
<link rel="alternate" hreflang="x-default" href="https://example.com/page">

Language declaration
<html lang="en">
<!-- or -->
<html lang="es-MX">

SEO audit checklist
Critical
 HTTPS enabled
 robots.txt allows crawling
 No noindex on important pages
 Title tags present and unique
 Single <h1> per page
High priority
 Meta descriptions present
 Sitemap submitted
 Canonical URLs set
 Mobile-responsive
 Core Web Vitals passing
Medium priority
 Structured data implemented
 Internal linking strategy
 Image alt text
 Descriptive URLs
 Breadcrumb navigation
Ongoing
 Fix crawl errors in Search Console
 Update sitemap when content changes
 Monitor ranking changes
 Check for broken links
 Review Search Console insights
Tools
Tool	Use
Google Search Console	Monitor indexing, fix issues
Google PageSpeed Insights	Performance + Core Web Vitals
Rich Results Test	Validate structured data
Lighthouse	Full SEO audit
Screaming Frog	Crawl analysis
References
Google Search Central
Schema.org
Core Web Vitals
Web Quality Audit
Weekly Installs
20.0K
Repository
addyosmani/web-…y-skills
GitHub Stars
1.8K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
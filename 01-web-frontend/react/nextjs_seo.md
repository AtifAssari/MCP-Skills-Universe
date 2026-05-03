---
rating: ⭐⭐⭐
title: nextjs-seo
url: https://skills.sh/laguagu/claude-code-nextjs-skills/nextjs-seo
---

# nextjs-seo

skills/laguagu/claude-code-nextjs-skills/nextjs-seo
nextjs-seo
Installation
$ npx skills add https://github.com/laguagu/claude-code-nextjs-skills --skill nextjs-seo
Summary

Complete SEO setup for Next.js 16+ apps with metadata, sitemaps, robots.txt, and Core Web Vitals guidance.

Covers essential files (root metadata, dynamic sitemaps, robots configuration) with ready-to-use TypeScript examples for App Router
Includes rendering strategy comparison (SSG, SSR, ISR, CSR) and Core Web Vitals targets (LCP, INP, CLS) for performance optimization
Provides quick audit checklist, common mistakes to avoid, and dynamic metadata patterns for product pages and canonical URLs
References structured data (JSON-LD), troubleshooting guides, and noindex configuration for controlling search engine indexing
SKILL.md
Next.js SEO Optimization

Comprehensive SEO guide for Next.js App Router applications.

Quick SEO Audit

Run this checklist for any Next.js project:

Check robots.txt: curl https://your-site.com/robots.txt
Check sitemap: curl https://your-site.com/sitemap.xml
Check metadata: View page source, search for <title> and <meta name="description">
Check JSON-LD: View page source, search for application/ld+json
Check Core Web Vitals: Run Lighthouse in Chrome DevTools
Essential Files
app/layout.tsx - Root Metadata
import type { Metadata, Viewport } from 'next';

// Viewport must be a separate export — `themeColor`, `colorScheme`, and
// `viewport` inside the `metadata` object are not supported.
export const viewport: Viewport = {
  width: 'device-width',
  initialScale: 1,
  maximumScale: 5,
  userScalable: true,
  themeColor: [
    { media: '(prefers-color-scheme: light)', color: '#ffffff' },
    { media: '(prefers-color-scheme: dark)', color: '#0a0a0a' },
  ],
};

export const metadata: Metadata = {
  metadataBase: new URL('https://your-site.com'),
  title: {
    default: 'Site Title - Main Keyword',
    template: '%s | Site Name',
  },
  description: 'Compelling description with keywords (150-160 chars; Google typically displays this range)',
  keywords: ['keyword1', 'keyword2', 'keyword3'],
  openGraph: {
    type: 'website',
    locale: 'en_US',
    url: 'https://your-site.com',
    siteName: 'Site Name',
    title: 'Site Title',
    description: 'Description for social sharing',
    images: [{ url: '/og-image.png', width: 1200, height: 630, alt: 'Site preview' }],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Site Title',
    description: 'Description for Twitter',
    images: ['/og-image.png'],
  },
  alternates: {
    canonical: '/',
  },
  robots: {
    index: true,
    follow: true,
  },
};

app/sitemap.ts - Dynamic Sitemap
import type { MetadataRoute } from 'next';

export default function sitemap(): MetadataRoute.Sitemap {
  const baseUrl = 'https://your-site.com';

  return [
    {
      url: baseUrl,
      lastModified: new Date(),
      changeFrequency: 'weekly',
      priority: 1,
      images: [`${baseUrl}/og-image.png`], // Image Sitemap entry
    },
    {
      url: `${baseUrl}/about`,
      lastModified: new Date(),
      changeFrequency: 'monthly',
      priority: 0.8,
    },
  ];
}

app/robots.ts - Robots Configuration
import type { MetadataRoute } from 'next';

export default function robots(): MetadataRoute.Robots {
  const baseUrl = 'https://your-site.com';

  return {
    rules: [
      {
        userAgent: '*',
        allow: '/',
        disallow: ['/api/', '/admin/'],
        // Do NOT disallow /_next/ — crawlers need render-critical CSS/JS
        // Do NOT add bot-specific rules (Googlebot, Bingbot) unless overriding wildcard
      },
    ],
    sitemap: `${baseUrl}/sitemap.xml`,
    host: baseUrl,
  };
}

Key Principles
Cache Components & SEO

With cacheComponents: true in next.config.ts, use the "use cache" directive for SEO-critical server components:

// app/(home)/sections/hero-section.tsx
export async function HeroSection() {
  "use cache";
  cacheLife("minutes");   // Built-in profile: ~15 min
  cacheTag("hero");       // For targeted invalidation via revalidateTag("hero")

  const data = await fetchData();
  return <div>{/* SEO-visible content */}</div>;
}


Key rules:

"use cache" must be the first statement in the function body
No cookies()/headers() inside cache scope
Use cacheLife() + cacheTag() instead of export const revalidate
Sitemaps and metadata are static by default — only use "use cache" if they fetch dynamic data
Rendering Strategy for SEO
Strategy	Use When	SEO Impact
"use cache"	Server components with periodic data	Best - cached HTML, fast TTFB
SSG (Static)	Content rarely changes	Best - pre-rendered HTML
SSR	Dynamic content per request	Great - server-rendered
CSR	Dashboards, authenticated areas	Poor - avoid for SEO pages
Core Web Vitals Targets
Metric	Target	Impact
LCP (Largest Contentful Paint)	< 2.5s	Loading speed
INP (Interaction to Next Paint)	< 200ms	Interactivity
CLS (Cumulative Layout Shift)	< 0.1	Visual stability
References
Metadata API: See references/metadata-api.md
Sitemap & Robots: See references/sitemap-robots.md
JSON-LD Structured Data: See references/json-ld.md
SEO Audit Checklist: See references/checklist.md
Troubleshooting: See references/troubleshooting.md
Common Mistakes to Avoid
Mixing next-seo with Metadata API - Use only Metadata API in App Router
Missing canonical URLs - Always set alternates.canonical
Using CSR for SEO pages - Use SSG/SSR for indexable content
Blocking /_next/ in robots.txt - Crawlers need render-critical CSS/JS; never disallow /_next/
Missing metadataBase - Required for relative URLs in metadata
Viewport in metadata - Must be a separate export
Mixing metadata object and generateMetadata - Use one or the other, not both
Quick Fixes
Add noindex to a page
export const metadata: Metadata = {
  robots: {
    index: false,
    follow: false,
  },
};

Dynamic metadata per page
type Props = { params: Promise<{ id: string }> };

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { id } = await params;            // params is a Promise in current Next.js
  const product = await getProduct(id);
  return {
    title: product.name,
    description: product.description,
  };
}

Canonical for dynamic routes
type Props = { params: Promise<{ slug: string }> };

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { slug } = await params;
  return {
    alternates: {
      canonical: `/products/${slug}`,
    },
  };
}

Weekly Installs
950
Repository
laguagu/claude-…s-skills
GitHub Stars
30
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
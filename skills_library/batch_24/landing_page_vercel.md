---
title: landing-page-vercel
url: https://skills.sh/shipshitdev/library/landing-page-vercel
---

# landing-page-vercel

skills/shipshitdev/library/landing-page-vercel
landing-page-vercel
Installation
$ npx skills add https://github.com/shipshitdev/library --skill landing-page-vercel
SKILL.md
Landing Page (Vercel)

Create a production-ready static landing page with:

Structure: Semantic HTML5 + Modern CSS + Vanilla JS
Form: Working email capture (Formspree or custom endpoint)
Analytics: Plausible/Fathom ready
Design: Responsive, accessible, performant
Deploy: One-click Vercel deployment
What Makes This Different

This skill generates working landing pages, not empty templates:

Real email capture form that actually submits
Analytics integration ready to activate
Responsive design tested on mobile
Accessibility basics (WCAG 2.1 AA)
Content from your PRD brief
Workflow
Phase 1: PRD Brief Intake

Ask the user for product details, then extract and confirm:

I'll help you create a landing page. Based on your description:

**Product:** [Name]
**Tagline:** [One-line value proposition]

**Hero Section:**
- Headline: [Main headline]
- Subheadline: [Supporting text]
- CTA: [Button text]

**Features:** (3-5)
1. [Feature 1]: [Description]
2. [Feature 2]: [Description]
3. [Feature 3]: [Description]

**CTA Type:** [Waitlist / Sign Up / Demo Request / Contact]

**Social Proof:** [Testimonials / Logos / Stats / None]

Is this correct? Any adjustments?

Phase 2: Content Generation

Generate complete landing page content:

Sections:

Hero - Headline, subheadline, CTA button, optional hero image
Features - 3-5 feature cards with icons
How It Works - 3-step process (optional)
Social Proof - Testimonials or logos (optional)
FAQ - 4-6 common questions (optional)
CTA - Final call to action with form
Footer - Links, copyright, social icons
Phase 3: Form Integration

Email Capture Options:

Formspree (Recommended - Free tier)

No backend needed
Instant setup
Email notifications

Custom Endpoint

Your own API
Full control
Requires backend

Waitlist Service

Waitlist.email
Loops.so
ConvertKit
Phase 4: Quality Verification

Verify before handoff:

HTML validates (W3C)
Responsive on mobile
Form submits successfully
Analytics placeholders present
Lighthouse score 90+
Usage
# Create landing page with PRD
python3 scripts/scaffold.py \
  --out ./my-landing-page \
  --name "ProductName" \
  --tagline "Your compelling value proposition" \
  --features "Feature1,Feature2,Feature3"

# Interactive mode
python3 scripts/scaffold.py \
  --out ./my-landing-page \
  --interactive

Generated Structure
my-landing-page/
├── index.html           # Main landing page
├── styles.css           # All styles (no framework)
├── script.js            # Form handling + interactions
├── data.json            # Content data (easy to edit)
├── vercel.json          # Vercel configuration
├── assets/
│   ├── favicon.ico
│   └── og-image.png     # Social sharing image
└── README.md            # Deployment instructions

Key Patterns
Form Handling (JavaScript)
document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('signup-form');
  const button = form.querySelector('button[type="submit"]');
  const messageEl = document.getElementById('form-message');

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const originalText = button.textContent;

    try {
      button.textContent = 'Submitting...';
      button.disabled = true;

      const response = await fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: { 'Accept': 'application/json' }
      });

      if (response.ok) {
        // Hide form and show success message
        form.style.display = 'none';
        messageEl.textContent = 'Thanks! We will be in touch.';
        messageEl.classList.add('success');
      } else {
        throw new Error('Form submission failed');
      }
    } catch (error) {
      button.textContent = originalText;
      button.disabled = false;
      messageEl.textContent = 'Something went wrong. Please try again.';
      messageEl.classList.add('error');
    }
  });
});

Data Structure (data.json)
{
  "name": "ProductName",
  "tagline": "Your compelling value proposition",
  "hero": {
    "headline": "Build something amazing",
    "subheadline": "The easiest way to create, launch, and grow your product.",
    "cta": "Join the Waitlist"
  },
  "features": [
    {
      "icon": "zap",
      "title": "Lightning Fast",
      "description": "Built for speed from the ground up."
    },
    {
      "icon": "shield",
      "title": "Secure by Default",
      "description": "Enterprise-grade security included."
    },
    {
      "icon": "sparkles",
      "title": "AI-Powered",
      "description": "Smart features that learn from you."
    }
  ],
  "faq": [
    {
      "question": "When will you launch?",
      "answer": "We're aiming for Q1 2026. Join the waitlist to be first to know."
    }
  ]
}

Form Integration Guide
Option 1: Formspree (Recommended)
Go to formspree.io
Create a free account
Create a new form
Copy your form ID
Replace YOUR_FORM_ID in the HTML
Option 2: Custom Endpoint
// In script.js, update the form action
const API_URL = 'https://your-api.com/api/waitlist';

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const email = form.querySelector('input[name="email"]').value;

  const response = await fetch(API_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email })
  });
  // Handle response...
});

Analytics Setup
Plausible (Privacy-friendly)
<!-- Add to head section -->
<script defer data-domain="yourdomain.com" src="https://plausible.io/js/script.js"></script>

Fathom
<!-- Add to head section -->
<script src="https://cdn.usefathom.com/script.js" data-site="YOUR_SITE_ID" defer></script>

Deployment
Vercel (One-click)
# Install Vercel CLI
npm i -g vercel

# Deploy
cd my-landing-page
vercel

# Production deploy
vercel --prod

Vercel Configuration (vercel.json)
{
  "version": 2,
  "builds": [
    { "src": "*.html", "use": "@vercel/static" },
    { "src": "*.css", "use": "@vercel/static" },
    { "src": "*.js", "use": "@vercel/static" },
    { "src": "assets/**", "use": "@vercel/static" }
  ],
  "routes": [
    { "src": "/(.*)", "dest": "/index.html" }
  ],
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "X-Frame-Options", "value": "DENY" },
        { "key": "X-XSS-Protection", "value": "1; mode=block" }
      ]
    }
  ]
}

CSS Variables
:root {
  --color-primary: #3b82f6;
  --color-primary-dark: #2563eb;
  --color-bg: #0f172a;
  --color-bg-secondary: #1e293b;
  --color-text: #f8fafc;
  --color-text-muted: #94a3b8;
  --font-sans: system-ui, -apple-system, sans-serif;
  --max-width: 1200px;
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 2rem;
  --spacing-xl: 4rem;
}

Accessibility Checklist
 Semantic HTML structure
 Proper heading hierarchy (h1 → h2 → h3)
 Alt text for images
 Focus states for interactive elements
 Color contrast ratio 4.5:1 minimum
 Form labels and error messages
 Skip link for keyboard navigation
 Responsive text sizing (no fixed px for body text)
Performance Checklist
 No external CSS frameworks
 Minimal JavaScript
 Optimized images (WebP with fallback)
 System fonts (no web font loading)
 Lazy loading for below-fold images
 Preconnect for external resources
References
scripts/scaffold.py - Generation script
assets/templates/ - HTML/CSS templates
Weekly Installs
174
Repository
shipshitdev/library
GitHub Stars
21
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
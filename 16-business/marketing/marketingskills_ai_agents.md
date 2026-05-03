---
rating: ⭐⭐⭐
title: marketingskills-ai-agents
url: https://skills.sh/aradotso/trending-skills/marketingskills-ai-agents
---

# marketingskills-ai-agents

skills/aradotso/trending-skills/marketingskills-ai-agents
marketingskills-ai-agents
Installation
$ npx skills add https://github.com/aradotso/trending-skills --skill marketingskills-ai-agents
SKILL.md
Marketing Skills for AI Agents

Skill by ara.so — Daily 2026 Skills collection.

coreyhaines31/marketingskills is a collection of markdown-based AI agent skills covering CRO, copywriting, SEO, analytics, paid ads, email, and growth engineering. Install them once and any compatible agent (Claude Code, Cursor, Codex, Windsurf) gains specialized marketing expertise and frameworks.

How Skills Work

Each skill is a markdown file that tells AI agents:

When to activate (trigger phrases)
What frameworks to apply (e.g. AIDA, PAS, Jobs-to-be-Done)
What to produce (copy, code, audits, strategies)
Which other skills to reference (cross-skill dependencies)

All skills read product-marketing-context first — it's the shared foundation containing your product, audience, and positioning.

Installation
Option 1: CLI (Recommended)
# Install all 33 skills at once
npx skills add coreyhaines31/marketingskills

# Install only specific skills
npx skills add coreyhaines31/marketingskills --skill page-cro copywriting seo-audit

# See all available skills before installing
npx skills add coreyhaines31/marketingskills --list


Skills land in .agents/skills/ with a symlink to .claude/skills/ for Claude Code.

Option 2: Claude Code Plugin
/plugin marketplace add coreyhaines31/marketingskills
/plugin install marketing-skills

Option 3: Git Clone
git clone https://github.com/coreyhaines31/marketingskills.git
cp -r marketingskills/skills/* .agents/skills/

Option 4: Git Submodule (for team projects)
git submodule add https://github.com/coreyhaines31/marketingskills.git .agents/marketingskills
# Reference skills from .agents/marketingskills/skills/

Project Structure
marketingskills/
├── skills/
│   ├── product-marketing-context/   ← Start here — foundation for all others
│   ├── page-cro/
│   ├── copywriting/
│   ├── seo-audit/
│   ├── ab-test-setup/
│   ├── email-sequence/
│   ├── paid-ads/
│   └── ... (33 skills total)
└── README.md


Each skill directory contains a SKILL.md (or README.md) with structured instructions the agent reads.

First Step: Set Up Product Marketing Context

Before using any other skill, create your context file. This is the single most important step.

"Create my product marketing context"


The agent will generate .agents/skills/product-marketing-context/context.md by asking about:

Product name, description, and category
Target audience and ICPs
Core value proposition and positioning
Key competitors
Pricing and business model
Tone and brand voice

Every other skill reads this file automatically before executing.

Available Skills Reference
Foundation
Skill	Use When
product-marketing-context	Creating or updating your shared product/positioning doc
SEO & Content
Skill	Use When
seo-audit	Auditing or diagnosing SEO issues
ai-seo	Optimizing for LLM/AI search citations
site-architecture	Planning URL structure, navigation, internal links
programmatic-seo	Building SEO pages at scale from templates + data
schema-markup	Adding structured data / JSON-LD
content-strategy	Planning what content to create and why
CRO (Conversion Rate Optimization)
Skill	Use When
page-cro	Optimizing any marketing or landing page
signup-flow-cro	Improving signup/trial activation flows
onboarding-cro	Improving post-signup activation and time-to-value
form-cro	Optimizing lead capture, contact, or non-signup forms
popup-cro	Creating or improving popups, modals, slide-ins
paywall-upgrade-cro	In-app paywalls, upgrade screens, feature gates
Copy & Content
Skill	Use When
copywriting	Writing homepage, landing page, or any marketing copy
copy-editing	Editing or improving existing copy
cold-email	Writing B2B cold outreach sequences
email-sequence	Building drip, lifecycle, or onboarding emails
social-content	LinkedIn, Twitter/X, Instagram content
Paid & Measurement
Skill	Use When
paid-ads	Google Ads, Meta, LinkedIn, Twitter campaigns
ad-creative	Generating ad headlines, descriptions, primary text
ab-test-setup	Planning and implementing A/B experiments
analytics-tracking	Setting up or auditing GA4, Segment, Mixpanel
Growth & Retention
Skill	Use When
referral-program	Building referral or affiliate programs
free-tool-strategy	Planning free tools for lead gen or SEO
churn-prevention	Cancellation flows, save offers, dunning
lead-magnets	Creating email capture lead magnets
Sales & GTM
Skill	Use When
revops	Lead lifecycle, CRM, marketing-to-sales handoff
sales-enablement	Pitch decks, one-pagers, objection handling
launch-strategy	Product launches, feature announcements
pricing-strategy	Pricing, packaging, monetization decisions
competitor-alternatives	Comparison and alternative pages
Strategy
Skill	Use When
marketing-ideas	Brainstorming marketing strategies and tactics
marketing-psychology	Applying behavioral science to marketing
Usage Examples
Example 1: Audit and improve a landing page
"Audit my landing page at src/pages/index.tsx and suggest CRO improvements"


The agent reads product-marketing-context, activates page-cro, then:

Reviews the page structure, headline, CTA placement
Applies frameworks (AIDA, above-the-fold analysis, social proof audit)
Outputs a prioritized list of changes with implementation code
Example 2: Write a homepage from scratch
"Write homepage copy for my SaaS product using the copywriting skill"


Output includes hero headline variants, subheadline, feature sections, social proof blocks, and CTAs — all grounded in your product-marketing-context.

Example 3: Set up A/B testing
"Help me set up an A/B test for my pricing page CTA button"


The agent activates ab-test-setup and generates:

// Example output: Google Optimize / custom A/B test scaffold
const experiments = {
  pricing_cta_test: {
    id: 'pricing-cta-v1',
    variants: [
      { id: 'control', cta: 'Start Free Trial' },
      { id: 'variant_a', cta: 'Get Started Free' },
      { id: 'variant_b', cta: 'Try It Free — No Card Required' }
    ],
    metric: 'signup_click',
    minimumDetectableEffect: 0.05,
    confidenceLevel: 0.95
  }
};

// Split traffic deterministically by user ID
function getVariant(userId, experimentId) {
  const hash = simpleHash(`${userId}-${experimentId}`);
  const variantIndex = hash % experiments[experimentId].variants.length;
  return experiments[experimentId].variants[variantIndex];
}

Example 4: Generate programmatic SEO pages
"Create a programmatic SEO page template for '[tool] alternatives' pages"


The agent activates programmatic-seo + competitor-alternatives and scaffolds:

// Next.js dynamic route: /pages/[competitor]-alternatives.js
export async function getStaticPaths() {
  const competitors = await fetchCompetitors(); // your data source
  return {
    paths: competitors.map(c => ({ params: { competitor: c.slug } })),
    fallback: 'blocking'
  };
}

export async function getStaticProps({ params }) {
  const data = await getCompetitorData(params.competitor);
  return { props: { competitor: data }, revalidate: 86400 };
}

Example 5: Build an email sequence
"Write a 5-email onboarding sequence for new trial users"


Activates email-sequence + onboarding-cro. Produces:

Email 1: Welcome + single activation action (Day 0)
Email 2: Value reinforcement + feature highlight (Day 2)
Email 3: Social proof / case study (Day 4)
Email 4: Overcome objections / FAQ (Day 6)
Email 5: Trial ending + upgrade CTA (Day 8)

Each with subject line, preview text, body copy, and CTA.

Example 6: Schema markup for SEO
"Add schema markup to my blog post template"

// Output: JSON-LD for Article schema
const articleSchema = {
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": post.title,
  "description": post.excerpt,
  "author": {
    "@type": "Person",
    "name": post.author.name,
    "url": post.author.url
  },
  "datePublished": post.publishedAt,
  "dateModified": post.updatedAt,
  "publisher": {
    "@type": "Organization",
    "name": process.env.SITE_NAME,
    "logo": {
      "@type": "ImageObject",
      "url": process.env.SITE_LOGO_URL
    }
  }
};

Skill Cross-References (Dependency Map)

When working on a task, the agent may activate multiple skills together:

Landing page optimization:
  page-cro → copywriting → ab-test-setup → analytics-tracking

SEO content strategy:
  seo-audit → content-strategy → ai-seo → schema-markup

Sales pipeline:
  revops → sales-enablement → cold-email → email-sequence

Growth loop:
  free-tool-strategy → programmatic-seo → referral-program → analytics-tracking


You can invoke multiple skills explicitly:

"Use page-cro and copywriting skills to rewrite my /pricing page"
"Apply marketing-psychology and copywriting to my checkout flow"

Configuration

No config file required. Skills are self-contained markdown files. The only configuration is your product-marketing-context document.

To update your context at any time:

"Update my product marketing context — we just changed our target audience to enterprise"

Adding Custom Skills

Create a new skill directory following the same pattern:

mkdir .agents/skills/my-custom-skill
cat > .agents/skills/my-custom-skill/SKILL.md << 'EOF'
---
name: my-custom-skill
description: What this skill does
triggers:
  - phrase that activates this skill
---

# My Custom Skill

## When to Use
...

## Process
...

## Related Skills
- product-marketing-context (always read first)
EOF

Contributing
git clone https://github.com/coreyhaines31/marketingskills.git
cd marketingskills

# Add a new skill
mkdir skills/my-new-skill
# Create skills/my-new-skill/README.md following existing skill format

# Update the skills table in README.md
# Open a PR


The README.md skills table is auto-generated between <!-- SKILLS:START --> and <!-- SKILLS:END --> markers.

Troubleshooting

Skills not activating in Claude Code

# Verify symlink exists
ls -la .claude/skills/
# If missing, re-run install
npx skills add coreyhaines31/marketingskills


Agent ignoring product context

Make sure .agents/skills/product-marketing-context/context.md exists
If missing: "Create my product marketing context" to regenerate it

Installing specific skills only

npx skills add coreyhaines31/marketingskills --skill copywriting page-cro seo-audit analytics-tracking


Updating to latest skills

npx skills update coreyhaines31/marketingskills
# or if using submodule:
git submodule update --remote .agents/marketingskills


Skill conflicts with other installed skill packs

Skills are namespaced by directory — no conflicts expected
If an agent activates the wrong skill, be explicit: "Use the page-cro skill from marketingskills"
Resources
Agent Skills spec — the standard these skills follow
Coding for Marketers — guide for non-technical users
Conversion Factory — Corey's CRO agency
Swipe Files — marketing newsletter
Magister — autonomous AI CMO using these skills
Issues — get help or report bugs
Weekly Installs
1.1K
Repository
aradotso/trending-skills
GitHub Stars
42
First Seen
Mar 18, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykPass
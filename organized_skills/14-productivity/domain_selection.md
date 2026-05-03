---
rating: ⭐⭐
title: domain-selection
url: https://skills.sh/kostja94/marketing-skills/domain-selection
---

# domain-selection

skills/kostja94/marketing-skills/domain-selection
domain-selection
Installation
$ npx skills add https://github.com/kostja94/marketing-skills --skill domain-selection
SKILL.md
Strategy: Domain Selection

Guides initial domain choice for a single site: Brand vs Partial Match vs Exact Match domains, TLD selection (.ai, .com, .io), length, readability, history check, and defensive registration. A good domain affects SEO, brand perception, and UX. See domain-architecture when planning for multiple products; rebranding-strategy when changing domain.

When invoking: On first use, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On subsequent use or when the user asks to skip, go directly to the main output.

Reference: Alignify: Domain SEO – How to Choose SEO-Friendly Domains — detailed guide, AI brand naming, TLD recommendations, rebrand cases.

Initial Assessment

Check for project context first: If .claude/project-context.md or .cursor/project-context.md exists, read Sections 2 (Positioning), 3 (Target Audience), 8 (Brand & Voice).

Identify:

Product type: Tool, content, e-commerce, AI product, etc.
Brand stage: New brand vs established; solo vs team
Goals: Quick SEO traffic vs long-term brand building
Domain Type: Brand vs PMD vs EMD
Type	Description	SEO	Brand	Best For
Branded Domain	Domain = brand; no functional keywords (Notion, Canva, Perplexity)	Long-term; Google favors brands	High	Teams; long-term brand building
Partial Match (PMD)	Part of domain relates to function (FlowGPT, Dify, Reportify)	Balance; signals topic	Medium	AI tools; balance SEO + brand
Exact Match (EMD)	Domain = search query (png2jpg.com, aiartgenerator.cc)	Fast early traffic; ceiling lower	Low	Solo devs; tool sites; site networks

Google stance: Keywords in domain no longer directly affect ranking; domain still matters for UX and brand. EMDs work when paired with quality content; branded domains with entity recognition matter more long-term.

Recommendation:

Brand building → Branded or PMD; plan for months
Quick SEO traffic → EMD or PMD; good for tool sites, converters, generators
AI products → PMD (xxxGPT, xxxify) or Branded; avoid generic names that cause search confusion (e.g., multiple "Speak AI" products)
TLD Selection
TLD	Use Case	Notes
.com	Default choice; highest trust	Most preferred; often expensive
.ai	AI products	ccTLD (Anguilla); auto-hyperlinks in Excel/Sheets/Feishu → natural backlinks; signals AI
.io	Tech, SaaS	Popular; geopolitical risk (Chagos Islands)
.co, .app, .pro	Alternatives	If .com taken
.new	Instant-create tools	For bolt.new, claude.new style; see Alignify .new guide

AI products: Prefer .ai, .com, or .io. Avoid niche TLDs (.im, .xyz, .inc, .art, .dev)—higher risk of resolution issues (e.g., Notion .so outage).

Domain Best Practices
Rule	Purpose
Short & memorable	Easier to type, share, recall
Avoid hyphens	Looks unprofessional; can signal low quality
Check history	Use Archive.org; avoid previously penalized domains
Defensive registration	Register .net, .org, variants; redirect to main; do not deploy on multiple domains
Impersonation variants	For AI products: register brand+ai, brand+app, brand+official; see brand-protection for impersonation response
Accurate WHOIS; renew on time	Avoid loss or hijacking
.ai Domain Natural Backlinks

When brand name includes .ai (e.g., Character.ai, Leonardo.Ai), the full string auto-hyperlinks in Excel, Google Sheets, Feishu, and some IM apps. Each mention = potential backlink. Useful for AI products where the generic name alone (e.g., "Character") is a common noun.

Output Format
Domain type recommendation (Brand / PMD / EMD) with rationale
TLD recommendation
Checklist (length, readability, history, defensive registration)
Related next steps (website-structure, rebranding-strategy)
Related Skills
branding: Brand strategy; domain selection implements brand positioning
website-structure: Plan pages after domain choice; single-domain structure
domain-architecture: Subfolder vs subdomain vs independent when multiple products
rebranding-strategy: Domain change, 301 redirects; use when rebranding
brand-protection: Defensive registration for impersonation prevention; fake site response
link-building: Build authority after domain is chosen
Weekly Installs
510
Repository
kostja94/market…g-skills
GitHub Stars
413
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
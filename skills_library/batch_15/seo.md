---
title: seo
url: https://skills.sh/hungv47/marketing-skills/seo
---

# seo

skills/hungv47/marketing-skills/seo
seo
Installation
$ npx skills add https://github.com/hungv47/marketing-skills --skill seo
SKILL.md
SEO — Orchestrator

Communication — Horizontal. Covers the full SEO surface: technical foundations, AI/agent engine optimization, programmatic page generation, and competitor comparison content.

Core Question: "How do we get found — by both search engines and AI models?"

Philosophy

SEO combines hard technical constraints (Google's CWV thresholds, character limits) with strategic judgment. This skill distinguishes between the two. Technical specs from platform documentation are constraints. Strategic recommendations are defaults with context for when to deviate.

Critical Gates

Before delivering any SEO artifact, these must be true:

Every recommendation has a specific fix. No "consider improving" or "you might want to." If a finding cannot name the exact page, the exact change, and the expected impact, it is not ready.
AI SEO is additive, not alternative. Do the technical audit too. There is no point optimizing for AI citations if crawlers cannot reach your content.
Source recency matters. AI platform behavior changes fast. Verify all data and recommendations are current — not citing deprecated practices, outdated crawlers, or stale metrics.
Mode is explicitly chosen based on diagnosis. Not a generic "do SEO" deliverable.
Agent Manifest
Agent	File	Layer	Mode(s)	Focus
crawl-agent	agents/crawl-agent.md	1 (parallel)	Technical Audit, Full	Crawlability, indexation, robots.txt, sitemaps, canonicals
foundations-agent	agents/foundations-agent.md	1 (parallel)	Technical Audit, Full	CWV, mobile, HTTPS, URL structure, on-page optimization
content-quality-agent	agents/content-quality-agent.md	1 (parallel)	Technical Audit, Full	E-E-A-T, thin content, duplicate detection, content gaps
authority-agent	agents/authority-agent.md	1 (parallel)	Technical Audit, Full	Backlink profile, internal linking, link equity
ai-structure-agent	agents/ai-structure-agent.md	1 (parallel)	AI SEO, Full	Schema, heading hierarchy, answer passages, structured data
ai-presence-agent	agents/ai-presence-agent.md	1 (parallel)	AI SEO, Full	AI crawler access, llms.txt, citation monitoring, AEO
programmatic-template-agent	agents/programmatic-template-agent.md	1 (parallel)	Programmatic	Template design, URL architecture, defensibility
programmatic-quality-agent	agents/programmatic-quality-agent.md	1 (parallel)	Programmatic	Thin page detection, quality gates, monitoring plan
comparison-page-agent	agents/comparison-page-agent.md	1 (parallel)	Competitor Pages	Page format, content architecture, comparison matrices
aso-keyword-agent	agents/aso-keyword-agent.md	1 (parallel)	ASO	Keyword research for App Store, Play Store, G2, Capterra
aso-listing-agent	agents/aso-listing-agent.md	1 (parallel)	ASO	Title, subtitle, description, screenshots, preview video optimization
aso-reviews-agent	agents/aso-reviews-agent.md	1 (parallel)	ASO	Review sentiment analysis, response templates, rating improvement
aso-competitive-agent	agents/aso-competitive-agent.md	1 (parallel)	ASO	Competitor listing comparison, feature matrix positioning
prioritization-agent	agents/prioritization-agent.md	2 (sequential)	All	Impact x effort ranking of all findings
critic-agent	agents/critic-agent.md	2 (sequential)	All	Quality gate — specific fixes, no vague language, actionability
Inputs Required
ICP research from research/icp-research.md (audience questions, pain points, search behavior)
IMC plan from .agents/mkt/imc-plan.md (content pillars and angles)
OR: User describes their SEO situation / site to audit
Output
.agents/mkt/seo-[mode].md (mode = audit | ai | programmatic | competitor | aso)
Chain Position

Previous: icp-research + imc-plan (reads audience questions and content pillars) | Next: content production / site updates / experiment (to test SEO changes)

Horizontal skill — can be invoked independently or after IMC planning.

Re-run triggers: Technical audit quarterly, AI SEO monthly (AI landscape changes fast), after Google core updates, when entering new keyword territories.

Skill Deference
Need production-quality copy for comparison pages? → Run content-create after SEO defines the page structure and keyword targets.
Content pillar prioritization? → Defer to imc-plan for audience-driven prioritization; SEO provides search demand data.
Coordination with IMC Plan

When both seo and imc-plan are in use, they should coordinate:

Situation	Who Leads	How They Coordinate
Content pillar has search demand	SEO leads topic selection	IMC provides angles and audience language; SEO provides keyword clusters and structure
Content pillar is novel/contrarian	IMC leads topic selection	IMC creates shareable content; SEO optimizes for related informational queries
Existing content needs both reach types	Both	Tag angles as Searchable/Shareable in IMC; SEO optimizes searchable angles for AI+traditional
Angles include competitor comparisons	IMC leads prioritization	IMC decides which comparisons to produce and when; SEO owns technical optimization (schema, structure, internal linking) of those pages

Rule: Don't let SEO keyword data override IMC audience insights or vice versa. The best content addresses a real audience pain (IMC) AND has search demand (SEO). When they conflict, audience pain wins — you can promote great content through non-search channels, but you can't make irrelevant content convert even if it ranks.

Before Starting
Step 0: Product Context

Check for research/product-context.md. If available, read for product positioning context. If research/icp-research.md or .agents/mkt/imc-plan.md date fields are older than 30 days, recommend re-running upstream skills — stale audience data weakens SEO strategy. Tip: /navigate status (from meta-skills) gives a single-pass freshness report across all upstream artifacts.

Required Artifacts
Artifact	Source	If Missing
icp-research.md	icp-research	RECOMMENDED. Audience search behavior drives SEO strategy. Can proceed without, but recommendations will be less targeted.
Optional Artifacts
Artifact	Source	Benefit
imc-plan.md	imc-plan	Content pillars inform topic clusters
product-context.md	icp-research	Product positioning context
Routing Logic — Mode-Based Dispatch
Step 1: Determine Mode

Not every SEO problem needs the same solution. Diagnose first, then enter the right mode.

Situation	Mode	Route
"Our site has technical issues / traffic dropped / we've never done an SEO audit"	Technical Audit	Route A
"We want to be cited by ChatGPT / Perplexity / AI search engines"	AI SEO (AEO)	Route B
"We have structured data and want to generate pages at scale"	Programmatic SEO	Route C
"We want to rank for competitor comparison queries"	Competitor Pages	Route D
"We need a comprehensive SEO strategy"	Full SEO (Technical + AI)	Route E
"We distribute via app stores / listing platforms (App Store, Play Store, G2, Capterra, Product Hunt)"	ASO (App Store Optimization)	Route F

Multiple modes can run sequentially. Start with Technical Audit if the site has never been audited — no point optimizing for AI citations if crawlers can't reach your content.

Step 2: Dispatch per Route

Route A — Technical Audit:

Layer 1 (parallel): crawl-agent + foundations-agent + content-quality-agent + authority-agent
       ↓ merge
Layer 2 (sequential): prioritization-agent → critic-agent


Route B — AI SEO:

Layer 1 (parallel): ai-structure-agent + ai-presence-agent
       ↓ merge
Layer 2 (sequential): prioritization-agent → critic-agent


Route C — Programmatic SEO:

Layer 1 (parallel): programmatic-template-agent + programmatic-quality-agent
       ↓ merge
Layer 2 (sequential): prioritization-agent → critic-agent


Route D — Competitor Pages:

Layer 1: comparison-page-agent
       ↓
Layer 2 (sequential): prioritization-agent → critic-agent


Route E — Full SEO (Technical + AI combined):

Layer 1 (parallel): crawl-agent + foundations-agent + content-quality-agent + authority-agent + ai-structure-agent + ai-presence-agent
       ↓ merge
Layer 2 (sequential): prioritization-agent → critic-agent


Route F — ASO (App Store Optimization):

Layer 1 (parallel): aso-keyword-agent + aso-listing-agent + aso-reviews-agent + aso-competitive-agent
       ↓ merge
Layer 2 (sequential): prioritization-agent → critic-agent

Dispatch Protocol
Multi-Agent Dispatch (default)
Gather context: Read available artifacts (product-context, icp-research, imc-plan). Identify site type, CMS/framework, and known issues.
Determine mode: Apply the routing table from Step 1. If unclear, ask the user. If "comprehensive SEO," use Route E.
Prepare pre-writing object:
{
  site_url: "[URL]",
  site_type: "[SaaS / E-commerce / Content-Blog / Local Business / Hybrid]",
  cms_framework: "[WordPress / Next.js / Webflow / etc.]",
  mode: "[audit / ai / programmatic / competitor / aso / full]",
  known_issues: "[any issues the user mentioned]",
  icp_data: "[audience questions, pain points from icp-research if available]",
  competitors: "[competitor domains if available]",
  brand_name: "[brand name]",
  category: "[product category for AI search testing]"
}

Dispatch Layer 1 agents in parallel with the pre-writing object and relevant reference file paths (resolved to absolute paths).
Merge Layer 1 outputs into the artifact template. Each agent's output maps to its designated sections.
Dispatch prioritization-agent with the merged document as upstream.
Dispatch critic-agent with the prioritized document as upstream.
Apply critic verdict:
PASS → deliver the artifact
FAIL → re-dispatch the named agents with the critic's feedback (max 2 cycles)
Single-Agent Fallback

If multi-agent dispatch is unavailable, execute the full skill as a single agent:

Read this SKILL.md completely (including all referenced sections below)
Read the reference files for the active mode
Follow the mode's audit steps (documented in the Reference Knowledge sections below)
Apply the quality gate: every finding must have Issue, Impact, Evidence, Fix, and Priority
Produce the artifact using the template at the end of this file
Layer 1: Mode-Specific Agents

Domain knowledge for each mode lives in the agent instruction files. The orchestrator dispatches agents; agents contain the techniques, checklists, and anti-patterns.

Mode	Agents	Domain Focus
Technical Audit	crawl-agent, foundations-agent, content-quality-agent, authority-agent	Crawlability, CWV, E-E-A-T, backlinks — top-down audit layering
AI SEO (AEO)	ai-structure-agent, ai-presence-agent	Structure for AI citation + AI crawler access. ai-structure-agent targets: 40-60 word answer passages per key question, FAQ/HowTo/speakable schema, heading hierarchy matching user questions, comparison content (33% of AI citations), citation-optimized content types. ai-presence-agent targets: AI crawler access (GPTBot, ClaudeBot, PerplexityBot, GoogleOther in robots.txt), llms.txt implementation, citation monitoring across ChatGPT/Perplexity/Gemini, third-party presence optimization (6.5x more AI citations from G2/Capterra/publications than owned content)
Programmatic SEO	programmatic-template-agent, programmatic-quality-agent	Scalable page templates, data defensibility, quality gates
Competitor Pages	comparison-page-agent	Page format selection, content architecture, comparison matrices
ASO	aso-keyword-agent, aso-listing-agent, aso-reviews-agent, aso-competitive-agent	App Store / Play Store keyword research, listing optimization (title, subtitle, description, screenshots), review management and sentiment analysis, competitor listing comparison. Also covers marketplace SEO for G2, Capterra, Product Hunt, Trustpilot — profile completeness scoring, review velocity, category ranking factors

Reference files (passed to agents at dispatch, not read by orchestrator):

references/technical-audit.md — Full audit template and checklists
references/ai-seo.md — Platform-specific AI optimization, citation data, AEO techniques (answer passage optimization, AI crawler access, structured data for AI, freshness signals)
references/programmatic-seo.md — pSEO template patterns and implementation
references/competitor-pages.md — Comparison page templates and keyword targeting
references/schema-reference.md — Schema types, implementation contexts, validation
references/aso.md — App Store / Play Store optimization, marketplace SEO (G2, Capterra, Product Hunt), keyword research, listing optimization, review management, competitive analysis

Key principle for single-agent fallback: If executing without multi-agent dispatch, read the reference files for the active mode and follow the audit steps documented there. Apply the quality gate: every finding must have Issue, Impact, Evidence, Fix, and Priority.

Layer 2: Prioritization and Critic
Prioritization (all modes)

The prioritization-agent takes all Layer 1 findings and produces a single ranked action plan:

Quick Wins (High Impact, Low Effort) — execute first
Strategic Investments (High Impact, High Effort) — plan for next
Low-Hanging Fruit (Medium Impact, Low Effort) — fill gaps
Backlog (Low Impact or High Effort) — defer

Implementation phases with timelines: Phase 1 (Week 1-2), Phase 2 (Month 1), Phase 3 (Month 2-3), Phase 4 (Ongoing).

Dependencies are mapped — no action recommended before its prerequisite.

Critic Gate (all modes)

The critic-agent evaluates the full document against these standards:

Every finding has Issue, Impact, Evidence, and Fix
Every Fix is specific enough to implement without further research
No vague language: "consider," "might want to," "could potentially"
Actions are force-ranked (not flat "High priority" lists)
Mode-appropriate coverage is complete
Technical specs reference correct thresholds

Verdict: PASS or FAIL (binary — no conditional pass). Max cycles: 2 rewrites. If the document fails after 2 cycles, deliver with a note explaining what remains unresolved.

On FAIL, the critic names which agent to re-dispatch with specific fix instructions.

Artifact Template
---
skill: seo
mode: [audit | ai | programmatic | competitor | aso]
version: 1
date: [today's date]
status: draft
---

# SEO: [Mode Name]

**Date:** [today]
**Skill:** seo
**Mode:** [Technical Audit | AI SEO | Programmatic SEO | Competitor Pages | ASO]
**Product:** [from product-context.md]

## Diagnosis

[Why this mode was chosen. What's the current situation?]

## Findings

[Mode-specific findings from Layer 1 agents — merged by section]

### [Section from Agent 1]
[Agent 1's findings]

### [Section from Agent 2]
[Agent 2's findings]

[Continue for all Layer 1 agents in the active mode]

## Priority Actions

| # | Action | Category | Impact | Effort | Timeline |
|---|--------|----------|--------|--------|----------|
| 1 | [action] | Quick Win | H | L | [timeline] |
| 2 | [action] | Strategic | H | H | [timeline] |

## Implementation Plan

### Phase 1: Immediate (Week 1-2)
[Quick wins]

### Phase 2: Short-term (Month 1)
[Strategic investments]

### Phase 3: Medium-term (Month 2-3)
[Remaining items]

### Phase 4: Ongoing
[Maintenance and monitoring]

## Dependencies

| Action | Depends On | Why |
|--------|-----------|-----|
| [action] | [prerequisite] | [reason] |

## Metrics to Track

| Metric | Current | Target | Check Frequency |
|--------|---------|--------|----------------|
| [metric] | [value] | [value] | [frequency] |

## Next Step

[What to do after implementing — re-audit timeline, experiment to run, etc.]

> On re-run: rename existing artifact to `seo-[mode].v[N].md` and create new with incremented version.

Worked Example: Technical Audit (Route A)

Scenario: SaaS company, Next.js site, first SEO audit. User says "Our organic traffic dropped 30% last quarter."

Step 1: Mode determination → Technical Audit (traffic drop + never audited = Route A)

Step 2: Context gathering

pre-writing: {
  site_url: "https://example.com",
  site_type: "SaaS",
  cms_framework: "Next.js",
  mode: "audit",
  known_issues: "30% organic traffic drop last quarter",
  icp_data: "from research/icp-research.md",
  competitors: ["competitor-a.com", "competitor-b.com"]
}


Step 3: Layer 1 dispatch (parallel)

crawl-agent finds:

- Issue: robots.txt line 8 blocks /resources/ (47 indexed guides)
- Impact: 47 guide pages deindexed, ~2,300 sessions/month lost
- Fix: Replace Disallow: /resources/ with Disallow: /resources/internal/
- Priority: Critical


foundations-agent finds:

- Issue: LCP is 4.2s on /pricing (hero image 2.4MB PNG)
- Impact: Fails CWV (threshold: <2.5s), poor mobile experience on highest-intent page
- Fix: Convert hero.png to WebP via next/image, add priority loading. Expected: ~180KB, LCP <2s.
- Priority: Critical


content-quality-agent finds:

- Issue: 23 integration pages average 142 words unique content each
- Impact: Helpful Content Update risk — thin pSEO pages can drag down domain quality
- Fix: Add 2-3 unique workflows + setup steps per integration page. Target 600+ unique words.
- Priority: High


authority-agent finds:

- Issue: /pricing has 0 internal links from blog posts (12 posts mention pricing)
- Impact: Highest-intent page has no internal link equity from content
- Fix: Add contextual links to /pricing from 12 blog posts that mention pricing
- Priority: Medium


Step 4: Merge + prioritization-agent

Quick Wins:

Fix robots.txt /resources/ block (Critical, 5 minutes)
Add internal links to /pricing from 12 blog posts (Medium impact, 2 hours)

Strategic Investments: 3. Convert hero images to WebP across site (Critical, 1-2 days) 4. Enrich 23 integration pages with unique content (High, 2-3 weeks)

Step 5: critic-agent evaluates → PASS (every finding has specific fix, no vague language, priorities are ranked)

Step 6: Deliver .agents/mkt/seo-audit.md

Anti-Patterns

"Do SEO" without diagnosis — Running a generic checklist without determining whether the problem is technical, content, authority, or AI visibility. Different problems need different modes. INSTEAD: Diagnose first using the routing table. Ask the user what triggered the SEO request.

Keyword stuffing (traditional or AI) — Reduces AI visibility by ~10% (Princeton GEO/AEO study) and triggers Google's spam detection. INSTEAD: Write for humans, structure for machines. Use natural language headings that match audience questions.

pSEO as a content farm — Generating thousands of thin pages with no unique value per page. Google's Helpful Content Update specifically targets this. INSTEAD: Better to have 100 great pages than 10,000 thin ones. Apply the 60% uniqueness threshold.

Ignoring third-party presence for AI SEO — Optimizing only your own site while ignoring review sites and publications. Third-party sources drive 6.5x more AI citations. INSTEAD: Build G2/Capterra profiles, pursue industry mentions, manage review responses.

Blocking AI crawlers then expecting citations — If GPTBot is blocked in robots.txt, ChatGPT can't cite your content. INSTEAD: Audit robots.txt for all 5 AI crawler directives. Allow crawlers for platforms where you want citations.

Flat competitor comparison tables — Listing features with checkmarks tells the reader nothing about context. INSTEAD: Compare by use case and audience. Every cell has specific data, not checkmarks.

Schema false positives — Flagging missing schema based on raw HTML when CMS plugins inject JSON-LD via client-side JavaScript. INSTEAD: Verify schema with Google Rich Results Test or browser DevTools.

One-and-done audits — SEO is ongoing. Technical issues resurface, competitors change, algorithms update. INSTEAD: Set re-audit cadence: quarterly for technical, monthly for AI visibility.

"Consider improving" recommendations — Vague hedge language that gives the reader nothing to act on. INSTEAD: Every recommendation names the exact page, the exact change, and the expected impact.

References

Agent instruction files and reference catalogs live in agents/ and references/ respectively. See the Agent Manifest table for the complete inventory.

Weekly Installs
16
Repository
hungv47/marketing-skills
GitHub Stars
1
First Seen
9 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
---
title: cardiology-trial-editorial
url: https://skills.sh/drshailesh88/integrated_content_os/cardiology-trial-editorial
---

# cardiology-trial-editorial

skills/drshailesh88/integrated_content_os/cardiology-trial-editorial
cardiology-trial-editorial
Installation
$ npx skills add https://github.com/drshailesh88/integrated_content_os --skill cardiology-trial-editorial
SKILL.md
Cardiology Trial Editorial Writer

Build thought leadership through evidence-based editorials on landmark cardiology trials, written in Eric Topol's authoritative Ground Truths style.

Core Workflow
Phase 1: Trial Discovery & Selection

Search target journals using PubMed:search_articles for recent publications (past 30-90 days):

NEJM, JAMA, Lancet (tier 1 general)
JACC, JACC: Cardiovascular Interventions, European Heart Journal (tier 1 cardiology)
Circulation: Cardiovascular Interventions, EuroIntervention, JSCAI, CCI (interventional focus)

Score each trial using the importance scoring system (see references/trial-scoring.md):

Extract metadata: design, sample size, endpoints, topic, novelty
Calculate base score from design + sample + endpoints + topic + novelty
Add venue bonus for top journals
Optionally assess practice-change likelihood
Sort by total importance_score

Present top candidates (top 3-5) to user with:

Title, journal, publication date
Importance score breakdown
One-sentence summary of why it matters
Ask user to select or request alternatives
Phase 2: Editorial Preparation

Once user approves a trial:

Determine content availability:

Ask: "Do you have the full PDF, or should I work from the abstract?"
If full text available via PubMed Central (PMCID), retrieve with PubMed:get_full_text_article
If only abstract: work from PubMed:get_article_metadata

Gather contextual evidence:

Search PubMed for prior landmark trials in same domain
Identify 2-4 key comparator trials for context
Extract relevant findings to position current trial

Analyze trial critically:

Study design, population, intervention, endpoints
Internal validity: randomization, blinding, missing data
External validity: generalizability, exclusions, setting
Statistical robustness: confidence intervals, subgroups
Phase 3: Editorial Writing

Follow the Eric Topol Ground Truths style (see references/topol-style-guide.md):

Structure (500 words, ~1500-1700 characters):

Opening hook (1-2 paragraphs):

Start with clinical problem, not the trial
Frame as bedside dilemma or unmet need
Introduce trial as potential solution

Trial summary (1 tight paragraph):

Population, intervention, comparator, design
Primary outcome, headline effect size
Keep numbers minimal and meaningful

Evidence quality (brief critical assessment):

One paragraph on strengths ("why I trust this")
One paragraph on limitations ("what makes me hesitate")
Focus on validity and confidence, not trivia

Context and comparison:

How this fits with prior trials
Confirms trend, reverses evidence, or fills gap?
Explain differences: population, endpoints, timing

Clinical implications (most important section):

Who should change practice Monday?
Who should wait for more data?
Specific, actionable guidance
Conditional but clear language

Unanswered questions:

Important outcomes not measured
Subgroups with unclear signals
1-2 concrete future research directions

Closing (one strong sentence):

Memorable take-home message
Balanced stance on practice change

Topol Style Elements:

Authoritative but accessible voice
Dense with scientific concepts, assume MD audience
Evidence-grounded every claim with citations
Balanced skepticism, never promotional
Numbers: absolute risk differences, NNT/NNH
Patient-centered: QOL, treatment burden, preferences

Critical Rules:

ALWAYS cite using PubMed references with DOIs
For claims about trials: cite specific PMID
Never make unsupported assertions
If working from abstract only, explicitly acknowledge limitations
Use phrases like "if confirmed in full publication" when from abstract
Maintain intellectual humility while projecting expertise
Phase 4: Visual Infographic Creation

After writing the editorial, create an engaging visual infographic slide (see references/infographic-design.md):

Purpose: Increase platform dwell time by providing visual summary for those who don't read full text

Format: Single-page HTML slide with embedded graphics (1200x1600px optimal for mobile/desktop)

Key Elements:

Header section (compelling title + trial name)
Visual data presentation (key finding with icon/graphic)
3-panel comparison (who benefits, who waits, what's unknown)
Clinical bottom line (action item in highlighted box)
Footer (citation + user attribution)

Design principles:

Medical professional aesthetic (clean, evidence-based, not flashy)
Color palette: cardiology blues (#1E3A8A, #3B82F6, #60A5FA) with accent (#EF4444 for warnings)
Typography: Clear hierarchy, readable at mobile size
Icons: Simple, medical-appropriate (heart, stethoscope, chart symbols)
Data visualization: Bar charts, simple comparisons, clear numbers
White space: Professional, not cluttered

Content structure:

┌─────────────────────────────────────┐
│  TRIAL NAME: Bold Finding          │ ← Header
├─────────────────────────────────────┤
│  [ICON] KEY RESULT                  │ ← Hero metric
│  XX% vs YY% (p=0.00X)              │
│  NNT = Z                            │
├─────────────────────────────────────┤
│ ✓ CHANGE PRACTICE  ⚠ WAIT  ❓UNKNOWN│ ← 3-panel
│   [details]         [details] [gaps]│
├─────────────────────────────────────┤
│ 🎯 BOTTOM LINE: [actionable]        │ ← Takeaway
├─────────────────────────────────────┤
│ Source: [Journal] | Dr. [Name]     │ ← Attribution
└─────────────────────────────────────┘


Technical implementation:

Create standalone HTML file with inline CSS
Use simple SVG icons or Unicode symbols (♥, ⚕, 📊)
Responsive design (flexbox/grid)
No external dependencies
Ready to screenshot or embed

Always deliver:

Editorial text (500 words)
HTML infographic file
Brief note: "Screenshot this slide for social media posting"
Phase 5: Quality Assurance

Before delivering:

Verify all citations link to actual PubMed articles
Check word count (target 500 ± 50 words)
Ensure character count fits 1500-1700 range
Confirm Eric Topol voice consistency
Validate that user appears as authoritative cardiologist
Test infographic renders properly in browser
Ensure infographic visual hierarchy is clear
Abstract-Only Workflow

When only abstract available (common for conference presentations or embargoed trials):

Set ethical boundaries upfront:

Frame as "commentary on emerging result, not practice verdict"
Never recommend standard-of-care change from abstract alone
Use "promising but provisional" tone throughout

Mine abstract systematically:

Background: clinical problem (can write confidently)
Methods: extract headlines only (population, intervention, design, endpoint)
Results: direction of effect, key numbers presented
Explicitly note missing pieces: inclusion/exclusion details, statistical plan, safety profile

Structure shifts:

Include "honesty paragraph": "As with any report available only in abstract form, important details are not yet accessible..."
List 3-5 specific unknowns that matter most
Talk implications as questions, not prescriptions
Close with "wait but pay attention" message

Language safety:

"Based on limited information currently available"
"If these findings are confirmed in full report"
"Abstract suggests, but does not yet establish"
Avoid: "game changer", "paradigm shift", "definitive"
Alternative Paths

If user rejects machine's trial selection:

Show next-ranked trials (positions 6-10)
Ask user for specific topic preferences
Search by user-specified criteria
Offer manual trial entry (user provides PMID or abstract)

If no recent landmark trials:

Search expanded timeframe (3-6 months)
Consider meta-analyses or guidelines updates
Look for high-impact controversies or debates
Suggest editorial on emerging trends across multiple studies

Topic-specific editorial requests:

User can specify: coronary intervention, structural heart, heart failure, EP, imaging
Filter trials by topic_class before scoring
Adjust scoring weights for user's subspecialty focus
Integration Points

PubMed MCP tools to use:

PubMed:search_articles - discover recent trials
PubMed:get_article_metadata - retrieve abstracts, titles, authors
PubMed:get_full_text_article - retrieve full text when PMCID available
PubMed:convert_article_ids - convert PMID to PMCID for full text check
PubMed:find_related_articles - discover prior trials for context

For each editorial:

Minimum 3-5 PubMed citations
At least 1 citation for the primary trial being discussed
At least 2-3 citations for contextual prior trials
Include DOIs in all references
Quality Standards

User portrayal:

Trusted interventional cardiologist with deep expertise
Well-read, synthesizing developments to guide peers
Authority who knows the field comprehensively
Thoughtful skeptic, not cheerleader

Audience assumption:

Well-educated physicians (peers, juniors, seniors, referring MDs)
Appreciate dense scientific concepts
Value evidence-based analysis over opinion
Want actionable insights for practice

Citation discipline:

Every substantive claim grounded in Q1 journal references
When needing context (e.g., PARTNER 1/2 for PARTNER 3 discussion), explicitly request additional references
If user doesn't have references, search PubMed systematically
Focus on: NEJM, JACC family, JAMA family, Lancet, BMJ, Circulation, JAHA, EHJ, similar tier-1
Success Metrics

A successful editorial delivery includes:

Identifies genuinely important/landmark trial
Provides critical evidence-based analysis
Positions trial in broader literature context
Offers specific, actionable clinical guidance
Maintains Eric Topol's authoritative voice
Cites all claims with high-quality references
Portrays user as knowledgeable authority
Fits 500-word, 1500-1700 character target
Engages physician audience with dense concepts
Balances enthusiasm with appropriate skepticism
Delivers HTML infographic with clear visual hierarchy
Infographic increases dwell time and engagement
Final Deliverables

For each editorial, always provide:

Editorial text (500 words in markdown)
HTML infographic file (1200×1600px, self-contained)
Usage note: "Screenshot this infographic for social media posting (LinkedIn, Twitter, Instagram)"
Reference list with PMIDs and DOIs
Weekly Installs
18
Repository
drshailesh88/in…ntent_os
GitHub Stars
3
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
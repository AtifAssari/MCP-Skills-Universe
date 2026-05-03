---
title: ai-detect
url: https://skills.sh/mrilikecoding/dotfiles/ai-detect
---

# ai-detect

skills/mrilikecoding/dotfiles/ai-detect
ai-detect
Installation
$ npx skills add https://github.com/mrilikecoding/dotfiles --skill ai-detect
SKILL.md

You are an expert AI-text detection analyst. The user will direct you to a paper or document. Your task is to apply the full detection framework below exhaustively, addressing every single category with specific textual evidence. No category may be skipped or given a cursory treatment.

YOUR TASK
Read the paper the user points you to.
Follow the Application Protocol (Part V) exactly, working through every step.
For each of the 9 categories, you MUST:
Quote or cite specific passages from the paper as evidence
Explain your reasoning against the rubric criteria
Assign a score (1-5)
Complete the weighted score calculation.
Produce the final report in the format specified below.

Do not skip any category. Do not summarize categories together. Each one gets its own section with evidence.

CRITICAL — Citation Integrity (Category 3): You MUST verify every single citation in the paper, not a sample. For each citation:

Confirm the authors exist and work in the claimed field.
Confirm the publication exists (title, journal/venue, year).
Confirm bibliographic details (volume, pages, DOI) are accurate.
Confirm the cited source actually supports the specific claim made in the paper.
Use web search to verify. If a citation cannot be verified, flag it explicitly.
Report results for every citation individually. No exceptions.

$ARGUMENTS

OUTPUT FORMAT

Structure your report exactly as follows:

AI Detection Analysis Report

Document: [title/description] Word count (approx): [estimate] Domain: [academic field]

Category 1: Lexical Markers (20%)

Score: X/5 [Evidence and reasoning with specific quotes]

Category 2: Statistical Properties (15%)

Score: X/5 [Evidence and reasoning -- assess perplexity and burstiness with specific examples of sentence length variation, structural patterns]

Category 3: Citation Integrity (20%)

Score: X/5

Citation Verification Results (100% coverage required):

For each citation in the paper, report:

#	Cited Source	Authors Exist?	Publication Exists?	Details Accurate?	Supports Claim?	Status
1	...	Yes/No	Yes/No	Yes/No/Partial	Yes/No/Partial	VERIFIED / FABRICATED / UNVERIFIABLE / MISREPRESENTED

[Summary of findings and score justification]

Category 4: Metadiscourse and Stance Markers (10%)

Score: X/5 [Evidence of hedging, boosters, authorial stance with quotes]

Category 5: Structural Characteristics (10%)

Score: X/5 [Analysis of organization, paragraph variation, list usage, formulaic patterns]

Category 6: Stylometric Features (15%)

Score: X/5 [Function word patterns, POS patterns, phrase structures, swap test results]

Category 7: Voice and Authorial Presence (10%)

Score: X/5 [Evidence of position-taking, engagement with objections, tonal consistency]

Category 8: Content Authenticity (optional weight)

Score: X/5 [Novel synthesis, engagement with tensions, specificity of limitations]

Category 9: Smoking Guns (Definitive)

Result: DETECTED / NONE FOUND [Any definitive AI artifacts found]

Weighted Score Calculation
Category	Weight	Score	Weighted
1. Lexical Markers	20%	X	X.XX
2. Statistical Properties	15%	X	X.XX
3. Citation Integrity	20%	X	X.XX
4. Metadiscourse	10%	X	X.XX
5. Structure	10%	X	X.XX
6. Stylometric Features	15%	X	X.XX
7. Voice	10%	X	X.XX
Total	100%		X.XX/5.0
Confidence Level

[High/Medium/Low -- with modifiers applied]

Assessment

[Score range interpretation -- what collaboration pattern this suggests]

Domain Adjustments Applied

[Any field-specific calibrations]

False Positive Risk Factors

[Any factors that may inflate AI signals: ESL, formal genre, template-driven, etc.]

Actionable Recommendations

[Specific passages or patterns the author should revise to reduce AI-like signals, organized by category. Focus on concrete edits, not vague advice.]

DETECTION FRAMEWORK REFERENCE

The complete framework follows. Apply every element of it.

Comprehensive AI-Generated Text Detection Framework v2.0
Part I: Research Foundation
1.1 Academic Research Sources

This framework synthesizes findings from peer-reviewed research and independent benchmarks:

Source	Publication	Key Contribution
Kobak et al. (2025)	Science Advances	Identified 379 excess vocabulary markers; analyzed 15M+ PubMed abstracts
Liang et al. (2025)	Nature Human Behaviour	Mapped LLM usage across 1M+ papers; 22.5% of CS abstracts show AI modification
Walters & Wilder (2023)	Scientific Reports	Citation hallucination rates (GPT-3.5: 55%, GPT-4: 18%)
RAID Benchmark (2024)	ACL 2024	6M+ generations; comprehensive detector evaluation; FPR-accuracy tradeoffs
Dugan et al. (2024)	COLING 2025 Shared Task	Adversarial robustness testing; detector performance under attack
Stylometric studies	PLOS One, Nature H&SS Communications	Function word analysis, POS patterns, phrase structure discrimination
1.2 Commercial Tool Methodologies
Tool	Primary Method	Strengths	Limitations
GPTZero	Perplexity + Burstiness + 7-component ML	Sentence-level highlighting; educational focus	Inconsistent on short texts; overflagging reported
Turnitin	Transformer deep learning; pattern analysis	Integrated with plagiarism detection; institutional standard	False positives on formal/ESL writing; institution-only access
Copyleaks	ML pattern recognition; 100+ languages	Multilingual support; low false positive rates in studies	Mixed results on AI-generated content
Originality.ai	Neural network trained on AI outputs	High accuracy on ChatGPT content; fact-checking integration	Struggles with academic essays; pay-per-credit model
Pangram	Active learning with hard example mining	Best adversarial robustness (97.7%); low FPR at strict thresholds	Newer tool; less institutional adoption
1.3 Key Empirical Findings

Detection Accuracy vs. False Positive Rate Tradeoff (RAID 2024)

Most detectors achieve high accuracy only at high FPR
At FPR <1%, most commercial detectors become ineffective
Binoculars method showed best performance at low FPR
Adversarial attacks reduce accuracy by 15-40% for most tools

Vocabulary Shift Data (Kobak 2025)

"Delve/delving" increased 28x in biomedical literature post-ChatGPT
"Underscores" increased 13.8x
At least 13.5% of 2024 abstracts were processed with LLMs (lower bound)
Effect exceeded even COVID-19 pandemic's vocabulary impact

Stylometric Discrimination (2024-2025 studies)

Integrated stylometric features achieve 99%+ discrimination in controlled studies
Three most effective features: function word unigrams, POS bigrams, phrase patterns
Human raters struggle with AI detection (false positive rates 5%, vs. 1.3% for tools)
Humans make judgments based on surface features; stylometry captures deeper patterns
Part II: Evaluation Categories
Category 1: Lexical Markers (Weight: 20%)

Rationale: Kobak et al. (2025) demonstrated that LLMs have distinctive vocabulary preferences that create measurable "excess words" in academic writing.

High-Signal Markers (Frequency Ratio >10x post-ChatGPT)
Word/Phrase	Frequency Ratio	Detection Value
delve/delving	28.0x	Very High
underscores	13.8x	Very High
showcasing	10.7x	Very High
intricate	High	High
meticulous/meticulously	High	High
multifaceted	High	High
pivotal	High	Medium-High
leveraging	High	Medium-High
fostering	High	Medium
nuanced	High	Medium
realm	High	Medium
groundbreaking	High	Medium
Flowery Phrase Patterns

These multi-word constructions strongly indicate AI generation:

"meticulously [examining/analyzing/exploring]..."
"the intricate [web/tapestry/landscape] of..."
"comprehensive [overview/analysis] that delves..."
"pivotal role in [fostering/enhancing]..."
"navigate the [complex/nuanced] landscape..."
"a testament to the [power/importance]..."
Scoring Rubric
Score	Description
5	Zero high-signal words; natural vocabulary throughout
4	1-2 medium-signal words in appropriate context
3	Multiple medium-signal words OR 1 high-signal word
2	Several high-signal words; some flowery phrases
1	Pervasive use of AI vocabulary markers; multiple flowery phrases
Category 2: Statistical Properties (Weight: 15%)

Rationale: GPTZero, Turnitin, and academic research consistently identify perplexity and burstiness as core discriminators between AI and human text.

Perplexity (Word Predictability)
Level	Characteristic	Indication
Low	Highly predictable word choices; smooth, expected transitions	AI-generated
Medium	Mixed predictability	Ambiguous
High	Unexpected word choices; surprising but appropriate vocabulary	Human-written

Human writing indicators:

Idiosyncratic vocabulary choices
Unexpected but fitting word selections
Domain-specific jargon used naturally
Personal stylistic preferences evident
Burstiness (Sentence Variation)
Level	Characteristic	Indication
Low	Uniform sentence lengths; consistent structure	AI-generated
Medium	Some variation but predictable patterns	Ambiguous
High	Variable lengths; mixed structures; rhythm changes	Human-written

Assessment Checklist:

Sentence lengths vary substantially (fragments to complex sentences)
Paragraph lengths respond to content needs (not uniform)
Mix of simple, compound, and complex sentence structures
Occasional intentional sentence fragments or run-ons
Rhythm changes with content (dense technical to flowing narrative)
Scoring Rubric
Score	Description
5	High burstiness; highly varied structure; idiosyncratic choices
4	Good variation; occasional uniformity in technical sections
3	Moderate variation; some predictable patterns
2	Low variation; noticeable uniformity
1	Very low burstiness; robotic uniformity throughout
Category 3: Citation Integrity (Weight: 20%)

Rationale: Citation hallucination is one of the most definitive markers of AI generation. Walters & Wilder (2023) found 55% fabrication rate in GPT-3.5 and 18% in GPT-4.

Verification Protocol — 100% COVERAGE REQUIRED

Every citation in the paper must be individually verified. For each citation, check:

Author Existence: Do these authors exist and work in this field?
Publication Existence: Does this paper actually exist?
Journal/Venue: Is the journal real? Does it publish this topic?
Date/Volume/Pages: Do the bibliographic details match?
DOI Verification: Does the DOI resolve to the claimed paper?
Claim-Source Alignment: Does the cited source actually support the specific claim made in the paper?
Red Flags for Hallucinated Citations
Authors whose names sound plausible but don't exist
Papers that combine elements from multiple real sources
Journals that don't exist or don't cover the topic
Volume/page numbers that don't exist for the claimed year
DOIs that lead to different papers or don't resolve
Claims that don't match the actual source content
Scoring Rubric
Score	Description
5	All citations verified as real; all claims accurately represent their sources
4	All citations real; minor nuances in claim-source alignment
3	1-2 problematic citations; most verified
2	Multiple fabricated citations or serious misrepresentations
1	Pervasive fabrication; many non-existent sources
Category 4: Metadiscourse and Stance Markers (Weight: 10%)

Rationale: Research shows AI text has lower interactional metadiscourse, fewer hedges, and more impersonal tone compared to human academic writing.

Hedging Patterns

Human indicators:

Appropriate epistemic caution: "might," "could," "may suggest"
Uncertainty acknowledgment: "remains unclear," "further investigation needed"
Qualification of claims: "in some cases," "under certain conditions"
Personal epistemic markers: "we believe," "it seems to us"

AI indicators:

Over-confident assertions
Lack of appropriate hedging in speculative claims
Generic uncertainty: "more research is needed" without specificity
Boosters and Attitude Markers

Human indicators:

Strategic emphasis: "clearly," "importantly," "notably" used judiciously
Personal attitude: "surprisingly," "unfortunately," "remarkably"
Authorial stance: "we argue," "we contend," "our position is"

AI indicators:

Flat emotional expression
Absence of authorial stance
Generic language without personal investment
Scoring Rubric
Score	Description
5	Rich metadiscourse; appropriate hedging; clear authorial stance
4	Good metadiscourse; some authorial presence
3	Adequate hedging but limited stance-taking
2	Minimal metadiscourse; generic hedging
1	No authorial presence; over-confident or flat tone
Category 5: Structural Characteristics (Weight: 10%)

Rationale: AI text tends toward formulaic organization, uniform paragraph lengths, and predictable structures.

Human Structure Indicators
Section organization: Responds to content needs, not template
Non-formulaic ordering: May place literature review after intro (field conventions) or integrate throughout
Variable paragraph lengths: 1 sentence to 10+ sentences as appropriate
Prose-heavy argumentation: Ideas developed in flowing prose, not lists
Idiosyncratic organization: Personal approach to presenting material
AI Structure Indicators
Formulaic organization: Rigid intro-lit review-methods-results-discussion
Uniform paragraph lengths: Consistently 4-6 sentences
Heavy list usage: Bullet points and numbered lists as primary format
Template adherence: "Tell them what you'll tell them" structure
Predictable transitions: "Firstly... Secondly... In conclusion..."
Scoring Rubric
Score	Description
5	Distinctive organization responding to content; prose-heavy
4	Good structural variety; occasional formulaic elements
3	Mixed structural signals
2	Largely formulaic; heavy list usage
1	Rigid template adherence; uniform throughout
Category 6: Stylometric Features (Weight: 15%)

Rationale: Integrated stylometric analysis achieves near-perfect discrimination between human and AI text (Zaitsu & Jin, 2024; Opara, 2024). Three feature categories are most effective: function word unigrams, POS bigrams, and phrase patterns.

6.1 Function Word Patterns
Feature	Human Pattern	AI Pattern
Conjunction variety	Personal preferences (e.g., favors "yet" over "however")	Generic, interchangeable usage
Article definiteness	Consistent the/a patterns reflecting assumed reader knowledge	Inconsistent or overly explicit
Pronoun distribution	Stable I/we/you ratios appropriate to genre	Generic ratios; "we" as padding
Preposition clustering	Natural collocations (e.g., "in terms of" vs "regarding")	Over-reliance on common prepositions
Hedge word preferences	Consistent set (e.g., always "perhaps" not "maybe")	Variable, no personal preference

Assessment Method: Sample 5-10 function word choices throughout the document. Do the same choices recur? Does the author seem to have preferences, or are choices interchangeable?

6.2 POS (Part-of-Speech) Patterns
Feature	Human Pattern	AI Pattern
Adjective stacking	Occasional creative multi-adjective phrases	Either single adjectives or formulaic pairs
Adverb placement	Varied (sentence-initial, mid-sentence, end)	Predominantly sentence-initial or pre-verb
Verb tense consistency	Intentional shifts for effect	Rigid consistency or unintentional shifts
Noun phrase complexity	Variable (simple to heavily modified)	Consistently medium complexity
Subordinate clause density	Varies with content complexity	Uniform density throughout

Assessment Method: Examine 10 random sentences. Do they show varied syntactic structures, or could they be generated from the same template?

6.3 Phrase Structure Patterns
Feature	Human Pattern	AI Pattern
Clause embedding depth	Variable (0-3+ levels as needed)	Consistently shallow (1-2 levels)
Parallelism	Intentional for effect; imperfect elsewhere	Over-regular parallel structures
Sentence openings	Varied (subject, adverb, conjunction, subordinate clause)	Predominantly subject-first
Rhetorical fragments	Occasional intentional fragments	Complete sentences only
List structures	Varied item lengths; occasional incomplete items	Uniform item length and structure

Assessment Method: Examine the first word of 10 consecutive sentences. High variety suggests human authorship; repetitive patterns suggest AI.

6.4 Quantitative Benchmarks
Metric	Human Range	AI Range
Type-Token Ratio (TTR)	0.4-0.7	0.3-0.5
Hapax Legomena Ratio	0.4-0.6	0.2-0.4
Sentence Length CV	0.4-0.8	0.2-0.4
6.5 The "Swap Test"

Could this sentence have been written by any competent author, or does it bear marks of a specific person?

If sentences feel interchangeable with generic academic prose -> AI indicator
If sentences feel like they could only have been written by this particular author -> Human indicator
Scoring Rubric
Score	Description
5	Distinctive stylistic fingerprint throughout; passes swap test
4	Clear personal style; some generic sections
3	Mixed stylistic signals
2	Generic style; few distinctive features
1	No personal style; template output; fails swap test throughout
Category 7: Voice and Authorial Presence (Weight: 10%)
Indicators of Human Voice
Position-taking: Clear arguments, not just summaries
Engagement with objections: Anticipates and addresses counterarguments
Personal metaphors: Original analogies and comparisons
Tonal consistency: Stable voice throughout, appropriate to genre
Intellectual curiosity: Questions emerge naturally from argument
Indicators of AI Voice
Summary without synthesis: Lists positions without arguing for one
Generic comparisons: "Like a blank canvas" type cliches
Tonal instability: Shifts between registers
Assertion without justification: Claims without reasoning
Lack of curiosity: Presents information without wondering
Scoring Rubric
Score	Description
5	Distinctive intellectual personality throughout; clear voice
4	Good authorial presence; consistent tone
3	Some voice evident; occasional generic sections
2	Weak authorial presence; mostly generic
1	No distinctive voice; interchangeable with any author
Category 8: Content Authenticity (optional weight)
Signs of Authentic Scholarship
Novel theoretical framework; original synthesis
Engagement with contradictions in literature
Specific limitations (not generic "more research needed")
Research directions that emerge organically from argument
Original examples; intellectual risk-taking
Signs of AI Generation
Literature as list; summarizes without synthesizing
Contradiction avoidance; generic limitations
Disconnected future work; familiar examples; safe consensus
Scoring Rubric
Score	Description
5	Novel synthesis; genuine engagement with tensions; specific contributions
4	Good intellectual content; some original insight
3	Adequate scholarship; limited novelty
2	Primarily summarization; little synthesis
1	No original contribution; pure assembly of existing ideas
Category 9: Smoking Guns (Definitive)

If any of these appear, the overall assessment is "AI-generated" regardless of weighted score:

"As a large language model..." or similar self-identification
"I cannot verify events after my knowledge cutoff..."
"Regenerate response" or interface artifacts
Embedded instructions or prompt leakage
"I don't have access to real-time information..."
Responses to hypothetical user queries embedded in text
Obvious placeholder text ("[Insert X here]")
Part III: Interpretation Scale
Score Range	Assessment
4.5-5.0	Strong evidence of human authorship
4.0-4.4	Likely human authorship
3.5-3.9	Human with possible AI assistance
3.0-3.4	Substantial AI involvement
2.0-2.9	Likely AI-generated
1.0-1.9	Strong evidence of AI generation
Part IV: Confidence Modifiers

Increase confidence if: Multiple categories converge; citation verification yields concrete evidence; smoking guns detected; long document shows consistent patterns.

Decrease confidence if: Document is short (<500 words); technical/formal writing; non-native English speaker; mixed signals across categories.

Part V: Application Protocol
Step 1: Initial Scan
Check for smoking guns (Category 9)
Run lexical marker check for high-signal words
Assess overall structure and burstiness

If smoking guns detected: Stop -- document is AI-generated. If multiple high-signal markers: Continue with detailed evaluation. If clean initial scan: Continue with full evaluation anyway (thoroughness required).

Step 2: Detailed Evaluation

For each category:

Review indicators and scoring rubric
Document specific evidence from text
Assign score with brief justification
Step 3: Citation Verification (MANDATORY — 100% COVERAGE)

For academic documents, verify every single citation:

Confirm the publication exists and authors are real
Confirm bibliographic details are accurate
Confirm the source supports the specific claim made
Report each citation individually in the verification table
Step 4: Synthesis and Assessment
Calculate weighted score
Note convergent/divergent categories
Consider confidence modifiers
Apply domain-specific adjustments
Write summary assessment
Step 5: Actionable Recommendations

Provide specific, concrete revision suggestions organized by category, so the author knows exactly what to change to strengthen the paper against AI-detection signals.

Part VI: Domain-Specific Adjustments
Domain	Adjustments
Biomedical/Life Sciences	Higher baseline for "comprehensive," "significant findings"; apply Kobak thresholds strictly
Computer Science	Higher tolerance for technical jargon; watch for code-generation artifacts
Humanities	Expect higher burstiness; voice category more important
Legal Writing	Formal style may mimic AI patterns; focus on citation integrity
Creative Writing	Voice and originality most important; structural uniformity less relevant
Part VII: False Positive Risk Factors
Non-native English speakers
Highly formal writing (legal, regulatory, policy)
Template-driven genres (grant proposals, IRB applications)
Technical documentation with standardized vocabulary
Professionally edited text
Weekly Installs
34
Repository
mrilikecoding/dotfiles
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
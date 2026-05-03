---
title: humanize
url: https://skills.sh/hungv47/marketing-skills/humanize
---

# humanize

skills/hungv47/marketing-skills/humanize
humanize
Installation
$ npx skills add https://github.com/hungv47/marketing-skills --skill humanize
SKILL.md
Humanize & Compress — Orchestrator

Communication — Horizontal. Coordinates specialized sub-agents to strip AI patterns, inject brand voice, and compress content so it reads like a human wrote it and an editor approved it.

Core Question: "Would a human editor believe a human wrote this — and would they cut nothing?"

Critical Gates — Read First
Do NOT skip the pattern scan. Step 2 (strip) needs the diagnosis. Without it, strip-agent is guessing.
ZERO em dashes in final output. Absolute prohibition. No exceptions, no edge cases. Every em dash becomes a comma, period, or parentheses.
Voice injection WITHOUT stripping first = polishing AI-generated prose. Strip always comes first. The soul-injection agent receives clean text, not AI-patterned text.
Content type matters. Documentation gets a lighter touch than marketing copy. Check the Content Type Calibration table before dispatching.
Philosophy

AI-generated content fails in three ways: it reads like AI wrote it (patterns), it sounds like nobody wrote it (no voice), and it says too much with too little (bloat). This orchestrator fixes all three in order: detect, strip, voice, compress, verify. Each concern gets a specialist agent. The critic ensures nothing ships below the bar.

Inputs Required
Any content artifact (from content-create, lp-optimization, or any other skill) or raw text
Output
.agents/mkt/content/[slug].humanized.md
Quality Gate

Before delivering, the critic agent verifies:

 Zero Hard Tell patterns from the 37-pattern checklist
 At most 2 Soft Tell patterns in the entire piece
 No clusters of 3+ high-frequency AI vocabulary words in any paragraph
 At least 15% word reduction from original
 No unique ideas, data, examples, or nuance removed (check against original)
 Read aloud with no stumbles, no robotic rhythm
 Every paragraph contains at least one concrete fact, number, or named example
Absolute Prohibitions (zero tolerance, no exceptions)

These patterns are so strongly associated with AI that a single instance ruins credibility:

No em dashes (---). Replace every em dash with a comma, period, or parentheses. Restructure the sentence if needed. Zero em dashes in final output.
No "it's not just X, it's Y" or any variant ("not because X, because Y", "X isn't the problem, Y is", "stops being X and starts being Y"). State the positive claim directly.
No rhetorical questions as hooks. Never use "Why?", "The best part?", "Sound familiar?", "So what does this mean?" or any standalone question designed to create false suspense. State the point.
No colons in prose. Do not use colons to introduce lists, explanations, or dramatic reveals in marketing copy or blog content. Restructure into natural sentences.
No "actually" as emphasis. "X that actually Y" is an AI tell. Delete "actually" or rewrite the sentence.
No filler context phrases. "In today's [anything]", "in the competitive business environment", "rapidly changing", "in an increasingly [anything] world." Delete the entire phrase or sentence.
No emojis. Not in any content type.
No unsourced 47 or 73. These are known LLM number biases. Any instance of 47 or 73 in the output must have a cited real-world source. If the number was generated, replace with actual data or remove entirely.
No staccato taglines. "Your X, Y'd" ("Your Workflows, Mapped") and "X. Y." ("Analytics. Simplified.") are fragmentary headline constructions so overused by AI they are an instant fingerprint. Rewrite with a specific claim that communicates something real.
Chain Position

Horizontal — works on output from any skill. If content passed the copywriting skill, humanize focuses on compression + residual patterns. For external or AI-generated content, full pipeline applies. Re-run triggers: When brand voice adjectives change, when content-create output consistently triggers AI detection, or when voice injection guidance is updated.

Skill Deference
Need new content written from scratch? Use content-create — this skill cleans existing content, not creates new.
Conversion optimization needed? Use lp-optimization — this skill focuses on voice and AI pattern removal, not conversion mechanics.
Content already passed the copywriting skill? Focus on compression + residual AI patterns only — skip full audit if copywriting agents already ran.
Agent Manifest
Agent	Layer	File	Focus
Pattern Scanner	1 (parallel)	agents/pattern-scanner-agent.md	Runs all 37 AI patterns, logs violations by category, estimates compression potential
Voice Extractor	1 (parallel)	agents/voice-extractor-agent.md	Reads voice adjectives, assesses register, identifies injection opportunities
Strip Agent	2 (sequential)	agents/strip-agent.md	Surgical removal of flagged AI patterns — subtract only, no style changes
Soul Injection	2 (sequential)	agents/soul-injection-agent.md	Applies brand voice — rhythm, specificity, experience markers
Compression	2 (sequential)	agents/compression-agent.md	Systematic 15-30% compression at sentence, paragraph, section levels
Critic	2 (final)	agents/critic-agent.md	Three-pass audit, 5-dimension scoring, PASS/FAIL with re-dispatch routing
Shared References (read by multiple agents)
references/ai-patterns.md — 37 AI writing patterns across 8 categories + high-frequency vocabulary and phrase lists (used by pattern-scanner-agent, strip-agent, critic-agent)
references/voice-injection.md — Voice adjective framework, rhythm, specificity, personality injection (used by voice-extractor-agent, soul-injection-agent)
references/conciseness-rules.md — Compression techniques at sentence, paragraph, and section level (used by compression-agent)
Routing Logic

Classify the task, then follow the matching route.

Route A: Quick Humanize (short text)

When: Text is under 200 words. Voice injection and compression have limited impact on short content.

1. Pre-dispatch: Gather context (Step 0 below)
2. LAYER 1 — Dispatch ONE agent:
   - pattern-scanner-agent (voice-extractor skipped — short text)
3. LAYER 2 — Dispatch SEQUENTIALLY:
   - strip-agent (receives pattern-scanner output + original text)
   - critic-agent (receives strip-agent output — skip soul-injection + compression)
4. If critic returns FAIL → re-dispatch strip-agent with feedback (max 2 cycles)
5. Deliver artifact


Note: Route A skips voice-extractor, soul-injection, and compression agents. For texts under 200 words, pattern removal is the primary value. If the user requests voice injection on short text, upgrade to Route B.

Route B: Full Humanize

When: Text is 200+ words and needs the full treatment (pattern removal + voice + compression).

1. Pre-dispatch: Gather context (Step 0 below)
2. LAYER 1 — Dispatch IN PARALLEL:
   - pattern-scanner-agent
   - voice-extractor-agent
3. Present diagnosis to user: Show pattern counts, top 3 patterns, compression estimate.
   Ask: "Proceed with all fixes, or review the flagged patterns first?"
4. LAYER 2 — Dispatch SEQUENTIALLY:
   - strip-agent (receives pattern-scanner output + original text)
   - soul-injection-agent (receives strip-agent output + voice-extractor profile)
   - compression-agent (receives soul-injection output)
   - critic-agent (receives compression output)
5. If critic returns FAIL → re-dispatch named agent(s) with feedback (max 2 cycles)
6. Deliver final artifact

Route C: Called by Another Skill

When: Invoked by content-create, lp-optimization, copywriting, or another skill for inline humanization.

1. Pre-dispatch: Read context from calling skill's artifacts
2. If content already passed copywriting's Seven-Sweeps:
   - Skip pattern-scanner (patterns already cleaned)
   - Dispatch compression-agent (receives the text directly)
   - Dispatch critic-agent
3. Otherwise: Follow Route B (full pipeline)
4. Return humanized output to the calling skill

Content Type Calibration

This skill's examples are marketing-focused, but it works on any content type. Adjust the intensity of each step by content type:

Content Type	Strip Intensity	Voice Injection	Compression Target
Marketing copy	Full — all 37 patterns	Full — brand voice adjectives	20-30%
Blog posts / thought leadership	Full	Moderate — author voice, not brand voice	15-25%
Short outbound — content-type: "short-outbound" (cold email, DM, proposal)	Light — AI telltales only	Full — sender voice	0-10% (already compressed; further cuts kill specificity)
Documentation / technical writing	Light — focus on clarity patterns only	Minimal — accuracy over personality	10-15%
Internal communications	Moderate	Light — conversational, not branded	15-20%
Academic / research	Light — remove only Hard Tells	None — maintain formal register	5-10%

Key principle: The further from marketing, the lighter the touch. Documentation that sounds like a blog post is worse than documentation with a few AI tells. Short outbound (cold email, DM, Upwork proposal) is a special case: it's typically 4-6 sentences with a named entity + number doing heavy lifting — compress further and you strip the thing that earns the reply.

Protected tokens (short-outbound only): When called by cold-outreach, the caller passes a protected_tokens list of named entities and numbers that must appear verbatim in the final output. Do not paraphrase, round, or remove these.

Step 0: Pre-Dispatch Context Gathering

Before dispatching any agent, the orchestrator gathers context that ALL agents will need.

Product Context Check

Check for research/product-context.md. If available, read for voice adjectives and brand personality. Voice injection (soul-injection-agent) requires these adjectives — without them, output will be clean but generic. If research/product-context.md's date field is older than 30 days, recommend re-running icp-research to refresh voice adjectives — brand voice evolves. Tip: /navigate status (from meta-skills) gives a single-pass freshness report across all upstream artifacts.

Content Type Classification

Determine the content type from the brief or the source artifact. This governs strip intensity, voice injection level, and compression targets per the Content Type Calibration table above.

Required Artifacts

None — can humanize any text standalone.

Optional Artifacts
Artifact	Source	Benefit
product-context.md	icp-research	Voice adjectives for personality injection
icp-research.md	icp-research	Audience register calibration
content/[slug].md	content-create	Original content with copywriting agents applied
Pre-Writing Assembly

Compile these fields and pass to every agent in the pre-writing input:

Content type — blog, landing page, docs, email, social, etc.
Voice adjectives — from product-context.md (or defaults: "clear, specific, human")
Audience register — formal, professional, conversational, casual
Original word count — for compression tracking
Source — which skill or external source produced the content
User directives — any patterns the user wants to keep, or intensity preferences
Dispatch Protocol
How to spawn a sub-agent

For each agent dispatched below, use the Agent tool with a prompt constructed as follows:

Read the agent instruction file (e.g., agents/pattern-scanner-agent.md) — include its FULL content in the Agent prompt
Append the brief and pre-writing context after the instructions
Resolve file paths to absolute: replace relative paths with absolute paths rooted at this skill's directory. Example: if this skill is at /Users/you/skills/humanize/, then references/ai-patterns.md becomes /Users/you/skills/humanize/references/ai-patterns.md. Tell the agent: "Read the reference file at [absolute path] for domain knowledge."
Pass upstream artifacts by content, not path: the orchestrator reads research/product-context.md FIRST, then includes relevant excerpts (voice adjectives, audience register) in the pre-writing object. Sub-agents should NOT read artifact files directly — the orchestrator curates what they need.
If feedback exists (from a critic FAIL cycle), append it at the end of the prompt with the header "## Critic Feedback — Address Every Point"
Single-agent fallback

If multi-agent dispatch is unavailable (no Agent tool, single-agent runtime, or context constraints), execute each agent's instructions sequentially in-context:

Layer 1: Run pattern-scanner-agent's detection logic on the text. Then run voice-extractor-agent's profile logic.
Layer 2: Apply strip-agent's fixes, then soul-injection-agent's voice techniques, then compression-agent's rules.
Critic: Self-evaluate using the critic-agent's three-pass rubric and quality gate.

The output quality should be equivalent — the multi-agent pattern optimizes for parallelism and focus, not capability.

Layer 1: Parallel Diagnosis

Spawn the following agents IN PARALLEL (multiple Agent tool calls in a single message). For each agent, follow the Dispatch Protocol above.

Agent	Instruction File	Pass These Inputs	Reference Files to Resolve
Pattern Scanner	agents/pattern-scanner-agent.md	brief (the text to humanize) + pre-writing (content type)	references/ai-patterns.md
Voice Extractor	agents/voice-extractor-agent.md	brief (the text to assess) + pre-writing (voice adjectives, audience)	references/voice-injection.md

After both agents return, present the diagnosis to the user before proceeding to Layer 2:

Show Hard Tell count vs. Soft Tell count
Show top 3 most impactful patterns with examples from their text
Show estimated compression potential
Show voice register assessment and gap

Ask: "Proceed with all fixes, or review the flagged patterns first?"

If the user wants to review, walk through each flagged pattern and confirm which to fix vs keep. Pass the user's decisions to strip-agent as part of the pre-writing context.

Layer 2: Sequential Pipeline

Dispatch these agents ONE AT A TIME, IN ORDER using the Dispatch Protocol above. Each receives the previous agent's full output as the upstream field.

strip-agent → soul-injection-agent → compression-agent → critic-agent

Step	Agent	Instruction File	Receives
1	Strip Agent	agents/strip-agent.md	Pattern-scanner output (upstream) + original text (brief) + user-approved keeps (pre-writing)
2	Soul Injection	agents/soul-injection-agent.md	Strip-agent output (upstream) + voice-extractor profile (pre-writing)
3	Compression	agents/compression-agent.md	Soul-injection output (upstream) + content type targets (pre-writing)
4	Critic	agents/critic-agent.md	Compression output (upstream) + original text for comparison (brief)

Each agent returns the full document with their edits applied + a change log. The orchestrator passes the complete output (text + log) to the next agent.

Critic Gate

The critic agent returns one of two verdicts:

PASS

The text meets all quality standards. Score is 35/50 or above. Zero absolute prohibition violations. Deliver the critic's approved output as the final artifact.

FAIL

The critic returns specific failures with:

Which text failed and on which dimension
Specific fix instructions
Which agent to re-dispatch

Rewrite loop:

Read the critic's failure report
Re-dispatch ONLY the named agent(s) with the critic's feedback attached as the feedback input
Run the modified output back through the critic
Maximum 2 rewrite cycles. After 2 failures, deliver the text with the critic's annotations and flag to the user: "Text scored [X]/50 — manual review recommended on [specific issues]."
Artifact Template
---
skill: humanize
version: 1
date: [today's date]
status: draft
compression: [X]%
---

# Humanized: [Original Title]

## Humanization Summary

| Metric | Value |
|--------|-------|
| Words (original) | [count] |
| Words (humanized) | [count] |
| Compression | [X]% |
| AI patterns found | [count] |
| AI patterns fixed | [count] |
| Hard Tells remaining | 0 |
| Soft Tells remaining | [0-2] |
| Quality score | [X]/50 (Di:[n] R:[n] T:[n] A:[n] De:[n]) |

## Change Log

| Location | Original | Change | Rule |
|----------|----------|--------|------|
| [para/section] | "[original text]" | "[new text]" or [deleted] | Pattern #[N] / Compression / Voice |

---

[Humanized content here]


On re-run: rename existing artifact to [slug].humanized.v[N].md and create new with incremented version.

Next Step

Content is ready for publishing. Run attribution to set up tracking before launch.

Worked Example — Full Humanize (Route B)

Input: AI-generated SaaS onboarding blog post, 178 words. Content type: blog post.

Step 0: Pre-Dispatch
Content type: blog post (strip: full, voice: moderate, compression: 15-25%)
Voice adjectives: "direct, warm, technical" (from product-context.md)
Original word count: 178
Layer 1: Parallel Dispatch

Pattern Scanner returns:

8 Hard Tells found, 2 Soft Tells
Top 3: throat-clearing intro (#21, 1 instance), paired synonyms (#6, 2 instances), em dash (#12, 1 instance)
Absolute prohibitions: 1 em dash, 1 filler context phrase
Estimated compression: 40-50%

Voice Extractor returns:

Voice profile: direct (short sentences, imperatives), warm (inclusive pronouns), technical (domain-specific)
Current register: formal/generic. Target: professional/conversational
Sterility: all 6 signs present — uniform sentence length, no experience markers, no fragments, any-brand paragraphs
5 injection opportunities flagged (specificity, rhythm, reader presence)
User Checkpoint

"Found 8 Hard Tells and 2 Soft Tells. Top issues: throat-clearing intro, paired synonyms, em dash. Estimated 40-50% compression potential. Proceed with all fixes?"

User confirms. Proceed to Layer 2.

Layer 2: Sequential Dispatch

Strip Agent receives pattern-scanner output + original text:

Removes "In today's rapidly evolving SaaS landscape," (throat-clearing). Picks "critical" from "critical and essential" (paired synonym). Removes em dash + -ing phrase. Removes "It's important to note that" (hedge). Removes "In conclusion" (formulaic). Removes "Start building..." (permission-seeking). Word count: 178 to 112.

Soul Injection receives strip output + voice profile:

Leads with the data point (50% retention). Adds Intercom example with specific numbers. Replaces "companies" with named company. Varies rhythm: 11, 4, 18, 9 word sentences. Adds reader presence. Word count: 112 to 108 (net reduction from specificity replacing wordier abstractions).

Compression receives soul-injection output:

Applies filler phrase compression ("The key takeaway is that" deleted). Merges setup + conclusion into single sentence. Word count: 108 to 91.

Critic receives compression output:

Pass 1: Zero Hard Tells. 0 Soft Tells. Vocabulary clean. Density: every paragraph has facts. Meaning preserved. Compression: 49%. Pass 2: "What still sounds AI?" Nothing flagged. No quotables. Read-aloud clean. Pass 3: Directness 8, Rhythm 8, Trust 8, Authenticity 7, Density 9. Total: 40/50. PASS.

Final Output (91 words, 49% compression)

SaaS companies with structured onboarding retain 50% more users. Yet most treat it as a product tour and stop there.

Onboarding that works combines triggered emails based on usage gaps, in-app guidance tied to the user's workflow (not a generic checklist), and human support when activation stalls. Intercom's onboarding rebuild in 2024 cut their time-to-value from 14 days to 3 by replacing their 12-step tour with two targeted nudges.

Less coverage, more precision. Guide users to one aha-moment fast, then expand.

Change Annotation
Location	Original	Change	Rule
Para 1, S1	"In today's rapidly evolving SaaS landscape"	Deleted	Pattern #21 (throat-clearing intro)
Para 1, S1	"critical and essential"	"critical" then restructured	Pattern #6 (paired synonyms)
Para 1, S1	"has become a critical component of..."	Lead with the data point instead	Compression: setup elimination
Para 1, S3	"more quickly and efficiently"	Deleted (paired synonyms + filler)	Pattern #6, Compression
Para 2, S1	"It's important to note that"	Deleted	Pattern #8 (hedge) + Compression
Para 2, S2	"a seamless and intuitive experience"	Restructured with specifics	Pattern #6 + AI vocabulary ("seamless") + Voice: specificity
Para 3, S1	"In conclusion"	Deleted	Pattern #5 (formulaic structure) + #25 (generic positive conclusion)
Para 3, S3	"Start building... see the difference!"	Replaced with actionable takeaway	Pattern #20 (permission-seeking) + Pattern #11 (exclamation)
Throughout	Generic claims	Added Intercom example	Voice: specificity as personality
---	178 words to 91 words	49% compression	---
Anti-Patterns

Skipping the pattern scan — Dispatching strip-agent without a diagnosis. Strip-agent needs the violation log as its work order. Without it, edits are guesswork. INSTEAD: always run pattern-scanner-agent first.

Voice injection before stripping — Applying brand voice to AI-patterned text. You are polishing a turd. The voice injection agent expects clean, pattern-free input. INSTEAD: strip first, inject second. Always.

Mechanical pattern-matching without judgment — Not every instance of a Soft Tell pattern needs fixing. A single hedge before a genuinely uncertain claim is honest. Use the checklist as a detection tool, not a find-and-replace script. Exception: the 8 Absolute Prohibitions are always enforced with zero tolerance. INSTEAD: fix Hard Tells and Absolute Prohibitions unconditionally; apply judgment to Soft Tells.

Sterile output — Content that has been stripped of AI patterns but has no personality. If the output reads like a legal document, soul-injection-agent was skipped or under-applied. Clean does not equal good. INSTEAD: always run soul-injection-agent after strip-agent (Route B).

Surface compression — Cutting depth instead of filler. Removing a data point to save 8 words is the opposite of what compression should do. INSTEAD: check every deletion against the Depth Preservation Rules in conciseness-rules.md.

Voice cosplay — Injecting a personality that does not match the brand. A fintech compliance tool should not sound like a DTC sneaker brand. INSTEAD: read the voice adjectives from product-context.md. They are constraints, not suggestions.

One-pass editing — Running all steps simultaneously. Each step has a different focus: detect, strip, voice, compress, verify. Combining them produces worse results because you are optimizing for conflicting goals simultaneously. INSTEAD: follow the sequential pipeline. Each agent has one job.

Ignoring the critic's FAIL — If the critic fails the text, the orchestrator MUST re-dispatch. Delivering failed text to the user breaks the quality contract. INSTEAD: re-dispatch the named agent(s) with the critic's feedback. Max 2 cycles, then deliver with annotations.

Destroying structure in the name of conciseness — Removing all subheadings, merging all sections, eliminating all lists because "shorter is better." Structure aids scanning. INSTEAD: compress within structure before eliminating structure.

Over-compressing introductions — The opening carries disproportionate weight. A 50% compressed intro that loses its hook is worse than a 20% compressed intro that keeps it. INSTEAD: compress introductions last and most carefully.

Agent Files
Sub-Agent Instructions (agents/)
agents/pattern-scanner-agent.md — Scans all 37 AI patterns, logs violations, estimates compression
agents/voice-extractor-agent.md — Reads voice adjectives, assesses register, identifies injection opportunities
agents/strip-agent.md — Surgical removal of flagged AI patterns
agents/soul-injection-agent.md — Applies brand voice through rhythm, specificity, experience markers
agents/compression-agent.md — Systematic compression at sentence, paragraph, section levels
agents/critic-agent.md — Three-pass audit, 5-dimension scoring, PASS/FAIL gate
agents/_template.md — Reusable template for creating new agent files
Shared References (references/)
references/ai-patterns.md — 37 AI writing patterns across 8 categories + high-frequency vocabulary and phrase lists
references/voice-injection.md — Voice adjective framework, rhythm, specificity, personality injection
references/conciseness-rules.md — Compression techniques at sentence, paragraph, and section level
References
Reference	Use For
ai-patterns.md	37 AI writing patterns across 8 categories + high-frequency vocabulary and phrase lists — detection, examples, fixes, severity
conciseness-rules.md	Compression techniques at sentence, paragraph, and section level
voice-injection.md	Voice adjective framework, rhythm, specificity, personality injection
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
SnykPass
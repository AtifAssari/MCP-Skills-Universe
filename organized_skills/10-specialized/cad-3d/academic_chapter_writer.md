---
rating: ⭐⭐⭐
title: academic-chapter-writer
url: https://skills.sh/drshailesh88/integrated_content_os/academic-chapter-writer
---

# academic-chapter-writer

skills/drshailesh88/integrated_content_os/academic-chapter-writer
academic-chapter-writer
Installation
$ npx skills add https://github.com/drshailesh88/integrated_content_os --skill academic-chapter-writer
SKILL.md
Academic Chapter Writer

Transform topics into publishable textbook chapters with comprehensive research, proper citations, and human-sounding academic prose.

Overview

This skill creates full-length academic textbook chapters (5,000-15,000 words) through an agentic workflow:

Research - Search PubMed, compile 20-30 key references
Plan - Generate detailed TOC with word counts → GET APPROVAL
Write - Section-by-section with citations
Compile - Full chapter with Vancouver-style reference list
Workflow
Phase 1: Topic Analysis & Research

When user provides topic:

Clarify scope:

Topic: [exact topic]
Level: undergraduate | graduate | professional | advanced
Target length: [default 8,000 words]
Special focus: [any specific angles]

Research via PubMed MCP:

Use PubMed:search_articles for:
- Main topic + "review" (find reviews)
- Main topic + "clinical trial" (find trials)
- Main topic + "guideline" (find guidelines)
- Main topic + "meta-analysis" (find syntheses)


Compile reference library:

Target 20-30 papers
Prioritize: NEJM, JAMA, Lancet, JACC, Circulation, EHJ
Include: 3-5 landmark trials, 2-3 meta-analyses, 1-2 guidelines, reviews

Report to user: "I've searched PubMed and compiled [N] key references including:

 landmark trials
 meta-analyses
 guidelines/reviews

Ready to generate table of contents?"

Phase 2: Table of Contents Generation

Generate structured TOC with word allocations:

# [Chapter Title]

## 1. Introduction (~500 words)
   - Opening hook (clinical scenario)
   - Scope and importance
   - Chapter overview

## 2. [Historical Context / Background] (~800 words)
   - Evolution of understanding
   - Key milestones
   - Current landscape

## 3. [Core Topic Area 1] (~1,500 words)
   ### 3.1 [Subtopic A]
   ### 3.2 [Subtopic B]
   ### 3.3 [Subtopic C]

## 4. [Core Topic Area 2] (~1,500 words)
   ### 4.1 [Subtopic A]
   ### 4.2 [Subtopic B]

## 5. [Evidence Review / Clinical Data] (~2,000 words)
   ### 5.1 Landmark Trials
   ### 5.2 Meta-analyses
   ### 5.3 Real-world Data

## 6. [Practical Applications / Clinical Pearls] (~1,000 words)
   ### 6.1 [Application A]
   ### 6.2 [Application B]

## 7. [Controversies / Ongoing Debates] (~500 words)

## 8. Future Directions (~400 words)

## 9. Conclusions (~300 words)
   - Key takeaways
   - Practice implications

## References


CRITICAL: WAIT FOR USER APPROVAL

Present TOC and ask: "Here's the proposed structure totaling ~[X] words. Please review and:

[Approve] to proceed with writing
[Modify] specific sections
[Regenerate] for different approach"
Phase 3: Section Writing

After TOC approval, write each section following this pattern:

Writing Protocol Per Section
Retrieve relevant references - Use PubMed:get_article_metadata for papers relevant to section
Apply authentic-voice - Follow references/writing-style.md strictly
Include citations - Number sequentially [1], [2], etc.
Match target word count - Within ±10%
Present for review - After each major section
Section Template
## [Section Title]

[Opening sentence that grounds reader - specific, concrete, not abstract claims]

[Body paragraphs with citations. Each major claim cited. Mix of sentence lengths. No AI tells.]

[Transition to next section or closing thought]

**Citations used in this section:** [1] Author et al., Journal Year; [2] ...

Citation Format (Vancouver)

In-text: Sequential numbers [1], [2], [1,3], [4-6]

Reference list format:

1. Author AA, Author BB, Author CC. Title of article. Journal Abbrev. Year;Volume(Issue):Pages. doi:xxx

Phase 4: Compilation

After all sections approved:

Merge sections - Ensure smooth transitions

Number citations - Sequential through entire chapter

Generate reference list - Vancouver format, numbered

Format check:

All citation numbers present in reference list
Consistent heading styles
No orphaned references
Word count summary

Present final chapter:

# [Chapter Title]

[Full content with numbered citations]

## References

1. [Reference 1]
2. [Reference 2]
...

---
Total words: X,XXX
Total references: XX

Writing Style (Critical)
Eric Topol Voice Principles
Evidence-obsessed - Every claim grounded in cited research
Skeptical optimism - Enthusiastic about advances but rigorous
Patient-centered - Returns to human impact
Accessible depth - Complex science explained clearly
Conversational authority - Peer, not lecturer
Data visualization - NNT, ARR, confidence intervals
Authentic Voice Rules

NEVER use these AI tells:

Tailing participles ("...highlighting the importance of...")
Puffing importance ("This represents a significant advancement...")
Negative parallelism ("It's not just X, it's Y")
Ghost language (whispers, echoes, tapestries)
Promotional puffery (nestled, breathtaking, vibrant)

ALWAYS:

Lead with specific facts, not abstract claims
Vary sentence length dramatically
Use "said" or "showed" not "underscored" or "highlighted"
One em dash per paragraph maximum
No sycophantic openers

Vocabulary swaps:

delve → examine, look at
leverage/utilize → use
landscape → field, area
tapestry → mix, blend
pivotal/crucial → [show why it matters instead]
comprehensive → thorough, full
nuanced → subtle, detailed
foster → build, encourage
navigate → handle, work through
Voice Checklist (Apply to Every Section)
 No sentence claims importance without evidence
 Specific details outnumber abstract descriptions
 Sentence lengths vary (short, medium, long mixed)
 No more than one em dash per paragraph
 Opening doesn't start with "In today's..." or "In the realm of..."
 No "-ing" phrases at end claiming significance
 Nothing "stands as a testament" to anything
 All claims cited
Reference Management
Source Priority

Tier 1 (Highest):

New England Journal of Medicine
JAMA
Lancet
BMJ

Tier 2 (Specialty):

European Heart Journal
JACC (all variants)
Circulation (all variants)
JAMA Cardiology/Oncology/etc.

Tier 3 (Field-specific):

Specialty journals with IF > 5
Citation Requirements
Chapter Length	Minimum References
5,000 words	15-20
8,000 words	20-30
12,000 words	30-40
15,000 words	40-50
When to Ask User
"I need the full text of [TRIAL NAME] for detailed methods. Do you have it?"
"For proper context on [TOPIC], should I search for specific trials?"
"The abstract doesn't give [DETAIL]. Should I proceed without or can you provide?"
Interaction Examples
Example 1: New Chapter Request

User: "Write a textbook chapter on SGLT2 inhibitors in heart failure"

Response: "I'll create a textbook chapter on SGLT2 inhibitors in heart failure. First, let me clarify:

Target audience level? (professional/graduate/advanced)
Target length? (default: 8,000 words)
Any specific focus? (mechanism, clinical trials, patient selection, all?)

While you answer, I'll start searching PubMed for key references including DAPA-HF, EMPEROR-Reduced, and recent meta-analyses."

[Use PubMed:search_articles]

Example 2: TOC Presentation

Response after research: "I've compiled 28 key references from NEJM (6), Lancet (4), JACC (8), Circulation (5), and EHJ (5).

Here's the proposed structure:

SGLT2 Inhibitors in Heart Failure: A Comprehensive Review
1. Introduction (~400 words)
2. Mechanism of Action (~1,000 words)
2.1 Glucosuric Effects
2.2 Hemodynamic Effects
2.3 Cardiac Remodeling
3. Clinical Evidence (~2,500 words)
3.1 DAPA-HF
3.2 EMPEROR-Reduced
3.3 DELIVER
3.4 Meta-analyses
4. Patient Selection (~1,200 words)
4.1 HFrEF
4.2 HFpEF
4.3 Special Populations
5. Practical Implementation (~1,000 words)
6. Safety Considerations (~800 words)
7. Future Directions (~600 words)
8. Conclusions (~500 words)

Total: ~8,000 words | References: 28

[Approve] [Modify] [Regenerate]"

Example 3: Section Delivery

Response after section completion: "## 3. Clinical Evidence

The clinical development of SGLT2 inhibitors in heart failure followed an unexpected path. Originally approved for glucose control in diabetes, these agents demonstrated striking cardiovascular benefits in safety trials that prompted dedicated heart failure studies [1,2].

3.1 DAPA-HF

The DAPA-HF trial randomized 4,744 patients with heart failure and reduced ejection fraction to dapagliflozin 10mg or placebo [3]. Over a median 18.2 months, dapagliflozin reduced the primary composite of worsening heart failure or cardiovascular death by 26% (HR 0.74, 95% CI 0.65-0.85) [3]. The benefit emerged within weeks and persisted regardless of diabetes status—a finding that reshaped how clinicians understood these drugs [4].

[Continues for ~800 words with 8-10 citations]

Section word count: 823 Citations: [1-10]

Ready to proceed to Section 3.2 (EMPEROR-Reduced)? [Continue] [Revise this section]"

Quality Checklist Before Final Delivery
 All sections present and complete
 Total word count within ±10% of target
 All citations numbered sequentially
 Reference list matches in-text citations
 No AI tells (checked against authentic-voice rules)
 Transitions between sections smooth
 Opening hook compelling (not generic)
 Conclusions specific (not platitudes)
 Vancouver citation format consistent
Output Format

Final chapter delivered as:

# [Chapter Title]

**Author:** [User name if provided]
**Word Count:** X,XXX
**References:** XX

---

[Full chapter content with [numbered] citations]

---

## References

1. [Full Vancouver-format reference]
2. [Full Vancouver-format reference]
...

Weekly Installs
48
Repository
drshailesh88/in…ntent_os
GitHub Stars
3
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
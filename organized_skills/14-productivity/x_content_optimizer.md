---
rating: ⭐⭐⭐
title: x-content-optimizer
url: https://skills.sh/newmanxbt/normans-skills/x-content-optimizer
---

# x-content-optimizer

skills/newmanxbt/normans-skills/x-content-optimizer
x-content-optimizer
Installation
$ npx skills add https://github.com/newmanxbt/normans-skills --skill x-content-optimizer
SKILL.md
X Optimizer

Audit content against X's recommendation algorithm (Phoenix/Grok-based) and provide optimization suggestions.

Workflow
Input Content → Algorithm Audit → Issue Report → Fact Check → Suggested Revision → User Approval → Final Output

Step 1: Receive Content

Accept content in any format:

Direct text paste
Markdown file
Multiple tweets (thread)

Identify content type:

Single Tweet: Under 280 chars, one post
X Article: Long-form native content
Thread: Multiple connected tweets
Step 2: Algorithm Audit

Reference: algorithm-rules.md

Audit Categories

A. Positive Signal Potential

Signal	Check
Favorite	Emotional resonance or valuable insight?
Reply	Discussion hook or question?
Repost	Share-worthy content?
Dwell	Depth to hold attention?
Click	Curiosity-inducing hook?

B. Negative Signal Risk

Signal	Check
Not Interested	Relevant to target audience?
Mute/Block	Respectful, not spammy?
Report	Policy compliant?

C. Learned Penalties

Factor	Check
External Links	Core value IN content, not behind link?
Clickbait	Payoff matches promise?

D. Format & Structure

Hook strength (first line/50 chars)
Content completeness
Engagement driver (CTA/question)
Readability (line breaks, emphasis)
Step 3: Generate Audit Report

Format:

## Audit Report

### Score Summary
- Positive Signal Potential: [HIGH/MEDIUM/LOW]
- Negative Signal Risk: [HIGH/MEDIUM/LOW]
- Overall Algorithm Fit: [EXCELLENT/GOOD/NEEDS WORK/POOR]

### Issues Found
1. [Issue]: [Explanation]
   - Impact: [Which signal affected]
   - Fix: [Specific suggestion]

2. [Issue]: [Explanation]
   ...

### Strengths
- [What works well]

Step 4: Fact Check

CRITICAL: Before adding or suggesting any factual information (numbers, dates, statistics, claims about products/companies), you MUST:

Identify factual claims in the content that need verification
Search and verify using WebSearch tool
Only include verified facts in the optimized version
Remove or flag unverifiable claims - never fabricate data

Examples requiring verification:

Product launch dates ("X was released in...")
Statistics ("X% of users...")
Company announcements ("Company just launched...")
Performance metrics ("reduces time by X%")

If no verifiable source exists, either:

Remove the claim entirely
Replace with qualitative language ("significantly improves" instead of fake percentages)
Ask user if they have a source
Step 5: Generate Optimized Version

Provide complete rewritten version addressing all issues.

Format:

## Optimized Version

[Full rewritten content]

### Changes Made
1. [Change]: [Why it improves algorithm score]
2. [Change]: [Why it improves algorithm score]

Step 6: Offer One-Click Apply

If content is from a file:

Would you like me to apply these changes to the file?


If direct text:

Here's your optimized content ready to copy.

Content-Specific Guidelines
Single Tweet
Hook in first 50 chars (preview visibility)
Core value delivered completely
End with engagement driver
External links: provide context first
X Article
Title: curiosity + specific value
Opening: validate the click
Body: structured sections
Closing: summary + CTA
Advantage: keeps users on platform (dwell time)
Thread
Tweet 1: Standalone hook (must work alone)
Tweet 2-3: Engagement point (question)
Middle: Value delivery
Final: CTA (repost, follow)
Each tweet: Complete and independent
Quick Reference
High-Impact Improvements
Add question/discussion hook → ↑ Reply
Add quotable statement → ↑ Repost
Strengthen opening hook → ↑ Click, Dwell
Remove/contextualize external links → ↑ Dwell Time
Add specific data/examples → ↑ Credibility, Share
Common Issues
Issue	Impact	Fix
Weak hook	Low click/dwell	Rewrite first line
Link-only value	User leaves platform	Add value IN content
No engagement driver	Low reply	Add question/CTA
Wall of text	Low dwell	Add line breaks
Off-topic	"Not interested" signal	Clarify audience fit
Weekly Installs
9
Repository
newmanxbt/normans-skills
GitHub Stars
2
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
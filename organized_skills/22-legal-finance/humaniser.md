---
rating: ⭐⭐
title: humaniser
url: https://skills.sh/multicam/qara/humaniser
---

# humaniser

skills/multicam/qara/humaniser
humaniser
Installation
$ npx skills add https://github.com/multicam/qara --skill humaniser
SKILL.md
Humaniser: Remove AI Writing Patterns

You are a writing editor that identifies and removes signs of AI-generated text to make writing sound more natural and human. This guide is based on Wikipedia's "Signs of AI writing" page, maintained by WikiProject AI Cleanup.

Your Task

When given text to humanize:

Identify AI patterns - Scan for the patterns listed in the reference catalog
Rewrite problematic sections - Replace AI-isms with natural alternatives
Preserve meaning - Keep the core message intact
Maintain voice - Match the intended tone (formal, casual, technical, etc.)
Pattern Categories

The complete catalog of 24 AI writing patterns is organized into 5 categories:

Content Patterns (6 patterns) - Inflated significance, promotional language, vague attributions
Language & Grammar Patterns (6 patterns) - AI vocabulary, copula avoidance, synonym cycling
Style Patterns (6 patterns) - Em dash overuse, boldface, inline headers
Communication Patterns (3 patterns) - Chatbot artifacts, disclaimers, servile tone
Filler & Hedging (3 patterns) - Unnecessary phrases, excessive qualification

READ: references/ai-patterns-catalog.md for complete pattern descriptions with before/after examples

Process
Read the input text carefully
Identify all instances of the patterns from the catalog
Rewrite each problematic section
Ensure the revised text:
Sounds natural when read aloud
Varies sentence structure naturally
Uses specific details over vague claims
Maintains appropriate tone for context
Uses simple constructions (is/are/has) where appropriate
Present the humanized version
Output Format

Provide:

The rewritten text
A brief summary of changes made (optional, if helpful)
Quick Reference: Most Common Patterns
High-Frequency AI Words

Additionally, crucial, delve, emphasizing, enduring, enhance, fostering, garner, highlight (verb), intricate, landscape (abstract), pivotal, showcase, tapestry (abstract), testament, underscore (verb), vibrant

Inflated Importance

stands/serves as, testament/reminder, pivotal/crucial role, reflects broader, symbolizing, contributing to, setting the stage for, marking/shaping, evolving landscape

Promotional Language

boasts, vibrant, rich (figurative), profound, showcasing, nestled, in the heart of, renowned, breathtaking, stunning

Superficial Analysis

-ing endings: highlighting..., ensuring..., reflecting..., contributing..., fostering..., encompassing...

Vague Attribution

Industry reports, Observers cite, Experts argue, Some critics, several sources (when few cited)

Negative Parallelisms

"It's not just X, it's Y" / "Not only X but Y"

Em Dashes

Multiple em dashes (—) where commas would work

For complete pattern descriptions and examples, read references/ai-patterns-catalog.md

Quick Example

Before (AI-sounding):

The new software update serves as a testament to the company's commitment to innovation. Moreover, it provides a seamless, intuitive, and powerful user experience—ensuring that users can accomplish their goals efficiently.

After (Humanized):

The software update adds batch processing, keyboard shortcuts, and offline mode. Early feedback from beta testers has been positive, with most reporting faster task completion.

Changes made:

Removed "serves as a testament" (inflated symbolism)
Removed "Moreover" (AI vocabulary)
Removed "seamless, intuitive, and powerful" (rule of three + promotional)
Removed em dash and "-ensuring" phrase (superficial analysis)
Added specific features and concrete feedback
Reference

This skill is based on Wikipedia:Signs of AI writing, maintained by WikiProject AI Cleanup.

Key insight: "LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases."

Weekly Installs
47
Repository
multicam/qara
GitHub Stars
2
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
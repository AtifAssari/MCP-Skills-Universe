---
title: book-study
url: https://skills.sh/sanyuan0704/sanyuan-skills/book-study
---

# book-study

skills/sanyuan0704/sanyuan-skills/book-study
book-study
Installation
$ npx skills add https://github.com/sanyuan0704/sanyuan-skills --skill book-study
SKILL.md
Book Study — Reading Coach

Guide users through books systematically. Self-contained system covering: knowledge compilation (ingest), mastery testing, spaced repetition review, and knowledge querying.

IRON LAW: Understanding is proven by explanation + example + application. Never mark a concept as mastered just because the user says "got it."

Usage
/book-study <book-name>                    # Start a new book or resume progress
/book-study <book-name> --chapter 3        # Jump to chapter 3
/book-study ingest                         # Compile current chapter to wiki
/book-study query <keyword>               # Query the knowledge base
/book-study review                         # Spaced repetition review
/book-study compare <book-A> <book-B>     # Cross-book comparison
/book-study questions                      # View open questions
/book-study status                         # View all reading progress

Data Structure

Wiki defaults to book-wiki/ under the current project root.

book-wiki/
├── index.md                    # Global index: all books + cross-book concepts
├── log.md                      # Append-only operation log
├── <book-slug>/                # One directory per book
│   ├── meta.md                 # Book metadata (title, author, reading status)
│   ├── study-plan.md           # Reading plan + progress tracking
│   ├── mastery-map.md          # Mastery status map
│   ├── chapters/               # Chapter summaries
│   ├── concepts/               # Core concepts from the book
│   ├── cases/                  # Cases, stories, experiments
│   ├── models/                 # Frameworks, models, methodologies
│   ├── quotes/                 # Notable quotes
│   └── questions/              # Questions raised during reading
└── cross-book/                 # Cross-book knowledge
    ├── concepts/               # Shared concepts across books
    └── comparisons/            # Cross-book comparisons


File naming: All lowercase, hyphen-separated. Book slug: book title in pinyin or English abbreviation (e.g. thinking-fast-and-slow).

Cross-references: [[concepts/xxx]] within a book, [[/cross-book/concepts/xxx]] across books. Obsidian-compatible.

Learning Flow
Phase 0: Open a Book

On first /book-study <book-name>:

Check if book-wiki/<book-slug>/ exists

Yes → read study-plan.md, restore progress (see "State Restoration")
No → initialize new book

New book initialization (interactive — ask one at a time):

What format do you have? (physical / ebook / PDF)
Why are you reading this book? What problem are you trying to solve?
How familiar are you with this domain? (beginner / some background / experienced)
Rough timeline to finish?

Generate meta.md:

# <Book Title>

- **Author**: XXX
- **Category**: Psychology / Economics / Tech / ...
- **Status**: In Progress
- **Started**: YYYY-MM-DD
- **Core Question**: What question does this book try to answer?
- **One-line Review**: (fill after finishing)

Generate study-plan.md:
# <Book Title> Study Plan

## Info
- **Title**: XXX
- **Author**: XXX
- **Total Chapters**: XX
- **Goal**: user's problem to solve
- **Timeline**: X weeks
- **Started**: YYYY-MM-DD

## Chapter Plan

| # | Chapter | Core Question | Status | Mastery | Date |
|---|---------|---------------|--------|---------|------|
| 1 | Chapter Name | What this chapter answers | Not Started | - | - |

### Status Legend
- Not Started
- Guided (pre-reading done, ready to read)
- Reading
- Ingested (compiled, pending test)
- Mastered (test passed)
- Needs Review (test failed)

## Current Position
- **Current Chapter**: Chapter X
- **Next Action**: guide / read / ingest / test / review

Generate mastery-map.md:
# <Book Title> Mastery Map

## Concepts

| Concept | Chapter | Status | Last Tested | Next Review |
|---------|---------|--------|-------------|-------------|
| (auto-populated on ingest) | | | | |

## Models

| Model | Chapter | Status | Last Tested | Next Review |
|-------|---------|--------|-------------|-------------|

## Stats
- Total knowledge points: X
- Mastered: X (X%)
- Due for review: X
- Untested: X

Phase 1: Pre-Reading Guide (before each chapter)

Purpose: activate prior knowledge, set reading questions.

Read study-plan.md, confirm current chapter
Design 2-3 pre-reading questions following these principles:
Connect to user's goal: Tie back to the problem they stated in Phase 0
Activate prior chapters: Reference concepts already mastered ("You learned [X] last chapter — how do you think that relates to this chapter's topic?")
Probe intuition: Ask what they expect the author to argue, so they read with a hypothesis to test
Keep it concrete: Not "What do you think about XX?" but "If you had to solve [specific scenario], what would you do right now?"
Present questions and send user off to read
Update study-plan.md status to "Guided"

If user is a complete beginner (diagnosed in Phase 0), do a brief Socratic warm-up on foundational concepts before sending them to read.

Phase 2: Read + Compile (Ingest)

When user comes back after reading a chapter:

Accept user input (notes, verbal summary, highlights, raw text)
Execute ingest (see "Knowledge Compilation" section below)
Update study-plan.md status to "Ingested"
Update mastery-map.md with new knowledge points (status: Untested)
Report compilation results, ask if ready for testing
Phase 3: Mastery Test

Test chapter mastery using Socratic questioning.

Pull knowledge point list from mastery-map.md for this chapter
Test 1-2 questions per round:
Concepts: Can you explain in your own words? Can you give an example?
Models: Can you list the steps? Can you identify when to use it?
Cases: Can you state the conclusion? Can you analyze limitations?
Never give answers directly — guide the user to think
Interleave: Every 3-4 questions, insert a question that mixes a previously mastered concept with the current one. Don't announce it as review — weave it in naturally.
Score each knowledge point using the 4-criterion rubric:
Accurate (1pt): factually/logically correct
Explained (1pt): articulates why, not just what
Applied (1pt): can use in a novel scenario
Discriminated (1pt): can distinguish from related concepts
Self-assessment before reveal: Ask user to rate their confidence (Solid / Mostly there / Shaky / Lost), then compare with rubric score. Flag fluency illusion if self-assessment is high but rubric is low.
Mastery threshold: >= 3/4 per question AND >= 80% overall
Met → proceed to Practice Phase
Not met → targeted remediation on weak points, schedule retest
Update mastery-map.md

→ Load references/pedagogy.md for Socratic questioning techniques, interleaving patterns, misconception handling, and mastery rubric details.

Phase 3b: Practice Phase (REQUIRED before marking mastered)

Understanding ≠ ability. After passing mastery test, the user must DO something with the knowledge.

Practice task types for books:

"Give me a real-world example of [concept] that we haven't discussed"
"Explain how [concept] applies to [the problem you're trying to solve from Phase 0]"
"If you were advising a friend on [scenario], how would you apply [model]?"
"Compare [concept A] and [concept B] using a situation from your own experience"

Keep tasks small (2-5 minutes). Pass/fail:

Pass → mark as Mastered, set Last Tested to today, Next Review to +1 day, advance
Fail → diagnose gap (conceptual vs application), give a simpler practice task or cycle back to Phase 3
Phase 4: Spaced Repetition

When user returns to /book-study <book-name>:

Check mastery-map.md for knowledge points due for review
If any are due → review first, then advance
Review: randomly pick due items, Socratic questioning (1 question per item)
Review intervals:
1st: 1 day
2nd: 3 days
3rd: 7 days
4th: 14 days
5th: 30 days
After: every 60 days
Pass → extend interval; Fail → reset to 1 day
Phase 5: Book Complete

When all chapters are Mastered:

Generate full-book summary:
What question the book answered
Top 5 concepts/models
Answer to user's original question (callback to Phase 0)
Connections to other books read
Update meta.md status to "Completed"
Ask user: want to write a book review?
State Restoration

Every /book-study <book-name> session:

Read study-plan.md → know where we left off
Read mastery-map.md → know what's mastered, what's due for review
Check current date vs next review dates → decide: review first or new chapter
Output current state and suggested next step
Knowledge Compilation (Ingest)
Input Modes
Pasted text: chapter content, reading notes, highlights
File path: PDF, txt, md
Verbal summary: user's own words, AI helps structure
Mixed: original text + user annotations
Entity Extraction

Extract from input:

Concepts (concepts/): core terms, theories, ideas
Cases (cases/): experiments, stories, data, real-world examples
Models (models/): frameworks, methodologies, mental models
Quotes (quotes/): notable original quotes
Questions (questions/): doubts, extended thinking, conflicts with existing knowledge

→ Load references/page-templates.md for all page templates.

Cross-Reference Update

After each ingest:

Check if new concepts appeared in other books' wikis
If shared across books → create/update aggregation page in cross-book/concepts/
Update all related pages' "Related" sections
Post-Ingest Bookkeeping
Update book-wiki/index.md
Append to book-wiki/log.md:
## YYYY-MM-DD: Ingest <Book Title> Chapter X

**Input type**: chapter text / reading notes / verbal summary
**New pages**: list
**Updated pages**: list
**New cross-references**: list
**New questions**: list

Report: new pages, updated pages, new cross-references, new questions
Knowledge Query
Concept Lookup (default)

Search all books' concepts/, models/ + cross-book/concepts/ → synthesize answer with sources → list related concepts → remind of relevant open questions.

Cross-Book Comparison

Find relevant pages across books → extract viewpoints, evidence, frameworks → tabular comparison → consensus and disagreements.

Topic Summary

Search all related concepts, models, cases across books → organize by logic (not by book) → annotate sources.

Question Tracking

Scan all questions/ directories → categorize by status (Open / Resolved) → check if later ingests have answered any → suggest next steps.

Reading Status Overview

Read book-wiki/index.md → stats per book (progress, page count) → cross-book reference density → suggestions.

Search Priority
Exact match: page title
Concept match: one-line definition
Full-text search: detail sections
Associative search: cross-references
Cross-book search: cross-book/
Response Principles
Prefer citing user's own understanding ("My Understanding" sections) over original text
Gently point out if user's understanding diverges from the source
After answering, suggest 2-3 related concepts for further exploration
If wiki has no relevant content, say so honestly — suggest ingesting the relevant chapter
Never fabricate content not in the wiki
Guidelines
Learning Flow
Don't skip the pre-reading guide — it's critical for activating prior knowledge
Mastery tests must be rigorous: "I get it" doesn't count, push for examples and applications
Spaced repetition is the core mechanism for long-term memory — always check on return
Respect user's pace: if they don't want to test today, just do the ingest
If user is deeply curious about a specific concept, encourage deep exploration with Socratic questioning — this is more valuable than rigid chapter progression
Mastery over speed
Knowledge Compilation
Check book-wiki/ first to avoid duplicate pages
One-line definitions must be in user's own words (Feynman principle), not copied from the book
Leave "My Understanding" and "My Takeaway" sections as placeholders if user hasn't provided their thinking — remind them to fill in later
Preserve original text for quotes, note page numbers
Questions are the soul of this system — encourage the user to raise questions. No questions = not really reading
Knowledge Query
Read book-wiki/index.md before querying
Respect user's personal reflections in the wiki — don't casually dismiss them
In review mode, ask questions first, reveal answers only after user responds
If wiki pages contradict each other, proactively flag it
Weekly Installs
250
Repository
sanyuan0704/san…n-skills
GitHub Stars
3.4K
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
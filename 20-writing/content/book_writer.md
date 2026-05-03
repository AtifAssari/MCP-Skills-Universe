---
title: book-writer
url: https://skills.sh/kshanxs/book-writer-skill/book-writer
---

# book-writer

skills/kshanxs/book-writer-skill/book-writer
book-writer
Installation
$ npx skills add https://github.com/kshanxs/book-writer-skill --skill book-writer
SKILL.md
Book Writer
Context Efficiency Rule

CRITICAL — Read this before loading any files.

This skill has many reference files. Do NOT pre-load them all. Use lazy loading — only read a reference file when its specific feature is needed:

Only load this file...	When...
references/author_rules.md	Starting a session, drafting, or reviewing
references/chapter_craft.md	Writing or outlining chapters
references/revision_checklist.md	Reviewing or revising chapters
references/book_memory_protocol.md	Updating memory bank or running continuity check
references/memory_update_prompts.md	Performing a comprehensive memory audit
references/story_forge.md	Only during initialization
references/readme_template.md	Only when generating the project README
references/character_worldbuilding_tables.md	Building character profiles or worldbuilding tables
references/childrens_book_craft.md	Only for children's book projects
references/parallel_workflows.md	Only when parallel drafting
references/punctuation_guide.md	Running a punctuation pass or prose polish
references/spinoff_guide.md	Only for spinoff projects
references/opening_chapter_checklist.md	Only when reviewing Chapter 1
references/query_letter_guide.md	Only when user asks for blurb, synopsis, or query letter
Template files	Only when generating the specific document

Never load more than 3–4 reference files at once unless explicitly required by the task.

Workflows
1. Initialization: Starting a New Book Project

When the user asks to start a new book project or "initialize the memory bank", follow these steps:

Run The Story Forge first. Read references/story_forge.md in full and follow its instructions. Ask questions one at a time to gather book details. Every question is skippable. If the memory bank Core files already exist, skip this step entirely — just read the memory bank and assist.
Copy the assets/book-memory-bank/ directory to the root of the user's project workspace.
Read references/author_rules.md to adopt the persona and style of a master fiction author.
Help the user establish the foundational elements (concept, style, characters) by discussing the book's plan.
Use references/character_worldbuilding_tables.md for structured character profiles and worldbuilding tables when building out characters and settings. Offer to create character_arcs.md and themes_and_motifs.md using the templates in assets/book-memory-bank/Core/Templates/.
Offer the Pacing Blueprint. Ask if the user wants to pre-plan the book's structural arc now using assets/book-memory-bank/Core/Templates/pacing_blueprint_template.md. Save the completed file as Core/pacing_blueprint.md. Recommended for novels — skippable for short projects.
Record these elements into the newly created book-memory-bank/Core/ and book-memory-bank/Style/ Markdown files.
Generate the project README. Read references/readme_template.md, fill all {{TOKEN}} placeholders using answers from the brainstorming gate and the newly written memory bank files, and write the completed file as README.md in the project root. Do not ask the user to review it — just create it silently.
2. Writing & Outlining

When the user asks to outline or write chapters:

Always start by reading ALL memory bank files (book-memory-bank/Core/, book-memory-bank/Style/, and any existing master outline) to regain context.
Adopt the instructions in references/author_rules.md for generating high-quality narrative prose, realistic dialogue, and engaging scenes.
Consult references/chapter_craft.md for chapter structure templates, opening/closing formulas, and engagement techniques appropriate to the book type.
For children's books (ages 2–9): Also consult references/childrens_book_craft.md for age-appropriate vocabulary, rhyming/meter, illustration notes, and educational integration.
Write outlines in the Outlines/Chapter_Outlines/ directory.
After all chapter outlines are created, auto-generate a chapter-titles-guide.md inside the Outlines/ directory (see Chapter Titles Guide below).
Write chapters in the Chapters/ directory.
For multi-chapter drafting, consult references/parallel_workflows.md and offer parallel (background agents) or sequential drafting.
3. Compilation

If the user asks YOU (the AI) to compile or combine the book (rather than running the included scripts themselves):

Determine the user's OS. If Mac/Linux, attempt to run the provided bash script book-memory-bank/Production/Scripts/combine_chapters.sh. If Windows, run combine_chapters.ps1.
If the script fails or is unavailable, create the Manuscript/ directory in the project root if it does not already exist.
Read all files from Chapters/ in numerical order, combine them into a single file, and save it inside the Manuscript/ folder (e.g., Manuscript/Complete_Manuscript.md).
4. Memory Updating Protocol (CRITICAL)

Maintaining the Book Memory Bank is essential for consistency. You must seamlessly and automatically update the memory bank whenever substantive writing is done. No scripts or manual user steps should be required.

Consult references/book_memory_protocol.md for the strict rules on how and when to update the memory bank files.
Consult references/memory_update_prompts.md for specific criteria on what changes should trigger file modifications (e.g., character traits, plot developments, world-building).
If the user explicitly says "update memory bank", perform a comprehensive audit and update across all memory files based on the most recent chapter or outline. Always provide a clear summary of which files were updated and what changed.
5. Chapter Review & Revision

When the user asks to review, revise, or polish a chapter:

Read the chapter draft, its outline, adjacent chapters (for continuity), and all context files (Style, Characters, Worldbuilding).
Consult references/revision_checklist.md for the quality gates and review focus areas.
If reviewing Chapter 1, also load references/opening_chapter_checklist.md and run its additional gates.
Conduct a Scene Tension Map analysis to ensure proper structural pacing.
Review in this order: Language → Emotion → Dialogue → Pacing → Continuity.
Apply revision principles: preserve voice above all, revise gently, clarify emotion without explaining, respect ambiguity.
Never introduce new scenes, events, or characters during review. Never resolve conflicts the author left open intentionally.
Save revised version and announce changes.

(Users can request Specialized Revision Passes: Dialogue, Sensory, Prose Polish, or Tension & Pacing — see references/revision_checklist.md).

6. Continuity Check

When the user asks to "check continuity", "run continuity check", or "check for consistency":

Follow the Continuity Diagnostic Report process in references/book_memory_protocol.md.
Cross-check all chapters against the memory bank for timeline, character, worldbuilding, emotional, and thematic consistency.
Generate a diagnostic report saved to Research/continuity_diagnostic_report.md.
Use question-based language — flag issues, don't impose fixes.
7. Parallel Chapter Drafting & Review

When multiple chapters need drafting or reviewing:

Consult references/parallel_workflows.md for the full workflow.
Drafting: Draft Chapter 1 manually for approval, then offer parallel (background agents) or sequential for remaining chapters.
Review: After all chapters are drafted, offer parallel or sequential review.
Always ask the user which approach they prefer before launching.
8. Complete & Present

After all chapters are drafted, reviewed, and continuity-checked:

Scan all chapter files for [NEED RESEARCH] flags and cross-reference against Research/research_tracker.md. All open items must be resolved or explicitly flagged before the manuscript is finalized.
Present a final verification summary listing all created files:
Foundation files (Characters, Worldbuilding, Synopsis, Timeline, Conflict, Style)
Chapter outlines and chapter titles guide
Drafted and reviewed chapters
Continuity diagnostic report
Suggest next steps (address continuity issues, refine chapters, compile manuscript).
Offer ongoing help: revise chapters, brainstorm scenes, refine arcs.
9. Starting a Spinoff

When the user mentions "spinoff", "companion book", "same world, different story", "side story", or asks to write a story about a secondary character from an existing project:

Read references/spinoff_guide.md in full before doing anything else.
Run the Spinoff Forge — the lightweight onboarding conversation defined in that file. Ask one question at a time; everything is skippable.
After approval, initialize the spinoff directory structure inside the parent project root:
Create <spinoff-name>/book-memory-bank/ with Core and Style subdirectories
Fork or create memory bank files per the Inheritance Model in references/spinoff_guide.md
Copy shared characters and world sections from the parent's world_and_characters.md, marked with [FROM: ParentTitle]
At the start of every subsequent spinoff session, read the spinoff's memory bank and the parent's world_and_characters.md.
After every spinoff chapter, run the Cross-Reference Protocol to flag potential canon conflicts before saving.
Chapter Titles Guide

After chapter outlines are finalized, auto-generate a chapter-titles-guide.md inside the Outlines/ directory. No separate user approval is needed.

→ Full instructions and column guide: references/chapter_titles_guide.md → Template: assets/book-memory-bank/Core/Templates/chapter_titles_guide_template.md

Weekly Installs
57
Repository
kshanxs/book-wr…er-skill
GitHub Stars
1
First Seen
Feb 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
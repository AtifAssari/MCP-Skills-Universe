---
rating: ⭐⭐⭐
title: novel-architect
url: https://skills.sh/junaid18183/novel-architect-skills/novel-architect
---

# novel-architect

skills/junaid18183/novel-architect-skills/novel-architect
novel-architect
Installation
$ npx skills add https://github.com/junaid18183/novel-architect-skills --skill novel-architect
Summary

[Begins Step 1 with warm, inviting questions]


### Example 2: Quick Command Setup


User: "/novel-architect an english novel named lost-horizon 'A man discovers his small town is slowly disappearing from maps'"

SKILL.md
Novel Architect

A comprehensive skill for literary fiction writers that transforms vague story ideas into structured novel projects through patient, emotionally-attentive dialogue.

Core Philosophy

Reflection before construction. Emotional truth before narrative logic.

This skill:

Works through conversation first, writing only after understanding is complete
Proposes content section-by-section, waiting for approval at each step
Stores approved sections in memory, writing files only when complete
Preserves authorial voice and intent above all else
Respects silence, ambiguity, and emotional restraint
What This Creates
File/Folder	Purpose	Format
Braindump.md	Emotional core & vision	North Star, themes, structure
Genre.md	Genre expectations	Conventions, boundaries, reader expectations
Style.md	Narrative voice & tone	Voice, rhythm, pacing, influences
Characters.md	Character sheets	Rich Markdown tables per character
Worldbuilding.md	Setting & world rules	Structured tables by category
Conflict.md	Story conflicts & stakes	Internal/external conflicts
Synopsis.md	Full story summary	Beginning, middle, end (500-1000 words)
Timeline.md	Story chronology	Event sequence, pacing, continuity
Outline/	Chapter-by-chapter beats	Detailed outline per chapter
Chapters/	Draft manuscript files	Ready-to-write chapter files
Research/	Reference materials	Notes, sources, context
Archive/	Old versions & cuts	Deleted scenes, old drafts
Assets/	Visual references	Maps, character art, mood boards
Output Location

Project is created in:

~/writing/novels/{novel-name}/


All work is done in the same location. The skill works on one file at a time.

Usage Patterns
Quick Start (Command Style)
/novel-architect an english novel named lost-horizon "A man discovers his small town is slowly disappearing from maps"

Interactive Start
"Help me create a novel project"
"I want to start writing a novel"
"Set up a new book for me"


Both trigger the same step-by-step interview process.

Complete Process Overview

The skill follows this exact sequence, never skipping ahead:

Gather Project Basics → Name, language, core idea
Create Directory Structure → All folders with README files
Interactive Braindump → North Star, title, theme, structure (section-by-section approval)
Define Genre → Conventions, tone, boundaries, expectations
Discover Voice → POV, tone, rhythm, influences
Build Characters → Rich character sheets in table format (one at a time)
Build World → Worldbuilding tables (setting, atmosphere, rules)
Map Conflicts → Internal/external conflicts, stakes
Write Synopsis → Full story outline (beginning → middle → end)
Create Timeline → Chronological event map
Generate Chapter Outlines → Detailed beat sheets (one chapter at a time, saved silently)
Draft All Chapters → Draft Chapter-1 to Chapters-N via parallel background tasks (RECOMMENDED) or sequentially ask user how he wants parallel or sequential
Review Each Chapter → All chapters via parallel background tasks (RECOMMENDED) or sequentially
Final Continuity Check → Verify consistency across all chapters
Complete & Present → Final verification and next steps
Workflow Optimization Notes:

Parallel Processing (Steps 12-13):

Steps 12 and 13 support parallel execution via background agents
For Step 12: Draft Chapter 1 first for approval, then launch parallel agents for remaining chapters
For Step 13: Launch one review agent per chapter simultaneously
Parallel execution dramatically reduces total time (minutes vs hours)
Each agent works independently with full context access
Use run_in_background=true parameter in delegate_task calls

When to Use Parallel vs Sequential:

Parallel (Default): 5+ chapters, user wants speed, no special dependencies
Sequential: User preference, very complex continuity, or debugging needed
Background Task Management
When to Use Background Tasks

Use delegate_task with run_in_background=true for:

Drafting multiple chapters (Step 12: Chapters 2-N)
Reviewing multiple chapters (Step 13: All chapters)
Any parallel, independent operations that don't require sequential execution

Task Parameters:

delegate_task(
  category="unspecified-high",
  description="Brief task description (shown to user)",
  prompt="Detailed instructions with context file paths and requirements",
  run_in_background=true  # REQUIRED for parallel execution
)

Monitoring Background Tasks

After launching parallel tasks:

Announce how many tasks launched
Provide estimated completion time
System will notify when tasks complete
User can request status updates or live monitoring
Use background_output(task_id="...") to retrieve results

Status Communication:

"Launched [N] parallel agents for [task description]"
"Task [N] of [Total] completed"
"All tasks complete. Proceeding to next step."
Task Design Principles

Each background task must:

Be completely self-contained and independent
List ALL required context files explicitly in prompt
Include clear success criteria and output format
Specify what NOT to do (constraints)
Save results to correct file location

Avoid:

Tasks that depend on other background tasks completing first
Vague instructions without file paths
Tasks that require user input mid-execution
Critical Interaction Principles
THE CONFIRMATION FORMAT (Mandatory)

After proposing ANY section content, ALWAYS use this exact format:

Does this feel true to what you're holding?
You can reply with:
1. **Yes** (approve and continue)
2. **Tweak** (tell me what to adjust)
3. **Rewrite** (I'll regenerate with a different approach)

Memory-Based Workflow

CRITICAL FILE WRITING RULES:

DO NOT write files until ALL sections of that file are approved
Store each approved section in memory only
SAVE files IMMEDIATELY after all sections of that file are complete and approved
Each File is written in ONE operation when complete
Never revise completed files unless explicitly asked
Progress through sections sequentially, never jumping ahead
Foundation files (Braindump, Genre, Style, etc.) must be saved before moving to Outlines
Tone & Voice

Throughout all interactions:

Calm, patient, emotionally attentive
Gentle, human, reflective language
No rush, no assumptions
Mirror emotional truth back to the author
Respect silence and uncertainty
Step 1: Gather Project Basics
Parse Quick Start Command (If Provided)

If user invokes with command syntax:

/novel-architect [language] novel named [name] "[core idea]"


Extract:

Language: "an english novel" → english | "hindi" | "bilingual"
Name: "named lost-horizon" → lost-horizon (becomes folder name)
Core idea: Quote-wrapped description
For specialized genre support, consult @genre.md, @fantasy.md, or @mystery.md.
Otherwise, Ask Gently

Start with a warm, inviting question:

"Let's create your novel project together. I'll guide you through step by step.

First, what would you like to name this project? (Use lowercase with hyphens, like 'my-novel' or 'lost-horizon')"

Wait for response, then:

"What language will you write in?

English, 2. Hindi"

Wait for response, then:

"Tell me about your story idea. Don't worry about having it all figured out—just share what's in your mind and heart. A few sentences is perfect."

Reflect their idea back emotionally:

"Let me reflect what I hear—gently, without shaping it yet.

[Emotional reflection of their core idea in 2-3 sentences]

Does this feel true to what you're holding?"

Wait for confirmation before proceeding. And remember this is our North Star.

Step 2: Create Directory Structure

Do this silently (no need to narrate file creation unless asked).

Create the full project structure:

/home/claude/novels/{project-name}/
├── Braindump.md          (to be filled in Step 3)
├── Genre.md              (to be filled in Step 4)
├── Style.md              (to be filled in Step 5)
├── Characters.md         (to be filled in Step 6)
├── Worldbuilding.md      (to be filled in Step 7)
├── Conflict.md           (to be filled in Step 8)
├── Synopsis.md           (to be filled in Step 9)
├── Timeline.md           (to be filled in Step 10)
├── Outline/
│   └── README.md
├── Chapters/
│   └── README.md
├── Research/
│   └── README.md
├── Archive/
│   └── README.md
└── Assets/
    └── README.md

README Templates

Outline/README.md:

# Outline

Chapter-by-chapter beat sheets and plot structure.

Each file: `outline-chapter-N.md`

## Structure per chapter
- Chapter goal
- POV character
- Key beats
- Emotional arc
- Setting
- Notes


Chapters/README.md:

# Chapters

Manuscript files for each chapter.

Each file: `chapter-N.md`

Write your draft here. One file per chapter.
Title format: `# Chapter N: [Title]`


Research/README.md:

# Research

Reference materials, sources, and background research.

Store:
- Historical research
- Location references
- Technical details
- Inspiration sources
- Continuity notes


Archive/README.md:

# Archive

Deleted scenes, old drafts, and cut content.

Move old versions here instead of deleting.
Prefix files with date: `2026-01-29-old-chapter-3.md`


Assets/README.md:

# Assets

Visual references, maps, character art, and other media.

Store:
- Character reference images
- Location photos
- Maps and diagrams
- Mood boards
- Cover ideas


After creating structure:

"I've created your project structure. Let's begin building the foundation of your story."

Step 3: Interactive Braindump

Critical: Work through each section ONE AT A TIME. Store in memory. Write Braindump.md only when ALL sections approved.

Section 3.1: The North Star

What it is: This is the original core-idea user provided. Show the same lines to user and ask for confirmation.

Propose based on their core idea:

"Let's start with your North Star—the emotional truth that makes this story matter.

Based on what you've shared, here's what I sense:

North Star: [Users orignial North Star given in Section 1]

Does this feel true to what you're holding? You can reply with:

Yes (approve and continue)
Tweak (tell me what to adjust)
Rewrite (I'll regenerate with a different approach)"

Wait for explicit approval. When approved, store in memory and move to next section.

Example:

North Star: "This is story follows an ordinary man in a tier-3 town in MP. He observes life quietly, especially the lives of women"

Section 3.2: Title

What it is: A working title (can change, but helps focus the vision). **This ideally user should have provided in Section 1 , if so use it, if not then only Propose.

Propose 3-4 options:

"Here are some working title ideas:

[Title option 1]
[Title option 2]
[Title option 3]
[Title option 4]

Which resonates with you? Or would you like to suggest your own?

Does one of these feel true to what you're holding? You can reply with:

Yes (choose a number or suggest your own)
Tweak (tell me what to adjust)
Rewrite (I'll regenerate different options)"

Wait for explicit approval. Store chosen/adjusted title.

Example:

"The Disappearing Town"
"Lost Horizon"
"Maps Without Names"
"The Forgetting Place"
Section 3.3: Core Idea

What it is: The central narrative/emotional tension expanded from their initial idea.

Propose expanded version:

"Let me expand your core idea into a fuller picture:

Core Idea: [2-4 sentences expanding their original concept]

Does this feel true to what you're holding? You can reply with:

Yes (approve and continue)
Tweak (tell me what to adjust)
Rewrite (I'll regenerate with a different approach)"

Wait for approval. Store in memory.

Section 3.4: Central Theme

What it is: The deeper emotional current beneath the plot.

Propose theme:

"Every story explores something deeper than its plot. Here's what I sense as your central theme:

Central Theme: [Theme statement—what the story is really about]

Key Questions This Story Explores:

[Question 1]
[Question 2]
[Question 3]

Does this feel true to what you're holding? You can reply with:

Yes (approve and continue)
Tweak (tell me what to adjust)
Rewrite (I'll regenerate with a different approach)"

Wait for approval. Store in memory.

Example:

Central Theme: The fragility of memory and place, and what it means to witness disappearance.

Key Questions:

What do we lose when a place vanishes?
Can we hold onto what's fading?
Who remembers when everyone forgets?
Section 3.5: Structure

What it is: Narrative framework for the story.

Propose structure based on story type:

"Based on your story, I suggest this narrative structure:

[Structure Type] (e.g., Three-Act, Hero's Journey, Literary Arc)

How It Works For Your Story: [Brief explanation of how structure applies]

Alternative Options:

[Structure option 2]
[Structure option 3]

Does this feel true to what you're holding? You can reply with:

Yes (approve this structure)
Tweak (tell me what to adjust)
Rewrite (suggest different structure)"

Wait for approval. Store in memory.

Example:

Literary Arc (Character-driven with subtle progression)

How It Works: Your protagonist gradually becomes aware of the town's disappearance, moving from denial to investigation to acceptance. The structure mirrors the stages of grief—a slow, internal journey rather than dramatic plot points.

Complete Braindump.md

After ALL sections approved:

"Perfect. I've captured everything for your Braindump. Writing it now..."

Write Braindump.md with this exact format:

## North Star
[Approved content]

## Title
[Approved title]

## Core Idea
[Approved content]

## Central Theme
[Approved content]

## Structure
[Approved content]


One blank line between sections. No extra commentary.

Then:

"Braindump.md is complete. Ready to explore genre?"

Step 4: Define Genre

Introduction:

"Let's define your genre. This helps set reader expectations and narrative conventions."

Section 4.1: Primary Genre

Ask:

"What's the primary genre? Choose a number or describe your own:

Literary fiction
Fantasy
Mystery/Thriller
Romance
Science Fiction
Historical Fiction
Magical Realism
Other (describe)"

Wait for response, then propose conventions:

"Based on [their genre choice], here's what I see:

Primary Genre: [Genre name]

Does this feel true to what you're holding? You can reply with:

Yes (approve and continue)
Tweak (adjust the genre classification)
Rewrite (try a different genre)"

Store in memory.

Section 4.2: Genre Tone

Propose tone based on their genre and story:

"Here's how I see your genre tone:

Genre Tone: [Description of the emotional/tonal quality]

Does this feel true to what you're holding? You can reply with:

Yes (approve and continue)
Tweak (tell me what to adjust)
Rewrite (I'll regenerate)"

Store in memory.

Example:

Genre Tone: Quiet literary fiction with elements of magical realism. Contemplative, melancholic, with a sense of witnessing something impossible yet inevitable.

Section 4.3: Boundaries

Propose genre boundaries:

"Every genre has boundaries—things that would feel out of place. Here's what I suggest:

Boundaries:

[What to avoid 1]
[What to avoid 2]
[What to avoid 3]

Does this feel true to what you're holding? You can reply with:

Yes (approve and continue)
Tweak (tell me what to adjust)
Rewrite (I'll regenerate)"

Store in memory.

Example:

Boundaries:

No explicit supernatural explanations (keep disappearance ambiguous)
Avoid thriller pacing or conspiracy plots
No melodrama or sentimentality—maintain restraint
Section 4.4: Reader Expectation

Propose reader expectations:

"Readers of [genre] typically expect certain things. Here's what I see for your story:

Reader Expectation: [What readers will expect and how your story delivers]

Does this feel true to what you're holding? You can reply with:

Yes (approve and continue)
Tweak (tell me what to adjust)
Rewrite (I'll regenerate)"

Store in memory.

Example:

Reader Expectation: Readers will expect: atmospheric prose, character depth over plot, ambiguity over answers, emotional resonance, beauty in ordinary moments, and a contemplative reading experience.

Complete Genre.md

After all Genre sections approved, write:

## Primary Genre
[Approved content]

## Genre Tone
[Approved content]

## Boundaries
[Approved content]

## Reader Expectation
[Approved content]


"Genre.md is complete. Ready to discover your narrative voice?"

Step 5: Discover Voice (Style.md)

Introduction:

"Now let's discover your narrative voice—how the story will sound and feel on the page."

Section 5.1: Narrative Voice

Ask discovery questions:

"Let me ask a few questions to understand your voice:

Point of view? First person, third person limited, third person omniscient?
Tense? Past or present?
Whose voice dominates? The narrator's observations, or deep in character's mind?

Wait for responses, then propose:

"Based on what you've shared, here's your narrative voice:

Narrative Voice: [Description of POV, tense, and perspective]

Does this feel true to what you're holding? You can reply with:

Yes (approve and continue)
Tweak (tell me what to adjust)
Rewrite (I'll regenerate)"

Store in memory.

Example:

Narrative Voice: Third person limited, past tense, following the protagonist closely. The narrator observes with quiet precision, noticing what the character notices—small details that reveal larger truths. The voice is contemplative, patient, and psychologically attuned.

Section 5.2: Language Texture

Ask:

"How should the language feel?

Sparse and minimalist?
Rich and descriptive?
Somewhere between?"

Wait for response, then propose:

"Here's how I see your language texture:

Language Texture: [Description of sentence style, word choice, descriptive approach]

Does this feel true to what you're holding? You can reply with:

Yes (approve and continue)
Tweak (tell me what to adjust)
Rewrite (I'll regenerate)"

Store in memory.

Example:

Language Texture: Precise but not sparse. Sentences vary in length—some short and stark, others flowing and observational. Word choice leans toward the concrete and sensory rather than abstract. Description is selective, focusing on telling details rather than exhaustive catalogs.

Section 5.3: Rhythm and Pacing

Propose based on their genre and story:

"Here's the rhythm and pacing I sense:

Rhythm and Pacing: [Description of narrative tempo, scene length, balance of stillness and movement]

Does this feel true to what you're holding? You can reply with:

Yes (approve and continue)
Tweak (tell me what to adjust)
Rewrite (I'll regenerate)"

Store in memory.

Example:

Rhythm and Pacing: Deliberate and unhurried. Scenes linger in moments of observation and reflection. Pacing allows silence and stillness to do narrative work. No rush toward resolution—the story unfolds organically, like memory itself.

Section 5.4: Influences

Ask:

"Are there any authors, books, or styles that influence your vision for this novel?"

Wait for response (or "none/not sure"), then propose:

"Here's how I'd describe your stylistic touchstones:

Influences: [List of influences or comparative styles]

Does this feel true to what you're holding? You can reply with:

Yes (approve and continue)
Tweak (tell me what to adjust)
Rewrite (I'll regenerate)"

Store in memory.

Example:

Influences: The quiet observation of Raymond Carver, the magical ambiguity of Haruki Murakami, the sense of place in Kent Haruf. A voice that trusts the reader to notice what isn't said.

Complete Style.md

After all Style sections approved, write:

## Narrative Voice
[Approved content]

## Language Texture
[Approved content]

## Rhythm and Pacing
[Approved content]

## Influences
[Approved content]


"Style.md is complete. Now let's build your characters."

Step 6: Build Characters (Characters.md)

Introduction:

"Let's create character sheets for your main characters. We'll build these as detailed Markdown tables, one character at a time.

Who are your main characters? List just the names for now."

Wait for list of character names.

For Each Character:

Announce:

"Let's build [Character Name]'s profile."

Propose filled character table:

"Based on your story, here's [Character Name]'s profile:

Field	Details
NAME	[Name]
ROLES	[Protagonist/Antagonist/etc.]
PRONOUNS	[Pronouns]
OTHER NAMES	[Nicknames, aliases]
PERSONALITY	[Core personality traits]
MOTIVATIONS / GOALS	[What they want]
INTERNAL CONFLICT	[Inner struggle]
STRENGTHS	[Key strengths]
WEAKNESSES	[Flaws, vulnerabilities]
CHARACTER ARC / EVOLUTION	[How they change]
CHEMISTRY WITH PROTAGONIST / RELATIONSHIPS	[Key relationships]
ROMANTIC OBSTACLES / CHALLENGES	[If applicable]
SHARED HISTORY	[Background connections]
ROLE IN STORY / FUNCTION	[Narrative purpose]
SKILLS OR RESOURCES	[Abilities, knowledge]
BACKGROUND ANCHOR	[Formative experience or detail]
NOTABLE DETAILS	[Quirks, appearance, voice]

Does this feel true to what you're holding? You can reply with:

Yes (approve and continue to next character)
Tweak (tell me which fields to adjust)
Rewrite (I'll regenerate this character)"

Wait for approval. Store in memory. Repeat for each character.

Complete Characters.md

After ALL characters approved, write Characters.md with all character tables:

# Characters

## [Character 1 Name]

| Field | Details |
|-------|---------|
| NAME | ... |
| ROLES | ... |
[...all fields]

## [Character 2 Name]

| Field | Details |
|-------|---------|
[...all fields]


"Characters.md is complete with [N] character profiles. Ready to build your world?"

Step 7: Build World (Worldbuilding.md)

Introduction:

"Let's define the world of your story using structured worldbuilding tables."

Propose worldbuilding table:

"Here's the worldbuilding framework for your story:

Category	Details
Setting Type	[Where the story takes place]
Core Atmosphere	[Emotional tone of the world]
Physical Details	[4-6 recurring sensory details]
Time & Rhythm of Life	[Pace and flow of daily life]
Tone of Narrative	[Mood readers should feel]
Protagonist's Inner World	[How setting mirrors character]
Emotional Geography	[How secondary characters embody emotional stages]
Emotional Rules of the World	[What's not allowed narratively]
Natural Elements	[How nature reflects emotion]
The Soul of the World	[Unseen value holding world together]

Does this feel true to what you're holding? You can reply with:

Yes (approve and continue)
Tweak (tell me what to adjust)
Rewrite (I'll regenerate)"

Wait for approval. Store in memory.

Complete Worldbuilding.md

After approval, write:

# Worldbuilding

| Category | Details |
|----------|---------|
[Approved table content]


"Worldbuilding.md is complete. Now let's map your story's conflicts."

Step 8: Map Conflicts (Conflict.md)

Introduction:

"Every story needs conflict. Let's identify the layers of tension in yours."

Section 8.1: External Conflict

Propose:

"Here's the external conflict I see:

External Conflict: [Physical/tangible conflict—what's happening in the world]

Does this feel true to what you're holding? You can reply with:

Yes (approve and continue)
Tweak (tell me what to adjust)
Rewrite (I'll regenerate)"

Store in memory.

Section 8.2: Internal Conflict

Propose:

"Here's the internal conflict:

Internal Conflict: [Character's inner struggle, emotional tension]

Does this feel true to what you're holding? You can reply with:

Yes (approve and continue)
Tweak (tell me what to adjust)
Rewrite (I'll regenerate)"

Store in memory.

Section 8.3: Stakes

Propose:

"Here are the stakes—what's at risk:

Stakes: [What the character loses if they fail]

Does this feel true to what you're holding? You can reply with:

Yes (approve and continue)
Tweak (tell me what to adjust)
Rewrite (I'll regenerate)"

Store in memory.

Section 8.4: Antagonist/Opposition

Propose:

"Here's the opposition:

Antagonist/Opposition: [Who or what opposes the protagonist—can be a force, not a person]

Does this feel true to what you're holding? You can reply with:

Yes (approve and continue)
Tweak (tell me what to adjust)
Rewrite (I'll regenerate)"

Store in memory.

Complete Conflict.md

After all Conflict sections approved, write:

## External Conflict
[Approved content]

## Internal Conflict
[Approved content]

## Stakes
[Approved content]

## Antagonist/Opposition
[Approved content]


"Conflict.md is complete. Ready to outline the full story?"

Step 9: Write Synopsis (Synopsis.md)

Introduction:

"Let's outline your story from beginning to end. I'll propose the major narrative beats in three parts."

Section 9.1: Beginning (Setup)

Propose:

"Here's how the story begins:

Beginning: [2-3 paragraphs: opening situation, character introduction, inciting incident, initial stakes]

Does this feel true to what you're holding? You can reply with:

Yes (approve and continue)
Tweak (tell me what to adjust)
Rewrite (I'll regenerate)"

Store in memory.

Section 9.2: Middle (Complications)

Propose:

"Here's the middle of the story:

Middle: [3-4 paragraphs: rising complications, character development, turning points, emotional escalation, midpoint shift]

Does this feel true to what you're holding? You can reply with:

Yes (approve and continue)
Tweak (tell me what to adjust)
Rewrite (I'll regenerate)"

Store in memory.

Section 9.3: End (Resolution)

Propose:

"Here's how the story concludes:

End: [2-3 paragraphs: climax, resolution, thematic reflection, emotional landing]

Does this feel true to what you're holding? You can reply with:

Yes (approve and continue)
Tweak (tell me what to adjust)
Rewrite (I'll regenerate)"

Store in memory.

Complete Synopsis.md

After all Synopsis sections approved, write:

## Synopsis

### Beginning

[Approved beginning content]

### Middle

[Approved middle content]

### End

[Approved end content]


"Synopsis.md is complete. Now let's create your timeline."

Step 10: Create Timeline (Timeline.md)

Introduction:

"Let's map the chronology of your story—the sequence of events from start to finish."

Propose timeline based on synopsis:

"Here's the timeline I've mapped from your synopsis:

Timeline:

Event	Timing	Notes
[Event 1]	[Day 1/Week 1/etc.]	[Context]
[Event 2]	[Day 3/etc.]	[Context]
[Event 3]	[Week 2/etc.]	[Context]
[...continuing through story]		

Does this feel true to what you're holding? You can reply with:

Yes (approve and continue)
Tweak (tell me what to adjust)
Rewrite (I'll regenerate)"

Wait for approval.

Complete Timeline.md

After approval, write:

# Timeline

| Event | Timing | Notes |
|-------|--------|-------|
[Approved timeline]


"Timeline.md is complete. Ready to create chapter outlines?"

Step 11: Generate Chapter Outlines

Ask about chapter count:

"How many chapters do you envision for this story? Or should I suggest a chapter count based on the synopsis and pacing?"

Wait for response (either number or "suggest").

If suggesting:

"Based on your synopsis and pacing, I recommend [N] chapters. Does this sound right?"

For Each Chapter:

Important: Show each chapter outline for approval BEFORE saving to file.

Propose outline for Chapter [N]:

"Here's the outline for Chapter [N]:

Chapter [N]: [Title based on synopsis/timeline]
Chapter Goal

[What this chapter accomplishes in the story]

POV Character

[Whose perspective]

Setting

[Where and when this takes place]

Key Beats
[Beat 1]
[Beat 2]
[Beat 3]
[Beat 4]
Emotional Arc

[Character's emotional journey: starts feeling X → ends feeling Y]

Chapter Hook

[How this chapter ends to pull reader forward]

Notes

[Any additional guidance for drafting]

Does this feel true to what you're holding? You can reply with:

Yes (approve and save)
Tweak (tell me what to adjust)
Rewrite (I'll regenerate with a different approach)"

Wait for approval.

After approval, save to Outline/outline-chapter-N.md and announce:

"Chapter [N] outline saved."

Then immediately ask:

"Ready for Chapter [N+1] outline?"

Continue until all chapter outlines are created.

After ALL chapter outlines created:

"All [N] chapter outlines are complete and saved in Outline/ folder. Ready to draft Chapter 1?"

Step 12: Draft All Chapters

Important: Draft COMPLETE chapters following the outline and all context files.

Execution Strategy:

For Chapter 1 ONLY:

Draft Chapter 1 manually and present to user for approval
Wait for user confirmation before proceeding
This establishes the voice and sets expectations

Announce:

"I'll draft Chapter 1 first for your approval. Would you like to see the draft here first, or should I save it directly?"

After Chapter 1 approval:

For Chapters 2-N (Parallel Execution Recommended):

"I can now draft the remaining chapters (2-[N]) using two approaches:

Parallel (Faster): Launch [N-1] background agents, one per chapter, all drafting simultaneously
Sequential: Draft one chapter at a time in order

Which approach would you prefer?"

Parallel Drafting Workflow (Recommended):

Launch one background task per remaining chapter:

For each chapter N (where N = 2 to total chapters):

delegate_task(
  category="unspecified-high",
  description="Draft Chapter N of [Project Name]",
  prompt="TASK: Draft Chapter N as complete prose (1,000-1,400 words).

  REQUIRED CONTEXT FILES TO READ:
  - Outline/outline-chapter-N.md (chapter beat sheet)
  - Style.md (narrative voice, tone, language rules)
  - Characters.md (character profiles)
  - Worldbuilding.md (setting, atmosphere)
  - Timeline.md (chronological accuracy)
  - Synopsis.md (story direction)
  - Chapters/chapter-1.md (established voice from approved chapter)
  - Chapters/chapter-(N-1).md (if N > 2, for continuity)

  DRAFTING REQUIREMENTS:
  - Transform outline beats into full prose
  - Show moment-by-moment, never summarize
  - Follow Style.md voice and tone exactly
  - Maintain 1,000-1,400 words
  - Preserve emotional restraint and subtlety
  - Honor established character behavior
  - Respect silence and stillness as narrative tools

  OUTPUT: Save complete draft to Chapters/chapter-N.md
  Format:
  # Chapter N: [Title]
  [Complete prose draft]

  MUST DO: Read ALL context files before drafting. Cross-check continuity with previous chapter.
  MUST NOT: Add plot events not in outline. Change established voice. Summarize instead of showing.",
  run_in_background=true
)


Announce all tasks launched:

"Launched [N-1] parallel drafting agents for Chapters 2-[N]. You'll be notified as each completes. Estimated time: [X] minutes."

Sequential Drafting Workflow (Alternative):

For each Chapter N (2 to total):

Read context files:

Outline/outline-chapter-N.md
Style.md, Characters.md, Worldbuilding.md
Timeline.md, Synopsis.md
Chapters/chapter-(N-1).md (for continuity)

Draft complete chapter (1,000-1,400 words)

Transform outline beats into full prose
Show moment-by-moment, never summarize
Follow Style.md exactly
Preserve emotional restraint

Save to Chapters/chapter-N.md

Announce: "Chapter [N] drafted."

Move to next chapter immediately

After all chapters drafted:

"All [N] chapters drafted. Ready to begin chapter reviews?"

Step 13: Review Each Chapter

Important: Review and refine each chapter draft while preserving voice and intent.

Execution Strategy:

Recommend Parallel Execution:

"I can review all [N] chapters using two approaches:

Parallel (Faster): Launch [N] background agents, one per chapter, all reviewing simultaneously
Sequential: Review one chapter at a time in order

Which approach would you prefer?"

Parallel Review Workflow (Recommended):

Launch one background task per chapter:

For each chapter N (1 to total chapters):

delegate_task(
  category="unspecified-high",
  description="Review and refine Chapter N of [Project Name]",
  prompt="TASK: Review and gently refine Chapter N draft.

  EXPECTED OUTCOME: Improved draft saved as Chapters/chapter-N.md, preserving author's style, intent, emotional subtlety, narrative stillness, and requirements from Style.md.

  REQUIRED CONTEXT FILES TO READ:
  - Chapters/chapter-N.md (current draft)
  - Outline/outline-chapter-N.md (original plan)
  - Chapters/chapter-(N-1).md (if N > 1, for continuity)
  - Chapters/chapter-(N+1).md (if exists, for forward continuity)
  - Style.md (voice and tone guidelines)
  - Characters.md (character consistency)
  - Timeline.md (chronological accuracy)
  - Worldbuilding.md (setting consistency)

  REVIEW FOCUS AREAS:
  - Language: Reduce redundancy, tighten phrasing, improve rhythm
  - Emotion: Clarify undercurrents, strengthen subtext, avoid over-explanation
  - Dialogue: Make speech natural, remove exposition, preserve character voice
  - Pacing: Smooth transitions, balance stillness and movement
  - Word count: Ensure 1,000-1,400 words; expand slightly if needed

  REVISION PRINCIPLES:
  - Preserve author's voice above all else
  - Revise gently; never overwrite intention
  - Clarify emotion without explaining it
  - Maintain narrative stillness and restraint
  - Respect ambiguity and silence
  - Improve rhythm, not drama

  MUST DO: Cross-check with outline, prior/next chapters, and all context files. Revise only language, rhythm, and subtlety—never change events or add plot. Save when refined and elegant.

  MUST NOT: Introduce new scenes or events. Break authorial voice. Over-explain or summarize emotion. Resolve ambiguity without cause. Add new characters. Resolve future conflicts.

  OUTPUT: Save refined draft to Chapters/chapter-N.md (overwrite existing draft).",
  run_in_background=true
)


Announce all tasks launched:

"Launched [N] parallel review agents for all chapters. You'll be notified as each completes. Estimated time: [X] minutes."

Wait for all tasks to complete, then announce:

"All [N] chapters reviewed and refined. Ready for final continuity check?"

Sequential Review Workflow (Alternative):

For each Chapter N:

Read files:

Chapters/chapter-N.md (current draft)
Outline/outline-chapter-N.md (original plan)
Chapters/chapter-(N-1).md (previous chapter)
Style.md, Characters.md, Timeline.md, Worldbuilding.md

Review focus areas:

Language: Reduce redundancy, improve rhythm
Emotion: Clarify subtext, avoid over-explanation
Dialogue: Natural speech, preserve character voice
Pacing: Smooth transitions, balance stillness and movement
Word count: 1,000-1,400 words

Revision principles:

Preserve author's voice above all
Revise gently; never overwrite intention
Clarify emotion without explaining
Maintain narrative stillness and restraint
Respect ambiguity and silence
Improve rhythm, not drama
DO NOT add new plot events
DO NOT introduce new characters
DO NOT resolve future conflicts

Save revised chapter to Chapters/chapter-N.md

Announce: "Chapter [N] reviewed and refined."

Move to next chapter immediately

After all chapters reviewed:

"All [N] chapters reviewed and refined. Ready for final continuity check?"

Step 14: Final Continuity Check

Important: Detect and report inconsistencies across all chapters without altering content.

Announce start:

"Running final continuity check across all chapters..."

Continuity Check Process:

Load all files:

All Chapters/chapter-N.md files
Timeline.md
Characters.md
Worldbuilding.md
Synopsis.md
Conflict.md

Check for inconsistencies in:

Timeline: Event order, time compression/expansion, day/night logic
Character: Behavioral consistency, emotional jumps, knowledge continuity
Worldbuilding: Rule violations, setting inconsistencies, physical geography
Emotional continuity: Sudden shifts, repeated beats, regression without cause
Thematic: Accidental dilution or contradiction of core themes

Detection rules:

Observe without interfering
Flag inconsistencies, not stylistic preferences
Respect intentional ambiguity
Never impose interpretation
Preserve author's authority over meaning

Create diagnostic report:

Save to Research/continuity_diagnostic_report.md:

# Continuity Diagnostic Report

Generated: [Date]
Scope: All chapters (1-N)

## Summary of Findings
[High-level overview of what was checked]

## Confirmed Consistencies
[List elements that are properly consistent]

## Potential Issues

### Timeline
[Issues with references to specific chapters/lines]

### Character Behavior
[Issues with references]

### Worldbuilding
[Issues with references]

### Emotional Continuity
[Issues with references]

### Thematic Elements
[Issues with references]

## Questions for Author

For each flagged issue, provide 1-3 focused questions:

**Issue 1:** [Description]
- Question: [Neutral, specific question]
- Rationale: [Why this question is useful]

[Continue for each issue]


Output rules:

Use neutral, observational language
Reference exact chapter and section
Offer questions instead of conclusions
DO NOT propose rewrites
DO NOT change tone or language
DO NOT resolve ambiguity for the author

After creating report:

"Continuity check complete. Report saved to Research/continuity_diagnostic_report.md

Found [N] potential issues for your review. These are questions, not problems—you decide what needs addressing."

Step 15: Complete & Present

Create final verification summary:

"Your novel project [Project Name] is complete! Here's what's been created:

Foundation Files: ✓ Braindump.md (North Star, theme, structure) ✓ Genre.md (conventions, tone, boundaries) ✓ Style.md (voice, rhythm, influences) ✓ Characters.md ([N] character profiles) ✓ Worldbuilding.md (setting and atmosphere) ✓ Conflict.md (stakes and opposition) ✓ Synopsis.md (full story outline) ✓ Timeline.md (event chronology)

Chapter Work: ✓ [N] chapter outlines (Outline/ folder) ✓ [N] drafted chapters (Chapters/ folder) ✓ [N] reviewed and refined chapters ✓ Continuity diagnostic report

Project Folders: ✓ Research/ (continuity report and notes) ✓ Archive/ (for old drafts) ✓ Assets/ (for visual references)

Next Steps:

Review continuity report (Research/continuity_diagnostic_report.md)
Address any issues you want to resolve
Continue refining individual chapters as needed

Your complete novel draft is ready in ~/writing/novels/{project-name}/

I can help you:

Revise specific chapters
Address continuity issues
Brainstorm scenes or dialogue
Refine character arcs

What would you like to work on?"

Present the project to user:

Use present_files tool to share key files (optional based on user preference).

Drafting Chapters

When user asks to draft a chapter:

Read the chapter's outline file
Read all context files (Style, Characters, Worldbuilding, Synopsis, Timeline)
Draft the chapter following Style.md guidelines
Aim for 1,000-1,400 words per chapter
Show moment-by-moment rather than summarizing
Preserve emotional restraint and subtlety
Save to Chapters/chapter-N.md
Revising Chapters

When user asks to revise a chapter:

Read current chapter draft
Read chapter outline
Read previous chapter (for continuity)
Read context files
Refine language, rhythm, emotional clarity
Preserve author's voice—never overwrite intent
Around 1,000-1,400 words; expand slightly if needed
Save revised version
Checking Continuity

When user asks to check continuity:

Read target chapters
Read Timeline, Characters, Worldbuilding
Check for:
Timeline contradictions
Character behavior inconsistencies
Worldbuilding violations
Emotional jumps without cause
Create diagnostic report in Research/continuity_report.md
Flag issues with questions, not conclusions
Never rewrite—only observe
Language Handling
English Projects
All content in English
Standard literary conventions
Hindi Projects
All content in Hindi (Devanagari script)
Culturally appropriate terminology
Hindi literary conventions
Bilingual Projects
User chooses language per file
Support code-switching where appropriate
Quick Mode (Minimal Setup)

Trigger phrases:

"quick novel setup"
"just the basics"
"minimal structure"

Quick mode process:

Ask only: name, language, core idea
Create directory structure with README files
Create minimal Braindump.md with placeholders:
## North Star
[To be filled]

## Title
[To be filled]

## Core Idea
[User's initial idea]

## Central Theme
[To be filled]

## Structure
[To be filled]

Create empty placeholder files for all other documents
Tell user: "Basic structure created. You can fill in details later or ask me to complete any section."
Updating Existing Projects

If project already exists:

Read existing files first
Ask what to update:
Add more chapters?
Revise character profiles?
Update outline?
Expand worldbuilding?
Show proposed changes before writing
Never overwrite without confirmation
Archive old versions before updating
Tone Guidelines for All Interactions

Throughout the entire process:

Calm, patient, emotionally attentive
No rush, no pressure
Gentle, human language (avoid technical jargon)
Reflective rather than directive
Mirror emotional truth back to the author
Respect silence, uncertainty, and ambiguity
Protect authorial intent above all else
Build trust through careful listening
Self-Review Checklist (Internal)

Before proceeding with any file write:

 Have ALL sections been approved by the user?
 Am I preserving the author's voice and intent?
 Am I respecting emotional truth over narrative formula?
 Have I waited for explicit approval (not assumed)?
 Is the content stored correctly in memory?
 Am I writing files only when complete?
Hard Boundaries
Will NOT:
Rush the process or skip sections
Invent narrative without author grounding
Write files before all sections approved
Revise completed files without explicit request
Impose formulaic structure over emotional truth
Assume clarity when uncertainty exists
Narrate internal operations to the user
Will:
Work patiently, one section at a time
Mirror emotional truth back reflectively
Wait for explicit approval at each step
Preserve authorial voice and intent
Respect ambiguity and silence
Protect the author's creative authority
Allow the story to emerge naturally
Example Invocations
Example 1: Full Interactive Setup
User: "Help me create a novel project"

Weekly Installs
1.4K
Repository
junaid18183/nov…t-skills
GitHub Stars
1
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass
---
title: dndtale
url: https://skills.sh/mickume/dndtale/dndtale
---

# dndtale

skills/mickume/dndtale/dndtale
dndtale
Installation
$ npx skills add https://github.com/mickume/dndtale --skill dndtale
SKILL.md
Dndtale - DnD Campaign & Adventure Creator

Dndtale is a specialized skill designed to assist Dungeon Masters and creative content creators in building complete, engaging Dungeons & Dragons campaigns and adventures.

Quick Start
For New Campaigns
Use TaskCreate immediately to create a planning checklist
Follow the workflow: workflows/campaign-creation-workflow.md
Use AskUserQuestion to gather requirements if not provided
Use templates: All templates are in templates/
Quality check: Use checklists/campaign-quality-checklist.md when done
For Updating Existing Campaigns
Read existing content before making changes
Follow the iteration workflow: workflows/iteration-workflow.md
Check consistency: Use checklists/consistency-checklist.md
Use Edit tool for targeted changes to existing files
Need an Example?

See the complete sample campaign: examples/the-stolen-flame/

What Dndtale Does

This skill helps you create:

Complete Campaigns - Multi-session story arcs with interconnected plots, factions, and long-term consequences
One-Shot Adventures - Single-session adventures with clear objectives and satisfying conclusions
NPCs - Memorable characters with personalities, motivations, secrets, and stat blocks
Locations - Detailed settings with atmosphere, history, and interactive elements
Encounters - Balanced challenges with multiple solutions and meaningful consequences
Story Frameworks - Narrative structures that preserve player agency while ensuring coherent plots
Image Prompts - Detailed prompts for AI image generation tools
Core Principles
Creative Voice
Write with evocative, atmospheric prose — lead with mood, not measurements (see creative-voice.md)
Engage multiple senses in every scene description
Give every NPC a want, a speech pattern, and an opinion
Design encounters as drama engines, not math problems
Player Agency First
Always provide multiple solutions to problems
Design consequences that matter and ripple forward
Avoid railroading (forced single paths)
Let player choices shape the story
Character backstories are campaign fuel — weave them in
Usability at the Table
Write clear, scannable DM notes
Provide concise read-aloud text
Include quick reference tables
Anticipate common DM needs
Completeness and Consistency
Cross-reference between documents
Maintain timeline and logic
Keep names and facts consistent
Check dependencies when changing content
Use the Right Tools
TaskCreate/TaskUpdate: Track complex campaign creation tasks
AskUserQuestion: Clarify requirements and gather preferences
Read: Always read existing files before editing
Edit: Make targeted changes to existing content
Write: Create new files from templates
dndig: Generate campaign artwork (see dndig-reference.md)
File Organization

Every campaign should follow this structure:

campaigns/[campaign-name]/
├── campaign-overview.md         # Master document with full campaign arc
└── changelog/                   # Changelogs
    └── [change-name].md         # Documented changes to the campaign
├── README.md                  # Player-facing session zero document (spoiler-free)
├── chapter-01.md                # Detailed session content
├── chapter-02.md                # Continue for each chapter/session
├── chapters-summary.md          # Chapter/Scene-level summaries for all chapters of the campaign
├── npcs.md                      # Important characters with stats and motivations
├── locations.md                 # Key places with descriptions
├── factions.md                  # Organizations and their goals (optional)
├── timeline.md                  # Timeline of events in the campaign (optional)
└── art/                         # Image prompts and artwork
    ├── [scene-name].md          # Image generation prompts for scenes
    ├── [location-name].md       # Image generation prompts for locations/environment
    ├── [npc-name].md            # Image generation prompts for unique NPCs
    └── [generated-images.jpg]   # Actual artwork *.jpg (if generated)

Resource Library
Templates

Use these as starting points for all campaign documents:

campaign-overview.md - Master campaign document
chapter-template.md - Individual session structure
chapters-summary.md - Scene-level overview for all chapters of the campaign
timeline.md - Timeline of events in the campaign
README.md - Player-facing session zero document
npcs.md - NPC roster and details
locations.md - Location descriptions and maps
factions.md - Organizations and politics
Modules

Reference these for detailed guidance:

creative-voice.md - Creative identity, voice guidelines, writing philosophy
campaign-types.md - Linear, Sandbox, Event-Based, Setting-Based
world-building.md - Settings, NPCs, villain design, moral complexity, themes
encounter-design.md - Encounter philosophy, checklist, variety matrix, boss design
session-pacing.md - Session arc, dramatic structure, pacing tools
literary-adaptation.md - Adapting novels, films, mythology into campaigns
formatting-conventions.md - How to format all content
dndig-reference.md - AI image generation tool reference
Workflows

Step-by-step processes for different tasks:

campaign-creation-workflow.md - Complete campaign creation from start to finish
iteration-workflow.md - Updating and refining existing campaigns
Checklists

Quality assurance for your work:

campaign-research-checklist.md - Pre-creation foundation and research checklist
campaign-quality-checklist.md - Ensure completeness, balance, and quality
consistency-checklist.md - Maintain consistency when making changes
Examples

Complete sample campaigns demonstrating all templates:

The Stolen Flame - One-shot adventure showing all templates in action
Workflow Overview
Creating a New Campaign

Phase 1: Gather Requirements

Use TaskCreate to build a planning checklist
Use AskUserQuestion if briefing incomplete
Collect: story idea, length, level, setting, tone
If adapting source material, follow literary-adaptation.md
Complete campaign-research-checklist.md

Phase 2: Campaign Framework

Choose campaign type (see modules/campaign-types.md)
Create campaign-overview.md (use template)
Plan chapter breakdown with session pacing (see session-pacing.md)
Create chapters-summary.md (use template)
Identify major NPCs and locations

Phase 3: Detailed Development

Write each chapter using creative-voice.md for writing quality
Design encounters using encounter-design.md for variety and depth
Detail NPCs using tiered framework in world-building.md
Detail locations (use template)
Create factions if needed (use template)

Phase 4: Player-Facing Content

Write README.md (use template)
Ensure there are NO SPOILERS in the briefing

Phase 5: Polish & QA

Create image prompts for key scenes using dndig-reference.md
Run through campaign-quality-checklist.md
Read entire campaign for flow and consistency

See detailed workflow: workflows/campaign-creation-workflow.md

Updating an Existing Campaign
Read all affected files first
Plan changes and identify dependencies
Edit existing files with targeted changes
Update cross-references
Check consistency with consistency-checklist.md

See detailed workflow: workflows/iteration-workflow.md

Important Guidelines
Always Do This

Use TaskCreate/TaskUpdate for Complex Tasks

Create planning checklist immediately with TaskCreate
Track progress through creation phases
Mark tasks completed with TaskUpdate as you finish them
Keep exactly ONE task in_progress at a time

Ask Questions When Needed

Use AskUserQuestion for unclear requirements
Clarify tone, content boundaries, player preferences
Ask about multiple valid approaches
Don't guess—confirm with the DM

Read Before Editing

Always Read existing files before using Edit
Understand the full context
Check dependencies and cross-references
Maintain consistency with existing content

Preserve Player Agency

Provide multiple solutions to every problem
Design meaningful consequences
Allow creative approaches
Avoid forced single paths

Follow Templates

Use the templates in templates/
Maintain consistent formatting
Include all required sections
Match the style of examples
Never Do This

Don't Railroad Players

Never force a single solution
Don't invalidate player choices
Avoid "the NPC does everything" solutions

Don't Skip Quality Checks

Always use checklists before completion
Verify cross-references work
Check name consistency
Test story logic

Don't Forget Documentation

Cross-reference between documents
Link to related content
Include DM notes and tips
Provide stat blocks or references

Don't Break Existing Content

When editing, maintain story logic
Update all references to changed content
Check timeline consistency
Preserve what works
Session Zero Considerations

Unless stated otherwise, campaigns are written for consenting adults. When content might be disturbing or NSFW:

Include content warnings in README.md
Suggest Session Zero discussion topics
Recommend safety tools (X-Card, Lines & Veils)
Clearly mark mature content
Standard D&D Adventure Structure

The skill follows professional D&D adventure conventions (see STRUCTURE.md for full details):

Front Matter: Introduction, synopsis, hooks Core Structure: Chapter breakdown with scenes, encounters, NPCs Climax: Epic final encounter with multiple resolution paths Back Matter: Appendices with stat blocks, magic items, handouts

Each Chapter Includes:

Read-aloud text for scene setting
DM information and secrets
Encounter design (combat, social, skill challenges)
NPCs with personality and stats
Treasure and rewards
Connections to other chapters
Formatting Standards

Follow conventions in modules/formatting-conventions.md:

Read-Aloud Text:

> Text the DM reads to players
> Detailed, evocative, multi-sensory
> Present tense, no secrets


DM Notes: Regular text with mechanical details, secrets, contingencies

Stat Blocks: Reference Monster Manual when possible, or provide custom stats

Cross-References: Use markdown links: [Chapter 2](chapter-02.md) or [NPCs](npcs.md#npc-name)

Image Prompts: Create in art/ folder with proper metadata

Quick Reference
Campaign Types
Linear: Sequential chapters, clear path (easiest to prep)
Sandbox: Central hub, many options (most prep)
Event-Based: Timeline of events, player actions affect outcomes
Setting-Based: Location-focused, exploratory

See: modules/campaign-types.md

Encounter Design
Every fight answers: "Why is this fight happening, and what changes when it's over?"
Terrain is the third combatant — environment should force choices
Give enemies goals beyond "kill the party" (escape, protect, buy time, capture)
Use the Encounter Design Checklist: dramatic question, stakes, environment, multiple approaches, escalation, connection
Track variety with the Encounter Variety Matrix (combat/social/exploration/hybrid subtypes)
Boss fights need phases, legendary actions, emotional stakes, and multiple victory conditions

See: modules/encounter-design.md

NPC Design
Tier 1 (Walk-On): One trait, one useful thing, a rememberable name
Tier 2 (Recurring): Want vs. need, opinions about other NPCs, a secret, speech patterns
Tier 3 (Major): Full inner life, independent arc, mechanical weight, voice, relationship web
Villains: Motivation, Method, Vulnerability, Escalation, Mirror

See: modules/world-building.md, templates/npcs.md

Location Design
Atmosphere (sights, sounds, smells, feel)
History and current situation — use environmental storytelling
NPCs present and encounters
Secrets to discover — layered puzzles that reward curiosity

See: modules/world-building.md, templates/locations.md

Tone and Content

Adjust to DM's requested tone:

Heroic & Epic
Dark & Serious
Humorous & Lighthearted
Mystery & Intrigue
Horror
Adult-themed/NSFW (with appropriate warnings)

Always:

Match requested tone consistently
Warn about mature content in briefing
Provide Session Zero guidance for sensitive topics
Image Generation with dndig

Use dndig (../dndig) to generate campaign artwork from prompt files. See dndig-reference.md for complete documentation.

Quick usage:

dndig campaigns/my-campaign/art/throne-room.md --verbose


Prompt file format:

---
title: throne-room
aspect_ratio: "16:9"
resolution: 2K
temperature: 0.8
batch: 2
instructions: campaign-style.md
references:
  - refs/gothic-castle.jpg
---

Detailed visual description based on scene read-aloud text...
Include: composition, lighting, mood, style, atmosphere.


Key features:

Style consistency: Create a shared instructions file for the campaign's visual style
Reference images: Up to 14 reference images for style grounding (character consistency, architectural style)
Batch generation: Generate 1–4 variations per prompt
Aspect ratios: 1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9
Resolutions: 512px, 1K, 2K, 4K

Create prompts for:

Key locations and scenes (16:9 or 4:3 at 2K)
Important NPCs and character portraits (2:3 or 3:4 at 2K)
Climactic encounters (16:9 at 2K)
Maps and dungeons (1:1 or 4:3 at 2K+)
Items and artifacts (1:1 at 1K)
Examples in Action
Example: Starting a New Campaign
DM: "I want to create a 3-session campaign about smugglers in a port city"

You:
1. TaskCreate: Create planning checklist
2. AskUserQuestion: Clarify tone, starting level, player count
3. Choose campaign type: Sandbox (city hub with multiple quest lines)
4. Create campaign-overview.md from template
5. Create 3 chapters, npcs.md, locations.md
6. Create README.md for players
7. Run quality checklist
8. Create image prompts and generate art with dndig
9. Deliver organized campaign

Example: Updating Existing Campaign
DM: "The players killed the quest-giver NPC. I need to adapt."

You:
1. Read campaign-overview.md and affected chapters
2. Read npcs.md to understand the NPC's role
3. Follow iteration-workflow.md
4. Options:
   - Introduce heir/assistant to replace NPC
   - Redistribute quests to other NPCs
   - Show consequences of NPC death
5. Edit affected chapters
6. Update npcs.md and cross-references
7. Run consistency checklist

Success Criteria

A campaign is ready when:

 All chapters are complete and detailed
 NPCs have personality, motivations, and stats
 Locations are described with atmosphere and features
 Multiple solutions exist for every problem
 Cross-references are accurate
 Briefing is complete and spoiler-free
 Quality checklist passes
 DM can run Session 1 with current materials
Getting Help

Stuck on something?

Check the relevant module in modules/
Review the workflow in workflows/
Look at the example in examples/the-stolen-flame/
Use AskUserQuestion to clarify with the DM

Need to verify quality?

campaign-quality-checklist.md
consistency-checklist.md
Remember

You're helping a DM create memorable experiences for their players. Focus on:

✓ Usability - Easy to run at the table ✓ Flexibility - Multiple solutions, player agency ✓ Completeness - All necessary information present ✓ Consistency - Names, facts, timeline all align ✓ Quality - Engaging stories, balanced encounters, memorable moments

Good luck, and may your campaigns be legendary!

Weekly Installs
31
Repository
mickume/dndtale
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
---
rating: ⭐⭐
title: suno-music-creator
url: https://skills.sh/schwepps/skills/suno-music-creator
---

# suno-music-creator

skills/schwepps/skills/suno-music-creator
suno-music-creator
Installation
$ npx skills add https://github.com/schwepps/skills --skill suno-music-creator
Summary

AI-powered music creation with Suno V5 and Studio, supporting single tracks, playlists, and commercial projects.

Supports V5 model with persistent musical memory across 8-minute generations, authentic vocal synthesis, and negative prompting to exclude unwanted elements
Includes structured prompt formulas, style library by genre, BPM guides, and meta-tag system for precise control over song structure and vocal characteristics
Suno Studio (Premier tier) offers multi-track editing, stem separation, take lanes, section replacement, and MIDI export for professional post-production workflows
Commercial rights included on Pro and Premier plans; best practices cover corporate anthems, playlists with energy curves, and client revision workflows
SKILL.md
Suno Music Creator

Professional workflow for creating high-quality music with Suno AI V5 and Suno Studio.

Quick Reference
Topic	Reference File
Style prompts by genre	references/style-library.md
BPM guide by usage	references/bpm-guide.md
Structure & meta-tags	references/metatags.md
Project templates	references/project-types.md
Distribution & rights	references/distribution.md
Plan Availability
Feature	Pro ($10/mo)	Premier ($30/mo)
V5 Model	✅	✅
Commercial rights	✅	✅
Suno Studio (DAW)	❌	✅
Credits/month	2,500	10,000
Core Workflow
1. Project Setup

Gather requirements:

Type: Single track / Playlist / Album
Purpose: Personal / Client / Commercial distribution
Style: Genre(s), mood, energy level
Voice: Male / Female / Mix / Instrumental
Language: Target language for lyrics
Duration: Track length or playlist total time (up to 8 min per generation)
Constraints: Content restrictions, brand guidelines
2. Prompt Construction

Style prompt formula:

[Genre], [BPM] BPM, [Mood], [Key instruments], [Vocal type], [Production style]


Negative prompting (V5): Add exclusions directly:

Upbeat pop, 120 BPM, no guitars, no harsh distortion, clean mix


Lyrics structure: Place meta-tags in lyrics field (more effective than style prompt):

[Section Tag]
[Mood/Energy instruction]
Lyrics content (6-12 syllables per line for best alignment)


Consult references/style-library.md for tested prompts by genre. Consult references/metatags.md for structure tags and vocal controls.

3. Generation Process
Generate 2-4 versions per track (V5 is 10x faster)
Select best output based on:
BPM accuracy (verify with external tool if critical)
Vocal clarity and emotion (V5 has authentic vocal tone)
Mix quality and instrument separation
Adherence to prompt
Apply post-processing:
Extend: Add sections, fix abrupt endings (use callbacks: "continue with same vibe")
Remaster: Subtle (uniform quality) / Medium / Wide (more variation)
Crop: Remove unwanted intro/outro
Cover: Change style or voice
Replace Section: Regenerate specific parts (Studio)
4. Quality Checklist
 BPM matches target (±5 BPM acceptable)
 Vocals clear and expressive
 No audio artifacts (V5 has better frequency separation)
 Structure complete (intro → verses → chorus → outro)
 Energy level appropriate for purpose
 Lyrics audible and correct
 Musical memory consistent (motifs recur correctly across 8 min)
5. Export & Delivery
Distribution: WAV 16-bit/44.1kHz
Preview/Draft: MP3 320kbps
Stems: Vocals, drums, bass, guitar, synths, etc. (Pro/Premier)
MIDI: Export available (Studio)
Artwork: 3000x3000px for distribution
Suno Studio (Premier Only)

Suno Studio is a Generative Audio Workstation (GAW) combining DAW editing with AI generation.

Key Features
Feature	Description
Multi-track Timeline	Arrange, layer, edit with precision
Stem Separation	Auto-split into vocals, drums, bass, etc.
Take Lanes	Compare multiple generated versions
Comping	Combine best parts from different takes
Replace Section	Regenerate any slice with smooth crossfades
BPM/Pitch Control	Adjust tempo and pitch per track
Record Audio	Record directly into timeline
Sample to Song	Upload short clips, expand to full compositions
MIDI Export	Export for external DAW editing
Auto-save	Projects save automatically
Studio Workflow
Create or import song into Studio
View stems in Details panel → Insert All to timeline
Use Take Lanes to audition versions
Comp best sections to Main Track
Add/Replace instruments or vocals
Export: Full Song, Selected Range, or Multitracks
V5 Features Summary
Feature	Benefit
Persistent Memory	Motifs stay consistent across 8 minutes
Negative Prompting	Exclude elements: "no vocals", "no guitars"
Better Vocals	Natural pronunciation, authentic emotion
Cleaner Mix	Superior frequency separation, less "mud"
Faster Generation	10x speed improvement
Intelligent Arrangement	Auto-structures verses, choruses, bridges
Hoooks	Create shareable short clips for promotion
Project-Specific Workflows
Single Track
Define style, mood, target duration (up to 8 min)
Write structured lyrics with meta-tags (6-12 syllables/line)
Generate and select best version
Extend if needed (use callbacks for consistency)
Remaster (Subtle) for polish
Playlist Creation
Define theme, total duration, track count
Plan energy curve (see references/bpm-guide.md)
Create consistent style template or save a Persona
Generate tracks following progression
Remaster all tracks (Subtle) for cohesion
Verify total timing and transitions
Corporate/Client Projects
Research context (company, brand, values)
Identify key messages and tone
Write lyrics incorporating brand elements
Generate with appropriate professional style
Use Studio (Premier) for precise editing if needed
Prepare multiple versions for client review
Document process for revisions
Best Practices
Do
Specify exact BPM for tempo-critical projects
Write original lyrics (strengthens copyright claims)
Use era references ("80s synths", "90s boom bap")
Keep prompts focused: 1-2 genres + 1 mood + instruments
Front-load important tags in first lines
Use callbacks on Extend: "continue with same vibe as chorus"
Use negative prompting to exclude unwanted elements
Save successful prompts and Personas for reuse
Keep lyrics to 6-12 syllables per line for best alignment
Don't
Name specific artists (copyright risk)
Overload prompts with contradicting terms
Use vague descriptions ("cool song")
Skip the Remaster step for playlists
Ignore content restrictions for target audience
Chain too many Extends without callbacks (causes drift)
Commercial Rights
Pro/Premier accounts: Commercial rights included
Write original lyrics: Reinforces your rights
Keep invoices: Proof of license for distributors
After cancellation: Rights retained on created content

For distribution details, see references/distribution.md.

Weekly Installs
649
Repository
schwepps/skills
GitHub Stars
10
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
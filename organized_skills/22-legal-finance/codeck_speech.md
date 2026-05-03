---
rating: ⭐⭐⭐
title: codeck-speech
url: https://skills.sh/hiyeshu/codeck/codeck-speech
---

# codeck-speech

skills/hiyeshu/codeck/codeck-speech
codeck-speech
Installation
$ npx skills add https://github.com/hiyeshu/codeck --skill codeck-speech
SKILL.md
codeck speech
Role activation

Read $DECK_DIR/diagnosis.md. If a speech role is recommended, use it. Otherwise, pick a coach based on domain and audience:

Technical → Feynman: simplify the complex, bridge with analogy

Business → Jobs: build anticipation, one "one more thing"

Academic → Hans Rosling: let data tell the story

Setup
DECK_DIR="$HOME/.codeck/projects/$(basename "$(pwd)")"
mkdir -p "$DECK_DIR"
bash "$HOME/.claude/skills/codeck/scripts/status.sh" "$DECK_DIR"


Read:

HTML (latest *-r*.html) — actual slide content
outline.md — structure, arc, user intent
design-notes.md — visual intent (speech rhythm should match visual rhythm)

If no HTML and no outline, suggest /codeck-design or /codeck-outline first.

If only outline exists, write based on outline — note that the script is based on structure, not final visuals.

Smart skip: skip questions if user's instruction already specifies style and duration.

Questions
Q1: Style
A) TED — conversational, story-driven, breathing room
B) Formal — structured, precise language
C) Casual — natural, humor ok
Q2: Duration
A) 5 min — lightning, ~1000 words
B) 15 min — standard, ~3000 words
C) 30+ min — deep dive, ~6000 words
Generate

Before writing, build a fragment map. For each slide in the HTML, list: slide number, title, fragment count (data-f elements). This map determines the speech structure — slides with fragments get ### [on enter] + ### [fragment N] sections, slides without get a single block. Do not skip this step.

Write a complete, readable-aloud transcript. Page by page.

Rules
One section per slide — matches the deck
Transitions — natural bridges between pages
Stage directions — write in the same language as the transcript. Chinese: [停顿 2秒] [放慢] [看观众]; English: [pause 2s] [slow down] [look at audience]; other languages: translate accordingly. The speaker must understand them without switching languages.
Word count — ~200 words/min Chinese, ~130 words/min English
Source-based — no fabricated data
Strong opening — story, data, or question
Strong close — callback to opening or call to action
Style notes

TED: use "you" / "we", mix short and long sentences, pause after key points, end by echoing the opening.

Formal: complete sentences, logical progression, summarize + outlook at the end.

Casual: colloquial, self-deprecating ok, casual transitions, end with a surprise.

Time budget
Slide	Title	Words	Estimate
1	...	...	...
A) Help me trim the ones over time
B) I'll manage it myself
Write back HTML data-notes (fragment-synced)

The engine's buildNotes() concatenates the slide's data-notes with each visible fragment's data-notes as the presenter steps through. Use this to sync speech rhythm with fragment rhythm.

How it works
Read the slide's fragments — find all elements with data-f="N" to know the stepping order
Split the speech into segments — one segment per step (slide entry + each fragment)
Assign notes to each step:
Slide's data-notes → what to say when the slide first appears (before any fragment)
data-f="1" element's data-notes → what to say when fragment 1 reveals
data-f="2" element's data-notes → what to say when fragment 2 reveals
...and so on
Example

Speech for slide 3:

"Let's talk about the three ideas behind codeck. [pause 2s] First, it recruits people, not rules. [pause] Second, isomorphic mapping. [pause] Third, no schema ceiling."

Slide 3 has data-f="1", data-f="2", data-f="3":

<section class="slide" data-notes="Let's talk about the three ideas behind codeck. [pause 2s]">
  <h2 data-f="1" data-notes="First, it recruits people, not rules. [pause]">People, not rules</h2>
  <p data-f="2" data-notes="Second, isomorphic mapping. [pause]">Isomorphic mapping</p>
  <p data-f="3" data-notes="Third, no schema ceiling.">No schema ceiling</p>
</section>


Presenter presses → three times. Notes build up progressively:

Step 0: "Let's talk about the three ideas..."
Step 1: + "First, it recruits people..."
Step 2: + "Second, isomorphic mapping..."
Step 3: + "Third, no schema ceiling."
Rules
If a slide has no fragments, put the full speech in the slide's data-notes
HTML-escape quotes inside data-notes attribute values
Keep stage directions ([pause], [slow down], etc.) in the notes
Each segment should be self-contained — the presenter reads what's new at each step
Match the number of speech segments to the number of steps (1 + fragment count)
Output: $DECK_DIR/speech.md
---
style: "{style}"
duration: "{target}"
totalEstimate: "{estimate}"
---

# Speech: {topic}

---

## Slide 1: {title}
<!-- estimate: {N}s | {M} words | fragments: 0 -->

{verbatim speech text}

[pause 2s]

---

## Slide 2: {title}
<!-- estimate: {N}s | {M} words | fragments: 3 -->

### [on enter]

{what to say when slide appears, before any fragment}

### [fragment 1]

{what to say when fragment 1 reveals}

### [fragment 2]

{what to say when fragment 2 reveals}

### [fragment 3]

{what to say when fragment 3 reveals}

---

Done

Point to the single strongest moment in the script — the line or pause that will land hardest:

codeck speech done.

Strongest moment: {slide N — what happens and why it works. e.g., "Slide 4, the three-second pause after the question. That silence is where the audience decides you're worth listening to."}

{one line — readiness assessment}

Output: $DECK_DIR/speech.md + HTML data-notes updated Press P in the deck for speaker mode to see the script.

All done. Need to export? /codeck-export. Check progress anytime with /codeck.

Weekly Installs
131
Repository
hiyeshu/codeck
GitHub Stars
207
First Seen
Mar 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
---
title: tutor
url: https://skills.sh/roundtable02/tutor-skills/tutor
---

# tutor

skills/roundtable02/tutor-skills/tutor
tutor
Installation
$ npx skills add https://github.com/roundtable02/tutor-skills --skill tutor
Summary

Interactive quiz tutor that tracks concept mastery and identifies knowledge gaps.

Detects user language and maintains a StudyVault directory with a dashboard and per-area concept tracking files
Offers context-aware session types: diagnostic assessment for unmeasured areas, targeted drilling of weak concepts, section selection, or hard-mode review
Grades 4-question quizzes per session, maps results to concepts, and updates proficiency badges (🟥 weak through 🟦 mastered) and error notes
Rephases questions for weak areas to avoid repetition and builds learning history by tracking attempts, correct answers, and unresolved concepts
SKILL.md
Tutor Skill

Quiz-based tutor that tracks what the user knows and doesn't know at the concept level. The goal is helping users discover their blind spots through questions.

File Structure
StudyVault/
├── *dashboard*              ← Compact overview: proficiency table + stats
└── concepts/
    ├── {area-name}.md       ← Per-area concept tracking (attempts, status, error notes)
    └── ...

Dashboard: Only aggregated numbers. Links to concept files. Stays small forever.
Concept files: One per area. Tracks each concept with attempts, correct count, date, status, and error notes. Grows proportionally to unique concepts tested (bounded).
Workflow
Phase 0: Detect Language

Detect user's language from their message → {LANG}. All output and file content in {LANG}.

Phase 1: Discover Vault
Glob **/StudyVault/ in project
List section directories
Glob **/StudyVault/*dashboard* to find dashboard
If found, read it. Preserve existing file path regardless of language.
If not found, create from template (see Dashboard Template below)

If no StudyVault exists, inform user and stop.

Phase 2: Ask Session Type

MANDATORY: Use AskUserQuestion to let the user choose what to do. Analyze the dashboard to build context-aware options, then present them.

Read the dashboard proficiency table and build options based on current state:

If unmeasured areas (⬜) exist → include "Diagnostic" option targeting those areas
If weak areas (🟥/🟨) exist → include "Drill weak areas" option naming the weakest area(s)
Always include "Choose a section" option so the user can pick any area
If all areas are 🟩/🟦 → include "Hard-mode review" option

Present these as an AskUserQuestion with header "Session" and concise descriptions showing which areas each option targets. The user MUST select before proceeding.

Phase 3: Build Questions
Read markdown files in target section(s)
If drilling weak area: also read concepts/{area}.md to find 🔴 unresolved concepts — rephrase these in new contexts (don't repeat the same question)
Craft exactly 4 questions following references/quiz-rules.md

CRITICAL: Read references/quiz-rules.md before crafting ANY question. Zero hints allowed.

Phase 4: Present Quiz

Use AskUserQuestion:

4 questions, 4 options each, single-select
Header: "Q1. Topic" (max 12 chars)
Descriptions: neutral, no hints
Phase 5: Grade & Explain
Show results table (question / correct answer / user answer / result)
Wrong answers: concise explanation
Map each question to its area
Phase 6: Update Files
1. Update concept file (concepts/{area}.md)

For each question answered:

New concept: Add row to table + if wrong, add error note under ### 오답 메모 (or localized equivalent)
Existing 🔴 concept answered correctly: Increment attempts & correct, change status to 🟢, keep error note (learning history)
Existing 🟢 concept answered wrong again: Increment attempts, change status back to 🔴, update error note

Table format:

| Concept | Attempts | Correct | Last Tested | Status |
|---------|----------|---------|-------------|--------|
| concept name | 2 | 1 | 2026-02-24 | 🔴 |


Error notes format (only for wrong answers):

### Error Notes

**concept name**
- Confusion: what the user mixed up
- Key point: the correct understanding

2. Update dashboard
Recalculate per-area stats from concept files (sum attempts/correct across all concepts in that area)
Update proficiency badges: 🟥 0-39% · 🟨 40-69% · 🟩 70-89% · 🟦 90-100% · ⬜ no data
Update stats: total questions, cumulative rate, unresolved/resolved counts, weakest/strongest

Dashboard stays compact — no session logs, no per-question details.

Dashboard Template

Create when no dashboard exists. Filename localized to {LANG}. Example in English:

# Learning Dashboard

> Concept-based metacognition tracking. See linked files for details.

---

## Proficiency by Area

| Area | Correct | Wrong | Rate | Level | Details |
|------|---------|-------|------|-------|---------|
(one row per section, last column = [[concepts/{area}]] link)
| **Total** | **0** | **0** | **-** | ⬜ Unmeasured | |

> 🟥 Weak (0-39%) · 🟨 Fair (40-69%) · 🟩 Good (70-89%) · 🟦 Mastered (90-100%) · ⬜ Unmeasured

---

## Stats

- **Total Questions**: 0
- **Cumulative Rate**: -
- **Unresolved Concepts**: 0
- **Resolved Concepts**: 0
- **Weakest Area**: -
- **Strongest Area**: -

Concept File Template

Create per area when first question is asked. Example:

# {Area Name} — Concept Tracker

| Concept | Attempts | Correct | Last Tested | Status |
|---------|----------|---------|-------------|--------|

### Error Notes

(added as concepts are missed)

Important Reminders
ALWAYS read references/quiz-rules.md before creating questions
NEVER include hints in option labels or descriptions
NEVER use "(Recommended)" on any option
Randomize correct answer position
After grading, ALWAYS update both concept file AND dashboard
Communicate in user's language
Weekly Installs
1.2K
Repository
roundtable02/tu…r-skills
GitHub Stars
822
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
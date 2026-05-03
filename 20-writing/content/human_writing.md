---
title: human-writing
url: https://skills.sh/timlai666/skills/human-writing
---

# human-writing

skills/timlai666/skills/human-writing
human-writing
Installation
$ npx skills add https://github.com/timlai666/skills --skill human-writing
SKILL.md
Human Writing
Overview

Treat this as the default prose skill for anything a person will read. Use it for both rewrite and generate tasks. Aim for writing that sounds like someone meant it, not like a model averaged it.

If another skill owns the structure or domain logic, let that skill drive the content plan and use this skill to shape the final prose.

Workflow
Detect mode.
Use rewrite when source text exists.
Use generate when the user wants new text from notes, bullets, or intent.
Detect audience_and_context.
Identify who will read it and what the text must do.
Distinguish between professional, explanatory, persuasive, personal, editorial, and mixed-use writing.
Detect language_behavior.
Match the user's language by default.
Preserve intentional code-switching unless the user asks to normalize it.
Select style_mode.
Use grounded for professional, factual, restrained, or credibility-sensitive writing.
Use voiced for commentary, essays, persuasive copy, social writing, brand writing, or any case where stronger personality helps.
Draft or rewrite.
Make the prose specific rather than vague.
Make it controlled rather than inflated.
Make it varied rather than templated.
Make it voiced when useful and restrained when needed.
Run a cleanup pass.
Remove AI-writing artifacts, empty intensifiers, filler transitions, fake profundity, over-symmetry, and unnatural em-dash habits.
Keep the meaning, facts, and intent intact.
Mode guide
Rewrite

Use when the user provides source text and wants it to read better.

Preserve the original claim, purpose, and factual boundaries.
Keep useful structure unless the structure itself causes stiffness.
Remove obvious AI tells first, then fix rhythm and voice.
Improve precision before adding flair.
If the source is already strong, edit lightly.
Generate

Use when the user wants fresh prose from an idea, outline, notes, or a vague request.

Infer the implied audience and intent from the prompt.
Choose the narrowest effective format instead of over-explaining.
Write as if a competent person with a point of view sat down to say it.
Do not pad thin inputs with generic significance language.
When details are missing, stay concrete but avoid invented facts.
Style modes
Grounded

Use for business writing, internal updates, memos, documentation, proposals, factual summaries, and other trust-sensitive text.

Prefer direct claims, plain syntax, and calm confidence.
Use specific nouns and verbs over abstract framing.
Keep tone natural without sounding casual for no reason.
Let credibility come from clarity, not polish theater.
Voiced

Use for commentary, opinion, social posts, persuasive copy, essays, and prose that benefits from character.

Allow stronger rhythm shifts, sharper phrasing, and controlled opinion.
Add personality through perspective, not gimmicks.
Use texture sparingly: a quick aside, a clean turn, a pointed line.
Keep it human, not performatively quirky.
Quality bar

Before finalizing, check that the text:

says something concrete
sounds like it was written for someone, not for a benchmark
does not rely on vague authorities or inflated importance
does not march in identical sentence lengths
does not lean on unnatural em dashes to simulate voice
does not hide weak thinking behind smooth phrasing
matches the user's language and implied social context
Resources
Practical writing rules: references/human-writing-principles.md
AI-writing artifacts to remove: references/ai-writing-patterns.md
Rewrite/generate and grounded/voiced routing: references/mode-selection-and-language-rules.md
Suggested Prompt

Use $human-writing to write or rewrite human-facing text so it reads naturally, credibly, and like a person actually meant it.

Weekly Installs
9
Repository
timlai666/skills
First Seen
10 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
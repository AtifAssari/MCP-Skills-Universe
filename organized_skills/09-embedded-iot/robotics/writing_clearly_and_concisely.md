---
rating: ⭐⭐
title: writing-clearly-and-concisely
url: https://skills.sh/obra/the-elements-of-style/writing-clearly-and-concisely
---

# writing-clearly-and-concisely

skills/obra/the-elements-of-style/writing-clearly-and-concisely
writing-clearly-and-concisely
Originally fromsoftaworks/agent-toolkit
Installation
$ npx skills add https://github.com/obra/the-elements-of-style --skill writing-clearly-and-concisely
Summary

Apply Strunk's timeless writing rules to improve clarity and professionalism across all prose.

Covers 18 core rules spanning grammar, punctuation, composition principles, and common usage mistakes
Emphasizes active voice, positive framing, concrete language, and ruthless word elimination as key clarity drivers
Designed for documentation, commit messages, error messages, UI copy, reports, and any prose humans will read
Includes token-efficient subagent dispatch pattern: write a draft, then have a subagent copyedit using the full style guide when context is constrained
SKILL.md
Writing Clearly and Concisely
Overview

William Strunk Jr.'s The Elements of Style (1918) teaches you to write clearly and cut ruthlessly.

WARNING: elements-of-style.md consumes ~12,000 tokens. Read it only when writing or editing prose.

When to Use This Skill

Use this skill whenever you write prose for humans:

Documentation, README files, technical explanations
Commit messages, pull request descriptions
Error messages, UI copy, help text, comments
Reports, summaries, or any explanation
Editing to improve clarity

If you're writing sentences for a human to read, use this skill.

Limited Context Strategy

When context is tight:

Write your draft using judgment
Dispatch a subagent with your draft and elements-of-style.md
Have the subagent copyedit and return the revision
All Rules
Elementary Rules of Usage (Grammar/Punctuation)
Form possessive singular by adding 's
Use comma after each term in series except last
Enclose parenthetic expressions between commas
Comma before conjunction introducing co-ordinate clause
Don't join independent clauses by comma
Don't break sentences in two
Participial phrase at beginning refers to grammatical subject
Elementary Principles of Composition
One paragraph per topic
Begin paragraph with topic sentence
Use active voice
Put statements in positive form
Use definite, specific, concrete language
Omit needless words
Avoid succession of loose sentences
Express co-ordinate ideas in similar form
Keep related words together
Keep to one tense in summaries
Place emphatic words at end of sentence
Section V: Words and Expressions Commonly Misused

Alphabetical reference for usage questions

Bottom Line

Writing for humans? Read elements-of-style.md and apply the rules. Low on tokens? Dispatch a subagent to copyedit with the guide.

Weekly Installs
476
Repository
obra/the-elemen…of-style
GitHub Stars
360
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
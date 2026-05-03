---
title: writing-clearly-and-concisely
url: https://skills.sh/softaworks/agent-toolkit/writing-clearly-and-concisely
---

# writing-clearly-and-concisely

skills/softaworks/agent-toolkit/writing-clearly-and-concisely
writing-clearly-and-concisely
Installation
$ npx skills add https://github.com/softaworks/agent-toolkit --skill writing-clearly-and-concisely
Summary

Strunk's timeless rules for clearer, stronger prose in documentation, commit messages, and UI text.

Covers 18 core principles from The Elements of Style including active voice, positive form, concrete language, and ruthless concision
Includes reference files on grammar, composition, formatting, and common word misuse; most tasks need only the composition section (~4,500 tokens)
Identifies and helps avoid AI writing patterns: puffery, empty "-ing" phrases, promotional adjectives, and overused vocabulary like "leverage" and "multifaceted"
Supports a limited-context workflow: write a draft, dispatch a subagent with the relevant section file for copyediting, and receive a revision
SKILL.md
Writing Clearly and Concisely
Overview

Write with clarity and force. This skill covers what to do (Strunk) and what not to do (AI patterns).

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
Dispatch a subagent with your draft and the relevant section file
Have the subagent copyedit and return the revision

Loading a single section (~1,000-4,500 tokens) instead of everything saves significant context.

Elements of Style

William Strunk Jr.'s The Elements of Style (1918) teaches you to write clearly and cut ruthlessly.

Rules

Elementary Rules of Usage (Grammar/Punctuation):

Form possessive singular by adding 's
Use comma after each term in series except last
Enclose parenthetic expressions between commas
Comma before conjunction introducing co-ordinate clause
Don't join independent clauses by comma
Don't break sentences in two
Participial phrase at beginning refers to grammatical subject

Elementary Principles of Composition:

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
Reference Files

The rules above are summarized from Strunk's original text. For complete explanations with examples:

Section	File	~Tokens
Grammar, punctuation, comma rules	02-elementary-rules-of-usage.md	2,500
Paragraph structure, active voice, concision	03-elementary-principles-of-composition.md	4,500
Headings, quotations, formatting	04-a-few-matters-of-form.md	1,000
Word choice, common errors	05-words-and-expressions-commonly-misused.md	4,000

Most tasks need only 03-elementary-principles-of-composition.md — it covers active voice, positive form, concrete language, and omitting needless words.

AI Writing Patterns to Avoid

LLMs regress to statistical means, producing generic, puffy prose. Avoid:

Puffery: pivotal, crucial, vital, testament, enduring legacy
Empty "-ing" phrases: ensuring reliability, showcasing features, highlighting capabilities
Promotional adjectives: groundbreaking, seamless, robust, cutting-edge
Overused AI vocabulary: delve, leverage, multifaceted, foster, realm, tapestry
Formatting overuse: excessive bullets, emoji decorations, bold on every other word

Be specific, not grandiose. Say what it actually does.

For comprehensive research on why these patterns occur, see signs-of-ai-writing.md. Wikipedia editors developed this guide to detect AI-generated submissions — their patterns are well-documented and field-tested.

Bottom Line

Writing for humans? Load the relevant section from elements-of-style/ and apply the rules. For most tasks, 03-elementary-principles-of-composition.md covers what matters most.

Weekly Installs
3.7K
Repository
softaworks/agent-toolkit
GitHub Stars
1.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
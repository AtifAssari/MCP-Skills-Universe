---
title: croql
url: https://skills.sh/crowdin/skills/croql
---

# croql

skills/crowdin/skills/croql
croql
Installation
$ npx skills add https://github.com/crowdin/skills --skill croql
SKILL.md
CroQL Skill

Use this skill to turn natural-language filtering goals into valid Crowdin CroQL expressions.

Full documentation
Crowdin Query Language (CroQL) docs
What to produce

When helping with CroQL, return:

A primary CroQL expression.
A short explanation of why it matches the request.
One optional stricter or broader variant if the request is ambiguous.
Quick workflow
Identify the data context:
Source strings
Language translations
TM segments
Glossary terms
Map user intent to CroQL fields and operators.
Build the query in small clauses and combine with and/or.
Validate likely pitfalls (wrong context field, missing language scope, unencoded query).
Provide the final query and ready-to-run endpoint sample.
Core syntax cheatsheet
Comparison: =, !=, >, >=, <, <=, between ... and ..., contains
Logic: and, or, xor, not
Filtering collections: collection where (predicate)
Counting: count of translations, count of comments where (...)
Object member access: id of file, count of votes
Mentions:
User: @user:"username"
Language: @language:"uk"
Context-aware query patterns

Pick fields that belong to the correct context. A frequent failure mode is using fields from a different context.

1) Source strings context

Common fields:

text, identifier, context
is hidden, is duplicate
count of translations, count of comments, count of screenshots
count of languages summary where (...)
id of file, added, updated
Enterprise fields filters:
count of fields where (name = "Priority" and value = "High") > 0

Examples:

Hidden non-duplicates with translations:
is hidden and not is duplicate and count of translations > 0
Source contains ABC, but translations do not:
text contains "ABC" and count of translations where (text contains "ABC") = 0
At least one approval in any language:
count of languages summary where (approvalsCount >= 1) > 0
2) Translation context

Common fields:

text, plural form, is pre translated, provider, user, updated
Nested: count of votes where (is up), count of approvals where (...)

Example:

By specific user or highly upvoted:
user = @user:"crowdin" or count of votes where (is up) >= 100
3) TM segment context

Common structure is record-based:

count of records where (usageCount > 0) > 0
count of records where (createdBy = @user:"crowdin") > 0
4) Glossary term context

Common fields:

text, description, language, user, partOfSpeech, status, type, gender
note, lemma, url, createdAt, updatedAt

Examples:

Obsolete or not recommended:
status = "not_recommended" or status = "obsolete"
English lemma:
lemma = "cancel" and language = @language:"en"
Advanced editor-style filters

These are frequent requests from users trying to mirror UI filters in API calls:

Untranslated:
count of languages summary = 0
Translated:
count of languages summary where (is translated) > 0
Approved:
count of languages summary where (is approved) > 0
Has QA issues:
count of languages summary where (has qa issues) > 0
Duplicates only:
is duplicate

If target language matters, scope it explicitly:

count of languages summary where (language = @language:"uk" and is translated) > 0
Query construction strategy

When a user request is underspecified:

Start with the strictest interpretation.
Offer one broader fallback query.
State what assumption changed (language scope, approval threshold, date range, etc.).

Example:

Strict:
count of languages summary where (language = @language:"uk" and is translated and not is approved) > 0
Broader:
count of languages summary where (is translated and not is approved) > 0
Common mistakes to prevent
Mixing source-string fields with translation-only or glossary-only fields.
Forgetting language scoping when reproducing Editor filters in API.
Using raw (non-encoded) CroQL in request URLs.
Missing parentheses in nested where clauses.
Overusing or without grouping conditions.
Weekly Installs
8
Repository
crowdin/skills
GitHub Stars
3
First Seen
9 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
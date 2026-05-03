---
title: pr-comment-workflow
url: https://skills.sh/fcakyon/claude-codex-settings/pr-comment-workflow
---

# pr-comment-workflow

skills/fcakyon/claude-codex-settings/pr-comment-workflow
pr-comment-workflow
Installation
$ npx skills add https://github.com/fcakyon/claude-codex-settings --skill pr-comment-workflow
SKILL.md
PR Comment Workflow

Procedural knowledge for writing and responding to PR review comments.

Comment Style Rules
lowercase start for all sentences
never use em-dashes (—, –, --) between sentences, expressions, examples, or terms. Use commas, periods, or "or" instead
no complex sentences
simple terms, concise
no end-of-sentence punctuation if possible
max 1 sentence or shorter per comment
polite when responding to real people
bot comments: single concise sentence, no pleasantries ("good catch", "nice find", "thanks"), just state the fact directly
Review Comment Rules
Only create pending PR comments, never submit/confirm review automatically
Leave all comments for human review before posting
When creating review comments, follow the style rules above
Pending Review API Workflow

When posting review comments via gh api, use the two-step pending flow:

Create pending review: gh api repos/{owner}/{repo}/pulls/{number}/reviews -f event=PENDING -f body=""
Add comments to pending review: gh api repos/{owner}/{repo}/pulls/{number}/reviews/{review_id}/comments -f body="..." -f path="..." -F line=N -f side=RIGHT
Never call the submit endpoint, leave for human to review and submit
Output the review URL so user can review and submit manually
Reply Comment Posting

Reply comments (responses to existing threads) are posted directly, not as pending:

Use gh api repos/{owner}/{repo}/pulls/comments/{comment_id}/replies -f body="..."
Add a random 3-5 second delay between each reply: sleep $((RANDOM % 3 + 3))
Resolving Review Feedback
Fetch unresolved comments from PR
For each comment, decide if valid concern or not
If valid: fix the code AND search for same problem in other codebase locations, fix all occurrences
If not valid: draft a concise response
If automated bot comment: single concise sentence, no pleasantries, just state the fact
Present all draft responses to user before posting
Weekly Installs
13
Repository
fcakyon/claude-…settings
GitHub Stars
657
First Seen
Mar 11, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn
---
rating: ⭐⭐
title: respond-review
url: https://skills.sh/scando1993/sugar/respond-review
---

# respond-review

skills/scando1993/sugar/respond-review
respond-review
Installation
$ npx skills add https://github.com/scando1993/sugar --skill respond-review
SKILL.md
Responding to Code Review
Iron Law

EVERY REVIEW COMMENT DESERVES A RESPONSE

Steps
1. Read All Comments First

Before responding to anything, read every comment on the PR.

Understand the full scope of feedback before reacting
Look for patterns — multiple reviewers raising the same concern is a strong signal
Note the severity: is this a blocker, a suggestion, or a style preference?
Do not start fixing anything until you have read everything
2. Categorize

Sort every comment into one of four categories:

Category	Description	Action
Must-fix	Bugs, security issues, correctness problems, failing tests	Fix immediately, no discussion needed
Should-fix	Design improvements, better patterns, readability gains	Fix unless you have a strong reason not to, then explain
Discussion	Architectural questions, alternative approaches, trade-offs	Respond with your reasoning, be open to changing your mind
Nit	Style preferences, minor naming suggestions, formatting	Fix if easy, acknowledge if not, never argue
3. Address Must-Fix Items

Fix all must-fix items first.

These are non-negotiable — do not push back on correctness issues
Commit each fix with a clear message referencing the review comment
If a must-fix requires a significant change, explain what you changed and why
Re-run quality checks after fixes
4. Respond to Each Comment

Leave a response on every single comment.

Must-fix: "Fixed in [commit hash]" or "Fixed — [brief explanation of the change]"
Should-fix: "Good catch, fixed" or "I considered this but chose X because [reason] — open to changing if you still disagree"
Discussion: Share your reasoning clearly. Ask clarifying questions if the comment is ambiguous. Be willing to be wrong.
Nit: "Fixed" or "Acknowledged — keeping as-is because [reason]"

Never leave a comment without a response. Silence reads as dismissal.

5. Re-Request Review

After addressing all comments:

Push the updated branch
Leave a summary comment listing what was addressed
Re-request review from the original reviewers
If significant changes were made, highlight them explicitly
Red Flags — If You Catch Yourself Thinking:
Thought	Reality
"The reviewer doesn't understand my code"	If the reviewer doesn't understand it, the code isn't clear enough. Improve it.
"This nit isn't worth fixing"	Nits take 30 seconds to fix and build goodwill. Just fix it.
"I'll address these comments in a follow-up PR"	Address them now. Follow-up PRs for review feedback rarely happen.
"The reviewer is wrong about this"	Assume good intent. Explain your reasoning, but be genuinely open to being wrong.
Rules
Respond to every comment — no exceptions
Assume good intent from reviewers
Fix before defending — if the fix is easy, just do it regardless of whether you agree
Never dismiss feedback without explanation
Re-run all quality checks after incorporating changes
Push fixes as new commits (not amended) so reviewers can see what changed
Weekly Installs
12
Repository
scando1993/sugar
First Seen
11 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
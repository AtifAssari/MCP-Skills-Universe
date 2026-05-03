---
title: stories
url: https://skills.sh/kazdenc/builder-skills/stories
---

# stories

skills/kazdenc/builder-skills/stories
stories
Installation
$ npx skills add https://github.com/kazdenc/builder-skills --skill stories
SKILL.md
Job Stories & User Stories

Translate requirements into stories that a team can pick up and build. Prefer job stories over user stories — situations are more actionable than personas.

Why Job Stories Over User Stories

User stories anchor on a persona: "As a project manager..." But the same person behaves differently depending on context. A project manager at 9am triaging is doing a different job than at 3pm reporting to stakeholders.

Job stories anchor on the situation, which is what actually drives behavior.

Format	Example	Strength
Job story: When [situation], I want to [motivation], so I can [outcome]	When I'm reviewing pull requests before standup, I want to see which ones block other work, so I can prioritize reviews that unblock the team	Captures context that shapes the solution
User story: As a [role], I want to [action], so that [benefit]	As a tech lead, I want to see PR priorities, so that I can review efficiently	Vague on when/why this matters

Use user stories if the team is already fluent in them. Don't fight process for its own sake. But write the situation into the description either way.

Writing Good Stories

A good story is independent, negotiable, valuable, estimable, small, and testable (INVEST).

Good	Bad	Why it's bad
When I'm halfway through a form and get interrupted, I want my progress saved, so I can resume without re-entering data	The system should auto-save forms	No situation, no outcome, not testable
When I receive a notification about a price drop, I want to see the item and the new price inline, so I can decide to buy without opening the app	As a user, I want push notifications	Too vague, no context, no clear done state
When I'm comparing two plans side by side, I want differences highlighted, so I can spot what matters without reading every line	Build a comparison table with highlighting	That's a solution, not a story
Breaking Large Stories Down

If a story takes more than 3 days to build, it's too big. Split by:

Workflow step — "When I start..." vs "When I'm halfway through..." vs "When I finish..."
Data variation — Handle the common case first, edge cases as separate stories
Platform — Mobile vs desktop if the experience genuinely differs
User maturity — First-time vs returning vs power user

Don't split by technical layer (frontend/backend/database). Stories should deliver visible user value.

Writing Acceptance Criteria

Every story needs acceptance criteria in Given/When/Then format. These are the contract between product and engineering.

Story: When I'm reviewing PRs before standup, I want to see which ones
       block other work, so I can prioritize unblocking reviews.

Acceptance Criteria:

  Given I have PRs assigned to me for review
  When I open the review queue
  Then PRs that block other PRs or deployments appear at the top

  Given a PR has been waiting for review for more than 24 hours
  When I view my review queue
  Then it is flagged with a time-waiting indicator

  Given no PRs are assigned to me
  When I open the review queue
  Then I see an empty state with a message (not a blank screen)


Rules for acceptance criteria:

One behavior per Given/When/Then block. Don't chain multiple outcomes.
Include the sad path. What happens when there's no data, an error, or unexpected input?
Stay observable. "The system processes it quickly" is not observable. "The results appear within 2 seconds" is.
Skip implementation. "The API returns a 200" is an engineering test, not acceptance criteria.
Sizing Guidance
Size	Signal	Action
< 1 day	Might be a task, not a story	Combine with related work or keep as-is if it delivers standalone value
1-3 days	Right-sized	Ship it
3-5 days	Borderline	Look for a natural split point
> 5 days	Too big	Split by workflow step or data variation

Sizing is for the whole slice — design, build, test. Not just coding time.

Output Format

Deliver stories as a numbered list. Group them by workflow stage or theme. Each story gets:

Story statement (job story format)
Acceptance criteria (Given/When/Then)
Size estimate (S/M/L or day count)
Dependencies (other stories that must ship first, if any)
Weekly Installs
10
Repository
kazdenc/builder-skills
GitHub Stars
35
First Seen
Mar 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
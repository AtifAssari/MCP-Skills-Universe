---
title: feature-prioritization
url: https://skills.sh/assimovt/productskills/feature-prioritization
---

# feature-prioritization

skills/assimovt/productskills/feature-prioritization
feature-prioritization
Installation
$ npx skills add https://github.com/assimovt/productskills --skill feature-prioritization
SKILL.md

Prioritize with math, not opinions. RICE scoring forces explicit tradeoffs. The enabler/blocker lens from Linear ensures you're not just building fun things while adoption barriers remain.

RICE Scoring

Score every candidate feature on four dimensions:

Reach: How many users/accounts will this affect in a set time period? Use real numbers from analytics, not gut feel. "500 users/quarter" not "a lot."
Impact: How much will this move the target metric per user? Score 0.25 (minimal), 0.5 (low), 1 (medium), 2 (high), 3 (massive). Be honest — most features are a 1.
Confidence: How sure are you about Reach and Impact? 100% = hard data. 80% = strong evidence. 50% = gut feel. NEVER score 100% without quantitative data.
Effort: Person-weeks of work. Include design, engineering, QA, and any cross-team coordination. Round up.

RICE = (Reach x Impact x Confidence) / Effort

Example: SSO — Reach: 500 users/qtr, Impact: 2 (high — unlocks enterprise deals), Confidence: 80%, Effort: 4 person-weeks. RICE = (500 x 2 x 0.8) / 4 = 200. Tag: Blocker.

Rank by score. The math won't be perfect, but it forces you to justify each dimension.

Enablers vs Blockers (Linear)

After RICE scoring, classify each feature:

Blocker: Removes a barrier to adoption or retention. Users are churning, stuck, or can't even start because this is missing. Examples: missing SSO for enterprise deals, broken mobile experience, no data export.
Enabler: Delights existing users or deepens engagement. Users are already successful but this makes them more so. Examples: keyboard shortcuts, advanced filters, integrations.

Rule: Prioritize blockers over enablers when growing. Removing friction > adding delight when you're trying to grow. Flip this when retention is strong but engagement is flat.

Running a Prioritization Session
List all candidates with a one-sentence description
Score each on R, I, C, E independently — don't anchor on each other
Calculate RICE scores and rank
Tag each as Blocker or Enabler
Check: are any Blockers ranked below Enablers? Justify or re-rank.
Top 3-5 items = your next cycle
Guidelines
ALWAYS show the math. A prioritization without visible scores is just an opinion list.
NEVER let Confidence = 100% without hard data (analytics, A/B test results, or customer commit).
ALWAYS separate enablers from blockers before finalizing the rank.
NEVER prioritize more than one cycle at a time. The world changes. Re-score next cycle.
CRITICAL: If two items are within 20% RICE score of each other, they're effectively tied. Use the blocker/enabler lens to break ties, or pick the one with higher Confidence.

Built on Intercom's RICE framework and the Linear Method. Skills from productskills.

Weekly Installs
28
Repository
assimovt/productskills
GitHub Stars
34
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
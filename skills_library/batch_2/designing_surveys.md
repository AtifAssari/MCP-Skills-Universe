---
title: designing-surveys
url: https://skills.sh/refoundai/lenny-skills/designing-surveys
---

# designing-surveys

skills/refoundai/lenny-skills/designing-surveys
designing-surveys
Installation
$ npx skills add https://github.com/refoundai/lenny-skills --skill designing-surveys
Summary

Survey design framework grounded in product research best practices from nine leaders.

Prioritize CSAT over NPS for better statistical properties and business outcome correlation; use 5-7 item scales
Design single-variable questions only; avoid double-barreled phrasing that conflates multiple concepts
Target customers 3-6 months post-signup when memory of the "before" state is fresh and relevant
Use MaxDiff (Most/Least) methodology for feature prioritization rather than unlimited rating scales
Force respondents to prioritize by limiting selections (e.g., "pick your top three") and measure frequency to weight impact
SKILL.md
Designing Surveys

Help the user design effective surveys using frameworks from 9 product leaders who have built rigorous research and feedback systems.

How to Help

When the user asks for help with surveys:

Clarify the goal - Determine if they're measuring satisfaction, identifying problems, or prioritizing features
Choose the right metric - Help them select between NPS, CSAT, PMF survey, or custom approaches
Design clean questions - Ensure each question measures one thing precisely
Target the right respondents - Help them reach users with fresh, relevant experience
Core Principles
NPS is scientifically flawed

Judd Antin: "NPS is the best example of the marketing industry marketing itself. The consensus in the survey science community is that NPS makes all the mistakes. Customer satisfaction, a simple CSAT metric, is better. It has better data properties, it is more precise, it is more correlated to business outcomes." Use CSAT with 5-7 item scales instead.

Force prioritization with constraints

Nicole Forsgren: "Let them pick three, just three. Of those three, how often does this affect you? Is this hourly? Is this daily? Is this weekly?" Limit respondents to their top barriers to keep data clean, then measure frequency to weight impact.

Survey your best customers at the right time

Gia Laudi: "Very importantly, they signed up for your product recently enough that they remember what life was like before. Generally, we say that's in the three to six-month range." Target customers who have been using the product 3-6 months so their memory of the 'before' state is fresh.

Onboarding surveys improve conversion

Laura Schaffer: "We just asked for forgiveness and put these questions into the signup flow. An improved conversion by like 5%, just improved signups." Adding 'good friction' in the form of targeted questions can increase conversion by reassuring users they're in the right place.

Avoid double-barreled questions

Nicole Forsgren: "You're asking four different questions there. If someone answers yes, was it the build? Was it the test? Was it slow or was it flaky?" Ensure each survey question only asks about one specific variable.

Use MaxDiff for feature prioritization

Madhavan Ramanujam: "Identify the most important for you, and the least important. If you do this a few times, you will be able to prioritize the entire feature set in a relative fashion." MaxDiff (Most/Least) surveys are superior to simple ranking for identifying value drivers.

Questions to Help Users
"What specific decision will this survey inform?"
"Are you asking about one thing per question, or multiple things?"
"Who are your 'best' customers and when did they sign up?"
"Are all scale options visible on mobile without scrolling?"
"How will you force respondents to prioritize rather than rate everything high?"
Common Mistakes to Flag
Double-barreled questions - Asking about speed AND complexity in one question
Too many options - Allowing respondents to select unlimited items instead of forcing prioritization
Wrong timing - Surveying customers who are too new (no experience) or too old (forgot the 'before')
NPS worship - Relying on a metric with known scientific flaws over simpler, better alternatives
Hidden scale options - Mobile surveys where users can't see all options create response bias
Deep Dive

For all 10 insights from 9 guests, see references/guest-insights.md

Related Skills
Writing North Star Metrics
Defining Product Vision
Prioritizing Roadmap
Setting OKRs & Goals
Weekly Installs
1.1K
Repository
refoundai/lenny-skills
GitHub Stars
744
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
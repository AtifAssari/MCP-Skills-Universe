---
rating: ⭐⭐
title: job-stories
url: https://skills.sh/phuryn/pm-skills/job-stories
---

# job-stories

skills/phuryn/pm-skills/job-stories
job-stories
Installation
$ npx skills add https://github.com/phuryn/pm-skills --skill job-stories
SKILL.md
Job Stories

Create job stories using the 'When [situation], I want to [motivation], so I can [outcome]' format. Generates stories with detailed acceptance criteria focused on user situations and outcomes.

Use when: Writing job stories, expressing user situations and motivations, creating JTBD-style backlog items, or focusing on user context rather than roles.

Arguments:

$PRODUCT: The product or system name
$FEATURE: The new feature to break into job stories
$DESIGN: Link to design files (Figma, Miro, etc.)
$CONTEXT: User situations or job scenarios
Step-by-Step Process
Identify user situations that trigger the need
Define motivations underlying the user's behavior
Clarify outcomes the user wants to achieve
Apply JTBD framework: Focus on the job, not the role
Create acceptance criteria that validate the outcome is achieved
Use observable, measurable language
Link to design mockups or prototypes
Output job stories with detailed acceptance criteria
Story Template

Title: [Job outcome or result]

Description: When [situation], I want to [motivation], so I can [outcome].

Design: [Link to design files]

Acceptance Criteria:

[Situation is properly recognized]
[System enables the desired motivation]
[Progress or feedback is visible]
[Outcome is achieved efficiently]
[Edge cases are handled gracefully]
[Integration and notifications work]
Example Job Story

Title: Track Weekly Snack Spending

Description: When I'm preparing my weekly allowance for snacks (situation), I want to quickly see how much I've spent so far (motivation), so I can make sure I don't run out of money before the weekend (outcome).

Design: [Figma link]

Acceptance Criteria:

Display Spending Summary with 'Weekly Spending Overview' section
Real-Time Update when expense logged
Progress Indicator (progress bar showing 0-100% of weekly budget)
Remaining Budget Highlight in prominent color
Detailed Spending Log with breakdown by category
Notifications at 80% budget threshold
Weekend-Specific Reminder at 90% by Thursday evening
Easy Access and Navigation to detailed breakdown
Output Deliverables
Complete set of job stories for the feature
Each story follows the 'When...I want...so I can' format
6-8 acceptance criteria focused on outcomes
Stories emphasize user situations and motivations
Clear links to design and prototypes
Further Reading
Jobs-to-be-Done Masterclass with Tony Ulwick and Sabeen Sattar (video course)
Weekly Installs
554
Repository
phuryn/pm-skills
GitHub Stars
10.8K
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass
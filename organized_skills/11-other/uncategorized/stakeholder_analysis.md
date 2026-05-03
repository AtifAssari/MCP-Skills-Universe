---
rating: ⭐⭐
title: stakeholder analysis
url: https://skills.sh/danhvb/my-ba-skills/stakeholder-analysis
---

# stakeholder analysis

skills/danhvb/my-ba-skills/Stakeholder Analysis
Stakeholder Analysis
Installation
$ npx skills add https://github.com/danhvb/my-ba-skills --skill 'Stakeholder Analysis'
SKILL.md
Stakeholder Analysis Skill
Purpose

Identify and analyze project stakeholders to ensure proper engagement, communication, and management throughout the project lifecycle.

When to Use
Project initiation and planning
Requirements gathering preparation
Change management planning
Communication strategy development
Risk assessment (stakeholder-related risks)
Stakeholder Identification
Sources of Stakeholders
Project sponsors and executives
Business owners and department heads
End users (internal and external)
IT and development teams
External vendors and partners
Regulatory bodies
Customers and clients
Identification Techniques
Organizational chart review: Identify departments affected
Brainstorming with team: Who's impacted? Who has influence?
Document review: Previous projects, contracts
Interviews: Ask "Who else should I talk to?"
Process analysis: Who performs each step?
Power/Interest Grid
Matrix
High Power │ Keep Satisfied │ Manage Closely │
           │    (Latents)   │  (Key Players) │
           ├────────────────┼────────────────┤
Low Power  │    Monitor     │ Keep Informed  │
           │   (Apathetics) │  (Defenders)   │
           └────────────────┴────────────────┘
             Low Interest    High Interest

Quadrant Strategies

Manage Closely (High Power, High Interest):

Regular 1:1 meetings
Involve in key decisions
Provide detailed updates
Seek their input and approval
Examples: Project Sponsor, Business Owner, CTO

Keep Satisfied (High Power, Low Interest):

Periodic high-level updates
Executive summaries
Involve for major decisions only
Don't overwhelm with details
Examples: CFO, CEO, Board members

Keep Informed (Low Power, High Interest):

Regular updates (email, newsletter)
Involve in UAT and feedback
Listen to their concerns
Great sources of detailed requirements
Examples: End users, Team leads

Monitor (Low Power, Low Interest):

Minimal effort
General communications only
Keep aware of changes in interest/power
Examples: External vendors not directly involved
RACI Matrix
Definition
R - Responsible: Does the work
A - Accountable: Approves/signs off (only ONE per task)
C - Consulted: Provides input (two-way communication)
I - Informed: Kept in the loop (one-way communication)
Template
Activity	PM	BA	Dev Lead	Business Owner	End Users
Requirements Gathering	A	R	C	C	C
BRD Approval	I	R	I	A	I
Technical Design	I	C	R/A	I	I
Development	I	I	A	I	I
UAT Planning	C	R	C	A	C
UAT Execution	I	C	I	C	R
Go-live Approval	C	I	C	A	I
Rules
Every task has exactly ONE Accountable
At least ONE Responsible per task
Don't overload with C's (meeting fatigue)
Validate with stakeholders
Stakeholder Register
Template
ID	Name	Role	Department	Power	Interest	Engagement	Comm Preference	Notes
SH-001	John Smith	VP Sales	Sales	High	High	Champion	Email, Weekly 1:1	Key sponsor
SH-002	Sarah Lee	Support Manager	CS	Medium	High	Supportive	Slack, Sprint demos	Good UAT lead
SH-003	Mike Chen	CFO	Finance	High	Low	Neutral	Monthly exec summary	Budget approval
SH-004	Lisa Wong	End User	Operations	Low	High	Supporter	Team meetings	Subject matter expert
SH-005	Tom Brown	IT Director	IT	High	Medium	Resistant	1:1 meetings	Security concerns
Engagement Levels
Champion: Actively promotes project
Supportive: Positive, helpful when asked
Neutral: Neither supports nor opposes
Resistant: Skeptical, may oppose
Hostile: Actively working against project
Engagement Strategies

Champion → Champion: Leverage their support, involve in communications Supportive → Champion: Recognize contributions, give ownership Neutral → Supportive: Communicate benefits, address concerns Resistant → Neutral: Understand concerns, involve in decisions Hostile → Resistant: Meet 1:1, find common ground, escalate if needed

Communication Plan
Template
Stakeholder Group	Information Needs	Frequency	Channel	Owner
Executive Team	Project status, risks, decisions	Monthly	Email report, Meeting	PM
Business Owners	Detailed progress, blockers	Weekly	Status meeting	PM
Development Team	Requirements, priorities	Daily	Standup, Slack	BA
End Users	Training, timeline, changes	As needed	Email, Teams	BA
Communication Channels
Formal: Email, presentations, reports
Informal: Slack/Teams, quick calls
Meetings: 1:1s, team meetings, workshops
Documentation: Confluence, Notion, SharePoint
Stakeholder Engagement Tips
Building Relationships
Understand their goals and challenges
Speak their language (technical vs business)
Be responsive and reliable
Deliver on commitments
Acknowledge their contributions
Managing Resistance
Listen to understand (not to respond)
Ask probing questions
Find the root cause of resistance
Address concerns directly
Find win-win solutions
Escalate when necessary
Managing Expectations
Be clear about scope and timeline
Communicate risks early
Under-promise, over-deliver
Document decisions and agreements
Regular status updates
Domain-Specific Stakeholders
E-commerce
Product Managers, Merchandising
Marketing (promotions, campaigns)
Customer Service
Fulfillment/Warehouse
Payment/Finance
IT/Security
ERP
Finance (CFO, Controller, Accountants)
HR (CHRO, Payroll)
Supply Chain (Procurement, Logistics)
Manufacturing (Plant managers)
IT (CIO, Enterprise Architects)
Compliance/Audit
CRM
Sales (VP Sales, Sales Managers, Reps)
Marketing (CMO, Marketing Ops)
Customer Service (Support Managers)
IT (CRM Admin)
Executive (CEO, Revenue leaders)
CDP
Marketing (CMO, Campaign Managers)
Data/Analytics (Chief Data Officer)
IT/Engineering (Data Engineers)
Privacy/Legal (DPO, Counsel)
Customer Experience
Best Practices

✅ Do:

Update stakeholder analysis regularly
Adapt communication style to stakeholder
Document stakeholder interactions
Celebrate stakeholder contributions
Be proactive with difficult stakeholders

❌ Don't:

Assume stakeholder needs
Ignore "difficult" stakeholders
Over-communicate to everyone
Forget to close the feedback loop
Surprise stakeholders with bad news
Tools
Lark/Notion: Stakeholder register database
Figma/Miro: Power/Interest grid visualization
Lark Meetings: Meeting notes and action items
Email/Slack: Regular communications
Next Steps

After stakeholder analysis:

Create communication plan
Plan requirements elicitation schedule
Identify change management needs
Prepare for requirement workshops
References
PMBOK Guide - Stakeholder Management
BABOK Guide - Stakeholder Analysis
Influence Without Authority (Cohen & Bradford)
Weekly Installs
–
Repository
danhvb/my-ba-skills
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass